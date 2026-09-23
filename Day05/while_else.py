i = int(input("Enter the number - "))

while i < 10:
    print(i)
    i += 1
    if i == 5:
        break
else:
    print(i)
    print("Executing else block")
