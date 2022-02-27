from src.Bank import Bank
from src.BanknoteVault import BanknoteVault


class ATM:

    def __init__(self, bank: Bank, data: dict):
        self.__bank: Bank = bank
        self.__vault = BanknoteVault(data["cash"])

    def start(self):
        pass
