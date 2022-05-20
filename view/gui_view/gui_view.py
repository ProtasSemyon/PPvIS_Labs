from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from presenter.presenter import IPresenter
from view.gui_view.digits_panel import DigitsPanel
from view.iview import IView


class MainWindow(IView, BoxLayout):
    def __init__(self):
        super().__init__()
        self.presenter: IPresenter
        self.orientation = 'vertical'
        self.add_widget(Label())
        self.add_widget(Button(text='Insert card', on_press=self.insertCard))
        self.add_widget(Label())
        self.__cards = []

        self.phone = None

    def set_presenter(self, presenter_init: IPresenter):
        self.presenter = presenter_init
        self.__cards = self.presenter.getCards()

    def getCard(self, button):
        self.presenter.changeInsertedState()
        self.presenter.endWork()

        self.clear_widgets()
        self.add_widget(Label(text='Goodbye!'))
        self.add_widget(Button(text='Exit', on_press=self.exit, size_hint=(1, 0.1)))

    def insertCard(self, button):
        self.clear_widgets()
        for card in self.__cards:
            self.add_widget(Button(text=card.getNumber(), on_press=self.selectCard))

    def selectCard(self, card: Button):
        for i, currCard in enumerate(self.__cards):
            if card.text == currCard.getNumber():
                self.presenter.selectCard(i + 1)
        self.enterPin()

    def enterPin(self):
        self.clear_widgets()
        digitsPanel = DigitsPanel(enter=self.presenter.enterPin, back=self.getCard, success=self.selectOption)
        self.add_widget(digitsPanel)

    def selectOption(self, button):
        self.clear_widgets()
        self.add_widget(Button(text='View balance', on_press=self.viewBalance))
        self.add_widget(Button(text='Withdraw money', on_press=self.withdrawMoney))
        self.add_widget(Button(text='Phone payment', on_press=self.phonePayment))
        self.add_widget(Button(text='Get card', on_press=self.getCard))

    def viewBalance(self, button):
        self.clear_widgets()
        self.add_widget(Label(text=str(self.presenter.getCardBalance())))
        self.add_widget(Button(text='Back', on_press=self.selectOption, size_hint=(1, 0.1)))

    def withdrawMoney(self, button):
        self.clear_widgets()
        self.add_widget(DigitsPanel(enter=self.outputMoney, back=self.selectOption, success=None))

    def outputMoney(self, amount):
        cash = self.presenter.withdrawMoney(amount)
        self.clear_widgets()
        for nominal in cash.keys():
            if cash[nominal] != 0:
                self.add_widget(Label(text=str(nominal) + "x" + str(cash[nominal])))
        self.add_widget(Button(text='Back', on_press=self.selectOption, size_hint=(1, 0.2)))

    def phonePayment(self, button):
        self.clear_widgets()
        self.add_widget(DigitsPanel(enter=self.inputAmount, back= self.selectOption, success=None))

    def inputAmount(self, phone):
        self.presenter.checkCorrectPhone(phone)
        self.phone = phone
        self.clear_widgets()
        self.add_widget(DigitsPanel(enter=self.makePayment, back = self.selectOption))

    def makePayment(self, amount):
        self.presenter.makeTelephonePayment(amount, self.phone)
        self.clear_widgets()
        self.add_widget(Label(text='Done'))
        self.add_widget(Button(text='Back', on_press=self.selectOption, size_hint=(1, 0.1)))

    def exit(self, button):
        quit()
