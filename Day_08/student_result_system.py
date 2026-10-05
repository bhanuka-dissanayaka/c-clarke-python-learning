
def get_total(marks_list):
    total = 0
    for mark in marks_list:
        total+=mark
    return total

def get_average(list):
    avg = get_total(list) / len(list)
    return avg

def grade_calculator(list):
    avg_mark = get_average(list)
    if avg_mark >= 75:
        return "A"
    elif avg_mark >= 65:
        return  "B"
    elif avg_mark >= 55:
        return  "C"
    elif avg_mark >= 35:
        return  "S"
    else:
        return  "W"

print("""
Enter a option : 
1 - Enter marks
2 - Get total
3 - Get Average
4 - Get the grade
""")

marks_list = []
while True:
    print("""
Enter a option : 
1 - Enter marks
2 - Get total
3 - Get Average
4 - Get the grade
    """)
    user_option = int(input("Enter your option : "))
    if user_option == 0:
        break
    if user_option == 1 :
        mark = float(input("Enter marks of a subject : "))
        marks_list.append(mark)
    if user_option == 2 :
        print(f"{get_total(marks_list)}")
    if user_option == 3 :
        print(f"{get_average(marks_list)}")
    if user_option == 4:
        print(f"{grade_calculator(marks_list)}")
