#!/Users/fritjof/anaconda3/bin/python3
w = int(input())
n = int(input())
cakesum = 0
for _ in range(n):
    w_i, l = [int(_) for _ in input().split()]
    cakesum += w_i * l

print(cakesum // w)
