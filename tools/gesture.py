"""Usage: gesture.py down|move|up  x,y [x,y ...]  (preview coords; doubled). Builds one adb shell call."""
import subprocess, sys
kind = sys.argv[1]
pts = [tuple(int(float(v) * 2) for v in p.split(',')) for p in sys.argv[2:]]
cmds = []
for i, (x, y) in enumerate(pts):
    if kind == 'path':
        ev = 'DOWN' if i == 0 else 'MOVE'
    else:
        ev = kind.upper()
    cmds.append(f'input motionevent {ev} {x} {y}')
subprocess.run(['adb', 'shell', '; '.join(cmds)], check=True)
