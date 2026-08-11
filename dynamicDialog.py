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
## Class Add_Dynamc_Model
###########################################################################

class AddDynamicModel ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Dynamic Model", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		self.planType = ''
		self.Pmax = 0
		self.busNum = 0
		self.busArea = 0
		self.busZone = 0
		self.voltageLevel = 0.0
		self.busName = ''
		self.dyrNewFile = ''
		self.gridDyn = wx.grid.Grid
		self.lineNum = 0

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel5.SetMaxSize( wx.Size( 1000,-1 ) )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 1, 10, 0, 0 )
		
		self.model1 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.model1.Wrap( -1 )
		gSizer3.Add( self.model1, 0, wx.ALL, 5 )
		
		comboBoxModel1Choices = []
		self.comboBoxModel1 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, comboBoxModel1Choices, 0 )
		gSizer3.Add( self.comboBoxModel1, 0, wx.ALL, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnAddMachine = wx.Button( self.m_panel5, wx.ID_ANY, u"Add New Gen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnAddMachine, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		bSizer16.Add( gSizer3, 1, wx.EXPAND, 0 )
		
		self.m_grid7 = wx.grid.Grid( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid7.CreateGrid( 1, 100 )
		self.m_grid7.EnableEditing( True )
		self.m_grid7.EnableGridLines( True )
		self.m_grid7.EnableDragGridSize( False )
		self.m_grid7.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid7.EnableDragColMove( False )
		self.m_grid7.EnableDragColSize( True )
		self.m_grid7.SetColLabelSize( 30 )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 80 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid7, 2, wx.ALL, 0 )

		#----------------------------------------
		
		gSizer4 = wx.GridSizer( 0, 10, 0, 0 )
		
		self.model2 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.model2.Wrap( -1 )
		gSizer4.Add( self.model2, 0, wx.ALL, 5 )
		
		comboBoxModel2Choices = []
		self.comboBoxModel2 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, comboBoxModel2Choices, 0 )
		gSizer4.Add( self.comboBoxModel2, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( gSizer4, 1, wx.EXPAND, 0 )
		
		self.m_grid9 = wx.grid.Grid( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid9.CreateGrid( 1, 100 )
		self.m_grid9.EnableEditing( True )
		self.m_grid9.EnableGridLines( True )
		self.m_grid9.EnableDragGridSize( False )
		self.m_grid9.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid9.EnableDragColMove( False )
		self.m_grid9.EnableDragColSize( True )
		self.m_grid9.SetColLabelSize( 30 )
		self.m_grid9.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid9.EnableDragRowSize( True )
		self.m_grid9.SetRowLabelSize( 80 )
		self.m_grid9.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid9.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid9, 2, wx.ALL, 0 )

		# ---------------------------------------------
		gSizer5 = wx.GridSizer( 0, 10, 0, 0 )
		
		self.model3 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.model3.Wrap( -1 )
		gSizer5.Add( self.model3, 0, wx.ALL, 5 )
		
		comboBoxModel3Choices = []
		self.comboBoxModel3 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, comboBoxModel3Choices, 0 )
		gSizer5.Add( self.comboBoxModel3, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( gSizer5, 1, wx.EXPAND, 0 )
		
		self.m_grid10 = wx.grid.Grid( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid10.CreateGrid( 1, 100 )
		self.m_grid10.EnableEditing( True )
		self.m_grid10.EnableGridLines( True )
		self.m_grid10.EnableDragGridSize( False )
		self.m_grid10.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid10.EnableDragColMove( False )
		self.m_grid10.EnableDragColSize( True )
		self.m_grid10.SetColLabelSize( 30 )
		self.m_grid10.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid10.EnableDragRowSize( True )
		self.m_grid10.SetRowLabelSize( 80 )
		self.m_grid10.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid10.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid10, 2, wx.ALL,0 )

		#---------------------------------
		gSizer6 = wx.GridSizer( 0, 10, 0, 0 )
		
		self.model4 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.model4.Wrap( -1 )
		gSizer6.Add( self.model4, 0, wx.ALL, 5 )
		
		comboBoxModel4Choices = []
		self.comboBoxModel4 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, comboBoxModel4Choices, 0 )
		gSizer6.Add( self.comboBoxModel4, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( gSizer6, 1, wx.EXPAND, 0 )
		
		self.m_grid11 = wx.grid.Grid( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid11.CreateGrid( 1, 100 )
		self.m_grid11.EnableEditing( True )
		self.m_grid11.EnableGridLines( True )
		self.m_grid11.EnableDragGridSize( False )
		self.m_grid11.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid11.EnableDragColMove( False )
		self.m_grid11.EnableDragColSize( True )
		self.m_grid11.SetColLabelSize( 30 )
		self.m_grid11.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid11.EnableDragRowSize( True )
		self.m_grid11.SetRowLabelSize( 80 )
		self.m_grid11.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid11.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid11,2, wx.ALL,0 )

		#------------------------------------------------------------------
		gSizer7 = wx.GridSizer( 0, 10, 0, 0 )
		
		self.model5 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.model5.Wrap( -1 )
		gSizer7.Add( self.model5, 0, wx.ALL, 5 )
		
		comboBoxModel5Choices = []
		self.comboBoxModel5 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, comboBoxModel5Choices, 0 )
		gSizer7.Add( self.comboBoxModel5, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( gSizer7, 1, wx.EXPAND, 0 )
		
		self.m_grid12 = wx.grid.Grid( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid12.CreateGrid( 1, 100 )
		self.m_grid12.EnableEditing( True )
		self.m_grid12.EnableGridLines( True )
		self.m_grid12.EnableDragGridSize( False )
		self.m_grid12.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid12.EnableDragColMove( False )
		self.m_grid12.EnableDragColSize( True )
		self.m_grid12.SetColLabelSize( 30 )
		self.m_grid12.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid12.EnableDragRowSize( True )
		self.m_grid12.SetRowLabelSize( 80 )
		self.m_grid12.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid12.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid12,2, wx.ALL,0 )

		#-------------------------------------------------------------------------------
		gSizer8 = wx.GridSizer( 0, 10, 0, 0 )
		
		self.model6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.model6.Wrap( -1 )
		gSizer8.Add( self.model6, 0, wx.ALL, 5 )
		
		comboBoxModel6Choices = []
		self.comboBoxModel6 = wx.ComboBox( self.m_panel5, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, comboBoxModel6Choices, 0 )
		gSizer8.Add( self.comboBoxModel6, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( gSizer8, 1, wx.EXPAND, 0 )
		
		self.m_grid13 = wx.grid.Grid( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid13.CreateGrid( 1, 100 )
		self.m_grid13.EnableEditing( True )
		self.m_grid13.EnableGridLines( True )
		self.m_grid13.EnableDragGridSize( False )
		self.m_grid13.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid13.EnableDragColMove( False )
		self.m_grid13.EnableDragColSize( True )
		self.m_grid13.SetColLabelSize( 30 )
		self.m_grid13.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid13.EnableDragRowSize( True )
		self.m_grid13.SetRowLabelSize( 80 )
		self.m_grid13.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid13.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid13,2, wx.ALL,0 )
		#-----------------------------------------------------------

		self.m_panel5.SetSizer( bSizer16 )
		self.m_panel5.Layout()
		bSizer16.Fit( self.m_panel5 )
		bSizer14.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )
		
		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		self.macroFile = ''
		self.flagSynch = 0
		self.PathFile = []
		self.Path = ''
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.comboBoxModel1.Bind( wx.EVT_TEXT, self.onModel1 )
		self.comboBoxModel2.Bind( wx.EVT_TEXT, self.onModel2 )
		self.comboBoxModel3.Bind( wx.EVT_TEXT, self.onModel3 )
		self.comboBoxModel4.Bind( wx.EVT_TEXT, self.onModel4 )
		self.comboBoxModel5.Bind( wx.EVT_TEXT, self.onModel5 )
		self.comboBoxModel6.Bind( wx.EVT_TEXT, self.onModel6 )
		self.btnAddMachine.Bind( wx.EVT_BUTTON, self.AddNewMachineDialog )
		self.m_grid7.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_model1 )
		self.m_grid9.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_model2 )
		self.m_grid10.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_model3 )
		self.m_grid11.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_model4 )
		self.m_grid12.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_model5 )
		self.m_grid13.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_model6 )
		self.m_grid7.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_model1 )
		self.m_grid9.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_model2 )
		self.m_grid10.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_model3 )
		self.m_grid11.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_model4 )
		self.m_grid12.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_model5 )
		self.m_grid13.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_model6 )

	def __del__( self ):
		pass
	
	
	# GEN model
	def onModel1( self, event ):
		flag = 1
		global valuesModel1,closestVal
		for i in range(100):
			self.m_grid7.SetColLabelValue( i, '' )
			self.m_grid7.SetCellValue(0,i,'' )
		model1 = str(self.comboBoxModel1.GetValue())
		pmaxArr = []
		if self.planType!='TYPE3' and self.planType!='TYPE4' :
			pmaxArr = self.SelectPmax(self.planType,model1,flag)
		else:
			pmaxArr = self.SelectPmax(self.planType,model1,0)
		closestVal = min(pmaxArr,key = lambda x:abs(float(x)-self.Pmax))

		if model1 == "GENROU": 
			label = ["T'do",'T"do',"T'qo",'T"qo','H','D','Xd','Xq',"X'd","X'q",'X"d','X1','S(1.0)','S(1.2)']
			valuesModel1 = self.SelectModel1(self.planType, closestVal,model1)

			for i in range(len(label)):
				self.m_grid7.SetColLabelValue( i, str(label[i]) )
				self.m_grid7.SetCellValue(0,i,str(valuesModel1[i] ))
		elif model1 == "GENSAL":
			label = ["T'do",'T"do','T"qo','H','D','Xd','Xq',"X'd",'X"d','X1','S(1.0)','S(1.2)']
			valuesModel1 = self.SelectModel1(self.planType, closestVal,model1)

			for i in range(len(label)):
				self.m_grid7.SetColLabelValue( i, str(label[i]) )
				self.m_grid7.SetCellValue(0,i,str(valuesModel1[i]) )
		# SOLAR
		elif model1 == 'PVGU1':
			label = ['','','','','','','TlqCmd','TlpCmd','VLVPL1','VLVPL2','GLVPL','VHVRCR','CURHVRCR','Rip_LVPL','T_LVPL']
			valuesModel1 = self.SelectModel1(self.planType, closestVal,model1)
			for i,val in enumerate(valuesModel1):
				if val == 'BUS_DN':
					valuesModel1[i]= '{}'.format(self.busNum)
			
			for i in range(len(label)):
				self.m_grid7.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel1)):
				if str(valuesModel1[i])!='None':
					self.m_grid7.SetCellValue(0,i,str(valuesModel1[i]) )
				else:
					self.m_grid7.SetCellValue(0,i,'')
		# WIND
		elif model1 == 'GEWTGCU1':
			label = ['','','','','','','WTs originNum','Full ConvFlag','Prate','Xeq','Vlvpl1','Vlvpl2','Glvpl','Vhvrcr2','CURhvrcr2','Vlvacr1','VLVACR2','Rip_LVPL','T_LVPL','LVPL1stV','LVPL1stP','LVPL2ndV','LVPL2ndP','LVPL3rdV','LVPL3rdP','Impedance']
			valuesModel1 = self.SelectModel1(self.planType, closestVal,model1)
			for i,val in enumerate(valuesModel1):
				if val == 'BUS_DN':
					valuesModel1[i]= '{}'.format(self.busNum)
				if i == 6:
					valuesModel1[i]= '{}'.format(self.Pmax/float(valuesModel1[i+2]))
					# print('------i and, value model[i], label:',i,valuesModel1[i],label[i])
			
			for i in range(len(label)):
				self.m_grid7.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel1)):
				if str(valuesModel1[i])!='None':
					self.m_grid7.SetCellValue(0,i,str(valuesModel1[i]) )
				else:
					self.m_grid7.SetCellValue(0,i,'')
		############################################################ Condition ##########
		if model1 == 'GENROU':
			self.set_restriction_model1('GENROU')
		elif model1 == 'GENSAL':
			self.set_restriction_model1('GENSAL')
		elif model1 == 'PVGU1':
			self.set_restriction_model1('PVGU1')
		elif model1 == 'GEWTGCU1':
			self.set_restriction_model1('GEWTGCU1')
		event.Skip()

	# AVR model
	def onModel2( self, event ):
		flag = 2
		global valuesModel2
		for i in range(100):
			self.m_grid9.SetColLabelValue( i, '' )
			self.m_grid9.SetCellValue(0,i,'' )

		model2 = str(self.comboBoxModel2.GetValue())

		if model2 == "ESST4B": 
			label = ['TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
			valuesModel2 = self.SelectAVGModel(self.planType, closestVal,model2)
			for i in range(len(label)):
				self.m_grid9.SetColLabelValue( i, str(label[i]) )
				self.m_grid9.SetCellValue(0,i,str(valuesModel2[i] ))
		elif model2 == "EXAC4":
			label = ["TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
			valuesModel2 = self.SelectAVGModel(self.planType, closestVal,model2)
			for i in range(len(label)):
				self.m_grid9.SetColLabelValue( i, str(label[i]) )
				self.m_grid9.SetCellValue(0,i,str(valuesModel2[i]) )
		elif model2 == "ESST1A":
			valuesModel2 = self.SelectAVGModel(self.planType, closestVal,model2)
			for i in range(len(label)):
				self.m_grid9.SetCellValue(0,i,str(valuesModel2[i]) )
		# SOLAR
		elif model2 == 'PVEU1':
			# print('1------------------I am here,pmax is:',self.Pmax)
			label = ['','','','','','','Remote Bus','PFAFLG','VARFLG','PQFLG','Tw','Kpv','Kiv','Kpp','Kip','Kf','Tf','Qmx','Qmn','IPmax','Trv','dPMX','dPMN','Tpower','KQi','Vmincl','Vmaxcl','KVi','Tv','Tp','ImaxTD','IphI','IqhI','PMX']
			valuesModel2 = self.SelectModel1(self.planType, closestVal,model2)
			for i,val in enumerate(valuesModel2):
				if val == 'BUS_DN':
					valuesModel2[i]= '{}'.format(self.busNum)
				if i == len(label)-1:
					
					valuesModel2[i] = self.Pmax
			# 		print('2------------------I am here,pmax is:',self.Pmax)
			for i in range(len(label)):
				self.m_grid9.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel2)):
				if str(valuesModel2[i])!='None':
					self.m_grid9.SetCellValue(0,i,str(valuesModel2[i]) )
				else:
					self.m_grid9.SetCellValue(0,i,'')
		# WIND
		elif model2 == 'GEWTECU1':
			label = ['','','','','','','Remote Bus','PFAFlg','VARFlg','APCFlg','PQFlg','Qdroof FromBus','Qdroof ToBus','Qdroof ID','Tfv','Kpv','Kiv','Rc','Xc','Tfp','Kpp','Kip','Pmax','Pmin','Qmax','Qmin','IPmax','Trv','RPmax','RPmin','Tpowwer','KQu','Vmincl','Vmaxcl','KV','XLmin',\
						'XLmax','Tv','Tp','Fn','Tpav','FRa','FRb','FRc','FRd','PFRa','PFRb','PFRc','PFRd','PFRmax','PFRmin','Tw','Tlvpl','Vlvpl','SPDW1','SPDWmax','SPDWmin','SPDlow','WTTHRES','EBST','KDBR','PDBRmax','IMAXtd','IPHL','IQHL','Tlpqd','Kqd','Xqd','Kwi','DBwi','TLPwi','TWOwi','URLwi','DRLwi','PMXwi','PMNwi','VERmx','VERmn','Vfrz','QZPmx','QZPmn']
			valuesModel2 = self.SelectModel1(self.planType, closestVal,model2)
			for i,val in enumerate(valuesModel2):
				if val == 'BUS_DN':
					valuesModel2[i]= '{}'.format(self.busNum)
			for i in range(len(label)):
				self.m_grid9.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel2)):
				if str(valuesModel2[i])!='None':
					self.m_grid9.SetCellValue(0,i,str(valuesModel2[i]) )
				else:
					self.m_grid9.SetCellValue(0,i,'')
		
		for i in range(self.m_grid9.GetNumberCols()):
			self.m_grid9.SetCellTextColour(0,i,wx.Colour(0,0,0))
		if model2 == 'EXAC4':
			self.set_restriction_model1('EXAC4')
		elif model2 == 'ESST4B':
			self.set_restriction_model1('ESST4B')
		elif model2 == 'PVEU1':
			self.set_restriction_model1('PVEU1')
		elif model2 == 'GEWTECU1':
			self.set_restriction_model1('GEWTECU1')

	# GOV MODEL
	def onModel3( self, event ):
		flag = 3
		global valuesModel3
		for i in range(100):
			self.m_grid10.SetColLabelValue( i, '' )
			self.m_grid10.SetCellValue(0,i,'' )

		model3 = str(self.comboBoxModel3.GetValue())

		if model3 == "TGOV1": 
			label = ['R','T1','VMAX','VMIN','T2','T3','Dt']
			valuesModel3 = self.SelectGOVModel(self.planType, closestVal,model3)
			for i in range(len(label)):
				self.m_grid10.SetColLabelValue( i, str(label[i]) )
				self.m_grid10.SetCellValue(0,i,str(valuesModel3[i] ))
		elif model3 == "HYGOV":
			label = ["R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
			valuesModel3 = self.SelectGOVModel(self.planType, closestVal,model3)
			for i in range(len(label)):
				self.m_grid10.SetColLabelValue( i, str(label[i]) )
				self.m_grid10.SetCellValue(0,i,str(valuesModel3[i]) )
		elif model3 == "GAST":
			label = ["R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
			valuesModel3 = self.SelectGOVModel(self.planType, closestVal,model3)
			for i in range(len(label)):
				self.m_grid10.SetColLabelValue( i, str(label[i]) )
				self.m_grid10.SetCellValue(0,i,str(valuesModel3[i]) )
		# solar
		elif model3 == "PANELU1":
			label = ['','','','','','','PDCMAX200','PDCMAX400','PDCMAX600','PDCMAX800','PDCMAX1000']
			valuesModel3 = self.SelectModel1(self.planType, closestVal,model3)
			for i in range(len(label)):
				self.m_grid10.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel3)):
				if str(valuesModel3[i])!='None':
					self.m_grid10.SetCellValue(0,i,str(valuesModel3[i]) )
				else:
					self.m_grid10.SetCellValue(0,i,'')
		# wind
		elif model3 == "GEWT2MU1":
			label = ['','','','','','','H','DAMP','HTfrac','FREQ','DSHAFT']
			valuesModel3 = self.SelectModel1(self.planType, closestVal,model3)
			for i in range(len(label)):
				self.m_grid10.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel3)):
				if str(valuesModel3[i])!='None':
					self.m_grid10.SetCellValue(0,i,str(valuesModel3[i]) )
				else:
					self.m_grid10.SetCellValue(0,i,'')

		for i in range(self.m_grid10.GetNumberCols()):
			self.m_grid10.SetCellTextColour(0,i,wx.Colour(0,0,0))
		if model3 == 'TGOV1':
			self.set_restriction_model1('TGOV1')
		elif model3 == 'HYGOV':
			self.set_restriction_model1('HYGOV')
		elif model3 == 'GAST':
			self.set_restriction_model1('GAST')
		elif model3 == 'PANELU1':
			self.set_restriction_model1('PANELU1')
		elif model3 == 'GEWT2MU1':
			self.set_restriction_model1('GEWT2MU1')

	# PSS MODEL
	def onModel4( self, event ):
		flag = 4
		global valuesModel4
		for i in range(100):
			self.m_grid11.SetColLabelValue( i, '' )
			self.m_grid11.SetCellValue(0,i,'' )

		model4 = str(self.comboBoxModel4.GetValue())

		if model4 == 'PSS2A':
			label = ['IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
			valuesModel4 = self.SelectPSSModel(self.planType, closestVal,model4)
			for i in range(len(label)):
				self.m_grid11.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel4)):
				if str(valuesModel4[i])!='None':
					self.m_grid11.SetCellValue(0,i,str(valuesModel4[i]) )
				else:
					self.m_grid11.SetCellValue(0,i,'')
		elif model4 == 'IRRADU1':
			label = ['','','','','','','Inservice flag','TIME1','IRRADIANCE1','TIME2','IRRADIANCE2','TIME3','IRRADIANCE3','TIME4','IRRADIANCE4','TIME5','IRRADIANCE5','TIME6','IRRADIANCE6','TIME7','IRRADIANCE7','TIME8','IRRADIANCE8','TIME9','IRRADIANCE9','TIME10','IRRADIANCE10']
			valuesModel4 = self.SelectModel1(self.planType, closestVal,model4)
			for i in range(len(label)):
				self.m_grid11.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel4)):
				if str(valuesModel4[i])!='None':
					self.m_grid11.SetCellValue(0,i,str(valuesModel4[i]) )
				else:
					self.m_grid11.SetCellValue(0,i,'')
		elif model4 == 'GEWTPTU1':
			label = ['','','','','','','','','Tp','Kppt','Kipt','Kpc','Kic','0min','0max','d0/dtmin','d0/dtmax','Pref']
			valuesModel4 = self.SelectModel1(self.planType, closestVal,model4)
			for i in range(len(label)):
				self.m_grid11.SetColLabelValue( i, str(label[i]) )
			for i in range(len(valuesModel4)):
				if str(valuesModel4[i])!='None':
					self.m_grid11.SetCellValue(0,i,str(valuesModel4[i]) )
				else:
					self.m_grid11.SetCellValue(0,i,'')

		for i in range(self.m_grid11.GetNumberCols()):
			self.m_grid11.SetCellTextColour(0,i,wx.Colour(0,0,0))
		if model4 == 'PSS2A':
			self.set_restriction_model1('TGOV1')
		elif model4 == 'IRRADU1':
			self.set_restriction_model1('IRRADU1')
		elif model4 == 'GEWTPTU1':
			self.set_restriction_model1('GEWTPTU1')

	# GEWTARU1 model of wind-type 3
	def onModel5( self, event ):
		global valuesModel5
		for i in range(100):
			self.m_grid12.SetColLabelValue( i, '' )
			self.m_grid12.SetCellValue(0,i,'' )

		model5 = str(self.comboBoxModel5.GetValue())

		label = ['','','','','','','','LamdaMax','LamdaMin','PITCHmax','PITCHmin','Ta','P','Raddius','GBRatio','SYNCHR']
		valuesModel5 = self.SelectModel1(self.planType, closestVal,model5)

		for i in range(len(label)):
			self.m_grid12.SetColLabelValue( i, str(label[i]) )
		for i in range(len(valuesModel5)):
			if str(valuesModel5[i])!='None':
				self.m_grid12.SetCellValue(0,i,str(valuesModel5[i]) )
			else:
				self.m_grid12.SetCellValue(0,i,'')
	
	# GEWTGDU1 model of wind-type 3
	def onModel6( self, event ):
		global valuesModel6
		for i in range(100):
			self.m_grid13.SetColLabelValue( i, '' )
			self.m_grid13.SetCellValue(0,i,'' )

		model6 = str(self.comboBoxModel6.GetValue())

		label = ['','','','','','','','T1G','Tg','MAXg','T1r','T2r','Max']
		# GEWTGDU1
		valuesModel6 = self.SelectModel1(self.planType, closestVal,model6)
		for i in range(len(label)):
			self.m_grid13.SetColLabelValue( i, str(label[i]) )
		for i in range(len(valuesModel6)):
			if str(valuesModel6[i])!='None':
				self.m_grid13.SetCellValue(0,i,str(valuesModel6[i]) )
			else:
				self.m_grid13.SetCellValue(0,i,'')

	# Kết nối với cơ sở dữ liệu, lựa chọn tất cả quy mô nguồn theo loại nhà máy và loại mô hình
	def SelectPmax(self,planType='',model='',flag = 0):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		pmaxArr = []
		if flag == 1: # Gen model
			cursor.execute("""SELECT DYNAMIC_GEN.[SCALE] FROM DYNAMIC_GEN 
						WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
		elif flag == 2: # AVR model
			cursor.execute("""SELECT DYNAMIC_AVR.[SCALE] FROM DYNAMIC_AVR 
						WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
		elif flag == 3: # GOV model
			cursor.execute("""SELECT DYNAMIC_GOV.[SCALE] FROM DYNAMIC_GOV 
						WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
		elif flag == 4:	# PSS model
			cursor.execute("""SELECT DYNAMIC_PSS.[SCALE] FROM DYNAMIC_PSS 
						WHERE (((DYNAMIC_PSS.[PLAN_TYPE])='{a}') AND (DYNAMIC_PSS.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
		else: # Renewable model
			cursor.execute("""SELECT DYNAMIC_RENEW.[SCALE] FROM DYNAMIC_RENEW 
						WHERE (((DYNAMIC_RENEW.[PLAN_TYPE])='{a}') AND (DYNAMIC_RENEW.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))

		for row in cursor.fetchall():
			if not float(row[0]) in pmaxArr:
				pmaxArr.append(float(row[0]))
			else:
				next
		return pmaxArr

	# Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ kích từ theo loại nguồn, theo quy mô và theo loại mô hình (ESST4B/ESST1A/EXAC4)
	def SelectAVGModel(self,planType='',pmax =0.0,model2=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		if model2 == "ESST4B":
			# label = ['TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
			cursor.execute("""SELECT DYNAMIC_AVR.[TR], DYNAMIC_AVR.[KPR], DYNAMIC_AVR.[KIR], DYNAMIC_AVR.[VRMAX],DYNAMIC_AVR.[VRMAX],
							DYNAMIC_AVR.[VRMIN],DYNAMIC_AVR.[TA],DYNAMIC_AVR.[KPM],DYNAMIC_AVR.[KIM],DYNAMIC_AVR.[VMMAX],DYNAMIC_AVR.[VMMIN],
							DYNAMIC_AVR.[KG],DYNAMIC_AVR.[KP],DYNAMIC_AVR.[KI],DYNAMIC_AVR.[VBMAX],DYNAMIC_AVR.[KC],DYNAMIC_AVR.[XL],DYNAMIC_AVR.[THETAP] FROM DYNAMIC_AVR 
							WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[SCALE])={b} AND (DYNAMIC_AVR.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model2)))
		elif model2 == "EXAC4":
			# label = ["TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
			cursor.execute("""SELECT DYNAMIC_AVR.[TR], DYNAMIC_AVR.[VIMAX], DYNAMIC_AVR.[VIMIN], DYNAMIC_AVR.[TC],DYNAMIC_AVR.[TB],
							DYNAMIC_AVR.[KA],DYNAMIC_AVR.[TA],DYNAMIC_AVR.[VRMAX],DYNAMIC_AVR.[VRMIN],DYNAMIC_AVR.[KC] FROM DYNAMIC_AVR 
								WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[SCALE])={b} AND (DYNAMIC_AVR.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model2)))	
		elif model2 == 'ESST1A':
			cursor.execute("""SELECT * FROM DYNAMIC_AVR 
								WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[SCALE])={b} AND (DYNAMIC_AVR.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model2)))	

		values = []
		for row in cursor.fetchall():
			for i in range(len(row)):
				values.append(row[i])
			break
		return values

	# Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ máy phát theo loại nguồn, theo quy mô và theo loại mô hình (GENROU/GENSAL)
	def SelectModel1(self,planType='',pmax =0.0,model1=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		values = []
		if model1 == "GENROU":
			
			cursor.execute("""SELECT DYNAMIC_GEN.[T'do], DYNAMIC_GEN.[T''do], DYNAMIC_GEN.[T'qo], DYNAMIC_GEN.[T''qo],DYNAMIC_GEN.[H],
							DYNAMIC_GEN.[D],DYNAMIC_GEN.[Xd],DYNAMIC_GEN.[Xq],DYNAMIC_GEN.[X'd],DYNAMIC_GEN.[X'q],DYNAMIC_GEN.[X''d],
							DYNAMIC_GEN.[X1],DYNAMIC_GEN.[S10],DYNAMIC_GEN.[S12] FROM DYNAMIC_GEN 
							WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[SCALE])={b} AND (DYNAMIC_GEN.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model1)))
		elif model1 == "GENSAL":
			cursor.execute("""SELECT DYNAMIC_GEN.[T'do], DYNAMIC_GEN.[T''do], DYNAMIC_GEN.[T''qo],DYNAMIC_GEN.[H],
								DYNAMIC_GEN.[D],DYNAMIC_GEN.[Xd],DYNAMIC_GEN.[Xq],DYNAMIC_GEN.[X'd],DYNAMIC_GEN.[X''d],
								DYNAMIC_GEN.[X1],DYNAMIC_GEN.[S10],DYNAMIC_GEN.[S12] FROM DYNAMIC_GEN
								WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[SCALE])={b} AND (DYNAMIC_GEN.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model1)))
		else:
			cursor.execute("""SELECT * FROM DYNAMIC_RENEW WHERE (((DYNAMIC_RENEW.[TYPE])='{a}'));""".format(a=(model1)))

		for row in cursor.fetchall():
			if model1 == "GENROU" or model1 == "GENSAL":
				for i in range(len(row)):
					values.append(row[i])
				break
			else:
				for i in range(4,len(row)):
					values.append(row[i])
				break
		return values

	# Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ điều tốc theo loại nguồn, theo quy mô và theo loại mô hình (TGOV1/HYGOV/GAST)
	def SelectGOVModel(self,planType='',pmax=0.0 ,model3=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		#TGOV1: label = ['R','T1','VMAX','VMIN','T2','T3','Dt']
		if model3 == "TGOV1":
			cursor.execute("""SELECT DYNAMIC_GOV.[R], DYNAMIC_GOV.[T1], DYNAMIC_GOV.[VMAX], DYNAMIC_GOV.[VMIN],DYNAMIC_GOV.[T2],
							DYNAMIC_GOV.[T3],DYNAMIC_GOV.[DT] FROM DYNAMIC_GOV 
							WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[SCALE])={b} AND (DYNAMIC_GOV.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model3)))
		#HYGOV: label = ["R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
		elif model3 == "HYGOV":
			cursor.execute("""SELECT DYNAMIC_GOV.[R], DYNAMIC_GOV.[R2], DYNAMIC_GOV.[TR], DYNAMIC_GOV.[TF],DYNAMIC_GOV.[TG],
							DYNAMIC_GOV.[VELM],DYNAMIC_GOV.[GMAX],DYNAMIC_GOV.[GMIN],DYNAMIC_GOV.[TW],DYNAMIC_GOV.[AT],DYNAMIC_GOV.[DTURB],DYNAMIC_GOV.[QNL] 
							FROM DYNAMIC_GOV WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[SCALE])={b} AND (DYNAMIC_GOV.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model3)))
		#GAST: label = ["R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
		elif model3 == 'GAST':
			cursor.execute("""SELECT DYNAMIC_GOV.[R], DYNAMIC_GOV.[T1], DYNAMIC_GOV.[T2], DYNAMIC_GOV.[T3],DYNAMIC_GOV.[AT_GAST],
							DYNAMIC_GOV.[KT],DYNAMIC_GOV.[VMAX],DYNAMIC_GOV.[VMIN],DYNAMIC_GOV.[DTURB] FROM DYNAMIC_GOV 
								WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[SCALE])={b} AND (DYNAMIC_GOV.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model3)))
		values = []
		for row in cursor.fetchall():
			for i in range(len(row)):
				values.append(row[i])
			break
		return values

	# Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ ổn định theo loại nguồn và theo quy mô
	def SelectPSSModel(self,planType='',pmax =0.0,model4=''):
		conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
							r'DBQ=Database.mdb;')
		cursor = conn.cursor()
		# label = ['IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
		cursor.execute("""SELECT DYNAMIC_PSS.[IC1], DYNAMIC_PSS.[REMBUS1], DYNAMIC_PSS.[IC2], DYNAMIC_PSS.[REMBUS2],DYNAMIC_PSS.[M],
						DYNAMIC_PSS.[N],DYNAMIC_PSS.[TW1],DYNAMIC_PSS.[TW2],DYNAMIC_PSS.[T6],DYNAMIC_PSS.[TW3],DYNAMIC_PSS.[TW4],DYNAMIC_PSS.[T7],
						DYNAMIC_PSS.[Ks2],DYNAMIC_PSS.[Ks3],DYNAMIC_PSS.[T8],DYNAMIC_PSS.[T9],DYNAMIC_PSS.[Ks1],DYNAMIC_PSS.[T1],DYNAMIC_PSS.[T2],
						DYNAMIC_PSS.[T3],DYNAMIC_PSS.[T4],DYNAMIC_PSS.[VSTMAX],DYNAMIC_PSS.[VATMIN] FROM DYNAMIC_PSS 
							WHERE (((DYNAMIC_PSS.[PLAN_TYPE])='{a}') AND (DYNAMIC_PSS.[SCALE])={b});""".format(a=str(planType),b=str(pmax)))
		values = []
		for row in cursor.fetchall():
			for i in range(len(row)):
				values.append(row[i])
			break
		return values

	# Kết nối với cơ sở dữ liệu, lựa chọn thông số mô hình NLTT
	def SelectRenewModel(self,planType='',pmax =0):
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

	# Dialog thêm mới nguồn
	def AddNewMachineDialog( self, event ):
		# GEN
		labelGENROU = ['','','',"T'do",'T"do',"T'qo",'T"qo','H','D','Xd','Xq',"X'd","X'q",'X"d','X1','S(1.0)','S(1.2)']
		labelGENSAL = ['','','',"T'do",'T"do','T"qo','H','D','Xd','Xq',"X'd",'X"d','X1','S(1.0)','S(1.2)']
		# AVR
		labelESST1A = ['','','']
		labelESST4B = ['','','','TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
		labelEXAC4 = ['','','',"TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
		# GOV
		labelTGOV1 = ['','','','R','T1','VMAX','VMIN','T2','T3','Dt']
		labelHYGOV = ['','','',"R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
		labelGAST = ['','','',"R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
		# PSS
		labelPSS2A = ['','','','IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
		# Solar
		labelPVGU1 = ['','','','','','','','','','TlqCmd','TlpCmd','VLVPL1','VLVPL2','GLVPL','VHVRCR','CURHVRCR','Rip_LVPL','T_LVPL']
		labelPVEU = ['','','','','','','','','','Remote Bus','PFAFLG','VARFLG','PQFLG','Tw','Kpv','Kiv','Kpp','Kip','Kf','Tf','Qmx','Qmn','IPmax','Trv','dPMX','dPMN','Tpower','KQi','Vmincl','Vmaxcl','KVi','Tv','Tp','ImaxTD','IphI','IqhI','PMX']
		labelPANELU1 = ['','','','','','','','','','PDCMAX200','PDCMAX400','PDCMAX600','PDCMAX800','PDCMAX1000']
		labelIRRADU1 = ['','','','','','','','','','Inservice flag','TIME1','IRRADIANCE1','TIME2','IRRADIANCE2','TIME3','IRRADIANCE3','TIME4','IRRADIANCE4','TIME5','IRRADIANCE5','TIME6','IRRADIANCE6','TIME7','IRRADIANCE7','TIME8','IRRADIANCE8','TIME9','IRRADIANCE9','TIME10','IRRADIANCE10']
		# Wind
		labelGEWTGCU1 = ['','','','','','','','','','WTs originNum','Full ConvFlag','Prate','Xeq','Vlvpl1','Vlvpl2','Glvpl','Vhvrcr2','CURhvrcr2','Vlvacr1','VLVACR2','Rip_LVPL','T_LVPL','LVPL1stV','LVPL1stP','LVPL2ndV','LVPL2ndP','LVPL3rdV','LVPL3rdP','Impedance']
		labelGEWTECU1 = ['','','','','','','','','','Remote Bus','PFAFlg','VARFlg','APCFlg','PQFlg','Qdroof FromBus','Qdroof ToBus','Qdroof ID','Tfv','Kpv','Kiv','Rc','Xc','Tfp','Kpp','Kip','Pmax','Pmin','Qmax','Qmin','IPmax','Trv','RPmax','RPmin','Tpowwer','KQu','Vmincl','Vmaxcl','KV','XLmin',\
						'XLmax','Tv','Tp','Fn','Tpav','FRa','FRb','FRc','FRd','PFRa','PFRb','PFRc','PFRd','PFRmax','PFRmin','Tw','Tlvpl','Vlvpl','SPDW1','SPDWmax','SPDWmin','SPDlow','WTTHRES','EBST','KDBR','PDBRmax','IMAXtd','IPHL','IQHL','Tlpqd','Kqd','Xqd','Kwi','DBwi','TLPwi','TWOwi','URLwi','DRLwi','PMXwi','PMNwi','VERmx','VERmn','Vfrz','QZPmx','QZPmn']
		labelGEWT2MU1 = ['','','','','','','','','','H','DAMP','HTfrac','FREQ','DSHAFT']
		labelGEWTPTU1 = ['','','','','','','','','','','','Tp','Kppt','Kipt','Kpc','Kic','0min','0max','d0/dtmin','d0/dtmax','Pref']
		labelGEWTARU1 = ['','','','','','','','','','','LamdaMax','LamdaMin','PITCHmax','PITCHmin','Ta','P','Raddius','GBRatio','SYNCHR']
		labelGEWTGDU1 = ['','','','','','','','','','','T1G','Tg','MAXg','T1r','T2r','Max']

		labelTypes = [labelGENROU,labelGENSAL,labelESST1A,labelESST4B,labelEXAC4,labelTGOV1,labelHYGOV,labelGAST,labelPSS2A,labelPVGU1,labelPVEU,labelPANELU1,labelIRRADU1,labelGEWTGCU1,labelGEWTECU1,labelGEWT2MU1,labelGEWTPTU1,labelGEWTARU1,labelGEWTGDU1]
		modelTypes = ['GENROU','GENSAL','ESST1A','ESST4B','EXAC4','TGOV1','HYGOV','GAST','PSS2A','PVGU1','PVEU1','PANELU1','IRRADU1','GEWTGCU1','GEWTECU1','GEWT2MU1','GEWTPTU1','GEWTARU1','GEWTGDU1']

		TypeModel1 = str(self.comboBoxModel1.GetValue()) # gen
		TypeModel2 = str(self.comboBoxModel2.GetValue()) # avr
		TypeModel3 = str(self.comboBoxModel3.GetValue()) # gov
		TypeModel4 = str(self.comboBoxModel4.GetValue()) # pss
		TypeModel5 = str(self.comboBoxModel5.GetValue()) # type3
		TypeModel6 = str(self.comboBoxModel6.GetValue()) # type4
		# label
		labelModel1 = labelTypes[modelTypes.index(TypeModel1)]
		labelModel2 = labelTypes[modelTypes.index(TypeModel2)]
		labelModel3 = labelTypes[modelTypes.index(TypeModel3)]
		labelModel4 = labelTypes[modelTypes.index(TypeModel4)]

		# bus owner =1 and code default = 2
		if self.flagSynch == 1:
			for i,path in enumerate(self.PathFile):
				psspy.case(path)
				psspy.bus_data_3(self.busNum,[2,self.busArea,self.busZone,1],[self.voltageLevel, 1.0,0.0,1.1,0.9,1.1,0.9],self.busName)
				psspy.plant_data(self.busNum,0,[ 1.0, 100.0])
				psspy.save(path)
		else:
			psspy.bus_data_3(self.busNum,[2,self.busArea,self.busZone,1],[self.voltageLevel, 1.0,0.0,1.1,0.9,1.1,0.9],self.busName)
			psspy.plant_data(self.busNum,0,[ 1.0, 100.0])
			psspy.save(self.Path)
		

		if self.macroFile != '':
			f = open(self.macroFile,'a')
			f.writelines("psspy.bus_data_3({a},[2,{b},{c},1],[{d}, 1.0,0.0,1.1,0.9,1.1,0.9],'{e}')\n".format(a=self.busNum,b= self.busArea,c=self.busZone,d=self.voltageLevel,e= self.busName))
			f.writelines("psspy.plant_data({a},0,[ 1.0, 100.0])\n".format(a=self.busNum))
			f.close()

		Qmax = float(self.Pmax*(sqrt(1-pow(0.9,2)))/0.9)
		MBase = round(sqrt(pow(self.Pmax,2)+pow(Qmax,2)))
		Pgen = self.Pmax
		Pmin = 0
		Qgen = Qmax
		Qmin = -Qmax

		rowNums = self.gridDyn.GetNumberRows()
		colNums = self.gridDyn.GetNumberCols()
		flag = 1
		for i in range(rowNums):
			rowArr = []
			if i%2==1:
				for j in range(colNums):
					val = self.gridDyn.GetCellValue(i,j)
					rowArr.append(str(val))
				if all(x is '' for x in rowArr) and i!=0:
					self.lineNum = (i-1)/2
					flag = 0
			if flag == 0:
				break

		if self.planType =='TD' or self.planType =='ND':

			if TypeModel1 == 'GENROU':
				Xsub = valuesModel1[10]
				Xtrans = valuesModel1[8]
				Xsyn = valuesModel1[6]
			else:
				Xsub = valuesModel1[8]
				Xtrans = valuesModel1[7]
				Xsyn = valuesModel1[5]

			XSource = Xneg = Xzero = Xsub

			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):
					psspy.case(path)
					psspy.machine_data_2(self.busNum,'1',REALAR1 = Pgen,REALAR2 = Qgen,
														REALAR3 = Qmax,REALAR4 = Qmin,
														REALAR5 = self.Pmax,REALAR6 = Pmin,
														REALAR7 = MBase,REALAR9 = XSource)
					psspy.seq_machine_data_3(self.busNum,'1', REALAR2 = Xsub,
														REALAR4 = Xneg,REALAR6 = Xzero,
														REALAR7 = Xtrans,REALAR8 = Xsyn)
					psspy.save(path)
			else:
				psspy.machine_data_2(self.busNum,'1',REALAR1 = Pgen,REALAR2 = Qgen,
													REALAR3 = Qmax,REALAR4 = Qmin,
													REALAR5 = self.Pmax,REALAR6 = Pmin,
													REALAR7 = MBase,REALAR9 = XSource)
				psspy.seq_machine_data_3(self.busNum,'1', REALAR2 = Xsub,
													REALAR4 = Xneg,REALAR6 = Xzero,
													REALAR7 = Xtrans,REALAR8 = Xsyn)
				psspy.save(self.Path)

			if self.macroFile != '':
				f = open(self.macroFile,'a')
				f.writelines("psspy.machine_data_2({a},'1',INTGAR6 ={b},REALAR1 = {c},REALAR2 = {d},REALAR3 ={e},REALAR4 = {f},REALAR5 = {g},REALAR6 ={h},REALAR7 = {i},REALAR9 ={j},REALAR17 ={k})\n".format(a=self.busNum,b= windMachineControlMode,c=Pgen,d=Qgen,e= Qmax,f=Qmin,g=self.Pmax,h= Pmin,i=MBase,j= XSource))
				f.writelines("psspy.seq_machine_data_3({a},'1', REALAR2 = {b},REALAR4 = {c},REALAR6 = {d},REALAR7 ={e},REALAR8 ={f})\n".format(a=self.busNum,b=Xsub,c=Xneg,d=Xzero,e= Xtrans,f= Xsyn))
				f.close()

			self.flag = 1
			self.Close()
			# gen id default is 1
			genArr = [str(self.busNum),"'{}'".format(TypeModel1),'1']
			for i1 in range(len(valuesModel1)):
				genArr.append(valuesModel1[i1])
			avrArr = [str(self.busNum),"'{}'".format(TypeModel2),'1']
			for i2 in range(len(valuesModel2)):
				avrArr.append(valuesModel2[i2])
			govArr = [str(self.busNum),"'{}'".format(TypeModel3),'1']
			for i3 in range(len(valuesModel3)):
				govArr.append(valuesModel3[i3])
			pssArr = [str(self.busNum),"'{}'".format(TypeModel4),'1']
			for i4 in range(len(valuesModel4)):
				pssArr.append(valuesModel4[i4])

			if self.dyrNewFile != '':
				f = open(self.dyrNewFile,'a')
				for i1 in range(len(genArr)):
					f.writelines(str(genArr[i1])+'	')
				f.writelines('/	/\n')
				for i2 in range(len(avrArr)):
					f.writelines(str(avrArr[i2])+'	')
				f.writelines('/	/\n')
				for i3 in range(len(govArr)):
					f.writelines(str(govArr[i3])+'	')
				f.writelines('/	/\n')
				for i4 in range(len(pssArr)):
					f.writelines(str(pssArr[i4])+'	')
				f.writelines('/	/\n')
				f.close()
			
			modelGen = ["'GENROU'","'GENSAL'"]
			modelAvr = ["'ESST1A'","'ESST4B'","'EXAC4'"]
			modelGov = ["'TGOV1'","'HYGOV'","'GAST'"]
			
			# celChoiceGen.Destroy()
			celChoiceGen =wx.grid.GridCellChoiceEditor(modelGen,allowOthers=True)
			self.gridDyn.SetCellEditor(self.lineNum*2+1,1,celChoiceGen)
			# celChoiceAvr.Destroy()
			celChoiceAvr =wx.grid.GridCellChoiceEditor(modelAvr,allowOthers=True)
			self.gridDyn.SetCellEditor(self.lineNum*2+3,1,celChoiceAvr)
			# celChoiceGov.Destroy()
			celChoiceGov =wx.grid.GridCellChoiceEditor(modelGov,allowOthers=True)
			self.gridDyn.SetCellEditor(self.lineNum*2+5,1,celChoiceGov)

			for i in range(len(labelModel1)):
				self.gridDyn.SetCellValue(self.lineNum*2,i,str(labelModel1[i]))
			for i in range(len(genArr)):
				self.gridDyn.SetCellValue(self.lineNum*2+1,i,str(genArr[i]))
			for i in range(len(labelModel2)):
				self.gridDyn.SetCellValue(self.lineNum*2+2,i,str(labelModel2[i]))
			for i in range(len(avrArr)):
				self.gridDyn.SetCellValue(self.lineNum*2+3,i,str(avrArr[i]))
			for i in range(len(labelModel3)):
				self.gridDyn.SetCellValue(self.lineNum*2+4,i,str(labelModel3[i]))
			for i in range(len(govArr)):
				self.gridDyn.SetCellValue(self.lineNum*2+5,i,str(govArr[i]))
			for i in range(len(labelModel4)):
				self.gridDyn.SetCellValue(self.lineNum*2+6,i,str(labelModel4[i]))
			for i in range(len(pssArr)):
				self.gridDyn.SetCellValue(self.lineNum*2+7,i,str(pssArr[i]))

		# WIND
		elif self.planType =='TYPE3':
			XSource = Xneg = Xzero = Xsub = Xtrans = Xsyn = 0.8
			windMachineControlMode =  2# +, - Q limits based on WPF
			windMachinePowerFactor = 0.95
			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):
					psspy.case(path)
					psspy.machine_data_2(self.busNum,'1',INTGAR6 = windMachineControlMode,REALAR1 = Pgen,REALAR2 = Qgen,
														REALAR3 = Qmax,REALAR4 = Qmin,
														REALAR5 = self.Pmax,REALAR6 = Pmin,
														REALAR7 = MBase,REALAR9 = XSource,REALAR17 =windMachinePowerFactor)
					psspy.seq_machine_data_3(self.busNum,'1', REALAR2 = Xsub,
												REALAR4 = Xneg,REALAR6 = Xzero,
												REALAR7 = Xtrans,REALAR8 = Xsyn)
					psspy.save(path)
			else:
				psspy.machine_data_2(self.busNum,'1',INTGAR6 = windMachineControlMode,REALAR1 = Pgen,REALAR2 = Qgen,
													REALAR3 = Qmax,REALAR4 = Qmin,
													REALAR5 = self.Pmax,REALAR6 = Pmin,
													REALAR7 = MBase,REALAR9 = XSource,REALAR17 =windMachinePowerFactor)
				psspy.seq_machine_data_3(self.busNum,'1', REALAR2 = Xsub,
											REALAR4 = Xneg,REALAR6 = Xzero,
											REALAR7 = Xtrans,REALAR8 = Xsyn)
				psspy.save(self.Path)

			if self.macroFile != '':
				f = open(self.macroFile,'a')
				f.writelines("psspy.machine_data_2({a},'1',INTGAR6 ={b},REALAR1 = {c},REALAR2 = {d},REALAR3 ={e},REALAR4 = {f},REALAR5 = {g},REALAR6 ={h},REALAR7 = {i},REALAR9 ={j},REALAR17 ={k})\n".format(a=self.busNum,b= windMachineControlMode,c=Pgen,d=Qgen,e= Qmax,f=Qmin,g=self.Pmax,h= Pmin,i=MBase,j= XSource,k=windMachinePowerFactor))
				f.writelines("psspy.seq_machine_data_3({a},'1', REALAR2 = {b},REALAR4 = {c},REALAR6 = {d},REALAR7 ={e},REALAR8 ={f})\n".format(a=self.busNum,b=Xsub,c=Xneg,d=Xzero,e= Xtrans,f= Xsyn))
				f.close()

			self.flag = 1
			self.Close()
			arrTGCU = []
			arrTECU = []
			arrT2MU = []
			arrTPTU = []
			arrTARU = []
			arrTGDU = []
			for i in range(len(valuesModel1)):
				arrTGCU.append(self.m_grid7.GetCellValue(0,i))
			for i in range(len(valuesModel2)):
				arrTECU.append(self.m_grid9.GetCellValue(0,i))
			for i in range(len(valuesModel3)):
				arrT2MU.append(self.m_grid10.GetCellValue(0,i))
			for i in range(len(valuesModel4)):
				arrTPTU.append(self.m_grid11.GetCellValue(0,i))
			for i in range(len(valuesModel5)):
				arrTARU.append(self.m_grid12.GetCellValue(0,i))
			for i in range(len(valuesModel6)):
				arrTGDU.append(self.m_grid13.GetCellValue(0,i))

			arrTGCUFinal = [str(self.busNum),"'{}'".format(TypeModel1),'1']
			arrTECUFinal = [str(self.busNum),"'{}'".format(TypeModel2),'1']
			arrT2MUFinal = [str(self.busNum),"'{}'".format(TypeModel3),'1']
			arrTPTUFinal = [str(self.busNum),"'{}'".format(TypeModel4),'1']
			arrTARUFinal = [str(self.busNum),"'{}'".format(TypeModel5),'1']
			arrTGDUFinal = [str(self.busNum),"'{}'".format(TypeModel6),'1']

			for i1 in range(len(arrTGCU)):
				arrTGCUFinal.append(arrTGCU[i1])
			for i2 in range(len(arrTECU)):
				arrTECUFinal.append(arrTECU[i2])
			for i3 in range(len(arrT2MU)):
				arrT2MUFinal.append(arrT2MU[i3])
			for i4 in range(len(arrTPTU)):
				arrTPTUFinal.append(arrTPTU[i4])
			for i5 in range(len(arrTARU)):
				arrTARUFinal.append(arrTARU[i5])
			for i6 in range(len(arrTGDU)):
				arrTGDUFinal.append(arrTGDU[i6])

			if self.dyrNewFile != '':
				f = open(self.dyrNewFile,'a')
				for i1 in range(len(arrTGCUFinal)):
					f.writelines(str(arrTGCUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrTECUFinal)):
					f.writelines(str(arrTECUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrT2MUFinal)):
					f.writelines(str(arrT2MUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrTPTUFinal)):
					f.writelines(str(arrTPTUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrTARUFinal)):
					f.writelines(str(arrTARUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrTGDUFinal)):
					f.writelines(str(arrTGDUFinal[i1])+'	')
				f.writelines('/	/\n')
				f.close()
			# update gridDyn
			labelModel5 = labelTypes[modelTypes.index(TypeModel5)]
			labelModel6 = labelTypes[modelTypes.index(TypeModel6)]

			for i in range(len(labelModel1)):
				self.gridDyn.SetCellValue(self.lineNum*2,i,str(labelModel1[i]))
			for i in range(len(arrTGCUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+1,i,str(arrTGCUFinal[i]))
			for i in range(len(labelModel2)):
				self.gridDyn.SetCellValue(self.lineNum*2+2,i,str(labelModel2[i]))
			for i in range(len(arrTECUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+3,i,str(arrTECUFinal[i]))
			for i in range(len(labelModel3)):
				self.gridDyn.SetCellValue(self.lineNum*2+4,i,str(labelModel3[i]))
			for i in range(len(arrT2MUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+5,i,str(arrT2MUFinal[i]))
			for i in range(len(labelModel4)):
				self.gridDyn.SetCellValue(self.lineNum*2+6,i,str(labelModel4[i]))
			for i in range(len(arrTPTUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+7,i,str(arrTPTUFinal[i]))
			for i in range(len(labelModel5)):
				self.gridDyn.SetCellValue(self.lineNum*2+8,i,str(labelModel5[i]))
			for i in range(len(arrTARUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+9,i,str(arrTARUFinal[i]))
			for i in range(len(labelModel6)):
				self.gridDyn.SetCellValue(self.lineNum*2+10,i,str(labelModel6[i]))
			for i in range(len(arrTGDUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+11,i,str(arrTGDUFinal[i]))
		# SOLAR
		elif self.planType =='TYPE4':
			XSource = Xneg = Xzero = Xsub = Xtrans = Xsyn = 9999
			windMachineControlMode =  2 # +, - Q limits based on WPF
			windMachinePowerFactor = 0.95
			if self.flagSynch == 1:
				for i,path in enumerate(self.PathFile):
					psspy.case(path)
					psspy.machine_data_2(self.busNum,'1',INTGAR6 = windMachineControlMode,REALAR1 = Pgen,REALAR2 = Qgen,
														REALAR3 = Qmax,REALAR4 = Qmin,
														REALAR5 = self.Pmax,REALAR6 = Pmin,
														REALAR7 = MBase,REALAR9 = XSource,REALAR17 =windMachinePowerFactor)
					psspy.seq_machine_data_3(self.busNum,'1', REALAR2 = Xsub,
														REALAR4 = Xneg,REALAR6 = Xzero,
														REALAR7 = Xtrans,REALAR8 = Xsyn)
					psspy.save(path)
			else:
				psspy.machine_data_2(self.busNum,'1',INTGAR6 = windMachineControlMode,REALAR1 = Pgen,REALAR2 = Qgen,
													REALAR3 = Qmax,REALAR4 = Qmin,
													REALAR5 = self.Pmax,REALAR6 = Pmin,
													REALAR7 = MBase,REALAR9 = XSource,REALAR17 =windMachinePowerFactor)
				psspy.seq_machine_data_3(self.busNum,'1', REALAR2 = Xsub,
													REALAR4 = Xneg,REALAR6 = Xzero,
													REALAR7 = Xtrans,REALAR8 = Xsyn)
				psspy.save(self.Path)

			if self.macroFile != '':
				f = open(self.macroFile,'a')
				f.writelines("psspy.machine_data_2({a},'1',INTGAR6 ={b},REALAR1 = {c},REALAR2 = {d},REALAR3 ={e},REALAR4 = {f},REALAR5 = {g},REALAR6 ={h},REALAR7 = {i},REALAR9 ={j},REALAR17 ={k})\n".format(a=self.busNum,b= windMachineControlMode,c=Pgen,d=Qgen,e= Qmax,f=Qmin,g=self.Pmax,h= Pmin,i=MBase,j= XSource,k=windMachinePowerFactor))
				f.writelines("psspy.seq_machine_data_3({a},'1', REALAR2 = {b},REALAR4 = {c},REALAR6 = {d},REALAR7 ={e},REALAR8 ={f})\n".format(a=self.busNum,b=Xsub,c=Xneg,d=Xzero,e= Xtrans,f= Xsyn))
				f.close()

			self.flag = 1
			self.Close()
						
			arrPVGU = []
			arrPVEU = []
			arrPANELU = []
			arrIRRADU = []
			for i in range(len(valuesModel1)):
				arrPVGU.append(self.m_grid7.GetCellValue(0,i))
			for i in range(len(valuesModel2)):
				arrPVEU.append(self.m_grid9.GetCellValue(0,i))
			for i in range(len(valuesModel3)):
				arrPANELU.append(self.m_grid10.GetCellValue(0,i))
			for i in range(len(valuesModel4)):
				arrIRRADU.append(self.m_grid11.GetCellValue(0,i))

			arrPVGUFinal = [str(self.busNum),"'{}'".format(TypeModel1),'1']
			arrPVEUFinal = [str(self.busNum),"'{}'".format(TypeModel2),'1']
			arrPANELUFinal = [str(self.busNum),"'{}'".format(TypeModel3),'1']
			arrIRRADUFinal = [str(self.busNum),"'{}'".format(TypeModel4),'1']

			for i1 in range(len(arrPVGU)):
				arrPVGUFinal.append(arrPVGU[i1])
			for i2 in range(len(arrPVEU)):
				arrPVEUFinal.append(arrPVEU[i2])
			for i3 in range(len(arrPANELU)):
				arrPANELUFinal.append(arrPANELU[i3])
			for i4 in range(len(arrIRRADU)):
				arrIRRADUFinal.append(arrIRRADU[i4])

			if self.dyrNewFile != '':
				f = open(self.dyrNewFile,'a')
				for i1 in range(len(arrPVGUFinal)):
					f.writelines(str(arrPVGUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrPVEUFinal)):
					f.writelines(str(arrPVEUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrPANELUFinal)):
					f.writelines(str(arrPANELUFinal[i1])+'	')
				f.writelines('/	/\n')
				for i1 in range(len(arrIRRADUFinal)):
					f.writelines(str(arrIRRADUFinal[i1])+'	')
				f.writelines('/	/\n')
				f.close()
				
			for i in range(len(labelModel1)):
				self.gridDyn.SetCellValue(self.lineNum*2,i,str(labelModel1[i]))
			for i in range(len(arrPVGUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+1,i,str(arrPVGUFinal[i]))
			for i in range(len(labelModel2)):
				self.gridDyn.SetCellValue(self.lineNum*2+2,i,str(labelModel2[i]))
			for i in range(len(arrPVEUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+3,i,str(arrPVEUFinal[i]))
			for i in range(len(labelModel3)):
				self.gridDyn.SetCellValue(self.lineNum*2+4,i,str(labelModel3[i]))
			for i in range(len(arrPANELUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+5,i,str(arrPANELUFinal[i]))
			for i in range(len(labelModel4)):
				self.gridDyn.SetCellValue(self.lineNum*2+6,i,str(labelModel4[i]))
			for i in range(len(arrIRRADUFinal)):
				self.gridDyn.SetCellValue(self.lineNum*2+7,i,str(arrIRRADUFinal[i]))
		else:
			event.Skip()
	
	# Thiết lập điều kiện ràng buộc để bôi đỏ những giá trị nằm ngoài vùng giới hạn của model 1
	def set_restriction_model1(self,model=''):
		if model == 'GENSAL':
			# labelGENSAL = ['','','',"T'do",'T"do','T"qo','H','D','Xd','Xq',"X'd",'X"d','X1','S(1.0)','S(1.2)']
			T1do = float(self.m_grid7.GetCellValue(0,0))
			T2do = float(self.m_grid7.GetCellValue(0,1))
			T2qo = float(self.m_grid7.GetCellValue(0,2))
			H = float(self.m_grid7.GetCellValue(0,3))
			D = float(self.m_grid7.GetCellValue(0,4))
			Xd = float(self.m_grid7.GetCellValue(0,5))
			Xq = float(self.m_grid7.GetCellValue(0,6))
			X1d = float(self.m_grid7.GetCellValue(0,7))
			X2d = float(self.m_grid7.GetCellValue(0,8))
			X1 = float(self.m_grid7.GetCellValue(0,9))
			S10 = float(self.m_grid7.GetCellValue(0,10))
			S12 = float(self.m_grid7.GetCellValue(0,11))

			# 0.5*Xd - X'd  > 0
			dk1 = 0.5*Xd - X1d 
			if dk1 <= 0:
				self.m_grid7.SetCellTextColour(0,5, wx.RED)
				self.m_grid7.SetCellTextColour(0,7, wx.RED)
			
			# Xd - Xq > 0
			dk2 = Xd - Xq
			if dk2 <= 0:
				self.m_grid7.SetCellTextColour(0,5, wx.RED)
				self.m_grid7.SetCellTextColour(0,6, wx.RED)

			# Xq - X'd > 0
			dk3 = Xq - X1d
			if dk3 <= 0:
				self.m_grid7.SetCellTextColour(0,6, wx.RED)
				self.m_grid7.SetCellTextColour(0,7, wx.RED)

			# dk4 > 0
			dk4 = X1d - X2d
			if dk4 <= 0:
				self.m_grid7.SetCellTextColour(0,7, wx.RED)
				self.m_grid7.SetCellTextColour(0,8, wx.RED)
			
			# dk5 > 0
			dk5 = X2d - X1
			if dk5 <= 0:
				self.m_grid7.SetCellTextColour(0,8, wx.RED)
				self.m_grid7.SetCellTextColour(0,9, wx.RED)

			# add 
			DELT = 0.01
			# 1<H<10
			if H<=1 or H>=10:
				self.m_grid7.SetCellTextColour(0,3, wx.RED)

			# 0<=D<3
			if D<0 or D>=3:
				self.m_grid7.SetCellTextColour(0,4, wx.RED)

			# 1<T1do<10
			if T1do <=1 or T1do >=10:
				self.m_grid7.SetCellTextColour(0,0, wx.RED)

			# 0.2 <= T1qo <= 1.5

			# 4*DELT <T2do <0.2
			if T2do <= 0.04 or T2do >=0.2:
				self.m_grid7.SetCellTextColour(0,1, wx.RED)

			# 4*DELT <T2qo <0.2
			if T2qo <= 0.04 or T2qo >=0.2:
				self.m_grid7.SetCellTextColour(0,2, wx.RED)

			# Xd <2.5
			if Xd >=2.5:
				self.m_grid7.SetCellTextColour(0,5, wx.RED)

			# S10 > 0
			if S10 <=0:
				self.m_grid7.SetCellTextColour(0,10, wx.RED)

			# S10 > S12
			if (S10 - S12) <= 0:
				self.m_grid7.SetCellTextColour(0,10, wx.RED)
				self.m_grid7.SetCellTextColour(0,11, wx.RED)

		elif model == 'GENROU':
			# labelGENROU = ['','','',"T'do",'T"do',"T'qo",'T"qo','H','D','Xd','Xq',"X'd","X'q",'X"d','X1','S(1.0)','S(1.2)']
			T1do = float(self.m_grid7.GetCellValue(0,0))
			T2do = float(self.m_grid7.GetCellValue(0,1))
			T1qo = float(self.m_grid7.GetCellValue(0,2))
			T2qo = float(self.m_grid7.GetCellValue(0,3))
			H = float(self.m_grid7.GetCellValue(0,4))
			D = float(self.m_grid7.GetCellValue(0,5))
			Xd = float(self.m_grid7.GetCellValue(0,6))
			Xq = float(self.m_grid7.GetCellValue(0,7))
			X1d = float(self.m_grid7.GetCellValue(0,8))
			X1q = float(self.m_grid7.GetCellValue(0,9))
			X2d = float(self.m_grid7.GetCellValue(0,10))
			X1 = float(self.m_grid7.GetCellValue(0,11))
			S10 = float(self.m_grid7.GetCellValue(0,12))
			S12 = float(self.m_grid7.GetCellValue(0,13))
			# X2d = IMAG ----------------------------
			# 0.5*Xd - X'd  > 0
			dk1 = 0.5*Xd - X1d 
			if dk1 <= 0:
				self.m_grid7.SetCellTextColour(0,6, wx.RED)
				self.m_grid7.SetCellTextColour(0,8, wx.RED)
			
			# Xd - Xq > 0
			dk2 = Xd - Xq
			if dk2 <= 0:
				self.m_grid7.SetCellTextColour(0,6, wx.RED)
				self.m_grid7.SetCellTextColour(0,7, wx.RED)

			# Xq - X'd > 0
			dk3 = Xq - X1d
			if dk3 <= 0:
				self.m_grid7.SetCellTextColour(0,7, wx.RED)
				self.m_grid7.SetCellTextColour(0,8, wx.RED)

			# dk4 > 0
			dk4 = X1d - X2d
			if dk4 <= 0:
				self.m_grid7.SetCellTextColour(0,8, wx.RED)
				self.m_grid7.SetCellTextColour(0,10, wx.RED)
			
			# dk5 > 0
			dk5 = X2d - X1
			if dk5 <= 0:
				self.m_grid7.SetCellTextColour(0,10, wx.RED)
				self.m_grid7.SetCellTextColour(0,11, wx.RED)

			# add 
			DELT = 0.01
			# 1<H<10
			if H<=1 or H>=10:
				self.m_grid7.SetCellTextColour(0,4, wx.RED)

			# 0<=D<3
			if D<0 or D>=3:
				self.m_grid7.SetCellTextColour(0,5, wx.RED)

			# 1<T1do<10
			if T1do <=1 or T1do >=10:
				self.m_grid7.SetCellTextColour(0,0, wx.RED)

			# 0.2 <= T1qo <= 1.5
			if T1qo < 0.2 or T1qo > 1.5:
				self.m_grid7.SetCellTextColour(0,2, wx.RED)

			# 4*DELT <T2do <0.2
			if T2do <= 0.04 or T2do >=0.2:
				self.m_grid7.SetCellTextColour(0,1, wx.RED)

			# 4*DELT <T2qo <0.2
			if T2qo <= 0.04 or T2qo >=0.2:
				self.m_grid7.SetCellTextColour(0,3, wx.RED)

			# Xd <2.5
			if Xd >=2.5:
				self.m_grid7.SetCellTextColour(0,6, wx.RED)

			# S10 > 0
			if S10 <=0:
				self.m_grid7.SetCellTextColour(0,12, wx.RED)

			# S10 > S12
			if (S10 - S12) <= 0:
				self.m_grid7.SetCellTextColour(0,12, wx.RED)
				self.m_grid7.SetCellTextColour(0,13, wx.RED)

			# X1q < Xq
			if (Xq - X1q) <= 0:
				self.m_grid7.SetCellTextColour(0,7, wx.RED)
				self.m_grid7.SetCellTextColour(0,9, wx.RED)

			# X1d < X1q
			if (X1q < X1d) <= 0:
				self.m_grid7.SetCellTextColour(0,8, wx.RED)
				self.m_grid7.SetCellTextColour(0,9, wx.RED)

			# X2d < X1q
			if (X1q < X2d) <= 0:
				self.m_grid7.SetCellTextColour(0,9, wx.RED)
				self.m_grid7.SetCellTextColour(0,10, wx.RED)
			
	# Thiết lập điều kiện ràng buộc để bôi đỏ những giá trị nằm ngoài vùng giới hạn của model 2
	def set_restriction_model2(self,model=''):
		if model == 'ESST4B':
			# labelESST4B = ['','','','TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
			TR = float(self.m_grid9.GetCellValue(0,0))
			KPR = float(self.m_grid9.GetCellValue(0,1))
			KIR = float(self.m_grid9.GetCellValue(0,2))
			VRMAX = float(self.m_grid9.GetCellValue(0,3))
			VRMIN = float(self.m_grid9.GetCellValue(0,4))
			TA = float(self.m_grid9.GetCellValue(0,5))
			KPM = float(self.m_grid9.GetCellValue(0,6))
			KIM = float(self.m_grid9.GetCellValue(0,7))
			VMMAX = float(self.m_grid9.GetCellValue(0,8))
			VMMIN = float(self.m_grid9.GetCellValue(0,9))
			KG = float(self.m_grid9.GetCellValue(0,10))
			KP = float(self.m_grid9.GetCellValue(0,11))
			KI = float(self.m_grid9.GetCellValue(0,12))
			VBMAX = float(self.m_grid9.GetCellValue(0,13))
			KC = float(self.m_grid9.GetCellValue(0,14))
			XL = float(self.m_grid9.GetCellValue(0,15))
			THETAP = float(self.m_grid9.GetCellValue(0,16))

			if TR<0 or TR >0.5:
				self.m_grid9.SetCellTextColour(0,0, wx.RED)
			if KPR<0 or KPR >75:
				self.m_grid9.SetCellTextColour(0,1, wx.RED)
			if KIR<0 or KIR >75:
				self.m_grid9.SetCellTextColour(0,2, wx.RED)
			if VRMAX<0.8 or VRMAX>10:
				self.m_grid9.SetCellTextColour(0,3, wx.RED)
			if VRMIN<-6 or VRMIN>0:
				self.m_grid9.SetCellTextColour(0,4, wx.RED)
			if TA<0 or TA >=1:
				self.m_grid9.SetCellTextColour(0,5, wx.RED)
			if KPM<0 or KPM >1.2:
				self.m_grid9.SetCellTextColour(0,6, wx.RED)
			if KIM<0 or KIM >18:
				self.m_grid9.SetCellTextColour(0,7, wx.RED)
			if VMMAX<0.8 or VMMAX >118:
				self.m_grid9.SetCellTextColour(0,8, wx.RED)
			if VMMIN<-118.8 or VMMIN >0:
				self.m_grid9.SetCellTextColour(0,9, wx.RED)
			if KG<0 or KG>=1.1:
				self.m_grid9.SetCellTextColour(0,10, wx.RED)
			if KP<1 or KP>=10:
				self.m_grid9.SetCellTextColour(0,11, wx.RED)
			if KI<0 or KI >1.1:
				self.m_grid9.SetCellTextColour(0,12, wx.RED)
			if VBMAX<=1 or VBMAX >=20:
				self.m_grid9.SetCellTextColour(0,13, wx.RED)
			if KC<0 or KC >=1:
				self.m_grid9.SetCellTextColour(0,14, wx.RED)
			if XL<0 or XL >=0.5:
				self.m_grid9.SetCellTextColour(0,15, wx.RED)
			if THETAP<=-90 or THETAP >=90:
				self.m_grid9.SetCellTextColour(0,16, wx.RED)

		elif model == 'EXAC4':
			# labelEXAC4 = ['','','',"TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
			TR = float(self.m_grid9.GetCellValue(0,0))
			VIMAX = float(self.m_grid9.GetCellValue(0,1))
			VIMIN = float(self.m_grid9.GetCellValue(0,2))
			TC = float(self.m_grid9.GetCellValue(0,3))
			TB = float(self.m_grid9.GetCellValue(0,4))
			KA = float(self.m_grid9.GetCellValue(0,5))
			TA = float(self.m_grid9.GetCellValue(0,6))
			VRMAX = float(self.m_grid9.GetCellValue(0,7))
			VRMIN = float(self.m_grid9.GetCellValue(0,8))
			KC = float(self.m_grid9.GetCellValue(0,9))

			if TR<0 or TR >0.1:
				self.m_grid9.SetCellTextColour(0,0, wx.RED)
			if VIMAX<=0 or VIMAX >0.2:
				self.m_grid9.SetCellTextColour(0,1, wx.RED)
			if VIMIN<=-0.2 or VIMIN >0:
				self.m_grid9.SetCellTextColour(0,2, wx.RED)
			if TC<0 or TC >=10:
				self.m_grid9.SetCellTextColour(0,3, wx.RED)
			if TB<=0.04 or TB >=20:
				self.m_grid9.SetCellTextColour(0,4, wx.RED)
			if KA<=50 or KA >1000:
				self.m_grid9.SetCellTextColour(0,5, wx.RED)
			if TA<0 or TA >=0.5:
				self.m_grid9.SetCellTextColour(0,6, wx.RED)
			if VRMAX<3 or VRMAX >8:
				self.m_grid9.SetCellTextColour(0,7, wx.RED)
			if VRMIN<-8 or VRMIN >-3:
				self.m_grid9.SetCellTextColour(0,8, wx.RED)
			if KC<0 or KC >0.3:
				self.m_grid9.SetCellTextColour(0,9, wx.RED)

	# Thiết lập điều kiện ràng buộc để bôi đỏ những giá trị nằm ngoài vùng giới hạn của model 3
	def set_restriction_model3(self,model=''):
		# GOV
		if model == 'TGOV1':
		# labelTGOV1 = ['','','','R','T1','VMAX','VMIN','T2','T3','Dt']
			R = float(self.m_grid10.GetCellValue(0,0))
			T1 = float(self.m_grid10.GetCellValue(0,1))
			VMAX = float(self.m_grid10.GetCellValue(0,2))
			VMIN = float(self.m_grid10.GetCellValue(0,3))
			T2 = float(self.m_grid10.GetCellValue(0,4))
			T3 = float(self.m_grid10.GetCellValue(0,5))
			Dt = float(self.m_grid10.GetCellValue(0,6))
			
			if R<=0 or R >=0.1:
				self.m_grid10.SetCellTextColour(0,0, wx.RED)
			if T1<=0.04 or T1>=0.5:
				self.m_grid10.SetCellTextColour(0,1, wx.RED)
			if VMAX<=0.5 or VMAX >=1.2 or VMAX <= VMIN:
				self.m_grid10.SetCellTextColour(0,2, wx.RED)
			if VMIN<0 or VMIN >=1.0 or VMIN>=VMAX:
				self.m_grid10.SetCellTextColour(0,3, wx.RED)
			if T2<=0 or T3<2*T2:
				self.m_grid10.SetCellTextColour(0,4, wx.RED)
			if T3<=0.04 or T3 >=10.0 or T3<2*T2:
				self.m_grid10.SetCellTextColour(0,5, wx.RED)
			if Dt<0 or Dt >=0.5:
				self.m_grid10.SetCellTextColour(0,6, wx.RED)

		elif model == 'HYGOV':
		# labelHYGOV = ['','','',"R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
			R = float(self.m_grid10.GetCellValue(0,0))
			r = float(self.m_grid10.GetCellValue(0,1))
			Tr = float(self.m_grid10.GetCellValue(0,2))
			Tf = float(self.m_grid10.GetCellValue(0,3))
			Tg = float(self.m_grid10.GetCellValue(0,4))
			VELM = float(self.m_grid10.GetCellValue(0,5))
			GMAX = float(self.m_grid10.GetCellValue(0,6))
			GMIN = float(self.m_grid10.GetCellValue(0,7))
			TW = float(self.m_grid10.GetCellValue(0,8))
			At = float(self.m_grid10.GetCellValue(0,9))
			Dturb = float(self.m_grid10.GetCellValue(0,10))
			qNL = float(self.m_grid10.GetCellValue(0,11))

			if R<=0 or R >=0.1 or R>r:
				self.m_grid10.SetCellTextColour(0,0, wx.RED)
			if r<=0 or r>=2 or r<R:
				self.m_grid10.SetCellTextColour(0,1, wx.RED)
			if Tr<=0.04 or Tr >=30:
				self.m_grid10.SetCellTextColour(0,2, wx.RED)
			if Tf<=0.04 or Tf >=0.1:
				self.m_grid10.SetCellTextColour(0,3, wx.RED)
			if Tg<=0.04 or Tg >=1.0:
				self.m_grid10.SetCellTextColour(0,4, wx.RED)
			if VELM<=0 or VELM >=0.3:
				self.m_grid10.SetCellTextColour(0,5, wx.RED)
			if GMAX<=0 or GMAX >1 or GMAX<=GMIN:
				self.m_grid10.SetCellTextColour(0,6, wx.RED)
			if GMIN<=0 or GMIN >1 or GMAX<=GMIN:
				self.m_grid10.SetCellTextColour(0,7, wx.RED)
			if TW<=0.5 or TW >=3.0:
				self.m_grid10.SetCellTextColour(0,8, wx.RED)
			if At<=0.8 or At >=1.5:
				self.m_grid10.SetCellTextColour(0,9, wx.RED)
			if Dturb<0 or Dturb >=0.5 :
				self.m_grid10.SetCellTextColour(0,10, wx.RED)
			if qNL<=0 or qNL>0.15:
				self.m_grid10.SetCellTextColour(0,11, wx.RED)

		elif model == 'GAST':
		# labelGAST = ['','','',"R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
			R = float(self.m_grid10.GetCellValue(0,0))
			T1 = float(self.m_grid10.GetCellValue(0,1))
			T2 = float(self.m_grid10.GetCellValue(0,2))
			T3 = float(self.m_grid10.GetCellValue(0,3))
			AT = float(self.m_grid10.GetCellValue(0,4))
			KT = float(self.m_grid10.GetCellValue(0,5))
			VMAX = float(self.m_grid10.GetCellValue(0,6))
			VMIN = float(self.m_grid10.GetCellValue(0,7))
			Dturb = float(self.m_grid10.GetCellValue(0,8))

			if R<=0 or R >=0.1:
				self.m_grid10.SetCellTextColour(0,0, wx.RED)
			if T1<=0.04 or T1 >=0.5:
				self.m_grid10.SetCellTextColour(0,1, wx.RED)
			if T2<=0.04 or T2 >=0.5:
				self.m_grid10.SetCellTextColour(0,2, wx.RED)
			if T3<=0.04 or T3 >=5.0:
				self.m_grid10.SetCellTextColour(0,3, wx.RED)
			if AT<=0 or AT >1:
				self.m_grid10.SetCellTextColour(0,4, wx.RED)
			if AT<=0 or AT >=5.0:
				self.m_grid10.SetCellTextColour(0,5, wx.RED)
			if VMAX<=0.5 or VMAX >=1.2 or VMAX<=VMIN:
				self.m_grid10.SetCellTextColour(0,6, wx.RED)
			if VMIN<0 or VMIN >=1.0 or VMAX<=VMIN:
				self.m_grid10.SetCellTextColour(0,7, wx.RED)
			if Dturb<0 or Dturb >=0.5 :
				self.m_grid10.SetCellTextColour(0,8, wx.RED)

	# Thiết lập điều kiện ràng buộc để bôi đỏ những giá trị nằm ngoài vùng giới hạn của model 4
	def set_restriction_model4(self,model=''):
		# GOV
		if model == 'PSS2A':
			# labelPSS2A = ['IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
			T1 = float(self.m_grid11.GetCellValue(0,17))
			T2 = float(self.m_grid11.GetCellValue(0,18))
			T3 = float(self.m_grid11.GetCellValue(0,19))
			T4 = float(self.m_grid11.GetCellValue(0,20))
			T6 = float(self.m_grid11.GetCellValue(0,8))
			T7 = float(self.m_grid11.GetCellValue(0,11))
			T8 = float(self.m_grid11.GetCellValue(0,14))
			T9 = float(self.m_grid11.GetCellValue(0,15))
			TW1 = float(self.m_grid11.GetCellValue(0,6))
			TW2 = float(self.m_grid11.GetCellValue(0,7))
			TW3 = float(self.m_grid11.GetCellValue(0,9))
			TW4 = float(self.m_grid11.GetCellValue(0,10))
			VSTMAX = float(self.m_grid11.GetCellValue(0,21))
			VATMIN = float(self.m_grid11.GetCellValue(0,22))

			if TW1<1.5 or TW1 > 15:
				self.m_grid11.SetCellTextColour(0,6, wx.RED)
			if TW2<1.5 or TW2 > 15:
				self.m_grid11.SetCellTextColour(0,7, wx.RED)
			if TW3<1.5 or TW3 > 15:
				self.m_grid11.SetCellTextColour(0,9, wx.RED)
			if TW4<1.5 or TW4 > 15:
				self.m_grid11.SetCellTextColour(0,10, wx.RED)
			if T1<0.02 or T1 > 2.0:
				self.m_grid11.SetCellTextColour(0,17, wx.RED)
			if T3<0.02 or T3 > 2.0:
				self.m_grid11.SetCellTextColour(0,19, wx.RED)
			if T2<0.02 or T2 > 6.0:
				self.m_grid11.SetCellTextColour(0,18, wx.RED)
			if T4<0.02 or T4 > 6.0:
				self.m_grid11.SetCellTextColour(0,20, wx.RED)
			if T6<=0.02:
				self.m_grid11.SetCellTextColour(0,8, wx.RED)
			if T7<=0.02:
				self.m_grid11.SetCellTextColour(0,11, wx.RED)
			if T8<=0.02 or T8 > 2.0:
				self.m_grid11.SetCellTextColour(0,14, wx.RED)
			if VSTMAX<=0 or VSTMAX>=0.99:
				self.m_grid11.SetCellTextColour(0,21, wx.RED)
			if VATMIN<-0.3 or VATMIN> 0:
				self.m_grid11.SetCellTextColour(0,22, wx.RED)

	# chức năng thực hiện khi có sự chuyển đổi ô làm việc trong dòng thông tin của model 1
	def on_cell_change_model1(self,event):
		TypeModel1 = str(self.comboBoxModel1.GetValue())
		for i in range(self.m_grid7.GetNumberCols()):
			self.m_grid7.SetCellTextColour(0,i,wx.Colour(0,0,0))
		if TypeModel1 == 'GENROU':
			self.set_restriction_model1('GENROU')
		elif TypeModel1 == 'GENSAL':
			self.set_restriction_model1('GENSAL')
		elif TypeModel1 == 'PVGU1':
			self.set_restriction_model1('PVGU1')
		elif TypeModel1 == 'GEWTGCU1':
			self.set_restriction_model1('GEWTGCU1')
		event.Skip()

	# chức năng thực hiện khi có sự chuyển đổi ô làm việc trong dòng thông tin của model 2
	def on_cell_change_model2(self,event):
		TypeModel2 = str(self.comboBoxModel2.GetValue())
		for i in range(self.m_grid9.GetNumberCols()):
			self.m_grid9.SetCellTextColour(0,i,wx.Colour(0,0,0))
		if TypeModel2 == 'EXAC4':
			self.set_restriction_model1('EXAC4')
		elif TypeModel2 == 'ESST4B':
			self.set_restriction_model1('ESST4B')
		elif TypeModel2 == 'PVEU1':
			self.set_restriction_model1('PVEU1')
		elif TypeModel2 == 'GEWTECU1':
			self.set_restriction_model1('GEWTECU1')
		event.Skip()

	# chức năng thực hiện khi có sự chuyển đổi ô làm việc trong dòng thông tin của model 3
	def on_cell_change_model3(self,event):
		TypeModel3 = str(self.comboBoxModel3.GetValue())
		for i in range(self.m_grid10.GetNumberCols()):
			self.m_grid10.SetCellTextColour(0,i,wx.Colour(0,0,0))
		if TypeModel3 == 'TGOV1':
			self.set_restriction_model1('TGOV1')
		elif TypeModel3 == 'HYGOV':
			self.set_restriction_model1('HYGOV')
		elif TypeModel3 == 'GAST':
			self.set_restriction_model1('GAST')
		elif TypeModel3 == 'PANELU1':
			self.set_restriction_model1('PANELU1')
		elif TypeModel3 == 'GEWT2MU1':
			self.set_restriction_model1('GEWT2MU1')
		event.Skip()

	# chức năng thực hiện khi có sự chuyển đổi ô làm việc trong dòng thông tin của model 4
	def on_cell_change_model4(self,event):
		TypeModel4 = str(self.comboBoxModel4.GetValue())
		for i in range(self.m_grid11.GetNumberCols()):
			self.m_grid11.SetCellTextColour(0,i,wx.Colour(0,0,0))
		if TypeModel4 == 'PSS2A':
			self.set_restriction_model1('TGOV1')
		elif TypeModel4 == 'IRRADU1':
			self.set_restriction_model1('IRRADU1')
		elif TypeModel4 == 'GEWTPTU1':
			self.set_restriction_model1('GEWTPTU1')

	def on_cell_change_model5(self,event):
		event.Skip()
	
	def on_cell_change_model6(self,event):
		event.Skip()

	def on_selected_cell_model1(self,event):
		event.Skip()

	def on_selected_cell_model2(self,event):
		event.Skip()

	def on_selected_cell_model3(self,event):
		event.Skip()

	def on_selected_cell_model4(self,event):
		event.Skip()

	def on_selected_cell_model5(self,event):
		event.Skip()

	def on_selected_cell_model6(self,event):
		event.Skip()
