#!/usr/local/bin/python3
n = int(input())
xs = [i for i in list(map(int, input().split())) if i >= 0]
print(sum(xs)/len(xs))