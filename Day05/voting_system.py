age = int(input("Enter your age - "))
is_citizen = input("Are you a citizen of Sri Lanka(y/n) - ") == "yes"

if age > 18 and is_citizen:
    print("\nYou can vote for election")
else:
    print("\nYou can't vote for election")