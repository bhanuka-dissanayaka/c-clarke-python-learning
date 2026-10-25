from . import booking

MAX_NO = 20

seats = list(range(1,MAX_NO + 1))



def display_seats():
    seats_list = []

    for book in booking.bookings:
        seats_list.append(book["seat_number"])

    print("\nSeat Availability:"
          "\n")

    for seat in seats:

        if seat in seats_list:
            booking_status = "[X]"

        else:
            booking_status = "[ ]"

        print(f"{seat:02} {booking_status}", end="  ")

        if seat % 4 == 0:
            print()

    print("\n[X] = Booked     [ ] = Available")

if __name__ == "__main__":
    display_seats()


