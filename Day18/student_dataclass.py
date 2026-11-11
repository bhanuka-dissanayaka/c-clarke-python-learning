from dataclasses import dataclass, field
from typing import List, ClassVar


@dataclass
class Student:

    student_count: ClassVar[int] = 0 #Defining a class variable in dataclass

    __name:str
    age:int
    student_id:str
    grades: List[int] = field(default_factory=list)

    def get_average(self) -> float:

        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    student1 = Student("Amal", age=22, grades=[50, 60, 70], student_id="S001")
    student2 = Student("Amal", age=22, grades=[50, 60, 70], student_id="S001")
    print(student1)
    print(student1.age)
    print(Student.student_count)

    if student1 == student2:
        print("Same")
    else:
        print("not same")