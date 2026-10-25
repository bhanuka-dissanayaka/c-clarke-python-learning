bookings = [
    {"reference": "BUS-1001",
     "passenger_name": "Nimal",
     "seat_number": 2,
     "route": ("Kurunegala" , "Colombo"),
     "ticket_price": 1500}
]

ref_id = 1000

def id_generator():
    global ref_id
    ref_id += 1
    return ref_id

def id_checker():
    new_ref_list = []

    for booking in bookings:
        new_ref = booking["reference"]
        new_ref_list.append(int(new_ref.removeprefix("BUS-")))

    while True:
        new_id = id_generator()
        if new_id in new_ref_list:
            continue
        else:
            return new_id

def reserve_seat():

    if len(bookings) != 20:
        name = input("Passenger name: ").strip()
        seat_no = int(input("Choose seat number: "))

        if not name:
            print("\nName can't be empty ❗")
            return

        if seat_no > 20 or seat_no == 0 or seat_no < 0:
            print("\nEnter number between 1 - 20")
            return

        for booking in bookings:
            if booking["seat_number"] == seat_no:
                print("\nThe seat no you entered already booked ⭕")
                return

            else:
                new_passenger_id = str(id_checker())
                new_passenger = {
                    "reference": "BUS-" + new_passenger_id,
                    "passenger_name": name,
                    "seat_number": seat_no,
                    "route": ("Kurunegala" , "Colombo"),
                    "ticket_price": 1500
                }

                bookings.append(new_passenger)
                print("\nReservation Successful ✅")
                return

    else:
        print("\nAll seats are booked 🚫")

def cancel_booking():

    ref_no = input("Enter Reference ID: ").strip().upper()

    for i in range(len(bookings)):
        if bookings[i]["reference"] == ref_no:
            del bookings[i]
            print("\nReservation Canceled Successfully ✅")
            return

    print("\nInvalid Reference ID ⭕")
    return

def search_booking():

    ref_no = input("Enter Reference ID: ").strip().upper()

    for i in range(len(bookings)):
        if bookings[i]["reference"] == ref_no:
            print(f"\nREFERENCE    PASSENGER    SEAT         PRICE"
                  f"\n"
                  f"\n{(bookings[i]["reference"]):>8}    {(bookings[i]["passenger_name"]):>8}    "
                  f"   {(bookings[i]["seat_number"]):02}     Rs.{(bookings[i]["ticket_price"]):.2F}")
            return

    print("\nInvalid Reference ID ⭕")
    return

def display_passengers():

    if len(bookings) == 0:
        print("\nNo Reservations ❗")

    else:
        print("\nREFERENCE    PASSENGER    SEAT         PRICE"
              "\n")
        for i in range(len(bookings)):
            print(f"{(bookings[i]["reference"]):>8}    {(bookings[i]["passenger_name"]):>8}    "
                  f"   {(bookings[i]["seat_number"]):02}     Rs.{(bookings[i]["ticket_price"]):.2F}")


if __name__ == "__main__":
    try:
        reserve_seat()


    except ValueError:
        print("\nPlease enter a number ❗")
    print(id_checker())