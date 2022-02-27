import json

from src.ATM import ATM
from src.Bank import Bank

databasePath = "database.json"
if __name__ == "__main__":
    try:
        file = open(databasePath, "r")
    except IOError:
        print("Database doesn't exist")
    else:
        with file as jsonLoad:
            data = json.load(jsonLoad)
    try:
        bank = Bank(data["infoBank"])
        atm = ATM(bank, data["infoATM"])
    except KeyError:
        print("Incorrect database")
    except ValueError:
        print("Incorrect database")
    else:
        atm.start()
