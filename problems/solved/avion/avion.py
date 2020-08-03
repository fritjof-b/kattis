#!/bin/python3

strings = []
omegalul = "HE GOT AWAY!"

for i in range(1,6):
    if "FBI" in input():
        strings.append(f'{i} ')

if len(strings):
    print("".join(strings))
else:
    print(omegalul)
