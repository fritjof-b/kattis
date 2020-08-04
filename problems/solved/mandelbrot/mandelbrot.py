#!/usr/bin/python3
import sys
from math import sqrt

case = 1

def quadratic(a):
    x, y = a[0], a[1]
    return (x*x - y*y, 2 * x * y)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def modulus(a):
    return sqrt(a[0]*a[0] + a[1]*a[1])

for line in sys.stdin.readlines():
    mandelbrot = 'IN'
    xyr = line.split()
    x, y, r = float(xyr[0]), float(xyr[1]), int(xyr[2])
    a, c = (0, 0), (x, y)

    for _ in range(r):
        b = add(quadratic(a), c)
        if (modulus(b)) > 2:
            mandelbrot = 'OUT'
        a = b
    
    print(f'CASE {case}: {mandelbrot}')
    case += 1
