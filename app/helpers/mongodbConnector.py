from mongoengine import connect

class Connection:
    def connect_mongodb(self, connection_string="127.0.0.1:27017", database_name="my_db"):

        connect(host="mongodb://"+connection_string+"/"+database_name)