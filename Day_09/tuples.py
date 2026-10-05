nums = (12,3,4,5)

# nums[0] = 12
# del nums[0]
nums2 = (2,3,4,5,6,7,8)


def get_numbers():
    x = 10
    y = 20
    return x,y  # Here returning a tuple

result = get_numbers()
print(result)

val1 , val2 = result # Value unpacking
print("Value one is", val1)


