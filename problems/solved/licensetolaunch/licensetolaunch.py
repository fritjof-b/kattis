#!/Users/fritjof/anaconda3/bin/python3
n = int(input())
days = [int(d) for d in input().split()]

print(days.index(min(days)))
