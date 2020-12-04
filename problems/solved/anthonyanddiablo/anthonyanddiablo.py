#!/Users/fritjof/anaconda3/bin/python3
# problem: anthonyanddiablo, rating: 2.4
from math import pi

a, n = [float(_) for _ in input().split()]

def circle(c):
    r = c/(2*pi)
    return (r**2)*pi 

if circle(n) >= a:
    print('Diablo is happy!')
else:
    print('Need more materials!')
