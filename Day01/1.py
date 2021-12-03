from sys import stdin
from math import inf

prev = inf
count = 0
for line in stdin:
    count += int(line) > prev
    prev = int(line)

print(count)
