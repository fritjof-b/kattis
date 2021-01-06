#!/Users/fritjof/anaconda3/bin/python3
# problem: haypoints, rating: 2.0

m, n = [int(_) for _ in input().split()]
tbl = {}

for _ in range(m):
    dat = input().split()
    description, value = dat[0], int(dat[-1])
    tbl[description] = value

req = []
while 0 < n:
    salary = 0
    x = input()
    if x != '.':
        req += x.split()
    elif x == '.':
        for word in req:
            if word in tbl.keys():
                salary += tbl[word]
        print(salary)
        req = []
        n -=1
