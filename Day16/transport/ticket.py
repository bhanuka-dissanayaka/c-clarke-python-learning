from Day16.transport.passenger import Passenger


class Ticket:
    def __init__(self, ticket_no: str, price: float, route: str, passenger: Passenger, data: str) -> None:
        self.__ticket_no = ticket_no
        self.__price = price
        self.__route = route
        self.__passenger = passenger
        self.__data = data







