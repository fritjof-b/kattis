#!/Users/fritjof/anaconda3/bin/python3
# problem: beehs, rating: 2.1
from math import hypot

data = 1
try:
    while data:
        data = input().split()
        if data[0] == '0.0' and data[1] == '0':
            break 

        D, N = float(data[0]), int(data[1]) 
        hs = []
        t = set()
        for _ in range(N):
            hs.append([float(_) for _ in input().split()])
        
        sweet = N
        for h in hs:
            dis = []
            for n in hs:
                if h != n:
                    dis.append(hypot(h[0] - n[0], h[1] - n[1]) >= D)

            if not all(dis):
                sweet -= 1

        print(f'{N - sweet} sour, {sweet} sweet')

except EOFError as e:
   pass 
