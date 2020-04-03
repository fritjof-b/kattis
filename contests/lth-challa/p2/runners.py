#!/bin/python3

distances = []
runners = int(input())

for i in range(runners):
    distances.append(int(input()))

distances += distances

shortest_path = max(distances) + max(distances)

x=2
for i in distances[2::]:
    start = distances[x]
    finish = distances[x-2]
    if (start + finish < shortest_path):
        shortest_path = start+finish
    x += 1

print(shortest_path)