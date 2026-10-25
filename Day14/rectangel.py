class Rectangle:

    def __init__(self,height, length):
        self.__length = height
        self.__height = length

    def perimeter(self):
        perimeter = (self.__length + self.__height) * 2
        return perimeter

    def area(self):
        area = self.__length * self.__height
        return area


rectangle_1 = Rectangle(5,10)
print(rectangle_1.perimeter())
print(rectangle_1.area())