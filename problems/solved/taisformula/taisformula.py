#!/Users/fritjof/anaconda3/bin/python3
# problem: taisformula, rating: 1.5
# could convert floats to int before calculating to use less memory
n = int(input())
a = 0
t_i = v_i = -1
for _ in range(n):
    d = input().split()
    t_0 = t_i
    v_0 = v_i
    t_i = int(d[0])
    v_i = float(d[-1])
    if t_0 != -1:
        a += (t_i - t_0) * (v_i + v_0)/2
print(a/1000) 
