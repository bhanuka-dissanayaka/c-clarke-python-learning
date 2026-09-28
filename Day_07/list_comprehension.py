numbers = []
for i in range(10):
    numbers.append(i)

# Same thing using list comprehension
nums = [i for i in range(10)]
print(f"Using list comprehension {nums}")

nums_10 = [i*10 for i in range(10)]
print(nums_10)

hello_list = ["Hello" for i in range(10)]
print(hello_list)

even_numbers = [i for i in range(10) if i % 2 == 0]
print(f"Even Number list: {even_numbers}")
