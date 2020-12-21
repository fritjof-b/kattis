#!/Users/fritjof/anaconda3/bin/python3
# problem: zoo, rating: 
n = -1
case = 1
while True: 
    n = input()
    if n == '0':
        break
    a = {}
    for _ in range(int(n)):
        animal = input().split()[-1].lower()
        if animal not in a.keys():
            a[animal] = 1
        else:
            a[animal] += 1

    print(f'List {case}:')
    for e in sorted(list(a.keys())):
        print(f'{e} | {a[e]}')
        
    case += 1
