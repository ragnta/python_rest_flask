class MadController:

    def __init__(self, MadDao):
        self.__MadDao = MadDao
    
    def getAllMedicienes(self):
        return self.__MadDao.getAllMadicines()

    def getMedicineById(self, id):
        return self.__MadDao.getMedicineById(id)
