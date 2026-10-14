try:
    user_input = int(input("Enter a number : "))
    print(user_input + "test")
except ValueError as e: #handling an exception gracefully
    print(f"Invalid user input : {str(e)}")
except TypeError: #Catching the most specific exception
    print("Type error occurred")

finally:
    print("\nFinal block is executed")

try:
    integer_input = int(input("Enter an Integer - "))
except (TypeError,ValueError) as e: # Handling multiple exceptions in a single catch block
    print("Type error occurred")
except Exception as e:
    print(f"{str(e)}")

print("\nHello World")