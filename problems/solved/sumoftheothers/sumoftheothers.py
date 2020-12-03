#!/Users/fritjof/anaconda3/bin/python3
# problem: sumoftheothers, rating: 2.1

import sys

data = [x.strip('\n') for x in sys.stdin.readlines()]

for d in data:
    Z = [int(_) for _ in d.split()] 
    for z in Z:
        if z == sum(Z) - z:
            print(z)
            break
