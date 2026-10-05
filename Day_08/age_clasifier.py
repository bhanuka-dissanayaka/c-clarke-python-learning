def age_classifier(age=0):
    if age<13:
        return "child"
    elif age<19:
        return "Teen"
    elif age<19:
        return "Adult"
    else:
        return "senior citizen"

age = age_classifier(int(input("Enter Age : ")))
print(age_classifier(int(input("Enter Age : "))))