from delership import vehicle

while True:
    print("""
    1 - Add New Vehicle
    2 - search by name
    3 - Search by manufacture or model
    4 - find vehicle by price range
    """)
    choice = input("Enter Your choice : ")
    if choice=="1":
        name = input("Enter name of the vehicle : ")
        manufacture = input("Enter Manufacture of the vehicle : ")
        year = int(input("Enter year of the vehicle : "))
        model = input("Enter model of the vehicle : ")
        region = input("Enter region of the vehicle : ")
        price = float(input("Enter price of the vehicle : "))
        new_vehicle = {"id": 1, "name": name,"manufacture":manufacture, "year": year, "model": model, "region": region,"price": price}
        vehicle.add_vehicle(vehicle)
    elif choice == "2":
        name = input("Enter name for search : ")
        print(vehicle.search_by_name(name))
    elif choice == "3":
        manufacture_or_model = input("Enter manufacture or model for search : ")
        print(vehicle.search_by_manufacture_or_model(manufacture_or_model))
    elif choice == "4":
        price = float(input("Enter price of the vehicle : "))
        print( vehicle.search_vehicle_by_price_range(price)
)