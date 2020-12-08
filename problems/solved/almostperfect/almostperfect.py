#!/Users/fritjof/anaconda3/bin/python3
# problem: almostperfect, rating: 3.1

try:
    while True:
        n = int(input())
        s = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if n // i == i:
                    s.append(i)
                else:
                    s.append(i)
                    s.append(n//i)
        if sum(s) - 2*n == 0:
            print(f'{n} perfect')
        elif abs(sum(s) - 2*n) <= 2:
            print(f'{n} almost perfect')
        else:
            print(f'{n} not perfect')


except EOFError:
    pass
            
