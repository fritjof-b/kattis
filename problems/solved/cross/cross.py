#!/usr/bin/python3

import sys
import string

data = []
board = [
    f'{letter}{num}' for letter in string.ascii_lowercase[0:9] for num in range(1, 10)]

print(board, len(board))

for line in sys.stdin.readlines():
    data.append(line.strip('\n'))


def validate_row():
    pass


for j in range(9):
    print(data[0][j])
