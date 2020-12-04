#!/Users/fritjof/anaconda3/bin/python3
# problem: anothercandies, rating: 2.5

t = int(input())

for _ in range(t):
    input()
    n = int(input())
    d = []
    for i in range(n):
        d.append(int(input()))
    s = sum(d) % len(d)
    if not s:
        print('YES')
    else:
        print('NO')
