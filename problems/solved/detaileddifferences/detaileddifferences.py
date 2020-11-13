#!/usr/local/bin/python3

n = int(input())

for _ in range(n):
    s1 = input()
    s2 = input()
    i = 0
    s3 = []
    while i < len(s1):
        if s1[i] == s2[i]:
            s3.append('.')
        else:
            s3.append('*')
        i += 1
    print(f'{s1}\n{s2}\n{"".join(s3)}\n')