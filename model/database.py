import parserDOM
import parserSAX


class Database:
    __recordFields = ["Name", "DateOfBirth", "DateOfLastAppointment", "VetFULLNAME", "Diagnosis"]

    def __init__(self):
        self.__data = list()

    def load(self, filepath) -> None:
        self.__data = parserSAX.parse(filepath)

    def save(self, filepath) -> None:
        parserDOM.writeXML(filepath, self.__data)

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
