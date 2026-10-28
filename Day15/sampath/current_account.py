from account import Account

class CurrentAccount(Account):
    def __init__(self, account_no, branch, balance, user,cheque_ids):
        super().__init__(account_no=account_no,branch=branch,balance=balance, user=user)
        self.__cheque_ids = cheque_ids

    def get_check_ids(self):
        return self.__cheque_ids

    def add_check_ids(self,check_id):
        self.__cheque_ids.append(check_id)

if __name__ == '__main__':
    curr_accnt = CurrentAccount("1235","Moratuwa",500000.0,"Kalana" , ["122","45454"])
    curr_accnt.show_account_details()
    print(curr_accnt.get_check_ids())
