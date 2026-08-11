# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
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
## Class Add_New_Gen
###########################################################################

class Scale_Zone( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Zone Source/Load", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		sampleList = []
		self.lb = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(150, 150),style = wx.LB_EXTENDED,choices=sampleList)
		gSizer2.Add(self.lb, 0, wx.ALL|wx.EXPAND, 5)

		self.lb2 = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(150, 150),style = wx.LB_EXTENDED,choices=sampleList)
		gSizer2.Add(self.lb2, 0, wx.ALL|wx.EXPAND, 5)
		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 4, 0, 0 )

		self.oneadd = wx.Button(self.m_panel6, wx.ID_ANY, ">",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.oneadd, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiadd = wx.Button(self.m_panel6,  wx.ID_ANY,">>", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.multiadd, 0, wx.ALL, 5 )
		self.oneMove = wx.Button(self.m_panel6, wx.ID_ANY, "<",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.oneMove, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiMove = wx.Button(self.m_panel6,  wx.ID_ANY,"<<", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.multiMove, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Current PLoad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		self.textCtrl_CurrentPLoad = wx.TextCtrl( self.m_panel6, style=wx.TE_MULTILINE)
		gSizer6.Add( self.textCtrl_CurrentPLoad, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText37 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"% Change", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		gSizer6.Add( self.m_staticText37, 0, wx.ALL, 10 )
		
		self.textCtrl_ChangePercent = wx.TextCtrl( self.m_panel6,style=wx.TE_MULTILINE )
		gSizer6.Add( self.textCtrl_ChangePercent, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"New PLoad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gSizer6.Add( self.m_staticText33, 0, wx.ALL, 10 )
		
		self.textCtrl_NewPLoad = wx.TextCtrl( self.m_panel6,style=wx.TE_MULTILINE)
		gSizer6.Add( self.textCtrl_NewPLoad, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
	
		self.m_staticText35 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Incremental change", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gSizer6.Add( self.m_staticText35, 0, wx.ALL, 10 )
		
		self.textCtrl_Incre = wx.TextCtrl( self.m_panel6,style=wx.TE_MULTILINE)
		gSizer6.Add( self.textCtrl_Incre, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		#----------------------------
		self.m_staticText32 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Current PGen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer6.Add( self.m_staticText32, 0, wx.ALL, 10 )
		
		self.textCtrl_CurrentPGen = wx.TextCtrl( self.m_panel6,style=wx.TE_MULTILINE )
		gSizer6.Add( self.textCtrl_CurrentPGen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"% Change", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer6.Add( self.m_staticText36, 0, wx.ALL, 10 )

		self.textCtrl_ChangePercentGen = wx.TextCtrl( self.m_panel6, style=wx.TE_MULTILINE )
		gSizer6.Add( self.textCtrl_ChangePercentGen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"New PGen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer6.Add( self.m_staticText34, 0, wx.ALL, 10 )

		self.textCtrl_NewPGen = wx.TextCtrl( self.m_panel6,style=wx.TE_MULTILINE)
		gSizer6.Add( self.textCtrl_NewPGen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
	
		self.m_staticText38 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Incremental change", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		gSizer6.Add( self.m_staticText38, 0, wx.ALL, 10 )
		
		self.textCtrl_IncreGen = wx.TextCtrl( self.m_panel6, style=wx.TE_MULTILINE )
		gSizer6.Add( self.textCtrl_IncreGen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Pmax Generator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		self.m_staticText35.Enable( False )
		gSizer6.Add( self.m_staticText35, 0, wx.ALL, 10 )

		self.textCtrl_PGenMax = wx.TextCtrl( self.m_panel6,style=wx.TE_MULTILINE)
		self.textCtrl_PGenMax.Enable( False )
		gSizer6.Add( self.textCtrl_PGenMax, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
	
		self.m_staticText39 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Pmin Generator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		self.m_staticText39.Enable( False )
		gSizer6.Add( self.m_staticText39, 0, wx.ALL, 10 )
		
		self.textCtrl_PGenMin = wx.TextCtrl( self.m_panel6, style=wx.TE_MULTILINE )
		self.textCtrl_PGenMin.Enable( False )
		gSizer6.Add( self.textCtrl_PGenMin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer33 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer34, 1, wx.EXPAND, 5 )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnChangeZoneLoad = wx.Button( self.m_panel6, wx.ID_ANY, u"Scale Zone", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnChangeZoneLoad, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer6.Add( bSizer35, 1, wx.EXPAND, 5 )
		gSizer1.Add( gSizer6, 4, wx.EXPAND, 5 )
		
		self.m_panel6.SetSizer( gSizer1 )
		self.m_panel6.Layout()
		gSizer1.Fit( self.m_panel6 )
		
		bSizer36.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer36 )
		self.Layout()
		bSizer36.Fit( self )
		
		self.CentreOnParent( wx.BOTH )

		self.flag = 0
		self.mygridZone = wx.grid.Grid
		self.selectedZone = []
		self.pGenZone = 0
		self.pLoadZone = 0
		self.qGenZone = 0
		self.qLoadZone = 0
		self.Path = ''
		self.PathFile = []
		self.flagSynch = 0
		self.macroFile = ''
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		# self.zoneNum.Bind( wx.EVT_TEXT, self.onZoneNum )
		# self.textCtrl_ZoneName.Bind( wx.EVT_TEXT, self.onTextZoneName )
		self.textCtrl_CurrentPLoad.Bind( wx.EVT_TEXT, self.onTextCurrentPLoad )
		self.textCtrl_NewPLoad.Bind( wx.EVT_TEXT, self.onTextNewPLoad )
		# self.textCtrl_NewPLoad.Bind( wx.EVT_TEXT_ENTER, self.onTextNewPLoad )
		self.textCtrl_ChangePercent.Bind( wx.EVT_TEXT, self.onTextChangePercent )
		self.textCtrl_Incre.Bind( wx.EVT_TEXT, self.onTextIncremental )
		self.textCtrl_CurrentPGen.Bind( wx.EVT_TEXT, self.onTextCurrentPGen )
		self.textCtrl_NewPGen.Bind( wx.EVT_TEXT, self.onTextNewPGen )
		self.textCtrl_ChangePercentGen.Bind( wx.EVT_TEXT, self.onTextChangePercentGen )
		self.textCtrl_IncreGen.Bind( wx.EVT_TEXT, self.onTextIncrementalGen )
		self.btnChangeZoneLoad.Bind( wx.EVT_BUTTON, self.ChangeZoneLoadDialog )
		self.lb.Bind(wx.EVT_LISTBOX, self.onSelect)
		self.lb2.Bind(wx.EVT_LISTBOX, self.onSelectToMove)
		self.oneadd.Bind( wx.EVT_BUTTON, self.oneAdd_Fcn )
		self.multiadd.Bind( wx.EVT_BUTTON, self.multipleAdd_Fcn )
		self.oneMove.Bind( wx.EVT_BUTTON, self.oneMove_Fcn )
		self.multiMove.Bind( wx.EVT_BUTTON, self.multiMove_Fcn )

	def __del__( self ):
		pass
	
	# Tính toán giá trị Pload, Q load sau các bước hiệu chỉnh
	def onCalculation(self,event):
		num = self.mygridZone.GetNumberRows()
		selectItems = self.lb2.Items
		global zoneNum
		zoneNum = []
		self.pGenZone = 0
		self.qGenZone = 0
		self.pLoadZone = 0
		self.qLoadZone = 0
		for i in range(len(selectItems)):
			obj = selectItems[i].split('-')
			zoneNum.append(int(obj[0]))
		psspy.bsys(1,0,[ 1.0, 0.985E+06],0,[],0,[],0,[],len(zoneNum),zoneNum)
		ierr, pmaxGenZone = psspy.agenbusreal(1,1, "PMAX")
		ierr, pminGenZone = psspy.agenbusreal(1,1, "PMIN")
		ierr, pGenZone = psspy.agenbusreal(1,1, "PGEN")
		ierr, qGenZone = psspy.agenbusreal(1,1, "QGEN")
		# print("--------pmaxGenZone,pminGenZone,pGenZone,qGenZone: ", sum(pmaxGenZone[0]),sum(pminGenZone[0]),sum(pGenZone[0]),sum(qGenZone[0]))
		for i in range(num):
			for j in range(len(zoneNum)):
				if self.mygridZone.GetCellValue(i,0)!= '' and int(zoneNum[j])==int(self.mygridZone.GetCellValue(i,0)):
					row = i
					self.pGenZone += float(self.mygridZone.GetCellValue(row,2))
					self.qGenZone += float(self.mygridZone.GetCellValue(row,3))
					self.pLoadZone += float(self.mygridZone.GetCellValue(row,4))
					self.qLoadZone += float(self.mygridZone.GetCellValue(row,5))
		self.textCtrl_CurrentPLoad.Label = (str(self.pLoadZone))
		self.textCtrl_CurrentPGen.Label = (str(self.pGenZone))
		self.textCtrl_PGenMax.Label = str(sum(pmaxGenZone[0]))
		self.textCtrl_PGenMin.Label = str(sum(pminGenZone[0]))
	
	def onTextCurrentPLoad( self, event ):
		event.Skip()

	# scale P load bằng cách nhập % thay đổi
	def onTextChangePercent( self, event ):
		percent = self.textCtrl_ChangePercent.GetValue()
		newPLoad = self.pLoadZone*(1+float(percent)/100)
		diff = float(newPLoad) - self.pLoadZone
		# từ giá trị mới suy ra % thay đổi và lượng tăng thêm
		self.textCtrl_NewPLoad.Label = str(newPLoad)
		self.textCtrl_Incre.Label = str(diff)

	# scale P load bằng cách nhập giá trị mới
	def onTextNewPLoad( self, event ):
		newPLoad = self.textCtrl_NewPLoad.GetValue()
		diff = float(newPLoad) - self.pLoadZone
		if self.pLoadZone != 0:
			percent = (diff)*100/self.pLoadZone
		else:
			percent = 0
		# từ giá trị mới suy ra % thay đổi và lượng tăng thêm	
		self.textCtrl_Incre.Label = str(diff)
		self.textCtrl_ChangePercent.Label = str(percent)

	# def onTextNewPLoadEnter(self,event):
	# 	event.Skip()

	# scale P load bằng cách nhập lượng tăng thêm
	def onTextIncremental( self, event ):
		diff = self.textCtrl_Incre.GetValue()
		newPLoad = self.pLoadZone + float(diff)
		if self.pGenZone != 0:
			percent = float(diff)*100/self.pLoadZone
		else:
			percent = 0
		# từ lượng tăng thêm suy ra % thay đổi và điền vào ô % thay đổi cũng như giá trị mới
		self.textCtrl_ChangePercent.Label = (str(percent))
		self.textCtrl_NewPLoad.Label = (str(newPLoad))
		event.Skip()

	def onTextCurrentPGen( self, event ):
		event.Skip()

	# scale P gen bằng cách nhập giá trị mới
	def onTextNewPGen( self, event ):
		newPGen = self.textCtrl_NewPGen.GetValue()
		diff = float(newPGen) - self.pGenZone
		if self.pGenZone != 0:
			percent = (diff)*100/self.pGenZone
		else:
			percent = 0
		self.textCtrl_IncreGen.Label = (str(diff))
		self.textCtrl_ChangePercentGen.Label = (str(percent))

	# scale P gen bằng cách nhập % thay đổi
	def onTextChangePercentGen( self, event ):
		percent = self.textCtrl_ChangePercentGen.GetValue()
		newPGen = self.pGenZone*(1+float(percent)/100)
		diff = float(newPGen) - self.pGenZone
		self.textCtrl_IncreGen.Label = (str(diff))
		self.textCtrl_NewPGen.Label = (str(newPGen))

	# scale P load bằng cách nhập lượng tăng thêm
	def onTextIncrementalGen( self, event ):
		diff = self.textCtrl_IncreGen.GetValue()
		newPGen = self.pGenZone + float(diff)
		if self.pGenZone != 0:
			percent = float(diff)*100/self.pGenZone
		else:
			percent = 0
		self.textCtrl_ChangePercentGen.Label = (str(percent))
		self.textCtrl_NewPGen.Label = (str(newPGen))

	def onClose( self, event ):
		event.Skip()
		return self.flag

	# Dialog thay đổi phụ tải của Zone được chọn
	def ChangeZoneLoadDialog( self, event ):
		newPLoad = self.textCtrl_NewPLoad.GetValue()
		newPGen = self.textCtrl_NewPGen.GetValue()
		self.flag = 0


		if not '' in zoneNum:
			if self.flagSynch == 1:
				for path in self.PathFile:
					psspy.case(path)
					psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],len(zoneNum),zoneNum)
					psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],len(zoneNum),zoneNum)
					ierr, shuntGBNomCplx = psspy.afxshuntcplx(0,4,"SHUNTNOM")
					totalReactor = 0
					totalCapacitor = 0
					for i in range(len(shuntGBNomCplx[0])):
						if shuntGBNomCplx[0][i].imag >0:
							totalCapacitor = totalCapacitor + shuntGBNomCplx[0][i].imag
						else:
							totalReactor = totalReactor + shuntGBNomCplx[0][i].imag

					if newPLoad !='' and newPGen =='':
						psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
						psspy.scal_2(0,1,2,[0,1,0,1,0],[float(newPLoad),float(self.pGenZone),0.0,float(totalReactor),float(totalCapacitor),-.0, float(self.qLoadZone)])
					elif newPLoad =='' and newPGen != '':
						psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
						psspy.scal_2(0,1,2,[0,1,0,1,0],[float(self.pLoadZone),float(newPGen),0.0,float(totalReactor),float(totalCapacitor),-.0, float(self.qLoadZone)])
					elif newPLoad != '' and newPGen != '':
						psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
						psspy.scal_2(0,1,2,[0,1,0,1,0],[float(newPLoad),float(newPGen),0.0,float(totalReactor),float(totalCapacitor),-.0, float(self.qLoadZone)])
					psspy.save(path)
			else:
				psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],len(zoneNum),zoneNum)
				psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],len(zoneNum),zoneNum)
				ierr, shuntGBNomCplx = psspy.afxshuntcplx(0,4,"SHUNTNOM")
				totalReactor = 0
				totalCapacitor = 0
				for i in range(len(shuntGBNomCplx[0])):
					if shuntGBNomCplx[0][i].imag >0:
						totalCapacitor = totalCapacitor + shuntGBNomCplx[0][i].imag
					else:
						totalReactor = totalReactor + shuntGBNomCplx[0][i].imag

				if newPLoad !='' and newPGen =='':
					psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
					psspy.scal_2(0,1,2,[0,1,0,1,0],[float(newPLoad),float(self.pGenZone),0.0,float(totalReactor),float(totalCapacitor),-.0, float(self.qLoadZone)])
				elif newPLoad =='' and newPGen != '':
					psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
					psspy.scal_2(0,1,2,[0,1,0,1,0],[float(self.pLoadZone),float(newPGen),0.0,float(totalReactor),float(totalCapacitor),-.0, float(self.qLoadZone)])
				elif newPLoad != '' and newPGen != '':
					psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
					psspy.scal_2(0,1,2,[0,1,0,1,0],[float(newPLoad),float(newPGen),0.0,float(totalReactor),float(totalCapacitor),-.0, float(self.qLoadZone)])
				psspy.save(self.Path)

			if self.macroFile != '':
				f = open(self.macroFile,'a')
				if newPLoad !='' and newPGen =='':
					f.writelines("psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])\n")
					f.writelines("psspy.scal_2(0,1,2,[0,1,0,1,0],[{a},{b},0.0,{c},{d},-.0, {e}])\n".format(a=float(newPLoad),b=float(self.pGenZone),c=float(totalReactor),d=float(totalCapacitor),e=float(self.qLoadZone)))
				elif newPLoad =='' and newPGen != '':
					f.writelines("psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])\n")
					f.writelines("psspy.scal_2(0,1,2,[0,1,0,1,0],[{a},{b},0.0,{c},{d},-.0, {e}])\n".format(a=float(self.pLoadZone),b=float(newPGen),c=float(totalReactor),d=float(totalCapacitor),e=float(self.qLoadZone)))
				elif newPLoad != '' and newPGen != '':
					f.writelines("psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])\n")
					f.writelines("psspy.scal_2(0,1,2,[0,1,0,1,0],[{a},{b},0.0,{c},{d},-.0, {e}])\n".format(a=float(newPLoad),b=float(newPGen),c=float(totalReactor),d=float(totalCapacitor),e=float(self.qLoadZone)))
				f.close()

			self.flag = 1
			self.Close()
		else:
			event.Skip()

	# chọn area để thêm vào cột quan sát
	def onSelect(self, event):
		global zoneNum
		zoneNum = self.lb.GetSelections()
		for i in range(len(zoneNum)):
			obj = self.lb.GetString(zoneNum[i])

	# chọn area để loại khỏi cột quan sát
	def onSelectToMove(self, event):
		global move
		move = self.lb2.GetSelections()
		for i in range(len(move)):
			obj = self.lb2.GetString(move[i])

	# Thêm 1 area vào cột quan sát
	def oneAdd_Fcn(self,event):
		for i in range(len(zoneNum)):
			obj = self.lb.GetString(zoneNum[i])
			if not obj in self.lb2.Items:
				self.selectedZone.append(obj)
				self.lb2.Append(obj)
		self.onCalculation(event)

	# Thêm nhiều area vào cột quan sát
	def multipleAdd_Fcn(self,event):
		b  = self.lb.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2.Items:
				self.lb2.Append(obj)
		self.onCalculation(event)

	# Di chuyển 1 area ra khỏi cột quan sát
	def oneMove_Fcn(self,event):
		for i in range(len(move)):
			obj = self.lb2.GetString(len(move)-1-i)
			self.lb2.Delete(move[len(move)-1-i])
		self.onCalculation(event)

	# Di chuyển nhiều area ra khỏi cột quan sát
	def multiMove_Fcn(self,event):
		b  = self.lb2.Items

		for i in range(len(b)):
			obj = self.lb.GetString(i)
			self.lb2.Delete(len(b)-1-i)
		self.onCalculation(event)
