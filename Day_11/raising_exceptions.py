def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be less than zero")

    else:
        print(f"Your age is {age}")


try:
    age_input = int(input("Enter your age : "))
    check_age(age_input)

except ValueError as e:
    print("Invalid age Input")