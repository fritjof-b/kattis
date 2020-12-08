#!/Users/fritjof/anaconda3/bin/python3
# problem: alexandbarb, rating: 3.5

k, m, n = [int(_) for _ in input().split()]

if k % (m + n) < m:
    print('Barb')
else: print('Alex')
