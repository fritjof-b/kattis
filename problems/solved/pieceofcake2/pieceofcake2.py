#!/usr/bin/python3

n, h, v = list(map(int, input().split()))
thicc = 4

if h <= n / 2:
    h = n - h

if v <= n / 2:
    v = n - v

print(h*v*thicc)