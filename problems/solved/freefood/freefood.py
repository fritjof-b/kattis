#!/Users/fritjof/anaconda3/bin/python3
# problem: freefood, rating: 1.5

n = int(input())

days = set()

for i in range(n):
    s, f = [int(_) for _ in input().split()]
    for j in range(s, f + 1):
        days.add(j)

print(len(days))
