from typing import List

class Student:
    def __init__(self, student_id: str, name:str, age:int  ):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades: List[int] = []

    def __eq__(self, other : object):
        return self.student_id == other.student_id


std1 = Student("S001", "Bhanuka" , 21)
std2 = Student("S001", "Bhanuka" , 21)

if std1 == std2:
    print("They are equal")   # They are equal because we override the __eq__ method to compare the student ids.
    print(std1==std2)
else:
    print("They are not equal")
    print(std1==std2)

print(std1.__eq__(std2))