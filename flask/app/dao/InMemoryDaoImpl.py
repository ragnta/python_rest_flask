from . import DataDao
from . import DataModel

class InMemoryDaoImpl(DataDao):

    def __init__(self, elements):
        self.__elements = elements

    def getAllElements(self):
        return self.__elements

   
    def getElementById(self, data_id):
        element = list(filter(lambda t: t['id'] == data_id, self.__elements))
        if len(element) != 0:
            filtered = element[0]
        return filtered

    
    def updateElement(self, dataobject):
        for i,item in enumerate(self.__elements):
            if item==dataobject.__idNumber.id:
                self.__elements[i]=dataobject

   
    def deleteElement(self, data_id):
        newElements = list(filter(lambda t: t['id'] != data_id, self.__elements))
        self.__elements = newElements