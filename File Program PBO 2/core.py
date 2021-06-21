# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Home
###########################################################################

class Home ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"E-BANSOS", pos = wx.DefaultPosition, size = wx.Size( 518,345 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		self.Home = wx.MenuBar( 0 )
		self.fitur1 = wx.Menu()
		self.m_menuHome = wx.MenuItem( self.fitur1, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.fitur1.Append( self.m_menuHome )

		self.Home.Append( self.fitur1, u"Home" )

		self.fitur2 = wx.Menu()
		self.m_menuLogin = wx.MenuItem( self.fitur2, wx.ID_ANY, u"Login", wx.EmptyString, wx.ITEM_NORMAL )
		self.fitur2.Append( self.m_menuLogin )

		self.Home.Append( self.fitur2, u"Login" )

		self.SetMenuBar( self.Home )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Sistem Informasi Pendataan dan Penyaluran Bantuan Pemerintah kepada Masyarakat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Myriad Pro Light" ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Kecamatan Tanggul Desa Tanggul Wetan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Myriad Pro Light" ) )

		bSizer1.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"assets/icon sistem informasi.png", wx.BITMAP_TYPE_ANY ) )
		gSizer2.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton2.SetBitmap( wx.Bitmap( u"assets/icon search.png", wx.BITMAP_TYPE_ANY ) )
		gSizer2.Add( self.m_bpButton2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnInformasiBantuan = wx.Button( self, wx.ID_ANY, u"Informasi Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnInformasiBantuan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnPenerimaanBantuan = wx.Button( self, wx.ID_ANY, u"Cek Penerima Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnPenerimaanBantuan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuHomeOnMenuSelection, id = self.m_menuHome.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuLoginOnMenuSelection, id = self.m_menuLogin.GetId() )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.m_bpButton1OnButtonClick )
		self.m_bpButton2.Bind( wx.EVT_BUTTON, self.m_bpButton2OnButtonClick )
		self.btnInformasiBantuan.Bind( wx.EVT_BUTTON, self.btnInformasiBantuanOnButtonClick )
		self.btnPenerimaanBantuan.Bind( wx.EVT_BUTTON, self.btnPenerimaanBantuanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_menuHomeOnMenuSelection( self, event ):
		event.Skip()

	def m_menuLoginOnMenuSelection( self, event ):
		event.Skip()

	def m_bpButton1OnButtonClick( self, event ):
		event.Skip()

	def m_bpButton2OnButtonClick( self, event ):
		event.Skip()

	def btnInformasiBantuanOnButtonClick( self, event ):
		event.Skip()

	def btnPenerimaanBantuanOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class informasiBantuan
###########################################################################

class informasiBantuan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Informasi Bantuan", pos = wx.DefaultPosition, size = wx.Size( 500,539 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton9 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton9.SetBitmap( wx.Bitmap( u"assets/BLT.png", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.m_bpButton9, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Bantuan Tunai Langsung (BLT)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"BLT adalah singkatan dari Bantuan Langsung Tunai yang merupakan program bantuan pemerintah dengan pemberian uang tunai atau beragam bantuan lainnya, baik bersyarat (conditional cash transfer) maupun tak bersyarat (unconditional cash transfer) untuk masyarakat miskin.", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_staticText91.Wrap( -1 )

		self.m_staticText91.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer3.Add( self.m_staticText91, 0, wx.ALL, 5 )

		self.m_bpButton10 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton10.SetBitmap( wx.Bitmap( u"assets/raskin.jpg", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.m_bpButton10, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Bantuan Beras untuk Rakyat Miskin (RASKIN)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Program Raskin adalah salah satu program penanggulangan kemiskinan dan perlindungan sosial di bidang pangan yang diselenggarakan oleh Pemerintah Pusat berupa bantuan beras bersubsidi kepada rumah tangga berpendapatan rendah (rumah tangga miskin dan rentan).", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.btnKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnKembali.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.btnKembali.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btnKembali.SetBackgroundColour( wx.Colour( 0, 128, 192 ) )

		bSizer3.Add( self.btnKembali, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnKembali.Bind( wx.EVT_BUTTON, self.btnKembaliOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembaliOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class cekPenerimaBantuan
###########################################################################

class cekPenerimaBantuan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cek Penerima Bantuan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		self.Home = wx.MenuBar( 0 )
		self.fitur1 = wx.Menu()
		self.m_menuHome = wx.MenuItem( self.fitur1, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.fitur1.Append( self.m_menuHome )

		self.Home.Append( self.fitur1, u"Home" )

		self.fitur2 = wx.Menu()
		self.m_menuLogin = wx.MenuItem( self.fitur2, wx.ID_ANY, u"Login", wx.EmptyString, wx.ITEM_NORMAL )
		self.fitur2.Append( self.m_menuLogin )

		self.Home.Append( self.fitur2, u"Login" )

		self.SetMenuBar( self.Home )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_bpButton12 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton12.SetBitmap( wx.Bitmap( u"assets/icon search.png", wx.BITMAP_TYPE_ANY ) )
		bSizer4.Add( self.m_bpButton12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"Masukkan NIK Anda", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer4.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnCariNikPenduduk = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCariNikPenduduk.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer4.Add( self.btnCariNikPenduduk, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuHomeOnMenuSelection, id = self.m_menuHome.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuLoginOnMenuSelection, id = self.m_menuLogin.GetId() )
		self.btnCariNikPenduduk.Bind( wx.EVT_BUTTON, self.btnCariNikPendudukOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_menuHomeOnMenuSelection( self, event ):
		event.Skip()

	def m_menuLoginOnMenuSelection( self, event ):
		event.Skip()

	def btnCariNikPendudukOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"E-BANSOS", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		self.Home = wx.MenuBar( 0 )
		self.fitur1 = wx.Menu()
		self.m_menuHome = wx.MenuItem( self.fitur1, wx.ID_ANY, u"Home", wx.EmptyString, wx.ITEM_NORMAL )
		self.fitur1.Append( self.m_menuHome )

		self.Home.Append( self.fitur1, u"Home" )

		self.SetMenuBar( self.Home )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton13 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton13.SetBitmap( wx.Bitmap( u"assets/icon login.png", wx.BITMAP_TYPE_ANY ) )
		bSizer7.Add( self.m_bpButton13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl2.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_textCtrl2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer7.Add( self.m_textCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
		self.m_textCtrl3.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_textCtrl3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer7.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_buttonLogin = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonLogin.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_buttonLogin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonLogin.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		bSizer7.Add( self.m_buttonLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuHomeOnMenuSelection, id = self.m_menuHome.GetId() )
		self.m_buttonLogin.Bind( wx.EVT_BUTTON, self.m_buttonLoginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_menuHomeOnMenuSelection( self, event ):
		event.Skip()

	def m_buttonLoginOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class sekretarisDesa
###########################################################################

class sekretarisDesa ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Penduduk Desa Tanggul Wetan", pos = wx.DefaultPosition, size = wx.Size( 1158,336 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		self.m_menubar4 = wx.MenuBar( 0 )
		self.Logout = wx.Menu()
		self.m_menuItemlogout = wx.MenuItem( self.Logout, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.Logout.Append( self.m_menuItemlogout )

		self.m_menubar4.Append( self.Logout, u"Logout" )

		self.SetMenuBar( self.m_menubar4 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.TabelDataPenduduk = wx.StaticText( self, wx.ID_ANY, u"Tabel Data Penduduk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TabelDataPenduduk.Wrap( -1 )

		self.TabelDataPenduduk.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bree Serif" ) )

		bSizer5.Add( self.TabelDataPenduduk, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_buttonsortirnikpenduduk = wx.Button( self, wx.ID_ANY, u"Sortir NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortirnikpenduduk.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortirnikpenduduk.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortirnikpenduduk.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortirnikpenduduk, 0, wx.ALL, 5 )

		self.m_buttonsortirterimabantuan = wx.Button( self, wx.ID_ANY, u"Sortir Penerima Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortirterimabantuan.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortirterimabantuan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortirterimabantuan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortirterimabantuan, 0, wx.ALL, 5 )

		self.m_buttonsortirgajipenduduk = wx.Button( self, wx.ID_ANY, u"Sortir Penghasilan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortirgajipenduduk.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortirgajipenduduk.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortirgajipenduduk.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortirgajipenduduk, 0, wx.ALL, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_buttontambahpenduduk = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttontambahpenduduk.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_buttontambahpenduduk.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttontambahpenduduk.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		bSizer7.Add( self.m_buttontambahpenduduk, 0, wx.ALL, 5 )

		self.m_buttonhapuspenduduk = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonhapuspenduduk.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_buttonhapuspenduduk.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonhapuspenduduk.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer7.Add( self.m_buttonhapuspenduduk, 0, wx.ALL, 5 )

		self.m_buttoneditpenduduk = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttoneditpenduduk.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_buttoneditpenduduk.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttoneditpenduduk.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		bSizer7.Add( self.m_buttoneditpenduduk, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 3, 7 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.SetColSize( 0, 100 )
		self.m_grid2.SetColSize( 1, 175 )
		self.m_grid2.SetColSize( 2, 300 )
		self.m_grid2.SetColSize( 3, 100 )
		self.m_grid2.SetColSize( 4, 120 )
		self.m_grid2.SetColSize( 5, 99 )
		self.m_grid2.SetColSize( 6, 98 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"NIK" )
		self.m_grid2.SetColLabelValue( 1, u"Nama Kepala Keluarga" )
		self.m_grid2.SetColLabelValue( 2, u"Alamat" )
		self.m_grid2.SetColLabelValue( 3, u"Pekerjaan" )
		self.m_grid2.SetColLabelValue( 4, u"Penghasilan" )
		self.m_grid2.SetColLabelValue( 5, u"Belum / Sudah" )
		self.m_grid2.SetColLabelValue( 6, u"Berhak / Tidak" )
		self.m_grid2.SetColLabelValue( 7, wx.EmptyString )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_grid2, 0, wx.ALL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuItemlogoutOnMenuSelection, id = self.m_menuItemlogout.GetId() )
		self.m_buttonsortirnikpenduduk.Bind( wx.EVT_BUTTON, self.m_buttonsortirnikpendudukOnButtonClick )
		self.m_buttonsortirterimabantuan.Bind( wx.EVT_BUTTON, self.m_buttonsortirterimabantuanOnButtonClick )
		self.m_buttonsortirgajipenduduk.Bind( wx.EVT_BUTTON, self.m_buttonsortirgajipendudukOnButtonClick )
		self.m_buttontambahpenduduk.Bind( wx.EVT_BUTTON, self.m_buttontambahpendudukOnButtonClick )
		self.m_buttonhapuspenduduk.Bind( wx.EVT_BUTTON, self.m_buttonhapuspendudukOnButtonClick )
		self.m_buttoneditpenduduk.Bind( wx.EVT_BUTTON, self.m_buttoneditpendudukOnButtonClick )
		self.m_grid2.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid2OnGridCmdSelectCell )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_menuItemlogoutOnMenuSelection( self, event ):
		event.Skip()

	def m_buttonsortirnikpendudukOnButtonClick( self, event ):
		event.Skip()

	def m_buttonsortirterimabantuanOnButtonClick( self, event ):
		event.Skip()

	def m_buttonsortirgajipendudukOnButtonClick( self, event ):
		event.Skip()

	def m_buttontambahpendudukOnButtonClick( self, event ):
		event.Skip()

	def m_buttonhapuspendudukOnButtonClick( self, event ):
		event.Skip()

	def m_buttoneditpendudukOnButtonClick( self, event ):
		event.Skip()

	def m_grid2OnGridCmdSelectCell( self, event ):
		event.Skip()


###########################################################################
## Class tambahdatapenduduk
###########################################################################

class tambahdatapenduduk ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Data Penduduk Desa Tanggul Wetan", pos = wx.DefaultPosition, size = wx.Size( 354,316 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama Kepala Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,50 ), 0 )
		self.m_textCtrl22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Penghasilan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl24, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Save )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer14.Add( m_sdbSizer1, 1, 0, 5 )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( bSizer14, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnCancelButtonClick )
		self.m_sdbSizer1Save.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_sdbSizer1OnCancelButtonClick( self, event ):
		event.Skip()

	def m_sdbSizer1OnSaveButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class editdatapenduduk
###########################################################################

class editdatapenduduk ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Data Penduduk Desa Tanggul Wetan", pos = wx.DefaultPosition, size = wx.Size( 366,326 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama Kepala Keluarga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,50 ), 0 )
		self.m_textCtrl22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Penghasilan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Belum / Sudah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		self.m_staticText44.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText44.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText44, 0, wx.ALL, 5 )

		m_comboBox1Choices = [ wx.EmptyString, u"Belum", u"sudah" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 0 )
		fgSizer2.Add( self.m_comboBox1, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		m_sdbSizer7 = wx.StdDialogButtonSizer()
		self.m_sdbSizer7Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer7.AddButton( self.m_sdbSizer7Save )
		self.m_sdbSizer7Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer7.AddButton( self.m_sdbSizer7Cancel )
		m_sdbSizer7.Realize();

		bSizer16.Add( m_sdbSizer7, 1, 0, 5 )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( bSizer16, 1, 0, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer7Cancel.Bind( wx.EVT_BUTTON, self.m_sdbSizer7OnCancelButtonClick )
		self.m_sdbSizer7Save.Bind( wx.EVT_BUTTON, self.m_sdbSizer7OnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_sdbSizer7OnCancelButtonClick( self, event ):
		event.Skip()

	def m_sdbSizer7OnSaveButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class adminAkunDesa
###########################################################################

class adminAkunDesa ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Akun Desa Tanggul Wetan", pos = wx.DefaultPosition, size = wx.Size( 973,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		self.m_menubar5 = wx.MenuBar( 0 )
		self.dataakun = wx.Menu()
		self.dataAkunDesa = wx.MenuItem( self.dataakun, wx.ID_ANY, u"Data Akun", wx.EmptyString, wx.ITEM_NORMAL )
		self.dataakun.Append( self.dataAkunDesa )

		self.m_menubar5.Append( self.dataakun, u"Data Akun " )

		self.datapenduduk = wx.Menu()
		self.dataPenduduk = wx.MenuItem( self.datapenduduk, wx.ID_ANY, u"Data Penduduk", wx.EmptyString, wx.ITEM_NORMAL )
		self.datapenduduk.Append( self.dataPenduduk )

		self.m_menubar5.Append( self.datapenduduk, u"Data Penduduk" )

		self.logout = wx.Menu()
		self.m_menuItemlogout = wx.MenuItem( self.logout, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.logout.Append( self.m_menuItemlogout )

		self.m_menubar5.Append( self.logout, u"Logout" )

		self.SetMenuBar( self.m_menubar5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_buttonsortiridakun = wx.Button( self, wx.ID_ANY, u"Sortir ID Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortiridakun.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortiridakun.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortiridakun.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortiridakun, 0, wx.ALL, 5 )

		self.m_buttonsortirnama = wx.Button( self, wx.ID_ANY, u"Sortir Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortirnama.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortirnama.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortirnama.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortirnama, 0, wx.ALL, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_buttonTambahDataDesa = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonTambahDataDesa.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_buttonTambahDataDesa.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonTambahDataDesa.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		bSizer7.Add( self.m_buttonTambahDataDesa, 0, wx.ALL, 5 )

		self.m_buttonHapusDataDesa = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonHapusDataDesa.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_buttonHapusDataDesa.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonHapusDataDesa.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer7.Add( self.m_buttonHapusDataDesa, 0, wx.ALL, 5 )

		self.m_buttonEditDataDesa = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonEditDataDesa.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_buttonEditDataDesa.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonEditDataDesa.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		bSizer7.Add( self.m_buttonEditDataDesa, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 3, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 85, 200 )

		# Columns
		self.m_grid2.SetColSize( 0, 100 )
		self.m_grid2.SetColSize( 1, 175 )
		self.m_grid2.SetColSize( 2, 300 )
		self.m_grid2.SetColSize( 3, 100 )
		self.m_grid2.SetColSize( 4, 138 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"ID Akun" )
		self.m_grid2.SetColLabelValue( 1, u"Nama" )
		self.m_grid2.SetColLabelValue( 2, u"Jabatan" )
		self.m_grid2.SetColLabelValue( 3, u"Username" )
		self.m_grid2.SetColLabelValue( 4, u"Password" )
		self.m_grid2.SetColLabelValue( 5, u"IdAkun" )
		self.m_grid2.SetColLabelValue( 6, wx.EmptyString )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_grid2, 0, wx.ALL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.dataAkunDesaOnMenuSelection, id = self.dataAkunDesa.GetId() )
		self.Bind( wx.EVT_MENU, self.dataPendudukOnMenuSelection, id = self.dataPenduduk.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemlogoutOnMenuSelection, id = self.m_menuItemlogout.GetId() )
		self.m_buttonsortiridakun.Bind( wx.EVT_BUTTON, self.m_buttonsortiridakunOnButtonClick )
		self.m_buttonsortirnama.Bind( wx.EVT_BUTTON, self.m_buttonsortirnamaOnButtonClick )
		self.m_buttonTambahDataDesa.Bind( wx.EVT_BUTTON, self.m_buttonTambahDataDesaOnButtonClick )
		self.m_buttonHapusDataDesa.Bind( wx.EVT_BUTTON, self.m_buttonHapusDataDesaOnButtonClick )
		self.m_buttonEditDataDesa.Bind( wx.EVT_BUTTON, self.m_buttonEditDataDesaOnButtonClick )
		self.m_grid2.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid2OnGridCmdSelectCell )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dataAkunDesaOnMenuSelection( self, event ):
		event.Skip()

	def dataPendudukOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemlogoutOnMenuSelection( self, event ):
		event.Skip()

	def m_buttonsortiridakunOnButtonClick( self, event ):
		event.Skip()

	def m_buttonsortirnamaOnButtonClick( self, event ):
		event.Skip()

	def m_buttonTambahDataDesaOnButtonClick( self, event ):
		event.Skip()

	def m_buttonHapusDataDesaOnButtonClick( self, event ):
		event.Skip()

	def m_buttonEditDataDesaOnButtonClick( self, event ):
		event.Skip()

	def m_grid2OnGridCmdSelectCell( self, event ):
		event.Skip()


###########################################################################
## Class tambahdataakundesa
###########################################################################

class tambahdataakundesa ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Data Akun Desa Tanggul Wetan", pos = wx.DefaultPosition, size = wx.Size( 297,271 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"ID Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
		fgSizer2.Add( self.m_textCtrl24, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Save )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer14.Add( m_sdbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( bSizer14, 1, 0, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnCancelButtonClick )
		self.m_sdbSizer1Save.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_sdbSizer1OnCancelButtonClick( self, event ):
		event.Skip()

	def m_sdbSizer1OnSaveButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class editdataakundesa
###########################################################################

class editdataakundesa ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Edit Akun Desa Tanggul Wetan", pos = wx.DefaultPosition, size = wx.Size( 308,274 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"ID Akun", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText29.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_textCtrl22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText30.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
		fgSizer2.Add( self.m_textCtrl24, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Save )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer14.Add( m_sdbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer2.Add( bSizer14, 1, 0, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnCancelButtonClick )
		self.m_sdbSizer1Save.Bind( wx.EVT_BUTTON, self.m_sdbSizer1OnSaveButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_sdbSizer1OnCancelButtonClick( self, event ):
		event.Skip()

	def m_sdbSizer1OnSaveButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class adminDataPenduduk
###########################################################################

class adminDataPenduduk ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Penduduk Desa Tanggul Wetan", pos = wx.DefaultPosition, size = wx.Size( 1168,521 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		self.m_menubar4 = wx.MenuBar( 0 )
		self.dataakun = wx.Menu()
		self.dataAkunDesa = wx.MenuItem( self.dataakun, wx.ID_ANY, u"Data Akun", wx.EmptyString, wx.ITEM_NORMAL )
		self.dataakun.Append( self.dataAkunDesa )

		self.m_menubar4.Append( self.dataakun, u"Data Akun" )

		self.datapenduduk = wx.Menu()
		self.dataPenduduk = wx.MenuItem( self.datapenduduk, wx.ID_ANY, u"Data Penduduk", wx.EmptyString, wx.ITEM_NORMAL )
		self.datapenduduk.Append( self.dataPenduduk )

		self.m_menubar4.Append( self.datapenduduk, u"Data Penduduk" )

		self.logout = wx.Menu()
		self.m_menuItemlogout = wx.MenuItem( self.logout, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.logout.Append( self.m_menuItemlogout )

		self.m_menubar4.Append( self.logout, u"Logout" )

		self.SetMenuBar( self.m_menubar4 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.TabelDataPenduduk = wx.StaticText( self, wx.ID_ANY, u"Tabel Data Penduduk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TabelDataPenduduk.Wrap( -1 )

		self.TabelDataPenduduk.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bree Serif" ) )

		bSizer5.Add( self.TabelDataPenduduk, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_buttonsortirnik = wx.Button( self, wx.ID_ANY, u"Sortir NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortirnik.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortirnik.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortirnik.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortirnik, 0, wx.ALL, 5 )

		self.m_buttonsortirpenerimaanbantuan = wx.Button( self, wx.ID_ANY, u"Sortir Penerima Bantuan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortirpenerimaanbantuan.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortirpenerimaanbantuan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortirpenerimaanbantuan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortirpenerimaanbantuan, 0, wx.ALL, 5 )

		self.m_buttonsortirkeberhakan = wx.Button( self, wx.ID_ANY, u"Sortir Berhak / Tidak", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonsortirkeberhakan.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_buttonsortirkeberhakan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_buttonsortirkeberhakan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

		bSizer7.Add( self.m_buttonsortirkeberhakan, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 3, 7 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 200 )

		# Columns
		self.m_grid2.SetColSize( 0, 100 )
		self.m_grid2.SetColSize( 1, 175 )
		self.m_grid2.SetColSize( 2, 300 )
		self.m_grid2.SetColSize( 3, 120 )
		self.m_grid2.SetColSize( 4, 120 )
		self.m_grid2.SetColSize( 5, 130 )
		self.m_grid2.SetColSize( 6, 108 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"NIK" )
		self.m_grid2.SetColLabelValue( 1, u"Nama Kepala Keluarga" )
		self.m_grid2.SetColLabelValue( 2, u"Alamat" )
		self.m_grid2.SetColLabelValue( 3, u"Pekerjaan" )
		self.m_grid2.SetColLabelValue( 4, u"Penghasilan" )
		self.m_grid2.SetColLabelValue( 5, u"Sudah / Belum" )
		self.m_grid2.SetColLabelValue( 6, u"Berhak / Tidak" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer5.Add( self.m_grid2, 0, wx.ALL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.dataAkunDesaOnMenuSelection, id = self.dataAkunDesa.GetId() )
		self.Bind( wx.EVT_MENU, self.dataPendudukOnMenuSelection, id = self.dataPenduduk.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemlogoutOnMenuSelection, id = self.m_menuItemlogout.GetId() )
		self.m_buttonsortirnik.Bind( wx.EVT_BUTTON, self.m_buttonsortirnikOnButtonClick )
		self.m_buttonsortirpenerimaanbantuan.Bind( wx.EVT_BUTTON, self.m_buttonsortirpenerimaanbantuanOnButtonClick )
		self.m_buttonsortirkeberhakan.Bind( wx.EVT_BUTTON, self.m_buttonsortirkeberhakanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dataAkunDesaOnMenuSelection( self, event ):
		event.Skip()

	def dataPendudukOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemlogoutOnMenuSelection( self, event ):
		event.Skip()

	def m_buttonsortirnikOnButtonClick( self, event ):
		event.Skip()

	def m_buttonsortirpenerimaanbantuanOnButtonClick( self, event ):
		event.Skip()

	def m_buttonsortirkeberhakanOnButtonClick( self, event ):
		event.Skip()


