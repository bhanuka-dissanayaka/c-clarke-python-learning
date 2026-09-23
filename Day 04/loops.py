# x=0
# while x<5:
#     x=x+1
#     print(f"Value of x: {x}")

# i = True
# odd_count=0
# even_count=0
# while i:
#     num = float(input("Input the number: "))
#     if num == -1:
#         i=False
#         print(f"You entered {even_count} even numbers and {odd_count} odd numbers")
#     else:
#         if num % 2 == 0:
#             even_count = even_count + 1
#         else:
#             odd_count = odd_count + 1


# x = 0
# while x<10:
#     x+=1
#     if x==8:
#         continue
#     print(x)

# x = 0
# while x<10:
#     x+=1
#     if x==8:
#         break
#     print("Loop executing")
#     print(x)



## collatz hypothesis
# num = int(input("Enter the number : "))
# steps = 0
# while True:
#     if num<=0:
#         print("Invalid Number")
#         break
#     elif num == 1:
#         print(f"{steps} steps")
#         break
#     elif num % 2 == 0:
#         steps+=1
#         num = num//2
#         print(num)
#     else:
#         steps+=1
#         num = (num*3)+1
#         print(num)


# for i in range(10):
#     print(i)
#
# print(range(10))


# for i in range(10,0,-1):
#     print(i)
# print("Welcome!")
#
# x=10
# while x>0:
#     print(x)
#     x-=1
# print("Welcome!")


# PASSWORD = "5645"
# input_p = input("Enter the password : ")
# while input_p != PASSWORD:
#     input_p = input("Reenter the password : ")
# print("you entered the correct password")


# PASSWORD = "5645"
# count = 1
# input_p = input("Enter the password : ")
# while count<3:
#     if PASSWORD==input_p:
#         print("You have entered the correct password")
#         exit()
#     else:
#         input_p = input(f"Password incorrect you have more {3-count} chances : ")
#         count+=1
# print("You Got Lock")


# count = int(input("How many numbers do you want to compare? Enter: "))
# largest_num = float(input("Enter the number : "))
# for i in range(0,count-1,1):
#     num = float(input("Enter the number : "))
#     if num>largest_num:
#         largest_num = num
# print(f"The largest number is {largest_num}")

print("Welocome to AMarket")
product_count = int(input("How many products do you want to buy? "))
bill_total = 0

for i in range(0,product_count,1):
    name = input("Enter the product name : ")
    price = float(input("Input the product price : "))
    quntity = int(input("Enter the quantity : "))
    product_total_price = price*quntity
    bill_total = bill_total + product_total_price
    print(f"Name: {name} Quantity: {quntity} Price: {price} Total price for this product :{product_total_price}")

if bill_total>20000:
    discount = 20000*0.2
    bill_total_with_discount = bill_total - discount
elif bill_total>10000:
    discount = 20000*0.1
    bill_total_with_discount = bill_total - discount
else:
    discount = 0
    bill_total_with_discount = bill_total

payment_option = input("Enter a payment option cash/card:")
if payment_option=="cash":
    cash_amount = float(input("Enter Money Here"))
    balance = cash_amount - bill_total_with_discount
    print(f"Youre balance is {balance}")
elif payment_option=="card":
    discount += bill_total*0.03
    bill_total_with_discount =bill_total_with_discount-(bill_total*0.03)

print("")
print(f"""
Welcome to Kumara Store
Total price : {bill_total}
Discount : {discount}
Total with Discount : {bill_total_with_discount}
Thank you for shop with us. Come Again!
""")




