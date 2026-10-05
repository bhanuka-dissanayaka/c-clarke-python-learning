students = []
ages = []
marks = []


# Calculate Grade
def calculate_grade(mark):
    if mark >= 75:
        return "A"
    elif mark >= 65:
        return "B"
    elif mark >= 55:
        return "C"
    elif mark >= 35:
        return "S"
    else:
        return "F"


# Add Student
def add_student():
    name = input("Enter student name: ")
    if name == "":
        print("Student name cannot be empty.")
        return
    age = int(input("Enter age: "))
    if age <= 0:
        print("Age must be greater than 0.")
        return
    mark = int(input("Enter marks: "))
    if mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        return

    students.append(name)
    ages.append(age)
    marks.append(mark)

    print("Student added successfully!")


# View Students
def view_students():
    if len(students) == 0:
        print("No students available.")
        return

    print("\n====== STUDENT LIST ======")
    for i in range(len(students)):
        print("\n", i + 1, ".", students[i])
        print("Age   :", ages[i])
        print("Marks :", marks[i])


# Search Student
# def search_student():
#     name = input("Enter student's name: ")
#     found = False
#     for i in range(len(students)):
#         if students[i].lower() == name.lower():
#             print("\n====== STUDENT FOUND ======")
#             print("Name  :", students[i])
#             print("Age   :", ages[i])
#             print("Marks :", marks[i])
#             found = True
#
#     if found == False:
#         print("Student not found.")

def search_student():
    name = input("Enter student's name: ")
    if name in students:
        index = students.index(name)
        print("\n====== STUDENT FOUND ======")
        print("Name  :", students[index])
        print("Age   :", ages[index])
        print("Marks :", marks[index])
    else:
        print("Student not found.")

# Calculate Results
def calculate_results():
    if len(students) == 0:
        print("No students available.")
        return

    print("\n====== RESULTS ======")

    for i in range(len(students)):
        grade = calculate_grade(marks[i])

        if marks[i] >= 35:
            result = "Pass"
        else:
            result = "Fail"

        print("\n", students[i])
        print("Marks  :", marks[i])
        print("Grade  :", grade)
        print("Result :", result)


# Show Statistics
def show_statistics():
    if len(students) == 0:
        print("No students available.")
        return

    total_students = len(students)
    highest_marks = max(marks)
    lowest_marks = min(marks)
    average_marks = sum(marks) / len(marks)

    passed_students = 0
    failed_students = 0

    for mark in marks:
        if mark >= 35:
            passed_students += 1
        else:
            failed_students += 1

    print("\n====== STATISTICS ======")
    print("Total students  :", total_students)
    print("Highest marks   :", highest_marks)
    print("Lowest marks    :", lowest_marks)
    print("Average marks   :", average_marks)
    print("Passed students :", passed_students)
    print("Failed students :", failed_students)


# Main Menu
while True:

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Results")
    print("5. Show Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_results()

    elif choice == "5":
        show_statistics()

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
