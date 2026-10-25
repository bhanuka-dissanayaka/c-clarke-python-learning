from reservation.bookings import bookings

def view_passenger_list():
    for i in bookings:
        print(f"{i["passenger_name"]}-{i["seat_number"]}")
