import csv
 
class Reader:

    def getListOfData(self, csvReaderFileUrl):
        listOfData=[]
        csv_reader = csv.reader( open(csvReaderFileUrl), delimiter=',')
        for row in csv_reader:
                listOfData.append(row)
        return listOfData