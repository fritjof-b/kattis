#!/usr/local/bin/python3
moves = input()

pos = [1,0,0]

for move in moves:
    if move == 'A':
        pos[0], pos[1] = pos[1], pos[0]
    if move == 'B':
        pos[1], pos[2] = pos[2], pos[1]
    if move == 'C':
        pos[0], pos[2] = pos[2], pos[0]
    
print(pos.index(1) + 1)