#!/Users/fritjof/anaconda3/bin/python3
# problem: aprizenoonecanwin, rating: 2.7

n, x = [int(_) for _ in input().split()]

items = [int(_) for _ in input().split()]
items.sort()

c = 1
tot = items[0]

for i in range(1, len(items)):
    if items[i-1] + items[i] <= x:
        tot += items[i]
        c += 1

print(c)
