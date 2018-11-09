#Ashby-Carson-Assn5
#this is a program that takes the input of a location and beginning radius from a user and draws a bullseye using it.

import turtle

turtle.showturtle()
x1, y1 = eval(input("Enter your starting coordinates: "))
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

radius = eval(input("Enter starting radius: "))
radius += 75


turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()


y1 += 25

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()


radius -= 25
turtle.color("red")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

y1 += 25

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

radius -= 25
turtle.color("blue")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()


y1 += 25

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

radius -= 25
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()




turtle.hideturtle()
turtle.done()