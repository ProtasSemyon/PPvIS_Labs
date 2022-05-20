from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class DigitsPanel(BoxLayout):
    enter = ObjectProperty(None)
    back = ObjectProperty(None)
    success = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label()
        self.grid = GridLayout()
        self.grid.cols = 4
        for i in range(9):
            self.grid.add_widget(Button(text=str(i+1), on_press=self.inputProcessor))
        self.grid.add_widget(Button(text='0', on_press=self.inputProcessor))
        self.grid.add_widget(Button(text='Back', on_press=self.back))
        self.grid.add_widget(Button(text='Enter', on_press=self.inputInfo))
        self.grid.add_widget(Button(text='<', on_press=self.removeSymbol))
        self.grid.add_widget(Button(text='<<<', on_press=self.removeAllSymbol))

        self.add_widget(self.label)
        self.add_widget(self.grid)

    def inputProcessor(self, button):
        self.label.text = self.label.text + button.text

    def inputInfo(self, button):
        try:
            if self.enter(self.label.text):
                self.label.text = "Done"
                self.success(button)
            else:
                self.label.text = "Fail"
        except ValueError as error:
            self.label.text = 'Error:' + str(error)

    def removeSymbol(self, button):
        self.label.text = self.label.text[:-1]

    def removeAllSymbol(self, button):
        self.label.text = ""
