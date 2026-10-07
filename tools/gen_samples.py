"""Generate sample Kritzel projects (document.json + gallery.json) for manual screenshots.

Usage: gen_samples.py <out_dir>/kritzel_projects <now-iso-timestamp>
"""
import json, math, os, random, sys, uuid
from datetime import datetime, timedelta

random.seed(7)
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
NOW = datetime.fromisoformat(sys.argv[2])

def uid():
    return str(uuid.uuid4())

def argb(hexstr, a=255):
    h = hexstr.lstrip('#')
    return (a << 24) | int(h, 16)

PRESETS = {
    'variable': dict(presetId='builtin-pen-variable', smoothing=0.5, streamline=0.5, thinning=0.5),
    'fixed': dict(presetId='builtin-pen-fixed', smoothing=0.5, streamline=0.5, thinning=0.0),
    'fountain': dict(presetId='builtin-pen-fountain', smoothing=0.7, streamline=0.6, thinning=0.7,
                     taperStart=True, taperStartLength=20.0, taperEnd=True, taperEndLength=20.0,
                     capStart=False, capEnd=False),
    'ballpoint': dict(presetId='builtin-pen-ballpoint', smoothing=0.4, streamline=0.4, thinning=0.3),
    'soft': dict(presetId='builtin-pencil-soft', smoothing=0.6, streamline=0.3, thinning=0.4,
                 taperStart=True, taperStartLength=10.0, taperEnd=True, taperEndLength=15.0,
                 capStart=False, capEnd=False, brushTexture='pencilGrain'),
    'highlighter': dict(presetId='builtin-marker-highlighter', smoothing=0.5, streamline=0.6, thinning=0.0),
    'broad': dict(presetId='builtin-marker-broad', smoothing=0.5, streamline=0.5, thinning=0.0),
}

def base_stroke(color, width, opacity=1.0, preset='variable'):
    s = dict(id=uid(), points=[], color=color, width=width, opacity=opacity,
             smoothing=0.5, streamline=0.5, thinning=0.5, simulatePressure=False,
             presetId=None, taperStart=False, taperStartLength=0.0, taperEnd=False,
             taperEndLength=0.0, capStart=True, capEnd=True,
             pressureCurveX1=0.25, pressureCurveY1=0.25, pressureCurveX2=0.75, pressureCurveY2=0.75,
             textureSeed=random.random())
    s.update(PRESETS[preset])
    return s

def resample(pts, step=3.0):
    out = [pts[0]]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        d = math.hypot(x1 - x0, y1 - y0)
        n = max(1, int(d / step))
        for i in range(1, n + 1):
            t = i / n
            out.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    return out

def freehand(pts, color, width, preset='variable', opacity=1.0, jitter=0.6, step=3.0, pmin=0.35, pmax=0.85):
    s = base_stroke(color, width, opacity, preset)
    rs = resample(pts, step)
    n = len(rs)
    t0 = random.randint(1000, 900000)
    for i, (x, y) in enumerate(rs):
        u = i / max(1, n - 1)
        p = pmin + (pmax - pmin) * math.sin(math.pi * u) ** 0.6
        p += random.uniform(-0.04, 0.04)
        s['points'].append(dict(x=round(x + random.uniform(-jitter, jitter), 2),
                                y=round(y + random.uniform(-jitter, jitter), 2),
                                pressure=round(max(0.05, min(1.0, p)), 3), timestamp=t0 + i * 8))
    return s

def curve(fn, t0, t1, n):
    return [fn(t0 + (t1 - t0) * i / n) for i in range(n + 1)]

