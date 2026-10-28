class User:
    def __init__(self,nic,age,name):
        self.__nic = nic
        self.__age = age
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_nic(self,nic):
        self.__nic = nic

    def get_nic(self):
        return self.__nic

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Name - {self.__name} | Age - {self.__age} | NIC - {self.__nic}"