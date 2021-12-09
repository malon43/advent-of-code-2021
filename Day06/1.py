from sys import stdin

fish = [int(i) for i in stdin.readline().split(',')]
new_fish = []

for day in range(80):
    fish.extend(new_fish)
    c = 0
    for n in range(len(fish)):
        fish[n] -= 1
        if fish[n] < 0:
            c += 1
            fish[n] = 6
    new_fish = [8] * c
fish.extend(new_fish)

print(len(fish))