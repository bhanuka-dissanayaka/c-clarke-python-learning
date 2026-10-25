import reservation.booking as b
import reservation.seats as s
import reservation.routes as r

while True:


    print(f"\n==============================================="
          f"\n            BUS RESERVATION SYSTEM"
          f"\n==============================================="
          f"\n01. View routes and seats"
          f"\n02. Reserve a seat"
          f"\n03. Cancel a reservation"
          f"\n04. Search booking"
          f"\n05. View passenger list"
          f"\n06. Exit"
          f"\n==============================================")

    choice = input("\nChoose an option: ")

    if choice == "1":
        r.display_routes()
        s.display_seats()

    elif choice == "2":
        try:
            b.reserve_seat()

        except ValueError:
            print("\nPlease enter a number ❗")

    elif choice == "3":
        try:
            b.cancel_booking()

        except ValueError:
            print("\nInvalid Reference ID ❗")

    elif choice == "4":
        try:
            b.search_booking()

        except ValueError:
            print("\nInvalid Reference ID ❗")

    elif choice == "5":
        b.display_passengers()

    elif choice == "6":
        exit()

    else:
        print("\nPlease enter valid choice no ❕")