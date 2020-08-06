#!/usr/bin/python3

from collections import Counter

x, y = 0, 0
xs, ys = [], []

for i in range(3):
    xp, yp = list(map(int, input().split()))
    xs.append(xp)
    ys.append(yp)

print(Counter(xs).most_common()[-1][0], Counter(ys).most_common()[-1][0])