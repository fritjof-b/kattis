#!/usr/bin/python3
from collections import Counter

deck = Counter(input()).most_common()
points = 0

for card in deck:
    points += card[1]**2

if len(deck) == 3:
    points += deck[2][1] * 7

print(points)