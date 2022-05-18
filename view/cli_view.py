import click
from view.iview import IView
from presenter.presenter import IPresenter


presenter: IPresenter

class CLI_view(IView):
    @click.group()
    @staticmethod
    def start_atm():
        pass

    @start_atm.command('get_card')
    @staticmethod
    def getCard():
        if presenter.isCardInserted():
            presenter.changeInsertedState()
        presenter.endWork()

    @start_atm.command('insert_card')
    @click.option('-n', '--number', default=-1)
    @staticmethod
    def insertCard(number):
        if presenter.isCardInserted():
            print('Card inserted')
            return
        if number == -1:
            currentNum = 1
            for card in presenter.getCards():
                print(str(currentNum) + " - " + card.getNumber())
                currentNum += 1
        else:
            try:
                presenter.selectCard(number)
            except ValueError as error:
                print("Error: ", error)
        presenter.endWork()

    @start_atm.command('enter_pin')
    @click.option('-p', '--password', prompt='PIN', hide_input=True)
    @staticmethod
    def enterPin(password):
        try:
            if presenter.enterPin(password):
                print('Success')
            else:
                print('Incorrect PIN')
        except ValueError as error:
            print('Error:', error)
        presenter.endWork()

    @start_atm.command('view_balance')
    @staticmethod
    def viewBalance():
        try:
            print(presenter.getCardBalance())
        except ValueError as error:
            print('Error:', error)

    @start_atm.command('withdraw_money')
    @click.option('-a', '--amount', prompt='Input amount')
    @staticmethod
    def withdrawMoney(amount):
        try:
            cash = presenter.withdrawMoney(amount)
        except ValueError as error:
            print("Error:", error)
        else:
            for nominal in cash.keys():
                if cash[nominal] != 0:
                    print(str(nominal) + "x" + str(cash[nominal]))
        presenter.endWork()

    @start_atm.command('phone_payment')
    @click.option('-p', '--phone', prompt='Input phone')
    @click.option('-a', '--amount', prompt='Input amount')
    @staticmethod
    def phonePayment(phone, amount):
        try:
            presenter.makeTelephonePayment(amount, phone)
        except ValueError as error:
            print("Error:", error)
        else:
            print('Success')
        presenter.endWork()

    @staticmethod
    def set_presenter(presenter_init: IPresenter):
        global presenter
        presenter = presenter_init
