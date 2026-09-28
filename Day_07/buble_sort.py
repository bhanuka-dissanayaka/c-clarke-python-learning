# Using While loop
numbers = [0,985,65,65,65,6,65,8,8,71,100,8]
swapped = True
while swapped:
    swapped = False
    for i in range(len(numbers)-1):
        print("Outer loop is Running")
        if numbers[i] > numbers[i+1]:
            numbers[i] , numbers[i+1] = numbers[i+1] , numbers[i]
            print("Inner loop is Running")
            swapped = True
print(numbers)
