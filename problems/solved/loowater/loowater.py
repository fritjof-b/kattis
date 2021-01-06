#!/Users/fritjof/anaconda3/bin/python3
# problem: loowater, rating: 2.7

while True:
    n, m = [int(_) for _ in input().split()]

    if n == 0 and m == 0:
        break

    heads, knights = [[], []]

    for _ in range(n):
        heads.append(int(input()))
    for _ in range(m):
        knights.append(int(input()))

    heads.sort()
    knights.sort()
    cost = 0
    removed = 0
    i = j = 0
    while j < len(heads) and i < len(knights):
        if knights[i] >= heads[j]:
            cost += knights[i]
            removed += 1
            j += 1
            i += 1
        else:
            i += 1
    if removed == len(heads):
        print(cost)
    else:
        print('Loowater is doomed!')
