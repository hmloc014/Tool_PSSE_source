# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import glob, os, sys
import pssepath
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
import pyodbc
from math import *
from decimal import *
###########################################################################
## Class Add_New_Load
###########################################################################

class Select_Idv_File ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select Idv File", pos = wx.DefaultPosition, size = wx.Size(500,-1), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.idv1 = wx.RadioButton( self, wx.ID_ANY, u"Choose dyn_1.idv file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.idv1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer35.Add( self.idv1, 0, wx.ALL, 10 )
		
		self.idv21 = wx.RadioButton( self, wx.ID_ANY, u"Choose dyn_21.idv file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.idv21.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer35.Add( self.idv21, 0, wx.ALL, 10 )

		self.idv22 = wx.RadioButton( self, wx.ID_ANY, u"Choose dyn_22.idv file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.idv22.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer35.Add( self.idv22, 0, wx.ALL, 10 )

		# bSizer35.Fit( self )
		bSizer34.Add( bSizer35,1, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.idv23 = wx.RadioButton( self, wx.ID_ANY, u"Add dyr file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.idv23.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer36.Add( self.idv23, 0, wx.ALL, 10 )

		self.dynProcess = wx.RadioButton( self, wx.ID_ANY, u"Run dynamic process", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dynProcess.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer36.Add( self.dynProcess, 0, wx.ALL, 10 )

		self.dynMultiProcess = wx.RadioButton( self, wx.ID_ANY, u"Run Multi dynamic process", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dynMultiProcess.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer36.Add( self.dynMultiProcess, 0, wx.ALL, 10 )
		
		self.btnSelect = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer36.Add( self.btnSelect, 0, wx.ALL, 15 )

		# bSizer36.Fit( self )
		bSizer34.Add( bSizer36,1, wx.EXPAND, 5 )
		bSizer34.Fit( self )
				
		self.SetSizer( bSizer34 )
		self.Layout()

		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		self.choose = 0
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.idv1.Bind( wx.EVT_RADIOBUTTON, self.choose_idv1_fcn )
		self.idv21.Bind( wx.EVT_RADIOBUTTON, self.choose_idv21_fcn )
		self.idv22.Bind( wx.EVT_RADIOBUTTON, self.choose_idv22_fcn )
		self.idv23.Bind( wx.EVT_RADIOBUTTON, self.add_dyr_fcn )
		self.dynProcess.Bind( wx.EVT_RADIOBUTTON, self.add_dyn_process_fcn )
		self.dynMultiProcess.Bind( wx.EVT_RADIOBUTTON, self.add_dyn_multi_process_fcn )

		self.btnSelect.Bind( wx.EVT_BUTTON, self.Next )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	# Chọn file dyn1.idv
	def choose_idv1_fcn( self, event ):
		self.choose = 1
		event.Skip()
	
	# Chọn file dyn21.idv
	def choose_idv21_fcn( self, event ):
		self.choose = 2
		event.Skip()

	# Chọn file dyn22.idv
	def choose_idv22_fcn( self, event ):
		self.choose = 3
		event.Skip()

	# Thêm file dyr (vd cho nguồn NLTT)
	def add_dyr_fcn( self, event ):
		self.choose = 4
		event.Skip()

	# Thêm sự cố
	def add_dyn_process_fcn( self, event ):
		self.choose = 5
		event.Skip()

	# Thêm nhiều sự cố khác nhau
	def add_dyn_multi_process_fcn( self, event):
		self.choose = 6
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag
	
	def Next( self, event ):
		self.flag = 1
		self.Close()
		event.Skip()
		return self.choose
