#!/Users/fritjof/anaconda3/bin/python3
# problem: driversdilemma, rating: 2.1

d = input().split()
c, x, m = float(d[0]), float(d[1]), float(d[-1])
c /= 2 
top_speed = 0
for _ in range(6):
    d = input().split()
    speed, fuel_eff = int(d[0]), float(d[-1])
    fuel = c
    time = m / speed
    leak = time * x
    fuel -= leak
    t = (fuel_eff * fuel)

    if t >= m:
        top_speed = speed

if top_speed > 0:
    print(f'YES {top_speed}')
else:
    print('NO')
