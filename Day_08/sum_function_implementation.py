def summation(num_list):
    total = 0
    for i in num_list:
        total+=i
    return  total

print(summation([1,2,3,4,5]))


def grade_calculator(mark):
    if mark >= 75:
        return "A"
    elif mark >= 65:
        return  "B"
    elif mark >= 55:
        return  "C"
    elif mark >= 35:
        return  "S"
    else:
        return  "W"

def area_calculator(length,width):
    return length*width

print(f"Your Grade is {grade_calculator(85)}")
print(f"Area is {area_calculator(10,20)}")