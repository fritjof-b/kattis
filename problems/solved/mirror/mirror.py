#!/Users/fritjof/anaconda3/bin/python3
# problem: mirror, rating: 1.7
import sys

T = int(input())

for i in range(T):
    r, c = [int(_) for _ in input().split()]
    d = []
    for _ in range(r):
        d.append(input()) 
    print(f'Test {i+1}')
    for r in d[::-1]:
        print(r[::-1])
