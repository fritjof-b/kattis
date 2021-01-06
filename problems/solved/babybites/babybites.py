#!/Users/fritjof/anaconda3/bin/python3
# problem: babybites, rating: 1.7

n = int(input())
c = 1

a = input().split()

for w in a:
    if w == 'mumble':
        c += 1
    elif int(w) == c:
        c += 1

if c == n + 1:
    print('makes sense')
else:
    print('something is fishy')
