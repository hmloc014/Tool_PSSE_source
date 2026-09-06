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
## Class Add_New_Load
###########################################################################

class Select_Source_Sink ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Choose Sink/Source", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Source", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer6.Add( self.m_staticText30, 0, wx.ALL, 10 )
		
		self.sourceChoices = []
		self.Source = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.sourceChoices )
		self.Source.SetSelection( 0 )
		gSizer6.Add( self.Source, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Sink", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer6.Add( self.m_staticText31, 0, wx.ALL, 10 )
		
		self.sinkChoices = []
		self.Sink = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), self.sinkChoices )
		self.Sink.SetSelection( 0 )
		gSizer6.Add( self.Sink, 0, wx.ALL, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )
	
		gSizer6.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnSelect = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer35.Add( self.btnSelect, 0, wx.ALL, 5 )
		
		
		gSizer6.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer6 )
		self.Layout()
		gSizer6.Fit( self )
		
		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.Source.Bind( wx.EVT_TEXT, self.onSelectSource )
		self.Sink.Bind( wx.EVT_TEXT, self.onSelectSink )
		self.btnSelect.Bind( wx.EVT_BUTTON, self.SelectSinkSource )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectSource( self, event ):
		event.Skip()
	
	def onSelectSink( self, event ):
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag
	
	# chọn sink, source
	def SelectSinkSource( self, event ):
		self.flag = 1
		source = str(self.Source.GetValue())
		sink = str(self.Sink.GetValue())

		if sink != '' and source != '':
			
			self.Close()
			return [source,sink]
		else:
			event.Skip()
