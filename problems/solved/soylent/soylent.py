#!/Users/fritjof/anaconda3/bin/python3
# problem: soylent, rating: 
from math import ceil

n = int(input())
cpb = 400

for _ in range(n):
    c = int(input())
    print(ceil(c/cpb))
