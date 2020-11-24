#!/Users/fritjof/anaconda3/bin/python3
w = [1,1,2,2,2,8]
a = list(map(int, input().split()))
o = []
for i in range(len(w)):
    o.append(str(w[i]-a[i]))

print(" ".join(o))
