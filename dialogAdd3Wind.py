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
## Class Add_New_3Wind
###########################################################################

class Add_New_3Wind ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add New 3-Windding Transformer ", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"From Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusNumChoices = []
		self.fromBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.fromBusNumChoices, wx.CB_SORT )
		self.fromBusNum.SetSelection( 0 )
		gSizer6.Add( self.fromBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"To Second Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		toSecondBusNumChoices = []
		self.toSecondBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), toSecondBusNumChoices, wx.CB_SORT )
		gSizer6.Add( self.toSecondBusNum, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"To Third Bus Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gSizer6.Add( self.m_staticText33, 0, wx.ALL, 10 )
		
		toThirdBusNumChoices = []
		self.toThirdBusNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), toThirdBusNumChoices, wx.CB_SORT )
		gSizer6.Add( self.toThirdBusNum, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer6.Add( self.m_staticText34, 0, wx.ALL, 10 )
		
		comboBoxTypeChoices = []
		self.comboBoxType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), comboBoxTypeChoices, 0 )
		gSizer6.Add( self.comboBoxType, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Trans Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gSizer6.Add( self.m_staticText35, 0, wx.ALL, 10 )
		
		self.textCtrl_Name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Name, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer6.Add( self.m_staticText32, 0, wx.ALL, 10 )
		
		self.textCtrl_Num = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Num, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAdd3Wind = wx.Button( self, wx.ID_ANY, u"Add 3-Wind", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnAdd3Wind, 0, wx.ALL, 5 )
		
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
		self.toSecondBusNum.Bind( wx.EVT_TEXT, self.OnTextToSecondBusNum )
		self.toThirdBusNum.Bind( wx.EVT_TEXT, self.OnTextToThirdBusNum )
		self.textCtrl_Num.Bind( wx.EVT_TEXT, self.onTextNum )
		self.comboBoxType.Bind( wx.EVT_TEXT, self.OnTextType )
		self.textCtrl_Name.Bind( wx.EVT_TEXT, self.onTextName )
		self.btnAdd3Wind.Bind( wx.EVT_BUTTON, self.AddNew3WindInDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	# Lấy thông tin nhập vào từ ô Frombus
	def onTextFromBusNum( self, event ):
		try:
			busNum = self.fromBusNum.GetValue()
			[transType] = self.SelectAllTransTypeByBusVoltage(int(busNum.split('-')[0]))
			self.comboBoxType.SetItems(transType.tolist())
			self.textCtrl_Name.SetValue(int(busNum.split('-')[1]))
			event.Skip()
		except:
			event.Skip()
	
	def OnTextToSecondBusNum( self, event ):
		event.Skip()

	def OnTextToThirdBusNum( self, event ):
		event.Skip()
	
	def onTextNum( self, event ):
		event.Skip()
	
	def OnTextType( self, event ):
		event.Skip()

	def onTextName( self, event ):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flaghay 

	# kết nối với database, lấy tất cả loại MBA 3 CD theo cấp điện áp
	def SelectAllTransTypeByBusVoltage(self,BusNum = 0):
		psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(BusNum)],0,[],0,[])
		ierr, busBaseKV = psspy.abusreal(0,2,'BASE')

		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT TRANS_MODELS_3_WIND.[TYPE] FROM TRANS_MODELS_3_WIND WHERE (((TRANS_MODELS_3_WIND.[BASE])={a}));""".format(a=float(busBaseKV[0][0])))

		TranType = [[]]

		for row in cursor.fetchall():
			TranType[0].append(row[0])
		TransType = np.array([TranType[0]])
		return TransType

	# kết nối với database, lấy dữ liệu MBA 3CD từ loại MBA
	def SelectTransInfoFromType(self,typeTrans = ''):
 		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
								r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		cursor.execute("""SELECT TRANS_MODELS_3_WIND.[TYPE], TRANS_MODELS_3_WIND.[SBASE1],TRANS_MODELS_3_WIND.[R12],TRANS_MODELS_3_WIND.[X12],
						TRANS_MODELS_3_WIND.[R23],TRANS_MODELS_3_WIND.[X23],TRANS_MODELS_3_WIND.[R31],TRANS_MODELS_3_WIND.[X31],TRANS_MODELS_3_WIND.[PCA],
						TRANS_MODELS_3_WIND.[PTA], TRANS_MODELS_3_WIND.[PHA] FROM TRANS_MODELS_3_WIND WHERE (((TRANS_MODELS_3_WIND.[TYPE])='{a}'));""".format(a=typeTrans))
		# SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS; # 

		for row in cursor.fetchall():
			transType = row[0]
			Base = row[1]  
			R12 = row[2]
			X12 = row[3]
			R23 = row[4]
			X23 = row[5]
			R31 = row[6]  
			X31 = row[7]
			PCA = row[8]
			PTA = row[9]
			PHA = row[10]
		return transType,Base,R12,X12,R23,X23,R31,X31,PCA,PTA,PHA
	
	# tạo dialog để thêm mới MBA 3CD
	def AddNew3WindInDialog( self, event ):
		self.flag = 0
		FromBusNum = int(self.fromBusNum.GetValue().split('-')[0])
		SecondBusNum = int(self.toSecondBusNum.GetValue().split('-')[0])
		ThirdBusNum = int(self.toThirdBusNum.GetValue().split('-')[0])
		windNum  = str(self.textCtrl_Num.GetValue())
		Type = str(self.comboBoxType.GetValue())
		windName = str(self.textCtrl_Name.GetValue())
		transInforList = [FromBusNum,SecondBusNum,ThirdBusNum,windNum,Type,windName]
		busNumber = FromBusNum
		# create subnumber from bus number
		psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(busNumber)],0,[],0,[])
		ierr, winding3Num1 = psspy.atr3int(0,1, 3, 2, 1, "WIND1NUMBER")
		ierr, winding3Num2 = psspy.atr3int(0, 1,3, 2, 1, "WIND2NUMBER")
		ierr, winding3Num3 = psspy.atr3int(0, 1, 3, 2, 1, "WIND3NUMBER")
		ierr, wind3ID = psspy.atr3char(0, 1, 3,2, 1,"ID")
		# ierr, wind3IDbyWind = psspy.awndchar(0, 1, 3,3, 1,"ID")

		# flag = 1
		id_3wind = []
		for i in range(len(winding3Num1[0])):
			if SecondBusNum == winding3Num2[0][i] and ThirdBusNum == winding3Num3[0][i]: # and TransID in wind3ID[0][i] :
				# wx.MessageBox('This 3-winding transformer already exists')
				# flag = 0
				id_3wind.append(int(wind3ID[0][i]))

		# print('id_3 wind : ',id_3wind)

		id_new = []
		if len(id_3wind)!= 0:
			count = 0
			for i in  range(int(windNum)):
				count +=1 
				id_new.append(max(id_3wind)+count)
		else:
			for i in  range(int(windNum)):
				id_new.append(i+1)

		# print('id_new: ',id_new)

		if not '' in transInforList: # and flag ==1:
			TransParams = self.SelectTransInfoFromType(Type)

			transType = str(TransParams[0])
			Rate = float(TransParams[1])  
			R12 = float(TransParams[2])  
			X12 = float(TransParams[3])
			R23 = float(TransParams[4])  
			X23 = float(TransParams[5])
			R31 = float(TransParams[6])  
			X31 = float(TransParams[7])
			PCA = float(TransParams[8])
			PTA = float(TransParams[9])  
			PHA = float(TransParams[10])
			a = 0.5*(R12-R23+R31)
			b = 0.5*(R12+R23-R31)
			c = 0.5*(R23+R31-R12)
			d = 0.5*(X12-X23+X31)
			e = 0.5*(X12+X23-X31)
			f = 0.5*(X23+X31-X12)
			# if (a>0):
			# 	R1 = a
			# else:
			# 	R1 = 0
			# if (b>0):
			# 	R2 = b
			# else:
			# 	R2 = 0
			# if (c>0):
			# 	R3 = c
			# else:
			# 	R3 = 0

			# if (d>0):
			# 	X1 = d
			# else:
			# 	X1 = 0
			# if (e>0):
			# 	X2 = e
			# else:
			# 	X2 = 0
			# if (f>0):
			# 	X3 = f
			# else:
			# 	X3 = 0	
			R1 = a
			R2 = b
			R3 = c
			X1 = d
			X2 = e
			X3 = f		
			# R01 = 0.8*R1
			# X01 = 0.8*X1
			# R02 = 0.8*R2
			# X02 = 0.8*X2
			# R03 = 0.8*R3
			# X03 = 0.8*X3
			R01 = R1
			X01 = X1
			R02 = R2
			X02 = X2
			R03 = R3
			X03 = X3

			#add new bus
			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):

					psspy.case(path)
					for id3wind in id_new:
						Name = windName.strip()+ '_{}'.format(id3wind)
						# print('Name: ',Name)
						psspy.three_wnd_imped_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),
																					[1,0,0,0,1,1,1,1,int(FromBusNum),int(FromBusNum),int(SecondBusNum),int(ThirdBusNum)],
																					[R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],
																					[str(Name),''])

						psspy.seq_three_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),
																					INTGAR3=2,
																					REALAR3 =R01,
																					REALAR4 =X01,
																					REALAR7 =R02,
																					REALAR8 =X02,
																					REALAR11 =R03,
																					REALAR12 =X03) # not an protected branch

						psspy.three_wnd_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
						psspy.three_wnd_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
						psspy.three_wnd_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
					
					psspy.save(path)
			else:
				for id3wind in id_new:
					Name = windName.strip()+ '_{}'.format(id3wind)
					# print(Name)
					psspy.three_wnd_imped_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),
																				[1,0,0,0,1,1,1,1,int(FromBusNum),int(FromBusNum),int(SecondBusNum),int(ThirdBusNum)],
																				[R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],[str(Name),''])

					psspy.seq_three_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),
																				INTGAR3=2,
																				REALAR3 =R01,
																				REALAR4 =X01,
																				REALAR7 =R02,
																				REALAR8 =X02,
																				REALAR11 =R03,
																				REALAR12 =X03) # not an protected branch

					psspy.three_wnd_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
					psspy.three_wnd_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
					psspy.three_wnd_winding_data_3(int(FromBusNum),int(SecondBusNum),int(ThirdBusNum),str(id3wind),3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
					psspy.save(self.Path)

			if self.macroFile != '':
				f = open(self.macroFile,'a')
				for id3wind in id_new:
					Name = Name+ '_{}'.format(id3wind)
					f.writelines("psspy.three_wnd_imped_data_3({a1},{a2},{a3},'{c}',[1,0,0,0,1,1,1,1,{a1},{a1},{a2},{a3}],[{d},{e},{f},{g},{h},{i},100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],['{j}',''])\n".format(a1=int(FromBusNum),a2=int(SecondBusNum),a3=int(ThirdBusNum),c=id3wind,d=R12,e=X12,f=R23,g=X23,h=R31,i=X31,j=Name))
					f.writelines("psspy.seq_three_winding_data_3({a1},{a2},{a3},'{c}',INTGAR3=2,REALAR3 ={k},REALAR4 ={l},REALAR7 ={m},REALAR8 ={n},REALAR11 ={o},REALAR12 ={p})\n".format(a1=int(FromBusNum),a2=int(SecondBusNum),a3=int(ThirdBusNum),c=id3wind,k=R01,l=X01,m=R02,n=X02,o=R03,p=X03))		
					f.writelines("psspy.three_wnd_winding_data_3({a1},{a2},{a3},'{c}',1,[17,0,0,1,0],[1.0,0.0,0.0,{q},{q},{q},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a1=int(FromBusNum),a2=int(SecondBusNum),a3=int(ThirdBusNum),c=id3wind,q=PCA))
					f.writelines("psspy.three_wnd_winding_data_3({a1},{a2},{a3},'{c}',2,[17,0,0,1,0],[1.0,0.0,0.0,{r},{r},{r},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a1=int(FromBusNum),a2=int(SecondBusNum),a3=int(ThirdBusNum),c=id3wind,r=PTA))
					f.writelines("psspy.three_wnd_winding_data_3({a1},{a2},{a3},'{c}',3,[17,0,0,1,0],[1.0,0.0,0.0,{s},{s},{s},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a1=int(FromBusNum),a2=int(SecondBusNum),a3=int(ThirdBusNum),c=id3wind,s=PHA))
				f.close()

			self.flag = 1
			self.Close()
			self.Update(event)
			return 1
		else:
			event.Skip()

	def Update(self,event):
		event.Skip()
