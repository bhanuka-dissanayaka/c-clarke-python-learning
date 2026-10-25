class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

        print(f"{self.name} | {self.age}")

kaveesha = Student("kaveesha", "18")
gayan = Student("gayan","20")

kaveesha.age = 22
print(kaveesha.name)