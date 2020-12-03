#!/Users/fritjof/anaconda3/bin/python3
# problem: somesum, rating: 1.7

n = int(input())

if n == 1:
    print('Either')
else:
    ns = [_ for _ in range(1,101)]
    sums = [sum(ns[i:i+n]) for i in range(len(ns) - n + 1)] 
    even = [s % 2 == 0 for s in sums]
    odd = [s % 2 == 1 for s in sums]
    
    if all(even):
        print('Even')
    elif all(odd):
        print('Odd')
    else:
        print('Either')
