from sys import stdin

c = 0

for line in stdin:
    _, out = line.split(' | ')
    outs = out.split()
    c += sum(len(o) in (2, 3, 4, 7) for o in outs)

print(c)