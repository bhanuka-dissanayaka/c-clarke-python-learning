from reservation.bookings import bookings

seats = list(range(1,21))

def view_seats():
    print("\nSeat Availability : ")
    for seat in seats:
        status = "[]"
        if check_booking_status(seat):
            status = "[X]"
        print(f"{seat:02d}-{status} ",end="")

def check_booking_status(seat_num):
    for i in bookings:
        if i["seat_number"] == seat_num:
            return True
    return False
