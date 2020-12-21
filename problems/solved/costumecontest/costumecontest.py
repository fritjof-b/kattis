#!/Users/fritjof/anaconda3/bin/python3
# problem: costumecontest, rating: 1.9
from collections import Counter

n = int(input())

costumes = []
for _ in range(n):
    costumes.append(input())

costumes = Counter(costumes)
common = []
for e in costumes.most_common()[::-1]:
    if len(common) == 0 or common[-1][-1] == e[-1]:
        common.append(e)

for c in sorted(common):
    print(c[0])
