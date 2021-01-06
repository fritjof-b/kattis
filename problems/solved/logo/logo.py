#!/Users/fritjof/anaconda3/bin/python3
# problem: logo, rating: 3.0

from math import cos, sin, radians, pi

cases = int(input())
for _ in range(cases):
    x = y = 0
    theta = 0 
    moves = range(int(input()))
    for move in moves:
        d = input().split()
        command, value = d[0], int(d[1])
        
        if command == 'fd':
            x += value * cos(theta)
            y += value * sin(theta)
        elif command == 'bk':
            x -= value * cos(theta)
            y -= value * sin(theta)
        elif command == 'lt':
            theta += radians(value)
            theta %= (2 * pi)
        elif command == 'rt':
            theta -= radians(value)
            theta %= (2 * pi)
    print(round(abs(0 - (x**2 + y**2)**(1/2))))

