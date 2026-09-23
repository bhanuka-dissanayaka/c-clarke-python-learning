maths = int(input("Enter Maths marks - ")) > 65
science = int(input("Enter Science marks - ")) > 65
english = int(input("Enter English marks - ")) > 65
ict = int(input("Enter ICT marks - ")) > 65

if maths and science and english or ict:
    print("\nYou are eligible")
else:
    print("\nYou are not eligible")