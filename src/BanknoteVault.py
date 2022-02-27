class BanknoteVault:
    def __init__(self, cash: list):
        self.__cash: dict = dict()
        for banknote in cash:
            self.__cash.update({banknote["nominal"]: banknote["count"]})
