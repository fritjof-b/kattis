#!/Users/fritjof/anaconda3/bin/python3
# problem: estimatingtheareaofacircle, rating: 1.5
from math import pi

while True:
    d = input()
    if d == "0 0 0":
        break
    d = d.split()
    r = float(d[0])
    m = int(d[1])
    c = int(d[-1])

    ratio = c/m
    square = (r*2)**2
    estimate = ratio * square
    circle = pi * r ** 2
    print(circle, estimate)
