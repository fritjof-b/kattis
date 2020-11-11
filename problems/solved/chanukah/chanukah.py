
cases = int(input())

for i in range(1, cases + 1):
    case, n = list(map(int, input().split()))
    candles = 0
    for j in range(1, n + 1):
        candles += j + 1
    print(i, candles)