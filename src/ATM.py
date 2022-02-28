import os

from src.Bank import Bank
from src.BankAccount import Card
from src.BanknoteVault import BanknoteVault

clear = lambda: os.system("cls")


class ATM:

    def __init__(self, bank: Bank, data: dict) -> None:
        self.__bank: Bank = bank
        self.__vault = BanknoteVault(data["cash"])

    @staticmethod
    def __selectNumberFromRange(upperLimit: int) -> int:
        selectedNumber: int
        while True:
            number: str = input("Select number:  ")
            if not number.isdigit():
                print("Incorrect input, try again")
                continue
            number: int = int(number)
            if upperLimit > number >= 0:
                return number
            else:
                print("Incorrect input, try again")

    def __selectCard(self) -> Card | None:
        cards = self.__bank.getCards()
        num: int = 1
        for card in cards:
            print(str(num) + ")", card.getNumber())
            num += 1
        print("0) Back")
        option = self.__selectNumberFromRange(num)

        if option == 0:
            clear()
            return None
        return cards[option - 1]

    def __enterPin(self) -> bool:
        if self.__card.isLocked():
            return False
        for i in range(self.__card.getAttempts()):
            while True:
                pin = input("Enter PIN: ")
                if len(pin) == 4 and pin.isdigit():
                    break
                else:
                    print("Incorrect input, try again")
            if self.__card.checkPIN(pin):
                return True
            else:
                print("Incorrect PIN, try again")
        self.__card.setLockedStatus(True)
        return False

    def __insertCard(self, card: Card) -> None:
        self.__card = card
        print("Hello,", self.__card.getBankAccount().getOwnerFirstName(),
              self.__card.getBankAccount().getOwnerLastName())
        if self.__enterPin():
            clear()
            self.__mainMenu()
        else:
            print("You're card is locked!")
            return

    def __mainMenu(self):
        clear()
        countOperation: int = 4
        print("1) View balance\n"
              "2) Get cash\n"
              "3) Phone payment\n"
              "0) Get card")
        option = self.__selectNumberFromRange(countOperation)
        match option:
            case 1:
                clear()
                self.__viewBalance()
            case 2:
                clear()
                self.__giveMoney()
            case 3:
                clear()
                self.__makeTelephonePayment()
            case 0:
                clear()
                return
            case _:
                return

    def __giveMoney(self):
        self.__vault.print()
        print("Input amount")
        while True:
            moneyCount = input()
            if moneyCount.isdigit():
                break
            else:
                print("Incorrect input, try again")
        if int(moneyCount) > self.__card.getBankAccount().getBalance():
            print("Not enough money in the account")
            input("Press Enter...")
            self.__mainMenu()
            return
        cash = self.__vault.giveMoney(int(moneyCount))
        if cash is None:
            print("ATM cannot dispense this amount")
            input("Press Enter...")
            self.__mainMenu()
            return
        for nominal in cash.keys():
            if cash[nominal] != 0:
                print(str(nominal) + "x" + str(cash[nominal]))
        self.__card.getBankAccount().decreaseBalance(int(moneyCount))
        input("Press Enter...")
        self.__mainMenu()

    def __makeTelephonePayment(self):
        print("Input amount")
        while True:
            moneyCount = input()
            if moneyCount.isdigit():
                break
            else:
                print("Incorrect input, try again")

        if int(moneyCount) > self.__card.getBankAccount().getBalance():
            print("Not enough money in the account")
            input("Press Enter...")
            self.__mainMenu()
            return

        while True:
            number = input("Enter your phone number:\n +375")
            if len(number) == 9 and number.isdigit():
                break
            print("Incorrect input, try again")

        self.__card.getBankAccount().decreaseBalance(int(moneyCount))
        print("Payment successful")
        input("Press Enter..")
        self.__mainMenu()

    def __viewBalance(self):
        print("Account balance:", str(self.__card.getBankAccount().getBalance()))
        input("Press Enter...")
        self.__mainMenu()

    def getData(self) -> dict:
        return {"cash": self.__vault.getData()}

    def start(self) -> None:
        card = self.__selectCard()
        if card is None:
            return
        self.__insertCard(card)
