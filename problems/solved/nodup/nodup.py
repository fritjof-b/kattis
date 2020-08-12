#!/usr/bin/python3

words = input().split()
filtererd = set(words)

msg = 'yes'

if len(words) != len(filtererd):
    msg = 'no'

print(msg)
