#!/Users/fritjof/anaconda3/bin/python3
# problem: grandpabernie, rating: 3.0
from collections import defaultdict
n = int(input())
trips = defaultdict()
for _ in range(n):
    c, y = input().split()
    y = int(y)
    if c in trips.keys():
        trips[c].append(y)
    else:
        trips[c] = [y]

for k in trips.keys():
    trips[k].sort()

q = int(input())
for _ in range(q):
    c, t = input().split()
    t = int(t)
    print(trips[c][t-1])
