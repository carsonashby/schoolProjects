#Ashby-Carson-Assn4
#This is a calculator that takes user inputs and generates outputs.



print("Welcome to the Cuboid Calculator")

print("Please enter values in feet")

length = input("Enter the length ")

width = input("Enter the width ")

height = input("Enter the height ")



volume = (int(length) * int(width) * int(height))

surfaceArea = (int(length)*int(width)*2+int(height)*int(width)*2+int(length)*int(height)*2)

print("Your", length, "X", width, "X", height, "cuboid has a volume  of", volume, "and a surface area of ", surfaceArea)

