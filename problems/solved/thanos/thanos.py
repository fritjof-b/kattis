#!/Users/fritjof/anaconda3/bin/python3
# problem: thanos, rating: 2.7

t = int(input())

for _ in range(t):
    yrs = 0
    p, r, f = input().split()
    p = int(p)
    r = float(r)
    f = float(f)
    
    while p <= f:
        p *= r
        p = int(p)
        yrs += 1 
    print(yrs)
