class Medicine:
    def __init__(self, idNumber, barCode, shortBar, name, dosage, pieces):
        self.__idNumber = idNumber
        self.__barCode = barCode
        self.__shortBar = shortBar
        self.__name = name
        self.__dosage = dosage
        self.__pieces = pieces
        self.idNumber = idNumber

    def asdict(self):
        return {
        "id": self.__idNumber, 
        "name": self.__barCode, 
        "shortBar": self.__shortBar,
         "name": self.__name,
         "dosage": self.__dosage,
         "pieces": self.__pieces}