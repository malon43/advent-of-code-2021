from sys import stdin

m = []
for line in stdin:
    m.append([int(i) for i in line.strip()])

def is_low(m, x, y):
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= x + a < len(m[0]) and 0 <= y + b < len(m) and m[y][x] >= m[y + b][x + a]:
            return False
    return True

largest = [0, 0, 0]

points = set()

for x in range(len(m[0])):
    for y in range(len(m)):
        if is_low(m, x, y):
            points.add((x, y))

largest = [0] * 3

while points:
    q = {points.pop()}
    count = 0
    while q:
        x, y = q.pop()
        count += 1
        m[y][x] = -1
        for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= x + a < len(m[0]) and 0 <= y + b < len(m) and 0 <= m[y + b][x + a] < 9:
                q.add((x + a, y + b))
                points -= {(x + a, y + b)}
    if count > min(largest):
        largest = [count] + sorted(largest)[1:]

print(largest[0] * largest[1] * largest[2])
