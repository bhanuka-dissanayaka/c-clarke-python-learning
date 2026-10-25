vehicles = [{"id":1,"name":"Toyota","manufacture":"Toyota","year":2025,"model":"LC300","regiion":"Sri lanka", "price":10000000.0}]

def add_vehicle(vehicle):
    vehicles.append(vehicle)
    print("New Vehicle added successfully")

def search_by_name(name):
    for vehicle in vehicles:
        if vehicle["name"] == name:
            return vehicle
    return "Vehicle not found"

def search_by_manufacture_or_model(manufacture_or_mode):
    for vehicle in vehicles:
        if vehicle["model"] == manufacture_or_mode or  vehicle["manufacture"] == manufacture_or_mode:
            return vehicle
    return "Vehicle not found"

def search_vehicle_by_price_range(max_range):
    for vehicle in vehicles:
        if vehicle["price"] < max_range:
            return vehicle
    return "Vehicle not found"


print(search_by_name("Toyota"))