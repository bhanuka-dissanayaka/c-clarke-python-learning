is_member = input("Are you a member (y/n) - ") == "y"
is_using_coupon = input("Are you using coupon (y/n) - ") == "y"
bill_value = int(input("Your bill amount - "))
have_vegetables = input("Are you buying vegetables (y/n) - ") == "y"

if is_member and (not is_using_coupon) and bill_value > 5E3 and (not have_vegetables):
    print("\nYou get 20% Discount")
    discount = bill_value * 0.2
    print(f"Total amount - LKR {bill_value - discount}")
else:
    print("\nNo Discount")
    print(f"Total amount - LKR {bill_value}")