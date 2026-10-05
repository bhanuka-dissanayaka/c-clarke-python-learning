def test_scope():
    y = 2
    global  x
    x = 2
    print(f"Value of z -{z}")
    print(f"Value of z -{x}")

z = 3
x = 1
test_scope()
print(x)

