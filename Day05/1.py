from sys import stdin

points = {}
for line in stdin:
    a, b = [x.split(',') for x in line.split(' -> ')]
    x1, y1 = [int(i) for i in a]
    x2, y2 = [int(i) for i in b]
    
    if x1 == x2:
        for n in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, n) in points:
                points[x1, n] += 1
            else:
                points[x1, n] = 1
        continue
    if y1 == y2:
        for n in range(min(x1, x2), max(x1, x2) + 1):
            if (n, y1) in points:
                points[n, y1] += 1
            else:
                points[n, y1] = 1

print(sum(val > 1 for val in points.values()))
