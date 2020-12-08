#!/Users/fritjof/anaconda3/bin/python3
# problem: easiest, rating: 1.6

while True:
    n = int(input())
    if n == 0:
        break
    s = 0
    for c in str(n):
        s += int(c)
    i = 11
    found = False
    while not found:
        p = i * n
        sp = sum([int(_) for _ in str(p)])
        if sp == s:
            print(i)
            found = True
        i += 1
