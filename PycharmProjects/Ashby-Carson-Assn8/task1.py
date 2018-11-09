#Ashby-Carson-Assn8-task1
#This is a program that finds the four perfect numbers before 10000
perfectNumbers = 0
count = 0
testNumber = 0
while perfectNumbers < 4:
    testNumber += 1
    divisorSum = 0
    divisor = 1
    while divisor < testNumber**.5:
        count += 1
        if testNumber % divisor == 0:
            divisorSum += divisor
            if divisor != testNumber/divisor:
                divisorSum += testNumber/divisor

        divisor += 1
    if divisorSum / 2 == testNumber:
        perfectNumbers += 1
        print(testNumber)


print(count)
