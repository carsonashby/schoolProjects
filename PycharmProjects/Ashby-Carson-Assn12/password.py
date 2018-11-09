




class Password:

    def __init__(self):
        self.userPassword = ""
        self.errorMessage = ""


    def setPassword(self, userPassword):
        userPassword = userPassword


    def isValid(self, userPassword):
        len(userPassword) >= 8
        isDigits = userpassword[0, len(userPassword)]
        if isDigits

    def getErrorMessage(self):
        self.errorMessage = "must have at least eight characters, only letters and digits, and at least two digits, must not contain the word password or end with 123"

