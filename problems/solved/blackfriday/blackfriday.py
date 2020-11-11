#!/usr/local/bin/python3
n = int(input())
xs = list(map(int, input().split()))

qs = []
i = 0
while i < len(xs):
    if xs[i] not in qs and xs[i] not in xs[i+1:] and xs[i] not in xs[0:i]:
        qs.append(xs[i])

    i += 1

if len(qs) > 0:
    top = sorted(qs)[-1]
    print(xs.index(top) + 1)
else:
    print('none')


