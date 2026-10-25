route = ("Kurunagala" , "Colombo" , "08:00 AM")
ticket_price = 1500

def display_routes():
    print(f"\nRoute: {route[0]} -> {route[1]}"
          f"\nDeparture: {route[2]}"
          f"\nTicket price: Rs. {ticket_price:,}")


if __name__ == "__main__":
    display_routes()