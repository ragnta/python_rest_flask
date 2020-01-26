import csv

class Reader:

    @staticmethod
    def getListOfData():
        listOfData=[]
        csv_reader = csv.reader( open("app/data.csv"), delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                listOfData.append({"id": row[0], "numData": row[1], "orderNum": row[2]})
            line_count += 1
        return listOfData