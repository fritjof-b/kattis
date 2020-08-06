#!/usr/bin/python3
w, p = list(map(int, input().split()))
partitions = list(map(int, input().split()))
partitions.append(w)

out = set(partitions)

for i in range(len(partitions)):
    for j in range(i+1):
        out.add(partitions[i] - partitions[j])

out.remove(0)

print(' '.join((str(i) for i in sorted(out))))
