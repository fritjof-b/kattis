#!/Users/fritjof/anaconda3/bin/python3
# problem: babelfish, rating: 2.2
import sys

t = {}

try:
    while True:
        v, k = input().split()
        t[k] = v

except:
    x = [l.strip('\n') for l in sys.stdin.readlines()]
    for k in x:
        if k in t.keys():
            print(t[k])
        else:
            print('eh')
