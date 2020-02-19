#!/bin/python3

import math
fact = float(input())

sonic_radius = 1
sonic_circ = 2*sonic_radius*math.pi

circle_radius = fact
circle_circ = 2*circle_radius*math.pi

print(circle_circ/(sonic_circ) - 1)