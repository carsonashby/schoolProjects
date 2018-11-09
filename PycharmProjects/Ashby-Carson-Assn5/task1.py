#Ashby-Carson-Assn5
#This is a file that calculates total investment gain by user inputed values.



investAmount = eval(input("Enter investment amount: "))
investRate = eval(input("Enter annual interest rate: "))
investYears = eval(input("Enter number of years: "))


investTotal = (investAmount * ((1+ (investRate / 100)))** (investYears / 12))

investTotal = int(investTotal * 100)/ 100


print ("Total accumulated value is: ", investTotal)


