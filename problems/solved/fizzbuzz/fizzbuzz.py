
x, y, n = list(map(int, input().split()))
f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'

for i in range(1, n+1):
    o = i
    if i % x == 0:
        o = f
    if i % y == 0:
        o = b
    if i % x == 0 and i % y == 0:
        o = fb
    print(o)
