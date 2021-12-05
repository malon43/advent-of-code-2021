from sys import stdin

points = {}
for line in stdin:
    a, b = [x.split(',') for x in line.split(' -> ')]
    x1, y1 = [int(i) for i in a]
    x2, y2 = [int(i) for i in b]

    if abs(x1 - x2) == abs(y1 - y2):
        sign_x = 1 if x1 - x2 >= 0 else -1
        sign_y = 1 if y1 - y2 >= 0 else -1
        for n in range(abs(y1 - y2) + 1):
            if (x2 + n * sign_x, y2 + n * sign_y) in points:
                points[x2 + n * sign_x, y2 + n * sign_y] += 1
            else:
                points[x2 + n * sign_x, y2 + n * sign_y] = 1
        continue
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
