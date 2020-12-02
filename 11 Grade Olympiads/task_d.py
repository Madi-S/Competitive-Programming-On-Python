

with open('INPUT.TXT') as f:
    w, h, _ = int(f.read(1)), int(f.read(2)), int(f.read(3))
    coords = list(map(lambda c: [int(e) for e in c], [e.replace(' ', '') for e in f.read().split('\n')]))
metrics = []
for x in range(w):
    for y in range(h):
        metrics.append((x, y, x+1, y+1))
for coord in coords:
    x1, y1, x2, y2 = coord
    for x in range(x1, x2):
        for y in range(y1, y2):
            try:
                metrics.remove((x, y, x+1, y+1))
            except ValueError:
                pass
with open('OUTPUT.TXT', 'w') as f:
    f.write(str(len(metrics)))


