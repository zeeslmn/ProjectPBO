from datetime import date, datetime
import locale

from wx.core import Locale
from conn import ModelUmum

class ModelTransaksi(ModelUmum):
    
    def __init__(self) -> None:
        super().__init__()
    
    def input_transaksi(self, kode_barang_choice, username_input, jaminan_choice):
        cursor = self.db.cursor()

        tanggal_sewa = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        sql_query = """INSERT INTO transaksi VALUES ("", %s, %s, NULL, %s, %s)"""
        values = (kode_barang_choice, tanggal_sewa, username_input, jaminan_choice)
        cursor.execute(sql_query, values)

        self.db.commit()
        return True

    def get_harga(self, kode_barang):
        if kode_barang == "A1" or kode_barang == "A2" or kode_barang == "A3" or kode_barang == "A4" or kode_barang == "A5":
            return 100000
        else:
            return 75000


    def get_hari(self, date_start, date_end):
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')

        if date_end == None:
            date_start = datetime.strptime(date_start, "%d/%m/%Y, %H:%M:%S")
            return abs((datetime.now() - date_start).days)

        else:
            date_start = datetime.strptime(date_start, "%d/%m/%Y, %H:%M:%S")
            date_end = datetime.strptime(date_end, "%d/%m/%Y, %H:%M:%S")
            return abs((date_end - date_start).days)

    

    def get_transaksi(self):
        cursor = self.db.cursor()
        sql_query = """SELECT * FROM transaksi"""
        cursor.execute(sql_query)

        result = cursor.fetchall()

        id_pinjam = []
        value_pinjam = []

        for i in result:
            temp = []
            for idx, j in enumerate(i):
                if idx == 0:
                    id_pinjam.append(i[0])
                else:
                    temp.append(j)
            value_pinjam.append(temp)


        for i in value_pinjam:
            for idx, j in enumerate(i):
                if idx == 0:
                    harga = self.get_harga(i[0])

                elif idx == 1:
                    hari = self.get_hari(i[1], i[2])

            i.append(hari)
            i.append(hari * harga)


        return id_pinjam, value_pinjam

    def get_transaksi_berlangsung(self):
        cursor = self.db.cursor()
        sql_query = """SELECT * FROM transaksi WHERE tanggal_kembali IS NULL"""
        cursor.execute(sql_query)

        result = cursor.fetchall()

        id_pinjam = []
        value_pinjam = []

        for i in result:
            temp = []
            for idx, j in enumerate(i):
                if idx == 0:
                    id_pinjam.append(i[0])
                else:
                    temp.append(j)
            value_pinjam.append(temp)

        for i in value_pinjam:
            for idx, j in enumerate(i):
                if idx == 0:
                    harga = self.get_harga(i[0])

                elif idx == 1:
                    hari = self.get_hari(i[1], i[2])

            i.append(hari)
            i.append(hari * harga)

        return id_pinjam, value_pinjam


    def get_transaksi_username(self, username):
        cursor = self.db.cursor()
        sql_query = """SELECT * FROM transaksi WHERE username_pelanggan = %s"""
        value = (username,)
        cursor.execute(sql_query, value)

        result = cursor.fetchall()

        id_pinjam = []
        value_pinjam = []

        for i in result:
            temp = []
            for idx, j in enumerate(i):
                if idx == 0:
                    id_pinjam.append(i[0])
                elif idx == 4:
                    continue
                else:
                    temp.append(j)
            value_pinjam.append(temp)


        for i in value_pinjam:
            for idx, j in enumerate(i):
                if idx == 0:
                    harga = self.get_harga(i[0])

                elif idx == 1:
                    hari = self.get_hari(i[1], i[2])

            i.append(hari)
            i.append(hari * harga)


        return id_pinjam, value_pinjam



    def pengembalian_barang(self, pengembalian_choice):
        cursor = self.db.cursor()

        tanggal_kembali = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        sql_query = """UPDATE transaksi SET tanggal_kembali = %s WHERE id_transaksi = %s"""
        values = (tanggal_kembali, pengembalian_choice)
        cursor.execute(sql_query, values)

        self.db.commit()

    



