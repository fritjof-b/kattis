#!/usr/bin/python3

grades = []
winner = (0, 0)

for i in range(1, 6):
    grades.append(list(map(int, input().split())))
    if sum(grades[i-1]) > winner[1]:
        winner = (i, sum(grades[i-1]))

print(winner[0], winner[1])