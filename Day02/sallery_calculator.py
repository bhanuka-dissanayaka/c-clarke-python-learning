#an employee has basic salary of 100,000 and receive bonus of 15,000
#the employee must pay 12.5% on their gross salary.
#calculate gross salary , tax amount, take home salary.


salary = int(input("Enter your basic salary - "))
bonus = 15000
gross_salary = salary + bonus
tax = 12.5
tax_amount = gross_salary * 12.5 /100

print(f"Your Gross Salary is - {gross_salary} "
      f"\nTax amount you have to pay - {tax_amount}"
      f"\nYour take home salary - {gross_salary - tax_amount}" )