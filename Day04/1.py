from sys import stdin

def verify_board(b, numbers):
    if any(all(n in numbers for n in row) for row in b):
        return True
    if any(all(row[n] in numbers for row in b) for n in range(len(b[0]))):
        return True
    return False

lines = stdin.readlines()

numbers = map(int, lines[0].strip().split(','))
boards = []
board = []
for i in lines[2:]:
    if i.strip() == "":
        boards.append(board)
        board = []
        continue
    board.append(list(map(int, i.split())))

curr_numbers = set()
for number in numbers:
    curr_numbers.add(number)
    for board in boards:
        if verify_board(board, curr_numbers):
            print(sum(n for row in board for n in row if n not in curr_numbers) * number)
            exit()
