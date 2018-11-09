#Ashby-Carson-Assn6
# This is a program to take inputs of how many sides a polygon has and its sidelength and generating an area

import math
from math import tan

sideAmount = eval(input("Enter how many sides: "))
sideLength = eval(input("Enter side length: "))



polygonArea = (sideAmount * math.pow(sideLength, 2))/(4 * tan((math.pi)/(sideAmount)))
polygonArea = round(polygonArea, 5)


print("The area of your polygon is: ", polygonArea)
