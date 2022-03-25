import csv

class Reader():
    def __init__(self, blob_storage) -> None:
        self.blob_storage = blob_storage

    def get_container_name(self):
        """
        Test
        """
        txt = self.blob_storage
        return txt.split("@")[0].upper()
    
    def printer(self):
        print(self.blob_storage)

    def csv_reader(self,local_file):
        with open(local_file, 'r') as file:
            csvreader = csv.reader(file) 
            for row in csvreader:
                print(row) 
            # return csvreader

        

myreader = Reader("mycontainer@storageaccount")

print(myreader.get_container_name())

path = 'C:\\Users\\lurbanski\\OneDrive - Objectivity Sp. z o.o\\Tools ALL\\Databricks\\Data\\Newcosts.csv'

# plik = myreader.csv_reader(path)  

with open(path, 'r') as file:
    csvreader = csv.reader(file)
    d = {} 
    for row in csvreader:
        k,*v = row
        d[k] = v
    
    d.pop("ď»żID")

    print(d)




