username = "user"
password = "1234"

is_logged = input("Have you logged before (y/n) - ") == "y"

for i in range(3):
    if not is_logged:
        print("\nPlease Login First!")
        user_name = input("Enter Your Username - ") == username
        user_password = input("Enter Your Password - ") == password

        if user_name and user_password:
            is_logged = True
            print("\nLogin Successful! Welcome admin")
        else:
            print("\nInvalid username and password")
    else:
        print("\nWelcome Back")
        break
else:
    print("Your Account is Locked. Please Contact Support.")