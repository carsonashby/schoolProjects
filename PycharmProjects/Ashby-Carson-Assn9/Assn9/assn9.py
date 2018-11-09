#Ashby-Carson-Assn9
#This is a program that draws a chessboard off of a user's input
#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startX, startY = eval(input("Enter starting X, and Y values: "))
    width = input("Enter width: ")
    height = input("Enter height: ")
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()