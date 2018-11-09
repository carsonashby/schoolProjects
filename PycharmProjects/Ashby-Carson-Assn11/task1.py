import turtle
turtle.showturtle()
turtle.speed(10)








class Face:

    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True

    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def is_smile(self):
        return self.__smile

    def is_happy(self):
        return self.__happy

    def is_dark_eyes(self):
        return self.__dark_eyes

    def change_mouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def change_emotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def change_eyes(self):
        self.__dark_eyes = not self.__dark_eyes
        self.draw_face()

    def __draw_head(self):

        turtle.penup()
        turtle.width(1)
        turtle.goto(0, -100)
        turtle.pendown()
        turtle.seth(0)
        if self.__happy == True:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

    def __draw_eyes(self):
        turtle.penup()
        turtle.width(1)
        turtle.goto(25, 25)
        turtle.pendown()
        if self.__dark_eyes == True:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(-25, 25)
        turtle.pendown()
        if self.__dark_eyes == True:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()

    def __draw_mouth(self):
        turtle.penup()
        turtle.goto(-10, -25)
        turtle.pendown()
        turtle.pensize(15)
        if self.__smile == True:

            turtle.circle(125, 75)
        else:

            turtle.circle(-125, 75)
def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else "happy"
        eyes = "blue" if face.is_dark_eyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
