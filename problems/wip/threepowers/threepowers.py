#!/Users/fritjof/anaconda3/bin/python3
from math import log2
from collections import deque
# { {}, {1}, {3}, {9}, {27}, {81}, {1,3}, {3,9}, {1,3,9} }
# --> { {}, {1}, {3}, {1,3}, {9}, {1,9}, {3,9}, {1,3,9} }
# -----> 7th index => {3, 9}

n = int(input())
while n != 0:
    # Save subsets to string because of memory
    s = deque()
    
    while n > 0:
        # closest power of 2 to n
        p = int(log2(n))

        # add correct subset to answer
        s.appendleft(str(3**p))

        # reduce n
        n %= int(2**p)

    n = int(input())
    print('{ ' + ", ".join(s) + ' }')
