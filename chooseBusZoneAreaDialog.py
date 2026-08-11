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
## Class Choose_Bus_Zone_Area
###########################################################################

class Choose_Bus_Zone_Area ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,393 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AreaPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lbAreaChoices = []
		self.lbArea = wx.ListBox( self.AreaPage, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= self.lbAreaChoices )
		gSizer2.Add( self.lbArea, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		lb2AreaChoices = []
		self.lb2Area = wx.ListBox( self.AreaPage,size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=lb2AreaChoices)
		gSizer2.Add( self.lb2Area, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer15.Add( gSizer2, 2, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.textCtrl_SearchArea = wx.TextCtrl( self.AreaPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		bSizer27.Add( self.textCtrl_SearchArea, 0, wx.ALL, 5 )
		bSizer15.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.oneaddArea = wx.Button( self.AreaPage, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.oneaddArea, 0, wx.ALL, 5 )
		
		self.multiaddArea = wx.Button( self.AreaPage, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.multiaddArea, 0, wx.ALL, 5 )
		
		self.oneMoveArea = wx.Button( self.AreaPage, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.oneMoveArea, 0, wx.ALL, 5 )
		
		self.multiMoveArea = wx.Button( self.AreaPage, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.multiMoveArea, 0, wx.ALL, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer3.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		self.areaBtn = wx.Button( self.AreaPage, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.areaBtn, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		self.AreaPage.SetSizer( bSizer15 )
		self.AreaPage.Layout()
		bSizer15.Fit( self.AreaPage )
		self.m_notebook2.AddPage( self.AreaPage, u"Area", True )
		self.ZonePage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lbZoneChoices = []
		self.lbZone = wx.ListBox( self.ZonePage,size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= self.lbZoneChoices )
		gSizer21.Add( self.lbZone, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		lb2ZoneChoices = []
		self.lb2Zone = wx.ListBox( self.ZonePage,size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=lb2ZoneChoices )
		gSizer21.Add( self.lb2Zone, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer151.Add( gSizer21, 2, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.textCtrl_SearchZone = wx.TextCtrl( self.ZonePage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		bSizer28.Add( self.textCtrl_SearchZone, 0, wx.ALL, 5 )
		bSizer151.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		gSizer31 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.oneaddZone = wx.Button( self.ZonePage, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.oneaddZone, 0, wx.ALL, 5 )
		
		self.multiaddZone = wx.Button( self.ZonePage, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.multiaddZone, 0, wx.ALL, 5 )
		
		self.oneMoveZone = wx.Button( self.ZonePage, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.oneMoveZone, 0, wx.ALL, 5 )
		
		self.multiMoveZone = wx.Button( self.ZonePage, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.multiMoveZone, 0, wx.ALL, 5 )
		
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer31.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer171 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer31.Add( bSizer171, 1, wx.EXPAND, 5 )
		
		bSizer181 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer31.Add( bSizer181, 1, wx.EXPAND, 5 )
		
		self.zoneBtn = wx.Button( self.ZonePage, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.zoneBtn, 0, wx.ALL, 5 )
		
		
		bSizer151.Add( gSizer31, 1, wx.EXPAND, 5 )
		
		
		self.ZonePage.SetSizer( bSizer151 )
		self.ZonePage.Layout()
		bSizer151.Fit( self.ZonePage )
		self.m_notebook2.AddPage( self.ZonePage, u"Zone", False )
		self.BusPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lbBusChoices = []
		self.lbBus = wx.ListBox( self.BusPage, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= self.lbBusChoices )
		gSizer22.Add( self.lbBus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		lb2BusChoices = []
		self.lb2Bus = wx.ListBox( self.BusPage,size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= lb2BusChoices )
		gSizer22.Add( self.lb2Bus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer152.Add( gSizer22, 2, wx.EXPAND, 5 )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.textCtrl_SearchBus = wx.TextCtrl( self.BusPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		bSizer29.Add( self.textCtrl_SearchBus, 0, wx.ALL, 5 )
		bSizer152.Add( bSizer29, 1, wx.EXPAND, 5 )

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
		
		
		bSizer152.Add( gSizer32, 1, wx.EXPAND, 5 )
		
		
		self.BusPage.SetSizer( bSizer152 )
		self.BusPage.Layout()
		bSizer152.Fit( self.BusPage )
		self.m_notebook2.AddPage( self.BusPage, u"Bus", False )
		
		bSizer14.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()

		self.flag = 0
		self.selectedArea = []
		self.selectedZone = []
		self.selectedBus = []

		self.CentreOnParent( wx.BOTH )
		
		# Connect Events
		self.lbArea.Bind( wx.EVT_LISTBOX, self.onSelectArea )
		self.lb2Area.Bind( wx.EVT_LISTBOX, self.onSelectToMoveArea )
		self.textCtrl_SearchArea.Bind( wx.EVT_TEXT, self.onText_SearchArea )
		self.oneaddArea.Bind( wx.EVT_BUTTON, self.oneAddArea_Fcn )
		self.multiaddArea.Bind( wx.EVT_BUTTON, self.multipleAddArea_Fcn )
		self.oneMoveArea.Bind( wx.EVT_BUTTON, self.oneMoveArea_Fcn )
		self.multiMoveArea.Bind( wx.EVT_BUTTON, self.multiMoveArea_Fcn )
		self.areaBtn.Bind( wx.EVT_BUTTON, self.goToZonePage )

		self.lbZone.Bind( wx.EVT_LISTBOX, self.onSelectZone )
		self.lb2Zone.Bind( wx.EVT_LISTBOX, self.onSelectToMoveZone )
		self.textCtrl_SearchZone.Bind( wx.EVT_TEXT, self.onText_SearchZone )
		self.oneaddZone.Bind( wx.EVT_BUTTON, self.oneAddZone_Fcn )
		self.multiaddZone.Bind( wx.EVT_BUTTON, self.multipleAddZone_Fcn )
		self.oneMoveZone.Bind( wx.EVT_BUTTON, self.oneMoveZone_Fcn )
		self.multiMoveZone.Bind( wx.EVT_BUTTON, self.multiMoveZone_Fcn )
		self.zoneBtn.Bind( wx.EVT_BUTTON, self.goToBusPage )

		self.lbBus.Bind( wx.EVT_LISTBOX, self.onSelectBus )
		self.lb2Bus.Bind( wx.EVT_LISTBOX, self.onSelectToMoveBus )
		self.textCtrl_SearchBus.Bind( wx.EVT_TEXT, self.onText_SearchBus )
		self.oneaddBus.Bind( wx.EVT_BUTTON, self.oneAddBus_Fcn )
		self.multiaddBus.Bind( wx.EVT_BUTTON, self.multipleAddBus_Fcn )
		self.oneMoveBus.Bind( wx.EVT_BUTTON, self.oneMoveBus_Fcn )
		self.multiMoveBus.Bind( wx.EVT_BUTTON, self.multiMoveBus_Fcn )
		self.busBtn.Bind( wx.EVT_BUTTON, self.ContigencyCalculation )

	def __del__( self ):
		pass

	def onClose( self, event ):
		event.Skip()
		return self.flag

	def goToZonePage( self, event ):
		self.m_notebook2.SetSelection(1)
		event.Skip()

	def goToBusPage( self, event ):
		self.m_notebook2.SetSelection(2)
		event.Skip()	

	# trả về danh sách các area, zone và bus cần quan sát
	def ContigencyCalculation( self, event ):

		self.flag = 0
		areaList  = self.lb2Area.Items
		zoneList  = self.lb2Zone.Items
		busList  = self.lb2Bus.Items
		areaNum = []
		zoneNum = []
		busNum = []
		for i in range(len(areaList)):
			obj = areaList[i].split('-')
			areaNum.append(int(obj[0]))
		for i in range(len(zoneList)):
			obj = zoneList[i].split('-')
			zoneNum.append(int(obj[0]))
		for i in range(len(busList)):
			obj = busList[i].split('-')
			busNum.append(int(obj[0]))

		if len(areaNum)*len(zoneNum)*len(busNum) != 0:
			self.flag = 1 
			self.Close()
			return [areaNum,zoneNum,busNum]
		else:
			event.Skip()

	# chọn area bên phía trái dialog (cột origin)
	def onSelectArea(self, event):
		global areaNum
		areaNum = self.lbArea.GetSelections()
		for i in range(len(areaNum)):
			obj = self.lbArea.GetString(areaNum[i])

	# chọn area bên phía phải dialog (cột lựa chọn)
	def onSelectToMoveArea(self, event):
		global moveArea
		moveArea = self.lb2Area.GetSelections()
		for i in range(len(moveArea)):
			obj = self.lb2Area.GetString(moveArea[i])
	
	# Thêm 1 area vào phía cần quan sát
	def oneAddArea_Fcn(self,event):
		for i in range(len(areaNum)):
			obj = self.lbArea.GetString(areaNum[i])
			if not obj in self.lb2Area.Items:
				self.selectedArea.append(obj)
				self.lb2Area.Append(obj)
	
	# Thêm nhiều area vào phía cần quan sát
	def multipleAddArea_Fcn(self,event):
		b  = self.lbArea.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2Area.Items:
				self.lb2Area.Append(obj)
	
	# bỏ bớt 1 area ra khỏi cột cần quan sát
	def oneMoveArea_Fcn(self,event):
		for i in range(len(moveArea)):
			obj = self.lb2Area.GetString(len(moveArea)-1-i)
			self.lb2Area.Delete(moveArea[len(moveArea)-1-i])

	# bỏ bớt nhiều area ra khỏi cột cần quan sát
	def multiMoveArea_Fcn(self,event):
		b  = self.lb2Area.Items
		for i in range(len(b)):
			obj = self.lbArea.GetString(i)
			self.lb2Area.Delete(len(b)-1-i)

	# chọn zone bên phía trái dialog (cột origin)
	def onSelectZone(self, event):
		global zoneNum
		zoneNum = self.lbZone.GetSelections()
		for i in range(len(zoneNum)):
			obj = self.lbZone.GetString(zoneNum[i])

	# chọn zone bên phía phải dialog (cột lựa chọn)
	def onSelectToMoveZone(self, event):
		global moveZone
		moveZone = self.lb2Zone.GetSelections()
		for i in range(len(moveZone)):
			obj = self.lb2Zone.GetString(moveZone[i])

	# Thêm 1 zone vào phía cần quan sát
	def oneAddZone_Fcn(self,event):
		for i in range(len(zoneNum)):
			obj = self.lbZone.GetString(zoneNum[i])
			if not obj in self.lb2Zone.Items:
				self.selectedZone.append(obj)
				self.lb2Zone.Append(obj)

	# Thêm nhiều zone vào phía cần quan sát
	def multipleAddZone_Fcn(self,event):
		b  = self.lbZone.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2Zone.Items:
				self.lb2Zone.Append(obj)
	
	# Bỏ bớt 1 zone khỏi phía cần quan sát
	def oneMoveZone_Fcn(self,event):
		for i in range(len(moveZone)):
			obj = self.lb2Zone.GetString(len(moveZone)-1-i)
			self.lb2Zone.Delete(moveZone[len(moveZone)-1-i])

	# Bỏ bớt nhiều zone khỏi phía cần quan sát
	def multiMoveZone_Fcn(self,event):
		b  = self.lb2Zone.Items
		for i in range(len(b)):
			obj = self.lbZone.GetString(i)
			self.lb2Zone.Delete(len(b)-1-i)

	# chọn bus bên phía trái dialog (cột origin)
	def onSelectBus(self, event):
		global busNum
		busNum = self.lbBus.GetSelections()
		for i in range(len(busNum)):
			obj = self.lbBus.GetString(busNum[i])

	# chọn bus bên phía phải dialog (cột lựa chọn)
	def onSelectToMoveBus(self, event):
		global moveBus
		moveBus = self.lb2Bus.GetSelections()
		for i in range(len(moveBus)):
			obj = self.lb2Bus.GetString(moveBus[i])

	# Thêm 1 bus vào phía cần quan sát
	def oneAddBus_Fcn(self,event):
		for i in range(len(busNum)):
			obj = self.lbBus.GetString(busNum[i])
			if not obj in self.lb2Bus.Items:
				self.selectedBus.append(obj)
				self.lb2Bus.Append(obj)

	# Thêm nhiều bus vào phía cần quan sát
	def multipleAddBus_Fcn(self,event):
		b  = self.lbBus.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.lb2Bus.Items:
				self.lb2Bus.Append(obj)
	
	# Bỏ bớt 1 bus khỏi phía cần quan sát
	def oneMoveBus_Fcn(self,event):
		for i in range(len(moveBus)):
			obj = self.lb2Bus.GetString(len(moveBus)-1-i)
			self.lb2Bus.Delete(moveBus[len(moveBus)-1-i])

	# Bỏ bớt nhiều bus khỏi phía cần quan sát
	def multiMoveBus_Fcn(self,event):
		b  = self.lb2Bus.Items
		for i in range(len(b)):
			obj = self.lbBus.GetString(i)
			self.lb2Bus.Delete(len(b)-1-i)

	# lấy kết quả từ ô tìm kiếm trong tab Bus
	def onText_SearchBus(self,event):
		searchText = self.textCtrl_SearchBus.GetValue()
		items = self.lbBusChoices
		result = []   
		for i in range(len(items)):
			if ((str(searchText)).upper() in (str(items[i]).upper())):
				result.append(items[i])
		self.lbBus.SetItems(result)
		event.Skip()

	# lấy kết quả từ ô tìm kiếm trong tab Zone
	def onText_SearchZone(self,event):
		searchText = self.textCtrl_SearchZone.GetValue()
		items = self.lbZoneChoices
		result = []   
		for i in range(len(items)):
			if ((str(searchText)).upper() in (str(items[i]).upper())):
				result.append(items[i])
		self.lbZone.SetItems(result)
		event.Skip()

	# lấy kết quả từ ô tìm kiếm trong tab Area
	def onText_SearchArea(self,event):
		searchText = self.textCtrl_SearchArea.GetValue()
		items = self.lbAreaChoices
		result = []   
		for i in range(len(items)):
			if ((str(searchText)).upper() in (str(items[i]).upper())):
				result.append(items[i])
		self.lbArea.SetItems(result)
		event.Skip()
