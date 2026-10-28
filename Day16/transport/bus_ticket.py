from Day16.transport.passenger import Passenger
from Day16.transport.ticket import Ticket


class BusTicket(Ticket):
    def __init__(self, ticket_no: str, price: float, route: str, passenger: Passenger, data: str, is_ac: bool) -> None:
        super().__init__(ticket_no=ticket_no,price=price,route=route,passenger=passenger,data=data)
        self.__is_ac = is_ac