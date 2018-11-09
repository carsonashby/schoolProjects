


# must have, eight characters, only letters and digits, and at least two digits
# must not contain the word password or end with 123
 
from password import Password






def main():
    password = Password()
    userPassword = ""
    done = False
    while not done:
        print("This is a password checker")
        password.setPassword = str(input("Enter a password to be checked"))
        if password.isValid == True:
            print("That password is secure")
        else:
            password.getErrorMessage
        if str(input("Would you like to go again, Y/N")) == "Y":
            done = done
        else: done = True
















main()