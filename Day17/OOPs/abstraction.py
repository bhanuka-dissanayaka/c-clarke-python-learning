from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def calculate_area(self)-> float:
        pass

class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius
    def calculate_area(self) -> float:
        return 3.14 * self.radius **2

class Rectangle(Shape):
    def __init__(self, height:float, width:float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

shapes : List[Shape] = []

rect = Rectangle(22,10)
circle = Circle(7)

shapes.append(rect)
shapes.append(circle)

for shape in shapes:
    print(f"Area is - {shape.calculate_area()}")
