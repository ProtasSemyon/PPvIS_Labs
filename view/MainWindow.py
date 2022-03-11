from datetime import date

from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from controller.Controller import Controller
from view.Dialog import OpenDialog, AddRecordDialog, SearchDialog, DeleteDialog
from view.Table import TableScreen

Builder.load_file("kv/ControllerPanel.kv")


class ControllerPanel(BoxLayout):
    def __init__(self, myWindow, **kwargs):
        super().__init__(**kwargs)
        self.isOpened = False
        self.controller = Controller()
        self.popup = Popup()
        self.myWindow = myWindow

    def openDialog(self):
        content = OpenDialog(open=self.open, cancel=self.dismissPopup)
        self.popup = Popup(title="Open", content=content, size_hint=(0.7, 0.7))
        self.popup.open()

    def addRecordDialog(self):
        if not self.isOpened: return
        content = AddRecordDialog(add=self.addRecord, cancel=self.dismissPopup)
        self.popup = Popup(title="AddRecord", content=content, size_hint=(0.7, 0.7))
        self.popup.open()

    def searchDialog(self):
        if not self.isOpened: return
        content = SearchDialog(cancel=self.dismissPopup, search=self.search)
        self.popup = Popup(title="Search", content=content)
        self.popup.open()

    def deleteDialog(self):
        if not self.isOpened: return
        content = DeleteDialog(cancel=self.dismissPopup, delete=self.delete)
        self.popup = Popup(title="Delete", content=content)
        self.popup.open()

    def open(self, filename):
        try:
            self.myWindow.update(self.controller.openFile(filename[0]))
        except:
            pass
        self.dismissPopup()
        self.isOpened = True

    def save(self):
        if not self.isOpened: return
        self.controller.saveFile()

    def addRecord(self, **kwargs):
        if not self.isOpened: return
        try:
            dateBirth = date.fromisoformat(kwargs["DateOfBirth"])
            dateAppointment = date.fromisoformat(kwargs["DateOfLastAppointment"])
        except:
            print("LOX")
            self.dismissPopup()
            return
        kwargs["DateOfBirth"] = dateBirth
        kwargs["DateOfLastAppointment"] = dateAppointment
        self.controller.addRecord(kwargs)
        self.myWindow.update(self.controller.getData())
        self.dismissPopup()

    def search(self, searchData: dict) -> dict:
        if not self.isOpened: return
        try:
            if "Diagnosis" in searchData.keys():
                return self.controller.searchByDiagnosis(searchData["Diagnosis"])
            elif "Name" in searchData.keys() and "DateOfBirth" in searchData.keys():
                searchData["DateOfBirth"] = date.fromisoformat(searchData["DateOfBirth"])
                return self.controller.searchByNameAndDateOfBirth(searchData["Name"], searchData["DateOfBirth"])
            elif "VetFULLNAME" in searchData.keys() and "DateOfLastAppointment" in searchData.keys():
                searchData["DateOfLastAppointment"] = date.fromisoformat(searchData["DateOfLastAppointment"])
                return self.controller.searchByVetNameAndDateOfLastAppointment(searchData["VetFULLNAME"],
                                                                               searchData["DateOfLastAppointment"])
        except:
            return []

    def delete(self, deleteData: dict):
        if not self.isOpened: return
        try:
            if "Diagnosis" in deleteData.keys():
                return self.controller.deleteByDiagnosis(deleteData["Diagnosis"])
            elif "Name" in deleteData.keys() and "DateOfBirth" in deleteData.keys():
                deleteData["DateOfBirth"] = date.fromisoformat(deleteData["DateOfBirth"])
                return self.controller.deleteByNameAndDateOfBirth(deleteData["Name"], deleteData["DateOfBirth"])
            elif "VetFULLNAME" in deleteData.keys() and "DateOfLastAppointment" in deleteData.keys():
                deleteData["DateOfLastAppointment"] = date.fromisoformat(deleteData["DateOfLastAppointment"])
                return self.controller.deleteByVetNameAndDateOfLastAppointment(deleteData["VetFULLNAME"],
                                                                               deleteData["DateOfLastAppointment"])
        except:
            return 0
        self.myWindow.update(self.controller.getData())

    def dismissPopup(self, *args):
        self.popup.dismiss()


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.table = TableScreen([])
        self.controller = ControllerPanel(self, size_hint=(1, 0.1))

        self.add_widget(self.table)
        self.add_widget(self.controller)

    def update(self, data: list):
        self.table.update(data)
