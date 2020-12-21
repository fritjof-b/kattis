#!/Users/fritjof/anaconda3/bin/python3
# problem: bookingaroom, rating: 1.7

r, n = [int(_) for _ in input().split()]

free = [True for _ in range(r)]
for _ in range(n):
    b = int(input()) - 1
    free[b] = False

f = False

for room in free:
    if room:
        print(free.index(room) + 1)
        f = True
        break

if not f:
    print('too late')
