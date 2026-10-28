from Day16.transport.passenger import Passenger
from Day16.transport.ticket import Ticket


class TrainTicket(Ticket):
    def __init__(self, ticket_no: str, price: float, route: str, passenger: Passenger, data: str, train_class: str) -> None:
        super().__init__(ticket_no=ticket_no,price=price,route=route,passenger=passenger,data=data)
        self.train_class = train_class