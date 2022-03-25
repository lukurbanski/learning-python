import requests

class APIreader:
    def __init__(self, connection):
        self.connection = connection

    def connect_to_source(self,type):
        self.type = type
        print("Connection to: ", self.connection, " has been established. Type: ", self.type)

class APIreaderSpecific(APIreader):
    def mypriv_connection(self):
        print(self.connection)


ap = APIreaderSpecific("ODBCconnectionToSource")
ap.mypriv_connection()

def three_decimal_points(x):
    y = "%.3f" % x
    return y

print(three_decimal_points(50.384923))

def list_compr(x):
    w = [f"%.3f" % i for i in range(x)]
    return w
    
print(list_compr(5))