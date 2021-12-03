from sys import stdin


def func(lines, bits):
    current_bit = 0
    while len(lines) > 1:
        desired_bit = bits[sum(map(lambda x: int(x[current_bit]), lines)) < len(lines) / 2]
        lines = list(filter(lambda x: x[current_bit] == desired_bit, lines))
        current_bit += 1
    return int(lines[0], base=2)


lines = list(map(str.strip, stdin))
print(func(lines, "01") * func(lines, "10"))

