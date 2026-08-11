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

class Add_New_Load_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add New Load", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Load Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusNumChoices = []
		self.fromBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.fromBusNumChoices, wx.CB_SORT )
		self.fromBusNum.SetSelection( 0 )
		gSizer6.Add( self.fromBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		self.textCtrl_Num = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Num, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Pmax", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer6.Add( self.m_staticText32, 0, wx.ALL, 10 )
		
		self.textCtrl_Pmax = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Pmax, 0, wx.ALL, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAddLoad = wx.Button( self, wx.ID_ANY, u"Add Load", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnAddLoad, 0, wx.ALL, 5 )
		
		
		gSizer6.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer6 )
		self.Layout()
		gSizer6.Fit( self )
		
		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		self.flagSynch = 0
		self.Path = ''
		self.PathFile = []
		self.macroFile = ''

		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.fromBusNum.Bind( wx.EVT_TEXT, self.onTextBusNum )
		self.textCtrl_Num.Bind( wx.EVT_TEXT, self.onTextNum )
		self.textCtrl_Pmax.Bind( wx.EVT_TEXT, self.onTextPMax )

		self.btnAddLoad.Bind( wx.EVT_BUTTON, self.AddNewLoadDialog )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onTextBusNum( self, event ):
		event.Skip()
	
	def onTextNum( self, event ):
		event.Skip()

	def onTextPMax( self, event ):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag
	
	# Tạo dialog để thêm mới phụ tải
	def AddNewLoadDialog( self, event ):
		# try:
		self.flag = 0
		loadNumNew = int(self.fromBusNum.GetValue().split('-')[0])
		loadNum = int(self.textCtrl_Num.GetValue())
		PloadNew = float(self.textCtrl_Pmax.GetValue())
		QloadNew = PloadNew/3

		busInforList = [loadNumNew, loadNum,PloadNew]

		ierr, loadNumber = psspy.aloadint(-1, 4, "NUMBER")
		# ierr, loadID = psspy.aloadchar(-1, 4, "ID")
		ierr, busID = psspy.abusint(-1,2,'NUMBER')
		
		flag = 1
		if not (int(loadNumNew) in busID[0][:]):
			wx.MessageBox("This bus number is not existing!")
			flag = 0

		psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(loadNumNew)],0,[],0,[])
		ierr, lodID = psspy.aloadchar(0, 4,"ID")

		loadID = []
		for i in range(len(lodID[0])):
			loadID.append(int(lodID[0][i].strip()))

		# for i in range(len(loadNumber[0])):
		# 	if loadNumNew == loadNumber[0][i] and  loadIDNew in loadID[0][i]:
		# 		wx.MessageBox('This load already exists')
		# 		flag = 0


		id_new = []
		if len(loadID)!= 0:
			count = 0
			for i in  range(int(loadNum)):
				count +=1 
				id_new.append(max(loadID)+count)
		else:
			for i in  range(int(loadNum)):
				id_new.append(i+1)

		if not '' in busInforList: 
			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):
					psspy.case(path)
					for idLoad in id_new:
						psspy.load_data_4(loadNumNew,str(idLoad),   REALAR1 = PloadNew, REALAR2 = QloadNew)
					
					psspy.save(path)
			else:
				for idLoad in id_new:
					psspy.load_data_4(loadNumNew,str(idLoad),   REALAR1 = PloadNew, REALAR2 = QloadNew)
				psspy.save(self.Path)
			
			if self.macroFile != '':
				f = open(self.macroFile,'a')
				for idLoad in id_new:
					f.writelines("psspy.load_data_4({a},'{b}',REALAR1 ={c}, REALAR2 = {d})\n".format(a=loadNumNew,b=idLoad,c=PloadNew,d=QloadNew))
				f.close()

			self.flag = 1
			self.Close()
		else:
			event.Skip()
