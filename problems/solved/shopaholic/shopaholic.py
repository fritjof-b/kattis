#!/Users/fritjof/anaconda3/bin/python3
# problem: shopaholic, rating: 2.3

n = int(input())

items = [int(_) for _ in input().split()]
items.sort(reverse=True)

discount = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        discount += items[i-1]

print(discount)