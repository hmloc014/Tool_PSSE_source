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
import numpy as np
from LoadTab import loadMachineTab
from dynamicDialog import AddDynamicModel
###########################################################################
## Class Add_New_Gen
###########################################################################

class Add_New_Gen ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add New Gen", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		self.matrixGen = []
		self.myGridSource = wx.grid.Grid
		self.indexFile = 0
		self.parent = wx.Frame
		self.Path = ''
		self.DyrNewFile = ''
		self.PathFile = []
		# self.lineNum = 0
		self.gridDyn = wx.grid.Grid
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Machine Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusNumChoices = []
		self.fromBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.fromBusNumChoices, wx.CB_SORT )
		self.fromBusNum.SetSelection( 0 )
		self.gSizer6.Add( self.fromBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Machine Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		self.textCtrl_Name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.gSizer6.Add( self.textCtrl_Name, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		self.gSizer6.Add( self.m_staticText37, 0, wx.ALL, 10 )

		self.cbxTypeChoices = ['Thuy Dien','Thuy Dien Tich Nang','Nhiet Than','Nhiet Khi','Hat Nhan','Sinh Khoi','Dien Gio','Dien Mat Troi']
		self.cbxType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.cbxTypeChoices, wx.CB_SORT )
		# self.cbxType.SetSelection( 0 )
		self.gSizer6.Add( self.cbxType, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Pmax", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		self.gSizer6.Add( self.m_staticText36, 0, wx.ALL, 10 )
		
		comboBoxPmaxChoices = []
		self.comboBoxPmax = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxPmaxChoices )
		self.gSizer6.Add( self.comboBoxPmax, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Voltage Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		self.gSizer6.Add( self.m_staticText33, 0, wx.ALL, 10 )
		
		comboBoxVoltageLevelChoices = []
		self.comboBoxVoltageLevel = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxVoltageLevelChoices )
		self.gSizer6.Add( self.comboBoxVoltageLevel, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Area Num", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		self.gSizer6.Add( self.m_staticText35, 0, wx.ALL, 10 )
		
		comboBoxAreaNum = []
		self.comboBoxArea = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxAreaNum, 0 )
		self.gSizer6.Add( self.comboBoxArea, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Zone Num", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		self.gSizer6.Add( self.m_staticText34, 0, wx.ALL, 10 )
		
		comboBoxZoneNum = []
		self.comboBoxZone = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxZoneNum, 0 )
		self.gSizer6.Add( self.comboBoxZone, 0, wx.ALL, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		self.gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAddDynModel = wx.Button( self, wx.ID_ANY, u"Add Dynamic Model", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnAddDynModel, 0, wx.ALL, 5 )
		
		
		self.gSizer6.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( self.gSizer6 )
		self.Layout()
		self.gSizer6.Fit( self )
		
		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		self.pmaxList = []
		self.flagSynch = 0
		self.macroFile = ''
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.fromBusNum.Bind( wx.EVT_TEXT, self.onTextBusNum )
		self.textCtrl_Name.Bind( wx.EVT_TEXT, self.onTextName )
		self.comboBoxPmax.Bind( wx.EVT_TEXT, self.onTextPMax )
		self.cbxType.Bind( wx.EVT_TEXT, self.onCbxType )
		self.comboBoxVoltageLevel.Bind( wx.EVT_TEXT, self.onTextVoltageLevel )
		self.comboBoxArea.Bind( wx.EVT_TEXT, self.OnTextArea )
		self.comboBoxZone.Bind( wx.EVT_TEXT, self.onTextZone )
		self.btnAddDynModel.Bind( wx.EVT_BUTTON, self.AddDynModelDialog )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	# Lấy thông tin từ ô Bus Num
	def onTextBusNum( self, event ):

		busNum = self.fromBusNum.GetValue().split('-')[0]
		genType = self.cbxType.GetValue()
		zone = busNum[1:3]
		self.comboBoxZone.SetValue(str(zone))
		event.Skip()
	
	def onTextName( self, event ):
		event.Skip()

	def onTextPMax( self, event ):
		event.Skip()
	
	# Lấy thông tin từ ô combo box chọn loại nguồn
	def onCbxType( self, event ):
		nguon_bac = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38] # 16(TD),17(NT),18(NK),19(HN),40(PV),41(W),42(SK),43(TDTN)
		nguon_trung = [50,51,52,53,54,55,56,57,58,59,60,61,62] # 26(TD),27(NT),28(NK),29(HN),50(PV),51(W),52(SK),53(TDTN)
		nguon_nam = [70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91] # 36(TD),37(NT),38(NK),39(HN),60(PV),61(W),62(SK),63(TDTN)
		# 70,80,90,100,110,120 (DMT)
		busNum = self.fromBusNum.GetValue().split('-')[0]
		genType = self.cbxType.GetValue()
		zone = busNum[1:3]
		if int(zone) in nguon_bac:
			if genType == 'Thuy Dien':
				self.comboBoxArea.SetValue(str(16))
			elif genType == 'Nhiet Than':
				self.comboBoxArea.SetValue(str(17))
			elif genType == 'Nhiet Khi':
				self.comboBoxArea.SetValue(str(18))
			elif genType == 'Hat Nhan':
				self.comboBoxArea.SetValue(str(19))
			elif genType == 'Dien Mat Troi':
				self.comboBoxArea.SetItems([str(40),str(70),str(110)])
			elif genType == 'Dien Gio':
				self.comboBoxArea.SetValue(str(41))
			elif genType == 'Sinh Khoi':
				self.comboBoxArea.SetValue(str(42))
			elif genType == 'Thuy Dien Tich Nang':
				self.comboBoxArea.SetValue(str(43))
		elif int(zone) in nguon_trung:
			if genType == 'Thuy Dien':
				self.comboBoxArea.SetValue(str(26))
			elif genType == 'Nhiet Than':
				self.comboBoxArea.SetValue(str(27))
			elif genType == 'Nhiet Khi':
				self.comboBoxArea.SetValue(str(28))
			elif genType == 'Hat Nhan':
				self.comboBoxArea.SetValue(str(29))
			elif genType == 'Dien Mat Troi':
				self.comboBoxArea.SetItems([str(50),str(70),str(80),str(110),str(120)])
			elif genType == 'Dien Gio':
				self.comboBoxArea.SetValue(str(51))
			elif genType == 'Sinh Khoi':
				self.comboBoxArea.SetValue(str(52))
			elif genType == 'Thuy Dien Tich Nang':
				self.comboBoxArea.SetValue(str(53))
		elif int(zone) in nguon_nam:
			if genType == 'Thuy Dien':
				self.comboBoxArea.SetValue(str(36))
			elif genType == 'Nhiet Than':
				self.comboBoxArea.SetValue(str(37))
			elif genType == 'Nhiet Khi':
				self.comboBoxArea.SetValue(str(38))
			elif genType == 'Hat Nhan':
				self.comboBoxArea.SetValue(str(39))
			elif genType == 'Dien Mat Troi':
				self.comboBoxArea.SetItems([str(60),str(90),str(110),str(120)])
			elif genType == 'Dien Gio':
				self.comboBoxArea.SetValue(str(61))
			elif genType == 'Sinh Khoi':
				self.comboBoxArea.SetValue(str(62))
			elif genType == 'Thuy Dien Tich Nang':
				self.comboBoxArea.SetValue(str(63))
		event.Skip()
	
	def onTextVoltageLevel( self, event ):
		event.Skip()
	
	def OnTextArea( self, event ):
		event.Skip()
	
	def onTextZone( self, event ):
		event.Skip()

	# Kết nối Database, chọn thông số mô hình bộ kích từ
	def SelectAVGModel(self,planType=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT DYNAMIC_AVR.[TYPE] FROM DYNAMIC_AVR WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}'));""".format(a=str(planType)))
		avrType = []

		for row in cursor.fetchall():
			if not row[0] in avrType:
				avrType.append(row[0])
		return avrType

	# Kết nối Database, chọn thông số mô hình bộ máy phát GEN
	def SelectGENModel(self,planType=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT DYNAMIC_GEN.[TYPE] FROM DYNAMIC_GEN WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}'));""".format(a=str(planType)))
		genType = []

		for row in cursor.fetchall():
			if not row[0] in genType:
				genType.append(row[0])
		return genType

	# Kết nối Database, chọn thông số mô hình bộ điều tốc GOV
	def SelectGOVModel(self,planType=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT DYNAMIC_GOV.[TYPE] FROM DYNAMIC_GOV WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}'));""".format(a=str(planType)))
		govType = []

		for row in cursor.fetchall():
			if not row[0] in govType:
				govType.append(row[0])
		return govType

	# Kết nối database, chọn mô hình PSS của nguồn
	def SelectPSSModel(self,planType=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT DYNAMIC_PSS.[TYPE] FROM DYNAMIC_PSS WHERE (((DYNAMIC_PSS.[PLAN_TYPE])='{a}'));""".format(a=str(planType)))
		pssType = []

		for row in cursor.fetchall():
			if not row[0] in pssType:
				pssType.append(row[0])
		return pssType

	# Kết nối database, chọn mô hình động của nguồn NLTT
	def SelectRenewModel(self,planType=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT DYNAMIC_RENEW.[TYPE] FROM DYNAMIC_RENEW WHERE (((DYNAMIC_RENEW.[PLAN_TYPE])='{a}'));""".format(a=str(planType)))
		renewType = []

		for row in cursor.fetchall():
			if not row[0] in renewType:
				renewType.append(row[0])
		return renewType

	def onClose( self, event ):
		event.Skip()
		return self.flag

	# Tạo dialog thêm mô hình động cho tổ máy
	def AddDynModelDialog( self, event ):
		self.flag = 0
		machineNum = int(self.fromBusNum.GetValue().split('-')[0])
		machineName = str(self.textCtrl_Name.GetValue())
		Pmax = float(self.comboBoxPmax.GetValue())

		Qmax = float(Pmax/(0.9*(sqrt(1-pow(0.9,2)))))
		planType = str(self.cbxType.GetValue())
		MBase = round(sqrt(pow(Pmax,2)+pow(Qmax,2)))
		voltageLevel = float(self.comboBoxVoltageLevel.GetValue())
		busArea = int(self.comboBoxArea.GetValue())
		busZone = int(self.comboBoxZone.GetValue())

		pType = ''
		if planType == 'Thuy Dien' or planType == 'Thuy Dien Tich Nang':
			pType = 'TD' 
		elif planType == 'Nhiet Than' or planType == 'Nhiet Khi' or planType == 'Hat Nhan' or planType == 'Sinh Khoi':
			pType = 'ND' 
		elif planType == 'Dien Gio':
			pType = 'TYPE3'
		elif planType == 'Dien Mat Troi':
			pType = 'TYPE4'

		genType = self.SelectGENModel(pType)
		avgType = self.SelectAVGModel(pType)
		govType = self.SelectGOVModel(pType)
		pssType = self.SelectPSSModel(pType)
		typeRenew = self.SelectRenewModel(pType)

		Pgen = Pmax
		Pmin = 0
		Qgen = Qmax
		Qmin = -Qmax

		busInforList = [machineNum,machineName,Pmax,voltageLevel,busArea,busZone]

		ierr, machineBusNumber = psspy.abusint(-1,2,'NUMBER') 

		flag = 1


		for i in range(len(machineBusNumber[0])):
			if machineNum == machineBusNumber[0][i]: 
				wx.MessageBox('This machine already exists')
				flag = 0
				break
		# ADD DYNAMIC MODEL
		if flag !=0:
			addDynModel = AddDynamicModel(self)
			addDynModel.planType = pType
			addDynModel.Pmax = Pmax
			addDynModel.busNum = int(machineNum)
			addDynModel.busArea = int(busArea)
			addDynModel.busZone = int(busZone)
			addDynModel.voltageLevel = float(voltageLevel)
			addDynModel.busName = str(machineName)
			addDynModel.dyrNewFile = self.DyrNewFile
			addDynModel.flagSynch = self.flagSynch
			addDynModel.macroFile = self.parent.macroFile
			addDynModel.Path = self.Path
			addDynModel.PathFile = self.PathFile
			addDynModel.gridDyn = self.gridDyn

			if pType == 'TD' or pType == 'ND':
				addDynModel.model1.SetLabel("GEN Model")
				addDynModel.comboBoxModel1.SetItems(genType)
				addDynModel.model2.SetLabel("AVG Model")
				addDynModel.comboBoxModel2.SetItems(avgType)
				addDynModel.model3.SetLabel("GOV Model")
				addDynModel.comboBoxModel3.SetItems(govType)
				addDynModel.model4.SetLabel("PSS Model")
				addDynModel.comboBoxModel4.SetItems(pssType)
				addDynModel.model5.Hide()
				addDynModel.m_grid12.Hide()
				addDynModel.comboBoxModel5.Hide()
				addDynModel.model6.Hide()
				addDynModel.comboBoxModel6.Hide()
				addDynModel.m_grid13.Hide()

			elif pType == 'TYPE3':
				addDynModel.model1.SetLabel("USRMDL")
				addDynModel.comboBoxModel1.SetValue(typeRenew[0])
				addDynModel.model2.SetLabel("USRMDL")
				addDynModel.comboBoxModel2.SetValue(typeRenew[1])
				addDynModel.model3.SetLabel("USRMDL")
				addDynModel.comboBoxModel3.SetValue(typeRenew[2])
				addDynModel.model4.SetLabel("USRMDL")
				addDynModel.comboBoxModel4.SetValue(typeRenew[3])
				addDynModel.model5.SetLabel("USRMDL")
				addDynModel.comboBoxModel5.SetValue(typeRenew[4])
				addDynModel.model6.SetLabel("USRMDL")
				addDynModel.comboBoxModel6.SetValue(typeRenew[5])
				# addDynModel.m_grid9.Hide()
				# addDynModel.m_grid10.Hide()
				# addDynModel.m_grid11.Hide()

			else:
				addDynModel.model1.SetLabel("USRMDL")
				addDynModel.comboBoxModel1.SetValue(typeRenew[0])
				addDynModel.model2.SetLabel("USRMDL")
				addDynModel.comboBoxModel2.SetValue(typeRenew[1])
				addDynModel.model3.SetLabel("USRMDL")
				addDynModel.comboBoxModel3.SetValue(typeRenew[2])
				addDynModel.model4.SetLabel("USRMDL")
				addDynModel.comboBoxModel4.SetValue(typeRenew[3])
				addDynModel.model5.Hide()
				addDynModel.m_grid12.Hide()
				addDynModel.comboBoxModel5.Hide()
				addDynModel.model6.Hide()
				addDynModel.comboBoxModel6.Hide()
				addDynModel.m_grid13.Hide()

			addDynModel.ShowModal()
			# Sau khi cập nhật mô hình động xong thì cập nhật lại bảng nguồn
			self.Close()
			if not addDynModel.onClose(event):
				event.Skip()
			elif self.parent.flagUpdate == 1:
				if self.parent.flagSynch == 1:
					for i,path in enumerate(self.PathFile):
						self.parent.UpdatedData(event,i,path)
				else:
					self.parent.UpdatedData(event,self.indexFile,self.Path)
			else:
				for row1 in range(self.myGridSource.GetNumberRows()):
					for column1 in range(27):
						self.myGridSource.SetCellValue(row1,column1,"")
				self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
				
				for row1 in range(len(self.matrixGen[self.indexFile])):
					for column1 in range(len(self.matrixGen[self.indexFile][0])):
						self.myGridSource.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
					# coff = self.myGridSource.GetCellValue(row1,13)
            		# self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))
