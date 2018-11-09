#Ashby-Carson-Assn11
#This is a program that emulates a bank account.

from account import Account


def main():
    account = Account()
    account.begin_input()
    done = False
    while not done:
        account.monthly_rate = account.getAnnualInterestRate() / 12
        account.interest = (account.monthly_rate) * account.getBalance()

        print("1): Display ID")
        print("2): Display Balance")
        print("3): Display Annual Interest Rate")
        print("4): Display Monthly Interest Rate")
        print("5): Display Monthly Interest")
        print("6): Withdraw Money")
        print("7): Deposit Money")
        print("8): Exit")
        menu = input("Enter a selection: ")


        if menu == "1":
                account.getID()
        elif menu == "2":
                account.printBalance()
        elif menu == "3":
                account.printAnnualInterestRate()
        elif menu == "4":
                account.getMonthlyInterestRate()
        elif menu == "5":
                account.getMonthlyInterest()
        elif menu == "6":
                account.withdrawMoney(float(input("How much? ")))
        elif menu == "7":
                account.depositMoney(float(input("How much? ")))
        elif menu == "8":
            break
        else:
            print("That is not a valid selection.")

    print("Thanks for playing!")





main()