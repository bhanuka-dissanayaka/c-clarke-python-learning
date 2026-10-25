

def email_validator(email):
    if email.startswith("@")  or email.endswith("@")  or email.count("@") != 1 or email.lower():
        print("\nInvalid Email ❗")

    else:
        print("\nValid Email ✅")


if __name__ == "__main__":
    user_email = input("Enter email : ")
    email_validator(email=user_email)