from sys import stdin

numbers = [int(i) for i in stdin.readline().split(',')]
numbers.sort()
median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) // 2

print(sum(abs(median - i) for i in numbers))
