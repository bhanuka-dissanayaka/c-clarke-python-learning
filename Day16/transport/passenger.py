class Passenger:
    def __init__(self, nic: str, name: str, age: int) -> None:
        self.__nic = nic
        self.__name = name
        self.__age = age

    def get_nic(self) -> str:
        return self.__nic

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age



