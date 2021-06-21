from models import dbcon

class modelPerangkatDesa(dbcon.dbModel):
    def show(self,orderby="nik"):
        self.orderby = orderby
        result = []
        query = "SELECT * FROM perangkatDesa ORDER BY {} ASC".format(self.orderby)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def getData(self, username=None, password=None):
        self.username = username
        self.password = password
        result = []
        query = "SELECT nik, username, password FROM perangkatDesa WHERE username='{}' AND password='{}'".format(self.username,self.password)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

    def getByid(self, id=1):
        self.id = id
        result = []
        query = "SELECT nik, nama, jabatan, username, password FROM perangkatDesa WHERE nik='{}'".format(self.id)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result

    def insert(self,nik,nama,jabatan,username,password,idadmin):
        self.nik = nik
        self.nama = nama
        self.jabatan = jabatan
        self.username = username
        self.password = password
        self.idadmin = idadmin
        query = "INSERT INTO perangkatDesa (nik,nama,jabatan,username,password,id_admin) VALUES ('{}','{}','{}','{}','{}','{}')".format(self.nik,self.nama,self.jabatan,self.username,self.password,self.idadmin)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()

    def update(self,nik,nama,jabatan,username,password,idadmin,oldid):
        self.nik = nik
        self.nama = nama
        self.jabatan = jabatan
        self.username = username
        self.password = password
        self.idadmin = idadmin
        self.oldid = oldid
        query = """UPDATE perangkatDesa 
                SET nik = '{}',
                nama = '{}',
                jabatan = '{}',
                username = '{}',
                password = '{}',
                id_admin = '{}'
                WHERE nik = '{}'""".format(self.nik,self.nama,self.jabatan,self.username,self.password,self.idadmin,self.oldid)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()

    def delete(self,id):
        self.id = id
        query = "DELETE FROM perangkatDesa WHERE nik = '{}'".format(self.id)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()

