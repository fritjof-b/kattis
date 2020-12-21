#!/Users/fritjof/anaconda3/bin/python3
# problem: judgingmoose, rating: 1.4

l, r = [int(_) for _ in input().split()]

if l == 0 and r == 0:
    print('Not a moose')
elif l - r == 0:
    print(f'Even {l*2}')
elif abs(l-r) >= 1:
    print(f'Odd {max(l, r)*2}')
