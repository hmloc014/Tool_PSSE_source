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
import time
import wx.aui

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TOOL-PSSE", pos = wx.DefaultPosition, size = wx.Size( 1600,800 ), style = wx.MAXIMIZE_BOX|wx.DEFAULT_FRAME_STYLE|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL ) #
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size(-1,-1  ) ) # 1635,996
		self.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		self.m_menubar1 = wx.MenuBar( wx.MB_DOCKABLE|wx.ALWAYS_SHOW_SB|wx.CLIP_CHILDREN|wx.DOUBLE_BORDER|wx.FULL_REPAINT_ON_RESIZE|wx.HSCROLL|wx.TRANSPARENT_WINDOW )
		self.m_menubar1.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )
		self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_menubar1.SetMinSize( wx.Size( 20,20 ) )
		self.m_menubar1.SetMaxSize( wx.Size( 50,50 ) )
		
		self.File = wx.Menu()

		self.Open_PSSE_File = wx.MenuItem( self.File, wx.ID_ANY, u"Open PSS/E File"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.Open_PSSE_File )
		
		self.Open_Multiple_PSSE_File = wx.MenuItem( self.File, wx.ID_ANY, u"Open Multiple PSS/E File"+ u"\t" + u"Ctrl+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.Open_Multiple_PSSE_File )

		self.Close_PSSE_File = wx.MenuItem( self.File, wx.ID_ANY, u"Close PSS/E File"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.Close_PSSE_File )

		self.Save_PSSE_File = wx.MenuItem( self.File, wx.ID_ANY, u"Save PSS/E File"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.Save_PSSE_File )

		self.Save_PSSE_File_As = wx.MenuItem( self.File, wx.ID_ANY, u"Save PSS/E File as", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.Save_PSSE_File_As )

		self.Save_All_PSSE_Files = wx.MenuItem( self.File, wx.ID_ANY, u"Save All PSS/E Files", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.Save_All_PSSE_Files )
		
		
		self.Close_PSSE_Case = wx.MenuItem( self.File, wx.ID_ANY, u"Close Window"+ u"\t" + u"Ctrl+W", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.AppendItem( self.Close_PSSE_Case )
		
		self.Export_Other_Files = wx.Menu()
		self.Export_to_Cad = wx.MenuItem( self.Export_Other_Files, wx.ID_ANY, u"Export to Cad (PQ)" + u"\t" + u"Ctrl+E", wx.EmptyString, wx.ITEM_NORMAL )
		self.Export_Other_Files.AppendItem( self.Export_to_Cad )

		self.Export_to_Cad_MVA = wx.MenuItem( self.Export_Other_Files, wx.ID_ANY, u"Export to Cad (MVA)", wx.EmptyString, wx.ITEM_NORMAL )
		self.Export_Other_Files.AppendItem( self.Export_to_Cad_MVA )

		self.Export_to_Cad_Load_Percent = wx.MenuItem( self.Export_Other_Files, wx.ID_ANY, u"Export to Cad (Load(%))", wx.EmptyString, wx.ITEM_NORMAL )
		self.Export_Other_Files.AppendItem( self.Export_to_Cad_Load_Percent )

		self.Export_to_Multi_Cad = wx.MenuItem( self.Export_Other_Files, wx.ID_ANY, u"Export to multiple Cad", wx.EmptyString, wx.ITEM_NORMAL )
		self.Export_Other_Files.AppendItem( self.Export_to_Multi_Cad )
		
		self.Export_to_Excel = wx.MenuItem( self.Export_Other_Files, wx.ID_ANY, u"Export to Excel", wx.EmptyString, wx.ITEM_NORMAL )
		self.Export_Other_Files.AppendItem( self.Export_to_Excel )
		
		self.Export_to_Dyn = wx.MenuItem( self.Export_Other_Files, wx.ID_ANY, u"Export to Dyn", wx.EmptyString, wx.ITEM_NORMAL )
		self.Export_Other_Files.AppendItem( self.Export_to_Dyn )
		
		self.File.AppendSubMenu( self.Export_Other_Files, u"Export Other Files" )
		
		self.m_menubar1.Append( self.File, u"File" ) 
		
		self.Edit = wx.Menu()
		self.Bus = wx.Menu()
		self.New_Bus = wx.MenuItem( self.Bus, wx.ID_ANY, u"New Bus"+ u"\t" + u"Ctrl+U", wx.EmptyString, wx.ITEM_NORMAL )
		self.Bus.AppendItem( self.New_Bus )
		
		self.Turn_On_Off_Bus = wx.MenuItem( self.Bus, wx.ID_ANY, u"Turn On/Off", wx.EmptyString, wx.ITEM_NORMAL )
		self.Bus.AppendItem( self.Turn_On_Off_Bus )

		self.Delete_Bus = wx.MenuItem( self.Bus, wx.ID_ANY, u"Delete Bus", wx.EmptyString, wx.ITEM_NORMAL )
		self.Bus.AppendItem( self.Delete_Bus )
		
		self.Split_Bus = wx.MenuItem( self.Bus, wx.ID_ANY, u"Split Bus", wx.EmptyString, wx.ITEM_NORMAL )
		self.Bus.AppendItem( self.Split_Bus )
		
		self.Joint_Bus = wx.MenuItem( self.Bus, wx.ID_ANY, u"Joint Bus", wx.EmptyString, wx.ITEM_NORMAL )
		self.Bus.AppendItem( self.Joint_Bus )
		
		self.Line_Tap = wx.MenuItem( self.Bus, wx.ID_ANY, u"Line Tap", wx.EmptyString, wx.ITEM_NORMAL )
		self.Bus.AppendItem( self.Line_Tap )
		
		self.Edit.AppendSubMenu( self.Bus, u"Bus" )
		
		self.Add_Elements = wx.Menu()
		self.Add_Gen = wx.MenuItem( self.Add_Elements, wx.ID_ANY, u"Add Generator"+ u"\t" + u"Ctrl+G", wx.EmptyString, wx.ITEM_NORMAL )
		self.Add_Elements.AppendItem( self.Add_Gen )
		
		self.Add_Branch = wx.MenuItem( self.Add_Elements, wx.ID_ANY, u"Add Branch"+ u"\t" + u"Ctrl+B", wx.EmptyString, wx.ITEM_NORMAL )
		self.Add_Elements.AppendItem( self.Add_Branch )
		
		self.Add_3Winding = wx.MenuItem( self.Add_Elements, wx.ID_ANY, u"Add 3 Winding"+ u"\t" + u"Ctrl+3", wx.EmptyString, wx.ITEM_NORMAL )
		self.Add_Elements.AppendItem( self.Add_3Winding )
		
		self.Add_2Winding = wx.MenuItem( self.Add_Elements, wx.ID_ANY, u"Add 2 Winding"+ u"\t" + u"Ctrl+2", wx.EmptyString, wx.ITEM_NORMAL )
		self.Add_Elements.AppendItem( self.Add_2Winding )
		
		self.Add_Load = wx.MenuItem( self.Add_Elements, wx.ID_ANY, u"Add Load"+ u"\t" + u"Ctrl+L", wx.EmptyString, wx.ITEM_NORMAL )
		self.Add_Elements.AppendItem( self.Add_Load )\

		self.Add_Shunt = wx.MenuItem( self.Add_Elements, wx.ID_ANY, u"Add Shunt", wx.EmptyString, wx.ITEM_NORMAL )
		self.Add_Elements.AppendItem( self.Add_Shunt )
		
		self.Edit.AppendSubMenu( self.Add_Elements, u"Add Elements" )
		
		self.Change = wx.Menu()
		self.Change_Zone_Source = wx.MenuItem( self.Change, wx.ID_ANY, u"Change Zone Source/Load", wx.EmptyString, wx.ITEM_NORMAL )
		self.Change.AppendItem( self.Change_Zone_Source )
		
		self.Change_Area_Source = wx.MenuItem( self.Change, wx.ID_ANY, u"Change Area Source/Load", wx.EmptyString, wx.ITEM_NORMAL )
		self.Change.AppendItem( self.Change_Area_Source )
		
		self.Edit.AppendSubMenu( self.Change, u"Change Source/Load" )

		self.Run_Macro = wx.MenuItem( self.Edit, wx.ID_ANY, u"Run Macro File", wx.EmptyString, wx.ITEM_NORMAL )
		self.Edit.AppendItem( self.Run_Macro )
		
		# self.Run_Multi_Macro = wx.MenuItem( self.Edit, wx.ID_ANY, u"Run Multi Macro File", wx.EmptyString, wx.ITEM_NORMAL )
		# self.Edit.AppendItem( self.Run_Multi_Macro )

		self.m_menubar1.Append( self.Edit, u"Edit" ) 

		self.View = wx.Menu()
		self.View_PSSE = wx.MenuItem( self.View, wx.ID_ANY, u"View PSS/E", wx.EmptyString, wx.ITEM_NORMAL )
		self.View.AppendItem( self.View_PSSE )
		
		self.View_Database = wx.MenuItem( self.View, wx.ID_ANY, u"View Database", wx.EmptyString, wx.ITEM_NORMAL )
		self.View.AppendItem( self.View_Database )
		
		self.m_menubar1.Append( self.View, u"View" ) 
		
		self.Window = wx.Menu()
		
		self.Reload = wx.MenuItem( self.Window, wx.ID_ANY, u"Reload" +  u"\t" + u"Ctrl+R", wx.EmptyString, wx.ITEM_NORMAL )
		self.Window.AppendItem( self.Reload )

		self.Minimize = wx.MenuItem( self.Window, wx.ID_ANY, u"Minimize", wx.EmptyString, wx.ITEM_NORMAL )
		self.Window.AppendItem( self.Minimize )
		
		self.m_menubar1.Append( self.Window, u"Window" ) 
		
		self.Calculation = wx.Menu()
		self.Power_Flow_Selected_Case = wx.MenuItem( self.Calculation, wx.ID_ANY, u"Power Flow Calculation Selected Case", wx.EmptyString, wx.ITEM_NORMAL )
		self.Calculation.AppendItem( self.Power_Flow_Selected_Case )

		self.Power_Flow = wx.MenuItem( self.Calculation, wx.ID_ANY, u"Power Flow Calculation All Cases", wx.EmptyString, wx.ITEM_NORMAL )
		self.Calculation.AppendItem( self.Power_Flow )

		self.Contigency_Cal = wx.Menu()

		self.Create_New_DFX = wx.MenuItem( self.Contigency_Cal, wx.ID_ANY, u"Create new sub,mon,con files", wx.EmptyString, wx.ITEM_NORMAL )
		self.Contigency_Cal.AppendItem( self.Create_New_DFX )

		self.Choose_Available_DFX = wx.MenuItem( self.Contigency_Cal, wx.ID_ANY, u"Choose available sub,mon,con files", wx.EmptyString, wx.ITEM_NORMAL )
		self.Contigency_Cal.AppendItem( self.Choose_Available_DFX )

		self.Auto_Contigencies = wx.MenuItem( self.Contigency_Cal, wx.ID_ANY, u"Auto Contigencies", wx.EmptyString, wx.ITEM_NORMAL )
		self.Contigency_Cal.AppendItem( self.Auto_Contigencies )
		
		self.Calculation.AppendSubMenu( self.Contigency_Cal, u"Contigency Calculation" )

		self.Short_Circuit_Cal = wx.Menu()

		self.Distribution_Short_Circuit = wx.MenuItem( self.Short_Circuit_Cal, wx.ID_ANY, u"Distribution Short Circuit", wx.EmptyString, wx.ITEM_NORMAL )
		self.Short_Circuit_Cal.AppendItem( self.Distribution_Short_Circuit )

		self.Distribution_Short_Circuit_From_File = wx.MenuItem( self.Short_Circuit_Cal, wx.ID_ANY, u"Distribution Short Circuit From File", wx.EmptyString, wx.ITEM_NORMAL )
		self.Short_Circuit_Cal.AppendItem( self.Distribution_Short_Circuit_From_File )

		self.Short_Circuit_Cal_New = wx.MenuItem( self.Short_Circuit_Cal, wx.ID_ANY, u"Short Circuit Calculation From Bus", wx.EmptyString, wx.ITEM_NORMAL )
		self.Short_Circuit_Cal.AppendItem( self.Short_Circuit_Cal_New )

		self.Short_Circuit_Cal_From_File = wx.MenuItem( self.Short_Circuit_Cal, wx.ID_ANY, u"Short Circuit Calculation From File", wx.EmptyString, wx.ITEM_NORMAL )
		self.Short_Circuit_Cal.AppendItem( self.Short_Circuit_Cal_From_File )

		self.Short_Circuit_Cal_All_Cases_Export_Word = wx.MenuItem( self.Short_Circuit_Cal, wx.ID_ANY, u"Short Circuit All Cases Export To One .txt", wx.EmptyString, wx.ITEM_NORMAL )
		self.Short_Circuit_Cal.AppendItem( self.Short_Circuit_Cal_All_Cases_Export_Word )

		self.Short_Circuit_Cal_All_Cases_Export_Txt = wx.MenuItem( self.Short_Circuit_Cal, wx.ID_ANY, u"Short Circuit All Cases Export Txt", wx.EmptyString, wx.ITEM_NORMAL )
		self.Short_Circuit_Cal.AppendItem( self.Short_Circuit_Cal_All_Cases_Export_Txt )

		self.Calculation.AppendSubMenu( self.Short_Circuit_Cal, u"Short Circuit Calculation" )
		
		self.Static_Stability_Cal = wx.Menu()

		self.Static_Stability_Cal_Selected_Case = wx.MenuItem( self.Static_Stability_Cal, wx.ID_ANY, u"Static Stability Calculation Selected Case", wx.EmptyString, wx.ITEM_NORMAL )
		self.Static_Stability_Cal.AppendItem( self.Static_Stability_Cal_Selected_Case )
	
		self.Auto_Static_Stability_Cal = wx.MenuItem( self.Static_Stability_Cal, wx.ID_ANY, u"Auto Static Stability Calculation", wx.EmptyString, wx.ITEM_NORMAL )
		self.Static_Stability_Cal.AppendItem( self.Auto_Static_Stability_Cal )

		self.Calculation.AppendSubMenu( self.Static_Stability_Cal, u"Static Stability Calculation"  )
		
		self.Dynamic_Stability_Cal = wx.Menu()

		self.Dynamic_Stability_Cal_From_IDV_File = wx.MenuItem( self.Dynamic_Stability_Cal, wx.ID_ANY, u"Dynamic Stability Calculation From IDV Files", wx.EmptyString, wx.ITEM_NORMAL )
		self.Dynamic_Stability_Cal.AppendItem( self.Dynamic_Stability_Cal_From_IDV_File )
	
		self.Dynamic_Stability_Cal_By_Create_New_IDV = wx.MenuItem( self.Dynamic_Stability_Cal, wx.ID_ANY, u"Dynamic Stability Calculation by create new IDV Files", wx.EmptyString, wx.ITEM_NORMAL )
		self.Dynamic_Stability_Cal.AppendItem( self.Dynamic_Stability_Cal_By_Create_New_IDV )

		# self.Dynamic_Stability_Cal = wx.MenuItem( self.Calculation, wx.ID_ANY, u"Dynamic Stability Calculation", wx.EmptyString, wx.ITEM_NORMAL )
		self.Calculation.AppendSubMenu( self.Dynamic_Stability_Cal,u"Dynamic Stability Calculation" )

		self.Shunt_Reactor_Cal = wx.MenuItem( self.Calculation, wx.ID_ANY, u"Shunt Reactor Calculation", wx.EmptyString, wx.ITEM_NORMAL )
		self.Calculation.AppendItem( self.Shunt_Reactor_Cal )
		
		self.PV_Cal = wx.MenuItem( self.Calculation, wx.ID_ANY, u"Inter-regional transmission limit", wx.EmptyString, wx.ITEM_NORMAL )
		self.Calculation.AppendItem( self.PV_Cal )
		self.m_menubar1.Append( self.Calculation, u"Calculation" ) 
		
		self.Help = wx.Menu()
		self.Version = wx.MenuItem( self.Help, wx.ID_ANY, u"Version", wx.EmptyString, wx.ITEM_NORMAL )
		self.Help.AppendItem( self.Version )

		self.Shortcut = wx.MenuItem( self.Help, wx.ID_ANY, u"Shortcut", wx.EmptyString, wx.ITEM_NORMAL )
		self.Help.AppendItem( self.Shortcut )
		
		self.m_menubar1.Append( self.Help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_mainSplitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_mainSplitter.SetMinimumPaneSize( 280 )
		self.m_mainSplitter.SetSashGravity( 0.0 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		#panel 8 =9. 6=10
		self.m_splitter4 = wx.SplitterWindow( self.m_mainSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter4.SetMinimumPaneSize( 100 )
		self.m_splitter4.SetSashGravity( 0.67 )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )
		
		self.m_panel9 = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter21 = wx.SplitterWindow( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SP_NO_XP_THEME )
		self.m_splitter21.SetMinimumPaneSize( 100 )
		self.m_splitter21.SetSashGravity( 0.5 )
		self.m_splitter21.Bind( wx.EVT_IDLE, self.m_splitter21OnIdle )
		
		self.m_panel10 = wx.Panel( self.m_splitter21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.gridFile = wx.grid.Grid( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB )
		
		# Grid
		self.gridFile.CreateGrid( 30, 8 )
		self.gridFile.EnableEditing( True )
		self.gridFile.EnableGridLines( True )
		self.gridFile.EnableDragGridSize( False )
		self.gridFile.SetMargins( 0, 0 )
		
		# Columns
		
		self.gridFile.SetColSize( 0, 140 )
		self.gridFile.SetColSize( 1, 60 )
		self.gridFile.SetColSize( 2, 60 )
		self.gridFile.SetColSize( 3, 60 )
		self.gridFile.SetColSize( 4, 60 )
		self.gridFile.SetColSize( 5, 90 )
		self.gridFile.SetColSize( 6, 90 )
		self.gridFile.SetColSize( 7, 90 )
		self.gridFile.EnableDragColMove( False )
		self.gridFile.EnableDragColSize( True )
		self.gridFile.SetColLabelSize( 40 )
		self.gridFile.SetColLabelValue( 0, u"File Name" )
		self.gridFile.SetColLabelValue( 1, u"P-MW\n Balance" )
		self.gridFile.SetColLabelValue( 2, u"Q-MVAr\n Balance" )
		self.gridFile.SetColLabelValue( 3, u"MVA\n error" )
		self.gridFile.SetColLabelValue( 4, u"P-MW\n loss" )
		self.gridFile.SetColLabelValue( 5, u"Convergence\n iterations" )
		self.gridFile.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridFile.AutoSizeRows()
		self.gridFile.EnableDragRowSize( False )
		self.gridFile.SetRowLabelSize( 40 )
		self.gridFile.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridFile.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.gridFile.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.gridFile.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.gridFile, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		# bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )
		self.m_panel10.SetSizer( bSizer8 )
		self.m_panel10.Layout()
		self.m_panel7 = wx.Panel( self.m_splitter21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		attr = wx.grid.GridCellAttr()
		attr.SetBackgroundColour('light blue')
		
		self.gridArea = wx.grid.Grid( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB)
		
		# Grid
		self.gridArea.CreateGrid( 100, 7 )
		self.gridArea.EnableEditing( True )
		self.gridArea.EnableGridLines( True )
		self.gridArea.EnableDragGridSize( False )
		self.gridArea.SetMargins( 0, 0 )
		
		# Columns
		self.gridArea.SetColSize( 0, 35 )
		self.gridArea.SetColAttr(0, attr)
		self.gridArea.SetColSize( 1, 110 )
		self.gridArea.SetColAttr(1, attr)
		self.gridArea.SetColSize( 2, 60 )
		self.gridArea.SetColSize( 3, 60 )
		self.gridArea.SetColAttr(3, attr)
		self.gridArea.SetColSize( 4, 60 )
		self.gridArea.SetColSize( 5, 60 )
		self.gridArea.SetColAttr(5, attr)
		self.gridArea.SetColSize( 6, 60 )
		self.gridArea.SetColAttr(6, attr)
		self.gridArea.EnableDragColMove( False )
		self.gridArea.EnableDragColSize( True )
		self.gridArea.SetColLabelSize( 40 )
		self.gridArea.SetColLabelValue( 0, u"No." )
		self.gridArea.SetColLabelValue( 1, u"Area Name" )
		self.gridArea.SetColLabelValue( 2, u"PGen" )
		self.gridArea.SetColLabelValue( 3, u"QGen" )
		self.gridArea.SetColLabelValue( 4, u"PLoad" )
		self.gridArea.SetColLabelValue( 5, u"QLoad" )
		self.gridArea.SetColLabelValue( 6, u"Cos ϕ" )
		self.gridArea.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridArea.EnableDragRowSize( True )
		self.gridArea.SetRowLabelSize( 40 )
		self.gridArea.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridArea.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		# Cell Defaults
		self.gridArea.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.gridArea.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer9.Add( self.gridArea, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel7.SetSizer( bSizer9 )
		self.m_panel7.Layout()
		self.m_splitter21.SplitHorizontally( self.m_panel10, self.m_panel7, 0 )
		bSizer6.Add( self.m_splitter21, 1, wx.EXPAND, 5 )
		
		# bSizer6.Add( bSizer9, 2, wx.EXPAND, 5 )

		self.m_panel9.SetSizer( bSizer6 )
		self.m_panel9.Layout()
		# panel9 = 18
		self.m_panel18 = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.gridZone = wx.grid.Grid( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB )
		
		# Grid
		self.gridZone.CreateGrid( 100, 7 )
		self.gridZone.EnableEditing( True )
		self.gridZone.EnableGridLines( True )
		self.gridZone.EnableDragGridSize( False )
		self.gridZone.SetMargins( 0, 0 )
		
		# Columns
		self.gridZone.SetColSize( 0, 35 )
		self.gridZone.SetColSize( 1, 110 )
		self.gridZone.SetColSize( 2, 60 )
		self.gridZone.SetColSize( 3, 60 )
		self.gridZone.SetColSize( 4, 60 )
		self.gridZone.SetColSize( 5, 60 )
		self.gridZone.SetColSize( 6, 60 )
		self.gridZone.EnableDragColMove( False )
		self.gridZone.EnableDragColSize( True )
		self.gridZone.SetColLabelSize( 40 )
		self.gridZone.SetColLabelValue( 0, u"No." )
		self.gridZone.SetColAttr(0, attr)
		self.gridZone.SetColLabelValue( 1, u"Zone Name" )
		self.gridZone.SetColAttr(1, attr)
		self.gridZone.SetColLabelValue( 2, u"PGen" )
		self.gridZone.SetColLabelValue( 3, u"QGen" )
		self.gridZone.SetColAttr(3, attr)
		self.gridZone.SetColLabelValue( 4, u"PLoad" )
		self.gridZone.SetColLabelValue( 5, u"QLoad" )
		self.gridZone.SetColAttr(5, attr)
		self.gridZone.SetColLabelValue( 6, u"Cos ϕ" )
		self.gridZone.SetColAttr(6, attr)
		self.gridZone.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridZone.EnableDragRowSize( True )
		self.gridZone.SetRowLabelSize( 40 )
		self.gridZone.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridZone.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		# Cell Defaults
		self.gridZone.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer10.Add( self.gridZone, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel18.SetSizer( bSizer10 )
		self.m_panel18.Layout()
		self.m_splitter4.SplitHorizontally( self.m_panel9, self.m_panel18, 0 )

		# bSizer6.Add( bSizer10, 2, wx.EXPAND, 5 )
		
		
		# bSizer5.Add( bSizer6, 2, wx.EXPAND, 5 )
		
		self.m_notebook2 = wx.Notebook( self.m_mainSplitter, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), wx.NB_FIXEDWIDTH|wx.NB_LEFT|wx.NB_NOPAGETHEME )
		self.m_notebook2.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		self.gridPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.gridPage.SetBackgroundColour( wx.Colour( 204, 240, 251 ) )
		# self.gridPage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.BusNum = wx.StaticText( self.gridPage, wx.ID_ANY, u"Bus Number", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_LEFT )
		self.BusNum.Wrap( -1 )
		self.BusNum.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.BusNum, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		toBusNumChoices = []
		self.BusNumInput = wx.ComboBox( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), toBusNumChoices, wx.CB_SORT )
		self.BusNumInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		gSizer1.Add( self.BusNumInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.BusName = wx.StaticText( self.gridPage, wx.ID_ANY, u"Bus Name", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.BusName.Wrap( -1 )
		self.BusName.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.BusName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.BusNameInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.BusNameInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.BusNameInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Code = wx.StaticText( self.gridPage, wx.ID_ANY, u"Code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Code.Wrap( -1 )
		self.Code.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.Code, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.CodeInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.CodeInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.CodeInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Udm = wx.StaticText( self.gridPage, wx.ID_ANY, u"Udm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Udm.Wrap( -1 )
		self.Udm.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.Udm, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.UdmInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.UdmInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.UdmInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Voltage = wx.StaticText( self.gridPage, wx.ID_ANY, u"Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Voltage.Wrap( -1 )
		self.Voltage.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.Voltage, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.VoltageInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.VoltageInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.VoltageInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Area = wx.StaticText( self.gridPage, wx.ID_ANY, u"Area", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Area.Wrap( -1 )
		self.Area.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.Area, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.AreaInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AreaInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.AreaInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.AreaName = wx.StaticText( self.gridPage, wx.ID_ANY, u"Area Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AreaName.Wrap( -1 )
		self.AreaName.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.AreaName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.AreaNameInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AreaNameInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.AreaNameInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.Zone = wx.StaticText( self.gridPage, wx.ID_ANY, u"Zone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Zone.Wrap( -1 )
		self.Zone.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.Zone, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ZoneInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ZoneInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.ZoneInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ZoneName = wx.StaticText( self.gridPage, wx.ID_ANY, u"Zone Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ZoneName.Wrap( -1 )
		self.ZoneName.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.ZoneName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ZoneNameInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.ZoneNameInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.ZoneNameInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.CosP = wx.StaticText( self.gridPage, wx.ID_ANY, u"CosP", wx.Point( -1,-1 ), wx.DefaultSize, wx.ALIGN_RIGHT )
		self.CosP.Wrap( -1 )
		self.CosP.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.CosP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.CosPInput = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.CosPInput.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer1.Add( self.CosPInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer16.Add( gSizer1, 0, 0, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		filter_selectionChoices = [ u"Bus ID", u"Bus Name", u"Base KV", u"Area Num", u"Area Name", u"Zone Num", u"Zone Name", u"Code", wx.EmptyString ]
		self.filter_selection = wx.Choice( self.gridPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( 85,-1 ), filter_selectionChoices, 0 )
		self.filter_selection.SetSelection( 0 )
		self.filter_selection.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.filter_selection.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer24.Add( self.filter_selection, 0, wx.ALL, 5 )
		
		self.filter_input_text = wx.TextCtrl( self.gridPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.filter_input_text.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer24.Add( self.filter_input_text, 0, wx.ALL, 5 )
		bSizer20.Add( bSizer24, 1, 0, 5 )
		
		bSizer16.Add( bSizer20, 0, 0, 5 )

		bSizer332 = wx.BoxSizer( wx.VERTICAL )
		bSizer16.Add(bSizer332, 0, 0, 5 )



		bSizer331 = wx.BoxSizer( wx.VERTICAL )

		# self.label = wx.StaticText( self.gridPage, wx.ID_ANY, u"Commonly used function", wx.Point( -1,-1 ), wx.DefaultSize, wx.ALIGN_CENTER )
		# self.label.Wrap( -1 )
		# self.label.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		# bSizer331.Add( self.label, 0, 0, 5 )

		self.m_staticText1 = wx.StaticText( self.gridPage, wx.ID_ANY, u"Commonly used function", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		bSizer331.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		functionButtonSize = wx.Size( -1, 40 )
		functionButtonFont = wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" )
		functionButtonBackground = wx.Colour( 242, 242, 242 )

		def styleFunctionButton( button, bitmapPath, toolTip ):
			bitmap = wx.Bitmap( bitmapPath, wx.BITMAP_TYPE_ANY )
			if bitmap.IsOk():
				bitmap = wx.BitmapFromImage( bitmap.ConvertToImage().Scale( 24, 24, wx.IMAGE_QUALITY_HIGH ) )
			button.SetBitmap( bitmap )
			button.SetBitmapPosition( wx.LEFT )
			button.SetBitmapMargins( 12, 4 )
			button.SetFont( functionButtonFont )
			button.SetBackgroundColour( functionButtonBackground )
			button.SetToolTipString( toolTip )

		self.m_tool0 = wx.Button( self.gridPage, wx.ID_ANY, u"Power Flow", wx.DefaultPosition, functionButtonSize, wx.BU_LEFT )
		styleFunctionButton( self.m_tool0, u"images/icon5.png", u"Calculate power flow and refresh grids" )
		bSizer331.Add( self.m_tool0, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 8 )

		self.m_tool1 = wx.Button( self.gridPage, wx.ID_ANY, u"Auto Contingencies", wx.DefaultPosition, functionButtonSize, wx.BU_LEFT )
		styleFunctionButton( self.m_tool1, u"images/c.jpg", u"Run automatic contingencies" )
		bSizer331.Add( self.m_tool1, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 8 )

		self.m_toolN1 = wx.Button( self.gridPage, wx.ID_ANY, u"Create N-1 sav files", wx.DefaultPosition, functionButtonSize, wx.BU_LEFT )
		styleFunctionButton( self.m_toolN1, u"images/c.jpg", u"Create one-outage SAV files from selected ACC contingencies" )
		bSizer331.Add( self.m_toolN1, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 8 )

		self.m_tool2 = wx.Button( self.gridPage, wx.ID_ANY, u"Export Multiple Cad", wx.DefaultPosition, functionButtonSize, wx.BU_LEFT )
		styleFunctionButton( self.m_tool2, u"images/cad.jpg", u"Export multiple CAD files" )
		bSizer331.Add( self.m_tool2, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 8 )

		self.m_tool4 = wx.ToggleButton( self.gridPage, wx.ID_ANY, u"Record", wx.DefaultPosition, functionButtonSize, wx.BU_LEFT )
		styleFunctionButton( self.m_tool4, u"images/record.png", u"Record PSSE commands" )
		bSizer331.Add( self.m_tool4, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 8 )
		#u"../SourceCode/Tool-PSSE-2/images/short-circuit2-1.jpg"
		bSizer16.Add( bSizer331, 1, wx.EXPAND, 15)
		
		
		bSizer15.Add( bSizer16, 0, 0, 10 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter41 = wx.SplitterWindow( self.gridPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_NO_XP_THEME )
		self.m_splitter41.Bind( wx.EVT_IDLE, self.m_splitter41OnIdle )
		
		self.m_panel19 = wx.Panel( self.m_splitter41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.gridBusInfo = wx.grid.Grid( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		# Grid
		self.gridBusInfo.CreateGrid( 100, 17 )
		self.gridBusInfo.EnableEditing( True )
		self.gridBusInfo.EnableGridLines( True )
		self.gridBusInfo.EnableDragGridSize( False )
		self.gridBusInfo.SetMargins( 0, 0 )
		
		# Columns
		self.gridBusInfo.SetColSize( 0, 80 )
		self.gridBusInfo.SetColSize( 1, 170 )
		self.gridBusInfo.SetColSize( 2, 65 )
		self.gridBusInfo.SetColSize( 3, 100 )
		self.gridBusInfo.SetColSize( 4, 35 )
		self.gridBusInfo.SetColSize( 5, 45 )
		self.gridBusInfo.SetColSize( 6, 55 )
		self.gridBusInfo.SetColSize( 7, 55 )
		self.gridBusInfo.SetColSize( 8, 55 )
		self.gridBusInfo.SetColSize( 9, 70 )
		self.gridBusInfo.SetColSize( 10, 70 )
		self.gridBusInfo.SetColSize( 11, 100 )
		self.gridBusInfo.SetColSize( 12, 100 )
		self.gridBusInfo.SetColSize( 13, 100 )
		self.gridBusInfo.SetColSize( 14, 180 )
		self.gridBusInfo.SetColSize( 15, 180 )
		self.gridBusInfo.SetColSize( 16, 180 )
		self.gridBusInfo.EnableDragColMove( False )
		self.gridBusInfo.EnableDragColSize( True )
		self.gridBusInfo.SetColLabelSize( 30 )
		self.gridBusInfo.SetColLabelValue( 0, u"Type" )
		self.gridBusInfo.SetColLabelValue( 1, u"Type Name" )
		self.gridBusInfo.SetColLabelValue( 2, u"Bus ID" )
		self.gridBusInfo.SetColAttr(2, attr)
		self.gridBusInfo.SetColLabelValue( 3, u"Bus Name" )
		self.gridBusInfo.SetColAttr(3, attr)
		self.gridBusInfo.SetColLabelValue( 4, u"ID" )
		self.gridBusInfo.SetColLabelValue( 5, u"Status" )
		self.gridBusInfo.SetColLabelValue( 6, u"P" )
		self.gridBusInfo.SetColAttr(6, attr)
		self.gridBusInfo.SetColLabelValue( 7, u"Q" )
		self.gridBusInfo.SetColAttr(7, attr)
		self.gridBusInfo.SetColLabelValue( 8, u"Load(%)" )
		self.gridBusInfo.SetColAttr(8, attr)
		self.gridBusInfo.SetColLabelValue( 9, u"Length\n(MVA)" )
		self.gridBusInfo.SetColLabelValue( 10, u"Rate" )
		self.gridBusInfo.SetColLabelValue( 11, u"R\n(W1-2 R)" )
		# self.gridBusInfo.SetColAttr(11, attr)
		self.gridBusInfo.SetColLabelValue( 12, u"X\n(W1-2 X)" )
		# self.gridBusInfo.SetColAttr(12, attr)
		self.gridBusInfo.SetColLabelValue( 13, u"Charging B\n(Trans Name)" )
		self.gridBusInfo.SetColLabelValue( 14, u"Branch R0\n(Wind3 R01+jX01)" )
		self.gridBusInfo.SetColAttr(14, attr)
		self.gridBusInfo.SetColLabelValue( 15, u"Branch X0\nWind3 R02+jX02" )
		self.gridBusInfo.SetColAttr(15, attr)
		self.gridBusInfo.SetColLabelValue( 16, u"Branch B0\nWind3 R03+jX03" )
		self.gridBusInfo.SetColAttr(16, attr)
		self.gridBusInfo.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridBusInfo.EnableDragRowSize( True )
		self.gridBusInfo.SetRowLabelSize( 50 )
		self.gridBusInfo.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridBusInfo.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.gridBusInfo.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.gridBusInfo.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.gridBusInfo.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridBusInfo.SetMaxSize( wx.Size( -1,396 ) )
		
		bSizer18.Add( self.gridBusInfo, 1, 0, 5 )
		
		self.m_panel19.SetSizer( bSizer18 )
		self.m_panel19.Layout()
		bSizer18.Fit( self.m_panel19 )
		
		# bSizer17.Add( bSizer18, 3, 0, 5 )
		
		self.m_panel20 = wx.Panel( self.m_splitter41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )


		self.m_splitter2 = wx.SplitterWindow( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_NO_XP_THEME )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		self.m_panel6 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.gridSearch = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		# Grid
		self.gridSearch.CreateGrid( 11000, 20 )
		self.gridSearch.EnableEditing( True )
		self.gridSearch.EnableGridLines( True )
		self.gridSearch.EnableDragGridSize( False )
		self.gridSearch.SetMargins( 0, 0 )
		
		# Columns
		self.gridSearch.SetColSize( 0, 59 )
		self.gridSearch.SetColSize( 1, 100 )
		self.gridSearch.SetColSize( 2, 58 )
		self.gridSearch.SetColSize( 3, 40 )
		self.gridSearch.SetColSize( 4, 90 )
		self.gridSearch.SetColSize( 5, 40 )
		self.gridSearch.SetColSize( 6, 80 )
		self.gridSearch.SetColSize( 7, 40 )
		self.gridSearch.SetColSize( 8, 40 )
		self.gridSearch.SetColSize( 9, 68 )
		self.gridSearch.SetColSize( 10, 78 )
		self.gridSearch.SetColSize( 11, 80 )
		self.gridSearch.SetColSize( 12, 80 )
		self.gridSearch.SetColSize( 13, 80 )
		self.gridSearch.SetColSize( 14, 80 )
		self.gridSearch.SetColSize( 15, 80 )
		self.gridSearch.SetColSize( 16, 80 )
		self.gridSearch.SetColSize( 17, 80 )
		self.gridSearch.SetColSize( 18, 80 )
		self.gridSearch.SetColSize( 19, 80 )
		self.gridSearch.EnableDragColMove( False )
		self.gridSearch.EnableDragColSize( True )
		self.gridSearch.SetColLabelSize( 40 )
		self.gridSearch.SetColLabelValue( 0, u"Bus Num" )
		self.gridSearch.SetColLabelValue( 1, u"Bus Name" )
		self.gridSearch.SetColLabelValue( 2, u"Base KV" )
		self.gridSearch.SetColLabelValue( 3, u"Area" )
		self.gridSearch.SetColLabelValue( 4, u"Area Name" )
		self.gridSearch.SetColAttr(4, attr)
		self.gridSearch.SetColLabelValue( 5, u"Zone" )
		self.gridSearch.SetColLabelValue( 6, u"Zone Name" )
		self.gridSearch.SetColAttr(6, attr)
		self.gridSearch.SetColLabelValue( 7, u"Owner" )
		self.gridSearch.SetColLabelValue( 8, u"Code" )
		self.gridSearch.SetColLabelValue( 9, u"Voltage Pu" )
		self.gridSearch.SetColAttr(9, attr)
		self.gridSearch.SetColLabelValue( 10, u"Angle (deg)" )
		self.gridSearch.SetColAttr(10, attr)
		self.gridSearch.SetColLabelValue( 11, u"Cos ϕ" )
		self.gridSearch.SetColAttr(11, attr)
		self.gridSearch.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridSearch.EnableDragRowSize( True )
		self.gridSearch.SetRowLabelSize( 50 )
		self.gridSearch.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridSearch.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.gridSearch.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.gridSearch.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.gridSearch.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.gridSearch.SetMaxSize( wx.Size( -1,-1 ) )
		
		bSizer38.Add( self.gridSearch, 1, 0, 5 )
		
		
		self.m_panel6.SetSizer( bSizer38 )
		self.m_panel6.Layout()
		bSizer38.Fit( self.m_panel6 )
		self.m_panel8 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook3 = wx.Notebook( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scrolledWindow5 = wx.ScrolledWindow( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow5.SetScrollRate( 5, 5 )
		bSizer291 = wx.BoxSizer( wx.VERTICAL )
		
		self.terminalText = wx.TextCtrl( self.m_scrolledWindow5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE )
		self.terminalText.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New" ) )
		bSizer291.Add( self.terminalText, 1, wx.ALL|wx.EXPAND,0 )
		
		
		self.m_scrolledWindow5.SetSizer( bSizer291 )
		self.m_scrolledWindow5.Layout()
		bSizer291.Fit( self.m_scrolledWindow5 )
		self.m_notebook3.AddPage( self.m_scrolledWindow5, u"Terminal", False )
		
		bSizer39.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer39 )
		self.m_panel8.Layout()
		bSizer39.Fit( self.m_panel8 )
		self.m_splitter2.SplitHorizontally( self.m_panel6, self.m_panel8, 0 )
		bSizer19.Add( self.m_splitter2, 1, wx.EXPAND, 5 )
		self.m_panel20.SetSizer( bSizer19 )
		self.m_panel20.Layout()
		bSizer19.Fit( self.m_panel20 )
		self.m_splitter41.SplitHorizontally( self.m_panel19, self.m_panel20, 0 )

		bSizer17.Add( self.m_splitter41, 1, wx.EXPAND, 5 )
		
		
		bSizer15.Add( bSizer17, 4, wx.EXPAND, 5 )
		
		
		self.gridPage.SetSizer( bSizer15 )
		self.gridPage.Layout()
		bSizer15.Fit( self.gridPage )
		self.m_notebook2.AddPage( self.gridPage, u"Grid", True )

		self.twoWind = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer182 = wx.BoxSizer( wx.VERTICAL )
		
		self.grid2wind = wx.grid.Grid( self.twoWind, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		# Grid
		self.grid2wind.CreateGrid( 3500, 17 )
		self.grid2wind.EnableEditing( True )
		self.grid2wind.EnableGridLines( True )
		self.grid2wind.EnableDragGridSize( True )
		self.grid2wind.SetMargins( 0, 0 )
		
		# Columns
		self.grid2wind.SetColSize( 0, 60 )
		self.grid2wind.SetColSize( 1, 97 )
		self.grid2wind.SetColSize( 2, 50 )
		self.grid2wind.SetColSize( 3, 116 )
		self.grid2wind.SetColSize( 4, 30 )
		self.grid2wind.SetColSize( 5, 60 )
		self.grid2wind.SetColSize( 6, 60 )
		self.grid2wind.SetColSize( 7, 80 )
		self.grid2wind.SetColSize( 8, 80 )
		self.grid2wind.SetColSize( 9, 80 )
		self.grid2wind.SetColSize( 10, 60 )
		self.grid2wind.SetColSize( 11, 80 )
		self.grid2wind.SetColSize( 12, 80 )
		self.grid2wind.SetColSize( 13, 80 )
		self.grid2wind.SetColSize( 14, 80 )
		self.grid2wind.SetColSize( 15, 80 )
		self.grid2wind.SetColSize( 16, 80 )
		self.grid2wind.EnableDragColMove( False )
		self.grid2wind.EnableDragColSize( True )
		self.grid2wind.SetColLabelSize( 30 )
		self.grid2wind.SetColLabelValue( 0, u"From Bus" )
		self.grid2wind.SetColAttr(0, attr)
		self.grid2wind.SetColLabelValue( 1, u"From Bus\n Name" )
		self.grid2wind.SetColAttr(1, attr)
		self.grid2wind.SetColLabelValue( 2, u"To Bus" )
		self.grid2wind.SetColAttr(2, attr)
		self.grid2wind.SetColLabelValue( 3, u"To Bus\n Name" )
		self.grid2wind.SetColAttr(3, attr)
		self.grid2wind.SetColLabelValue( 4, u"Id" )
		self.grid2wind.SetColLabelValue( 5, u"In \nService" )
		self.grid2wind.SetColLabelValue( 6, u"Tap\n Positions" )
		self.grid2wind.SetColLabelValue( 7, u"Specified \nR" )
		self.grid2wind.SetColLabelValue( 8, u"Specified \nX" )
		self.grid2wind.SetColLabelValue( 9, u"Rate A/B/C" )
		self.grid2wind.SetColLabelValue( 10, u"Wind 1 \nRatio" )
		self.grid2wind.SetColLabelValue( 11, u"Wind 1 \nNorminal" )
		self.grid2wind.SetColLabelValue( 12, u"R (table \ncorrected)" )
		self.grid2wind.SetColAttr(12, attr)
		self.grid2wind.SetColLabelValue( 13, u"X (table \ncorrected)" )
		self.grid2wind.SetColAttr(13, attr)
		self.grid2wind.SetColLabelValue( 14, u"Connection \nCode" )
		self.grid2wind.SetColLabelValue( 15, u"R01" )
		self.grid2wind.SetColLabelValue( 16, u"X01" )
		self.grid2wind.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		connectionCode2 = ['1','2','3','4','5','6','7','8','9','11','12','13','14','15','16','17','18','19','20','21','22']
		# connectionCode = [1,2,3,4,5,6,11,12,13,14,15,16,17,18]
		celChoice2 =wx.grid.GridCellChoiceEditor(connectionCode2,allowOthers=True)
		celChoice2.IncRef()
		for row1 in range(2500):
			self.grid2wind.SetCellEditor(row1,14,celChoice2)
		# Rows
		self.grid2wind.EnableDragRowSize( True )
		self.grid2wind.SetRowLabelSize( 50 )
		self.grid2wind.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.grid2wind.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.grid2wind.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.grid2wind.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.grid2wind.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer182.Add( self.grid2wind, 1, 0, 5 )
		
		
		self.twoWind.SetSizer( bSizer182 )
		self.twoWind.Layout()
		bSizer182.Fit( self.twoWind )
		self.m_notebook2.AddPage( self.twoWind, u"2 wind", False )
		self.threeWind = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer183 = wx.BoxSizer( wx.VERTICAL )
		
		self.grid3wind = wx.grid.Grid( self.threeWind, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		
		# Grid
		self.grid3wind.CreateGrid( 3000, 30 )
		self.grid3wind.EnableEditing( True )
		self.grid3wind.EnableGridLines( True )
		self.grid3wind.EnableDragGridSize( True )
		self.grid3wind.SetMargins( 0, 0 )
		
		# Columns
		self.grid3wind.SetColSize( 0, 60 )
		self.grid3wind.SetColAttr(0, attr)
		self.grid3wind.SetColSize( 1, 97 )
		self.grid3wind.SetColAttr(1, attr)
		self.grid3wind.SetColSize( 2, 60 )
		self.grid3wind.SetColAttr(2, attr)
		self.grid3wind.SetColSize( 3, 116 )
		self.grid3wind.SetColAttr(3, attr)
		self.grid3wind.SetColSize( 4, 60 )
		self.grid3wind.SetColAttr(4, attr)
		self.grid3wind.SetColSize( 5, 90 )
		self.grid3wind.SetColAttr(5, attr)
		self.grid3wind.SetColSize( 6, 120 )
		self.grid3wind.SetColSize( 7, 47 )
		self.grid3wind.SetColSize( 8, 50 )
		self.grid3wind.SetColSize( 9, 80 )
		self.grid3wind.SetColSize( 10, 80 )
		self.grid3wind.SetColSize( 11, 80 )
		self.grid3wind.SetColSize( 12, 80 )
		self.grid3wind.SetColSize( 13, 80 )
		self.grid3wind.SetColSize( 14, 80 )
		self.grid3wind.SetColSize( 15, 60 )
		self.grid3wind.SetColSize( 16, 60 )
		self.grid3wind.SetColSize( 17, 80 )
		self.grid3wind.SetColSize( 18, 80 )
		self.grid3wind.SetColSize( 19, 80 )
		self.grid3wind.SetColSize( 20, 80 )
		self.grid3wind.SetColSize( 21, 80 )
		self.grid3wind.SetColSize( 22, 80 )
		self.grid3wind.SetColSize( 23, 80 )
		self.grid3wind.SetColSize( 24, 80 )
		self.grid3wind.SetColSize( 25, 80 )
		self.grid3wind.SetColSize( 26, 80 )
		self.grid3wind.SetColSize( 27, 80 )
		self.grid3wind.SetColSize( 28, 80 )
		self.grid3wind.SetColSize( 29, 80 )
		self.grid3wind.EnableDragColMove( False )
		self.grid3wind.EnableDragColSize( True )
		self.grid3wind.SetColLabelSize( 30 )
		self.grid3wind.SetColLabelValue( 0, u"From Bus" )
		self.grid3wind.SetColLabelValue( 1, u"From Bus \nName" )
		self.grid3wind.SetColLabelValue( 2, u"To Bus" )
		self.grid3wind.SetColLabelValue( 3, u"To Bus \nName" )
		self.grid3wind.SetColLabelValue( 4, u"Last Bus \nNum" )
		self.grid3wind.SetColLabelValue( 5, u"Last Bus \nName" )
		self.grid3wind.SetColLabelValue( 6, u"Name" )
		self.grid3wind.SetColLabelValue( 7, u"Id" )
		self.grid3wind.SetColLabelValue( 8, u"In \nService" )
		self.grid3wind.SetColLabelValue( 9, u"W1-2 R" )
		self.grid3wind.SetColLabelValue( 10, u"W1-2 X" )
		self.grid3wind.SetColLabelValue( 11, u"W2-3 R" )
		self.grid3wind.SetColLabelValue( 12, u"W2-3 X" )
		self.grid3wind.SetColLabelValue( 13, u"W3-1 R" )
		self.grid3wind.SetColLabelValue( 14, u"W3-1 X" )
		self.grid3wind.SetColLabelValue( 15, u"Star Bus \nVoltage" )
		self.grid3wind.SetColLabelValue( 16, u"Star Bus \nAngle" )
		self.grid3wind.SetColLabelValue( 17, u"Connection \nCode" )
		self.grid3wind.SetColLabelValue( 18, u"R01" )
		self.grid3wind.SetColLabelValue( 19, u"X01" )
		self.grid3wind.SetColLabelValue( 20, u"R02" )
		self.grid3wind.SetColLabelValue( 21, u"X02" )
		self.grid3wind.SetColLabelValue( 22, u"R03" )
		self.grid3wind.SetColLabelValue( 23, u"X03" )
		self.grid3wind.SetColLabelValue( 24, u"Rate \n W1" )
		self.grid3wind.SetColLabelValue( 25, u"Rate \n W2" )
		self.grid3wind.SetColLabelValue( 26, u"Rate \n W3" )
		self.grid3wind.SetColLabelValue( 27, u"Ratio W1" )
		self.grid3wind.SetColLabelValue( 28, u"Ratio W2" )
		self.grid3wind.SetColLabelValue( 29, u"Ratio W3" )
		self.grid3wind.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		# connectionCode = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22]
		connectionCode = ['1','2','3','4','5','6','11','12','13','14','15','16','17','18']
		celChoice =wx.grid.GridCellChoiceEditor(connectionCode,allowOthers=True)
		celChoice.IncRef()
		for row1 in range(2500):
			self.grid3wind.SetCellEditor(row1,17,celChoice)
		# Rows
		self.grid3wind.EnableDragRowSize( True )
		self.grid3wind.SetRowLabelSize( 50 )
		self.grid3wind.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.grid3wind.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		self.grid3wind.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.grid3wind.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.grid3wind.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer183.Add( self.grid3wind, 1, 0, 5 )
		
		
		self.threeWind.SetSizer( bSizer183 )
		self.threeWind.Layout()
		bSizer183.Fit( self.threeWind )
		self.m_notebook2.AddPage( self.threeWind, u"3 wind", False )

		self.genPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.genPage.SetBackgroundColour( wx.Colour( 164, 244, 224 ) )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer181 = wx.BoxSizer( wx.VERTICAL )
		
		self.AddGen = wx.Button( self.genPage, wx.ID_ANY, u"  Add Generator  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AddGen.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer181.Add( self.AddGen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Apply1 = wx.Button( self.genPage, wx.ID_ANY, u"Check Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Apply1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer181.Add( self.Apply1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.checkDyr = wx.Button( self.genPage, wx.ID_ANY, u"Check Dynamic ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkDyr.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer181.Add( self.checkDyr, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		bSizer171.Add( bSizer181, 1, wx.EXPAND, 5 ) 

		gSizer10 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText17 = wx.StaticText( self.genPage, wx.ID_ANY, u"Search by:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gSizer10.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		bSizer37 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer10.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer10.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer10.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		self.m_staticText18 = wx.StaticText( self.genPage, wx.ID_ANY, u"Gen Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gSizer10.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		genNumChoices = []
		self.genNumber = wx.ComboBox( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, genNumChoices, wx.CB_SORT )
		gSizer10.Add( self.genNumber, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2 )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer10.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer10.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		self.m_staticText19 = wx.StaticText( self.genPage, wx.ID_ANY, u"Gen Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		gSizer10.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.genName = wx.ComboBox( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,[], 0 )
		self.genName.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		gSizer10.Add( self.genName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2)

		bSizer171.Add( gSizer10, 1, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer171.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer171.Add( bSizer36, 1, wx.EXPAND, 5 )
		gSizer9 = wx.GridSizer( 0, 5, 0, 0 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer9.Add( bSizer33, 1, wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self.genPage, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		gSizer9.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText13 = wx.StaticText( self.genPage, wx.ID_ANY, u"North", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		gSizer9.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.genPage, wx.ID_ANY, u"Central", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		gSizer9.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.genPage, wx.ID_ANY, u"South", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		gSizer9.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.genPage, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer9.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.totalLoad = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.totalLoad, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.loadNorth = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.loadNorth, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.loadCentral = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.loadCentral, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.loadSouth = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.loadSouth, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.genPage, wx.ID_ANY, u"Source", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gSizer9.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.totalSource = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.totalSource, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.sourceNorth = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.sourceNorth, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sourceCentral = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.sourceCentral, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sourceSouth = wx.TextCtrl( self.genPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.sourceSouth, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer171.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		bSizer14.Add( bSizer171, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid6 = wx.grid.Grid( self.genPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid6.CreateGrid( 3000, 33 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid6.SetColSize( 0, 60 )
		self.m_grid6.SetColSize( 1, 90 )
		self.m_grid6.SetColSize( 2, 40 )
		self.m_grid6.SetColSize( 3, 110 )
		self.m_grid6.SetColSize( 4, 40 )
		self.m_grid6.SetColSize( 5, 80 )
		self.m_grid6.SetColSize( 6, 80 )
		self.m_grid6.SetColSize( 7, 50 )
		self.m_grid6.SetColSize( 8, 50 )
		self.m_grid6.SetColSize( 9, 50 )
		self.m_grid6.SetColSize( 10, 50 )
		self.m_grid6.SetColSize( 11, 50 )
		self.m_grid6.SetColSize( 12, 50 )
		self.m_grid6.SetColSize( 13, 50 )
		self.m_grid6.SetColSize( 14, 50 )
		self.m_grid6.SetColSize( 15, 50 )
		self.m_grid6.SetColSize( 16, 90 )
		self.m_grid6.SetColSize( 17, 80 )
		self.m_grid6.SetColSize( 18, 90 )
		self.m_grid6.SetColSize( 19, 100 )
		self.m_grid6.SetColSize( 20, 80 )
		self.m_grid6.SetColSize( 21, 80 )
		self.m_grid6.SetColSize( 22, 80 )
		self.m_grid6.SetColSize( 23, 80 )
		self.m_grid6.SetColSize( 24, 80 )
		self.m_grid6.SetColSize( 25, 80 )
		self.m_grid6.SetColSize( 26, 80 )
		self.m_grid6.SetColSize( 27, 150 )
		self.m_grid6.SetColSize( 28, 150 )
		self.m_grid6.SetColSize( 29, 150 )
		self.m_grid6.SetColSize( 30, 150 )
		self.m_grid6.SetColSize( 31, 100 )
		self.m_grid6.SetColSize( 32, 100 )
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 50 )
		self.m_grid6.SetColLabelValue( 0, u"Machine\n ID" )
		self.m_grid6.SetColAttr(0, attr)
		self.m_grid6.SetColLabelValue( 1, u"Machine\n Name" )
		self.m_grid6.SetColAttr(1, attr)
		self.m_grid6.SetColLabelValue( 2, u"Area\n Num" )
		self.m_grid6.SetColAttr(2, attr)
		self.m_grid6.SetColLabelValue( 3, u"Area\n Name" )
		self.m_grid6.SetColAttr(3, attr)
		self.m_grid6.SetColLabelValue( 4, u"Zone\n Num" )
		self.m_grid6.SetColAttr(4, attr)
		self.m_grid6.SetColLabelValue( 5, u"Zone\n Name" )
		self.m_grid6.SetColAttr(5, attr)
		self.m_grid6.SetColLabelValue( 6, u"Machine ID" )#23
		self.m_grid6.SetColLabelValue( 7, u"Status" )#6
		self.m_grid6.SetColLabelValue( 8, u"Base KV" )#7
		self.m_grid6.SetColLabelValue( 9, u"Actual\n KV" )#8
		self.m_grid6.SetColAttr(9, attr)
		self.m_grid6.SetColLabelValue( 10, u"Vsched" ) #9
		self.m_grid6.SetColLabelValue( 11, u"Pgen" ) #10
		self.m_grid6.SetColLabelValue( 12, u"Pmax") #11
		self.m_grid6.SetColLabelValue( 13, u"Pgen(%)" )
		self.m_grid6.SetColAttr(13, attr)
		self.m_grid6.SetColLabelValue( 14, u"Qgen" )
		self.m_grid6.SetColLabelValue( 15, u"Qmax)" )
		self.m_grid6.SetColLabelValue( 16, u"Qgen(%)" )
		self.m_grid6.SetColAttr(16, attr)
		self.m_grid6.SetColLabelValue( 17, u"Cos ϕ" )
		self.m_grid6.SetColAttr(17, attr)
		self.m_grid6.SetColLabelValue( 18, u"MBASE" )
		self.m_grid6.SetColAttr(18, attr)
		self.m_grid6.SetColLabelValue( 19, u"SubTransient\n X" )
		self.m_grid6.SetColAttr(19, attr)
		self.m_grid6.SetColLabelValue( 20, u"Transient X" )
		self.m_grid6.SetColAttr(20, attr)
		self.m_grid6.SetColLabelValue( 21, u"Synch X" )
		self.m_grid6.SetColAttr(21, attr)
		self.m_grid6.SetColLabelValue( 22, u"Negative X" )
		self.m_grid6.SetColAttr(22, attr)
		self.m_grid6.SetColLabelValue( 23, u"Zero X" )
		self.m_grid6.SetColAttr(23, attr)
		self.m_grid6.SetColLabelValue( 24, u"X source" ) #24
		self.m_grid6.SetColLabelValue( 25, u"X source Dyr" ) #25
		self.m_grid6.SetColLabelValue( 26, u"Pgen/Pmax" ) #12
		self.m_grid6.SetColLabelValue( 27, u"" )
		self.m_grid6.SetColLabelValue( 28, u"Source Type" )
		self.m_grid6.SetColLabelValue( 29, u"Actual\n coefficient " )
		self.m_grid6.SetColLabelValue( 30, u"Correction\n coefficient" )
		self.m_grid6.SetColLabelValue( 31, u"" )
		self.m_grid6.SetColLabelValue( 32, u"" )

		sourceType = ["NGUON_BAC_TD","NGUON_BAC_NT","NGUONBAC_PV","NGUON_BAC_W","BTRUNBO_1931","NGUON_TRG_TD","NGUON_TRG_NT","NGUON_TRG_NK","NGUON_TRG_HN","NGUONTRG_PV","NGUONTRG_W","NGUONTRG_SK","TNGUYEN_1931","NGUON_NAM_TD","NGUON_NAM_NT","NGUON_NAM_NK","NGUON_NAM_HN","NGUONNAM_PV","NGUONNAM_W","NGUONNAM_SK","NGUONNAM_LNG","TANAMBO_1931","NITHUAN_1931","DMT_1632","DMT_NOI_1870"]
		for i in range(25):
			self.m_grid6.SetCellBackgroundColour(i, 28, wx.Colour( 131, 196, 235 ))
			self.m_grid6.SetCellBackgroundColour(i, 29, wx.Colour( 131, 196, 235 ) )
			self.m_grid6.SetCellBackgroundColour(i, 30,  wx.Colour( 131, 196, 235 ))
			self.m_grid6.SetCellValue(i,28, sourceType[i]  )
			self.m_grid6.SetCellFont(i,28, wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

		self.m_grid6.SetCellValue(0,31, 'APPLY CHANGE'  )
		self.m_grid6.SetCellBackgroundColour(0, 31, wx.CYAN)
		self.m_grid6.SetCellSize(27, 28, 12, 3)
		s = u"""
			Trong mùa mưa:
						Các nhà máy thủy điện phát tối đa trong cả chế độ MAX và MIN.
						Nút Swing Hòa Bình điều chỉnh hợp lý để tránh để công suất âm.
						Sau đó, điều chỉnh các nguồn còn lại theo thứ tự giá, trong đó 
						lưu ý giá của các nhà máy sẽ giảm tương đối theo thứ thự là:
						–>LNG (Tân Phước, Sơn Mỹ, Nhơn Trạch 3 4)
						–> Khí lô B (Kiên Giang, Ô Môn, Cà Mau)
						–> Cụm Phú Mỹ - Nhơn Trạch (do trộn LNG) 
						–> Khí CVX 
						–> NĐ than sử dụng than nhập khẩu
			Trong mùa khô:
						Tính với công suất thủy điện khoảng 70% trong chế độ MAX 
						và khoảng 50% trong chế độ MIN.
						Các nguồn NĐ than, khí (lô B, CVX) có thể chạy tối đa, 
						các nguồn còn lại điều chỉnh để phù hợp với tải.
			"""
		self.m_grid6.SetCellValue(27, 28,s)
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 50 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.m_grid6.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.m_grid6.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer151.Add( self.m_grid6, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer151, 5, wx.EXPAND, 5 )
		
		
		self.genPage.SetSizer( bSizer13 )
		self.genPage.Layout()
		bSizer13.Fit( self.genPage )
		self.m_notebook2.AddPage( self.genPage, u"Source", False )
		self.loadPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.loadPage.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText28 = wx.StaticText( self.loadPage, wx.ID_ANY, u"Scale Zone Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		self.m_staticText28.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer29.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.changePercentP = wx.RadioButton( self.loadPage, wx.ID_ANY, u"Change P(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.changePercentP.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer29.Add( self.changePercentP, 0, wx.ALL, 5 )
		
		self.change_delta_p = wx.RadioButton( self.loadPage, wx.ID_ANY, u"Change ∆P", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.change_delta_p.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer29.Add( self.change_delta_p, 0, wx.ALL, 5 )
		
		self.ChangeNew = wx.RadioButton( self.loadPage, wx.ID_ANY, u"New PLoad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ChangeNew.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer29.Add( self.ChangeNew, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl17 = wx.TextCtrl( self.loadPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl17, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.loadPage, wx.ID_ANY, u"Apply", wx.DefaultPosition,wx.Size(112,-1), 0 )
		self.m_button5.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer27.Add( self.m_button5, 0, wx.ALL, 5 )

		loadNumChoices = []
		self.loadNumber = wx.ComboBox( self.loadPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, loadNumChoices, wx.CB_SORT )
		bSizer27.Add( self.loadNumber, 0, wx.ALL, 2 )
		
		
		bSizer25.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		
		bSizer23.Add( bSizer25, 1, wx.EXPAND, 5 )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText29 = wx.StaticText( self.loadPage, wx.ID_ANY, u"Current Zone Params", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer32.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		gSizer8 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_staticText25 = wx.StaticText( self.loadPage, wx.ID_ANY, u"P-MW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer8.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText26 = wx.StaticText( self.loadPage, wx.ID_ANY, u"Q-MVAr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		self.m_staticText26.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer8.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticText27 = wx.StaticText( self.loadPage, wx.ID_ANY, u"Cos ϕ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		self.m_staticText27.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer8.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		self.P_value = wx.TextCtrl( self.loadPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.P_value, 0, wx.ALL, 5 )
		
		self.Q_Value = wx.TextCtrl( self.loadPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.Q_Value, 0, wx.ALL, 5 )
		
		self.Cos_Phi_Value = wx.TextCtrl( self.loadPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.Cos_Phi_Value, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( gSizer8, 3, wx.EXPAND, 5 )
		
		
		bSizer23.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.new_load = wx.Button( self.loadPage, wx.ID_ANY, u"New Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.new_load.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer28.Add( self.new_load, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 30 )
		
		
		bSizer23.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		
		bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		bSizer241 = wx.BoxSizer( wx.VERTICAL )
		
		self.gridLoad = wx.grid.Grid( self.loadPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gridLoad.CreateGrid( 4000, 15 )
		self.gridLoad.EnableEditing( True )
		self.gridLoad.EnableGridLines( True )
		self.gridLoad.EnableDragGridSize( False )
		self.gridLoad.SetMargins( 0, 0 )
		
		# Columns
		self.gridLoad.SetColSize( 0, 60 )
		self.gridLoad.SetColSize( 1, 80 )
		self.gridLoad.SetColSize( 2, 50 )
		self.gridLoad.SetColSize( 3, 110 )
		self.gridLoad.SetColSize( 4, 50 )
		self.gridLoad.SetColSize( 5, 80 )
		self.gridLoad.SetColSize( 6, 50 )
		self.gridLoad.SetColSize( 7, 50 )
		self.gridLoad.SetColSize( 8, 60 )
		self.gridLoad.SetColSize( 9, 60 )
		self.gridLoad.SetColSize( 10, 80 )
		self.gridLoad.SetColSize( 11, 80 )
		self.gridLoad.SetColSize( 12, 80 )
		self.gridLoad.SetColSize( 13, 80 )
		self.gridLoad.SetColSize( 14, 80 )
		self.gridLoad.EnableDragColMove( False )
		self.gridLoad.EnableDragColSize( True )
		self.gridLoad.SetColLabelSize( 50 )
		self.gridLoad.SetColLabelValue( 0, u"Load\n Number" )
		self.gridLoad.SetColAttr(0, attr)
		self.gridLoad.SetColLabelValue( 1, u"Name" )
		self.gridLoad.SetColAttr(1, attr)
		self.gridLoad.SetColLabelValue( 2, u"Area" )
		self.gridLoad.SetColLabelValue( 3, u"Area\n Name" )
		self.gridLoad.SetColAttr(3, attr)
		self.gridLoad.SetColLabelValue( 4, u"Zone" )
		self.gridLoad.SetColLabelValue( 5, u"Zone\n Name" )
		self.gridLoad.SetColAttr(5, attr)
		self.gridLoad.SetColLabelValue( 6, u"ID" )
		self.gridLoad.SetColLabelValue( 7, u"Status" )
		self.gridLoad.SetColLabelValue( 8, u"P" )
		self.gridLoad.SetColLabelValue( 9, u"Q" )
		self.gridLoad.SetColLabelValue( 10, u"Cos ϕ" )
		self.gridLoad.SetColAttr(10, attr)
		self.gridLoad.SetColLabelValue( 11, u"MVA" )
		self.gridLoad.SetColAttr(11, attr)

		self.gridLoad.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridLoad.EnableDragRowSize( True )
		self.gridLoad.SetRowLabelSize( 50 )
		self.gridLoad.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridLoad.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.gridLoad.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.gridLoad.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer241.Add( self.gridLoad, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer22.Add( bSizer241, 5, wx.EXPAND, 5 )
		
		
		self.loadPage.SetSizer( bSizer22 )
		self.loadPage.Layout()
		bSizer22.Fit( self.loadPage )
		self.m_notebook2.AddPage( self.loadPage, u"Load", False )
		self.shuntPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		shuntNumChoices = []
		self.shuntNumber = wx.ComboBox( self.shuntPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, shuntNumChoices, wx.CB_SORT )
		bSizer33.Add( self.shuntNumber, 0, wx.ALL, 2 )

		self.gridShunt = wx.grid.Grid( self.shuntPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gridShunt.CreateGrid( 1000, 13 )
		self.gridShunt.EnableEditing( True )
		self.gridShunt.EnableGridLines( True )
		self.gridShunt.EnableDragGridSize( False )
		self.gridShunt.SetMargins( 0, 0 )
		
		# Columns
		self.gridShunt.SetColSize( 0, 65 )
		self.gridShunt.SetColSize( 1, 60 )
		self.gridShunt.SetColSize( 2, 80 )
		self.gridShunt.SetColSize( 3, 40 )
		self.gridShunt.SetColSize( 4, 110 )
		self.gridShunt.SetColSize( 5, 40 )
		self.gridShunt.SetColSize( 6, 80 )
		self.gridShunt.SetColSize( 7, 40 )
		self.gridShunt.SetColSize( 8, 40 )
		self.gridShunt.SetColSize( 9, 50 )
		self.gridShunt.SetColSize( 10, 100 )
		self.gridShunt.SetColSize( 11, 70)
		self.gridShunt.SetColSize( 12, 70 )
		self.gridShunt.EnableDragColMove( False )
		self.gridShunt.EnableDragColSize( True )
		self.gridShunt.SetColLabelSize( 50 )
		self.gridShunt.SetColLabelValue( 0, u"Type" )
		self.gridShunt.SetColAttr(0, attr)
		self.gridShunt.SetColLabelValue( 1, u"Bus\n Number" )
		self.gridShunt.SetColAttr(1, attr)
		self.gridShunt.SetColLabelValue( 2, u"Bus\n Name" )
		self.gridShunt.SetColAttr(2, attr)
		self.gridShunt.SetColLabelValue( 3, u"Area" )
		self.gridShunt.SetColAttr(3, attr)
		self.gridShunt.SetColLabelValue( 4, u"Area Name" )
		self.gridShunt.SetColAttr(4, attr)
		self.gridShunt.SetColLabelValue( 5, u"Zone" )
		self.gridShunt.SetColAttr(5, attr)
		self.gridShunt.SetColLabelValue( 6, u"Zone Name" )
		self.gridShunt.SetColAttr(6, attr)
		self.gridShunt.SetColLabelValue( 7, u"ID" )
		self.gridShunt.SetColLabelValue( 8, u"Status" )
		self.gridShunt.SetColLabelValue( 9, u"U(kV)" )
		self.gridShunt.SetColAttr(9, attr)
		self.gridShunt.SetColLabelValue( 10, u"GB Actual\n (MVAr)" )
		self.gridShunt.SetColAttr(10, attr)
		self.gridShunt.SetColLabelValue( 11, u"GB Nom\n (MVAr)" )
		self.gridShunt.SetColLabelValue( 12, u"GB Zero\n (MVAr)" )
		self.gridShunt.SetColAttr(12, attr)
		self.gridShunt.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridShunt.EnableDragRowSize( True )
		self.gridShunt.SetRowLabelSize( 50 )
		self.gridShunt.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridShunt.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.gridShunt.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.gridShunt.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer33.Add( self.gridShunt, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.shuntPage.SetSizer( bSizer33 )
		self.shuntPage.Layout()
		bSizer33.Fit( self.shuntPage )
		self.m_notebook2.AddPage( self.shuntPage, u"Shunt", False )

		self.dynamicPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
				
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		gSizer8 = wx.GridSizer( 0, 4, 0, 0 )
		self.LoadDynFile = wx.Button( self.dynamicPage, wx.ID_ANY, u"Load Dyr File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LoadDynFile.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		gSizer8.Add( self.LoadDynFile, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.SetRestriction = wx.CheckBox( self.dynamicPage, wx.ID_ANY, u"Set Restriction", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.SetRestriction, 0, wx.ALL, 5 )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		gSizer8.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		gSizer8.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self.dynamicPage, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer8.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.search_dyn = wx.ComboBox( self.dynamicPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,[], 0 )
		gSizer8.Add( self.search_dyn, 0, wx.ALL, 5 )

		bSizer35.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		bSizer30.Add( bSizer35, 1, wx.EXPAND, 5 )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.SaveDynFile = wx.Button( self.dynamicPage, wx.ID_ANY, u"Save Dyr File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SaveDynFile.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer36.Add( self.SaveDynFile, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		bSizer30.Add( bSizer36, 1,  wx.RIGHT, 5 )


		bSizer34.Add( bSizer30, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.gridDyn = wx.grid.Grid( self.dynamicPage, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gridDyn.CreateGrid( 20000, 100 )
		self.gridDyn.EnableEditing( True )
		self.gridDyn.EnableGridLines( True )
		self.gridDyn.EnableDragGridSize( False )
		self.gridDyn.SetMargins( 0, 0 )

		self.gridDyn.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridDyn.EnableDragRowSize( True )
		self.gridDyn.SetRowLabelSize( 50 )
		self.gridDyn.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.gridDyn.SetLabelFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		# Cell Defaults
		self.gridDyn.SetDefaultCellFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.gridDyn.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		for i in range(15000):
			if i%2==0:
				self.gridDyn.SetRowAttr(i, attr)
		bSizer34.Add( self.gridDyn, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.dynamicPage.SetSizer( bSizer34 )
		self.dynamicPage.Layout()
		bSizer34.Fit( self.dynamicPage )
		self.m_notebook2.AddPage( self.dynamicPage, u"Dynamic", False )

		self.configure_page = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer321 = wx.BoxSizer( wx.VERTICAL )
		self.m_panel11 = wx.Panel( self.configure_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer322 = wx.BoxSizer( wx.VERTICAL )
		self.m_staticText281 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Choose the way to update data:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )
		bSizer322.Add( self.m_staticText281, 0, wx.ALL, 5 )
		
		self.updateDirect = wx.RadioButton( self.m_panel11, wx.ID_ANY, u"Update step by step", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer322.Add( self.updateDirect, 0, wx.ALL, 5 )
		
		self.UpdatedLater = wx.RadioButton( self.m_panel11, wx.ID_ANY, u"Update Later (Ctrl+R)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UpdatedLater.SetValue( True )
		bSizer322.Add( self.UpdatedLater, 0, wx.ALL, 5 )
		self.m_panel11.SetSizer( bSizer322 )
		self.m_panel11.Layout()
		bSizer322.Fit( self.m_panel11 )
		bSizer321.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self.configure_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer323 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText282 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Update change:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText282.Wrap( -1 )
		bSizer323.Add( self.m_staticText282, 0, wx.ALL, 5 )
		
		self.UpdateSynch = wx.RadioButton( self.m_panel12, wx.ID_ANY, u"Synchronous changes of files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer323.Add( self.UpdateSynch, 0, wx.ALL, 5 )
		
		self.UpdatedIndividual = wx.RadioButton( self.m_panel12, wx.ID_ANY, u"Change each file individually", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer323.Add( self.UpdatedIndividual, 0, wx.ALL, 5 )

		self.m_panel12.SetSizer( bSizer323 )
		self.m_panel12.Layout()
		bSizer323.Fit( self.m_panel12 )
		bSizer321.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel13 = wx.Panel( self.configure_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer324 = wx.BoxSizer( wx.VERTICAL )
		self.m_staticText283 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Create Macro:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText283.Wrap( -1 )
		bSizer324.Add( self.m_staticText283, 0, wx.ALL, 5 )
		
		self.CreateMacro = wx.RadioButton( self.m_panel13, wx.ID_ANY, u"Create macro file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer324.Add( self.CreateMacro, 0, wx.ALL, 5 )

		self.FinishRecord = wx.RadioButton( self.m_panel13, wx.ID_ANY, u"Stop recording", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer324.Add( self.FinishRecord, 0, wx.ALL, 5 )

		self.m_panel13.SetSizer( bSizer324 )
		self.m_panel13.Layout()
		bSizer324.Fit( self.m_panel13 )
		bSizer321.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel14 = wx.Panel( self.configure_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer325 = wx.BoxSizer( wx.VERTICAL )
		self.m_staticText284 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Power flow:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText284.Wrap( -1 )
		bSizer325.Add( self.m_staticText284, 0, wx.ALL, 5 )

		self.PowerFlowRefresh = wx.Button( self.m_panel14, wx.ID_ANY, u"Calculate Power Flow and Refresh Grids", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer325.Add( self.PowerFlowRefresh, 0, wx.ALL, 5 )

		self.m_panel14.SetSizer( bSizer325 )
		self.m_panel14.Layout()
		bSizer325.Fit( self.m_panel14 )
		bSizer321.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel15 = wx.Panel( self.configure_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer321.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel16 = wx.Panel( self.configure_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer321.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel17 = wx.Panel( self.configure_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer321.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		self.configure_page.SetSizer( bSizer321 )
		self.configure_page.Layout()
		bSizer321.Fit( self.configure_page )
		self.m_notebook2.AddPage( self.configure_page, u"Configuration", False )
		
		self.m_mainSplitter.SplitVertically( self.m_splitter4, self.m_notebook2, 540 )
		bSizer5.Add( self.m_mainSplitter, 1, wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.Bind( wx.EVT_MENU, self.Open_PSSE, id = self.Open_PSSE_File.GetId() )
		self.Bind( wx.EVT_MENU, self.Open_Multiple_PSSE, id = self.Open_Multiple_PSSE_File.GetId() )
		self.Bind( wx.EVT_MENU, self.Close_PSSE_Fcn, id = self.Close_PSSE_File.GetId() )
		self.Bind( wx.EVT_MENU, self.Save_PSSE, id = self.Save_PSSE_File.GetId() )
		self.Bind( wx.EVT_MENU, self.Save_All_PSSE, id = self.Save_All_PSSE_Files.GetId() )
		self.Bind( wx.EVT_MENU, self.Save_As_Fcn, id = self.Save_PSSE_File_As.GetId() )
		self.Bind( wx.EVT_MENU, self.Close_PSSE, id = self.Close_PSSE_Case.GetId() )
		self.Bind( wx.EVT_MENU, self.Export_Cad, id = self.Export_to_Cad.GetId() )
		self.Bind( wx.EVT_MENU, self.Export_Cad_MVA, id = self.Export_to_Cad_MVA.GetId() )
		self.Bind( wx.EVT_MENU, self.Export_Cad_Load_Percent, id = self.Export_to_Cad_Load_Percent.GetId() )
		self.Bind( wx.EVT_MENU, self.Export_Multi_Cad, id = self.Export_to_Multi_Cad.GetId() )
		self.Bind( wx.EVT_MENU, self.Export_Excel, id = self.Export_to_Excel.GetId() )
		self.Bind( wx.EVT_MENU, self.Export_Dyn, id = self.Export_to_Dyn.GetId() )
		self.Bind( wx.EVT_MENU, self.Add_New_Bus, id = self.New_Bus.GetId() )
		self.Bind( wx.EVT_MENU, self.Turn_On_Off, id = self.Turn_On_Off_Bus.GetId() )
		self.Bind( wx.EVT_MENU, self.Split_Bus_Fcn, id = self.Split_Bus.GetId() )
		self.Bind( wx.EVT_MENU, self.Joint_Bus_Fcn, id = self.Joint_Bus.GetId() )
		self.Bind( wx.EVT_MENU, self.Line_Tap_Fcn, id = self.Line_Tap.GetId() ) 
		self.Bind( wx.EVT_MENU, self.Run_Macro_Fcn, id = self.Run_Macro.GetId() )
		# self.Bind( wx.EVT_MENU, self.Run_Multi_Macro_Fcn, id = self.Run_Multi_Macro.GetId() )
		self.Bind( wx.EVT_MENU, self.Delete_Bus_Fcn, id = self.Delete_Bus.GetId() )
		self.Bind( wx.EVT_MENU, self.Add_Gen_Fcn, id = self.Add_Gen.GetId() )
		self.Bind( wx.EVT_MENU, self.Add_Branch_Fcn, id = self.Add_Branch.GetId() )
		self.Bind( wx.EVT_MENU, self.Add_3Winding_Fcn, id = self.Add_3Winding.GetId() )
		self.Bind( wx.EVT_MENU, self.Add_2Winding_Fcn, id = self.Add_2Winding.GetId() )
		self.Bind( wx.EVT_MENU, self.Add_Load_Fcn, id = self.Add_Load.GetId() )
		self.Bind( wx.EVT_MENU, self.Add_Shunt_Fcn, id = self.Add_Shunt.GetId() )
		self.Bind( wx.EVT_MENU, self.Change_Zone_Source_Fcn, id = self.Change_Zone_Source.GetId() )
		self.Bind( wx.EVT_MENU, self.Change_Area_Source_Fcn, id = self.Change_Area_Source.GetId() )
		self.Bind( wx.EVT_MENU, self.View_PSSE_Fcn, id = self.View_PSSE.GetId() )
		self.Bind( wx.EVT_MENU, self.View_Database_Fcn, id = self.View_Database.GetId() )
		self.Bind( wx.EVT_MENU, self.Minimize_Fcn, id = self.Minimize.GetId() )
		self.Bind( wx.EVT_MENU, self.Reload_Fcn, id = self.Reload.GetId() )
		self.Bind( wx.EVT_MENU, self.Power_Flow_Selected_Cal_Fcn, id = self.Power_Flow_Selected_Case.GetId() )
		self.Bind( wx.EVT_MENU, self.Power_Flow_Cal_Fcn, id = self.Power_Flow.GetId() )
		self.Bind( wx.EVT_MENU, self.Choose_Available_DFX_Fcn, id = self.Choose_Available_DFX.GetId() )
		self.Bind( wx.EVT_MENU, self.Create_New_DFX_Fcn, id = self.Create_New_DFX.GetId() )
		self.Bind( wx.EVT_MENU, self.Auto_Contigencies_Fcn, id = self.Auto_Contigencies.GetId() )
		self.Bind( wx.EVT_MENU, self.Distribution_Short_Circuit_Cal_Fcn, id = self.Distribution_Short_Circuit.GetId() )
		self.Bind( wx.EVT_MENU, self.Distribution_Short_Circuit_From_File_Fcn, id = self.Distribution_Short_Circuit_From_File.GetId() )
		self.Bind( wx.EVT_MENU, self.Short_Circuit_Cal_New_Fcn, id = self.Short_Circuit_Cal_New.GetId() )
		self.Bind( wx.EVT_MENU, self.Short_Circuit_Cal_From_File_Fcn, id = self.Short_Circuit_Cal_From_File.GetId() )
		self.Bind( wx.EVT_MENU, self.Short_Circuit_Cal_All_Cases_Fcn_Export_Word, id = self.Short_Circuit_Cal_All_Cases_Export_Word.GetId() )
		self.Bind( wx.EVT_MENU, self.Short_Circuit_Cal_All_Cases_Fcn_Export_Txt, id = self.Short_Circuit_Cal_All_Cases_Export_Txt.GetId() )
		self.Bind( wx.EVT_MENU, self.Static_Stability_Cal_Selected_Case_Fcn, id = self.Static_Stability_Cal_Selected_Case.GetId() )
		self.Bind( wx.EVT_MENU, self.Auto_Static_Stability_Cal_Fcn, id = self.Auto_Static_Stability_Cal.GetId() )
		self.Bind( wx.EVT_MENU, self.Dynamic_Stability_Cal_Fcn, id = self.Dynamic_Stability_Cal_From_IDV_File.GetId() )
		self.Bind( wx.EVT_MENU, self.Dynamic_Stability_Cal_By_Create_New_IDV_Fcn, id = self.Dynamic_Stability_Cal_By_Create_New_IDV.GetId() )
		self.Bind( wx.EVT_MENU, self.Shunt_Reactor_Cal_Fcn, id = self.Shunt_Reactor_Cal.GetId() )
		self.Bind( wx.EVT_MENU, self.InterRegionLimit, id = self.PV_Cal.GetId() )
		self.Bind( wx.EVT_MENU, self.Help_Fcn, id = self.Version.GetId() )
		self.Bind( wx.EVT_MENU, self.Shortcut_Fcn, id = self.Shortcut.GetId() )
		self.gridFile.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_file )
		self.gridFile.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_file )
		self.gridFile.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_file )
		self.gridFile.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_file )
		self.gridArea.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_area )
		self.gridArea.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_area )
		self.gridArea.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_area )
		self.gridArea.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_area )
		self.gridZone.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_zone )
		self.gridZone.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_zone )
		self.gridZone.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_zone )
		self.gridZone.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_zone )
		self.BusNumInput.Bind( wx.EVT_TEXT, self.busNumberEnter_Fcn )
		self.filter_selection.Bind( wx.EVT_CHOICE, self.OnChoice )
		self.filter_input_text.Bind( wx.EVT_TEXT, self.OnTextSearch )
		self.gridBusInfo.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_bus )
		self.gridBusInfo.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_bus )
		self.gridBusInfo.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_bus )
		self.gridBusInfo.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_bus )
		self.gridSearch.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_search )
		self.gridSearch.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_search )
		self.gridSearch.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_search )
		self.gridSearch.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_search )
		self.AddGen.Bind( wx.EVT_BUTTON, self.add_gen_fcn )
		self.genNumber.Bind( wx.EVT_TEXT, self.genNumberEnter_Fcn )
		self.genName.Bind( wx.EVT_TEXT, self.genNameEnter_Fcn )
		self.loadNumber.Bind( wx.EVT_TEXT, self.loadNumberEnter_Fcn )
		self.shuntNumber.Bind( wx.EVT_TEXT, self.shuntNumberEnter_Fcn )
		self.search_dyn.Bind( wx.EVT_TEXT, self.dynNumberEnter_Fcn )
		self.Apply1.Bind( wx.EVT_BUTTON, self.checkDatabase_fcn ) 
		self.checkDyr.Bind( wx.EVT_BUTTON, self.checkDyr_fcn )
		self.m_button5.Bind(wx.EVT_BUTTON, self.scale_zone_load )
		self.m_grid6.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_source )
		self.m_grid6.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_source )
		self.m_grid6.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_source )
		self.m_grid6.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_source )
		self.changePercentP.Bind( wx.EVT_RADIOBUTTON, self.change_percent_p_fcn )
		self.change_delta_p.Bind( wx.EVT_RADIOBUTTON, self.change_delta_p_fcn )
		self.ChangeNew.Bind( wx.EVT_RADIOBUTTON, self.change_new_fcn )
		self.new_load.Bind( wx.EVT_BUTTON, self.load_new_fcn )
		self.gridLoad.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_load )
		self.gridLoad.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_load )
		self.gridLoad.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_load )
		self.gridLoad.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_load )
		self.gridShunt.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_shunt )
		self.gridShunt.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_shunt )
		self.gridShunt.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_shunt )
		self.gridShunt.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_shunt )
		self.gridDyn.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_dyn )
		self.gridDyn.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_dyn )
		self.gridDyn.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_dyn )
		self.gridDyn.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_dyn )
		self.LoadDynFile.Bind(wx.EVT_BUTTON, self.Load_Dyr_File )
		self.SaveDynFile.Bind(wx.EVT_BUTTON, self.Save_Dyr_File )
		self.updateDirect.Bind( wx.EVT_RADIOBUTTON, self.onUpdatedStepByStep )
		self.UpdatedLater.Bind( wx.EVT_RADIOBUTTON, self.onUpdatedLater )
		self.PowerFlowRefresh.Bind( wx.EVT_BUTTON, self.Power_Flow_Refresh_Fcn )
		self.UpdateSynch.Bind( wx.EVT_RADIOBUTTON, self.onUpdateSynch )
		self.UpdatedIndividual.Bind( wx.EVT_RADIOBUTTON, self.onUpdateIndividual )
		self.CreateMacro.Bind( wx.EVT_RADIOBUTTON, self.onCreateMacro )
		self.FinishRecord.Bind( wx.EVT_RADIOBUTTON, self.onFinishRecord )
		self.SetRestriction.Bind( wx.EVT_CHECKBOX, self.onSetRestriction )
		self.m_tool0.Bind( wx.EVT_BUTTON, self.Power_Flow_Refresh_Fcn )
		self.m_tool1.Bind( wx.EVT_BUTTON, self.Auto_Contingency )
		self.m_toolN1.Bind( wx.EVT_BUTTON, self.Create_N1_SAV_Files )
		self.m_tool2.Bind( wx.EVT_BUTTON, self.Export_Multiple_Cad )
		self.m_tool4.Bind( wx.EVT_TOGGLEBUTTON, self.Record_Automation )
		self.grid2wind.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_2wind )
		self.grid2wind.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_2wind )
		self.grid2wind.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_2wind )
		self.grid2wind.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_2wind )
		self.grid3wind.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change_grid_3wind )
		self.grid3wind.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_grid_3wind )
		self.grid3wind.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_selected_cell_grid_3wind )
		self.grid3wind.Bind( wx.EVT_KEY_DOWN, self.on_key_down_grid_3wind )

	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onClose( self, event ):
		event.Skip()

	def Open_PSSE( self, event ):
		event.Skip()
	
	def Open_Multiple_PSSE( self, event ):
		event.Skip()

	def Close_PSSE_Fcn( self, event ):
		event.Skip()

	def Save_PSSE( self, event ):
		event.Skip()

	def Save_All_PSSE( self, event ):
		event.Skip()
	
	def Save_As_Fcn( self, event ):
		event.Skip()
	
	def Close_PSSE( self, event ):
		event.Skip()
	
	def Export_Cad( self, event ):
		event.Skip()
	
	def Export_Cad_MVA( self, event ):
		event.Skip()

	def Export_Cad_Load_Percent( self, event ):
		event.Skip()

	def Export_Multi_Cad( self, event ):
		event.Skip()

	def Export_Excel( self, event ):
		event.Skip()
	
	def Export_Dyn( self, event ):
		event.Skip()
	
	def Add_New_Bus( self, event ):
		event.Skip()
	
	def Turn_On_Off( self, event ):
		event.Skip()
	
	def Split_Bus_Fcn( self, event ):
		event.Skip()
	
	def Joint_Bus_Fcn( self, event ):
		event.Skip()
	
	def Line_Tap_Fcn( self, event ):
		event.Skip()
	
	def Run_Macro_Fcn( self, event ):
		event.Skip()

	# def Run_Multi_Macro_Fcn( self, event ):
	# 	event.Skip()

	def Delete_Bus_Fcn( self, event ):
		event.Skip()
	
	def Add_Gen_Fcn( self, event ):
		event.Skip()
	
	def Add_Branch_Fcn( self, event ):
		event.Skip()
	
	def Add_3Winding_Fcn( self, event ):
		event.Skip()
	
	def Add_2Winding_Fcn( self, event ):
		event.Skip()
	
	def Add_Load_Fcn( self, event ):
		event.Skip()

	def Add_Shunt_Fcn( self, event ):
		event.Skip()
	
	def Change_Zone_Source_Fcn( self, event ):
		event.Skip()

	def Change_Area_Source_Fcn( self, event ):
		event.Skip()
	
	def View_PSSE_Fcn( self, event ):
		event.Skip()
	
	def View_Database_Fcn( self, event ):
		event.Skip()

	def Reload_Fcn( self, event ):
		event.Skip()
	
	def Minimize_Fcn( self, event ):
		event.Skip()
	
	def Power_Flow_Cal_Fcn( self, event ):
		event.Skip()
	
	def Power_Flow_Selected_Cal_Fcn( self, event ):
		event.Skip()

	def Create_New_DFX_Fcn( self, event ):
		event.Skip()

	def Choose_Available_DFX_Fcn( self, event ):
		event.Skip()
	
	def Auto_Contigencies_Fcn(self, event):
		event.Skip()

	def Distribution_Short_Circuit_Cal_Fcn(self,event):
		event.Skip()

	def Distribution_Short_Circuit_From_File_Fcn(self,event):
		event.Skip()

	def Short_Circuit_Cal_New_Fcn( self, event ):
		event.Skip()

	def Short_Circuit_Cal_From_File_Fcn( self, event ):
		event.Skip()
	
	def Short_Circuit_Cal_All_Cases_Fcn_Export_Word(self, event ):
		event.Skip()

	def Short_Circuit_Cal_All_Cases_Fcn_Export_Txt(self, event ):
		event.Skip()

	def Static_Stability_Cal_Selected_Case_Fcn(self,event):
		event.Skip()

	def Auto_Static_Stability_Cal_Fcn( self, event ):
		event.Skip()
	
	def Dynamic_Stability_Cal_Fcn( self, event ):
		event.Skip()
	
	def Dynamic_Stability_Cal_By_Create_New_IDV_Fcn(self,event):
		event.Skip()

	def Shunt_Reactor_Cal_Fcn(self,event):
		event.Skip()

	def Help_Fcn( self, event ):
		event.Skip()

	def Shortcut_Fcn(self, event):
		event.Skip()
	
	def on_cell_change_grid_file( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_file( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_file( self, event ):
		event.Skip()
	
	def on_key_down_grid_file( self, event ):
		event.Skip()
	
	def on_cell_change_grid_area( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_area( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_area( self, event ):
		event.Skip()
	
	def on_key_down_grid_area( self, event ):
		event.Skip()
	
	def on_cell_change_grid_zone( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_zone( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_zone( self, event ):
		event.Skip()
	
	def on_key_down_grid_zone( self, event ):
		event.Skip()
	
	def busNumberEnter_Fcn( self, event ):
		event.Skip()
	
	def OnChoice( self, event ):
		event.Skip()
	
	def OnTextSearch( self, event ):
		event.Skip()
	
	def on_cell_change_grid_bus( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_bus( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_bus( self, event ):
		event.Skip()
	
	def on_key_down_grid_bus( self, event ):
		event.Skip()
	
	def on_cell_change_grid_search( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_search( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_search( self, event ):
		event.Skip()
	
	def on_key_down_grid_search( self, event ):
		event.Skip()
	
	def add_gen_fcn( self, event ):
		event.Skip()

	def checkDatabase_fcn( self,event):
		event.Skip()

	def checkDyr_fcn(self,event):
		event.Skip()

	def genNumberEnter_Fcn(self,event):
		event.Skip()
	
	def genNameEnter_Fcn(self, event):
		event.Skip()

	def onKeyDownGenNumber(self,event):
		event.Skip()

	def onKeyDownGenName(self,event):
		event.Skip()

	def loadNumberEnter_Fcn(self,event):
		event.Skip()

	def shuntNumberEnter_Fcn(self, event):
		event.Skip()

	def dynNumberEnter_Fcn(self,event):
		event.Skip()

	def on_cell_change_grid_source( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_source( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_source( self, event ):
		event.Skip()
	
	def on_key_down_grid_source( self, event ):
		event.Skip()
	
	def change_percent_p_fcn( self, event ):
		event.Skip()
	
	def change_delta_p_fcn( self, event ):
		event.Skip()
	
	def change_new_fcn( self, event ):
		event.Skip()

	def load_new_fcn( self, event ):
		event.Skip()
	
	def on_cell_change_grid_load( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_load( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_load( self, event ):
		event.Skip()
	
	def on_key_down_grid_load( self, event ):
		event.Skip()

	def on_cell_change_grid_shunt( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_shunt( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_shunt( self, event ):
		event.Skip()
	
	def on_key_down_grid_shunt( self, event ):
		event.Skip()
	
	def on_cell_change_grid_dyn( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_dyn( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_dyn( self, event ):
		event.Skip()
	
	def on_key_down_grid_dyn( self, event ):
		event.Skip()

	def Load_Dyr_File(self,event):
		event.Skip()

	def onSetRestriction(self,event):
		event.Skip()

	def Save_Dyr_File(self,event):
		event.Skip()

	def onUpdatedStepByStep( self, event ):
		event.Skip()
	
	def onUpdatedLater( self, event ):
		event.Skip()

	def Power_Flow_Refresh_Fcn( self, event ):
		event.Skip()
	
	def onUpdateSynch(self,event):
		event.Skip()

	def onUpdateIndividual(self,event):
		event.Skip()

	def	onCreateMacro(self,event):
		event.Skip()

	def	onFinishRecord(self,event):
		event.Skip()

	def scale_zone_load( self,event):
		event.Skip()

	def InterRegionLimit(self,event):
		event.Skip()

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 0 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )

	def m_splitter4OnIdle( self, event ):
		height = self.m_splitter4.GetClientSize().GetHeight()
		self.m_splitter4.SetSashPosition( int( height * 0.67 ) )
		self.m_splitter4.Unbind( wx.EVT_IDLE )
	
	def m_splitter41OnIdle( self, event ):
		self.m_splitter41.SetSashPosition( 0 )
		self.m_splitter41.Unbind( wx.EVT_IDLE )

	def m_splitter21OnIdle( self, event ):
		height = self.m_splitter21.GetClientSize().GetHeight()
		self.m_splitter21.SetSashPosition( int( height * 0.5 ) )
		self.m_splitter21.Unbind( wx.EVT_IDLE )

	def Auto_Contingency( self, event ):
		event.Skip()

	def Create_N1_SAV_Files( self, event ):
		event.Skip()
	
	def Export_Multiple_Cad( self, event ):
		event.Skip()
	
	def Short_Circuit_All_File( self, event ):
		event.Skip()

	def Record_Automation( self, event ):
		event.Skip()

	def on_cell_change_grid_2wind( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_2wind( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_2wind( self, event ):
		event.Skip()

	def on_key_down_grid_2wind( self, event ):
		event.Skip()

	def on_cell_change_grid_3wind( self, event ):
		event.Skip()
	
	def on_cell_right_click_grid_3wind( self, event ):
		event.Skip()
	
	def on_selected_cell_grid_3wind( self, event ):
		event.Skip()

	def on_key_down_grid_3wind( self, event ):
		event.Skip()

# if __name__ == "__main__":
#	 app = wx.App(False)
#	 frame = MyFrame1(None)
#	 frame.Show(True)
#	 app.MainLoop()
