n = int(input())
secs = []
gunilla, edward = "gunilla has a point", "edward is right"

for i in range(n):
    line = list(map(int, input().split()))
    secs.append(list(range(line[0], line[1] + 1)))

result = set(secs[0])
for s in secs[1:]:
    result.intersection_update(s)

if len(result) > 0:
    print(gunilla)
else:
    print(edward)
