from reservation.routes import view_routes
from reservation.seats import view_seats
from reservation.bookings import (
    reserve_seat,
    cancel_booking,
    search_booking
)
from reservation.reports import view_passenger_list



while True:
    print("\n========================================")
    print("          BUS RESERVATION SYSTEM")
    print("========================================")
    view_routes()
    print("\n1. View routes and seats")
    print("2. Reserve a seat")
    print("3. Cancel a reservation")
    print("4. Search booking")
    print("5. View passenger list")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        view_routes()
        view_seats()

    elif choice == "2":
        reserve_seat()

    elif choice == "3":
        cancel_booking()

    elif choice == "4":
        search_booking()

    elif choice == "5":
        view_passenger_list()

    elif choice == "6":
        print("\nThank you for using the Bus Reservation System.")
        print("Program closed.")
        break

    else:
        print("\nInvalid choice. Please select 1-6.")
