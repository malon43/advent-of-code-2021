from sys import stdin

fish = [0] * 9

fishin = [int(i) for i in stdin.readline().split(',')]
for f in fishin:
    fish[f] += 1

for day in range(256):
    f0 = fish[0]
    for f in range(len(fish) -1):
        fish[f] = fish[f + 1]
    fish[6] += f0
    fish[-1] = f0


print(sum(fish))
