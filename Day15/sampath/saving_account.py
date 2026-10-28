from account import Account

class SavingAccount(Account):
    def __init__(self,account_no, branch, balance, user,card_number):
        super().__init__(account_no, branch, balance, user)
        self.__card_number = card_number

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self,card_number):
        self.__card_number = card_number