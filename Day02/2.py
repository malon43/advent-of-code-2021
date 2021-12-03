from sys import stdin

position = (0, 0, 0)

commands = {
    "forward": lambda pos, x: (pos[0] + x, pos[1] + pos[2] * x, pos[2]),
    "down": lambda pos, x: (*pos[:2], pos[2] + x),
    "up": lambda pos, x: (*pos[:2], pos[2] - x)
}

for line in stdin:
    command, number = line.split()
    position = commands[command](position, int(number))

print(position[0] * position[1])
