from typing import Any


class BankAccount:
    """Кошелек"""

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self) -> Any:
        print('getter')
        return self.__balance

    @my_balance.setter
    def my_balance(self, new_balance: Any) -> None:
        print('setter')
        if isinstance(new_balance, (int, float)):
            self.__balance = new_balance
        else:
            raise ValueError("Balance must be of type int or float")

    @my_balance.deleter
    def my_balance(self) -> None:
        print('deleter')
        del self.__balance


a = BankAccount('Nar', 1000)

