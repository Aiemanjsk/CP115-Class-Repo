import math
radius = input("radius for the circle: ")
radius = int(radius)
from math import sqrt, pow, sin, cos
power = pow(radius, 2)
circle_area = math.pi * power
circle_curcimference = 2 * math.pi * radius
print("area of a circle is: " + str(circle_area))
print("curcimference for a circle is: " + str(circle_curcimference))