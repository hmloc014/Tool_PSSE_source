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
from ui_performance import profiled
import pyodbc
from math import *
from decimal import *
###########################################################################
## Class Add_New_Load
###########################################################################

class Add_New_Shunt_Dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add New Shunt", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Shunt Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusNumChoices = []
		self.fromBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.fromBusNumChoices, wx.CB_SORT )
		self.fromBusNum.SetSelection( 0 )
		gSizer6.Add( self.fromBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Shunt ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		self.textCtrl_ID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_ID, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"B-Shunt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer6.Add( self.m_staticText32, 0, wx.ALL, 10 )
		
		self.textCtrl_BShunt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_BShunt, 0, wx.ALL, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAddShunt = wx.Button( self, wx.ID_ANY, u"Add Shunt", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnAddShunt, 0, wx.ALL, 5 )
		
		
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
		self.textCtrl_ID.Bind( wx.EVT_TEXT, self.onTextID )
		self.textCtrl_BShunt.Bind( wx.EVT_TEXT, self.onTextBShunt )

		self.btnAddShunt.Bind( wx.EVT_BUTTON, self.AddNewShuntDialog )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onTextBusNum( self, event ):
		event.Skip()
	
	def onTextID( self, event ):
		event.Skip()

	def onTextBShunt( self, event ):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag
	
	# Dialog thêm mới kháng tụ
	@profiled('psse.add.shunt_and_save')
	def AddNewShuntDialog( self, event ):
		self.flag = 0
		shuntNum = int(self.fromBusNum.GetValue().split('-')[0])
		shuntID = str(self.textCtrl_ID.GetValue())
		BShunt = float(self.textCtrl_BShunt.GetValue())

		shuntInforList = [shuntNum, shuntID,BShunt]

		ierr, shuntNumList = psspy.afxshuntint(-1,4,"NUMBER")
		ierr, shuntIDList = psspy.afxshuntchar(-1,4,"ID")
		ierr, busID = psspy.abusint(-1,2,'NUMBER')

		flag = 1
		if not (int(shuntNum) in busID[0][:]):
			wx.MessageBox("This bus number is not existing!")
			flag = 0

		for i in range(len(shuntNumList[0])):
			if shuntNum == shuntNumList[0][i] and  shuntID in shuntIDList[0][i]:
				wx.MessageBox('This shunt already exists')
				flag = 0

		if not '' in shuntInforList and flag ==1:
			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):
					psspy.case(path)
					psspy.shunt_data(shuntNum,shuntID,REALAR2 = BShunt)
					psspy.save(path)
			else:
				psspy.shunt_data(shuntNum,shuntID,REALAR2 = BShunt)
				psspy.save(self.Path)

			# Ghi vào file macros
			if self.macroFile != '':
				f = open(self.macroFile,'a')
				f.writelines("psspy.shunt_data({a},'{b}',REALAR2 = {c})\n".format(a=shuntNum,b=shuntID,c=BShunt))
				f.close()

			self.flag = 1
			self.Close()
		else:
			event.Skip()
