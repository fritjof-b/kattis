#!/Users/fritjof/anaconda3/bin/python3
# problem: apaxianparent, rating: 1.5

y, p = input().split()

if y.endswith('e'):
    s = f'{y}x{p}'
elif y[-1] in ['a', 'i', 'o', 'u']:
    s = f'{y[:-1]}ex{p}'
elif y.endswith('ex'):
    s = y + p
else:
    s = f'{y}ex{p}'

print(s)
