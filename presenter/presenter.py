import json

from model.ATM import ATM
from model.Bank import Bank


class IPresenter:
    @staticmethod
    def loadDatabase(path):
        try:
            file = open(path, "r")
        except IOError:
            print("Database doesn't exist")
        else:
            with file as jsonLoad:
                return json.load(jsonLoad)

    @staticmethod
    def saveDatabase(bank: Bank, atm: ATM, path):
        data: dict = {"infoBank": bank.getData(), "infoATM": atm.getData()}
        with open(path, "w") as dataFile:
            json.dump(data, dataFile, indent=4)

    def start(self):
        pass

    def isCardInserted(self):
        pass

    def changeInsertedState(self):
        pass

    def getCards(self):
        pass

    def selectCard(self, number):
        pass

    def enterPin(self, password):
        pass

    def getCardBalance(self):
        pass

    def withdrawMoney(self, amount):
        pass

    def makeTelephonePayment(self, amount, phone):
        pass

    def endWork(self):
        pass

    def checkCorrectPhone(self, phone):
        pass


class Presenter(IPresenter):
    def __init__(self, databasePath, view):
        self.__view = view
        self.__databasePath = databasePath
        data = self.loadDatabase(self.__databasePath)
        try:
            self.__bank = Bank(data["infoBank"])
            self.__atm = ATM(self.__bank, data["infoATM"])
        except KeyError:
            print("Incorrect database")
        except ValueError as exception:
            print("Incorrect database", exception, sep="\n")

    def start(self):
        self.__view.start_atm()

    def isCardInserted(self):
        return self.__atm.isCardInserted()

    def changeInsertedState(self):
        self.__atm.changeInsertedState()

    def getCards(self):
        return self.__atm.getCards()

    def selectCard(self, number):
        self.__atm.selectCard(number)

    def enterPin(self, password):
        return self.__atm.enterPin(password)

    def getCardBalance(self):
        return self.__atm.getCardBalance()

    def withdrawMoney(self, amount):
        return self.__atm.withdrawMoney(amount)

    def makeTelephonePayment(self, amount, phone):
        self.__atm.makeTelephonePayment(amount, phone)

    def checkCorrectPhone(self, number):
        if not len(number) == 9 or not number.isdigit():
            raise ValueError("incorrect phone number, expected 9 digits")

    def endWork(self):
        self.saveDatabase(self.__bank, self.__atm, self.__databasePath)
