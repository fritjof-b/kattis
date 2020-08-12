#!/usr/bin/python3

c = float(input())
l = int(input())
tot = 0

for i in range(l):
    w, l = list(map(float, input().split()))
    tot += w * l * c

print(tot)
