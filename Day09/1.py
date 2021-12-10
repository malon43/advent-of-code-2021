from sys import stdin

m = []
for line in stdin:
    m.append([int(i) for i in line.strip()])

def is_low(m, x, y):
    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= x + a < len(m[0]) and 0 <= y + b < len(m) and m[y][x] >= m[y + b][x + a]:
            return False
    return True


s = 0
for x in range(len(m[0])):
    for y in range(len(m)):
        if is_low(m, x, y):
            s += m[y][x] + 1

print(s)
