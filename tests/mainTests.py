import unittest

from src.BankAccount import BankAccount, Card


class CardTestCase(unittest.TestCase):
    defaultBA = BankAccount(
        {"firstName": "Semen", "lastName": "Protas", "balance": 1, "cards": [], "number": "0123456789"})

    def test_constructorCard(self):
        with self.assertRaises(ValueError):
            Card({"cardNum": "012345678901234", "cardPIN": "1234", "status": "lock"}, self.defaultBA)
        with self.assertRaises(ValueError):
            Card({"cardNum": "012345678901234q", "cardPIN": "1234", "status": "lock"}, self.defaultBA)
        with self.assertRaises(ValueError):
            Card({"cardNum": "0123456789012345", "cardPIN": "123q", "status": "lock"}, self.defaultBA)
        with self.assertRaises(ValueError):
            Card({"cardNum": "0123456789012345", "cardPIN": "123", "status": "lock"}, self.defaultBA)
        with self.assertRaises(ValueError):
            Card({"cardNum": "0123456789012345", "cardPIN": "1234", "status": "ock"}, self.defaultBA)
        with self.assertRaises(ValueError):
            Card({"cardNum": "0123456789012345", "cardPIN": "1234", "status": 1}, self.defaultBA)

    testCard = Card({"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}, defaultBA)
    testCard2 = Card({"cardNum": "0123456789012345", "cardPIN": "1234", "status": "unlock"}, defaultBA)

    def test_checkPIN(self):
        self.assertEqual(self.testCard.checkPIN("1234"), True)
        self.assertEqual(self.testCard.checkPIN("1235"), False)

        with self.assertRaises(ValueError):
            self.testCard.checkPIN("123")
        with self.assertRaises(ValueError):
            self.testCard.checkPIN("123a")

    def test_getBankAccount(self):
        self.assertEqual(self.testCard.getBankAccount(), self.defaultBA)

    def test_getNumber(self):
        self.assertEqual(self.testCard.getNumber(), "0123456789012345")

    def test_getAttempts(self):
        self.assertEqual(self.testCard.getAttempts(), 3)

    def test_isLocked(self):
        self.assertEqual(self.testCard.isLocked(), True)
        self.assertEqual(self.testCard2.isLocked(), False)

    def test_setLockedStatus(self):
        self.testCard.setLockedStatus(False)
        self.assertEqual(self.testCard.isLocked(), False)
        self.testCard.setLockedStatus(True)
        self.assertEqual(self.testCard.isLocked(), True)

    def test_getData(self):
        self.assertEqual(self.testCard.getData(), {"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"})
        self.assertEqual(self.testCard2.getData(),
                         {"cardNum": "0123456789012345", "cardPIN": "1234", "status": "unlock"})


class BankAccountTestCase(unittest.TestCase):
    def test_constructor(self):
        with self.assertRaises(ValueError):
            BankAccount(
                {"firstName": 1, "lastName": "Protas", "balance": 1, "number": "0123456789",
                 "cards": [{"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}]})
        with self.assertRaises(ValueError):
            BankAccount(
                {"firstName": "Semen", "lastName": 0, "balance": 1, "number": "0123456789",
                 "cards": [{"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}]})
        with self.assertRaises(ValueError):
            BankAccount(
                {"firstName": "Semen", "lastName": "Protas", "balance": "1", "number": "0123456789",
                 "cards": [{"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}]})
        with self.assertRaises(ValueError):
            BankAccount(
                {"firstName": "Semen", "lastName": "Protas", "balance": 1, "number": "012345678",
                 "cards": [{"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}]})
        with self.assertRaises(ValueError):
            BankAccount(
                {"firstName": "Semen", "lastName": "Protas", "balance": 1, "number": "012345678a",
                 "cards": [{"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}]})

    testBA = BankAccount(
        {"firstName": "Semen", "lastName": "Protas", "balance": 1, "number": "0123456789",
         "cards": [{"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}]})
    card = testBA.getCards()[0]

    def test_getBalance(self):
        self.assertEqual(self.testBA.getBalance(), 1)

    def test_decreaseBalance(self):
        self.testBA.decreaseBalance(1)
        self.assertEqual(self.testBA.getBalance(), 0)
        self.testBA.increaseBalance(1)

    def test_increaseBalance(self):
        self.testBA.increaseBalance(1)
        self.assertEqual(self.testBA.getBalance(), 2)
        self.testBA.decreaseBalance(1)

    def test_getCards(self):
        self.assertEqual(self.testBA.getCards(), [self.card])

    def test_getOwnerFirstName(self):
        self.assertEqual(self.testBA.getOwnerFirstName(), "Semen")

    def test_getOwnerLastName(self):
        self.assertEqual(self.testBA.getOwnerLastName(), "Protas")

    def test_getData(self):
        self.assertEqual(self.testBA.getData(),
                         {"firstName": "Semen", "lastName": "Protas", "balance": 1, "number": "0123456789",
                          "cards": [{"cardNum": "0123456789012345", "cardPIN": "1234", "status": "lock"}]})


if __name__ == '__main__':
    unittest.main()
