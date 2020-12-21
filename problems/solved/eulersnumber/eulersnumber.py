#!/Users/fritjof/anaconda3/bin/python3
# problem: eulersnumber, rating: 2.1
from math import factorial

n = int(input())
e = 1
facs = 1
for i in range(1, n + 1):
   facs *= i
   e += (1/facs) 
print(e)

