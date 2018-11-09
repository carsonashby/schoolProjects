import turtle

defaultWidth, defaultHeight = 125, 125


def drawChessboard(x, y, width=defaultWidth, height=defaultHeight):
    turtle.showturtle()
    turtle.speed(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    drawAllRectangles(x, y, width, height)
    turtle.hideturtle()
    turtle.done()


def drawAllRectangles(x, y, width=defaultWidth, height=defaultHeight):
    width /= 8
    height /= 8
    count = 0
    moveUp = 0
    gotoHeight = height
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
    while count < 16:
        if moveUp == 1:
            turtle.goto(x,y + gotoHeight + height )
            gotoHeight += height * 2
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.end_fill()
        turtle.seth(0)
        turtle.penup()
        turtle.forward(width * 2)
        count += 1
        if count % 4 == 0:
            moveUp = 1
        else:
            moveUp = 0
    count = 0
    moveUp = 0
    gotoHeight = height
    x += width
    y += height
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(0)
    while count < 16:
        if moveUp == 1:
            turtle.goto(x,y + gotoHeight + height )
            gotoHeight += height * 2
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.end_fill()
        turtle.seth(0)
        turtle.penup()
        turtle.forward(width * 2)

        count += 1
        if count % 4 == 0:
            moveUp = 1
        else:
            moveUp = 0



