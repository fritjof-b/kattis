#!/Users/fritjof/anaconda3/bin/python3
# problem: closingtheloop, rating: 1.5

n = int(input())

for case in range(1, n + 1):
    ns = int(input())
    s = sorted(input().split(), reverse=True)
    r = []
    b = []
    for c in s:
        if c[-1] == 'R':
            r.append(int(c[:-1]))
        else:
            b.append(int(c[:-1]))
    
    l = min(len(r), len(b))
    t = 0
    for i in range(l):
        t += r[i] + b[i]
    t -= l << 1
    if l == 0 or ns < 2:
        print(f'Case #{case}: 0')
    else:
        print(f'Case #{case}: {t}')
