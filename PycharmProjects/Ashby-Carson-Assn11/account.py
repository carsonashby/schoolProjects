

class Account:
    def __init__(self):
        self.__id = ""
        self.__balance = 0
        self.__annual_rate = 0
        self.monthly_rate = 0
        self.interest = 0




    def begin_input(self):
        print("Enter account information")
        self.__id = input("ID: ")

        self.__balance = eval(input("Balance: "))
        while self.__balance < 0:
            self.__balance = eval(input("Please reenter your balance: "))

        self.__annual_rate = eval(input("Annual interest rate, cannot be higher than 10%: "))
        self.__annual_rate /= 100
        while self.__annual_rate >= .1 or self.__annual_rate < 0:
            self.__annual_rate = eval(input("Please reenter your annual interest rate: "))

    def getID(self):
        print(self.__id)
        return self.__id

    def getBalance(self):
        return self.__balance
    def printBalance(self):
        print(self.__balance)
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annual_rate
    def printAnnualInterestRate(self):
        print(self.__annual_rate)
        return self.__annual_rate

    def getMonthlyInterestRate(self):
        print(self.monthly_rate)
        return self.monthly_rate

    def getMonthlyInterest(self):
        print(self.interest)
        return self.interest

    def withdrawMoney(self, value):
        self.__balance -= value
        print("New balance", self.__balance)

    def depositMoney(self, value):
        self.__balance += value
        print("New balance", self.__balance)
