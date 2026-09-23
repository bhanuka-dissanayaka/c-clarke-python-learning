# # password = "test@1996"
# # username ="test"
# # username_input = input("Enter your Username - ")
# #
# # if username==username_input:
# #     print("Username is correct ")
# #     password_input = input("Enter your password - ")
# #     if password==password_input:
# #         print("Your password is correct")
# #         print("""
# #         Welocome to our secret game
# #         1) press 1 to start the game
# #         """)
# #         user_input = input("Choice: ")
# #         if user_input=="1":
# #             print("Snake Game is loading.....")
# #     else:
# #         print("Entered Password is incorrect")
# # else:
#     print("Incorrect username")

# -------------------------------------------------------------------------------------------------

# num1 = int(input("Enter number one: "))
# num2 = int(input("Enter number two: "))
# if num1>num2:
#     print(f"First Number - {num1} is grater that second number")
# # elif num2>num1:
# #     print(f"Second Number - {num2} is grater that First number")
# else:
#     if num2>num1:
#         print(f"Second Number - {num2} is grater that First number")
#     else:
#         print("Numbers are equal")

# -------------------------------------------------------------------------------------------------

# min_height = 1.2
# input_height = float(input("Enter your height: "))
#
# if input_height < min_height:
#     print("You are not elligible")
# else:
#     age = int(input("Enter Your Age: "))
#     if age < 18:
#         discount = (1000/100)*20
#     elif age> 55:
#         discount = (1000/100)*50
#     else:
#         discount = 0
#     ticket_price = 1000-discount
#     print("Ticket Price is: ",ticket_price)

# -------------------------------------------------------------------------------------------------

# Tax Calculator

# monthly_tax = float(input("Enter Your Monthly salary"))
# relife_treshold = 1800000
# tax = 0
#
# anual_salary = monthly_tax*12
#
# if anual_salary<1800000:
#     print("You have no tax")
# else:
#     taxable_amount = anual_salary - relife_treshold
#     if taxable_amount>1000000:
#         tax = 1000000*(6/100)
#         remaining_taxable_amount = taxable_amount- 1000000
#         if remaining_taxable_amount>500000:
#             tax=tax+(500000*(18/100))
#             remaining_taxable_amount = remaining_taxable_amount - 500000
#             if remaining_taxable_amount > 500000:
#                 tax = tax + (500000 * (24 / 100))
#                 remaining_taxable_amount = remaining_taxable_amount - 500000
#                 if remaining_taxable_amount > 500000:
#                     tax = tax + (500000 * (30 / 100))
#                     remaining_taxable_amount = remaining_taxable_amount - 500000
#                     if remaining_taxable_amount > 0:
#                         tax = tax + ( remaining_taxable_amount* (36 / 100))
#                 else:
#                     tax = tax + (remaining_taxable_amount * (30 / 100))
#             else:
#                 tax = tax + (remaining_taxable_amount * (24 / 100))
#
#         else:
#             tax = tax+(remaining_taxable_amount*(18/100))
#     else:
#         tax = taxable_amount*(6/100)
#
# print("your Anual tax is", tax)
# print("your Monthly tax is", tax/12)


# -------------------------------------------------------------------------------------------------

# num = float(input("Enter the number"))
# if num==0:
#     print("Number is Zero")
# elif num>0:
#     print("Number is Positive")
# else:
#     print("Number is Negative")


# -------------------------------------------------------------------------------------------------

# marks_maths = float(input("Enter marks of Maths"))
# marks_science = float(input("Enter marks of science"))
# marks_ict = float(input("Enter marks of ict"))
# marks_stats = float(input("Enter marks of stats"))
# marks_database = float(input("Enter marks of database"))
# avg = (marks_maths+marks_science+marks_ict+marks_stats+marks_database)/5
#
# if avg>75:
#     print("You got A grade: ")
# elif avg>65:
#     print("You got B grade: ")
# elif avg>55:
#     print("You got C grade: ")
# elif avg>35:
#     print("You got S grade: ")
# else:
#     print("Repeat. Please try again")
#
# print("avarage is",avg)

# -------------------------------------------------------------------------------------------------

# age = int(input("Enter Your AGe: "))
# if  age>18:
#     liecense_status = input("DO you have a Driving lisence yes/no: ")
#     if  liecense_status=="yes":
#         print("You can drive")
#     else:
#         print("You can not drive")
# else:
#     print("You can not drive")

# -------------------------------------------------------------------------------------------------

acc_balance = 500000
INTEREST = 10
PIN = "123"

input_pin  = input("Enter Your Pin: ")
if input_pin != PIN:
    print("Incorrect pin. Retry")
else:
    print("""
        Welcome to ABC ATM. Enter a option.
        Check balance:1, Withdraw:2, Deposit:3
    """)
    option = input("option: ")
    if option == "1":
        print(f"Your balance is {acc_balance}")
    elif option == "2":
        withdraw_amount = int(input("Enter amount to withdraw"))
        if withdraw_amount<acc_balance:
            acc_balance = acc_balance - withdraw_amount
            print(f"You withdraw Rs {withdraw_amount} and current balance is {acc_balance}")
        else:
            print("Insufficient balance in your account")
    elif option == "3":
        deposit_amount = int(input("Enter amount to Deposit"))
        deposit_amount_with_interest = deposit_amount +(deposit_amount*(INTEREST/100))
        acc_balance = acc_balance + deposit_amount_with_interest
        print(f"You Deposit Rs {deposit_amount} and current balance is {acc_balance}")


# -------------------------------------------------------------------------------------------------
