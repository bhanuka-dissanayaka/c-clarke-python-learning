order_ids = []
customer_names = []
distances = []
order_values = []
delivery_charges = []
delivery_statuses = []

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
    new_id = len(order_ids) + 1
    order_ids.append(new_id)
    customer_name = input("Enter Customer Name : ")
    customer_names.append(customer_name)
    distance = float(input("Enter the distance in KM : "))
    distances.append(distance)
    order_value = float(input("Enter the value of the order : "))
    order_values.append(order_value)
    delivery_charge = calculate_delivery_charges(distance)
    delivery_charges.append(delivery_charge)
    delivery_status = "Pack"
    delivery_statuses.append(delivery_status)

def view_orders():
    for i in range(len(order_ids)):
        print(f"Id- {order_ids[i]}")
        print(f"Customer Name - {customer_names[i]}")
        print(f"Distance - {distances[i]}")
        print(f"Order Value - {order_values[i]}")
        print(f"Delivery Charge - {delivery_charges[i]}")
        print(f"Delivery Status - {delivery_statuses[i]}")

def search_order():
    order_id = int(input("Enter Order's Id: "))
    if order_id in order_ids:
        "=====ORDER FOUND======"
        i = order_ids.index(order_id)
        print(f"Id - {order_ids[i]}")
        print(f"Customer Name - {customer_names[i]}")
        print(f"Distance - {distances[i]}")
        print(f"Order Value - {order_values[i]}")
        print(f"Delivery Charge - {delivery_charges[i]}")
        print(f"Delivery Status - {delivery_statuses[i]}")
    else:
        print("Order not found.")

def change_status():
    order_id = int(input("Enter order Id : "))
    if order_id in order_ids:
        index = order_ids.index(order_id)
        new_status = input("Enter new status : ")
        delivery_statuses[index] = new_status
        print("Order status updates successfully.")

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
