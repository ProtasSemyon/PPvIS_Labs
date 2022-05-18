from presenter.presenter import IPresenter


class IView:
    @staticmethod
    def start_atm():
        pass

    @staticmethod
    def set_presenter(presenter_init: IPresenter):
        pass
