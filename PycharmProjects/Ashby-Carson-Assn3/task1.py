#Ashby-Carson-Assn4
#This is a program that draws a snowman step by step.


import turtle

turtle.showturtle()
turtle.speed(9)

#first two circles
turtle.circle(25)
turtle.goto(0,0)
turtle.left(180)
turtle.circle(50)


#moving to third circle starting position
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(75)

turtle.penup()
turtle.goto(7, 32)
turtle.pendown()

#Eyes
turtle.color("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(-7,32)
turtle.pendown()


turtle.color("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
#Smile
turtle.penup()
turtle.goto(-10, 13)
turtle.pendown()
turtle.left(165)
turtle.circle(50, 45)

#Hat
turtle.penup()
turtle.goto(0,50)
turtle.pendown()

turtle.seth(0)
turtle.forward(150)
turtle.left(180)
turtle.forward(300)
turtle.left(180)
turtle.forward(75)
turtle.left(90)

turtle.color("blue")
turtle.begin_fill()
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()
turtle.color("black")

turtle.penup()
turtle.goto(-35,-25)
turtle.pendown()
#left arm


turtle.seth(200)
turtle.forward(50)
turtle.right(15)
turtle.forward(20)
turtle.backward(20)
turtle.left(15)
turtle.forward(20)
turtle.backward(20)
turtle.left(15)
turtle.forward(20)
turtle.backward(20)

turtle.penup()
turtle.goto(35,-25)
turtle.pendown()

#right arm

turtle.seth(-20)
turtle.forward(50)
turtle.right(15)
turtle.forward(20)
turtle.backward(20)
turtle.left(15)
turtle.forward(20)
turtle.backward(20)
turtle.left(15)
turtle.forward(20)
turtle.backward(20)


turtle.penup()
turtle.goto(-15,-25)
turtle.pendown()

#buttons

turtle.seth(270)
turtle.color("red")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.seth(270)
turtle.forward(30)
turtle.pendown()

turtle.color("green")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.seth(270)
turtle.forward(30)
turtle.pendown()

turtle.color("orange")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()


turtle.done()