def shape(kind, x0, y0, x1, y1, color, width=3.0, filled=False, sides=5, radius=0.0, opacity=1.0, vertices=None, closed=False):
    s = base_stroke(color, width, opacity, 'fixed')
    s['presetId'] = None
    sd = dict(type=kind, startX=x0, startY=y0, endX=x1, endY=y1, filled=filled, polygonSides=sides,
              freeformClosed=closed)
    if vertices:
        sd['vertices'] = [[vx, vy] for vx, vy in vertices]
    if radius:
        sd['cornerRadius'] = radius
    s['shapeData'] = sd
    pts = []
    if kind == 'line':
        pts = [(x0, y0), (x1, y1)]
    elif kind == 'rectangle':
        if radius:
            r = min(radius, abs(x1 - x0) / 2, abs(y1 - y0) / 2)
            L, T, R, B = min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)
            seg = max(4, min(24, math.ceil(r / 2)))
            def arc(cx, cy, a0, a1):
                for i in range(seg + 1):
                    a = math.radians(a0 + (a1 - a0) * i / seg)
                    pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
            arc(L + r, T + r, 180, 270); arc(R - r, T + r, 270, 360)
            arc(R - r, B - r, 0, 90); arc(L + r, B - r, 90, 180)
            pts.append(pts[0])
        else:
            pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
    elif kind in ('ellipse', 'polygon'):
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        rx, ry = abs(x1 - x0) / 2, abs(y1 - y0) / 2
        if kind == 'ellipse':
            pts = [(cx + rx * math.cos(2 * math.pi * i / 64), cy + ry * math.sin(2 * math.pi * i / 64)) for i in range(65)]
        else:
            pts = [(cx + rx * math.cos(2 * math.pi * i / sides - math.pi / 2),
                    cy + ry * math.sin(2 * math.pi * i / sides - math.pi / 2)) for i in range(sides + 1)]
    elif kind == 'freeform':
        pts = list(vertices) + ([vertices[0]] if closed else [])
    s['points'] = [dict(x=round(x, 3), y=round(y, 3), pressure=0.5, timestamp=i) for i, (x, y) in enumerate(pts)]
    return s

def text(txt, x, y, color, family='Roboto', size=24.0, weight=400, italic=False, align=0, opacity=1.0):
    s = base_stroke(color, 2.0, opacity, 'fixed')
    s['presetId'] = None
    s['points'] = [dict(x=x, y=y, pressure=0.5, timestamp=0)]
    s['textData'] = dict(text=txt, fontFamily=family, fontSize=size, fontWeight=weight,
                         fontStyle=1 if italic else 0, textAlign=align)
    return s

def layer(name, strokes, opacity=1.0):
    return dict(id=uid(), name=name, strokes=strokes, isVisible=True, isLocked=False, opacity=opacity)

def grid(kind='none', spacing=20.0, opacity=0.15, color=0xFFFFFFFF):
    return dict(type=kind, spacing=spacing, subdivisions=4, color=color, opacity=opacity,
                snapMode='off', snapSensitivity=8.0, showMeasurements=False, inBackground=False)

projects, folders = [], []

def project(name, layers, bg, gridcfg=None, age=timedelta(0), created_age=timedelta(days=3), folder=None):
    pid = uid()
    doc = {
        'formatVersion': 13, 'id': pid, 'name': name, 'layers': layers,
        'activeLayerId': layers[-1]['id'],
        'gridConfig': gridcfg or grid(),
        'canvasBackground': dict(color=bg, isTransparent=False),
        'guideConfig': dict(guides=[], guidesEnabled=False, snapToGuides=False),
        'createdAt': (NOW - created_age).isoformat(), 'modifiedAt': (NOW - age).isoformat(),
    }
    os.makedirs(os.path.join(OUT, pid), exist_ok=True)
    with open(os.path.join(OUT, pid, 'document.json'), 'w') as f:
        json.dump(doc, f)
    projects.append(dict(id=pid, name=name, createdAt=doc['createdAt'], modifiedAt=doc['modifiedAt'], folderId=folder))
    return pid

def folder(name, parent=None):
    fid = uid()
    folders.append(dict(id=fid, name=name, createdAt=(NOW - timedelta(days=10)).isoformat(), **({'parentId': parent} if parent else {})))
    return fid

OFFWHITE = 4294309360
WHITE = 0xFFFFFFFF
DARK = 4279900698
BLUEPRINT = 4278926737

# ---------------------------------------------------------------- mountain lake
navy, steel, pine, sun, water = argb('2B3A55'), argb('5B7DB1'), argb('2F6B4F'), argb('F2A541'), argb('3D7EA6')
sky = [shape('ellipse', 880, 130, 990, 240, sun, filled=True, opacity=0.9)]
for cx, cy, w in [(300, 170, 150), (620, 140, 110)]:
    pts = curve(lambda t: (cx + w * t, cy - 18 * math.sin(math.pi * t * 2) * (1 if t < .5 else .6)), 0, 1, 40)
    sky.append(freehand(pts, argb('8FA3BF'), 4, 'fountain'))
ridge1 = [(140, 470), (240, 360), (300, 400), (410, 250), (470, 320), (540, 280), (650, 420), (720, 380), (800, 450)]
ridge2 = [(560, 470), (680, 330), (740, 370), (850, 230), (930, 330), (1000, 300), (1150, 470)]
mountains = [freehand(ridge1, navy, 6, 'fountain', jitter=1.2), freehand(ridge2, steel, 6, 'fountain', jitter=1.2)]
for peak in [(410, 250), (850, 230)]:
    px, py = peak
    mountains.append(freehand([(px - 30, py + 40), (px - 12, py + 30), (px, py + 44), (px + 14, py + 30), (px + 34, py + 42)], navy, 3, 'ballpoint'))
