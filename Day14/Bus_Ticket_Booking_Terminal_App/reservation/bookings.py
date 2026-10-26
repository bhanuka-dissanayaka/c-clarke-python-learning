from reservation.routes import (route,ticket_price)
bookings = [
 {
 "reference": "BUS-1001",
 "passenger_name": "Nimal",
 "seat_number": 2,
 "route": ("Kurunegala", "Colombo"),
 "ticket_price": 1500
 }
]


def check_booking_status(seat_num):
 for i in bookings:
  if i["seat_number"] == seat_num:
   return True
 return False


def generate_booking_reference():
 last_ref_num = int(bookings[-1]["reference"].split("-")[1])
 new_reference = f"BUS-{last_ref_num+1}"
 return new_reference

def reserve_seat():
 name = input("Passenger name: ")
 while True:
  seat_no = input("Choose seat number: ")
  try:
   seat_no = int(seat_no)
  except ValueError:
   print("Invalid input. Please enter a number.")
   continue
  if seat_no < 1 or seat_no > 20:
   print("Invalid seat number. Please choose 1-20.")
   continue
  if check_booking_status(seat_no):
   print(f"Seat {seat_no} is already booked. Choose another seat.")
   continue
  break
 reference = generate_booking_reference()
 booking = {
 "reference": reference,
 "passenger_name": name,
 "seat_number": seat_no,
 "route": route,
 "ticket_price": ticket_price
 }
 bookings.append(booking)
 print("\nReservation successful!")
 print("Booking Reference:", reference)
 print(f"Seat Number: {seat_no:02d}")
 print("Route:", route[0], "->", route[1])
 print("Ticket Price: Rs.", ticket_price)


def cancel_booking():
 reference = input("Enter Booking Reference : ")
 for booking in bookings:
  if booking["reference"] == reference:
   bookings.remove(booking)
   print("Booking successfully canceled")
   return
 print("\nBooking not found.")
 print("Please check the booking reference.")

def search_booking():
 reference = input("Enter Booking Reference Number to search: ")
 for booking in bookings:
  if booking["reference"] == reference:
   print("Booking Found")
   print(booking)
   return
 print("Booking number not found.")




