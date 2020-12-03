#!/Users/fritjof/anaconda3/bin/python3
# problem: lastfactorialdigit, rating: 1.3

from math import factorial

t = int(input())
fac = [factorial(i) for i in range(1, 11)]
for _ in range(t):
    n = int(input())
    print(str(fac[n-1])[-1]) 
