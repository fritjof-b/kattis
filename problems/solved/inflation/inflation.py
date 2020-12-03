#!/Users/fritjof/anaconda3/bin/python3
# problem: inflation, rating: 1.7

b = int(input())
cans = [int(_) for _ in input().split()]
cans.sort()
r = 2
for i in range(len(cans)): 
    if (i+1) - cans[i] < 0:
        print('impossible')
        r = 2
        break
    if cans[i]/(i+1) < r:
        r = cans[i]/(i+1)

if r > 0 and r <= 1:
    print(r)
elif r == 0.0:
    print('0')
