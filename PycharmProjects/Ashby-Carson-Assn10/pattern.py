#Ashby-Carson-Assn10
#This is a program that draws shapes dependant on a user input
import turtle
import math
import random

def reset():
    turtle.clear()



def setup():
    turtle.showturtle()
    turtle.speed(10)
    turtle.setworldcoordinates(-500,-400,500,400)

#pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)#


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    drawTimes = 0
    theta = 0
    dTheta = (2*math.pi) / count

    while drawTimes < count:
        setRandomColor()
        drawTimes += 1
        xBar = offset * math.cos(theta)
        yBar = offset * math.sin(theta)
        turtle.penup()
        turtle.goto(centerX + xBar, centerY + yBar)
        turtle.pendown()
        drawRectangle(width, height, rotation)
        rotation += 360 / count
        theta += dTheta


def drawRectangle(width, height, rotation):
    turtle.seth(rotation)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)



def drawCirclePattern(centerX, centerY, offset, count, radius):
    drawTimes = 0
    theta = 0
    rotation = 0
    dTheta = (2*math.pi) / count

    while drawTimes < count:
        setRandomColor()
        drawTimes += 1
        xBar = offset * math.cos(theta)
        yBar = offset * math.sin(theta)
        turtle.penup()
        turtle.goto(centerX + xBar, centerY + yBar)
        turtle.pendown()
        drawCircle(radius, rotation)
        rotation += 360 / count
        theta += dTheta

def drawCircle(radius, rotation):
    turtle.seth(rotation)
    turtle.circle(radius)


def drawSuperPattern(num):
    runAmount = 0
    while runAmount < eval(num):
        whichShape = random.randint(0, 1)
        if whichShape == 0:
            centerX = random.randint(-500,500)
            centerY = random.randint(-400,400)
            offset = random.randint(-150,150)
            width = random.randint(-150,150)
            height = random.randint(-150,150)
            count = random.randint(1,50)
            rotation = random.randint(-150,150)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        else:
            centerX = random.randint(-500,500)
            centerY = random.randint(-400,400)
            offset = random.randint(-150,150)
            count = random.randint(1,50)
            radius = random.randint(-150,150)
            drawCirclePattern(centerX, centerY, offset, count, radius)
        runAmount += 1

def setRandomColor():
    randColor = random.randint(1,5)
    if randColor == 1:
        turtle.color("red")
    elif randColor == 2:
        turtle.color("blue")
    elif randColor == 3:
        turtle.color("green")
    elif randColor == 4:
        turtle.color("cyan")
    elif randColor == 5:
        turtle.color("purple")


def done():
    turtle.exitonclick()
