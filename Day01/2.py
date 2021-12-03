from collections import deque
from math import inf
from sys import stdin

prev = deque([inf] * 3, 3)
count = 0
for line in stdin:
    prev_sum = sum(prev)
    prev.append(int(line))
    count += sum(prev) > prev_sum

print(count)
