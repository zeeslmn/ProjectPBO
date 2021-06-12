import mysql.connector

class ModelUmum():
    
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="dekstop_rental"
    )

    #KERJA DISINI!

    def is_connected(self):
        if self.db.is_connected():
            return True