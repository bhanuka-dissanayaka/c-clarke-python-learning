from dataclasses import dataclass, field
from datetime import datetime
from typing import List


class SuperMarketError(Exception):
    pass

@dataclass
class Product:

    product_id:str
    name:str
    price:float
    quantity:int

    def is_available(self) -> bool:

        return self.quantity > 0

    def reduce_quantity(self, amount: int):

        if amount > self.quantity:
            raise SuperMarketError(f"Amount is greater than qty - {self.quantity}")

        self.quantity -= amount

    def add_quantity(self, amount):

        if amount < 0:
            raise SuperMarketError("Amount can't be negative")

        self.quantity += amount


@dataclass
class Customer:

    customer_id:str
    name:str
    email:str
    phone_no:str

@dataclass
class OrderItem:

    product_id:str
    product_name:str
    quantity:int
    unit_price:float

    def total_price(self):

        return self.quantity * self.unit_price

@dataclass
class Order:

    order_id:str
    customer_id:str
    customer_name:str
    created_at: datetime = field(default=datetime.now())
    items: List[OrderItem] = field(default_factory=list)

    def add_item(self, item: OrderItem) -> None:

        self.items.append(item)

    def total_price(self):
        total = 0

        if len(self.items) == 0:
            raise SuperMarketError("\nNo items in items list")

        for item in self.items:

            total += item.total_price()

        return total

    def item_count(self):

        return len(self.items)


if __name__ == "__main__":
    item1 = OrderItem(product_id="P001", product_name="CocaCola", quantity=2, unit_price=200)

    order1 = Order(order_id="O001", customer_id="C001", customer_name="Amal")

    print(order1.total_price())
    print(order1.items)