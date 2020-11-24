#!/Users/fritjof/anaconda3/bin/python3
from math import sin, cos, radians

g = 9.81

def x(v_0, t, theta):
    return v0 * t * cos(theta)
    
def y(v_0, t, theta):
    return v_0 * t * sin(theta) - (g/2)*(t**2)

def t(x_1, v_0, theta):
    return x_1/(v_0*cos(theta))

n = int(input())
for _ in range(n):
    v_0, theta, x_1, h1, h2 = list(map(float, input().split()))
    theta = radians(theta)
    t_1 = t(x_1, v_0, theta)
    height = y(v_0, t_1, theta)

    if height > h1 and height < h2:
        print('Safe')
    else:
        print('Not Safe')
