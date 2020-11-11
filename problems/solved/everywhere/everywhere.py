#!/usr/local/bin/python3
t = int(input())

for _ in range(t):
    trips = int(input())
    trip_set = set()
    for _ in range(trips):
        trip_set.add(input())
    print(len(trip_set))