#!/Users/fritjof/anaconda3/bin/python3
# problem: oddmanout, rating: 1.5

n = int(input())

for i in range(1, n + 1):
    g = int(input())
    u = set()
    for x in input().split():
        if x not in u:
            u.add(x)
        elif x in u:
            u.remove(x)

    print(f'Case #{i}: {u.pop()}')