for i in range(14):
    x = 200 + i * 55 + random.uniform(-10, 10)
    mountains.append(freehand([(x, 400 + random.uniform(0, 40)), (x + 25, 380 + random.uniform(0, 40))], steel, 2, 'soft', opacity=0.7))
lake = [freehand([(120, 480), (1180, 480)], navy, 4, 'ballpoint', jitter=0.8)]
for i in range(9):
    y = 510 + i * 26
    x0 = 160 + random.uniform(0, 260)
    lake.append(freehand([(x0, y), (x0 + random.uniform(160, 420), y + random.uniform(-2, 2))], water, 3, 'fountain', opacity=0.8))
for tx in [170, 215, 1060, 1110, 1150]:
    base = 470
    h = random.uniform(90, 130)
    zz = [(tx, base - h)]
    for k in range(1, 5):
        yy = base - h + k * h / 5
        zz += [(tx - 8 - k * 6, yy), (tx + 8 + k * 6, yy + 4)]
    lake.append(freehand(zz, pine, 4, 'variable', jitter=0.5))
    lake.append(freehand([(tx, base - 10), (tx, base + 4)], navy, 4, 'fixed'))
for bx, by in [(520, 200), (565, 185), (600, 215)]:
    lake.append(freehand(curve(lambda t: (bx + 30 * t, by + 10 * math.sin(math.pi * t * 2) ** 2 * (1 if t < .5 else 1) - 8 * abs(math.sin(math.pi * t))), 0, 1, 20), navy, 2.5, 'fountain'))
lake.append(text('Alpsee, Oktober', 900, 720, navy, 'Caveat', 40))
project('mountain_lake', [layer('Sky', sky), layer('Mountains', mountains), layer('Lake', lake)], OFFWHITE, age=timedelta(minutes=4))

# ---------------------------------------------------------------- logo ideas
purple, coral, teal, ink = argb('7C5CFF'), argb('FF6B6B'), argb('2EC4B6'), argb('1E1E2E')
logo = [
    shape('rectangle', 160, 150, 400, 390, purple, 4, filled=True, radius=48),
    text('K', 225, 155, WHITE, 'Pacifico', 150),
    shape('polygon', 470, 150, 710, 390, coral, 6, sides=6),
    shape('ellipse', 530, 210, 650, 330, coral, 4, filled=True, opacity=0.85),
    shape('polygon', 790, 160, 1030, 380, teal, 5, filled=True, sides=3),
    shape('ellipse', 870, 260, 950, 340, WHITE, 3, filled=True),
    text('Kritzel', 160, 450, ink, 'Pacifico', 84),
    text('STUDIO', 520, 495, ink, 'Montserrat', 52, weight=700),
]
for i, c in enumerate(['7C5CFF', 'FF6B6B', '2EC4B6', 'FFD166', '1E1E2E']):
    logo.append(shape('rectangle', 160 + i * 90, 640, 230 + i * 90, 710, argb(c), 2, filled=True, radius=14))
logo.append(freehand(curve(lambda t: (820 + 260 * t, 610 + 40 * math.sin(t * 5)), 0, 1, 60), coral, 5, 'fountain'))
logo.append(text('v2 — rounder?', 830, 650, ink, 'Caveat', 36))
project('logo_ideas', [layer('Shapes', logo)], WHITE, age=timedelta(minutes=12))

# ---------------------------------------------------------------- floor plan
W = WHITE
plan = [
    shape('rectangle', 200, 140, 1000, 700, W, 6),
    shape('line', 600, 140, 600, 460, W, 4),
    shape('line', 200, 460, 760, 460, W, 4),
    shape('line', 760, 460, 760, 700, W, 4),
    shape('line', 600, 320, 1000, 320, W, 4),
    shape('rectangle', 230, 170, 330, 230, W, 2, opacity=0.8),
    shape('rectangle', 640, 360, 740, 430, W, 2, opacity=0.8, radius=12),
    shape('ellipse', 860, 520, 960, 660, W, 2, opacity=0.8),
]
for (cx, cy, a0) in [(600, 400, 180), (760, 540, 270)]:
    plan.append(shape('freeform', 0, 0, 0, 0, W, 2,
                      vertices=[(cx + 50 * math.cos(math.radians(a0 + d)), cy + 50 * math.sin(math.radians(a0 + d))) for d in range(0, 91, 10)]))
