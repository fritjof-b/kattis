#!/Users/fritjof/anaconda3/bin/python3
# problem: cursethedarkness, rating: 2.4
from math import hypot

m = int(input())

for _ in range(m):
    x, y = [float(_) for _ in input().split()]
    cpos = []
    n = int(input())
    for _ in range(n):
        cpos.append([float(_) for _ in input().split()])
    curse = True 
    for p in cpos:
        if hypot(x - p[0], y - p[1]) < 8: 
            curse = False 

    if not curse:
        print('light a candle')
    else:
        print('curse the darkness')
