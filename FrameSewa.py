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
## Class Frame_Home_Karyawan
###########################################################################

class Frame_Home_Karyawan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 90, 127, 180 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook1.SetForegroundColour( wx.Colour( 90, 127, 180 ) )
		self.m_notebook1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		self.panel_lihat_data_peminjaman = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_lihat_data_peminjaman.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )


		bSizer21.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.text_judul = wx.StaticText( self.panel_lihat_data_peminjaman, wx.ID_ANY, u"List Data Penyewaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_judul.Wrap( -1 )

		self.text_judul.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )
		self.text_judul.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer21.Add( self.text_judul, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_peminjaman = wx.grid.Grid( self.panel_lihat_data_peminjaman, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_peminjaman.CreateGrid( 15, 7 )
		self.grid_daftar_peminjaman.EnableEditing( True )
		self.grid_daftar_peminjaman.EnableGridLines( True )
		self.grid_daftar_peminjaman.EnableDragGridSize( False )
		self.grid_daftar_peminjaman.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_peminjaman.SetColSize( 0, 100 )
		self.grid_daftar_peminjaman.SetColSize( 1, 175 )
		self.grid_daftar_peminjaman.SetColSize( 2, 175 )
		self.grid_daftar_peminjaman.SetColSize( 3, 125 )
		self.grid_daftar_peminjaman.SetColSize( 4, 75 )
		self.grid_daftar_peminjaman.SetColSize( 5, 75 )
		self.grid_daftar_peminjaman.SetColSize( 6, 125 )
		self.grid_daftar_peminjaman.EnableDragColMove( False )
		self.grid_daftar_peminjaman.EnableDragColSize( True )
		self.grid_daftar_peminjaman.SetColLabelSize( 30 )
		self.grid_daftar_peminjaman.SetColLabelValue( 0, u"Kode Motor" )
		self.grid_daftar_peminjaman.SetColLabelValue( 1, u"Tanggal Sewa" )
		self.grid_daftar_peminjaman.SetColLabelValue( 2, u"Tanggal Kembali" )
		self.grid_daftar_peminjaman.SetColLabelValue( 3, u"Username Customer" )
		self.grid_daftar_peminjaman.SetColLabelValue( 4, u"Jaminan" )
		self.grid_daftar_peminjaman.SetColLabelValue( 5, u"Hari" )
		self.grid_daftar_peminjaman.SetColLabelValue( 6, u"Biaya Total" )
		self.grid_daftar_peminjaman.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_peminjaman.SetRowSize( 0, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 1, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 2, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 3, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 4, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 5, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 6, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 7, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 8, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 9, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 10, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 11, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 12, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 13, 30 )
		self.grid_daftar_peminjaman.SetRowSize( 14, 30 )
		self.grid_daftar_peminjaman.EnableDragRowSize( True )
		self.grid_daftar_peminjaman.SetRowLabelSize( 60 )
		self.grid_daftar_peminjaman.SetRowLabelValue( 0, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 1, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 2, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 3, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 4, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 5, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 6, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 7, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 8, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 9, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 10, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 11, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 12, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 13, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelValue( 14, wx.EmptyString )
		self.grid_daftar_peminjaman.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_peminjaman.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.grid_daftar_peminjaman.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_peminjaman.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer21.Add( self.grid_daftar_peminjaman, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.panel_lihat_data_peminjaman.SetSizer( bSizer21 )
		self.panel_lihat_data_peminjaman.Layout()
		bSizer21.Fit( self.panel_lihat_data_peminjaman )
		self.m_notebook1.AddPage( self.panel_lihat_data_peminjaman, u"Data Penyewaan", False )
		self.panel_lihat_data_pelanggan = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_lihat_data_pelanggan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )


		bSizer211.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.text_judul1 = wx.StaticText( self.panel_lihat_data_pelanggan, wx.ID_ANY, u"List Data Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_judul1.Wrap( -1 )

		self.text_judul1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )
		self.text_judul1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer211.Add( self.text_judul1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer211.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_pelanggan = wx.grid.Grid( self.panel_lihat_data_pelanggan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_pelanggan.CreateGrid( 15, 4 )
		self.grid_daftar_pelanggan.EnableEditing( True )
		self.grid_daftar_pelanggan.EnableGridLines( True )
		self.grid_daftar_pelanggan.EnableDragGridSize( False )
		self.grid_daftar_pelanggan.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_pelanggan.SetColSize( 0, 155 )
		self.grid_daftar_pelanggan.SetColSize( 1, 200 )
		self.grid_daftar_pelanggan.SetColSize( 2, 125 )
		self.grid_daftar_pelanggan.SetColSize( 3, 350 )
		self.grid_daftar_pelanggan.EnableDragColMove( False )
		self.grid_daftar_pelanggan.EnableDragColSize( True )
		self.grid_daftar_pelanggan.SetColLabelSize( 30 )
		self.grid_daftar_pelanggan.SetColLabelValue( 0, u"Username Customer" )
		self.grid_daftar_pelanggan.SetColLabelValue( 1, u"Nama Lengkap" )
		self.grid_daftar_pelanggan.SetColLabelValue( 2, u"No Telp" )
		self.grid_daftar_pelanggan.SetColLabelValue( 3, u"Alamat" )
		self.grid_daftar_pelanggan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_pelanggan.SetRowSize( 0, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 1, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 2, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 3, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 4, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 5, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 6, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 7, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 8, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 9, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 10, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 11, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 12, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 13, 30 )
		self.grid_daftar_pelanggan.SetRowSize( 14, 30 )
		self.grid_daftar_pelanggan.EnableDragRowSize( True )
		self.grid_daftar_pelanggan.SetRowLabelSize( 60 )
		self.grid_daftar_pelanggan.SetRowLabelValue( 0, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 1, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 2, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 3, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 4, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 5, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 6, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 7, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 8, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 9, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 10, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 11, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 12, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 13, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelValue( 14, wx.EmptyString )
		self.grid_daftar_pelanggan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_pelanggan.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.grid_daftar_pelanggan.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_pelanggan.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer211.Add( self.grid_daftar_pelanggan, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.panel_lihat_data_pelanggan.SetSizer( bSizer211 )
		self.panel_lihat_data_pelanggan.Layout()
		bSizer211.Fit( self.panel_lihat_data_pelanggan )
		self.m_notebook1.AddPage( self.panel_lihat_data_pelanggan, u"Data Customer", False )
		self.panel_tambah_data_peminjaman = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_tambah_data_peminjaman.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.panel_tambah_data_peminjaman.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer212 = wx.BoxSizer( wx.VERTICAL )

		bSizer2111 = wx.BoxSizer( wx.VERTICAL )


		bSizer2111.Add( ( 0, 75), 0, wx.EXPAND, 5 )

		self.text_judul11 = wx.StaticText( self.panel_tambah_data_peminjaman, wx.ID_ANY, u"Form Penyewaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_judul11.Wrap( -1 )

		self.text_judul11.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )
		self.text_judul11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2111.Add( self.text_judul11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2111.Add( ( 0, 100), 0, wx.EXPAND, 5 )


		bSizer212.Add( bSizer2111, 0, wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer4.SetMinSize( wx.Size( 350,-1 ) )
		self.label_kode_barang = wx.StaticText( self.panel_tambah_data_peminjaman, wx.ID_ANY, u"Kode Sewa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang.Wrap( -1 )

		self.label_kode_barang.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang.SetMinSize( wx.Size( -1,50 ) )

		fgSizer4.Add( self.label_kode_barang, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 100, 0), 1, wx.EXPAND, 5 )

		choice_kode_barangChoices = []
		self.choice_kode_barang = wx.Choice( self.panel_tambah_data_peminjaman, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), choice_kode_barangChoices, 0 )
		self.choice_kode_barang.SetSelection( 0 )
		fgSizer4.Add( self.choice_kode_barang, 0, wx.ALL, 5 )

		self.label_kode_barang1 = wx.StaticText( self.panel_tambah_data_peminjaman, wx.ID_ANY, u"Username Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang1.Wrap( -1 )

		self.label_kode_barang1.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang1.SetMinSize( wx.Size( -1,50 ) )

		fgSizer4.Add( self.label_kode_barang1, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_username = wx.TextCtrl( self.panel_tambah_data_peminjaman, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.input_username.SetMinSize( wx.Size( 175,-1 ) )

		fgSizer4.Add( self.input_username, 0, wx.ALL, 5 )

		self.label_kode_barang11 = wx.StaticText( self.panel_tambah_data_peminjaman, wx.ID_ANY, u"Jaminan Penyewaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang11.Wrap( -1 )

		self.label_kode_barang11.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang11.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang11.SetMinSize( wx.Size( -1,50 ) )

		fgSizer4.Add( self.label_kode_barang11, 0, wx.ALL, 5 )


		fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		choice_jaminanChoices = []
		self.choice_jaminan = wx.Choice( self.panel_tambah_data_peminjaman, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), choice_jaminanChoices, 0 )
		self.choice_jaminan.SetSelection( 0 )
		fgSizer4.Add( self.choice_jaminan, 0, wx.ALL, 5 )


		bSizer212.Add( fgSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer21111 = wx.BoxSizer( wx.VERTICAL )


		bSizer21111.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.button_submit = wx.Button( self.panel_tambah_data_peminjaman, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.Size( 170,50 ), 0 )
		self.button_submit.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer21111.Add( self.button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer212.Add( bSizer21111, 1, wx.EXPAND, 5 )


		self.panel_tambah_data_peminjaman.SetSizer( bSizer212 )
		self.panel_tambah_data_peminjaman.Layout()
		bSizer212.Fit( self.panel_tambah_data_peminjaman )
		self.m_notebook1.AddPage( self.panel_tambah_data_peminjaman, u"Tambah Data Penyewaan", True )
		self.panel_pengembalian_barang = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_pengembalian_barang.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer213 = wx.BoxSizer( wx.VERTICAL )


		bSizer213.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.text_judul2 = wx.StaticText( self.panel_pengembalian_barang, wx.ID_ANY, u"Tabel Pengembalian Motor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_judul2.Wrap( -1 )

		self.text_judul2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )
		self.text_judul2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer213.Add( self.text_judul2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer213.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		self.grid_daftar_peminjaman2 = wx.grid.Grid( self.panel_pengembalian_barang, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_peminjaman2.CreateGrid( 15, 7 )
		self.grid_daftar_peminjaman2.EnableEditing( True )
		self.grid_daftar_peminjaman2.EnableGridLines( True )
		self.grid_daftar_peminjaman2.EnableDragGridSize( False )
		self.grid_daftar_peminjaman2.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_peminjaman2.SetColSize( 0, 100 )
		self.grid_daftar_peminjaman2.SetColSize( 1, 175 )
		self.grid_daftar_peminjaman2.SetColSize( 2, 175 )
		self.grid_daftar_peminjaman2.SetColSize( 3, 125 )
		self.grid_daftar_peminjaman2.SetColSize( 4, 75 )
		self.grid_daftar_peminjaman2.SetColSize( 5, 75 )
		self.grid_daftar_peminjaman2.SetColSize( 6, 125 )
		self.grid_daftar_peminjaman2.EnableDragColMove( False )
		self.grid_daftar_peminjaman2.EnableDragColSize( True )
		self.grid_daftar_peminjaman2.SetColLabelSize( 30 )
		self.grid_daftar_peminjaman2.SetColLabelValue( 0, u"Kode Motor" )
		self.grid_daftar_peminjaman2.SetColLabelValue( 1, u"Tanggal Sewa" )
		self.grid_daftar_peminjaman2.SetColLabelValue( 2, u"Tanggal Kembali" )
		self.grid_daftar_peminjaman2.SetColLabelValue( 3, u"Username Customer" )
		self.grid_daftar_peminjaman2.SetColLabelValue( 4, u"Jaminan" )
		self.grid_daftar_peminjaman2.SetColLabelValue( 5, u"Hari" )
		self.grid_daftar_peminjaman2.SetColLabelValue( 6, u"Biaya Total" )
		self.grid_daftar_peminjaman2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_peminjaman2.SetRowSize( 0, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 1, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 2, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 3, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 4, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 5, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 6, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 7, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 8, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 9, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 10, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 11, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 12, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 13, 30 )
		self.grid_daftar_peminjaman2.SetRowSize( 14, 30 )
		self.grid_daftar_peminjaman2.EnableDragRowSize( True )
		self.grid_daftar_peminjaman2.SetRowLabelSize( 60 )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 0, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 1, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 2, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 3, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 4, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 5, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 6, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 7, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 8, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 9, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 10, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 11, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 12, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 13, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelValue( 14, wx.EmptyString )
		self.grid_daftar_peminjaman2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_peminjaman2.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.grid_daftar_peminjaman2.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_peminjaman2.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer213.Add( self.grid_daftar_peminjaman2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer213.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		fgSizer41 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer41.SetMinSize( wx.Size( 350,-1 ) )
		self.label_kode_barang2 = wx.StaticText( self.panel_pengembalian_barang, wx.ID_ANY, u"ID yang dikembalikan:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang2.Wrap( -1 )

		self.label_kode_barang2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang2.SetMinSize( wx.Size( -1,40 ) )

		fgSizer41.Add( self.label_kode_barang2, 0, wx.ALL, 5 )


		fgSizer41.Add( ( 100, 0), 1, wx.EXPAND, 5 )

		choice_pengembalianChoices = []
		self.choice_pengembalian = wx.Choice( self.panel_pengembalian_barang, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), choice_pengembalianChoices, 0 )
		self.choice_pengembalian.SetSelection( 0 )
		fgSizer41.Add( self.choice_pengembalian, 0, wx.ALL, 5 )


		bSizer213.Add( fgSizer41, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer211111 = wx.BoxSizer( wx.VERTICAL )

		self.m_button41 = wx.Button( self.panel_pengembalian_barang, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.Size( 170,40 ), 0 )
		self.m_button41.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer211111.Add( self.m_button41, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer213.Add( bSizer211111, 1, wx.EXPAND, 5 )


		self.panel_pengembalian_barang.SetSizer( bSizer213 )
		self.panel_pengembalian_barang.Layout()
		bSizer213.Fit( self.panel_pengembalian_barang )
		self.m_notebook1.AddPage( self.panel_pengembalian_barang, u"Pengembalian Motor", False )
		self.panel_tambah_data_pelanggan = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_tambah_data_pelanggan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer2121 = wx.BoxSizer( wx.VERTICAL )

		bSizer21112 = wx.BoxSizer( wx.VERTICAL )


		bSizer21112.Add( ( 0, 75), 0, wx.EXPAND, 5 )

		self.text_judul111 = wx.StaticText( self.panel_tambah_data_pelanggan, wx.ID_ANY, u"Form Tambah Data Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_judul111.Wrap( -1 )

		self.text_judul111.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )
		self.text_judul111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer21112.Add( self.text_judul111, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21112.Add( ( 0, 75), 0, wx.EXPAND, 5 )


		bSizer2121.Add( bSizer21112, 0, wx.EXPAND, 5 )

		fgSizer42 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer42.SetMinSize( wx.Size( 350,-1 ) )
		self.label_kode_barang3 = wx.StaticText( self.panel_tambah_data_pelanggan, wx.ID_ANY, u"Username Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang3.Wrap( -1 )

		self.label_kode_barang3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang3.SetMinSize( wx.Size( -1,50 ) )

		fgSizer42.Add( self.label_kode_barang3, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 100, 0), 1, wx.EXPAND, 5 )

		self.input_username_pelanggan = wx.TextCtrl( self.panel_tambah_data_pelanggan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer42.Add( self.input_username_pelanggan, 0, wx.ALL, 5 )

		self.label_kode_barang12 = wx.StaticText( self.panel_tambah_data_pelanggan, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang12.Wrap( -1 )

		self.label_kode_barang12.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang12.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang12.SetMinSize( wx.Size( -1,50 ) )

		fgSizer42.Add( self.label_kode_barang12, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_nama_lengkap = wx.TextCtrl( self.panel_tambah_data_pelanggan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer42.Add( self.input_nama_lengkap, 0, wx.ALL, 5 )

		self.label_kode_barang111 = wx.StaticText( self.panel_tambah_data_pelanggan, wx.ID_ANY, u"Nomor Telepon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang111.Wrap( -1 )

		self.label_kode_barang111.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang111.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang111.SetMinSize( wx.Size( -1,50 ) )

		fgSizer42.Add( self.label_kode_barang111, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_nomor_telepon = wx.TextCtrl( self.panel_tambah_data_pelanggan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer42.Add( self.input_nomor_telepon, 0, wx.ALL, 5 )

		self.label_kode_barang1111 = wx.StaticText( self.panel_tambah_data_pelanggan, wx.ID_ANY, u"Alamat Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang1111.Wrap( -1 )

		self.label_kode_barang1111.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang1111.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang1111.SetMinSize( wx.Size( -1,50 ) )

		fgSizer42.Add( self.label_kode_barang1111, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_alamat_lengkap = wx.TextCtrl( self.panel_tambah_data_pelanggan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer42.Add( self.input_alamat_lengkap, 0, wx.ALL, 5 )

		self.label_kode_barang11111 = wx.StaticText( self.panel_tambah_data_pelanggan, wx.ID_ANY, u"Password Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_kode_barang11111.Wrap( -1 )

		self.label_kode_barang11111.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.label_kode_barang11111.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.label_kode_barang11111.SetMinSize( wx.Size( -1,50 ) )

		fgSizer42.Add( self.label_kode_barang11111, 0, wx.ALL, 5 )


		fgSizer42.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_password_pelanggan = wx.TextCtrl( self.panel_tambah_data_pelanggan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer42.Add( self.input_password_pelanggan, 0, wx.ALL, 5 )


		bSizer2121.Add( fgSizer42, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer211112 = wx.BoxSizer( wx.VERTICAL )


		bSizer211112.Add( ( 0, 60), 0, wx.EXPAND, 5 )

		self.m_button42 = wx.Button( self.panel_tambah_data_pelanggan, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.Size( 170,50 ), 0 )
		self.m_button42.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer211112.Add( self.m_button42, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2121.Add( bSizer211112, 1, wx.EXPAND, 5 )


		self.panel_tambah_data_pelanggan.SetSizer( bSizer2121 )
		self.panel_tambah_data_pelanggan.Layout()
		bSizer2121.Fit( self.panel_tambah_data_pelanggan )
		self.m_notebook1.AddPage( self.panel_tambah_data_pelanggan, u"Tambah Data Customer", False )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_submit.Bind( wx.EVT_BUTTON, self.submit_data_peminjaman )
		self.m_button41.Bind( wx.EVT_BUTTON, self.submit_data_pengembalian )
		self.m_button42.Bind( wx.EVT_BUTTON, self.submit_data_pelanggan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def submit_data_peminjaman( self, event ):
		event.Skip()

	def submit_data_pengembalian( self, event ):
		event.Skip()

	def submit_data_pelanggan( self, event ):
		event.Skip()


###########################################################################
## Class Frame_Home_Pelanggan
###########################################################################

class Frame_Home_Pelanggan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 90, 127, 180 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_notebook1.SetForegroundColour( wx.Colour( 90, 127, 180 ) )
		self.m_notebook1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		self.panel_lihat_data_peminjaman = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_lihat_data_peminjaman.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )


		bSizer21.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.text_judul = wx.StaticText( self.panel_lihat_data_peminjaman, wx.ID_ANY, u"List Data Penyewaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_judul.Wrap( -1 )

		self.text_judul.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Montserrat Medium" ) )
		self.text_judul.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer21.Add( self.text_judul, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_peminjaman1 = wx.grid.Grid( self.panel_lihat_data_peminjaman, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_peminjaman1.CreateGrid( 15, 6 )
		self.grid_daftar_peminjaman1.EnableEditing( True )
		self.grid_daftar_peminjaman1.EnableGridLines( True )
		self.grid_daftar_peminjaman1.EnableDragGridSize( False )
		self.grid_daftar_peminjaman1.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_peminjaman1.SetColSize( 0, 100 )
		self.grid_daftar_peminjaman1.SetColSize( 1, 175 )
		self.grid_daftar_peminjaman1.SetColSize( 2, 175 )
		self.grid_daftar_peminjaman1.SetColSize( 3, 75 )
		self.grid_daftar_peminjaman1.SetColSize( 4, 75 )
		self.grid_daftar_peminjaman1.SetColSize( 5, 125 )
		self.grid_daftar_peminjaman1.EnableDragColMove( False )
		self.grid_daftar_peminjaman1.EnableDragColSize( True )
		self.grid_daftar_peminjaman1.SetColLabelSize( 30 )
		self.grid_daftar_peminjaman1.SetColLabelValue( 0, u"Kode Motor" )
		self.grid_daftar_peminjaman1.SetColLabelValue( 1, u"Tanggal Sewa" )
		self.grid_daftar_peminjaman1.SetColLabelValue( 2, u"Tanggal Kembali" )
		self.grid_daftar_peminjaman1.SetColLabelValue( 3, u"Jaminan" )
		self.grid_daftar_peminjaman1.SetColLabelValue( 4, u"Hari" )
		self.grid_daftar_peminjaman1.SetColLabelValue( 5, u"Biaya Total" )
		self.grid_daftar_peminjaman1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_peminjaman1.SetRowSize( 0, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 1, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 2, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 3, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 4, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 5, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 6, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 7, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 8, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 9, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 10, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 11, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 12, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 13, 30 )
		self.grid_daftar_peminjaman1.SetRowSize( 14, 30 )
		self.grid_daftar_peminjaman1.EnableDragRowSize( True )
		self.grid_daftar_peminjaman1.SetRowLabelSize( 60 )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 0, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 1, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 2, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 3, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 4, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 5, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 6, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 7, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 8, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 9, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 10, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 11, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 12, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 13, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelValue( 14, wx.EmptyString )
		self.grid_daftar_peminjaman1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_peminjaman1.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.grid_daftar_peminjaman1.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_peminjaman1.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		self.grid_daftar_peminjaman1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer21.Add( self.grid_daftar_peminjaman1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.panel_lihat_data_peminjaman.SetSizer( bSizer21 )
		self.panel_lihat_data_peminjaman.Layout()
		bSizer21.Fit( self.panel_lihat_data_peminjaman )
		self.m_notebook1.AddPage( self.panel_lihat_data_peminjaman, u"Data Penyewaan", False )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Frame_Login
###########################################################################

class Frame_Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )


		bSizer21.Add( ( 0, 80), 0, wx.EXPAND, 5 )

		self.text_judul = wx.StaticText( self, wx.ID_ANY, u"Welcome To", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.text_judul.Wrap( -1 )

		self.text_judul.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Nirmala UI" ) )
		self.text_judul.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer21.Add( self.text_judul, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_judul1 = wx.StaticText( self, wx.ID_ANY, u"Aplication Sewa Aja!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_judul1.Wrap( -1 )

		self.text_judul1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Nirmala UI" ) )
		self.text_judul1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer21.Add( self.text_judul1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer21.Add( ( 0, 60), 0, wx.EXPAND, 5 )


		bSizer2.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		fgSizer16 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText103 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText103.Wrap( -1 )

		self.m_staticText103.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.m_staticText103.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer16.Add( self.m_staticText103, 0, wx.ALL, 5 )


		fgSizer16.Add( ( 100, 0), 1, wx.EXPAND, 5 )

		self.username_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		fgSizer16.Add( self.username_input, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		fgSizer16.Add( ( 0, 25), 1, wx.EXPAND, 5 )


		fgSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1031 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText1031.Wrap( -1 )

		self.m_staticText1031.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "PT Sans" ) )
		self.m_staticText1031.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer16.Add( self.m_staticText1031, 0, wx.ALL, 5 )


		fgSizer16.Add( ( 100, 0), 1, wx.EXPAND, 5 )

		self.password_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		fgSizer16.Add( self.password_input, 0, wx.ALL, 5 )


		bSizer79.Add( fgSizer16, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer79, 0, wx.EXPAND, 5 )

		bSizer21111 = wx.BoxSizer( wx.VERTICAL )


		bSizer21111.Add( ( 0, 70), 0, wx.EXPAND, 5 )

		choice_loginChoices = [ u"Login Admin", u"Login Costumer" ]
		self.choice_login = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), choice_loginChoices, 0 )
		self.choice_login.SetSelection( 0 )
		self.choice_login.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT) )
		self.choice_login.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT) )

		bSizer21111.Add( self.choice_login, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer21111, 1, wx.EXPAND, 5 )

		bSizer211111 = wx.BoxSizer( wx.VERTICAL )


		bSizer211111.Add( ( 0, 60), 0, wx.EXPAND, 5 )

		self.button_submit1 = wx.Button( self, wx.ID_ANY, u"Sign In", wx.DefaultPosition, wx.Size( 170,50 ), 0 )
		self.button_submit1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer211111.Add( self.button_submit1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer211111, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.button_submit1.Bind( wx.EVT_BUTTON, self.submit_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def submit_login( self, event ):
		event.Skip()


