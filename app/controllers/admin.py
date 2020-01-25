class Admin:
    
    def __init__(self, dataDao):
        self.__dataDao = dataDao

    def getAllElement(self):
        return self.__dataDao.getAllElements()


    def updateElement(self, dataobject):
        self.__dataDao.updateElement(dataobject)

    def deleteElement(self, data_id):
        self.__dataDao.updateElement(data_id)