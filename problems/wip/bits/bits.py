#!/Users/fritjof/anaconda3/bin/python3
# problem: bits, rating: 2.5
n = int(input())
for _ in range(n):
    x = bin(int(input())).count('1')
    if x <= 32:
        print(x)
    else:
        print(31)
