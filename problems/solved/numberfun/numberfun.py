for _ in range(int(input())):
    a, b, c = [int(i) for i in input().split()]

    if a / b == c or a + b == c or a * b == c or b / a == c or abs(a - b) == c:
        print('Possible')
    else: 
        print('Impossible')