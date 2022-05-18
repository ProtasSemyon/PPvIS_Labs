from view.cli_view import CLI_view
from presenter.presenter import Presenter

databasePath = "database.json"

def run():
    view: CLI_view = CLI_view()
    presenter: Presenter = Presenter(databasePath, view)
    view.set_presenter(presenter)
    presenter.start()

if __name__ == "__main__":
    run()
