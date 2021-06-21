from models import dbcon

#Untuk login admin 
class modelAdmin(dbcon.dbModel):
    def getData(self, username=None, password=None):
        self.username = username
        self.password = password
        result = [] #array yang berisi tupple 
        query = "SELECT username, password FROM admin WHERE username='{}' AND password='{}'".format(self.username,self.password)
        self.cur = self.conn.cursor() #memanggil metodh kursor dari sql lite
        self.cur.execute(query) #memanggil query dari sql lite >> self.cur berfungsi untuk koneksi db untuk dijadikan cursor
        result = self.cur.fetchone() #untuk mengambil data dalam 1 row 
        return result

# db = modelAdmin()
# print(db.getData("admin", "123"))