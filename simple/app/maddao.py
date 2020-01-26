from .madicines import Medicine

class MadDao:
    def  __init__(self, reader):
        self.__reader = reader

    def getAllMadicines(self):
        madicines = self.__reader.getListOfData("app/medsTypes.csv")
        mads = [Medicine(x[0], x[1], x[2], x[3], x[4], x[5])  for x in madicines]
        return mads
    
    def getMedicineById(self, id):
        madicines = self.__reader.getListOfData("app/medsTypes.csv")
        mads = [Medicine(x[0], x[1], x[2], x[3], x[4], x[5])  for x in madicines]
        element = list(filter(lambda t: t.idNumber == id, mads))
        if len(element) != 0:
            filtered = element[0]
        return filtered