for label, x, y in [('Living', 330, 300), ('Kitchen', 730, 220), ('Bedroom', 820, 380), ('Bath', 400, 560), ('Hall', 830, 580)]:
    plan.append(text(label, x, y, W, 'Source Code Pro', 26))
plan.append(text('8.00 m', 560, 100, W, 'Source Code Pro', 22))
plan.append(shape('line', 200, 120, 1000, 120, W, 2, opacity=0.7))
project('floor_plan', [layer('Walls', plan)], BLUEPRINT, grid('graph', 20.0, 0.25), age=timedelta(minutes=20))

# ---------------------------------------------------------------- flower doodles
flowers = []
cols = ['FF8FAB', 'FFD166', 'B388FF', '80DEEA']
for i, (cx, cy) in enumerate([(300, 300), (620, 230), (930, 330), (460, 560), (820, 600)]):
    c = argb(cols[i % len(cols)])
    k = random.choice([5, 6, 7])
    r = random.uniform(70, 100)
    pts = curve(lambda t: (cx + r * math.cos(k * t) * math.cos(t), cy + r * math.cos(k * t) * math.sin(t)), 0, math.pi if k % 2 else 2 * math.pi, 220)
    flowers.append(freehand(pts, c, 5, 'fountain', jitter=0.4, step=2.5))
    flowers.append(shape('ellipse', cx - 14, cy - 14, cx + 14, cy + 14, argb('FFD166'), 2, filled=True))
    flowers.append(freehand(curve(lambda t: (cx + 30 * math.sin(t * 3), cy + r + t * 140), 0, 1, 30), argb('7BD389'), 5, 'soft', step=2.5))
flowers.append(freehand([(150, 760), (1150, 760)], argb('FFD166'), 26, 'highlighter', opacity=0.4))
flowers.append(text('spring doodles', 180, 690, argb('F5F5F5'), 'Permanent Marker', 40))
project('flower_doodles', [layer('Flowers', flowers)], DARK, age=timedelta(minutes=28))

# ---------------------------------------------------------------- notes
notes = [text('Kritzel launch — notes', 120, 90, argb('1E1E2E'), 'Caveat', 52, weight=700)]
items = ['finish manual (EN + DE)', 'take screenshots on the tablet', 'test SVG export', 'share .kritzel with team']
for i, it in enumerate(items):
    y = 190 + i * 70
    notes.append(shape('rectangle', 130, y + 8, 160, y + 38, argb('1E1E2E'), 2.5, radius=5))
    notes.append(text(it, 185, y - 4, argb('1E1E2E'), 'Caveat', 40))
    if i < 2:
        notes.append(freehand([(134, y + 22), (145, y + 34), (168, y - 2)], argb('2E7D32'), 4, 'variable'))
notes.append(freehand([(180, 190 + 2 * 70 + 26), (430, 190 + 2 * 70 + 26)], argb('FFD166'), 24, 'highlighter', opacity=0.5))
notes.append(freehand(curve(lambda t: (560 + 200 * t, 520 - 60 * math.sin(math.pi * t)), 0, 1, 40), argb('D7263D'), 4, 'ballpoint'))
notes.append(freehand([(745, 500), (762, 521), (735, 528)], argb('D7263D'), 4, 'ballpoint'))
notes.append(text('due Friday!', 790, 490, argb('D7263D'), 'Caveat', 44))
project('meeting_notes', [layer('Notes', notes)], OFFWHITE, grid('lined', 35.0, 0.35, argb('7FA7D9')), age=timedelta(minutes=30))

sketch = folder('Sketchbook')
work = folder('Work')
# A couple of quick extra projects inside folders so the folder cards show a count.
project('quick_sketch', [layer('Layer 1', [freehand(curve(lambda t: (400 + 300 * math.cos(t), 400 + 200 * math.sin(2 * t)), 0, 2 * math.pi, 200), argb('7C5CFF'), 6, 'fountain')])], OFFWHITE, age=timedelta(days=5), folder=sketch)
project('wireframe', [layer('Layer 1', [shape('rectangle', 200, 150, 900, 650, argb('1E1E2E'), 3, radius=20), shape('rectangle', 240, 190, 860, 260, argb('7C5CFF'), 2, filled=True, radius=8)])], WHITE, age=timedelta(days=8), folder=work)

with open(os.path.join(OUT, 'gallery.json'), 'w') as f:
    json.dump(dict(formatVersion=1, projects=projects, folders=folders), f)
print('ok', len(projects), 'projects')
