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
## Class line tab
###########################################################################

class Line_Tab ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Line Tab", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"From bus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.fromBusChoices = []
		self.fromBus = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.fromBusChoices )
		self.fromBus.SetSelection( 0 )
		gSizer6.Add( self.fromBus, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Middle Bus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer6.Add( self.m_staticText32, 0, wx.ALL, 10 )
		
		self.middleChoices = []
		self.Middle = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.middleChoices )
		self.Middle.SetSelection( 0 )
		gSizer6.Add( self.Middle, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gSizer6.Add( self.m_staticText35, 0, wx.ALL, 10 )
		
		self.textCtrl_ID1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_ID1, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"To Bus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		self.toBusChoices = []
		self.toBus = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.toBusChoices )
		self.toBus.SetSelection( 0 )
		gSizer6.Add( self.toBus, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer6.Add( self.m_staticText36, 0, wx.ALL, 10 )
		
		self.textCtrl_ID2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_ID2, 0, wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Segments number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer6.Add( self.m_staticText34, 0, wx.ALL, 10 )
		
		self.textCtrl_Number = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		gSizer6.Add( self.textCtrl_Number, 0, wx.ALL, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnNext = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnNext, 0, wx.ALL, 5 )
		
		
		gSizer6.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer6 )
		self.Layout()
		gSizer6.Fit( self )
		
		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.fromBus.Bind( wx.EVT_TEXT, self.onSelectFromBus )
		self.Middle.Bind( wx.EVT_TEXT, self.onSelectMiddle )
		self.toBus.Bind( wx.EVT_TEXT, self.onSelectToBus )
		self.textCtrl_ID1.Bind( wx.EVT_TEXT, self.onTextID1 )
		self.textCtrl_ID2.Bind( wx.EVT_TEXT, self.onTextID2 )
		self.textCtrl_Number.Bind( wx.EVT_TEXT, self.onTextNumber )
		self.btnNext.Bind( wx.EVT_BUTTON, self.Next )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectFromBus( self, event ):
		event.Skip()

	def onSelectMiddle( self, event ):
		event.Skip()

	def onTextID1( self,event):
		event.Skip()
	
	def onSelectToBus( self, event ):
		event.Skip()

	def onTextID2( self,event):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag

	def onTextNumber( self,event):
		event.Skip()
	
	# lấy thông tin frombus, middle bus, tobus, id, số đoạn chia và trả về mảng chứa thông tin tương ứng
	def Next( self, event ):
		self.flag = 1
		fromBus = str(self.fromBus.GetValue()).split('-')[0]
		middle = str(self.Middle.GetValue()).split('-')[0]
		id1 = str(self.textCtrl_ID1.GetValue())
		toBus = str(self.toBus.GetValue()).split('-')[0]
		id2 = str(self.textCtrl_ID2.GetValue())
		segments = str(self.textCtrl_Number.GetValue())

		if str(fromBus) != '' and str(toBus) != '' and  str(segments) != '' and str(id1) =='' and str(id2) != '' and str(middle)=='':
			# print('line tab 2 point')
			tabLinetype = 2
			self.Close()
			return [int(fromBus),str(middle),id1,int(toBus),id2,int(segments),tabLinetype]
		elif str(fromBus) != '' and str(toBus) != '' and  str(segments) != '' and str(middle)!='' and str(id1) !='' and str(id2) != '':
			# print('line tab 3 point')
			tabLinetype = 3
			self.Close()
			return [int(fromBus),int(middle),id1,int(toBus),id2,int(segments),tabLinetype]
		else:
			event.Skip()
