

with open('INPUT.TXT') as f:
    w, h, _ = int(f.read(1)), int(f.read(2)), int(f.read(3))
    coords = list(map(lambda c: [int(e) for e in c], [
                  e.replace(' ', '') for e in f.read().split('\n')]))
    print(coords)
    coords = [[1, 2, 3, 4], [2, 5, 7, 7], [9, 9, 10, 10]]
    w, h = 10, 10
    print(w, h, coords)
metrics = []
for x in range(w):
    for y in range(h):
        metrics.append((x, y, x+1, y+1))
print(metrics)
for coord in coords:
    x1, y1, x2, y2 = coord
    for x in range(x1, x2):
        for y in range(y1, y2):
            try:
                metrics.remove((x, y, x+1, y+1))
            except ValueError:
                pass
with open('OUTPUT.TXT', 'w') as f:
    print(metrics)
    f.write(str(len(metrics)))
