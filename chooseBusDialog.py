# -*- coding: utf-8 -*- 

###########################################################################
## Python code Loaderated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Choose_Bus
###########################################################################

class Choose_Bus ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,393 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		self.BusPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lbBusChoices = []
		self.lbBus = wx.ListBox( self.BusPage,size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= self.lbBusChoices )
		gSizer22.Add( self.lbBus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		lb2BusChoices = []
		self.lb2Bus = wx.ListBox( self.BusPage, size=wx.DefaultSize, style=wx.LB_EXTENDED, choices=lb2BusChoices )
		gSizer22.Add( self.lb2Bus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer152.Add( gSizer22, 2, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.textCtrl_Search = wx.TextCtrl( self.BusPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		bSizer27.Add( self.textCtrl_Search, 0, wx.ALL, 5 )
		bSizer152.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		
		gSizer32 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.oneaddBus = wx.Button( self.BusPage, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.oneaddBus, 0, wx.ALL, 5 )
		
		self.multiaddBus = wx.Button( self.BusPage, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.multiaddBus, 0, wx.ALL, 5 )
		
		self.oneMoveBus = wx.Button( self.BusPage, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.oneMoveBus, 0, wx.ALL, 5 )
		
		self.multiMoveBus = wx.Button( self.BusPage, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.multiMoveBus, 0, wx.ALL, 5 )
		
		bSizer162 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer32.Add( bSizer162, 1, wx.EXPAND, 5 )
		
		bSizer172 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer32.Add( bSizer172, 1, wx.EXPAND, 5 )
		
		bSizer182 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer32.Add( bSizer182, 1, wx.EXPAND, 5 )
		
		self.busBtn = wx.Button( self.BusPage, wx.ID_ANY, u"Calculation", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.busBtn, 0, wx.ALL, 5 )
		
		
		bSizer152.Add( gSizer32,1, wx.EXPAND, 5 )
		
		
		self.BusPage.SetSizer( bSizer152 )
		self.BusPage.Layout()
		bSizer152.Fit( self.BusPage )
		self.m_notebook2.AddPage( self.BusPage, u"Bus", False )
		
		bSizer14.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()

		self.flag = 0
		self.selectedBus = []

		self.CentreOnParent( wx.BOTH )
		
		# Connect Events
		self.lbBus.Bind( wx.EVT_LISTBOX, self.onSelectBus )
		self.lb2Bus.Bind( wx.EVT_LISTBOX, self.onSelectToMoveBus )
		self.oneaddBus.Bind( wx.EVT_BUTTON, self.oneAddBus_Fcn )
		self.multiaddBus.Bind( wx.EVT_BUTTON, self.multipleAddBus_Fcn )
		self.oneMoveBus.Bind( wx.EVT_BUTTON, self.oneMoveBus_Fcn )
		self.multiMoveBus.Bind( wx.EVT_BUTTON, self.multiMoveBus_Fcn )
		self.textCtrl_Search.Bind( wx.EVT_TEXT, self.onText_Search )
		self.busBtn.Bind( wx.EVT_BUTTON, self.Calculation )

	def __del__( self ):
		pass

	def onClose( self, event ):
		event.Skip()
		return self.flag

	def Calculation( self, event ):

		self.flag = 0
		busList  = self.lb2Bus.Items

		busNum = []

		for i in range(len(busList)):
			obj = busList[i].split('-')
			busNum.append(int(obj[0]))

		if len(busNum) != 0:
			self.flag = 1 
			self.Close()
			return busNum
		else:
			event.Skip()

	# chọn phần tử trong cột danh sách bus (bên trái của dialog)
	def onSelectBus(self, event):
		global busNum
		busNum = self.lbBus.GetSelections()
		for i in range(len(busNum)):
			obj = self.lbBus.GetString(busNum[i])

	# chọn phần tử trong cột danh sách bus cần quan sát (bên phải của dialog)
	def onSelectToMoveBus(self, event):
		global moveBus
		moveBus = self.lb2Bus.GetSelections()
		for i in range(len(moveBus)):
			obj = self.lb2Bus.GetString(moveBus[i])

	# thêm 1 phần tử vào cột danh sách bus cần quan sát
	def oneAddBus_Fcn(self,event):
		for i in range(len(busNum)):
			obj = self.lbBus.GetString(busNum[i])
			if not obj in self.lb2Bus.Items:
				self.selectedBus.append(obj)
				self.lb2Bus.Append(obj)
	
	# thêm nhiều phần tử vào cột danh sách bus cần quan sát
	def multipleAddBus_Fcn(self,event):
		b  = self.lbBus.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2Bus.Items:
				self.lb2Bus.Append(obj)
	
	# di chuyển 1 phần tử ra khỏi cột danh sách bus cần quan sát
	def oneMoveBus_Fcn(self,event):
		for i in range(len(moveBus)):
			obj = self.lb2Bus.GetString(len(moveBus)-1-i)
			self.lb2Bus.Delete(moveBus[len(moveBus)-1-i])

	# di chuyển nhiều phần tử ra khỏi cột danh sách bus cần quan sát
	def multiMoveBus_Fcn(self,event):
		b  = self.lb2Bus.Items
		for i in range(len(b)):
			obj = self.lbBus.GetString(i)
			self.lb2Bus.Delete(len(b)-1-i)
	
	# lấy nội dung trong ô tìm kiếm
	def onText_Search(self,event):
		searchText = self.textCtrl_Search.GetValue()
		items = self.lbBusChoices
		result = []   
		for i in range(len(items)):
			if ((str(searchText)).upper() in (str(items[i]).upper())):
				result.append(items[i])
		self.lbBus.SetItems(result)
		event.Skip()
