import sqlite3

class dbModel:
    def __init__(self):
        self.conn = sqlite3.connect("models\ebansosdatabase.db")

    

# db = dbModel()
# print(db.getData())