def addition(a,b):
    return a+b
def substraction(a,b):
    return  a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b == 0:
        return "can not divide from 0"
    else:
        return a/b
def get_inputs():
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 :"))
    return  num1,num2

while True:


    operator = input("Enter A Operator : ")
    answer = 0

    if operator == "+":
        num1,num2 = get_inputs()
        answer = addition(num1, num2)
    elif operator == "-":
        num1,num2 = get_inputs()
        answer = substraction(num1, num2)
    elif operator == "*":
        num1,num2 = get_inputs()
        answer = multiply(num1, num2)
    elif operator == "/":
        num1,num2 = get_inputs()
        answer = division(num1, num2)
    else:
        print("Invalid Operator")
    print(answer)

