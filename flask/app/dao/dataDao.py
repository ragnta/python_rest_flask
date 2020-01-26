import abc

class DataDao(abc.ABC):
    @abc.abstractclassmethod
    def getAllElements(self):
        pass

    @abc.abstractclassmethod
    def getElementById(self, data_id):
        pass

    @abc.abstractclassmethod
    def updateElement(self, dataobject):
        pass

    @abc.abstractclassmethod
    def deleteElement(self, data_id):
        pass  