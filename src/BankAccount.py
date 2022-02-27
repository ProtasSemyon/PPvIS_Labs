from typing import List


class BankAccount:
    __numberSize = 10

    def __init__(self, data: dict):
        self.__ownerFirstName: str = data["firstName"]
        if type(self.__ownerFirstName) is not str:
            raise ValueError("Incorrect first name")

        self.__ownerLastName: str = data["lastName"]
        if type(self.__ownerLastName) is not str:
            raise ValueError("Incorrect last name")

        self.__number: str = data["number"]
        if len(self.__number) != self.__numberSize or not self.__number.isdigit():
            raise ValueError("Incorrect account number")

        self.__balance: float = data["balance"]
        if type(self.__balance) is not float and type(self.__balance) is not int:
            raise ValueError("Incorrect account balance")

        self.__cards: List[Card] = list()
        for card in data["cards"]:
            self.__cards.append(Card(card, self))


class Card:
    __numberSize = 16
    __pinSize = 4

    def __init__(self, data: dict, account: BankAccount):
        self.__account = account
        self.__number = data["cardNum"]
        if len(self.__number) != self.__numberSize or not self.__number.isdigit():
            raise ValueError("Incorrect card number")

        self.__pin = data["cardPIN"]
        if len(self.__pin) != self.__pinSize or not self.__pin.isdigit():
            raise ValueError("Incorrect card PIN")
