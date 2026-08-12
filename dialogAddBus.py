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
## Class Add_New_Branch
###########################################################################

class Add_New_Bus ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add New Bus", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"New Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusNumChoices = []
		self.fromBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.fromBusNumChoices, wx.CB_SORT )
		self.fromBusNum.SetSelection( 0 )
		gSizer6.Add( self.fromBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"New Bus Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		self.textCtrl_Name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Name, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Voltage Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gSizer6.Add( self.m_staticText33, 0, wx.ALL, 10 )
		
		comboBoxVoltageLevelChoices = []
		self.comboBoxVoltageLevel = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxVoltageLevelChoices, wx.CB_SORT )
		gSizer6.Add( self.comboBoxVoltageLevel, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Area Num", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		gSizer6.Add( self.m_staticText37, 0, wx.ALL, 10 )
		
		comboBoxAreaNum = []
		self.comboBoxArea = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxAreaNum, 0 )
		gSizer6.Add( self.comboBoxArea, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Zone Num", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer6.Add( self.m_staticText34, 0, wx.ALL, 10 )
		
		comboBoxZoneNum = []
		self.comboBoxZone = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxZoneNum, 0 )
		gSizer6.Add( self.comboBoxZone, 0, wx.ALL, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAddBus = wx.Button( self, wx.ID_ANY, u"Add Bus", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnAddBus, 0, wx.ALL, 5 )
		
		
		gSizer6.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer6 )
		self.Layout()
		gSizer6.Fit( self )
		
		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		self.Path = ''
		self.PathFile = []
		self.flagSynch = 0
		self.macroFile = ''
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.fromBusNum.Bind( wx.EVT_TEXT, self.onTextBusNum )
		self.textCtrl_Name.Bind( wx.EVT_TEXT, self.OnTextBusName )
		self.comboBoxVoltageLevel.Bind( wx.EVT_TEXT, self.onTextVoltageLevel )
		self.comboBoxArea.Bind( wx.EVT_TEXT, self.OnTextArea )
		self.comboBoxZone.Bind( wx.EVT_TEXT, self.onTextZone )
		self.btnAddBus.Bind( wx.EVT_BUTTON, self.AddNewBusDialog )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	# Lấy thông tin từ ô BusNum
	def onTextBusNum( self, event ):
		busNum = self.fromBusNum.GetValue()
		# bac

		luoi_bac = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38] 
		luoi_trung = [50,51,52,53,54,55,56,57,58,59,60,61,62]
		luoi_nam = [70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91]

		zone = 0
		if len(busNum) == 5:
			self.comboBoxVoltageLevel.SetValue(str(500.0))
			self.comboBoxZone.SetValue(busNum[0:2])
			zone = str(busNum[0:2])
			if int(zone) in luoi_bac:
				self.comboBoxArea.SetValue(str(15))
			elif int(zone) in luoi_trung:
				self.comboBoxArea.SetValue(str(25))
			elif int(zone) in luoi_nam:
				self.comboBoxArea.SetValue(str(35))
		else:
			self.comboBoxZone.SetValue(busNum[1:3])
			zone = str(busNum[1:3])
			if int(busNum[0]) == 2:
				self.comboBoxVoltageLevel.SetValue(str(220.0))
				if int(zone) in luoi_bac:
					self.comboBoxArea.SetValue(str(12))
				elif int(zone) in luoi_trung:
					self.comboBoxArea.SetValue(str(22))
				elif int(zone) in luoi_nam:
					self.comboBoxArea.SetValue(str(32))
			elif int(busNum[0]) == 1:
				self.comboBoxVoltageLevel.SetValue(str(110.0))
				if int(zone) in luoi_bac:
					self.comboBoxArea.SetValue(str(11))
				elif int(zone) in luoi_trung:
					self.comboBoxArea.SetValue(str(21))
				elif int(zone) in luoi_nam:
					self.comboBoxArea.SetValue(str(31))
			elif int(busNum[0]) == 3:
				self.comboBoxVoltageLevel.SetValue(str(35.0))
				if int(zone) in luoi_bac:
					self.comboBoxArea.SetValue(str(10))
				elif int(zone) in luoi_trung:
					self.comboBoxArea.SetValue(str(20))
				elif int(zone) in luoi_nam:
					self.comboBoxArea.SetValue(str(30))
			elif int(busNum[0]) == 4:
				self.comboBoxVoltageLevel.SetItems([str(35.0),str(22.0)])
				if int(zone) in luoi_bac:
					self.comboBoxArea.SetValue(str(10))
				elif int(zone) in luoi_trung:
					self.comboBoxArea.SetValue(str(20))
				elif int(zone) in luoi_nam:
					self.comboBoxArea.SetValue(str(30))
	
	def OnTextBusName( self, event ):
		event.Skip()

	def onTextVoltageLevel( self, event ):
		event.Skip()
	
	def OnTextArea( self, event ):
		event.Skip()
	
	def onTextZone( self, event ):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag

	# Tạo dialog thêm mới Bus
	@profiled('psse.add.bus_and_save')
	def AddNewBusDialog( self, event ):
		self.flag = 0
		busNum = int(self.fromBusNum.GetValue().split('-')[0])
		busName = str(self.textCtrl_Name.GetValue())
		voltageLevel = float(self.comboBoxVoltageLevel.GetValue())
		busArea = int(self.comboBoxArea.GetValue())
		busZone = int(self.comboBoxZone.GetValue())
		busInforList = [busNum,busName,voltageLevel,busArea,busZone]

		ierr, busID = psspy.abusint(-1,2,'NUMBER')
		flag = 1
		if (int(busNum) in busID[0][:]):
			wx.MessageBox("This bus number is existing, please change new number!")
			flag = 0

		if not '' in busInforList and flag ==1:
			# bus owner and code default = 1

			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):
					psspy.case(path)
					psspy.bus_data_3(busNum,[1,busArea,busZone,1],[voltageLevel, 1.0,0.0,1.1,0.9,1.1,0.9],busName)
					psspy.save(path)
			else:
				psspy.bus_data_3(busNum,[1,busArea,busZone,1],[voltageLevel, 1.0,0.0,1.1,0.9,1.1,0.9],busName)
				psspy.save(self.Path)

			if self.macroFile != '':
				f = open(self.macroFile,'a')
				f.writelines("""
				psspy.bus_data_3({a},[1,{b},{c},1],[{d}, 1.0,0.0,1.1,0.9,1.1,0.9],'{e}')\n
				""".format(a=busNum,b=busArea,c=busZone,d=voltageLevel,e=busName))
				f.close()

			self.flag = 1
			self.Close()
		else:
			event.Skip()
