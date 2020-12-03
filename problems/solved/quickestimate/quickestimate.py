#!/Users/fritjof/anaconda3/bin/python3
import sys
data = sys.stdin.readlines()

for d in data[1:]:
    print(len(d) -1)
