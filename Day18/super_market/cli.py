from Day18.super_market.models import SuperMarketError
from Day18.super_market.repositories import InMemoryCustomerRepository, InMemoryProductRepository, \
    InMemoryOrderRepository
from Day18.super_market.service import SuperMarketService

supermarket_service = SuperMarketService(
    product_repository=InMemoryProductRepository(),
    customer_repository=InMemoryCustomerRepository(),
    order_repository=InMemoryOrderRepository()
)

def add_product():

    prod_id = input("\nEnter Product id: ").strip()
    name = input("Enter product name: ").strip().title()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    supermarket_service.add_product(prod_id=prod_id,name=name,price=price,quantity=quantity)

def list_all_products():
    product_list = supermarket_service.list_all_products()

    for product in product_list:
        print(f"\nProduct ID: {product.product_id}"
              f"\nName: {product.name}"
              f"\nPrice: {product.price}"
              f"\nQuantity: {product.quantity}")

def get_product_by_id():

    prod_id = input("Enter Product ID: ").strip()
    product = supermarket_service.get_product_by_id(product_id=prod_id)
    print(f"\nProduct ID: {product.product_id}"
          f"\nName: {product.name}"
          f"\nPrice: {product.price}"
          f"\nQuantity: {product.quantity}")

def update_product():

    prod_id = input("\nEnter Product id: ").strip()
    name = input("Enter product name: ").strip().title()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    supermarket_service.update_product(prod_id=prod_id,name=name,price=price,quantity=quantity)

def add_customer():

    cus_id = input("\nEnter Customer ID: ").strip()
    name = input("Enter Customer Name: ").strip().title()
    email = input("Enter Email: ").strip().lower()
    phone_no = input("Enter Phone NO: ").strip()
    supermarket_service.add_customer(cus_id=cus_id,name=name,email=email,phone_no=phone_no)

def list_all_customers():

    customer_list = supermarket_service.list_all_customers()

    for customer in customer_list:
        print(f"\nCustomer ID: {customer.customer_id}"
              f"\nName: {customer.name}"
              f"\nEmail: {customer.email}"
              f"\nPhone NO: {customer.phone_no}")

def get_customer_by_id():

    customer_id = input("Enter Customer ID: ").strip()
    customer = supermarket_service.get_customer_by_id(customer_id=customer_id)
    print(f"\nCustomer ID: {customer.customer_id}"
          f"\nName: {customer.name}"
          f"\nEmail: {customer.email}"
          f"\nPhone NO: {customer.phone_no}")

def update_customer():

    cus_id = input("\nEnter Customer ID: ").strip()
    name = input("Enter Customer Name: ").strip().title()
    email = input("Enter Email: ").strip().lower()
    phone_no = input("Enter Phone NO: ").strip()
    supermarket_service.update_customer(cus_id=cus_id,name=name,email=email,phone_no=phone_no)

def add_order():

    order_id = input("\nEnter Order ID: ").strip()
    customer_id = input("Enter Customer ID: ").strip()
    cus_name = input("Enter Customer Name: ").strip().title()
    supermarket_service.add_order(order_id=order_id,customer_id=customer_id,customer_name=cus_name)

def list_all_orders():

    order_list = supermarket_service.order_repository.list_all_orders()

    for order in order_list:
        print(f"\nOrder ID: {order.order_id}"
              f"\nCustomer ID: {order.customer_id}"
              f"\nCustomer Name: {order.customer_name}"
              f"\nCreated At: {order.created_at}")


def get_order_by_id():

    order_id = input("Enter Order ID: ").strip()
    order = supermarket_service.get_order_by_id(order_id=order_id)
    print(f"\nOrder ID: {order.order_id}"
          f"\nCustomer ID: {order.customer_id}"
          f"\nCustomer Name: {order.customer_name}"
          f"\nCreated At: {order.created_at}")

def update_order():
    order_id = input("\nEnter Order ID: ").strip()
    customer_id = input("Enter Customer ID: ").strip()
    cus_name = input("Enter Customer Name: ").strip().title()
    supermarket_service.update_order(order_id=order_id,customer_id=customer_id,customer_name=cus_name)

def main_cli():

    while True:

        try:

            print("\n=============================================="
                  "\n01. Add product"
                  "\n02. View All Products"
                  "\n03. Search Product"
                  "\n04. Update Product"
                  "\n=============================================="
                  "\n05. Add Customer"
                  "\n06. View Customers"
                  "\n07. Search Customer"
                  "\n08. Update Customer"
                  "\n=============================================="
                  "\n09. Add order"
                  "\n10. View All Orders"
                  "\n11. Search Order"
                  "\n12. Update Order"
                  "\n=============================================="
                  "\n0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_product()

            elif choice == "2":
                list_all_products()

            elif choice == "3":
                get_product_by_id()

            elif choice == "4":
                update_product()

            elif choice == "5":
                add_customer()

            elif choice == "6":
                list_all_customers()

            elif choice == "7":
                get_customer_by_id()

            elif choice == "8":
                update_customer()

            elif choice == "9":
                add_order()

            elif choice == "10":
                list_all_orders()

            elif choice == "11":
                get_order_by_id()

            elif choice == "12":
                update_order()

            elif choice == "0":
                exit()

            else:
                print("\nInvalid choice selection ❌")

        except SuperMarketError as e:
            print(f"\nError - {str(e)}")


if __name__ == "__main__":

    main_cli()