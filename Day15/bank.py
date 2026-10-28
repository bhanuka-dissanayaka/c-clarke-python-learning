from typing import List, Optional

from sampath.account import Account
from sampath.current_account import CurrentAccount
from sampath.users import User
from sampath.account import Account

users: List[User] = []
accounts: List[Account] = []

def find_user_by_nic(nic: str) -> Optional[User]:
    for user in users:
        if user.get_nic() == nic:
            return user
    return None

def find_user_account_number(acc_number: str) -> Optional[Account]:
    for account in accounts:
        print(account.get_account_no())
        if account.get_account_no() == acc_number:
            return account
    return None


def list_all_cheques() -> None:
    cheques = []
    for account in accounts:
        if isinstance(account,CurrentAccount):
            cheques.extend(account.get_check_ids())
    print(f"All cheque ids - {cheques}")

if __name__ == '__main__':
    user1 = User("222","21","Kalana")
    user2 = User("223","22","Gayan")
    users.append(user1)
    users.append(user2)
    print(find_user_by_nic("222"))

    # account1 = SavingAccount("123", "Kurunegala", 250000000.0, user1,'554')
    # accounts.append(account1)
    # print(find_user_by_nic("123"))
