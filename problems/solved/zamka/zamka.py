#!/usr/local/bin/python3
import sys
data = []
for line in sys.stdin.readlines():
    data.append(int(line.strip('\n')))

l, d, x = data
o = []
for i in range(l,d + 1):
    q = 0
    for c in str(i):
        q += int(c)
    
    if q == x:
        o.append(i)

print(f'{o[0]}\n{o[-1]}')
