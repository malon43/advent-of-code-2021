from sys import stdin

numbers = [int(i) for i in stdin.readline().split(',')]

avg = round(sum(numbers) / len(numbers)) - 1

print(sum(abs(avg - i) * (abs(avg - i) + 1) / 2 for i in numbers))
