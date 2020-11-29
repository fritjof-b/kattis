#!/Users/fritjof/anaconda3/bin/python3
p, n = [int(d) for d in input().split()]

parts = set()
day = -1

for _ in range(n):
    parts.add(input())
    if len(parts) == p:
        day = _
        break

if day > -1:
    print(day + 1)
else:
    print('paradox avoided')
