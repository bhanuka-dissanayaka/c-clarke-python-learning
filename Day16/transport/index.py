from Day16.transport.bus_ticket import BusTicket
from Day16.transport.passenger import Passenger
from Day16.transport.train_ticket import TrainTicket

passenger1 = Passenger(nic="2005112855" , name="Bhanuka", age=21)
bus_ticket1 = BusTicket(ticket_no="001", price=150 , route="Kurunegala" , passenger=passenger1 , data="2026-10-28", is_ac=True)
train_ticket1 = TrainTicket(ticket_no="001", price=150 , route="Kurunegala" , passenger=passenger1 , data="2026-10-28", train_class="First Class")

print(passenger1.__dict__)
print(bus_ticket1.__dict__)
print(train_ticket1.__dict__)