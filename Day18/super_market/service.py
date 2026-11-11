from dataclasses import dataclass
from typing import Optional, List

from Day18.super_market.models import SuperMarketError, Product, Customer, Order
from Day18.super_market.repositories import ProductRepository, CustomerRepository, OrderRepository, \
    InMemoryCustomerRepository, InMemoryProductRepository, InMemoryOrderRepository


@dataclass
class SuperMarketService:

    product_repository: ProductRepository
    customer_repository: CustomerRepository
    order_repository: OrderRepository

    def add_product(self, prod_id: str, name: str, price: float, quantity: int) -> Product:

        if self.product_repository.get_by_id(product_id=prod_id) is not None:
            raise SuperMarketError("Product already exists")

        if quantity < 0:
            raise SuperMarketError("Quantity cannot be less than zero")

        if price < 0:
            raise SuperMarketError("Price cannot be less than zero")

        product = Product(product_id=prod_id,name=name,price=price,quantity=quantity)
        self.product_repository.add_product(product)

        return product

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        if self.product_repository.get_by_id(product_id=product_id) is None:
            raise SuperMarketError(f"No product related to {product_id} this product id")

        return self.product_repository.get_by_id(product_id=product_id)

    def list_all_products(self) -> List[Product]:
        if len(self.product_repository.list_all_products()) == 0:
            raise SuperMarketError("No products in the list")

        return self.product_repository.list_all_products()

    def update_product(self, prod_id: str, name: str, price: float, quantity: int) -> Product:
        if self.product_repository.get_by_id(product_id=prod_id) is None:
            raise SuperMarketError("No Product exists")

        if quantity < 0:
            raise SuperMarketError("Quantity cannot be less than zero")

        if price < 0:
            raise SuperMarketError("Price cannot be less than zero")

        product = Product(product_id=prod_id,name=name,price=price,quantity=quantity)
        self.product_repository.update_product(product=product)

        return product


    def add_customer(self, cus_id: str, name: str, email: str, phone_no: str) -> Customer:

        if self.customer_repository.get_by_id(customer_id=cus_id) is not None:
            raise SuperMarketError("Customer already exists")

        if self.customer_repository.find_by_email(email=email) is not None:
            raise SuperMarketError("Email already exists")

        customer = Customer(customer_id=cus_id,name=name,email=email,phone_no=phone_no)
        self.customer_repository.add_customer(customer)

        return customer

    def get_customer_by_id(self, customer_id: str) -> Optional[Customer]:
        if self.customer_repository.get_by_id(customer_id=customer_id) is None:
            raise SuperMarketError(f"No customer related to {customer_id} this customer ID")

        return self.customer_repository.get_by_id(customer_id=customer_id)

    def list_all_customers(self) -> List[Customer]:
        if len(self.customer_repository.list_all_customers()) == 0:
            raise SuperMarketError("No customers in the list")

        return self.customer_repository.list_all_customers()

    def update_customer(self, cus_id: str, name: str, email: str, phone_no: str) -> Customer:
        if self.customer_repository.get_by_id(customer_id=cus_id) is None:
            raise SuperMarketError("No Customer exists")

        if self.customer_repository.find_by_email(email=email) is not None:
            raise SuperMarketError("Email already exists")

        customer = Customer(customer_id=cus_id,name=name,email=email,phone_no=phone_no)
        self.customer_repository.update_customer(customer=customer)

        return customer

    def add_order(self, order_id: str, customer_id: str, customer_name: str) -> Order:

        if self.order_repository.get_by_id(order_id=order_id) is not None:
            raise SuperMarketError("Order already exists")

        if self.customer_repository.get_by_id(customer_id=customer_id) is None:
            raise SuperMarketError("Customer not registered")

        order = Order(order_id=order_id,customer_id=customer_id,customer_name=customer_name)
        self.order_repository.add_order(order=order)

        return order

    def list_all_orders(self) -> List[Order]:
        if len(self.order_repository.list_all_orders()) == 0:
            raise SuperMarketError("No orders in the list")

        return self.order_repository.list_all_orders()

    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        if self.order_repository.get_by_id(order_id=order_id) is None:
            raise SuperMarketError(f"No order related to {order_id} this Order ID")

        return self.order_repository.get_by_id(order_id=order_id)

    def update_order(self, order_id: str, customer_id: str, customer_name: str) -> Order:
        if self.order_repository.get_by_id(order_id=order_id) is None:
            raise SuperMarketError("No Order exists")

        if self.customer_repository.get_by_id(customer_id=customer_id) is None:
            raise SuperMarketError("Customer not registered")

        order = Order(order_id=order_id,customer_id=customer_id,customer_name=customer_name)
        self.order_repository.update_order(order=order)

        return order


if __name__ == "__main__":

    super_market = SuperMarketService(
        product_repository=InMemoryProductRepository(),
        customer_repository=InMemoryCustomerRepository(),
        order_repository=InMemoryOrderRepository()
    )

    super_market.add_product(prod_id="P001",name="Anchor",price=1500.0,quantity=10)
    x = super_market.get_product_by_id(product_id="P001")
    print(x)
    print(x.product_id)