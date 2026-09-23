value = int(input("Item value - "))
member_status = input("Are you a member (y/n) - ") == "yes"

if value > 5E3 and member_status:
    print("You get a free delivery")
else:
    print("You didn't get a free delivery")