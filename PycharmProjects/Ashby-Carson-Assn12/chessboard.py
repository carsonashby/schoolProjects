#Ashby-Carson-Assn12



class Chessboard:
    def __init__(self, x, y, width , height):
        self.width = 125
        self.height = 125
        self.chessboardInfo = x, y, width, height



    def draw(self, chessboardInfo):
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
        __drawAllRectangles(x, y, width, height)
        turtle.hideturtle()
        turtle.done()

    def __drawAllRectangles(self, x, y, width, height):
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
                turtle.goto(x, y + gotoHeight + height)
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
                turtle.goto(x, y + gotoHeight + height)
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

