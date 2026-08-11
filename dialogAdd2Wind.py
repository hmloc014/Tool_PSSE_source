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
## Class Add_New_2Wind
###########################################################################

class Add_New_2Wind ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add New 2-Windding Transformer ", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"From Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusNumChoices = []
		self.fromBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.fromBusNumChoices, wx.CB_SORT )
		self.fromBusNum.SetSelection( 0 )
		gSizer6.Add( self.fromBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"To Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		toBusNumChoices = []
		self.toBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), toBusNumChoices, wx.CB_SORT )
		gSizer6.Add( self.toBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer6.Add( self.m_staticText32, 0, wx.ALL, 10 )
		
		self.textCtrl_ID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_ID, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer6.Add( self.m_staticText34, 0, wx.ALL, 10 )
		
		comboBoxTypeChoices = []
		self.comboBoxType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxTypeChoices, 0 )
		gSizer6.Add( self.comboBoxType, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAdd2Wind = wx.Button( self, wx.ID_ANY, u"Add 2-Wind", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnAdd2Wind, 0, wx.ALL, 5 )
		
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
		self.textCtrl_ID.Bind( wx.EVT_TEXT, self.onTextID )
		self.comboBoxType.Bind( wx.EVT_TEXT, self.OnTextType )
		self.btnAdd2Wind.Bind( wx.EVT_BUTTON, self.AddNew2WindInDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onTextFromBusNum( self, event ):
		event.Skip()
	
	def OnTextToBusNum( self, event ):
		event.Skip()
	
	def onTextID( self, event ):
		event.Skip()
	
	def OnTextType( self, event ):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag

	# kết nối với database, lấy dữ liệu MBA 2CD từ loại MBA
	def SelectTransInfoFromType(self,typeTrans = ''):
 		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
								r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT TRANS_MODELS_2_WIND.[TYPE], TRANS_MODELS_2_WIND.[R],TRANS_MODELS_2_WIND.[X],TRANS_MODELS_2_WIND.[RATE],
						TRANS_MODELS_2_WIND.[R01],TRANS_MODELS_2_WIND.[X01] FROM TRANS_MODELS_2_WIND WHERE (((TRANS_MODELS_2_WIND.[TYPE])='{a}'));""".format(a=typeTrans))
		# SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS; # 

		for row in cursor.fetchall():
			transType = row[0]
			R = row[1]  
			X = row[2]
			Rate = row[3]
			R01 = row[4]
			X01 = row[5]
		return transType,R,X,Rate,R01,X01
	
	# tạo dialog để thêm mới MBA 2CD
	def AddNew2WindInDialog( self, event ):
		self.flag = 0
		FromBusNum = int(self.fromBusNum.GetValue().split('-')[0])
		ToBusNum = int(self.toBusNum.GetValue().split('-')[0])
		TransID  = str(self.textCtrl_ID.GetValue())
		Type = str(self.comboBoxType.GetValue())
		transInforList = [FromBusNum,ToBusNum,TransID,Type]
		busNumber = FromBusNum
		# create subnumber from bus number
		psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(busNumber)],0,[],0,[])
		# branch

		ierr, machineBusNumber = psspy.abrnint (0, 2,3,6,1,'TONUMBER')
		ierr, wind2ID = psspy.atrnchar(0,2, 3,2, 1,"ID")

		flag = 1
		for i in range(len(machineBusNumber[0])):
			if ToBusNum == machineBusNumber[0][i] and  TransID in wind2ID[0][i]:
				wx.MessageBox('This 2-winding transformer already exists')
				flag = 0

		if not '' in transInforList and flag ==1:
			TransParams = self.SelectTransInfoFromType(Type)

			transType = str(TransParams[0])
			R = float(TransParams[1])
			X = float(TransParams[2])
			Rate = float(TransParams[3])
			R01 = float(TransParams[4])
			X01 = float(TransParams[5])
 
			#add new bus
			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):

					psspy.case(path)
					psspy.two_winding_data_4(int(FromBusNum),int(ToBusNum),TransID,[1,1,1,0,0,0,17,0,int(FromBusNum),0,1,0,1,1,1],
																				[R,X,100.0,1.0,0.0,0.0,1.0,0.0,Rate,Rate,Rate,1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],
																				["NONE",""])
					psspy.seq_two_winding_data_3(int(FromBusNum),int(ToBusNum),TransID,INTGAR1=2,
																				REALAR3 =R01,
																				REALAR4 =X01) # not an protected branch
					psspy.save(path)
			else:
				psspy.two_winding_data_4(int(FromBusNum),int(ToBusNum),TransID,[1,1,1,0,0,0,17,0,int(FromBusNum),0,1,0,1,1,1],
																			[R,X,100.0,1.0,0.0,0.0,1.0,0.0,Rate,Rate,Rate,1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],
																			["NONE",""])
				psspy.seq_two_winding_data_3(int(FromBusNum),int(ToBusNum),TransID,INTGAR1=2,
																			REALAR3 =R01,
																			REALAR4 =X01) # not an protected branch
				psspy.save(self.Path)

			if self.macroFile != '':
				f = open(self.macroFile,'a')
				f.writelines("psspy.two_winding_data_4({a},{b},'{c}',[1,1,1,0,0,0,17,0,{a},0,1,0,1,1,1],[{d},{e},100.0,1.0,0.0,0.0,1.0,0.0,{f},{f},{f},1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],['NONE',''])\n".format(a=int(FromBusNum),b=int(ToBusNum),c=TransID,d=R,e=X,f=Rate))
				f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',INTGAR1=2,REALAR3 = {g},REALAR4 ={h})\n".format(a=int(FromBusNum),b=int(ToBusNum),c=TransID,g=R01,h=X01))
				f.close()

			self.flag = 1
			self.Close()
			self.Update(event)
			return 1
		else:
			event.Skip()

	def Update(self,event):
		event.Skip()
