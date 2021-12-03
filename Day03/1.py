from sys import stdin

line_count = 0
bit_count = [0] * 12
for line in stdin:
    line_count += 1
    for n, bit in enumerate(line.strip()):
        bit_count[n] += int(bit)

a = int(''.join(map(lambda x: "0" if x > line_count // 2 else "1", bit_count)), base=2)
print(a * (a ^ (2 ** 12 - 1)))
