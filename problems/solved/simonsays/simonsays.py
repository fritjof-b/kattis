#!/Users/fritjof/anaconda3/bin/python3
n = int(input())

for _ in range(n):
    s = input().split()
    if " ".join(s[0:2]) == "Simon says":
        print(" ".join(s[2:len(s)]))
