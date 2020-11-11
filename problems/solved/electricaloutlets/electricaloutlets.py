#!/usr/local/bin/python3

n = int(input())

for _ in range(n):
    x = list(map(int, input().split()))
    print(sum(x[1:]) - (x[0] - 1))