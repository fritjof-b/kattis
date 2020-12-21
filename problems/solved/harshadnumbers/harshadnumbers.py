#!/Users/fritjof/anaconda3/bin/python3
# problem: harshadnumbers, rating: 1.4

n = int(input())

while True:
    ns = sum([int(_) for _ in str(n)])
    if n % ns == 0:
        print(n)
        break
    else:
        n += 1
