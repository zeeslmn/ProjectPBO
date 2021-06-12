import wx
from wx.core import NOT_FOUND
import wx.xrc
import FrameSewa as frame

import model_admin
import model_customer
import transaksi


class SubClassFrame_Home_Karyawan(frame.Frame_Home_Karyawan):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model_admin = model_admin.ModelKaryawan()
        self.model_customer = model_customer.ModelPelanggan()
        self.transaksi = transaksi.ModelTransaksi()

        self.choice_kode_barang.SetItems([("A{}".format(i+1)) for i in range(10)])
        self.choice_jaminan.SetItems(["KTP", "SIM"])

        self.id_pinjam, self.value_pinjam = self.transaksi.get_transaksi()

        for num in range(len(self.id_pinjam)):
            self.grid_daftar_peminjaman.SetRowLabelValue(num, str(self.id_pinjam[num]))
            
        for i in range(len(self.value_pinjam)):
            for j in range(len(self.value_pinjam[0])):
                if self.value_pinjam[i][j] is None:
                    self.grid_daftar_peminjaman.SetCellValue(i, j, "-Belum Kembali-")
                else:
                    self.grid_daftar_peminjaman.SetCellValue(i, j, str(self.value_pinjam[i][j]))

        self.id_pinjam2, self.value_pinjam2 = self.transaksi.get_transaksi_berlangsung()

        for num in range(len(self.id_pinjam2)):
            self.grid_daftar_peminjaman2.SetRowLabelValue(num, str(self.id_pinjam2[num]))
            
        for i in range(len(self.value_pinjam2)):
            for j in range(len(self.value_pinjam2[0])):
                if self.value_pinjam2[i][j] is None:
                    self.grid_daftar_peminjaman2.SetCellValue(i, j, "-Belum Kembali-")
                else:
                    self.grid_daftar_peminjaman2.SetCellValue(i, j, str(self.value_pinjam2[i][j]))

        self.choice_pengembalian.SetItems([str(i) for i in self.id_pinjam2])

        self.pelanggan = self.model_customer.get_all_data()

        for i in range(len(self.pelanggan)):
            for j in range(len(self.pelanggan[0])):
                self.grid_daftar_pelanggan.SetCellValue(i, j, str(self.pelanggan[i][j]))


    def refresh_table(self):

        self.id_pinjam, self.value_pinjam = self.transaksi.get_transaksi()

        for num in range(len(self.id_pinjam)):
            self.grid_daftar_peminjaman.SetRowLabelValue(num, str(self.id_pinjam[num]))
            
        for i in range(len(self.value_pinjam)):
            for j in range(len(self.value_pinjam[0])):
                if self.value_pinjam[i][j] is None:
                    self.grid_daftar_peminjaman.SetCellValue(i, j, "-Belum Kembali-")
                else:
                    self.grid_daftar_peminjaman.SetCellValue(i, j, str(self.value_pinjam[i][j]))

        self.id_pinjam2, self.value_pinjam2 = self.transaksi.get_transaksi_berlangsung()

        for num in range(len(self.id_pinjam2)):
            self.grid_daftar_peminjaman2.SetRowLabelValue(num, str(self.id_pinjam2[num]))
            
        for i in range(len(self.value_pinjam2)):
            for j in range(len(self.value_pinjam2[0])):
                if self.value_pinjam2[i][j] is None:
                    self.grid_daftar_peminjaman2.SetCellValue(i, j, "-Belum Kembali-")
                else:
                    self.grid_daftar_peminjaman2.SetCellValue(i, j, str(self.value_pinjam2[i][j]))

        self.choice_pengembalian.SetItems([str(i) for i in self.id_pinjam2])

        self.pelanggan = self.model_customer.get_all_data()

        for i in range(len(self.pelanggan)):
            for j in range(len(self.pelanggan[0])):
                self.grid_daftar_pelanggan.SetCellValue(i, j, str(self.pelanggan[i][j]))


    def submit_data_peminjaman( self, event ):
        kode_barang_choice = self.choice_kode_barang.GetString(self.choice_kode_barang.GetSelection())
        username_input = self.input_username.GetValue()
        jaminan_choice = self.choice_jaminan.GetString(self.choice_jaminan.GetSelection())

        self.transaksi.input_transaksi(kode_barang_choice, username_input, jaminan_choice)

        self.choice_kode_barang.SetSelection(NOT_FOUND)
        self.input_username.SetValue(str())
        self.choice_jaminan.SetSelection(NOT_FOUND)

        self.refresh_table()


    def submit_data_pengembalian( self, event ):
        pengembalian_choice = self.choice_pengembalian.GetString(self.choice_pengembalian.GetSelection())
        
        self.transaksi.pengembalian_barang(pengembalian_choice)
        
        self.refresh_table()

    def submit_data_pelanggan( self, event ):
        username_input = self.input_username_pelanggan.GetValue()
        nama_input = self.input_nama_lengkap.GetValue()
        telp_input = self.input_nomor_telepon.GetValue()
        alamat_input = self.input_alamat_lengkap.GetValue()
        pass_input = self.input_password_pelanggan.GetValue()

        self.model_customer.input_pelanggan(username_input, nama_input, telp_input, alamat_input, pass_input)

        self.input_nama_lengkap.SetValue(str())
        self.input_nomor_telepon.SetValue(str())
        self.input_alamat_lengkap.SetValue(str())
        self.input_password_pelanggan.SetValue(str())



class SubClassFrame_Home_Pelanggan(frame.Frame_Home_Pelanggan):
    def __init__(self, username, parent=None):
        super().__init__(parent)

        self.username = username
        self.model_admin = model_admin.ModelKaryawan()
        self.model_customer = model_customer.ModelPelanggan()
        self.transaksi = transaksi.ModelTransaksi()

        self.id_pinjam, self.value_pinjam = self.transaksi.get_transaksi_username(self.username)

        for num in range(len(self.id_pinjam)):
            self.grid_daftar_peminjaman1.SetRowLabelValue(num, str(self.id_pinjam[num]))
            
        for i in range(len(self.value_pinjam)):
            for j in range(len(self.value_pinjam[0])):
                if self.value_pinjam[i][j] is None:
                    self.grid_daftar_peminjaman1.SetCellValue(i, j, "-Belum Kembali-")
                else:
                    self.grid_daftar_peminjaman1.SetCellValue(i, j, str(self.value_pinjam[i][j]))



class SubClassFrame_Login(frame.Frame_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model_admin = model_admin.ModelKaryawan()
        self.model_customer = model_customer.ModelPelanggan()

    def submit_login(self, event):
        username = self.username_input.GetValue()
        password = self.password_input.GetValue()
        login_as = self.choice_login.GetSelection()

        if login_as == 0:
            auth_login = self.model_admin.auth_login(username, password)
            print(auth_login)
            if auth_login == True:
                frame_new = SubClassFrame_Home_Karyawan()
                frame_new.Show()
                self.Close()

        else:
            auth_login = self.model_customer.auth_login(username, password)
            print(auth_login)
            if auth_login == True:
                frame_new = SubClassFrame_Home_Pelanggan(username)
                frame_new.Show()
                self.Close()

        self.username_input.SetValue(str())
        self.password_input.SetValue(str())

class Init_Main():

    def __init__(self):
        app = wx.App()
        frame = SubClassFrame_Login()
        frame.Show()
        app.MainLoop()
    

if __name__ == "__main__":
	login = Init_Main()
