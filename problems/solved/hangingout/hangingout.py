#!/usr/bin/python3

import sys

data = []
l, x = list(map(int, input().split()))
rejected = inside = 0

for line in sys.stdin.readlines():
    data.append(line.strip('\n'))

for element in data:
    event, people = element.split()
    people = int(people)

    if event == 'enter' and people + inside <= l:
        inside += people
    elif event == 'leave':
        inside -= people
    else:
        rejected += 1

print(rejected)
