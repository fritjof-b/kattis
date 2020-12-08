#!/Users/fritjof/anaconda3/bin/python3
# problem: buka, rating: 1.7
import operator

ops = { '+': operator.add, '*': operator.mul }

x = int(input())
op = input()
y = int(input())

print(ops[op](x,y))
