import math
import sys

for line in sys.stdin:
    digs = [int(dig) for dig in line.split()]
    a,b = digs[0], digs[1]
    print(abs(a-b))
