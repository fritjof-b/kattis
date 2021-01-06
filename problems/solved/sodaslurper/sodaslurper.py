#!/Users/fritjof/anaconda3/bin/python3
# problem: sodaslurper, rating: 1.6

e, f, c = [int(_) for _ in input().split()]
total = 0
nfi = e + f

while nfi >= c:
    nfi -= c
    total += 1
    nfi += 1

print(total)

