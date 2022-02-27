from typing import List

from src.BankAccount import BankAccount


class Bank:
    __accounts: List[BankAccount] = list()

    def __init__(self, data: dict):
        self.__name: str = data["name"]
        if type(self.__name) is not str:
            raise ValueError("Invalid bank name")
        for account in data["accounts"]:
            self.__accounts.append(BankAccount(account))
