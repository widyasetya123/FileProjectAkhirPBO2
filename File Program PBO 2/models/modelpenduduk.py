from models import dbcon

#Untuk kelas data penduduk 
class modelPenduduk(dbcon.dbModel):
    def show(self,orderby="dataPenduduk.id"): #untuk menampilkan data penduduk 
        self.orderby = orderby #Untuk menampilkan semua data berdasarkan kolom tabel (kolom nama dari yg terkecil - terbesar)
        result = []
        query = "SELECT dataPenduduk.id,nama,alamat,pekerjaan,penghasilan,status_penerimaan,status FROM dataPenduduk JOIN keberhakan ON dataPenduduk.id_keberhakan = keberhakan.id ORDER BY {} ASC".format(self.orderby)
        self.cur = self.conn.cursor() #memanggil metodh kursor dari sql lite
        self.cur.execute(query) #memanggil query dari sql lite >> self.cur berfungsi untuk koneksi db untuk dijadikan cursor
        result = self.cur.fetchall() #untuk mengambil semua data 
        return result
#select data berdasarkan urutan id/NIK 
    def getByid(self, id=1):
        self.id = id
        result = []
        query = "SELECT dataPenduduk.id,nama,alamat,pekerjaan,penghasilan,status_penerimaan FROM dataPenduduk JOIN keberhakan ON dataPenduduk.id_keberhakan = keberhakan.id WHERE dataPenduduk.id = {}".format(self.id)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        result = self.cur.fetchone() #untuk mengambil data dalam 1 row 
        return result
#menambahkan data penduduk pada sekertaris desa 
    def insert(self,id,nama,alamat,pekerjaan,penghasilan,status_penerimaan,id_perangkatDesa,id_keberhakan):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.pekerjaan = pekerjaan
        self.penghasilan = penghasilan
        self.status_penerimaan = status_penerimaan
        self.id_perangkatDesa = id_perangkatDesa
        self.id_keberhakan = id_keberhakan
        query = "INSERT INTO dataPenduduk (id,nama,alamat,pekerjaan,penghasilan,status_penerimaan,id_perangkatDesa,id_keberhakan) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(self.id,self.nama,self.alamat,self.pekerjaan,self.penghasilan,self.status_penerimaan,self.id_perangkatDesa,self.id_keberhakan)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit() 
#mengedit data penduduk pada sekertaris desa 
    def update(self,id,nama,alamat,pekerjaan,penghasilan,status_penerimaan,id_perangkatDesa,id_keberhakan,oldid):
        self.oldid = oldid #variabel id nik yang belum diperbarui 
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.pekerjaan = pekerjaan
        self.penghasilan = penghasilan
        self.status_penerimaan = status_penerimaan
        self.id_perangkatDesa = id_perangkatDesa
        self.id_keberhakan = id_keberhakan
        query = """UPDATE dataPenduduk 
                SET id = '{}', 
                nama = '{}', 
                alamat = '{}', 
                pekerjaan = '{}', 
                penghasilan = '{}', 
                status_penerimaan = '{}', 
                id_perangkatDesa = '{}', 
                id_keberhakan = '{}' 
                WHERE id = '{}'""".format(self.id, self.nama, self.alamat, self.pekerjaan, self.penghasilan, self.status_penerimaan, self.id_perangkatDesa, self.id_keberhakan, self.oldid)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit() 
#menghapus data penduduk pada sekertaris desa 
    def delete(self,id):
        self.id = id
        query = "DELETE FROM dataPenduduk WHERE id = '{}'".format(self.id)
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()
    
