import wx
import core
from models import modeladmin
from models import modelperangkatdesa
from models import modelpenduduk



class MainApp(wx.App):
    def OnInit(self):
        self.frame = turunanHome(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

class turunanHome(core.Home):
    def __init__(self,parent):
        core.Home.__init__(self,parent)

    def m_menuHomeOnMenuSelection( self, event ):
        event.Skip()

    def m_menuLoginOnMenuSelection( self, event ):
		# event.Skip()
        self.login = turunanLogin(None)
        self.Destroy()
        self.login.Show()

    def m_bpButton1OnButtonClick( self, event ):
		# event.Skip()
        self.infoBantuan = turunaninformasiBantuan(None)
        self.Destroy()
        self.infoBantuan.Show()

    def m_bpButton2OnButtonClick( self, event ):
		# event.Skip()
        self.infoPenerimaan = turunanCekPenerimaanBantuan(None)
        self.Destroy()
        self.infoPenerimaan.Show()

    def btnInformasiBantuanOnButtonClick( self, event ):
		# event.Skip()
        self.infoBantuan = turunaninformasiBantuan(None)
        self.Destroy()
        self.infoBantuan.Show()
    
    def btnPenerimaanBantuanOnButtonClick( self, event ):
		# event.Skip()
        self.infoPenerimaan = turunanCekPenerimaanBantuan(None)
        self.Destroy()
        self.infoPenerimaan.Show()

class turunanCekPenerimaanBantuan(core.cekPenerimaBantuan):
    def __init__(self,parent):
        core.cekPenerimaBantuan.__init__(self,parent)

    def m_menuHomeOnMenuSelection( self, event ):
		# event.Skip()
        self.frame = turunanHome(None)
        self.Destroy()
        self.frame.Show()

    def m_menuLoginOnMenuSelection( self, event ):
		# event.Skip()
        self.login = turunanLogin(None)
        self.Destroy()
        self.login.Show()

    def btnCariNikPendudukOnButtonClick( self, event ):
		# event.Skip()
        penduduk = modelpenduduk.modelPenduduk()
        datapenduduk = penduduk.getByid(str(self.m_textCtrl1.GetValue()))
        if int(datapenduduk[4]) < 1000000 :
            wx.MessageBox("NIK dengan nomor " + str(datapenduduk[0]) + "\nBerhak Mendapat Bantuan BLT" , "BANTUAN BLT", wx.OK | wx.ICON_INFORMATION)
        elif int(datapenduduk[4]) >= 1000000 and int(datapenduduk[4]) < 2000000:
            wx.MessageBox("NIK dengan nomor " + str(datapenduduk[0]) + "\nBerhak Mendapat Bantuan Beras RASKIN" , "BANTUAN BERAS RASKIN", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Mohon Maaf Anda Sudah Tidak Berhak Mendapat Bantuan", "ERROR", wx.OK | wx.ICON_ERROR)

class turunaninformasiBantuan(core.informasiBantuan):
    def __init__(self,parent):
        core.informasiBantuan.__init__(self,parent)

    def btnKembaliOnButtonClick( self, event ):
        self.frame = turunanHome(None)
        self.Destroy()
        self.frame.Show()

class turunanLogin(core.Login):
    def __init__(self,parent):
        core.Login.__init__(self,parent)

    def m_menuHomeOnMenuSelection( self, event ):
		# event.Skip()
        self.frame = turunanHome(None)
        self.Destroy()
        self.frame.Show()

    def m_buttonLoginOnButtonClick( self, event ):
		# event.Skip()
        admin = modeladmin.modelAdmin()
        desa = modelperangkatdesa.modelPerangkatDesa()
        dataAdmin = admin.getData(str(self.m_textCtrl2.GetValue()),str(self.m_textCtrl3.GetValue()))
        dataDesa = desa.getData(str(self.m_textCtrl2.GetValue()),str(self.m_textCtrl3.GetValue()))
        if dataAdmin != None:
            self.adminAkunDesa = turunanAdminAkunDesa(None,str(dataAdmin[0]))
            self.Destroy()
            self.adminAkunDesa.Show()
        elif dataDesa != None:
            self.sekretarisDesa = turunanSekretarisDesa(None,str(dataDesa[0]))
            self.Destroy()
            self.sekretarisDesa.Show()
        else:
            wx.MessageBox("Username Dan Password Salah", "ERROR", wx.OK | wx.ICON_ERROR)

class turunanSekretarisDesa(core.sekretarisDesa):
    def __init__(self,parent, id):
        core.sekretarisDesa.__init__(self,parent)
        self.id = id
        self.initData()

    def initData(self,orderby="dataPenduduk.id"):
        penduduk = modelpenduduk.modelPenduduk()
        dataPenduduk = penduduk.show(orderby)
        self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())

        self.m_grid2.AppendRows(len(dataPenduduk))

        for row in range(len(dataPenduduk)):
            for col in range(self.m_grid2.GetNumberCols()):
                val = dataPenduduk[row][col]
                self.m_grid2.SetCellValue(row,col,str(val))


    def m_menuItemlogoutOnMenuSelection( self, event ):
        dlg = wx.MessageBox("Yakin Mau Logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
        if dlg == 2:
            self.login = turunanLogin(None)
            self.Destroy()
            self.login.Show()

    def m_buttonsortirnikpendudukOnButtonClick( self, event ):
        self.initData()

    def m_buttonsortirterimabantuanOnButtonClick( self, event ):
        self.initData("dataPenduduk.status_penerimaan")

    def m_buttonsortirgajipendudukOnButtonClick( self, event ):
        self.initData("dataPenduduk.penghasilan")

    def m_buttontambahpendudukOnButtonClick( self, event ):
        dlg = turunanTambahDataPenduduk(None, self.id)
        dlg.ShowModal()

    def m_buttonhapuspendudukOnButtonClick( self, event ):
        deletependuduk = modelpenduduk.modelPenduduk()
        dlg = wx.MessageBox("Anda Yakin Ingin Hapus Data Dengan Nama " + str(self.m_grid2.GetCellValue(self.row,1)) +" ?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
        if dlg == 2:
            deletependuduk.delete(str(self.m_grid2.GetCellValue(self.row,0)))
            wx.MessageBox("Data berhasil dihapus", "Delete", wx.OK | wx.ICON_INFORMATION)


    def m_buttoneditpendudukOnButtonClick( self, event ):
        dlg = turunanEditDataPenduduk(None,self.m_grid2.GetCellValue(self.row,0),self.id)
        dlg.ShowModal()

    def m_grid2OnGridCmdSelectCell( self, event ):
        col = event.GetCol()
        self.row = event.GetRow()


class turunanAdminAkunDesa(core.adminAkunDesa):
    def __init__(self,parent, id):
        core.adminAkunDesa.__init__(self,parent)
        self.id = id
        self.initData()

    def initData(self,orderby="nik"):
        desa = modelperangkatdesa.modelPerangkatDesa()
        dataDesa = desa.show(orderby)
        self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())

        self.m_grid2.AppendRows(len(dataDesa))

        for row in range(len(dataDesa)):
            for col in range(self.m_grid2.GetNumberCols()):
                val = dataDesa[row][col]
                self.m_grid2.SetCellValue(row,col,str(val))

    def dataPendudukOnMenuSelection( self, event ):
        self.adminPenduduk = turunanAdminDataPenduduk(None,self.id)
        self.Destroy()
        self.adminPenduduk.Show()

    def m_menuItemlogoutOnMenuSelection( self, event ):
        dlg = wx.MessageBox("Yakin Mau Logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
        if dlg == 2:
            self.login = turunanLogin(None)
            self.Destroy()
            self.login.Show()

    def m_buttonsortiridakunOnButtonClick( self, event ):
        self.initData()

    def m_buttonsortirnamaOnButtonClick( self, event ):
        self.initData("nama")

    def m_buttonTambahDataDesaOnButtonClick( self, event ):
        dlg = turunanTambahDataAkunDesa(None, self.id)
        dlg.ShowModal()

    def m_buttonHapusDataDesaOnButtonClick( self, event ):
        deleteperangkat = modelperangkatdesa.modelPerangkatDesa()
        dlg = wx.MessageBox("Anda Yakin Ingin Hapus Data Dengan Nama " + str(self.m_grid2.GetCellValue(self.row,1)) +" ?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
        if dlg == 2:
            deleteperangkat.delete(str(self.m_grid2.GetCellValue(self.row,0)))
            wx.MessageBox("Data berhasil dihapus", "Delete", wx.OK | wx.ICON_INFORMATION)

    def m_buttonEditDataDesaOnButtonClick( self, event ):
        dlg = turunanEditDataAkunDesa(None,self.m_grid2.GetCellValue(self.row,0),self.id)
        dlg.ShowModal()


    def m_grid2OnGridCmdSelectCell( self, event ):
        col = event.GetCol()
        self.row = event.GetRow()


class turunanAdminDataPenduduk(core.adminDataPenduduk):
    def __init__(self,parent,id):
        core.adminDataPenduduk.__init__(self,parent)
        self.id = id
        self.initData()

    def initData(self,orderby="dataPenduduk.id"):
        penduduk = modelpenduduk.modelPenduduk()
        dataPenduduk = penduduk.show(orderby)
        self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())

        self.m_grid2.AppendRows(len(dataPenduduk))

        for row in range(len(dataPenduduk)):
            for col in range(self.m_grid2.GetNumberCols()):
                val = dataPenduduk[row][col]
                self.m_grid2.SetCellValue(row,col,str(val))

    def dataAkunDesaOnMenuSelection( self, event ):
		# event.Skip()
        self.adminAkunDesa = turunanAdminAkunDesa(None,self.id)
        self.Destroy()
        self.adminAkunDesa.Show()

    def m_menuItemlogoutOnMenuSelection( self, event ):
        dlg = wx.MessageBox("Yakin Mau Logout?", "Peringatan", wx.YES_NO | wx.ICON_INFORMATION)
        if dlg == 2:
            self.login = turunanLogin(None)
            self.Destroy()
            self.login.Show()

    def m_buttonsortirnikOnButtonClick( self, event ):
        self.initData()

    def m_buttonsortirpenerimaanbantuanOnButtonClick( self, event ):
        self.initData("dataPenduduk.status_penerimaan")

    def m_buttonsortirkeberhakanOnButtonClick( self, event ):
        self.initData("keberhakan.status")



class turunanTambahDataAkunDesa(core.tambahdataakundesa):
    def __init__(self,parent, id):
        core.tambahdataakundesa.__init__(self,parent)
        self.id = id

    def m_sdbSizer1OnCancelButtonClick( self, event ):
        self.Destroy()

    def m_sdbSizer1OnSaveButtonClick( self, event ):
        insertperangkat = modelperangkatdesa.modelPerangkatDesa()
        self.m_textCtrl20.GetValue()
        self.m_textCtrl21.GetValue()
        self.m_textCtrl22.GetValue()
        self.m_textCtrl23.GetValue()
        self.m_textCtrl24.GetValue()
        if self.m_textCtrl20.GetValue()=="" or self.m_textCtrl21.GetValue()=="" or self.m_textCtrl22.GetValue()=="" or self.m_textCtrl23.GetValue()=="" or self.m_textCtrl24.GetValue()=="":
            wx.MessageBox("Form Tidak Boleh Ada Yang Kosong", "ERROR", wx.OK | wx.ICON_ERROR)
        else:
            insertperangkat.insert(str(self.m_textCtrl20.GetValue()),str(self.m_textCtrl21.GetValue()),str(self.m_textCtrl22.GetValue()),str(self.m_textCtrl23.GetValue()),self.m_textCtrl24.GetValue(),str(self.id))
            wx.MessageBox("Data berhasil ditambah", "Insert", wx.OK | wx.ICON_INFORMATION)
            self.Destroy()


class turunanEditDataAkunDesa(core.editdataakundesa):
    def __init__(self,parent, id, idadmin):
        core.editdataakundesa.__init__(self,parent)
        perangkatdesa = modelperangkatdesa.modelPerangkatDesa()
        self.oldid = id
        self.idadmin = idadmin
        perangkatdesaid = perangkatdesa.getByid(self.oldid)
        self.m_textCtrl20.SetValue(str(perangkatdesaid[0]))
        self.m_textCtrl21.SetValue(str(perangkatdesaid[1]))
        self.m_textCtrl22.SetValue(str(perangkatdesaid[2]))
        self.m_textCtrl23.SetValue(str(perangkatdesaid[3]))
        self.m_textCtrl24.SetValue(str(perangkatdesaid[4]))

    def m_sdbSizer1OnCancelButtonClick( self, event ):
        self.Destroy()

    def m_sdbSizer1OnSaveButtonClick( self, event ):
        updateperangkat = modelperangkatdesa.modelPerangkatDesa()
        self.m_textCtrl20.GetValue()
        self.m_textCtrl21.GetValue()
        self.m_textCtrl22.GetValue()
        self.m_textCtrl23.GetValue()
        self.m_textCtrl24.GetValue()

        updateperangkat.update(str(self.m_textCtrl20.GetValue()),str(self.m_textCtrl21.GetValue()),str(self.m_textCtrl22.GetValue()),str(self.m_textCtrl23.GetValue()),str(self.m_textCtrl24.GetValue()),str(self.idadmin),str(self.oldid))
        wx.MessageBox("Data berhasil diubah", "Update", wx.OK | wx.ICON_INFORMATION)
        self.Destroy()

class turunanTambahDataPenduduk(core.tambahdatapenduduk):
    def __init__(self,parent, id):
        core.tambahdatapenduduk.__init__(self,parent)
        self.id = id

    def m_sdbSizer1OnCancelButtonClick( self, event ):
        self.Destroy()

    def m_sdbSizer1OnSaveButtonClick( self, event ):
        insertpenduduk = modelpenduduk.modelPenduduk()
        self.m_textCtrl20.GetValue()
        self.m_textCtrl21.GetValue()
        self.m_textCtrl22.GetValue()
        self.m_textCtrl23.GetValue()
        self.m_textCtrl24.GetValue()
        if self.m_textCtrl20.GetValue()=="" or self.m_textCtrl21.GetValue()=="" or self.m_textCtrl22.GetValue()=="" or self.m_textCtrl23.GetValue()=="" or self.m_textCtrl24.GetValue()=="":
            wx.MessageBox("Form Tidak Boleh Ada Yang Kosong", "ERROR", wx.OK | wx.ICON_ERROR)
        elif int(self.m_textCtrl24.GetValue()) >= 2500000 :
            insertpenduduk.insert(str(self.m_textCtrl20.GetValue()),str(self.m_textCtrl21.GetValue()),str(self.m_textCtrl22.GetValue()),str(self.m_textCtrl23.GetValue()),self.m_textCtrl24.GetValue(),str("Belum"),str(self.id),str(2))
            wx.MessageBox("Data berhasil ditambah", "Insert", wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        else:
            insertpenduduk.insert(str(self.m_textCtrl20.GetValue()),str(self.m_textCtrl21.GetValue()),str(self.m_textCtrl22.GetValue()),str(self.m_textCtrl23.GetValue()),self.m_textCtrl24.GetValue(),str("Belum"),str(self.id),str(1))
            wx.MessageBox("Data berhasil ditambah", "Insert", wx.OK | wx.ICON_INFORMATION)
            self.Destroy()


class turunanEditDataPenduduk(core.editdatapenduduk):
    def __init__(self,parent, id, idperangkat):
        core.editdatapenduduk.__init__(self,parent)
        penduduk = modelpenduduk.modelPenduduk()
        self.oldid = id
        self.idperangkat = idperangkat
        pendudukid = penduduk.getByid(self.oldid)
        self.m_textCtrl20.SetValue(str(pendudukid[0]))
        self.m_textCtrl21.SetValue(str(pendudukid[1]))
        self.m_textCtrl22.SetValue(str(pendudukid[2]))
        self.m_textCtrl23.SetValue(str(pendudukid[3]))
        self.m_textCtrl24.SetValue(str(pendudukid[4]))
        self.m_comboBox1.SetValue(str(pendudukid[5]))

    def m_sdbSizer7OnCancelButtonClick( self, event ):
        self.Destroy()

    def m_sdbSizer7OnSaveButtonClick( self, event ):
        updatependuduk = modelpenduduk.modelPenduduk()
        self.m_textCtrl20.GetValue()
        self.m_textCtrl21.GetValue()
        self.m_textCtrl22.GetValue()
        self.m_textCtrl23.GetValue()
        self.m_textCtrl24.GetValue()
        self.m_comboBox1.GetValue()
        
        updatependuduk.update(str(self.m_textCtrl20.GetValue()),str(self.m_textCtrl21.GetValue()),str(self.m_textCtrl22.GetValue()),str(self.m_textCtrl23.GetValue()),str(self.m_textCtrl24.GetValue()),str(self.m_comboBox1.GetValue()),str(self.idperangkat),str(1),str(self.oldid))
        wx.MessageBox("Data berhasil diubah", "Update", wx.OK | wx.ICON_INFORMATION)
        self.Destroy()



if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()

