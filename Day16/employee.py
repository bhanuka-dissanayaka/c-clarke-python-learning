class Employee:
    def __init__(self, name, position , base_salary):
        self.__name = name
        self.__position = position
        self.__base_salary = base_salary

    def calculate_salary(self) -> float:
        return self.__base_salary

class Manager(Employee):
    def __init__(self, name, position , base_salary , bonus):
        super().__init__(name,position,base_salary)
        self.__bonus = bonus

    def calculate_salary(self) -> float:
        return self.__base_salary +  self.__bonus

class Developer(Employee):
    def __init__(self, name, position , base_salary , overtime):
        super().__init__(name,position,base_salary)
        self.__overtime = overtime

    def calculate_salary(self) -> float:
        return self.__base_salary
