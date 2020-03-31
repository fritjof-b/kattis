#!/bin/python3

import math

def price(k):
    return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)

args = list(map(int, input().split()))

p,a,b,c,d,n = [i for i in args]

price_list = []
for i in range(n):
    price_list.append(price(i+1))

largest_decline = 0

