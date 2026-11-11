from abc import ABC, abstractmethod
from typing import List, Optional, Dict

from Day18.super_market.models import Product, Customer, Order, SuperMarketError


class ProductRepository(ABC):

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]:
        pass

    @abstractmethod
    def update_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def list_all_products(self) -> List[Product]:
        pass


class CustomerRepository(ABC):

    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: str) -> Optional[Customer]:
        pass

    @abstractmethod
    def update_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def list_all_customers(self) -> List[Customer]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Customer]:
        pass

class OrderRepository(ABC):

    @abstractmethod
    def add_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id) -> Optional[Order]:
        pass

    @abstractmethod
    def update_order(self, order: Order) -> None:
        pass

    @abstractmethod
    def list_all_orders(self) -> List[Order]:
        pass


class InMemoryProductRepository(ProductRepository):

    def __init__(self):
        self.__products : Dict[str, Product] = {}  # {"001" : product_object}

    def add_product(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def update_product(self, product: Product) -> None:

        if self.__products.get(product.product_id) is None:
            raise SuperMarketError("Product does not exists")

        self.__products[product.product_id] = product

    def get_by_id(self, product_id: str) -> Optional[Product]:
        return self.__products.get(product_id)

    def list_all_products(self) -> List[Product]:
        return list(self.__products.values())


class InMemoryCustomerRepository(CustomerRepository):

    def find_by_email(self, email: str) -> Optional[Customer]:
        for customer in self.__customers.values():
            if customer.email == email:
                return customer

        return None

    def __init__(self):
        self.__customers : Dict[str, Customer] = {}

    def add_customer(self, customer: Customer) -> None:
        self.__customers[customer.customer_id] = customer

    def get_by_id(self, customer_id: str) -> Optional[Customer]:
        return self.__customers.get(customer_id)

    def update_customer(self, customer: Customer) -> None:

        if self.__customers.get(customer.customer_id) is None:
            raise SuperMarketError("Customer does not exists")

        self.__customers[customer.customer_id] = customer

    def list_all_customers(self) -> List[Customer]:
        return list(self.__customers.values())


class InMemoryOrderRepository(OrderRepository):

    def __init__(self):
        self.__orders : Dict[str, Order] = {}

    def add_order(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def get_by_id(self, order_id) -> Optional[Order]:
        return self.__orders.get(order_id)

    def update_order(self, order: Order) -> None:

        if self.__orders.get(order.order_id) is None:
            raise SuperMarketError("Order does not exists")

        self.__orders[order.order_id] = order

    def list_all_orders(self) -> List[Order]:
        return list(self.__orders.values())


if __name__ == "__main__":

    in_memory_prod_repo = InMemoryProductRepository()

    prod1 = Product(product_id="P001",name="Anchor",price=1000.0,quantity=10)

    in_memory_prod_repo.add_product(prod1)
    print(in_memory_prod_repo.list_all_products())
    print(in_memory_prod_repo.get_by_id(product_id="P001"))

    in_memory_cust_repo = InMemoryCustomerRepository()

    cust1 = Customer(customer_id="C001",name="Sahan",email="sahan@gmail.com",phone_no="0784545236")

    in_memory_cust_repo.add_customer(customer=cust1)
    print(in_memory_cust_repo.list_all_customers())