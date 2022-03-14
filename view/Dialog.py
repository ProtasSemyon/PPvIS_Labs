from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from view.Table import TableScreen

Builder.load_file("kv/OpenDialog.kv")
Builder.load_file("kv/AddRecordDialog.kv")
Builder.load_file("kv/SelectModeDialog.kv")
Builder.load_file("kv/SearchDialog.kv")
Builder.load_file("kv/DeleteDialog.kv")


class OpenDialog(FloatLayout):
    open = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SelectModeDialog(BoxLayout):
    cancel = ObjectProperty(None)
    selectDiagnosis = ObjectProperty(None)
    selectNameAndDateOfBirth = ObjectProperty(None)
    selectVetNameAndDateOfLastAppointment = ObjectProperty(None)


class AddRecordDialog(FloatLayout):
    add = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SearchDialog(BoxLayout):
    cancel = ObjectProperty(None)
    search = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content = SelectModeDialog(cancel=self.cancel, selectDiagnosis=self.searchByDiagnosis,
                                   selectNameAndDateOfBirth=self.searchByNameAndDateOfBirth,
                                   selectVetNameAndDateOfLastAppointment=self.searchByVetNameAndDateOfLastAppointment)
        self.add_widget(content)

    def searchByDiagnosis(self):
        self.clear_widgets()
        grid = GridLayout(cols=2, spacing=15)

        textInput = TextInput()
        cancelButton = Button(text="Cancel")
        cancelButton.bind(on_press=self.cancel)
        searchButton = Button(text="Search")
        searchButton.bind(on_press=lambda start: self.startSearch({"Diagnosis": textInput.text}))

        grid.add_widget(Label(text="Diagnosis"))
        grid.add_widget(textInput)
        grid.add_widget(cancelButton)
        grid.add_widget(searchButton)

        self.add_widget(grid)

    def searchByNameAndDateOfBirth(self):
        self.clear_widgets()
        grid = GridLayout(cols=2, spacing=15)

        nameInput = TextInput()
        dateOfBirthInput = TextInput(text="YYYY-MM-DD")
        cancelButton = Button(text="Cancel")
        cancelButton.bind(on_press=self.cancel)
        searchButton = Button(text="Search")
        searchButton.bind(
            on_press=lambda start: self.startSearch({"Name": nameInput.text, "DateOfBirth": dateOfBirthInput.text}))

        grid.add_widget(Label(text="Name"))
        grid.add_widget(nameInput)
        grid.add_widget(Label(text="Date of birth"))
        grid.add_widget(dateOfBirthInput)
        grid.add_widget(cancelButton)
        grid.add_widget(searchButton)

        self.add_widget(grid)

    def searchByVetNameAndDateOfLastAppointment(self):
        self.clear_widgets()
        grid = GridLayout(cols=2, spacing=15)

        vetNameInput = TextInput()
        dateOfLastAppointment = TextInput(text="YYYY-MM-DD")
        cancelButton = Button(text="Cancel")
        cancelButton.bind(on_press=self.cancel)
        searchButton = Button(text="Search")
        searchButton.bind(on_press=lambda start: self.startSearch(
            {"VetFULLNAME": vetNameInput.text, "DateOfLastAppointment": dateOfLastAppointment.text}))

        grid.add_widget(Label(text="Vet fullname"))
        grid.add_widget(vetNameInput)
        grid.add_widget(Label(text="Date of last appointment"))
        grid.add_widget(dateOfLastAppointment)
        grid.add_widget(cancelButton)
        grid.add_widget(searchButton)

        self.add_widget(grid)

    def startSearch(self, searchData: dict):
        self.clear_widgets()
        table = TableScreen(self.search(searchData))
        closeButton = Button(text="Close", size_hint=(1, 0.1))
        closeButton.bind(on_press=self.cancel)
        box = BoxLayout(orientation="vertical")
        box.add_widget(table)
        box.add_widget(closeButton)

        self.add_widget(box)


class DeleteDialog(FloatLayout):
    cancel = ObjectProperty(None)
    delete = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content = SelectModeDialog(cancel=self.cancel, selectDiagnosis=self.deleteByDiagnosis,
                                   selectNameAndDateOfBirth=self.deleteByNameAndDateOfBirth,
                                   selectVetNameAndDateOfLastAppointment=self.deleteByVetNameAndDateOfLastAppointment)
        self.add_widget(content)

    def deleteByDiagnosis(self):
        self.clear_widgets()
        grid = GridLayout(cols=2, spacing=15)

        textInput = TextInput()
        cancelButton = Button(text="Cancel")
        cancelButton.bind(on_press=self.cancel)
        searchButton = Button(text="Delete")
        searchButton.bind(on_press=lambda start: self.startDelete({"Diagnosis": textInput.text}))

        grid.add_widget(Label(text="Diagnosis"))
        grid.add_widget(textInput)
        grid.add_widget(cancelButton)
        grid.add_widget(searchButton)

        self.add_widget(grid)

    def deleteByNameAndDateOfBirth(self):
        self.clear_widgets()
        grid = GridLayout(cols=2, spacing=15)

        nameInput = TextInput()
        dateOfBirthInput = TextInput(text="YYYY-MM-DD")
        cancelButton = Button(text="Cancel")
        cancelButton.bind(on_press=self.cancel)
        searchButton = Button(text="Delete")
        searchButton.bind(
            on_press=lambda start: self.startDelete({"Name": nameInput.text, "DateOfBirth": dateOfBirthInput.text}))

        grid.add_widget(Label(text="Name"))
        grid.add_widget(nameInput)
        grid.add_widget(Label(text="Date of birth"))
        grid.add_widget(dateOfBirthInput)
        grid.add_widget(cancelButton)
        grid.add_widget(searchButton)

        self.add_widget(grid)

    def deleteByVetNameAndDateOfLastAppointment(self):
        self.clear_widgets()
        grid = GridLayout(cols=2, spacing=15)

        vetNameInput = TextInput()
        dateOfLastAppointment = TextInput(text="YYYY-MM-DD")
        cancelButton = Button(text="Cancel")
        cancelButton.bind(on_press=self.cancel)
        searchButton = Button(text="Delete")
        searchButton.bind(on_press=lambda start: self.startDelete(
            {"VetFULLNAME": vetNameInput.text, "DateOfLastAppointment": dateOfLastAppointment.text}))

        grid.add_widget(Label(text="Vet fullname"))
        grid.add_widget(vetNameInput)
        grid.add_widget(Label(text="Date of last appointment"))
        grid.add_widget(dateOfLastAppointment)
        grid.add_widget(cancelButton)
        grid.add_widget(searchButton)

        self.add_widget(grid)

    def startDelete(self, deleteData: dict):
        self.clear_widgets()
        label = Label(text="You delete " + str(self.delete(deleteData)) + " records")
        closeButton = Button(text="Close", size_hint=(1, 0.1))
        closeButton.bind(on_press=self.cancel)
        box = BoxLayout(orientation="vertical")
        box.add_widget(label)
        box.add_widget(closeButton)

        self.add_widget(box)
