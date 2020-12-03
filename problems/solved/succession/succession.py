#!/Users/fritjof/anaconda3/bin/python3
# problem: succession, rating: 3.2

class FamilyTree

n, m = list(map(int, input().split()))

founder = input()

ftree = { founder: [] }

for _ in range(n):
    c, p1, p2 = input().split()
    
    if c in ftree.keys():
        ftree[c] += [p1, p2]
    else:
        ftree[c] = [p1, p2]
    
print(ftree)