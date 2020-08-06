#!/usr/bin/python3
import sys

n = int(input())
data = []

for line in sys.stdin.readlines():
    data.append(line.strip('\n'))

for message in data:
    square = m = 1
    l = len(message)
    while m < l:
        square += 1
        m = square * square

    encrypted = [[' ' for _ in range(square)] for _ in range(square)]
    message += (m - l) * '*'
    message = list(reversed(message))

    for i in range(square):
        for j in range(square):
            encrypted[i][j] = message.pop()

    rotated = list(zip(*encrypted[::-1]))
    flattened = [char for tup in rotated for char in tup if char != '*']

    print(''.join(flattened))

    # print(' '.join(zip(*rotated)))
