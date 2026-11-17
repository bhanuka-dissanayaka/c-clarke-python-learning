def hello():
    print("Hello")
    return hello()

# hello()

def countdown(n):
    print(n)
    if n==0:
        return None
    return countdown(n-1-0)

countdown(5)


def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

print(sum(3))


def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(f"factorial: {factorial(5)}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print("fib", fibonacci(5))