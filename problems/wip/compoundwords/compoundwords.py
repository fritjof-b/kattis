#!/Users/fritjof/anaconda3/bin/python3
# problem: compoundwords, rating: 1.6
import sys
from itertools import chain

words = [_.strip('\n').split() for _ in sys.stdin.readlines()]
words = sorted(list(chain.from_iterable(words)))

a = set()

for i in words:
    for j in words:
        if i != j:
            a.add(i + j)

print(a)
for word in a:
    print(word)
