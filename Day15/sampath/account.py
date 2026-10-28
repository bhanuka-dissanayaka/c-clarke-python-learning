from Day15.sampath.users import User


class Account:
    def __init__(self, account_no: str, branch: str, balance: float, user: User):
        self.__account_no = account_no
        self.__branch = branch
        self.__balance = balance
        self.__user = user

    def show_account_details(self) -> None:
        print(f"Account no - {self.__account_no} | branch - {self.__branch} | Balance - {self.__balance}")

    def deposit(self,amount) -> str:
        if amount<0:
            return "Invalid Amount"
        self.__balance += amount
        return "Successfully updated the balance"

    def withdraw(self,withdraw_amount) -> str:
        if self.__balance < withdraw_amount:
            return "Invalid balance"
        self.__balance -= withdraw_amount
        return "Withdraw successfully"

    def get_account_no(self) -> str:
        return self.__account_no

    def get_balance(self) -> float:
        return self.__balance

    def get_user(self) -> User:
        return self.__user

    def set_user(self,user) -> None:
        self.__user = user

    def __str__(self):  # Overriding the object calss __str__ method. Object class is the top class
        return self.__account_no



if __name__=='__main__':
    user1 = User(nic="200054545",age=21,name="Bhanuka")
    user2 = User(nic="20545454545",age=21,name="Dilshan")

    account1 = Account("123", "Kurunegala", 250000000.0, user1)
    account2 = Account("124", "Colombo", 2500000.0, user2)
    account1.deposit(500)
    account1.show_account_details()
    print(account2.get_user())  # <Day14.sampath.users.User object at 0x0000028C9A6A8550>
    print(account2.get_user().get_name())  # Dilshan
    print(account2)

# a = "cc"
# a.__str__()
# print("gg".__str__())