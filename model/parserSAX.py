import xml.sax
from datetime import date
from xml.sax import make_parser, handler


class DataHandler(handler.ContentHandler):
    def __init__(self, contentList: list):
        super().__init__()
        self.__contentList = contentList
        self.__currentRecord = dict()
        self.__name = False
        self.__dateOfBirth = False
        self.__dateOfLastAppointment = False
        self.__vetFULLNAME = False
        self.__diagnosis = False

    def startElement(self, tag, attrs):
        if tag == "Record":
            self.__currentRecord = dict()
        if tag == "Name":
            self.__name = True
        if tag == "DateOfBirth":
            self.__dateOfBirth = True
        if tag == "DateOfLastAppointment":
            self.__dateOfLastAppointment = True
        if tag == "VetFULLNAME":
            self.__vetFULLNAME = True
        if tag == "Diagnosis":
            self.__diagnosis = True

    def endElement(self, tag):
        if tag == "Record":
            self.__contentList.append(self.__currentRecord)
        if tag == "Name":
            self.__name = False
        if tag == "DateOfBirth":
            self.__dateOfBirth = False
        if tag == "DateOfLastAppointment":
            self.__dateOfLastAppointment = False
        if tag == "VetFULLNAME":
            self.__vetFULLNAME = False
        if tag == "Diagnosis":
            self.__diagnosis = False

    def characters(self, content):
        if self.__name:
            self.__currentRecord.update({"Name": content})
        if self.__dateOfBirth:
            d = date.fromisoformat(content)
            self.__currentRecord.update({"DateOfBirth": d})
        if self.__dateOfLastAppointment:
            d = date.fromisoformat(content)
            self.__currentRecord.update({"DateOfLastAppointment": d})
        if self.__vetFULLNAME:
            self.__currentRecord.update({"VetFULLNAME": content})
        if self.__diagnosis:
            self.__currentRecord.update({"Diagnosis": content})


def parse(filepath: str) -> list:
    out: list = list()
    parser = make_parser()
    parser.setContentHandler(DataHandler(out))
    parser.parse(filepath)
    return out


if __name__ == "__main__":
    data: list = list()
    xml.sax.parse("../data/database.xml", DataHandler(data))
    print(data)
