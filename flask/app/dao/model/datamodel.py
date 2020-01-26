class DataModel:

    def __init__(self, idNumber, name, timeStamp):
        self.__idNumber = idNumber
        self.__name = name
        self.__timeStamp = timeStamp

    def asdict(self):
        return {"id": self.__idNumber, "name": self.__name, "createdDate": self.__timeStamp }
