#!/Users/fritjof/anaconda3/bin/python3
# problem: apaxiaaans, rating: 1.5

s = input()
ss = s[0]

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        ss += s[i]

print(ss)
