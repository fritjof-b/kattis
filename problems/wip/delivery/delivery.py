#!/bin/python3

# Read N and K
# N = number of locations
# K = carrying capacity
n, k = map(int, input().split())

# Read letters and locations
# Save somewhere
for i in range(n):
    loc, ltr = map(int, input().split())
    