orders = []

def calculate_delivery_charges(distance):
    charge = 0
    if 0<distance <=5:
        charge = 200
    elif 5 < distance <= 10:
        charge = 350
    elif 10 < distance <= 20:
        charge = 500
    elif 20 < distance:
        charge = 700
    return charge

def create_order():
    order = {}
    new_id = len(orders) + 1
    order["id"] = new_id
    customer_name = input("Enter Customer Name : ")
    order["customer_name"] = customer_name
    distance = float(input("Enter the distance in KM : "))
    order["distance"] = distance
    order_value = float(input("Enter the value of the order : "))
    order["value"] = order_value
    delivery_charge = calculate_delivery_charges(distance)
    order["delivery_charge"] = delivery_charge
    delivery_status = "Pack"
    order["delivery_status"] = delivery_status
    orders.append(order)
    print("Order created successfully")

def view_orders():
    for order in orders:
        print(f"Id- {order["id"]}")
        print(f"Customer Name - {order["customer_name"]}")
        print(f"Distance - {order["distance"]}")
        print(f"Order Value - {order["value"]}")
        print(f"Delivery Charge - {order["delivery_charge"]}")
        print(f"Delivery Status - {order["delivery_status"]}")

def search_order():
    order_id = int(input("Enter Order's Id: "))
    for order in orders:
        if order["id"] == order_id:
            print(f"Id- {order["id"]}")
            print(f"Customer Name - {order["customer_name"]}")
            print(f"Distance - {order["distance"]}")
            print(f"Order Value - {order["value"]}")
            print(f"Delivery Charge - {order["delivery_charge"]}")
            print(f"Delivery Status - {order["delivery_status"]}")
            return
    print("Order not found")

def change_status():
    order_id = int(input("Enter order Id : "))
    new_status = input("Enter new status : ")
    for order in orders:
        if order["id"] == order_id:
            order["delivery_status"] = new_status
            print("Order status updates successfully.")
            return
    print("Order not found")

while True:
    print("\n==============================")
    print("   ORDER MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Order")
    print("2. View All Orders")
    print("3. Search Order")
    print("4. Change Delivery Status")
    print("0. Exit")
    choice = input("Enter a choice : ")
    if choice=="1":
        create_order()
    elif choice == "2":
        view_orders()
    elif choice == "3":
        search_order()
    elif choice == "4":
        change_status()
    elif choice == "0":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")


