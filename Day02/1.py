from sys import stdin

position = (0, 0)

commands = {
    "forward": lambda pos, x: (pos[0] + x, pos[1]),
    "down": lambda pos, x: (pos[0], pos[1] + x),
    "up": lambda pos, x: (pos[0], pos[1] - x)
}

for line in stdin:
    command, number = line.split()
    position = commands[command](position, int(number))

print(position[0] * position[1])
