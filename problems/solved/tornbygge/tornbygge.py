#!/Users/fritjof/anaconda3/bin/python3
# problem: tornbygge, rating: 1.7
n = int(input())
xs = [int(_) for _ in input().split()]

t = 1

for i in range(len(xs) - 1):
    if xs[i] < xs[i+1]:
        t += 1
print(t)
