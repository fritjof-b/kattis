#!/Users/fritjof/anaconda3/bin/python3
# problem: alphabetspam, rating: 1.4
from collections import Counter

st = input()

frequencies = [0, 0, 0, 0]

for c in st:
    if c == '_':
        frequencies[0] += 1
    elif c.islower():
        frequencies[1] += 1
    elif c.isupper():
        frequencies[2] += 1
    else:
        frequencies[3] += 1

for frequence in frequencies:
    print(frequence/len(st))
