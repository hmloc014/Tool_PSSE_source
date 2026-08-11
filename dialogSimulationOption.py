# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyDialog2
###########################################################################

class Simulation_option ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Set Relative Machine Angles", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"Relative to machine", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Gen Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.Enable( False )
		gSizer6.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		comboBox_GenNumChoices = []
		self.comboBox_GenNum = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBox_GenNumChoices, 0 )
		self.comboBox_GenNum.Enable( False )
		gSizer6.Add( self.comboBox_GenNum, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer28.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"Relative to system average angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.SetValue( True )
		bSizer29.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"Relative to system weighted average angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_radioBtn5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnSelect = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.btnSelect, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer29.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer28.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer28 )
		self.Layout()
		bSizer28.Fit( self )
		
		self.CentreOnParent( wx.BOTH )
		self.flag = 0
		self.choose = 0
		
		# Connect Events
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.choice1 )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.choice2 )
		self.m_radioBtn5.Bind( wx.EVT_RADIOBUTTON, self.choice3 )
		self.btnSelect.Bind( wx.EVT_BUTTON, self.Next )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	# Set relative machine angle relative to machine
	def choice1( self, event ):
		self.choose = 1
		self.m_staticText13.Enable( True )
		# self.m_staticText14.Enable( True )
		self.comboBox_GenNum.Enable( True )
		# self.comboBox_Id.Enable( True )
		event.Skip()
	
	# Set relative machine angle relative to system average angle
	def choice2( self, event ):
		self.choose = 2
		self.m_staticText13.Enable( False )
		# self.m_staticText14.Enable( False  )
		self.comboBox_GenNum.Enable( False )
		# self.comboBox_Id.Enable( False  )
		event.Skip()
	
	# Set relative machine angle relative to system weighted average angle
	def choice3( self, event ):
		self.choose = 3
		self.m_staticText13.Enable( False )
		# self.m_staticText14.Enable( False  )
		self.comboBox_GenNum.Enable( False )
		# self.comboBox_Id.Enable( False  )
		event.Skip()
	
	def onClose( self, event ):
		event.Skip()
		return self.flag
	
	def Next( self, event ):
		if self.choose == 1 and self.comboBox_GenNum.GetValue() == '':
			wx.MessageBox('Gen number cannot null!')
		else:
			self.flag = 1
			self.Close()
			event.Skip()
			return self.choose

