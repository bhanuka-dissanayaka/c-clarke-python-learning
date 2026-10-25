class Animal:

    def __init__(self,name,color):
        self.name = name
        self.color = color

    def eat(self):
        print(f"Animal - {self.name} is eating")

    def sleep(self):
        print(f"Animal - {self.name} is sleeping")

class Mammal(Animal):

    def __init__(self,name,color,breed):
        super().__init__(name,color)
        self.breed = breed

    def drinking_milk(self):
        print(f"Animal - {self.name} with breed - {self.breed} is drinking milk.")

class Dog(Mammal):

    def __init__(self,color,breed,is_domesticated):
        super().__init__("Canis lupus familiaris",color,breed)
        self.is_domesticated = is_domesticated

dog = Dog("brown", "German Shephard", True)
