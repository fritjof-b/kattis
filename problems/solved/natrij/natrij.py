#!/usr/bin/python3

h0, m0, s0 = list(map(int, input().split(':')))
h1, m1, s1 = list(map(int, input().split(':')))
curr = h0 * 60 * 60 + m0 * 60 + s0
expl = h1 * 60 * 60 + m1 * 60 + s1

ans = []

def make_dec(num):
    if num <= 9:
        return f'0{num}'
    else:
        return str(num)

if curr > expl:
    expl += 24*60*60

tot = expl - curr

s = tot % (24 * 3600)
h = s // 3600
s %= 3600
m = s // 60
s %= 60

ans.append(make_dec(h))
ans.append(make_dec(m))
ans.append(make_dec(s))

if tot == 0:
    print('24:00:00')
else:
    print(':'.join(ans))