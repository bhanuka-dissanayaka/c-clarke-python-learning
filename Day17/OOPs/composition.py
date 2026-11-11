class Engine:
    def __init__(self, horsepower:int, capacity: str):
        self.horsepower = horsepower
        self.capacity = capacity

    def start(self):
        print(f"Engine with horsepower - {self.horsepower} is starting")

class Car:
    def __init__(self , model:str, engine:Engine):
        self.engine = engine
        self.model = model

    def print_car_details(self):
        print(f"car model - {self.model} | capacity - {self.engine.capacity}")

engine1 = Engine(600 , "2000")
car1 = Car("Gtr" , engine1)
print("Capacity", car1.engine.capacity)
car1.print_car_details()