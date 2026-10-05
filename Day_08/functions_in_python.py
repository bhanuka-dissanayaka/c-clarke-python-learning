from fontTools.misc.cython import returns


def hello_world():
    for i in range(10):
        print("Hello World")
hello_world()

def print_full_name(first_name,second_name):
    print(f"My First Name is {first_name} and second name is {second_name}")

print_full_name("Bhanuka", "Dilshara") # Positional argument passing
print_full_name(first_name="Bhanuka" , second_name="Dilshara") # Keyword argument passing

def multiply(a,b):
    print(f"Multiplying 0 {a} and {b}")
    return a*b
result = multiply(2,5)
print(result)