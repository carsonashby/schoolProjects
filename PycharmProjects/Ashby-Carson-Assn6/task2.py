#Ashby-Carson-Assn6-task2
#This program will take input from a user in order to print a full payroll stub for them.





payName = input("Enter employee's name: ")
payHours = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
payFedTaxRate = eval(input("Enter federal tax witholding rate(ex. 0.16): "))
payStateTaxRate = eval(input("Enter state tax witholding rate (ex. 0.10): "))

payAmount = payRate * payHours
payFedTax = payAmount * payFedTaxRate
payStateTax = payAmount * payStateTaxRate
payDeduction = payStateTax + payFedTax
payActualAmount = payAmount - (payStateTax + payFedTax)


print(payName.upper(), "PAY INFORMATION")

print(format("Pay", ">10"))
print(format("Hours worked:  ",  ">40"), payHours)
print(format("Pay Rate: $",">40"), payRate)
print(format("Gross Pay: $", ">40"), payAmount)

print(format("Deductions", ">15"))
print("Federal withholding", "(",format(payFedTaxRate * 100, ">40"),"%): $",  payFedTax)
print("State withholding", "(",format(payStateTaxRate * 100, ">40"),"%): $", payStateTax)
print(format("Total Deduction: $", ">40"), payDeduction)

print(format("Net Pay: $", ">40"), payActualAmount)
