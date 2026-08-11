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
###########################################################################
## Class Add_New_Branch
###########################################################################

class Add_New_Branch ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add New Branch", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"From Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusNumChoices = []
		self.fromBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), self.fromBusNumChoices, wx.CB_SORT )
		self.fromBusNum.SetSelection( 0 )
		gSizer6.Add( self.fromBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"To Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		toBusNumChoices = []
		self.toBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), toBusNumChoices, wx.CB_SORT )
		gSizer6.Add( self.toBusNum, 0, wx.ALL, 5 )
		
		# self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.m_staticText32.Wrap( -1 )
		# gSizer6.Add( self.m_staticText32, 0, wx.ALL, 10 )
		
		# self.textCtrl_ID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		# gSizer6.Add( self.textCtrl_ID, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Voltage Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gSizer6.Add( self.m_staticText33, 0, wx.ALL, 10 )
		
		comboBoxVoltageLevelChoices = []
		self.comboBoxVoltageLevel = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), comboBoxVoltageLevelChoices, wx.CB_SORT )
		gSizer6.Add( self.comboBoxVoltageLevel, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer6.Add( self.m_staticText34, 0, wx.ALL, 10 )
		
		comboBoxTypeChoices = []
		self.comboBoxType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), comboBoxTypeChoices, 0 )
		gSizer6.Add( self.comboBoxType, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gSizer6.Add( self.m_staticText35, 0, wx.ALL, 10 )
		
		self.textCtrl_Length = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Length, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer6.Add( self.m_staticText36, 0, wx.ALL, 10 )
		
		self.textCtrl_Num = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Num, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAddBranch = wx.Button( self, wx.ID_ANY, u"Add Branch", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		bSizer35.Add( self.btnAddBranch, 0, wx.ALL, 5 )
		
		
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
		self.fromBusNum.Bind( wx.EVT_TEXT, self.onTextFromBusNum )
		self.toBusNum.Bind( wx.EVT_TEXT, self.OnTextToBusNum )
		# self.textCtrl_ID.Bind( wx.EVT_TEXT, self.onTextID )
		self.comboBoxVoltageLevel.Bind( wx.EVT_TEXT, self.onTextVoltageLevel )
		self.comboBoxType.Bind( wx.EVT_TEXT, self.OnTextType )
		self.textCtrl_Length.Bind( wx.EVT_TEXT, self.onTextLength )
		self.textCtrl_Num.Bind( wx.EVT_TEXT, self.onTextNum )
		self.btnAddBranch.Bind( wx.EVT_BUTTON, self.AddNewBranchInDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	# Lấy thông tin ở ô From Bus
	def onTextFromBusNum( self, event ):
		busNum = self.fromBusNum.GetValue()
		if len(busNum) == 5:
			self.comboBoxVoltageLevel.SetValue(str(500.0))
		else:
			if int(busNum[0]) == 2:
				self.comboBoxVoltageLevel.SetValue(str(220.0))
			elif int(busNum[0]) == 1:
				self.comboBoxVoltageLevel.SetValue(str(110.0))
			elif int(busNum[0]) == 3:
				self.comboBoxVoltageLevel.SetValue(str(35.0))
			elif int(busNum[0]) == 4:
				self.comboBoxVoltageLevel.SetItems([str(35.0),str(22.0)])
		event.Skip()
	
	def OnTextToBusNum( self, event ):
		event.Skip()
	
	def onTextID( self, event ):
		event.Skip()
	
	# lấy thông tin ở ô Cấp điện áp
	def onTextVoltageLevel( self, event ):
		try:
			busNum = self.fromBusNum.GetValue()
			[linesType] = self.SelectAllLineTypeByBusVoltage(int(busNum))
			self.comboBoxType.SetItems(linesType.tolist())
			event.Skip()
		except:
			event.Skip()
			
	def OnTextType( self, event ):
		event.Skip()
	
	def onTextLength( self, event ):
		event.Skip()

	def onTextNum( self, event ):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag

	# kết nối với database, lấy dữ liệu đường dây từ loại dây
	def SelectBranchInfoFromType(self,typeBr = '',voltage = 0):
		branchType = typeBr
 		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
								r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT LINE_MODELS.[BASE], LINE_MODELS.[TYPE], LINE_MODELS.[I], LINE_MODELS.[Ro], LINE_MODELS.[Xo], LINE_MODELS.[Go], LINE_MODELS.[Bo], LINE_MODELS.[RoZero], LINE_MODELS.[XoZero], LINE_MODELS.[GoZero], LINE_MODELS.[BoZero]
						FROM LINE_MODELS WHERE (((LINE_MODELS.[TYPE])='{a}') AND ((LINE_MODELS.[BASE])={b}));""".format(a=typeBr,b=voltage))
		# SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS; # 
		baseKV = 0
		lineType = ''
		current = 0
		Ro = 0
		Xo = 0
		Bo = 0
		RoZero = 0
		XoZero = 0
		GoZero = 0
		BoZero = 0
		for row in cursor.fetchall():
			baseKV = row[0]
			lineType = row[1]  
			current = row[2]
			Ro = row[3]
			Xo = row[4]
			Go = row[5]
			Bo = row[6]
			RoZero = row[7]
			XoZero = row[8]
			GoZero = row[9]
			BoZero = row[10]
		return baseKV,lineType,current,Ro,Xo,Bo,RoZero,XoZero,GoZero,BoZero

	# kết nối với database, lấy dữ liệu đường dây từ loại dây
	def SelectBranchInfoFromType2(self,typeBr = '',voltage = 0):
		branchType = typeBr
 		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
								r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT LINE_MODELS_2.[BASE], LINE_MODELS_2.[TYPE], LINE_MODELS_2.[I], LINE_MODELS_2.[Ro], LINE_MODELS_2.[Xo], LINE_MODELS_2.[Go], LINE_MODELS_2.[Bo], LINE_MODELS_2.[RoZero], LINE_MODELS_2.[XoZero], LINE_MODELS_2.[GoZero], LINE_MODELS_2.[BoZero],LINE_MODELS_2.[S_MVA]
						FROM LINE_MODELS_2 WHERE (((LINE_MODELS_2.[TYPE])='{a}') AND ((LINE_MODELS_2.[BASE])={b}));""".format(a=typeBr,b=voltage))
		# SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS; # 
		baseKV = 0
		lineType = ''
		current = 0
		Ro = 0
		Xo = 0
		Bo = 0
		RoZero = 0
		XoZero = 0
		GoZero = 0
		BoZero = 0
		for row in cursor.fetchall():
			baseKV = row[0]
			lineType = row[1]  
			current = row[2]
			Ro = row[3]
			Xo = row[4]
			Go = row[5]
			Bo = row[6]
			RoZero = row[7]
			XoZero = row[8]
			GoZero = row[9]
			BoZero = row[10]
			S_MVA = row[11]
		return baseKV,lineType,current,Ro,Xo,Bo,RoZero,XoZero,GoZero,BoZero,S_MVA

	# Lấy tất cả loại đường dây theo cấp điện áp
	def SelectAllLineTypeByBusVoltage(self,BusNum = 0):
		psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(BusNum)],0,[],0,[])
		ierr, busBaseKV = psspy.abusreal(0,2,'BASE')

		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		try:
			cursor.execute("""SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS WHERE (((LINE_MODELS.[BASE])={a}));""".format(a=float(busBaseKV[0][0])))

			lineType = [[]]

			for row in cursor.fetchall():
				lineType[0].append(row[0])
			linesType = np.array([lineType[0]])
			return linesType
		except:
			return []
	
	# Tạo dialog thêm mới đường dây
	def AddNewBranchInDialog( self, event ):
		self.flag = 0
		FromBusNum = int(self.fromBusNum.GetValue().split('-')[0])
		ToBusNum = int(self.toBusNum.GetValue().split('-')[0])
		# BranchID  = str(self.textCtrl_ID.GetValue())
		BranchNum  = str(self.textCtrl_Num.GetValue())
		VoltageLevel = float(self.comboBoxVoltageLevel.GetValue())
		Type = str(self.comboBoxType.GetValue())
		Length = float(self.textCtrl_Length.GetValue())
		branchInforList = [FromBusNum,ToBusNum,VoltageLevel,Type,Length,BranchNum]
		busNumber = FromBusNum
		# create subsystem from bus number
		psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(busNumber)],0,[],0,[])
		# branch

		ierr, fromNumber = psspy.abrnint (0, 2,2,2,1,'FROMNUMBER')
		ierr, toNumber = psspy.abrnint (0, 2,2,2,1,'TONUMBER')

		for i in range(len(fromNumber[0])):
			if busNumber in fromNumber[0]:
				index = fromNumber[0].index(busNumber)
				fromNumber[0].remove(busNumber)

		for i in range(len(toNumber[0])):
			if busNumber in toNumber[0]:
				index = toNumber[0].index(busNumber)
				toNumber[0].remove(busNumber)
		for i in range(len(toNumber[0])):
			fromNumber[0].append(toNumber[0][i])
		ierr, branchID = psspy.abrnchar (0, 2,2,2,1,'ID')

		# flag = 1
		id_branch = []
		for i in range(len(fromNumber[0])):
			if ToBusNum == fromNumber[0][i]: # and  BranchID in branchID[0][i]:
				id_branch.append(int(branchID[0][i]))
		# print('id_branch : ',id_branch)

		id_new = []
		if len(id_branch)!= 0:
			count = 0
			for i in  range(int(BranchNum)):
				count +=1 
				id_new.append(max(id_branch)+count)
		else:
			for i in  range(int(BranchNum)):
				id_new.append(i+1)

		# print('id_new: ',id_new)

		# 		wx.MessageBox('This branch already exists')
		# 		flag = 0
		# 	else:
		


		if not '' in branchInforList: # and flag ==1:
			BrachParams = self.SelectBranchInfoFromType2(Type,VoltageLevel)
			# BrachParams2 = self.SelectBranchInfoFromType2(Type,VoltageLevel)
			bundle = int(str(Type)[-3])

			baseKV = int(BrachParams[0])
			lineType = str(BrachParams[1])
			I = int(BrachParams[2])
			Ro = float(BrachParams[3])
			Xo = float(BrachParams[4])
			Bo = float(BrachParams[5])
			RoZero = float(BrachParams[6])
			XoZero = float(BrachParams[7])
			GoZero = float(BrachParams[8])
			BoZero = float(BrachParams[9])
			BoZero = float(BrachParams[9])
			S_MVA = float(BrachParams[10])

			# if bundle ==1:
			# 	S_MVA = sqrt(3)*I*VoltageLevel*0.001
			# elif (bundle) == 2 or bundle == 3:
			# 	S_MVA = sqrt(3)*I*VoltageLevel*0.0009
			# elif bundle == 4 or bundle == 6 or bundle == 8:
			# 	S_MVA = sqrt(3)*I*VoltageLevel*0.00081

			PBase = 100 #MVA
			Resistor_R = PBase*Length*Ro/pow(VoltageLevel,2)
			Reactor_X = PBase*Length*Xo/pow(VoltageLevel,2)
			Charging_B = pow(VoltageLevel,2)*Bo*Length/(PBase*1000000)
			Resistor_R_Zero = PBase*Length*RoZero/pow(VoltageLevel,2)
			Reactor_X_Zero = PBase*Length*XoZero/pow(VoltageLevel,2)
			Charging_B_Zero = pow(VoltageLevel,2)*BoZero*Length/(PBase*1000000)
			RateA = RateB = RateC = S_MVA 

			# print('param : ',I,Resistor_R,Reactor_X,Charging_B,Resistor_R_Zero,Reactor_X_Zero,Charging_B_Zero)

			#add new bus
			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):
					psspy.case(path)
					for id_br in id_new:
						a = psspy.branch_data(int(FromBusNum),int(ToBusNum),str(id_br),INTGAR2=int(ToBusNum),
																					REALAR1 =Resistor_R,
																					REALAR2 =Reactor_X,
																					REALAR3 =Charging_B,
																					REALAR4 =RateA,
																					REALAR5 =RateB,
																					REALAR6 =RateC,
																					REALAR11 =Length)
						psspy.seq_branch_data_3(int(FromBusNum),int(ToBusNum),str(id_br),0,[Resistor_R_Zero,Reactor_X_Zero,Charging_B_Zero,0.0,0.0,0.0,0.0,0.0]) # not an protected branch
					psspy.save(path)
			else:
				for id_br in id_new:
					a = psspy.branch_data(int(FromBusNum),int(ToBusNum),str(id_br),INTGAR2=int(ToBusNum),
																					REALAR1 =Resistor_R,
																					REALAR2 =Reactor_X,
																					REALAR3 =Charging_B,
																					REALAR4 =RateA,
																					REALAR5 =RateB,
																					REALAR6 =RateC,
																					REALAR11 =Length)
					psspy.seq_branch_data_3(int(FromBusNum),int(ToBusNum),str(id_br),0,[Resistor_R_Zero,Reactor_X_Zero,Charging_B_Zero,0.0,0.0,0.0,0.0,0.0]) # not an protected branch
				psspy.save(self.Path)
			
			if self.macroFile != '':
				f = open(self.macroFile,'a')
				for id_br in id_new:
					f.writelines("psspy.branch_data({a},{b},'{c}',INTGAR2={d},REALAR1 ={e},REALAR2 ={f},REALAR3 ={g},REALAR4 ={h},REALAR5 ={i},REALAR6 ={j},REALAR11 ={k})\n".format(a=int(FromBusNum),b=int(ToBusNum),c=id_br,d=int(ToBusNum),e=Resistor_R,f=Reactor_X,g=Charging_B,h=RateA,i=RateB,j=RateC,k=Length))			
					f.writelines("psspy.seq_branch_data_3({l},{m},'{n}',0,[{o},{p},{q},0.0,0.0,0.0,0.0,0.0]) \n".format(l=int(FromBusNum),m=int(ToBusNum),n=id_br,o=Resistor_R_Zero,p=Reactor_X_Zero,q=Charging_B_Zero))
				f.close()
			self.flag = 1
			self.Close()
			self.Update(event)
			return 1
		else:
			event.Skip()

	def Update(self,event):
		event.Skip()
