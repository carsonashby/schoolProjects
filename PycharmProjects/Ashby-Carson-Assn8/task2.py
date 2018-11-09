#Ashby-Carson-Assn8-Task2
#this is a program that simulates the Monty hall problem 100,000 times based on a users input
import random

playGame = 1
count = 0
successes = 0
failures = 1
userDoor = 0
while playGame == 1:
    carDoor = random.randint(1, 3)
    userChoice = random.randint(0, 1)
    if carDoor == 1 and userChoice == 0: userDoor = 0
    if carDoor == 1 and userChoice == 1: userDoor = 1
    if carDoor == 2 and userChoice == 0: userDoor = 0
    if carDoor == 2 and userChoice == 1: userDoor = 2
    if carDoor == 3 and userChoice == 0: userDoor = 0
    if carDoor == 3 and userChoice == 1: userDoor = 3
    print("Welcome to the random goat door gameshow, where there are three doors and you have a 1/3 chance of winning a new car!")
    print("Your pick and the door the car is behind will be randomly selected, and you will have a choice to change the door you are on!")
    print("The host reveals that a door has a goat behind it!")
    print(carDoor)
    print(userDoor)
    userSwitch = input("The host gives you the option to change the door you have chosen, do you change? (Y/N)")
    successes = 0
    count = 0
    while count < 100000:
        count += 1
        carDoor = random.randint(1, 3)
        userChoice = random.randint(1, 3)
        if userSwitch == 'Y' or userSwitch == 'y' and userChoice == carDoor: failures += 1
        elif userSwitch == 'Y' or userSwitch == 'y' and userChoice != carDoor: successes += 1
        elif userChoice == carDoor: successes += 1
        else: failures += 1
    print("You won", successes, "times")
    print("Your win percent was", ((successes / count)*100), "percent")
    playAgain = input("Play again? (Y/N)")
    if playAgain == "y" or playAgain == "Y": playGame = 1
    else: break

print("The game is over.")