from kivy.app import App

from presenter.presenter import Presenter
from view.gui_view.gui_view import MainWindow

databasePath = "database.json"


class ATM(App):
    def build(self):
        gui = MainWindow()
        presenter = Presenter(databasePath, gui)
        gui.set_presenter(presenter)
        return gui


def run():
    ATM().run()

if __name__ == '__main__':
    run()