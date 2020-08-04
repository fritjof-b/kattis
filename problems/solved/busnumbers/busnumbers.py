#!/usr/bin/python3

n = int(input())
buses = sorted(map(int, input().split()))
buses.append(-1)

prev = buses[0]
length = i = 1
ans = []

while i < len(buses):
    bus = buses[i]

    if bus == prev + 1:
        length += 1
    else:
        if length >= 3:
            ans.append(f'{buses[i-length]}-{buses[i-1]}')
        elif length == 2:
            ans.append(buses[i-2])
            ans.append(buses[i-1])
        else:
            ans.append(buses[i-1])
        length = 1
    prev = bus
    i += 1

print(' '.join([str(i) for i in ans]))