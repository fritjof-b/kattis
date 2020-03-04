import math

inp = list(map(int, input().split()))

h, v = inp[0], inp[1]

print(math.ceil(h/math.sin(math.radians(v))))
