#!/Users/fritjof/anaconda3/bin/python3
# problem: 2naire, rating: 2.8

# { 1 --> 2 } : p
# { 1 --> 0 } : 1 - p

data = input().split()
n = int(data[0])
t = float(data[1])

W = [2**i for i in range(n+1)]
p = (1 + t)/2
print(W)
Q = [W[i]*p - (W[i]*(1-p)) for i in range(n + 1)]
print(sum(Q)/2)
