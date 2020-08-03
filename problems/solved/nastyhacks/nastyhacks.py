#!/usr/bin/python3

n = int(input())

ad, nad, dm = 'advertise', 'do not advertise', 'does not matter'

for i in range(n):
    r, e, c = list(map(int, input().split()))
    diff = e - c

    if r > diff:
        msg = nad
    if r < diff:
        msg = ad
    if r == diff:
        msg = dm

    print(msg)
