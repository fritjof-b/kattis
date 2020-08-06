#!/bin/python3

n = 0

while n < 10:
	travelled = 0
	last_time = 0

	x = int(input())
	if x == -1: break
	for i in range(x):
		speed, time = [int(i) for i in input().split()]
		travelled += speed * (time - last_time)
		last_time = time

	print(f'{travelled} miles')
	n += 1

