#!/Users/fritjof/anaconda3/bin/python3
from collections import Counter
hand = input().split()
ranks = Counter([h[0] for h in hand]).most_common()[0][1]
print(ranks)
