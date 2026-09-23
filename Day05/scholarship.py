average = float(input("Enter average - "))
attendance = int(input("Enter attendance - "))
income = int(input("Enter your income - "))
achievements = input("Do you have achievements (y/n) - ")

if average > 75.0 and attendance > 80 and income < 1E5 or achievements == "y":
    if average > 90.0:
        print("You have 100% scholarship")
    elif average > 80.0:
        print("You have 75% scholarship")
    else:
        print("You have 50% scholarship")
else:
    print("\nYou are not eligible for scholarship")