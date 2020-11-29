#!/Users/fritjof/anaconda3/bin/python3
n = int(input())

for _ in range(n):
    d = [int(x) for x in input().split()]
    total = 0
    for i in range(len(d[1:])):
        if (d[i] - (2 * d[i-1])) > 0:
            total += (d[i] - (2 * d[i-1]))
    print(total - 1)
