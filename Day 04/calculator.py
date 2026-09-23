num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))
operator = input("Enter the operator (-+ - / *): ")

if operator=="+":
    answer = num1+num2
    print(answer)
elif operator=="-":
    answer = num1-num2
    print(answer)
elif operator=="/":
    if num2!=0:
        answer = num1 / num2
        print(answer)
    else:
        print("Can not divide from zero")
elif operator=="*":
    answer = num1*num2
    print(answer)
else:
    print("Invalid operator")


