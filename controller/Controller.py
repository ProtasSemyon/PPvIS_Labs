from datetime import date

from model.database import Database


class Controller:
    def __init__(self):
        self.data = Database()
        self.filepath = ""

    def openFile(self, filepath: str):
        self.filepath = filepath
        self.data.load(self.filepath)
        return self.data.getData()

    def saveFile(self):
        if self.filepath == "": return
        self.data.save(self.filepath)

    def addRecord(self, record: dict):
        try:
            self.data.addRecord(record)
        except ValueError:
            pass

    def searchByDiagnosis(self, diagnosis: str):
        return self.data.searchByDiagnosis(diagnosis)

    def searchByNameAndDateOfBirth(self, name: str, dateOfBirth: date) -> list:
        return self.data.searchByNameAndDateOfBirth(name, dateOfBirth)

    def searchByVetNameAndDateOfLastAppointment(self, vetName: str, dateOfLastAppointment: date) -> list:
        return self.data.searchByVetNameAndDateOfLastAppointment(vetName, dateOfLastAppointment)

    def deleteByDiagnosis(self, diagnosis: str) -> int:
        return self.data.deleteByDiagnosis(diagnosis)

    def deleteByNameAndDateOfBirth(self, name: str, dateOfBirth: date) -> int:
        return self.data.deleteByNameAndDateOfBirth(name, dateOfBirth)

    def deleteByVetNameAndDateOfLastAppointment(self, vetName: str, dateOfLastAppointment: date) -> int:
        return self.data.deleteByVetNameAndDateOfLastAppointment(vetName, dateOfLastAppointment)

    def getData(self):
        return self.data.getData()
