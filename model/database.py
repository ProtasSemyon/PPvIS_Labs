from datetime import date

from model.parserDOM import writeXML
from model.parserSAX import parse


class Database:
    __recordFields = ["Name", "DateOfBirth", "DateOfLastAppointment", "VetFULLNAME", "Diagnosis"]

    def __init__(self):
        self.__data = list()

    def load(self, filepath) -> None:
        self.__data = parse(filepath)

    def save(self, filepath) -> None:
        writeXML(filepath, self.__data)

    def getData(self) -> list:
        return self.__data

    def addRecord(self, record: dict) -> None:
        if sorted([*record.keys()]) != sorted(self.__recordFields):
            raise ValueError("Incorrect record!")
        else:
            self.__data.append(record)

    def searchByDiagnosis(self, diagnosis: str) -> list:
        result: list = list()
        for record in self.__data:
            if diagnosis in record["Diagnosis"]:
                result.append(record)
        return result

    def searchByNameAndDateOfBirth(self, name: str, dateOfBirth: date) -> list:
        result: list = list()
        for record in self.__data:
            if name == record["Name"] and dateOfBirth == record["DateOfBirth"]:
                result.append(record)
        return result

    def searchByVetNameAndDateOfLastAppointment(self, vetName: str, dateOfLastAppointment: date) -> list:
        result: list = list()
        for record in self.__data:
            if vetName == record["VetFULLNAME"] and dateOfLastAppointment == record["DateOfLastAppointment"]:
                result.append(record)
        return result

    def deleteByDiagnosis(self, diagnosis: str) -> int:
        delete = self.searchByDiagnosis(diagnosis)
        result = len(delete)
        for element in delete:
            self.__data.remove(element)
        return result

    def deleteByNameAndDateOfBirth(self, name: str, dateOfBirth: date) -> int:
        delete = self.searchByNameAndDateOfBirth(name, dateOfBirth)
        result = len(delete)
        for element in delete:
            self.__data.remove(element)
        return result

    def deleteByVetNameAndDateOfLastAppointment(self, vetName: str, dateOfLastAppointment: date) -> int:
        delete = self.searchByVetNameAndDateOfLastAppointment(vetName, dateOfLastAppointment)
        result = len(delete)
        for element in delete:
            self.__data.remove(element)
        return result


if __name__ == "__main__":
    data = Database()
    data.load("../data/database.xml")
    data.save("../data/database.xml")
    try:
        data.addRecord({"Name": "Van Darknolm", "DateOfBirth": "1972-10-24", "DateOfLastAppointment": "2018-03-02",
                        "VetFULLNAME": "Billy Herrington", "Diagnosis": "Gay"})
    except ValueError:
        print("YOU GAY")
    data.save("../data/database.xml")
