#!/Users/fritjof/anaconda3/bin/python3
# problem: modulo, rating: 1.4
import sys

data = [int(x.strip('\n')) for x in sys.stdin.readlines()]
d = set()

for e in data:
    d.add(e%42)

print(len(d))
