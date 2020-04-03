#!/bin/python3

import math

def price(k):
    return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)

args = list(map(int, input().split()))

p, a, b, c, d, n = [i for i in args]

max_value = price(1)
max_dif = 0

for i in range(2,n+1):
    price_i = price(i)
    if price_i > max_value:
        max_value = price_i
    if max_dif < max_value - price_i:
        max_dif = (max_value - price_i) 

print(round(max_dif,6))