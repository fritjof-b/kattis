#!/Users/fritjof/anaconda3/bin/python3
# problem: ofugsnuid, rating: 1.4

n = int(input())

xs = []

for _ in range(n):
    xs.append(input())

for i in xs[::-1]:
    print(i)
