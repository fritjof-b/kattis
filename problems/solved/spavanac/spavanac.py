#!/usr/bin/python3

h, m = list(map(int, input().split()))

if h == 0:
    h = 24

m += h * 60
m -= 45

print(int(m/60), m%60)