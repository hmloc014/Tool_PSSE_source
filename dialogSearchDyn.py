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

###########################################################################
## Class MyDialog2
###########################################################################

class SearchDyn ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1300,-1 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.gridDynSearch = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridDynSearch.CreateGrid( 15, 100 )
		self.gridDynSearch.EnableEditing( True )
		self.gridDynSearch.EnableGridLines( True )
		self.gridDynSearch.EnableDragGridSize( False )
		self.gridDynSearch.SetMargins( 0, 0 )
		
		# Columns
		self.gridDynSearch.EnableDragColMove( False )
		self.gridDynSearch.EnableDragColSize( True )
		self.gridDynSearch.SetColLabelSize( 30 )
		self.gridDynSearch.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridDynSearch.EnableDragRowSize( True )
		self.gridDynSearch.SetRowLabelSize( 80 )
		self.gridDynSearch.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gridDynSearch.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		attr = wx.grid.GridCellAttr()
		attr.SetBackgroundColour(wx.Colour(255,255,185))
		for i in range(12):
			if i%2==0:
				self.gridDynSearch.SetRowAttr(i, attr)

		bSizer30.Add( self.gridDynSearch, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		
		self.CentreOnParent( wx.BOTH )
	
	def __del__( self ):
		pass
	

