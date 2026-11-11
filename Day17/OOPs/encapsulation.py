class DataPlans:
    def __init__(self, phone_no: str, data_amount: float):
        self.__phone_no = phone_no
        self.__data_amount = data_amount

    def get_phone_no(self) -> str:
        return self.__phone_no

    def get_data_amount(self) -> float:
        return self.__data_amount

    def set_phone_no(self , phone_no: str):
        self.__phone_no = phone_no

    def set_data_amount(self , data_amount: float):
        self.__data_amount = data_amount

data_plan = DataPlans("071215454",1500)
print(f"Phone Number - {data_plan.get_phone_no()}")
print(f"Data Amount - {data_plan.get_data_amount()} MB")

data_plan.set_data_amount(40000)
print(f"Data Amount after update - {data_plan.get_data_amount()} MB")
