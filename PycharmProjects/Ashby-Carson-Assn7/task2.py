#Ashby-Carson-Assn7-task2
#This is a program that takes inputs for two circles and states if those circles overlap and how.

circle1x, circle1y, circle1Radius = eval(input("Enter circle1's center x-, y-coordinates, and radius:"))
circle2x, circle2y, circle2Radius = eval(input("Enter circle2's center x-, y-coordinates, and radius:"))


circleDistance = ((circle1x - circle2x)^2 + (circle1y - circle2y)^2) ** .5



if circleDistance < abs(circle1Radius - circle2Radius): print("Circle 2 is inside circle 1")
elif circleDistance < abs(circle2Radius - circle1Radius): print("Circle 1 is inside circle 2")
elif circleDistance < circle1Radius + circle2Radius: print("The circles overlap")
else: print("The circles do not overlap.")


