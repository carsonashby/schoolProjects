#Ashby-Carson-Assn7
#This is a program that plays rock paper scissors versus a user using randomly generated computer plays.

import random

userPlay = eval(input("Enter your move, (scissor(0), rock(1) or paper(2)): "))
comPlay = random.randint(0,2)




print("The computer plays", comPlay)

if comPlay == userPlay:
    print("It's a draw")

elif userPlay > comPlay:
    print("You win!")
elif userPlay == 0:
    if comPlay == 2: print("You win!")
elif userPlay < comPlay:
    print("You lose")



