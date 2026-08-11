# -*- coding: utf-8 -*- 

###########################################################################
## Python code Loaderated with wxFormBuilder (version Dec 21 2016)
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
## Class Choose bus, area, zone
###########################################################################

class Choose_Bus_Zone_Area( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Choose Bus Zone Area", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		sampleList = []
		self.lbArea = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(100, 100),choices=sampleList)
		gSizer2.Add(self.lbArea, 0, wx.ALL|wx.EXPAND, 5)

		self.lb2Area = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(100, 100),choices=sampleList)
		gSizer2.Add(self.lb2Area, 0, wx.ALL|wx.EXPAND, 5)
		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 4, 0, 0 )


		self.oneaddArea = wx.Button(self.m_panel6, wx.ID_ANY, ">",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.oneaddArea, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiaddArea = wx.Button(self.m_panel6,  wx.ID_ANY,">>", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.multiaddArea, 0, wx.ALL, 5 )
		self.oneMoveArea = wx.Button(self.m_panel6, wx.ID_ANY, "<",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.oneMoveArea, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiMoveArea = wx.Button(self.m_panel6,  wx.ID_ANY,"<<", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer6.Add( self.multiMoveArea, 0, wx.ALL, 5 )
		gSizer1.Add( gSizer6, 4, wx.EXPAND, 5 )
		bSizer30.Add( gSizer1, 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 1, 0, 0 )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		sampleList = []
		self.lbZone = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(100, 100),choices=sampleList) #style = wx.LB_SORT
		gSizer4.Add(self.lbZone, 0, wx.ALL|wx.EXPAND, 5)

		self.lb2Zone = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(100, 100),choices=sampleList) #style = wx.LB_SORT
		gSizer4.Add(self.lb2Zone, 0, wx.ALL|wx.EXPAND, 5)
		gSizer3.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 4, 0, 0 )

		self.oneaddZone = wx.Button(self.m_panel6, wx.ID_ANY, ">",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer7.Add( self.oneaddZone, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiaddZone = wx.Button(self.m_panel6,  wx.ID_ANY,">>", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer7.Add( self.multiaddZone, 0, wx.ALL, 5 )
		self.oneMoveZone = wx.Button(self.m_panel6, wx.ID_ANY, "<",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer7.Add( self.oneMoveZone, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiMoveZone = wx.Button(self.m_panel6,  wx.ID_ANY,"<<", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer7.Add( self.multiMoveZone, 0, wx.ALL, 5 )
		gSizer3.Add( gSizer7, 4, wx.EXPAND, 5 )
		bSizer30.Add( gSizer3, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 1, 0, 0 )
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		sampleList = []
		self.lbBus = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(100, 100),choices=sampleList)
		gSizer9.Add(self.lbBus, 0, wx.ALL|wx.EXPAND, 5)

		self.lb2Bus = wx.ListBox(self.m_panel6, wx.ID_ANY,wx.DefaultPosition,size=(100, 100),choices=sampleList)
		gSizer9.Add(self.lb2Bus, 0, wx.ALL|wx.EXPAND, 5)
		gSizer5.Add( gSizer9, 1, wx.EXPAND, 5 )

		gSizer8 = wx.GridSizer( 0, 4, 0, 0 )


		self.oneaddBus = wx.Button(self.m_panel6, wx.ID_ANY, ">",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer8.Add( self.oneaddBus, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiaddBus = wx.Button(self.m_panel6,  wx.ID_ANY,">>", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer8.Add( self.multiaddBus, 0, wx.ALL, 5 )
		self.oneMoveBus = wx.Button(self.m_panel6, wx.ID_ANY, "<",  wx.DefaultPosition,wx.DefaultSize,0)
		gSizer8.Add( self.oneMoveBus, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		self.multiMoveBus = wx.Button(self.m_panel6,  wx.ID_ANY,"<<", wx.DefaultPosition,wx.DefaultSize,0)
		gSizer8.Add( self.multiMoveBus, 0, wx.ALL, 5 )
		gSizer5.Add( gSizer8, 4, wx.EXPAND, 5 )
		bSizer30.Add( gSizer5, 1, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer8.Add( bSizer33, 1, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer8.Add( bSizer34, 1, wx.EXPAND, 5 )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer8.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnCalContigency = wx.Button( self.m_panel6, wx.ID_ANY, u"Calculation", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnCalContigency, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer8.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		# bSizer30.Add( gSizer1, 1, wx.EXPAND, 5 )
		self.m_panel6.SetSizer( bSizer30 )
		self.m_panel6.Layout()
		bSizer30.Fit( self.m_panel6 )
		
		bSizer36.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer36 )
		self.Layout()
		bSizer36.Fit( self )
		
		self.Centre( wx.BOTH )

		self.flag = 0
		self.mygridArea = wx.grid.Grid
		self.selectedArea = []
		self.pGenArea = 0
		self.pLoadArea = 0
		self.qGenArea = 0
		self.qLoadArea = 0

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		# self.areaNum.Bind( wx.EVT_TEXT, self.onAreaNum )
		# self.textCtrl_AreaName.Bind( wx.EVT_TEXT, self.onTextAreaName )
		# self.textCtrl_CurrentPLoad.Bind( wx.EVT_TEXT, self.onTextCurrentPLoad )
		# self.textCtrl_NewPLoad.Bind( wx.EVT_TEXT, self.onTextNewPLoad )
		# self.textCtrl_ChangePercent.Bind( wx.EVT_TEXT, self.onTextChangePercent )
		# self.textCtrl_Incre.Bind( wx.EVT_TEXT, self.onTextIncremental )
		# self.textCtrl_CurrentPGen.Bind( wx.EVT_TEXT, self.onTextCurrentPGen )
		# self.textCtrl_NewPGen.Bind( wx.EVT_TEXT, self.onTextNewPGen )
		# self.textCtrl_ChangePercentGen.Bind( wx.EVT_TEXT, self.onTextChangePercentGen )
		# self.textCtrl_IncreGen.Bind( wx.EVT_TEXT, self.onTextIncrementalGen )
		self.btnCalContigency.Bind( wx.EVT_BUTTON, self.ContigencyCalculation )
		self.lbBus.Bind(wx.EVT_LISTBOX, self.onSelectBus)
		self.lb2Bus.Bind(wx.EVT_LISTBOX, self.onSelectToMoveBus)
		self.oneaddBus.Bind( wx.EVT_BUTTON, self.oneAddBus_Fcn )
		self.multiaddBus.Bind( wx.EVT_BUTTON, self.multipleAddBus_Fcn )
		self.oneMoveBus.Bind( wx.EVT_BUTTON, self.oneMoveBus_Fcn )
		self.multiMoveBus.Bind( wx.EVT_BUTTON, self.multiMoveBus_Fcn )
		
		self.lbZone.Bind(wx.EVT_LISTBOX, self.onSelectZone)
		self.lb2Zone.Bind(wx.EVT_LISTBOX, self.onSelectToMoveZone)
		self.oneaddZone.Bind( wx.EVT_BUTTON, self.oneAddZone_Fcn )
		self.multiaddZone.Bind( wx.EVT_BUTTON, self.multipleAddZone_Fcn )
		self.oneMoveZone.Bind( wx.EVT_BUTTON, self.oneMoveZone_Fcn )
		self.multiMoveZone.Bind( wx.EVT_BUTTON, self.multiMoveZone_Fcn )

		self.lbArea.Bind(wx.EVT_LISTBOX, self.onSelectArea)
		self.lb2Area.Bind(wx.EVT_LISTBOX, self.onSelectToMoveArea)
		self.oneaddArea.Bind( wx.EVT_BUTTON, self.oneAddArea_Fcn )
		self.multiaddArea.Bind( wx.EVT_BUTTON, self.multipleAddArea_Fcn )
		self.oneMoveArea.Bind( wx.EVT_BUTTON, self.oneMoveArea_Fcn )
		self.multiMoveArea.Bind( wx.EVT_BUTTON, self.multiMoveArea_Fcn )

	def __del__( self ):
		pass

	def onClose( self, event ):
		event.Skip()
		return self.flag

	def ContigencyCalculation( self, event ):

		self.flag = 0
		areaList  = self.lb2Area.Items
		zoneList  = self.lb2Area.Items
		busList  = self.lb2Area.Items
		print('---------------------',areaList,zoneList,busList)
		if not '' in areaNum:

			self.flag = 1 
			self.Close()
			return [areaList,zoneList,busList]
		else:
			event.Skip()

	def onSelectArea(self, event):
		global areaNum
		areaNum = self.lbArea.GetSelections()
		for i in range(len(areaNum)):
			obj = self.lbArea.GetString(areaNum[i])

	def onSelectToMoveArea(self, event):
		global moveArea
		moveArea = self.lb2Area.GetSelections()
		for i in range(len(moveArea)):
			obj = self.lb2Area.GetString(moveArea[i])

	def oneAddArea_Fcn(self,event):
		for i in range(len(areaNum)):
			obj = self.lbArea.GetString(areaNum[i])
			if not obj in self.lb2Area.Items:
				self.selectedArea.append(obj)
				self.lb2Area.Append(obj)

	def multipleAddArea_Fcn(self,event):
		b  = self.lbArea.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2Area.Items:
				self.lb2Area.Append(obj)

	def oneMoveArea_Fcn(self,event):
		for i in range(len(moveArea)):
			obj = self.lb2Area.GetString(len(moveArea)-1-i)
			self.lb2Area.Delete(moveArea[len(moveArea)-1-i])

	def multiMoveArea_Fcn(self,event):
		b  = self.lb2Area.Items
		for i in range(len(b)):
			obj = self.lbArea.GetString(i)
			self.lb2Area.Delete(len(b)-1-i)

	def onSelectZone(self, event):
		global zoneNum
		zoneNum = self.lbZone.GetSelections()
		for i in range(len(zoneNum)):
			obj = self.lbZone.GetString(zoneNum[i])

	def onSelectToMoveZone(self, event):
		global moveZone
		moveZone = self.lb2Zone.GetSelections()
		for i in range(len(moveZone)):
			obj = self.lb2Zone.GetString(moveZone[i])

	def oneAddZone_Fcn(self,event):
		for i in range(len(zoneNum)):
			obj = self.lbZone.GetString(zoneNum[i])
			if not obj in self.lb2Zone.Items:
				self.selectedZone.append(obj)
				self.lb2Zone.Append(obj)

	def multipleAddZone_Fcn(self,event):
		b  = self.lbZone.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2Zone.Items:
				self.lb2Zone.Append(obj)

	def oneMoveZone_Fcn(self,event):
		for i in range(len(moveZone)):
			obj = self.lb2Zone.GetString(len(moveZone)-1-i)
			self.lb2Zone.Delete(moveZone[len(moveZone)-1-i])

	def multiMoveZone_Fcn(self,event):
		b  = self.lb2Zone.Items
		for i in range(len(b)):
			obj = self.lbZone.GetString(i)
			self.lb2Zone.Delete(len(b)-1-i)

	def onSelectBus(self, event):
		global busNum
		busNum = self.lbBus.GetSelections()
		for i in range(len(busNum)):
			obj = self.lbBus.GetString(busNum[i])

	def onSelectToMoveBus(self, event):
		global moveBus
		moveBus = self.lb2Bus.GetSelections()
		for i in range(len(moveBus)):
			obj = self.lb2Bus.GetString(moveBus[i])

	def oneAddBus_Fcn(self,event):
		for i in range(len(busNum)):
			obj = self.lbBus.GetString(busNum[i])
			if not obj in self.lb2Bus.Items:
				self.selectedBus.append(obj)
				self.lb2Bus.Append(obj)

	def multipleAddBus_Fcn(self,event):
		b  = self.lbBus.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2Bus.Items:
				self.lb2Bus.Append(obj)

	def oneMoveBus_Fcn(self,event):
		for i in range(len(moveBus)):
			obj = self.lb2Bus.GetString(len(moveBus)-1-i)
			self.lb2Bus.Delete(moveBus[len(moveBus)-1-i])

	def multiMoveBus_Fcn(self,event):
		b  = self.lb2Bus.Items
		for i in range(len(b)):
			obj = self.lbBus.GetString(i)
			self.lb2Bus.Delete(len(b)-1-i)

if __name__ == "__main__":
    app = wx.Dialog(False)
    frame = Choose_Bus_Zone_Area(None)
    frame.ShowModal(True)
    app.MainLoop()