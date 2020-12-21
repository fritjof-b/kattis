#!/Users/fritjof/anaconda3/bin/python3
# problem: notamused, rating: 2.2
import sys
from collections import deque

xs = sys.stdin.read().split('\n')

tbl = {}
pricing = .1
day = 0

for x in xs:
    if x == 'OPEN':
        if day != 0:
            print()
        tbl.clear()
        day += 1
    elif x == 'CLOSE':
        for p in tbl:
            time_spent = 0
            for i in range(0, len(tbl[p]), 2):
                time_spent += tbl[p][i] - tbl[p][i+1]

            tbl[p] = time_spent * pricing

        print(f'Day {day}')
        for p in sorted(list(tbl.keys())):
            print(f'{p} ${tbl[p]:.2f}') 

    elif x == "":
        break
    else:
        op, name, time = x.split()
        if name not in tbl.keys():
            tlist = deque()
            tlist.append(int(time))
            tbl[name] = tlist
        else:
            tbl[name].appendleft(int(time))

