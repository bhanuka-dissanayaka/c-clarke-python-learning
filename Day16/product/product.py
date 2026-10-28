class Product:
    def __init__(self, name, price , quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def display_prodycts(self):
        return self.__name,self.__price,self.__quantity

    def sell(self) -> None:
        if self.__quantity <= 0:
            print("Out of stock")
            return
        self.__quantity -= 1
        print("Product sold successfully")


product1 = Product(name="Buscuits", price=1500 , quantity=100)
name , price , quantity = product1.display_prodycts()
print(f"name - {name} | price - Rs.{price} | quantity - {quantity}")