pi = 3.14

def add(a,b):
    return a + b

def calculate_circumference_of_a_circle(radius):
    return 2 * pi * radius

def calculate_circle_area(radius):
    return pi * radius ** 2


if __name__ == "__main__":
    print("running from calculator")
    print(calculate_circle_area(20))
    print(__name__)#Dunder Variable/ Double Underscore variable
    #Name variable changes according to how the underscore variable
    #it will be __mail__ if run directly or name of the file
    #if been imported as a module