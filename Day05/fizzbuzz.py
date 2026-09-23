for i in range(1,21,1):
    if i % 5 == 0  and i % 3 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")