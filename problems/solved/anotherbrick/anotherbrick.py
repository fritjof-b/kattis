#!/bin/python3

# First line 3 ints => h w n
# h, w, n = height, width, bricks
# seconds line n integers => x_1 x_2 ... x_n
# x_1 length of brick 1 etc
# output = YES or NO, if wall  complete

h, w, n = [ int(i) for i in input().split() ]
bricks = [ int(i) for i in input().split() ]



msg = "NO"
current_height = 0
current_width = 0

while current_width <= w and current_height < h:
	current_width += bricks.pop(0)

	if current_width == w:
		current_height += 1
		current_width = 0

	if current_width > w:
		break

print(msg)