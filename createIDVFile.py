# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from DialogBox import openFile,openFolder
from Create_Sub_Mon_Con_Files import createIDVFile,createIncidentFile
import glob, os, sys
from redirectOuput import silence
from subprocess import call
import pssepath
import dyntools
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 

###########################################################################
## Class MyFrame2
###########################################################################

class Create_New_Idv ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title =  u"Create new Idv files", pos = wx.DefaultPosition, size = wx.Size( 600,574 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"File Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer6.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_textCtrl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Load Dyr File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Observe Channels", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox3Choices = []
		self.m_listBox3 = wx.ListBox( self.m_panel1, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox3Choices)
		gSizer21.Add( self.m_listBox3, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self.m_panel1, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox4Choices)
		gSizer21.Add( self.m_listBox4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer131.Add( gSizer21, 5, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button6 = wx.Button( self.m_panel1, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self.m_panel1, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button8 = wx.Button( self.m_panel1, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button8, 0, wx.ALL, 5 )
		
		
		bSizer131.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer131 )
		self.m_panel1.Layout()
		bSizer131.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"ANGLE", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1311 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer211 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox31Choices = []
		self.m_listBox31 = wx.ListBox( self.m_panel2, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox31Choices )
		gSizer211.Add( self.m_listBox31, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox41Choices = []
		self.m_listBox41 = wx.ListBox( self.m_panel2,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox41Choices )
		gSizer211.Add( self.m_listBox41, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1311.Add( gSizer211, 5, wx.EXPAND, 5 )
		
		gSizer31 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button51 = wx.Button( self.m_panel2, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button61 = wx.Button( self.m_panel2, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_button61, 0, wx.ALL, 5 )
		
		self.m_button71 = wx.Button( self.m_panel2, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_button71, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button81 = wx.Button( self.m_panel2, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_button81, 0, wx.ALL, 5 )
		
		
		bSizer1311.Add( gSizer31, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer1311 )
		self.m_panel2.Layout()
		bSizer1311.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"PELEC", False )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1312 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer212 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox32Choices = []
		self.m_listBox32 = wx.ListBox( self.m_panel3,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox32Choices )
		gSizer212.Add( self.m_listBox32, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox42Choices = []
		self.m_listBox42 = wx.ListBox( self.m_panel3,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox42Choices)
		gSizer212.Add( self.m_listBox42, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1312.Add( gSizer212, 5, wx.EXPAND, 5 )
		
		gSizer32 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button52 = wx.Button( self.m_panel3, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_button52, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button62 = wx.Button( self.m_panel3, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_button62, 0, wx.ALL, 5 )
		
		self.m_button72 = wx.Button( self.m_panel3, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_button72, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button82 = wx.Button( self.m_panel3, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer32.Add( self.m_button82, 0, wx.ALL, 5 )
		
		
		bSizer1312.Add( gSizer32, 1, wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer1312 )
		self.m_panel3.Layout()
		bSizer1312.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"QELEC", False )
		self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1313 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer213 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox33Choices = []
		self.m_listBox33 = wx.ListBox( self.m_panel4,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox33Choices)
		gSizer213.Add( self.m_listBox33, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox43Choices = []
		self.m_listBox43 = wx.ListBox( self.m_panel4,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox43Choices)
		gSizer213.Add( self.m_listBox43, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1313.Add( gSizer213, 5, wx.EXPAND, 5 )
		
		gSizer33 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button53 = wx.Button( self.m_panel4, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer33.Add( self.m_button53, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button63 = wx.Button( self.m_panel4, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer33.Add( self.m_button63, 0, wx.ALL, 5 )
		
		self.m_button73 = wx.Button( self.m_panel4, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer33.Add( self.m_button73, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button83 = wx.Button( self.m_panel4, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer33.Add( self.m_button83, 0, wx.ALL, 5 )
		
		
		bSizer1313.Add( gSizer33, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer1313 )
		self.m_panel4.Layout()
		bSizer1313.Fit( self.m_panel4 )
		self.m_notebook1.AddPage( self.m_panel4, u"ETERM", False )
		self.m_panel5 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1314 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer214 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox34Choices = []
		self.m_listBox34 = wx.ListBox( self.m_panel5, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox34Choices)
		gSizer214.Add( self.m_listBox34, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox44Choices = []
		self.m_listBox44 = wx.ListBox( self.m_panel5, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox44Choices)
		gSizer214.Add( self.m_listBox44, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1314.Add( gSizer214, 5, wx.EXPAND, 5 )
		
		gSizer34 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button54 = wx.Button( self.m_panel5, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer34.Add( self.m_button54, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button64 = wx.Button( self.m_panel5, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer34.Add( self.m_button64, 0, wx.ALL, 5 )
		
		self.m_button74 = wx.Button( self.m_panel5, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer34.Add( self.m_button74, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button84 = wx.Button( self.m_panel5, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer34.Add( self.m_button84, 0, wx.ALL, 5 )
		
		
		bSizer1314.Add( gSizer34, 1, wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( bSizer1314 )
		self.m_panel5.Layout()
		bSizer1314.Fit( self.m_panel5 )
		self.m_notebook1.AddPage( self.m_panel5, u"EFD", False )
		self.m_panel6 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1315 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer215 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox35Choices = []
		self.m_listBox35 = wx.ListBox( self.m_panel6, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox35Choices)
		gSizer215.Add( self.m_listBox35, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox45Choices = []
		self.m_listBox45 = wx.ListBox( self.m_panel6,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox45Choices)
		gSizer215.Add( self.m_listBox45, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1315.Add( gSizer215, 5, wx.EXPAND, 5 )
		
		gSizer35 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button55 = wx.Button( self.m_panel6, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer35.Add( self.m_button55, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button65 = wx.Button( self.m_panel6, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer35.Add( self.m_button65, 0, wx.ALL, 5 )
		
		self.m_button75 = wx.Button( self.m_panel6, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer35.Add( self.m_button75, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button85 = wx.Button( self.m_panel6, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer35.Add( self.m_button85, 0, wx.ALL, 5 )
		
		
		bSizer1315.Add( gSizer35, 1, wx.EXPAND, 5 )
		
		
		self.m_panel6.SetSizer( bSizer1315 )
		self.m_panel6.Layout()
		bSizer1315.Fit( self.m_panel6 )
		self.m_notebook1.AddPage( self.m_panel6, u"PMECH", False )
		self.m_panel7 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1316 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer216 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox36Choices = []
		self.m_listBox36 = wx.ListBox( self.m_panel7, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices = m_listBox36Choices)
		gSizer216.Add( self.m_listBox36, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox46Choices = []
		self.m_listBox46 = wx.ListBox( self.m_panel7, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox46Choices)
		gSizer216.Add( self.m_listBox46, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1316.Add( gSizer216, 5, wx.EXPAND, 5 )
		
		gSizer36 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button56 = wx.Button( self.m_panel7, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer36.Add( self.m_button56, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button66 = wx.Button( self.m_panel7, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer36.Add( self.m_button66, 0, wx.ALL, 5 )
		
		self.m_button76 = wx.Button( self.m_panel7, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer36.Add( self.m_button76, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button86 = wx.Button( self.m_panel7, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer36.Add( self.m_button86, 0, wx.ALL, 5 )
		
		
		bSizer1316.Add( gSizer36, 1, wx.EXPAND, 5 )
		
		
		self.m_panel7.SetSizer( bSizer1316 )
		self.m_panel7.Layout()
		bSizer1316.Fit( self.m_panel7 )
		self.m_notebook1.AddPage( self.m_panel7, u"SPEED", False )
		self.m_panel8 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1317 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer217 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox37Choices = []
		self.m_listBox37 = wx.ListBox( self.m_panel8, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices = m_listBox37Choices)
		gSizer217.Add( self.m_listBox37, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox47Choices = []
		self.m_listBox47 = wx.ListBox( self.m_panel8,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices = m_listBox47Choices)
		gSizer217.Add( self.m_listBox47, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1317.Add( gSizer217, 5, wx.EXPAND, 5 )
		
		gSizer37 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button57 = wx.Button( self.m_panel8, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer37.Add( self.m_button57, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button67 = wx.Button( self.m_panel8, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer37.Add( self.m_button67, 0, wx.ALL, 5 )
		
		self.m_button77 = wx.Button( self.m_panel8, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer37.Add( self.m_button77, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button87 = wx.Button( self.m_panel8, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer37.Add( self.m_button87, 0, wx.ALL, 5 )
		
		
		bSizer1317.Add( gSizer37, 1, wx.EXPAND, 5 )
		
		
		self.m_panel8.SetSizer( bSizer1317 )
		self.m_panel8.Layout()
		bSizer1317.Fit( self.m_panel8 )
		self.m_notebook1.AddPage( self.m_panel8, u"XADIFD", False )
		self.m_panel9 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1318 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer218 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox38Choices = []
		self.m_listBox38 = wx.ListBox( self.m_panel9,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox38Choices)
		gSizer218.Add( self.m_listBox38, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox48Choices = []
		self.m_listBox48 = wx.ListBox( self.m_panel9, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox48Choices)
		gSizer218.Add( self.m_listBox48, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1318.Add( gSizer218, 5, wx.EXPAND, 5 )
		
		gSizer38 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button58 = wx.Button( self.m_panel9, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer38.Add( self.m_button58, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button68 = wx.Button( self.m_panel9, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer38.Add( self.m_button68, 0, wx.ALL, 5 )
		
		self.m_button78 = wx.Button( self.m_panel9, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer38.Add( self.m_button78, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button88 = wx.Button( self.m_panel9, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer38.Add( self.m_button88, 0, wx.ALL, 5 )
		
		
		bSizer1318.Add( gSizer38, 1, wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer1318 )
		self.m_panel9.Layout()
		bSizer1318.Fit( self.m_panel9 )
		self.m_notebook1.AddPage( self.m_panel9, u"ECOMP", False )
		self.m_panel10 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1319 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer219 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox39Choices = []
		self.m_listBox39 = wx.ListBox( self.m_panel10,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox39Choices)
		gSizer219.Add( self.m_listBox39, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox49Choices = []
		self.m_listBox49 = wx.ListBox( self.m_panel10,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox49Choices)
		gSizer219.Add( self.m_listBox49, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1319.Add( gSizer219, 5, wx.EXPAND, 5 )
		
		gSizer39 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button59 = wx.Button( self.m_panel10, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer39.Add( self.m_button59, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button69 = wx.Button( self.m_panel10, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer39.Add( self.m_button69, 0, wx.ALL, 5 )
		
		self.m_button79 = wx.Button( self.m_panel10, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer39.Add( self.m_button79, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button89 = wx.Button( self.m_panel10, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer39.Add( self.m_button89, 0, wx.ALL, 5 )
		
		
		bSizer1319.Add( gSizer39, 1, wx.EXPAND, 5 )
		
		
		self.m_panel10.SetSizer( bSizer1319 )
		self.m_panel10.Layout()
		bSizer1319.Fit( self.m_panel10 )
		self.m_notebook1.AddPage( self.m_panel10, u"VOTHSG", False )
		self.m_panel11 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13110 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2110 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox310Choices = []
		self.m_listBox310 = wx.ListBox( self.m_panel11,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox310Choices)
		gSizer2110.Add( self.m_listBox310, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox410Choices = []
		self.m_listBox410 = wx.ListBox( self.m_panel11,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox410Choices)
		gSizer2110.Add( self.m_listBox410, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13110.Add( gSizer2110, 5, wx.EXPAND, 5 )
		
		gSizer310 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button510 = wx.Button( self.m_panel11, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer310.Add( self.m_button510, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button610 = wx.Button( self.m_panel11, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer310.Add( self.m_button610, 0, wx.ALL, 5 )
		
		self.m_button710 = wx.Button( self.m_panel11, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer310.Add( self.m_button710, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button810 = wx.Button( self.m_panel11, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer310.Add( self.m_button810, 0, wx.ALL, 5 )
		
		
		bSizer13110.Add( gSizer310, 1, wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer13110 )
		self.m_panel11.Layout()
		bSizer13110.Fit( self.m_panel11 )
		self.m_notebook1.AddPage( self.m_panel11, u"VREF", False )
		self.m_panel12 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13111 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2111 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox311Choices = []
		self.m_listBox311 = wx.ListBox( self.m_panel12,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox311Choices)
		gSizer2111.Add( self.m_listBox311, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox411Choices = []
		self.m_listBox411 = wx.ListBox( self.m_panel12,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox411Choices)
		gSizer2111.Add( self.m_listBox411, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13111.Add( gSizer2111, 5, wx.EXPAND, 5 )
		
		gSizer311 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button511 = wx.Button( self.m_panel12, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer311.Add( self.m_button511, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button611 = wx.Button( self.m_panel12, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer311.Add( self.m_button611, 0, wx.ALL, 5 )
		
		self.m_button711 = wx.Button( self.m_panel12, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer311.Add( self.m_button711, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button811 = wx.Button( self.m_panel12, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer311.Add( self.m_button811, 0, wx.ALL, 5 )
		
		
		bSizer13111.Add( gSizer311, 1, wx.EXPAND, 5 )
		
		
		self.m_panel12.SetSizer( bSizer13111 )
		self.m_panel12.Layout()
		bSizer13111.Fit( self.m_panel12 )
		self.m_notebook1.AddPage( self.m_panel12, u"BSFREQ", False )
		self.m_panel13 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13112 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2112 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox312Choices = []
		self.m_listBox312 = wx.ListBox( self.m_panel13, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox312Choices)
		gSizer2112.Add( self.m_listBox312, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox412Choices = []
		self.m_listBox412 = wx.ListBox( self.m_panel13,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox412Choices)
		gSizer2112.Add( self.m_listBox412, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13112.Add( gSizer2112, 5, wx.EXPAND, 5 )
		
		gSizer312 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button512 = wx.Button( self.m_panel13, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer312.Add( self.m_button512, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button612 = wx.Button( self.m_panel13, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer312.Add( self.m_button612, 0, wx.ALL, 5 )
		
		self.m_button712 = wx.Button( self.m_panel13, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer312.Add( self.m_button712, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button812 = wx.Button( self.m_panel13, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer312.Add( self.m_button812, 0, wx.ALL, 5 )
		
		
		bSizer13112.Add( gSizer312, 1, wx.EXPAND, 5 )
		
		
		self.m_panel13.SetSizer( bSizer13112 )
		self.m_panel13.Layout()
		bSizer13112.Fit( self.m_panel13 )
		self.m_notebook1.AddPage( self.m_panel13, u"VOlTAGE", False )
		self.m_panel14 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13113 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2113 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox313Choices = []
		self.m_listBox313 = wx.ListBox( self.m_panel14,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox313Choices)
		gSizer2113.Add( self.m_listBox313, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox413Choices = []
		self.m_listBox413 = wx.ListBox( self.m_panel14,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox413Choices)
		gSizer2113.Add( self.m_listBox413, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13113.Add( gSizer2113, 5, wx.EXPAND, 5 )
		
		gSizer313 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button513 = wx.Button( self.m_panel14, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer313.Add( self.m_button513, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button613 = wx.Button( self.m_panel14, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer313.Add( self.m_button613, 0, wx.ALL, 5 )
		
		self.m_button713 = wx.Button( self.m_panel14, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer313.Add( self.m_button713, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button813 = wx.Button( self.m_panel14, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer313.Add( self.m_button813, 0, wx.ALL, 5 )
		
		
		bSizer13113.Add( gSizer313, 1, wx.EXPAND, 5 )
		
		
		self.m_panel14.SetSizer( bSizer13113 )
		self.m_panel14.Layout()
		bSizer13113.Fit( self.m_panel14 )
		self.m_notebook1.AddPage( self.m_panel14, u"VOL&ANG", False )
		self.m_panel15 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13114 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2114 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox314Choices = []
		self.m_listBox314 = wx.ListBox( self.m_panel15,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox314Choices)
		gSizer2114.Add( self.m_listBox314, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox414Choices = []
		self.m_listBox414 = wx.ListBox( self.m_panel15,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox414Choices)
		gSizer2114.Add( self.m_listBox414, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13114.Add( gSizer2114, 5, wx.EXPAND, 5 )
		
		gSizer314 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button514 = wx.Button( self.m_panel15, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer314.Add( self.m_button514, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button614 = wx.Button( self.m_panel15, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer314.Add( self.m_button614, 0, wx.ALL, 5 )
		
		self.m_button714 = wx.Button( self.m_panel15, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer314.Add( self.m_button714, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button814 = wx.Button( self.m_panel15, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer314.Add( self.m_button814, 0, wx.ALL, 5 )
		
		
		bSizer13114.Add( gSizer314, 1, wx.EXPAND, 5 )
		
		
		self.m_panel15.SetSizer( bSizer13114 )
		self.m_panel15.Layout()
		bSizer13114.Fit( self.m_panel15 )
		self.m_notebook1.AddPage( self.m_panel15, u"FLOW", False )
		self.m_panel18 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13115 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2115 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox315Choices = []
		self.m_listBox315 = wx.ListBox( self.m_panel18,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices=m_listBox315Choices)
		gSizer2115.Add( self.m_listBox315, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox415Choices = []
		self.m_listBox415 = wx.ListBox( self.m_panel18, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox415Choices)
		gSizer2115.Add( self.m_listBox415, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13115.Add( gSizer2115, 5, wx.EXPAND, 5 )
		
		gSizer315 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button515 = wx.Button( self.m_panel18, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer315.Add( self.m_button515, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button615 = wx.Button( self.m_panel18, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer315.Add( self.m_button615, 0, wx.ALL, 5 )
		
		self.m_button715 = wx.Button( self.m_panel18, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer315.Add( self.m_button715, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button815 = wx.Button( self.m_panel18, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer315.Add( self.m_button815, 0, wx.ALL, 5 )
		
		
		bSizer13115.Add( gSizer315, 1, wx.EXPAND, 5 )
		
		
		self.m_panel18.SetSizer( bSizer13115 )
		self.m_panel18.Layout()
		bSizer13115.Fit( self.m_panel18 )
		self.m_notebook1.AddPage( self.m_panel18, u"FLOWPQ", False )
		self.m_panel19 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13117 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2117 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox317Choices = []
		self.m_listBox317 = wx.ListBox( self.m_panel19, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox317Choices)
		gSizer2117.Add( self.m_listBox317, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox417Choices = []
		self.m_listBox417 = wx.ListBox( self.m_panel19, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox417Choices)
		gSizer2117.Add( self.m_listBox417, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13117.Add( gSizer2117, 5, wx.EXPAND, 5 )
		
		gSizer317 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button517 = wx.Button( self.m_panel19, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer317.Add( self.m_button517, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button617 = wx.Button( self.m_panel19, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer317.Add( self.m_button617, 0, wx.ALL, 5 )
		
		self.m_button717 = wx.Button( self.m_panel19, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer317.Add( self.m_button717, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button817 = wx.Button( self.m_panel19, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer317.Add( self.m_button817, 0, wx.ALL, 5 )
		
		
		bSizer13117.Add( gSizer317, 1, wx.EXPAND, 5 )
		
		
		self.m_panel19.SetSizer( bSizer13117 )
		self.m_panel19.Layout()
		bSizer13117.Fit( self.m_panel19 )
		self.m_notebook1.AddPage( self.m_panel19, u"FLOWMVA", False )
		self.m_panel20 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13118 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2118 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox318Choices = []
		self.m_listBox318 = wx.ListBox( self.m_panel20,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox318Choices)
		gSizer2118.Add( self.m_listBox318, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox418Choices = []
		self.m_listBox418 = wx.ListBox( self.m_panel20,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox418Choices)
		gSizer2118.Add( self.m_listBox418, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13118.Add( gSizer2118, 5, wx.EXPAND, 5 )
		
		gSizer318 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button518 = wx.Button( self.m_panel20, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer318.Add( self.m_button518, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button618 = wx.Button( self.m_panel20, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer318.Add( self.m_button618, 0, wx.ALL, 5 )
		
		self.m_button718 = wx.Button( self.m_panel20, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer318.Add( self.m_button718, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button818 = wx.Button( self.m_panel20, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer318.Add( self.m_button818, 0, wx.ALL, 5 )
		
		
		bSizer13118.Add( gSizer318, 1, wx.EXPAND, 5 )
		
		
		self.m_panel20.SetSizer( bSizer13118 )
		self.m_panel20.Layout()
		bSizer13118.Fit( self.m_panel20 )
		self.m_notebook1.AddPage( self.m_panel20, u"RELAY2", False )
		self.m_panel21 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13119 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2119 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox319Choices = []
		self.m_listBox319 = wx.ListBox( self.m_panel21, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox319Choices)
		gSizer2119.Add( self.m_listBox319, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox419Choices = []
		self.m_listBox419 = wx.ListBox( self.m_panel21, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox419Choices)
		gSizer2119.Add( self.m_listBox419, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13119.Add( gSizer2119, 5, wx.EXPAND, 5 )
		
		gSizer319 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button519 = wx.Button( self.m_panel21, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer319.Add( self.m_button519, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button619 = wx.Button( self.m_panel21, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer319.Add( self.m_button619, 0, wx.ALL, 5 )
		
		self.m_button719 = wx.Button( self.m_panel21, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer319.Add( self.m_button719, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button819 = wx.Button( self.m_panel21, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer319.Add( self.m_button819, 0, wx.ALL, 5 )
		
		
		bSizer13119.Add( gSizer319, 1, wx.EXPAND, 5 )
		
		
		self.m_panel21.SetSizer( bSizer13119 )
		self.m_panel21.Layout()
		bSizer13119.Fit( self.m_panel21 )
		self.m_notebook1.AddPage( self.m_panel21, u"VAR", False )
		self.m_panel22 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13120 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2120 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox320Choices = []
		self.m_listBox320 = wx.ListBox( self.m_panel22,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox320Choices)
		gSizer2120.Add( self.m_listBox320, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox420Choices = []
		self.m_listBox420 = wx.ListBox( self.m_panel22,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox420Choices)
		gSizer2120.Add( self.m_listBox420, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13120.Add( gSizer2120, 5, wx.EXPAND, 5 )
		
		gSizer320 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button520 = wx.Button( self.m_panel22, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer320.Add( self.m_button520, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button620 = wx.Button( self.m_panel22, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer320.Add( self.m_button620, 0, wx.ALL, 5 )
		
		self.m_button720 = wx.Button( self.m_panel22, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer320.Add( self.m_button720, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button820 = wx.Button( self.m_panel22, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer320.Add( self.m_button820, 0, wx.ALL, 5 )
		
		
		bSizer13120.Add( gSizer320, 1, wx.EXPAND, 5 )
		
		
		self.m_panel22.SetSizer( bSizer13120 )
		self.m_panel22.Layout()
		bSizer13120.Fit( self.m_panel22 )
		self.m_notebook1.AddPage( self.m_panel22, u"STATE", False )
		self.m_panel23 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13121 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2121 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox321Choices = []
		self.m_listBox321 = wx.ListBox( self.m_panel23,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox321Choices)
		gSizer2121.Add( self.m_listBox321, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox421Choices = []
		self.m_listBox421 = wx.ListBox( self.m_panel23,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox421Choices)
		gSizer2121.Add( self.m_listBox421, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13121.Add( gSizer2121, 5, wx.EXPAND, 5 )
		
		gSizer321 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button521 = wx.Button( self.m_panel23, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_button521, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button621 = wx.Button( self.m_panel23, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_button621, 0, wx.ALL, 5 )
		
		self.m_button721 = wx.Button( self.m_panel23, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_button721, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button821 = wx.Button( self.m_panel23, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer321.Add( self.m_button821, 0, wx.ALL, 5 )
		
		
		bSizer13121.Add( gSizer321, 1, wx.EXPAND, 5 )
		
		
		self.m_panel23.SetSizer( bSizer13121 )
		self.m_panel23.Layout()
		bSizer13121.Fit( self.m_panel23 )
		self.m_notebook1.AddPage( self.m_panel23, u"MACHITERM", False )
		self.m_panel24 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13122 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2122 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox322Choices = []
		self.m_listBox322 = wx.ListBox( self.m_panel24,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox322Choices)
		gSizer2122.Add( self.m_listBox322, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox422Choices = []
		self.m_listBox422 = wx.ListBox( self.m_panel24,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox422Choices)
		gSizer2122.Add( self.m_listBox422, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13122.Add( gSizer2122, 5, wx.EXPAND, 5 )
		
		gSizer322 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button522 = wx.Button( self.m_panel24, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer322.Add( self.m_button522, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button622 = wx.Button( self.m_panel24, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer322.Add( self.m_button622, 0, wx.ALL, 5 )
		
		self.m_button722 = wx.Button( self.m_panel24, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer322.Add( self.m_button722, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button822 = wx.Button( self.m_panel24, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer322.Add( self.m_button822, 0, wx.ALL, 5 )
		
		
		bSizer13122.Add( gSizer322, 1, wx.EXPAND, 5 )
		
		
		self.m_panel24.SetSizer( bSizer13122 )
		self.m_panel24.Layout()
		bSizer13122.Fit( self.m_panel24 )
		self.m_notebook1.AddPage( self.m_panel24, u"MACHAPPIMP", False )
		self.m_panel25 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13123 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2123 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox323Choices = []
		self.m_listBox323 = wx.ListBox( self.m_panel25,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox323Choices)
		gSizer2123.Add( self.m_listBox323, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox423Choices = []
		self.m_listBox423 = wx.ListBox( self.m_panel25,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox423Choices)
		gSizer2123.Add( self.m_listBox423, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13123.Add( gSizer2123, 5, wx.EXPAND, 5 )
		
		gSizer323 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button523 = wx.Button( self.m_panel25, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer323.Add( self.m_button523, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button623 = wx.Button( self.m_panel25, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer323.Add( self.m_button623, 0, wx.ALL, 5 )
		
		self.m_button723 = wx.Button( self.m_panel25, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer323.Add( self.m_button723, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button823 = wx.Button( self.m_panel25, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer323.Add( self.m_button823, 0, wx.ALL, 5 )
		
		
		bSizer13123.Add( gSizer323, 1, wx.EXPAND, 5 )
		
		
		self.m_panel25.SetSizer( bSizer13123 )
		self.m_panel25.Layout()
		bSizer13123.Fit( self.m_panel25 )
		self.m_notebook1.AddPage( self.m_panel25, u"VUEL", False )
		self.m_panel26 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13124 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2124 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox324Choices = []
		self.m_listBox324 = wx.ListBox( self.m_panel26,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox324Choices)
		gSizer2124.Add( self.m_listBox324, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox424Choices = []
		self.m_listBox424 = wx.ListBox( self.m_panel26,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox424Choices)
		gSizer2124.Add( self.m_listBox424, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13124.Add( gSizer2124, 5, wx.EXPAND, 5 )
		
		gSizer324 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button524 = wx.Button( self.m_panel26, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer324.Add( self.m_button524, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button624 = wx.Button( self.m_panel26, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer324.Add( self.m_button624, 0, wx.ALL, 5 )
		
		self.m_button724 = wx.Button( self.m_panel26, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer324.Add( self.m_button724, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button824 = wx.Button( self.m_panel26, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer324.Add( self.m_button824, 0, wx.ALL, 5 )
		
		
		bSizer13124.Add( gSizer324, 1, wx.EXPAND, 5 )
		
		
		self.m_panel26.SetSizer( bSizer13124 )
		self.m_panel26.Layout()
		bSizer13124.Fit( self.m_panel26 )
		self.m_notebook1.AddPage( self.m_panel26, u"VOEL", False )
		self.m_panel27 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13125 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2125 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox325Choices = []
		self.m_listBox325 = wx.ListBox( self.m_panel27,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox325Choices)
		gSizer2125.Add( self.m_listBox325, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox425Choices = []
		self.m_listBox425 = wx.ListBox( self.m_panel27,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox425Choices)
		gSizer2125.Add( self.m_listBox425, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13125.Add( gSizer2125, 5, wx.EXPAND, 5 )
		
		gSizer325 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button525 = wx.Button( self.m_panel27, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer325.Add( self.m_button525, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button625 = wx.Button( self.m_panel27, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer325.Add( self.m_button625, 0, wx.ALL, 5 )
		
		self.m_button725 = wx.Button( self.m_panel27, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer325.Add( self.m_button725, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button825 = wx.Button( self.m_panel27, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer325.Add( self.m_button825, 0, wx.ALL, 5 )
		
		
		bSizer13125.Add( gSizer325, 1, wx.EXPAND, 5 )
		
		
		self.m_panel27.SetSizer( bSizer13125 )
		self.m_panel27.Layout()
		bSizer13125.Fit( self.m_panel27 )
		self.m_notebook1.AddPage( self.m_panel27, u"PLOAD", False )
		self.m_panel28 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13126 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2126 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox326Choices = []
		self.m_listBox326 = wx.ListBox( self.m_panel28, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox326Choices)
		gSizer2126.Add( self.m_listBox326, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox426Choices = []
		self.m_listBox426 = wx.ListBox( self.m_panel28, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox426Choices)
		gSizer2126.Add( self.m_listBox426, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13126.Add( gSizer2126, 5, wx.EXPAND, 5 )
		
		gSizer326 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button526 = wx.Button( self.m_panel28, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer326.Add( self.m_button526, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button626 = wx.Button( self.m_panel28, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer326.Add( self.m_button626, 0, wx.ALL, 5 )
		
		self.m_button726 = wx.Button( self.m_panel28, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer326.Add( self.m_button726, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button826 = wx.Button( self.m_panel28, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer326.Add( self.m_button826, 0, wx.ALL, 5 )
		
		
		bSizer13126.Add( gSizer326, 1, wx.EXPAND, 5 )
		
		
		self.m_panel28.SetSizer( bSizer13126 )
		self.m_panel28.Layout()
		bSizer13126.Fit( self.m_panel28 )
		self.m_notebook1.AddPage( self.m_panel28, u"QLOAD", False )
		self.m_panel29 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13127 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2127 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox327Choices = []
		self.m_listBox327 = wx.ListBox( self.m_panel29,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox327Choices)
		gSizer2127.Add( self.m_listBox327, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox427Choices = []
		self.m_listBox427 = wx.ListBox( self.m_panel29, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox427Choices)
		gSizer2127.Add( self.m_listBox427, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13127.Add( gSizer2127, 5, wx.EXPAND, 5 )
		
		gSizer327 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button527 = wx.Button( self.m_panel29, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer327.Add( self.m_button527, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button627 = wx.Button( self.m_panel29, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer327.Add( self.m_button627, 0, wx.ALL, 5 )
		
		self.m_button727 = wx.Button( self.m_panel29, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer327.Add( self.m_button727, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button827 = wx.Button( self.m_panel29, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer327.Add( self.m_button827, 0, wx.ALL, 5 )
		
		
		bSizer13127.Add( gSizer327, 1, wx.EXPAND, 5 )
		
		
		self.m_panel29.SetSizer( bSizer13127 )
		self.m_panel29.Layout()
		bSizer13127.Fit( self.m_panel29 )
		self.m_notebook1.AddPage( self.m_panel29, u"GREF", False )
		self.m_panel30 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13128 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2128 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox328Choices = []
		self.m_listBox328 = wx.ListBox( self.m_panel30,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox328Choices)
		gSizer2128.Add( self.m_listBox328, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox428Choices = []
		self.m_listBox428 = wx.ListBox( self.m_panel30,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox428Choices)
		gSizer2128.Add( self.m_listBox428, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13128.Add( gSizer2128, 5, wx.EXPAND, 5 )
		
		gSizer328 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button528 = wx.Button( self.m_panel30, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer328.Add( self.m_button528, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button628 = wx.Button( self.m_panel30, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer328.Add( self.m_button628, 0, wx.ALL, 5 )
		
		self.m_button728 = wx.Button( self.m_panel30, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer328.Add( self.m_button728, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button828 = wx.Button( self.m_panel30, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer328.Add( self.m_button828, 0, wx.ALL, 5 )
		
		
		bSizer13128.Add( gSizer328, 1, wx.EXPAND, 5 )
		
		
		self.m_panel30.SetSizer( bSizer13128 )
		self.m_panel30.Layout()
		bSizer13128.Fit( self.m_panel30 )
		self.m_notebook1.AddPage( self.m_panel30, u"LCREF", False )
		self.m_panel31 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13129 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2129 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox329Choices = []
		self.m_listBox329 = wx.ListBox( self.m_panel31, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox329Choices)
		gSizer2129.Add( self.m_listBox329, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox429Choices = []
		self.m_listBox429 = wx.ListBox( self.m_panel31, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox429Choices)
		gSizer2129.Add( self.m_listBox429, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13129.Add( gSizer2129, 5, wx.EXPAND, 5 )
		
		gSizer329 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button529 = wx.Button( self.m_panel31, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer329.Add( self.m_button529, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button629 = wx.Button( self.m_panel31, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer329.Add( self.m_button629, 0, wx.ALL, 5 )
		
		self.m_button729 = wx.Button( self.m_panel31, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer329.Add( self.m_button729, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button829 = wx.Button( self.m_panel31, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer329.Add( self.m_button829, 0, wx.ALL, 5 )
		
		
		bSizer13129.Add( gSizer329, 1, wx.EXPAND, 5 )
		
		
		self.m_panel31.SetSizer( bSizer13129 )
		self.m_panel31.Layout()
		bSizer13129.Fit( self.m_panel31 )
		self.m_notebook1.AddPage( self.m_panel31, u"WINDVEL", False )
		self.m_panel32 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13130 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2130 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox330Choices = []
		self.m_listBox330 = wx.ListBox( self.m_panel32,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox330Choices)
		gSizer2130.Add( self.m_listBox330, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox430Choices = []
		self.m_listBox430 = wx.ListBox( self.m_panel32,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox430Choices)
		gSizer2130.Add( self.m_listBox430, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13130.Add( gSizer2130, 5, wx.EXPAND, 5 )
		
		gSizer330 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button530 = wx.Button( self.m_panel32, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer330.Add( self.m_button530, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button630 = wx.Button( self.m_panel32, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer330.Add( self.m_button630, 0, wx.ALL, 5 )
		
		self.m_button730 = wx.Button( self.m_panel32, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer330.Add( self.m_button730, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button830 = wx.Button( self.m_panel32, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer330.Add( self.m_button830, 0, wx.ALL, 5 )
		
		
		bSizer13130.Add( gSizer330, 1, wx.EXPAND, 5 )
		
		
		self.m_panel32.SetSizer( bSizer13130 )
		self.m_panel32.Layout()
		bSizer13130.Fit( self.m_panel32 )
		self.m_notebook1.AddPage( self.m_panel32, u"WINDTURSPD", False )
		self.m_panel33 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13131 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2131 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox331Choices = []
		self.m_listBox331 = wx.ListBox( self.m_panel33,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox331Choices)
		gSizer2131.Add( self.m_listBox331, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox431Choices = []
		self.m_listBox431 = wx.ListBox( self.m_panel33,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox431Choices)
		gSizer2131.Add( self.m_listBox431, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13131.Add( gSizer2131, 5, wx.EXPAND, 5 )
		
		gSizer331 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button531 = wx.Button( self.m_panel33, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer331.Add( self.m_button531, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button631 = wx.Button( self.m_panel33, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer331.Add( self.m_button631, 0, wx.ALL, 5 )
		
		self.m_button731 = wx.Button( self.m_panel33, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer331.Add( self.m_button731, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button831 = wx.Button( self.m_panel33, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer331.Add( self.m_button831, 0, wx.ALL, 5 )
		
		
		bSizer13131.Add( gSizer331, 1, wx.EXPAND, 5 )
		
		
		self.m_panel33.SetSizer( bSizer13131 )
		self.m_panel33.Layout()
		bSizer13131.Fit( self.m_panel33 )
		self.m_notebook1.AddPage( self.m_panel33, u"WINDPITCH", False )
		self.m_panel34 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13132 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2132 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox332Choices = []
		self.m_listBox332 = wx.ListBox( self.m_panel34,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox332Choices)
		gSizer2132.Add( self.m_listBox332, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox432Choices = []
		self.m_listBox432 = wx.ListBox( self.m_panel34,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox432Choices)
		gSizer2132.Add( self.m_listBox432, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13132.Add( gSizer2132, 5, wx.EXPAND, 5 )
		
		gSizer332 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button532 = wx.Button( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer332.Add( self.m_button532, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button632 = wx.Button( self.m_panel34, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer332.Add( self.m_button632, 0, wx.ALL, 5 )
		
		self.m_button732 = wx.Button( self.m_panel34, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer332.Add( self.m_button732, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button832 = wx.Button( self.m_panel34, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer332.Add( self.m_button832, 0, wx.ALL, 5 )
		
		
		bSizer13132.Add( gSizer332, 1, wx.EXPAND, 5 )
		
		
		self.m_panel34.SetSizer( bSizer13132 )
		self.m_panel34.Layout()
		bSizer13132.Fit( self.m_panel34 )
		self.m_notebook1.AddPage( self.m_panel34, u"WINDAEROTOR", False )
		self.m_panel35 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13133 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2133 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox333Choices = []
		self.m_listBox333 = wx.ListBox( self.m_panel35,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox333Choices)
		gSizer2133.Add( self.m_listBox333, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox433Choices = []
		self.m_listBox433 = wx.ListBox( self.m_panel35,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox433Choices)
		gSizer2133.Add( self.m_listBox433, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13133.Add( gSizer2133, 5, wx.EXPAND, 5 )
		
		gSizer333 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button533 = wx.Button( self.m_panel35, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer333.Add( self.m_button533, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button633 = wx.Button( self.m_panel35, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer333.Add( self.m_button633, 0, wx.ALL, 5 )
		
		self.m_button733 = wx.Button( self.m_panel35, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer333.Add( self.m_button733, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button833 = wx.Button( self.m_panel35, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer333.Add( self.m_button833, 0, wx.ALL, 5 )
		
		
		bSizer13133.Add( gSizer333, 1, wx.EXPAND, 5 )
		
		
		self.m_panel35.SetSizer( bSizer13133 )
		self.m_panel35.Layout()
		bSizer13133.Fit( self.m_panel35 )
		self.m_notebook1.AddPage( self.m_panel35, u"WINDROTORVOL", False )
		self.m_panel36 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13134 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2134 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox334Choices = []
		self.m_listBox334 = wx.ListBox( self.m_panel36,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox334Choices)
		gSizer2134.Add( self.m_listBox334, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox434Choices = []
		self.m_listBox434 = wx.ListBox( self.m_panel36,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox434Choices)
		gSizer2134.Add( self.m_listBox434, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13134.Add( gSizer2134, 5, wx.EXPAND, 5 )
		
		gSizer334 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button534 = wx.Button( self.m_panel36, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer334.Add( self.m_button534, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button634 = wx.Button( self.m_panel36, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer334.Add( self.m_button634, 0, wx.ALL, 5 )
		
		self.m_button734 = wx.Button( self.m_panel36, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer334.Add( self.m_button734, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button834 = wx.Button( self.m_panel36, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer334.Add( self.m_button834, 0, wx.ALL, 5 )
		
		
		bSizer13134.Add( gSizer334, 1, wx.EXPAND, 5 )
		
		
		self.m_panel36.SetSizer( bSizer13134 )
		self.m_panel36.Layout()
		bSizer13134.Fit( self.m_panel36 )
		self.m_notebook1.AddPage( self.m_panel36, u"WINDROTORCUR", False )
		self.m_panel37 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13135 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2135 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox335Choices = []
		self.m_listBox335 = wx.ListBox( self.m_panel37,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox335Choices)
		gSizer2135.Add( self.m_listBox335, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox435Choices = []
		self.m_listBox435 = wx.ListBox( self.m_panel37,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox435Choices)
		gSizer2135.Add( self.m_listBox435, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13135.Add( gSizer2135, 5, wx.EXPAND, 5 )
		
		gSizer335 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button535 = wx.Button( self.m_panel37, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer335.Add( self.m_button535, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button635 = wx.Button( self.m_panel37, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer335.Add( self.m_button635, 0, wx.ALL, 5 )
		
		self.m_button735 = wx.Button( self.m_panel37, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer335.Add( self.m_button735, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button835 = wx.Button( self.m_panel37, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer335.Add( self.m_button835, 0, wx.ALL, 5 )
		
		
		bSizer13135.Add( gSizer335, 1, wx.EXPAND, 5 )
		
		
		self.m_panel37.SetSizer( bSizer13135 )
		self.m_panel37.Layout()
		bSizer13135.Fit( self.m_panel37 )
		self.m_notebook1.AddPage( self.m_panel37, u"WINDPCOMAND", False )
		self.m_panel38 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13136 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2136 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox336Choices = []
		self.m_listBox336 = wx.ListBox( self.m_panel38,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox336Choices)
		gSizer2136.Add( self.m_listBox336, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox436Choices = []
		self.m_listBox436 = wx.ListBox( self.m_panel38, size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox436Choices)
		gSizer2136.Add( self.m_listBox436, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13136.Add( gSizer2136, 5, wx.EXPAND, 5 )
		
		gSizer336 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button536 = wx.Button( self.m_panel38, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer336.Add( self.m_button536, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button636 = wx.Button( self.m_panel38, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer336.Add( self.m_button636, 0, wx.ALL, 5 )
		
		self.m_button736 = wx.Button( self.m_panel38, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer336.Add( self.m_button736, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button836 = wx.Button( self.m_panel38, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer336.Add( self.m_button836, 0, wx.ALL, 5 )
		
		
		bSizer13136.Add( gSizer336, 1, wx.EXPAND, 5 )
		
		
		self.m_panel38.SetSizer( bSizer13136 )
		self.m_panel38.Layout()
		bSizer13136.Fit( self.m_panel38 )
		self.m_notebook1.AddPage( self.m_panel38, u"WINDQCOMAND", False )
		self.m_panel39 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13137 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2137 = wx.GridSizer( 0, 2, 0, 0 )
		
		m_listBox337Choices = []
		self.m_listBox337 = wx.ListBox( self.m_panel39,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox337Choices)
		gSizer2137.Add( self.m_listBox337, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox437Choices = []
		self.m_listBox437 = wx.ListBox( self.m_panel39,  size=wx.DefaultSize,style=wx.LB_EXTENDED, choices= m_listBox437Choices)
		gSizer2137.Add( self.m_listBox437, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13137.Add( gSizer2137, 5, wx.EXPAND, 5 )
		
		gSizer337 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_button537 = wx.Button( self.m_panel39, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer337.Add( self.m_button537, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button637 = wx.Button( self.m_panel39, wx.ID_ANY, u">>", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer337.Add( self.m_button637, 0, wx.ALL, 5 )
		
		self.m_button737 = wx.Button( self.m_panel39, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer337.Add( self.m_button737, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_button837 = wx.Button( self.m_panel39, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer337.Add( self.m_button837, 0, wx.ALL, 5 )
		
		
		bSizer13137.Add( gSizer337, 1, wx.EXPAND, 5 )
		
		
		self.m_panel39.SetSizer( bSizer13137 )
		self.m_panel39.Layout()
		bSizer13137.Fit( self.m_panel39 )
		self.m_notebook1.AddPage( self.m_panel39, u"WINDAUX", False )
		
		bSizer5.Add( self.m_notebook1, 5, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13138 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		bSizer13138.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl42 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13138.Add( self.m_textCtrl42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( bSizer13138, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		gSizer2 = wx.GridSizer( 0, 5, 0, 0 )
		
		self.m_radioBtn10 = wx.RadioButton( self, wx.ID_ANY, u"Relative to machine", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_radioBtn10, 0, wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Gen Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.Enable( False )
		
		gSizer2.Add( self.m_staticText4, 1, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices)
		self.m_comboBox1.Enable( False )
		
		gSizer2.Add( self.m_comboBox1,1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
				
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		self.m_radioBtn12 = wx.RadioButton( self, wx.ID_ANY, u"Relative to system average angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn12.SetValue( True )
		gSizer2.Add( self.m_radioBtn12, 0, wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer2.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer2.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		
		gSizer2.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		self.m_radioBtn13 = wx.RadioButton( self, wx.ID_ANY, u"Relative to system weighted average angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_radioBtn13, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Check Initial Condition", wx.DefaultPosition, wx.Size(200,-1), 0 )
		bSizer5.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		
		# gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.dynProcess = wx.Button( self, wx.ID_ANY, u"Run dynamic process", wx.DefaultPosition, wx.Size(200,-1), 0 )
		bSizer5.Add( self.dynProcess, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		# self.dynProcess.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		# bSizer5.Add( self.dynProcess, 0, wx.ALL, 10 )

		self.dynMultiProcess = wx.Button( self, wx.ID_ANY, u"Run Multi dynamic process", wx.DefaultPosition, wx.Size(200,-1), 0 )
		bSizer5.Add( self.dynMultiProcess, 0, wx.ALL|wx.ALIGN_CENTER, 5 )
		# self.dynMultiProcess.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		# bSizer5.Add( self.dynMultiProcess, 0, wx.ALL, 10 )
		# bSizer5.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.CentreOnParent( wx.BOTH )
		
		# Connect Events
		self.m_textCtrl42.Bind( wx.EVT_TEXT, self.onText_Search )
		self.m_listBox3.Bind( wx.EVT_LISTBOX, self.onSelectAngle )
		self.m_listBox4.Bind( wx.EVT_LISTBOX, self.onSelectToMoveAngle )
		self.m_button5.Bind( wx.EVT_BUTTON, self.oneAddAngle )
		self.m_button6.Bind( wx.EVT_BUTTON, self.multiAddAngle )
		self.m_button7.Bind( wx.EVT_BUTTON, self.oneMoveAngle )
		self.m_button8.Bind( wx.EVT_BUTTON, self.multiMoveAngle )
		self.m_listBox31.Bind( wx.EVT_LISTBOX, self.onSelectPELEC )
		self.m_listBox41.Bind( wx.EVT_LISTBOX, self.onSelectToMovePELEC )
		self.m_button51.Bind( wx.EVT_BUTTON, self.oneAddPELEC )
		self.m_button61.Bind( wx.EVT_BUTTON, self.multiAddPELEC )
		self.m_button71.Bind( wx.EVT_BUTTON, self.oneMovePELEC )
		self.m_button81.Bind( wx.EVT_BUTTON, self.multiMovePELEC )
		self.m_listBox32.Bind( wx.EVT_LISTBOX, self.onSelectQELEC )
		self.m_listBox42.Bind( wx.EVT_LISTBOX, self.onSelectToMoveQELEC )
		self.m_button52.Bind( wx.EVT_BUTTON, self.oneAddQELEC )
		self.m_button62.Bind( wx.EVT_BUTTON, self.multiAddQELEC )
		self.m_button72.Bind( wx.EVT_BUTTON, self.oneMoveQELEC )
		self.m_button82.Bind( wx.EVT_BUTTON, self.multiMoveQELEC )
		self.m_listBox33.Bind( wx.EVT_LISTBOX, self.onSelectETERM )
		self.m_listBox43.Bind( wx.EVT_LISTBOX, self.onSelectToMoveETERM )
		self.m_button53.Bind( wx.EVT_BUTTON, self.oneAddETERM )
		self.m_button63.Bind( wx.EVT_BUTTON, self.multiAddETERM )
		self.m_button73.Bind( wx.EVT_BUTTON, self.oneMoveETERM )
		self.m_button83.Bind( wx.EVT_BUTTON, self.multiMoveETERM )
		self.m_listBox34.Bind( wx.EVT_LISTBOX, self.onSelectEFD )
		self.m_listBox44.Bind( wx.EVT_LISTBOX, self.onSelectToMoveEFD )
		self.m_button54.Bind( wx.EVT_BUTTON, self.oneAddEFD )
		self.m_button64.Bind( wx.EVT_BUTTON, self.multiAddEFD )
		self.m_button74.Bind( wx.EVT_BUTTON, self.oneMoveEFD )
		self.m_button84.Bind( wx.EVT_BUTTON, self.multiMoveEFD )
		self.m_listBox35.Bind( wx.EVT_LISTBOX, self.onSelectPMECH )
		self.m_listBox45.Bind( wx.EVT_LISTBOX, self.onSelectToMovePMECH )
		self.m_button55.Bind( wx.EVT_BUTTON, self.oneAddPMECH )
		self.m_button65.Bind( wx.EVT_BUTTON, self.multiAddPMECH )
		self.m_button75.Bind( wx.EVT_BUTTON, self.oneMovePMECH )
		self.m_button85.Bind( wx.EVT_BUTTON, self.multiMovePMECH )
		self.m_listBox36.Bind( wx.EVT_LISTBOX, self.onSelectSPEED )
		self.m_listBox46.Bind( wx.EVT_LISTBOX, self.onSelectToMoveSPEED )
		self.m_button56.Bind( wx.EVT_BUTTON, self.oneAddSPEED )
		self.m_button66.Bind( wx.EVT_BUTTON, self.multiAddSPEED )
		self.m_button76.Bind( wx.EVT_BUTTON, self.oneMoveSPEED )
		self.m_button86.Bind( wx.EVT_BUTTON, self.multiMoveSPEED )
		self.m_listBox37.Bind( wx.EVT_LISTBOX, self.onSelectXADIFD )
		self.m_listBox47.Bind( wx.EVT_LISTBOX, self.onSelectToMoveXADIFD )
		self.m_button57.Bind( wx.EVT_BUTTON, self.oneAddXADIFD )
		self.m_button67.Bind( wx.EVT_BUTTON, self.multiAddXADIFD )
		self.m_button77.Bind( wx.EVT_BUTTON, self.oneMoveXADIFD )
		self.m_button87.Bind( wx.EVT_BUTTON, self.multiMoveXADIFD )
		self.m_listBox38.Bind( wx.EVT_LISTBOX, self.onSelectECOMP )
		self.m_listBox48.Bind( wx.EVT_LISTBOX, self.onSelectToMoveECOMP )
		self.m_button58.Bind( wx.EVT_BUTTON, self.oneAddECOMP )
		self.m_button68.Bind( wx.EVT_BUTTON, self.multiAddXADIFD )
		self.m_button78.Bind( wx.EVT_BUTTON, self.oneMoveXADIFD )
		self.m_button88.Bind( wx.EVT_BUTTON, self.multiMoveXADIFD )
		self.m_listBox39.Bind( wx.EVT_LISTBOX, self.onSelectVOTHSG )
		self.m_listBox49.Bind( wx.EVT_LISTBOX, self.onSelectToMoveVOTHSG )
		self.m_button59.Bind( wx.EVT_BUTTON, self.oneAddVOTHSG )
		self.m_button69.Bind( wx.EVT_BUTTON, self.multiAddECOMP )
		self.m_button79.Bind( wx.EVT_BUTTON, self.oneMoveVOTHSG )
		self.m_button89.Bind( wx.EVT_BUTTON, self.multiMoveVOTHSG )
		self.m_listBox310.Bind( wx.EVT_LISTBOX, self.onSelectVREF )
		self.m_listBox410.Bind( wx.EVT_LISTBOX, self.onSelectToMoveVREF )
		self.m_button510.Bind( wx.EVT_BUTTON, self.oneAddVREF )
		self.m_button610.Bind( wx.EVT_BUTTON, self.multiAddVREF )
		self.m_button710.Bind( wx.EVT_BUTTON, self.oneMoveVREF )
		self.m_button810.Bind( wx.EVT_BUTTON, self.multiMoveVREF )
		self.m_listBox311.Bind( wx.EVT_LISTBOX, self.onSelectBSFREQ )
		self.m_listBox411.Bind( wx.EVT_LISTBOX, self.onSelectToMoveBSFREQ )
		self.m_button511.Bind( wx.EVT_BUTTON, self.oneAddBSFREQ )
		self.m_button611.Bind( wx.EVT_BUTTON, self.multiAddBSFREQ )
		self.m_button711.Bind( wx.EVT_BUTTON, self.oneMoveBSFREQ )
		self.m_button811.Bind( wx.EVT_BUTTON, self.multiMoveBSFREQ )
		self.m_listBox312.Bind( wx.EVT_LISTBOX, self.onSelectVOLTAGE )
		self.m_listBox412.Bind( wx.EVT_LISTBOX, self.onSelectToMoveVOLTAGE )
		self.m_button512.Bind( wx.EVT_BUTTON, self.oneAddVOLTAGE )
		self.m_button612.Bind( wx.EVT_BUTTON, self.multiAddVOLTAGE )
		self.m_button712.Bind( wx.EVT_BUTTON, self.oneMoveVOLTAGE )
		self.m_button812.Bind( wx.EVT_BUTTON, self.multiMoveVOLTAGE )
		self.m_listBox313.Bind( wx.EVT_LISTBOX, self.onSelectVOLANG )
		self.m_listBox413.Bind( wx.EVT_LISTBOX, self.onSelectToMoveVOLANG )
		self.m_button513.Bind( wx.EVT_BUTTON, self.oneAddVOLANG )
		self.m_button613.Bind( wx.EVT_BUTTON, self.multiAddVOLANG )
		self.m_button713.Bind( wx.EVT_BUTTON, self.oneMoveVOLANG )
		self.m_button813.Bind( wx.EVT_BUTTON, self.multiMoveVOLANG )
		self.m_listBox314.Bind( wx.EVT_LISTBOX, self.onSelectFLOW )
		self.m_listBox414.Bind( wx.EVT_LISTBOX, self.onSelectToMoveFLOW )
		self.m_button514.Bind( wx.EVT_BUTTON, self.oneAddFLOW )
		self.m_button614.Bind( wx.EVT_BUTTON, self.multiAddFLOW )
		self.m_button714.Bind( wx.EVT_BUTTON, self.oneMoveFLOW )
		self.m_button814.Bind( wx.EVT_BUTTON, self.multiMoveFLOW )
		self.m_listBox315.Bind( wx.EVT_LISTBOX, self.onSelectFLOWPQ )
		self.m_listBox415.Bind( wx.EVT_LISTBOX, self.onSelectToMoveFLOWPQ )
		self.m_button515.Bind( wx.EVT_BUTTON, self.oneAddFLOWPQ )
		self.m_button615.Bind( wx.EVT_BUTTON, self.multiAddFLOWPQ )
		self.m_button715.Bind( wx.EVT_BUTTON, self.oneMoveFLOWPQ )
		self.m_button815.Bind( wx.EVT_BUTTON, self.multiMoveFLOWPQ )
		self.m_listBox317.Bind( wx.EVT_LISTBOX, self.onSelectFLOWMVA )
		self.m_listBox417.Bind( wx.EVT_LISTBOX, self.onSelectToMoveFLOWMVA )
		self.m_button517.Bind( wx.EVT_BUTTON, self.oneAddFLOWMVA )
		self.m_button617.Bind( wx.EVT_BUTTON, self.multiAddFLOWMVA )
		self.m_button717.Bind( wx.EVT_BUTTON, self.oneMoveFLOWMVA )
		self.m_button817.Bind( wx.EVT_BUTTON, self.multiMoveFLOWMVA )
		self.m_listBox318.Bind( wx.EVT_LISTBOX, self.onSelectRELAY2 )
		self.m_listBox418.Bind( wx.EVT_LISTBOX, self.onSelectToMoveRELAY2 )
		self.m_button518.Bind( wx.EVT_BUTTON, self.oneAddRELAY2 )
		self.m_button618.Bind( wx.EVT_BUTTON, self.multiAddRELAY2 )
		self.m_button718.Bind( wx.EVT_BUTTON, self.oneMoveRELAY2 )
		self.m_button818.Bind( wx.EVT_BUTTON, self.multiMoveRELAY2 )
		self.m_listBox319.Bind( wx.EVT_LISTBOX, self.onSelectVAR )
		self.m_listBox419.Bind( wx.EVT_LISTBOX, self.onSelectToMoveVAR )
		self.m_button519.Bind( wx.EVT_BUTTON, self.oneAddVAR )
		self.m_button619.Bind( wx.EVT_BUTTON, self.multiAddVAR )
		self.m_button719.Bind( wx.EVT_BUTTON, self.oneMoveVAR )
		self.m_button819.Bind( wx.EVT_BUTTON, self.multiMoveVAR )
		self.m_listBox320.Bind( wx.EVT_LISTBOX, self.onSelectSTATE )
		self.m_listBox420.Bind( wx.EVT_LISTBOX, self.onSelectToMoveSTATE )
		self.m_button520.Bind( wx.EVT_BUTTON, self.oneAddSTATE )
		self.m_button620.Bind( wx.EVT_BUTTON, self.multiAddVAR )
		self.m_button720.Bind( wx.EVT_BUTTON, self.oneMoveSTATE )
		self.m_button820.Bind( wx.EVT_BUTTON, self.multiMoveSTATE )
		self.m_listBox321.Bind( wx.EVT_LISTBOX, self.onSelectMACHINETERM )
		self.m_listBox421.Bind( wx.EVT_LISTBOX, self.onSelectToMoveMACHINETERM )
		self.m_button521.Bind( wx.EVT_BUTTON, self.oneAddMACHINETERM )
		self.m_button621.Bind( wx.EVT_BUTTON, self.multiAddMACHINETERM )
		self.m_button721.Bind( wx.EVT_BUTTON, self.oneMoveMACHINETERM )
		self.m_button821.Bind( wx.EVT_BUTTON, self.multiMoveMACHINETERM )
		self.m_listBox322.Bind( wx.EVT_LISTBOX, self.onSelectMACHAPPIMP )
		self.m_listBox422.Bind( wx.EVT_LISTBOX, self.onSelectToMoveMACHAPPIMP )
		self.m_button522.Bind( wx.EVT_BUTTON, self.oneAddMACHAPPIMP )
		self.m_button622.Bind( wx.EVT_BUTTON, self.multiAddMACHAPPIMP )
		self.m_button722.Bind( wx.EVT_BUTTON, self.oneMoveMACHAPPIMP )
		self.m_button822.Bind( wx.EVT_BUTTON, self.multiMoveMACHAPPIMP )
		self.m_listBox323.Bind( wx.EVT_LISTBOX, self.onSelectVUEL )
		self.m_listBox423.Bind( wx.EVT_LISTBOX, self.onSelectToMoveVUEL )
		self.m_button523.Bind( wx.EVT_BUTTON, self.oneAddVUEL )
		self.m_button623.Bind( wx.EVT_BUTTON, self.multiAddVUEL )
		self.m_button723.Bind( wx.EVT_BUTTON, self.oneMoveVUEL )
		self.m_button823.Bind( wx.EVT_BUTTON, self.multiMoveVUEL )
		self.m_listBox324.Bind( wx.EVT_LISTBOX, self.onSelectVOEL )
		self.m_listBox424.Bind( wx.EVT_LISTBOX, self.onSelectToMoveVOEL )
		self.m_button524.Bind( wx.EVT_BUTTON, self.oneAddVOEL )
		self.m_button624.Bind( wx.EVT_BUTTON, self.multiAddVOEL )
		self.m_button724.Bind( wx.EVT_BUTTON, self.oneMoveVOEL )
		self.m_button824.Bind( wx.EVT_BUTTON, self.multiMoveVOEL )
		self.m_listBox325.Bind( wx.EVT_LISTBOX, self.onSelectPLOAD )
		self.m_listBox425.Bind( wx.EVT_LISTBOX, self.onSelectToMovePLOAD )
		self.m_button525.Bind( wx.EVT_BUTTON, self.oneAddPLOAD )
		self.m_button625.Bind( wx.EVT_BUTTON, self.multiAddPLOAD )
		self.m_button725.Bind( wx.EVT_BUTTON, self.oneMovePLOAD )
		self.m_button825.Bind( wx.EVT_BUTTON, self.multiMovePLOAD )
		self.m_listBox326.Bind( wx.EVT_LISTBOX, self.onSelectQLOAD )
		self.m_listBox426.Bind( wx.EVT_LISTBOX, self.onSelectToMoveQLOAD )
		self.m_button526.Bind( wx.EVT_BUTTON, self.oneAddQLOAD )
		self.m_button626.Bind( wx.EVT_BUTTON, self.multiAddQLOAD )
		self.m_button726.Bind( wx.EVT_BUTTON, self.oneMoveQLOAD )
		self.m_button826.Bind( wx.EVT_BUTTON, self.oneMoveQLOAD )
		self.m_listBox327.Bind( wx.EVT_LISTBOX, self.onSelectGREF )
		self.m_listBox427.Bind( wx.EVT_LISTBOX, self.onSelectToMoveGREF )
		self.m_button527.Bind( wx.EVT_BUTTON, self.oneAddGREF )
		self.m_button627.Bind( wx.EVT_BUTTON, self.multiAddGREF )
		self.m_button727.Bind( wx.EVT_BUTTON, self.oneMoveGREF )
		self.m_button827.Bind( wx.EVT_BUTTON, self.multiMoveGREF )
		self.m_listBox328.Bind( wx.EVT_LISTBOX, self.onSelectLCREF )
		self.m_listBox428.Bind( wx.EVT_LISTBOX, self.onSelectToMoveLCREF )
		self.m_button528.Bind( wx.EVT_BUTTON, self.oneAddLCREF )
		self.m_button628.Bind( wx.EVT_BUTTON, self.multiAddLCREF )
		self.m_button728.Bind( wx.EVT_BUTTON, self.oneMoveLCREF )
		self.m_button828.Bind( wx.EVT_BUTTON, self.multiMoveGREF )
		self.m_listBox329.Bind( wx.EVT_LISTBOX, self.onSelectWINDVEL )
		self.m_listBox429.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDVEL )
		self.m_button529.Bind( wx.EVT_BUTTON, self.oneAddWINDVEL )
		self.m_button629.Bind( wx.EVT_BUTTON, self.multiAddWINDVEL )
		self.m_button729.Bind( wx.EVT_BUTTON, self.oneMoveWINDVEL )
		self.m_button829.Bind( wx.EVT_BUTTON, self.multiMoveWINDVEL )
		self.m_listBox330.Bind( wx.EVT_LISTBOX, self.onSelectWINDTURSPD )
		self.m_listBox430.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDTURSPD )
		self.m_button530.Bind( wx.EVT_BUTTON, self.oneAddWINDTURSPD )
		self.m_button630.Bind( wx.EVT_BUTTON, self.multiAddWINDTURSPD )
		self.m_button730.Bind( wx.EVT_BUTTON, self.oneMoveWINDTURSPD )
		self.m_button830.Bind( wx.EVT_BUTTON, self.multiMoveWINDTURSPD )
		self.m_listBox331.Bind( wx.EVT_LISTBOX, self.onSelectWINDPITCH )
		self.m_listBox431.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDPITCH )
		self.m_button531.Bind( wx.EVT_BUTTON, self.oneAddWINDPITCH )
		self.m_button631.Bind( wx.EVT_BUTTON, self.multiAddWINDPITCH )
		self.m_button731.Bind( wx.EVT_BUTTON, self.oneMoveWINDPITCH )
		self.m_button831.Bind( wx.EVT_BUTTON, self.multiMoveWINDPITCH )
		self.m_listBox332.Bind( wx.EVT_LISTBOX, self.onSelectWINDAEROTOR )
		self.m_listBox432.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDAEROTOR )
		self.m_button532.Bind( wx.EVT_BUTTON, self.oneAddWINDAEROTOR )
		self.m_button632.Bind( wx.EVT_BUTTON, self.multiAddWINDAEROTOR )
		self.m_button732.Bind( wx.EVT_BUTTON, self.oneMoveWINDAEROTOR )
		self.m_button832.Bind( wx.EVT_BUTTON, self.multiMoveWINDAEROTOR )
		self.m_listBox333.Bind( wx.EVT_LISTBOX, self.onSelectWINDROTORVOL )
		self.m_listBox433.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDROTORVOL )
		self.m_button533.Bind( wx.EVT_BUTTON, self.oneAddWINDROTORVOL )
		self.m_button633.Bind( wx.EVT_BUTTON, self.multiAddWINDROTORVOL )
		self.m_button733.Bind( wx.EVT_BUTTON, self.oneMoveWINDROTORVOL )
		self.m_button833.Bind( wx.EVT_BUTTON, self.multiMoveWINDROTORVOL )
		self.m_listBox334.Bind( wx.EVT_LISTBOX, self.onSelectWINDROTORCUR )
		self.m_listBox434.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDROTORCUR )
		self.m_button534.Bind( wx.EVT_BUTTON, self.oneAddWINDROTORCUR )
		self.m_button634.Bind( wx.EVT_BUTTON, self.multiAddWINDROTORCUR )
		self.m_button734.Bind( wx.EVT_BUTTON, self.oneMoveWINDROTORCUR )
		self.m_button834.Bind( wx.EVT_BUTTON, self.multiMoveWINDROTORCUR )
		self.m_listBox335.Bind( wx.EVT_LISTBOX, self.onSelectWINDPCOMAND )
		self.m_listBox435.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDPCOMAND )
		self.m_button535.Bind( wx.EVT_BUTTON, self.oneAddWINDPCOMAND )
		self.m_button635.Bind( wx.EVT_BUTTON, self.multiAddWINDPCOMAND )
		self.m_button735.Bind( wx.EVT_BUTTON, self.oneMoveWINDPCOMAND )
		self.m_button835.Bind( wx.EVT_BUTTON, self.multiMoveWINDPCOMAND )
		self.m_listBox336.Bind( wx.EVT_LISTBOX, self.onSelectWINDQCOMAND )
		self.m_listBox436.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDQCOMAND )
		self.m_button536.Bind( wx.EVT_BUTTON, self.oneAddWINDQCOMAND )
		self.m_button636.Bind( wx.EVT_BUTTON, self.multiAddWINDQCOMAND )
		self.m_button736.Bind( wx.EVT_BUTTON, self.oneMoveWINDQCOMAND )
		self.m_button836.Bind( wx.EVT_BUTTON, self.multiMoveWINDQCOMAND )
		self.m_listBox337.Bind( wx.EVT_LISTBOX, self.onSelectWINDAUX )
		self.m_listBox437.Bind( wx.EVT_LISTBOX, self.onSelectToMoveWINDAUX )
		self.m_button537.Bind( wx.EVT_BUTTON, self.oneAddWINDAUX )
		self.m_button637.Bind( wx.EVT_BUTTON, self.multiAddWINDAUX )
		self.m_button737.Bind( wx.EVT_BUTTON, self.oneMoveWINDAUX )
		self.m_button837.Bind( wx.EVT_BUTTON, self.multiMoveWINDAUX )
		self.m_button2.Bind( wx.EVT_BUTTON, self.loadDyrFile_Fcn )
		self.m_button3.Bind( wx.EVT_BUTTON, self.createIDVFcn )
		self.dynProcess.Bind( wx.EVT_BUTTON, self.add_dyn_process_fcn )
		self.dynMultiProcess.Bind( wx.EVT_BUTTON, self.add_dyn_multi_process_fcn )
		self.m_radioBtn10.Bind( wx.EVT_RADIOBUTTON, self.choice1 )
		self.m_radioBtn12.Bind( wx.EVT_RADIOBUTTON, self.choice2 )
		self.m_radioBtn13.Bind( wx.EVT_RADIOBUTTON, self.choice3 )
		self.choose = 0
		self.flag = 0
		self.selectedAngle = []
		self.selectedPELEC = []
		self.selectedQELEC = []
		self.selectedETERM = []
		self.selectedEFD = []
		self.selectedPMECH = []
		self.selectedSPEED = []
		self.selectedXADIFD = []
		self.selectedVOTHSG = []
		self.selectedVREF = []
		self.selectedBSFREQ = []
		self.selectedVOLTAGE = []
		self.selectedVOLANG = []
		self.selectedFLOW = []
		self.selectedFLOWPQ = []
		self.selectedFLOWMVA = []
		self.selectedRELAY2 = []
		self.selectedVAR = []
		self.selectedSTATE = []
		self.selectedMACHINETERM = []
		self.selectedMACHAPPIMP = []
		self.selectedVUEL = []
		self.selectedVOEL = []
		self.selectedPLOAD = []
		self.selectedQLOAD = []
		self.selectedGREF = []
		self.selectedLCREF = []
		self.selectedWINDVEL = []
		self.selectedWINDTURSPD = []
		self.selectedWINDPITCH = []
		self.selectedWINDAEROTOR = []
		self.selectedWINDROTORVOL = []
		self.selectedWINDROTORCUR = []
		self.selectedWINDPCOMAND = []
		self.selectedWINDQCOMAND = []
		self.selectedWINDAUX = []
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def choice1( self, event ):
		self.choose = 1
		self.m_staticText4.Enable( True )
		self.m_comboBox1.Enable( True )
		# print(self.m_radioBtn10.GetValue(),self.m_radioBtn12.GetValue(),self.m_radioBtn13.GetValue())
		event.Skip()
	
	def choice2( self, event ):
		self.choose = 0
		self.m_staticText4.Enable( False )
		self.m_comboBox1.Enable( False )
		event.Skip()
	
	def choice3( self, event ):
		self.choose = -1
		self.m_staticText4.Enable( False )
		self.m_comboBox1.Enable( False )
		event.Skip()

	def onText_Search(self,event):
		searchText = self.m_textCtrl42.GetValue()
		items = self.m_listBox3Choices
		result = []   
		for i in range(len(items)):
			if ((str(searchText)).upper() in (str(items[i]).upper())):
				result.append(items[i])
		self.m_listBox3.SetItems(result)
		self.m_listBox31.SetItems(result)
		self.m_listBox32.SetItems(result)
		self.m_listBox33.SetItems(result)
		self.m_listBox34.SetItems(result)
		self.m_listBox35.SetItems(result)
		self.m_listBox36.SetItems(result)
		self.m_listBox37.SetItems(result)
		self.m_listBox38.SetItems(result)
		self.m_listBox39.SetItems(result)
		self.m_listBox310.SetItems(result)
		self.m_listBox311.SetItems(result)
		self.m_listBox312.SetItems(result)
		self.m_listBox313.SetItems(result)
		self.m_listBox314.SetItems(result)
		self.m_listBox315.SetItems(result)
		self.m_listBox317.SetItems(result)
		self.m_listBox318.SetItems(result)
		self.m_listBox319.SetItems(result)
		self.m_listBox320.SetItems(result)
		self.m_listBox321.SetItems(result)
		self.m_listBox322.SetItems(result)
		self.m_listBox323.SetItems(result)
		self.m_listBox324.SetItems(result)
		self.m_listBox325.SetItems(result)
		self.m_listBox326.SetItems(result)
		self.m_listBox327.SetItems(result)
		self.m_listBox328.SetItems(result)
		self.m_listBox329.SetItems(result)
		self.m_listBox330.SetItems(result)
		self.m_listBox331.SetItems(result)
		self.m_listBox332.SetItems(result)
		self.m_listBox333.SetItems(result)
		self.m_listBox334.SetItems(result)
		self.m_listBox335.SetItems(result)
		self.m_listBox336.SetItems(result)
		self.m_listBox337.SetItems(result)

		event.Skip()

	def loadDyrFile_Fcn( self, event ):
		global dyrPath
		dyrPath = openFile(self,'Choose the dyr file', "Dyr files (*.dyr)|*.dyr|All files|*")
		self.m_textCtrl1.SetValue(dyrPath)
		event.Skip()

	def onClose( self, event ):
		event.Skip()
		return self.flag
	
	def createIDVFcn( self, event ):
		# angle  = self.m_listBox4.GetValue()
		dict_of_channel = dict()
		ang =  self.m_listBox4.Items
		angleArr = []
		angleNameArr = []
		for i in range(len(ang)):
			angleArr.append(ang[i].split('-')[0])
			angleNameArr.append('ANGLE_'+ang[i].split('-')[1])
		angle = {'angleArr':angleArr,'angleNameArr':angleNameArr}
		# PELEC
		pelecChosen =  self.m_listBox41.Items
		pelecArr = []
		pelecNameArr = []
		for i in range(len(pelecChosen)):
			pelecArr.append(pelecChosen[i].split('-')[0])
			pelecNameArr.append('PELEC_'+pelecChosen[i].split('-')[1])
		pelec = {'pelecArr':pelecArr,'pelecNameArr':pelecNameArr}

		# QELEC
		qelecChosen =  self.m_listBox42.Items
		qelecArr = []
		qelecNameArr = []
		for i in range(len(qelecChosen)):
			qelecArr.append(qelecChosen[i].split('-')[0])
			qelecNameArr.append('QELEC_'+qelecChosen[i].split('-')[1])
		qelec = {'qelecArr':qelecArr,'qelecNameArr':qelecNameArr}

		# ETERM
		etermChosen =  self.m_listBox43.Items
		etermArr = []
		etermNameArr = []
		for i in range(len(etermChosen)):
			etermArr.append(etermChosen[i].split('-')[0])
			etermNameArr.append('ETERM_'+ etermChosen[i].split('-')[1])
		eterm = {'etermArr':etermArr,'etermNameArr':etermNameArr}

		# EFD
		efdChosen =  self.m_listBox44.Items
		efdArr = []
		efdNameArr = []
		for i in range(len(efdChosen)):
			efdArr.append(efdChosen[i].split('-')[0])
			efdNameArr.append('EFD_'+efdChosen[i].split('-')[1])
		efd = {'efdArr':efdArr,'efdNameArr':efdNameArr}

		# pmech
		pmechChosen =  self.m_listBox45.Items
		pmechArr = []
		pmechNameArr = []
		for i in range(len(pmechChosen)):
			pmechArr.append(pmechChosen[i].split('-')[0])
			pmechNameArr.append('PMECH_'+pmechChosen[i].split('-')[1])
		pmech = {'pmechArr':pmechArr,'pmechNameArr':pmechNameArr}

		# SPEED
		speedChosen =  self.m_listBox46.Items
		speedArr = []
		speedNameArr = []
		for i in range(len(speedChosen)):
			speedArr.append(speedChosen[i].split('-')[0])
			speedNameArr.append('SPEED_'+speedChosen[i].split('-')[1])
		speed = {'speedArr':speedArr,'speedNameArr':speedNameArr}

		# XADIFD
		xadifdChosen =  self.m_listBox47.Items
		xadifdArr = []
		xadifdNameArr = []
		for i in range(len(xadifdChosen)):
			xadifdArr.append(xadifdChosen[i].split('-')[0])
			xadifdNameArr.append('XADIFD_'+xadifdChosen[i].split('-')[1])
		xadifd = {'xadifdArr':xadifdArr,'xadifdNameArr':xadifdNameArr}

		# ECOMP
		ecompChosen =  self.m_listBox48.Items
		ecompArr = []
		ecompNameArr = []
		for i in range(len(ecompChosen)):
			ecompArr.append(ecompChosen[i].split('-')[0])
			ecompNameArr.append('ECOMP_'+ecompChosen[i].split('-')[1])
		ecomp = {'ecompArr':ecompArr,'ecompNameArr':ecompNameArr}

		# VOTHSG
		vothsgChosen =  self.m_listBox49.Items
		vothsgArr = []
		vothsgNameArr = []
		for i in range(len(vothsgChosen)):
			vothsgArr.append(vothsgChosen[i].split('-')[0])
			vothsgNameArr.append('VOTHSG_'+vothsgChosen[i].split('-')[1])
		vothsg = {'vothsgArr':vothsgArr,'vothsgNameArr':vothsgNameArr}

		# vref
		vrefChosen =  self.m_listBox410.Items
		vrefArr = []
		vrefNameArr = []
		for i in range(len(vrefChosen)):
			vrefArr.append(vrefChosen[i].split('-')[0])
			vrefNameArr.append('VREF_'+vrefChosen[i].split('-')[1])
		vref = {'vrefArr':vrefArr,'vrefNameArr':vrefNameArr}

		# bsfreq
		bsfreqChosen =  self.m_listBox411.Items
		bsfreqArr = []
		bsfreqNameArr = []
		for i in range(len(bsfreqChosen)):
			bsfreqArr.append(bsfreqChosen[i].split('-')[0])
			bsfreqNameArr.append('BSFREQ_'+bsfreqChosen[i].split('-')[1])
		bsfreq = {'bsfreqArr':bsfreqArr,'bsfreqNameArr':bsfreqNameArr}

		# VOLTAGE
		voltageChosen =  self.m_listBox412.Items
		voltageArr = []
		voltageNameArr = []
		for i in range(len(voltageChosen)):
			voltageArr.append(voltageChosen[i].split('-')[0])
			voltageNameArr.append('VOLTAGE_'+voltageChosen[i].split('-')[1])
		voltage = {'voltageArr':voltageArr,'voltageNameArr':voltageNameArr}

		# VOLANG
		volangChosen =  self.m_listBox413.Items
		volangArr = []
		volangNameArr = []
		for i in range(len(volangChosen)):
			volangArr.append(volangChosen[i].split('-')[0])
			volangNameArr.append('VOLANG_'+volangChosen[i].split('-')[1])
		volang = {'volangArr':volangArr,'volangNameArr':volangNameArr}

		# FLOW
		flowChosen =  self.m_listBox414.Items
		flowArr = []
		flowNameArr = []
		for i in range(len(flowChosen)):
			flowArr.append(flowChosen[i].split('-')[0])
			flowNameArr.append('FLOW_'+flowChosen[i].split('-')[1])
		flow = {'flowArr':flowArr,'flowNameArr':flowNameArr}

		# FLOWPQ
		flowpqChosen =  self.m_listBox415.Items
		flowpqArr = []
		flowpqNameArr = []
		for i in range(len(flowpqChosen)):
			flowpqArr.append(flowpqChosen[i].split('-')[0])
			flowpqNameArr.append('FLOWPQ_'+flowpqChosen[i].split('-')[1])
		flowpq = {'flowpqArr':flowpqArr,'flowpqNameArr':flowpqNameArr}

		# FLOWMVA
		flowmvaChosen =  self.m_listBox417.Items
		flowmvaArr = []
		flowmvaNameArr = []
		for i in range(len(flowmvaChosen)):
			flowmvaArr.append(flowmvaChosen[i].split('-')[0])
			flowmvaNameArr.append('FLOWPQ_'+flowmvaChosen[i].split('-')[1])
		flowmva = {'flowmvaArr':flowmvaArr,'flowmvaNameArr':flowmvaNameArr}

		# RELAY2
		relay2Chosen =  self.m_listBox418.Items
		relay2Arr = []
		relay2NameArr = []
		for i in range(len(relay2Chosen)):
			relay2Arr.append(relay2Chosen[i].split('-')[0])
			relay2NameArr.append('RELAY2_'+relay2Chosen[i].split('-')[1])
		relay2 = {'relay2Arr':relay2Arr,'relay2NameArr':relay2NameArr}

		# VAR
		varChosen =  self.m_listBox419.Items
		varArr = []
		varNameArr = []
		for i in range(len(varChosen)):
			varArr.append(varChosen[i].split('-')[0])
			varNameArr.append('VAR_'+varChosen[i].split('-')[1])
		var = {'varArr':varArr,'varNameArr':varNameArr}

		# STATE
		stateChosen =  self.m_listBox420.Items
		stateArr = []
		stateNameArr = []
		for i in range(len(stateChosen)):
			stateArr.append(stateChosen[i].split('-')[0])
			stateNameArr.append('STATE_'+stateChosen[i].split('-')[1])
		state = {'stateArr':stateArr,'stateNameArr':stateNameArr}

		# MACHINETERM
		machinetermChosen =  self.m_listBox421.Items
		machinetermArr = []
		machinetermNameArr = []
		for i in range(len(machinetermChosen)):
			machinetermArr.append(machinetermChosen[i].split('-')[0])
			machinetermNameArr.append('MACHINETERM_'+machinetermChosen[i].split('-')[1])
		machineterm = {'machinetermArr':machinetermArr,'machinetermNameArr':machinetermNameArr}

		# MACHAPPIMP
		machappimpChosen =  self.m_listBox422.Items
		machappimpArr = []
		machappimpNameArr = []
		for i in range(len(machappimpChosen)):
			machappimpArr.append(machappimpChosen[i].split('-')[0])
			machappimpNameArr.append('MACHAPPIMP_'+machappimpChosen[i].split('-')[1])
		machappimp = {'machappimpArr':machappimpArr,'machappimpNameArr':machappimpNameArr}

		# VUEL
		vuelChosen =  self.m_listBox423.Items
		vuelArr = []
		vuelNameArr = []
		for i in range(len(vuelChosen)):
			vuelArr.append(vuelChosen[i].split('-')[0])
			vuelNameArr.append('VUEL_'+vuelChosen[i].split('-')[1])
		vuel = {'vuelArr':vuelArr,'vuelNameArr':vuelNameArr}

		# VOEL
		voelChosen =  self.m_listBox424.Items
		voelArr = []
		voelNameArr = []
		for i in range(len(voelChosen)):
			voelArr.append(voelChosen[i].split('-')[0])
			voelNameArr.append('VOEL_'+voelChosen[i].split('-')[1])
		voel = {'voelArr':voelArr,'voelNameArr':voelNameArr}

		# PLOAD
		ploadChosen =  self.m_listBox425.Items
		ploadArr = []
		ploadNameArr = []
		for i in range(len(ploadChosen)):
			ploadArr.append(ploadChosen[i].split('-')[0])
			ploadNameArr.append('PLOAD_'+ploadChosen[i].split('-')[1])
		pload = {'ploadArr':ploadArr,'ploadNameArr':ploadNameArr}

		# QLOAD
		qloadChosen =  self.m_listBox426.Items
		qloadArr = []
		qloadNameArr = []
		for i in range(len(qloadChosen)):
			qloadArr.append(qloadChosen[i].split('-')[0])
			qloadNameArr.append('QLOAD_'+qloadChosen[i].split('-')[1])
		qload = {'qloadArr':qloadArr,'qloadNameArr':qloadNameArr}

		# GREF
		grefChosen =  self.m_listBox427.Items
		grefArr = []
		grefNameArr = []
		for i in range(len(grefChosen)):
			grefArr.append(grefChosen[i].split('-')[0])
			grefNameArr.append('GREF_'+grefChosen[i].split('-')[1])
		gref = {'grefArr':grefArr,'grefNameArr':grefNameArr}

		# LCREF
		lcrefChosen =  self.m_listBox428.Items
		lcrefArr = []
		lcrefNameArr = []
		for i in range(len(lcrefChosen)):
			lcrefArr.append(lcrefChosen[i].split('-')[0])
			lcrefNameArr.append('LCREF_'+lcrefChosen[i].split('-')[1])
		lcref = {'lcrefArr':lcrefArr,'lcrefNameArr':lcrefNameArr}

		# WINDVEL
		windvelChosen =  self.m_listBox429.Items
		windvelArr = []
		windvelNameArr = []
		for i in range(len(windvelChosen)):
			windvelArr.append(windvelChosen[i].split('-')[0])
			windvelNameArr.append('WINDVEL_'+windvelChosen[i].split('-')[1])
		windvel = {'windvelArr':windvelArr,'windvelNameArr':windvelNameArr}

		# WINDTURSPD
		windturspdChosen =  self.m_listBox430.Items
		windturspdArr = []
		windturspdNameArr = []
		for i in range(len(windturspdChosen)):
			windturspdArr.append(windturspdChosen[i].split('-')[0])
			windturspdNameArr.append('WINDTURSPD_'+windturspdChosen[i].split('-')[1])
		windturspd = {'windturspdArr':windturspdArr,'windturspdNameArr':windturspdNameArr}

		# WINDPITCH
		windpitchChosen =  self.m_listBox431.Items
		windpitchArr = []
		windpitchNameArr = []
		for i in range(len(windpitchChosen)):
			windpitchArr.append(windpitchChosen[i].split('-')[0])
			windpitchNameArr.append('WINDPITCH_'+windpitchChosen[i].split('-')[1])
		windpitch = {'windpitchArr':windpitchArr,'windpitchNameArr':windpitchNameArr}

		#WINDAEROTOR
		windaerotorChosen =  self.m_listBox432.Items
		windaerotorArr = []
		windaerotorNameArr = []
		for i in range(len(windaerotorChosen)):
			windaerotorArr.append(windaerotorChosen[i].split('-')[0])
			windaerotorNameArr.append('WINDAEROTOR_'+windaerotorChosen[i].split('-')[1])
		windaerotor = {'windaerotorArr':windaerotorArr,'windaerotorNameArr':windaerotorNameArr}

		# WINDROTORVOL
		windrotorvolChosen =  self.m_listBox433.Items
		windrotorvolArr = []
		windrotorvolNameArr = []
		for i in range(len(windrotorvolChosen)):
			windrotorvolArr.append(windrotorvolChosen[i].split('-')[0])
			windrotorvolNameArr.append('WINDROTORVOL_'+windrotorvolChosen[i].split('-')[1])
		windrotorvol = {'windrotorvolArr':windrotorvolArr,'windrotorvolNameArr':windrotorvolNameArr}

		# WINDROTORCUR
		windrotorcurChosen =  self.m_listBox434.Items
		windrotorcurArr = []
		windrotorcurNameArr = []
		for i in range(len(windrotorcurChosen)):
			windrotorcurArr.append(windrotorcurChosen[i].split('-')[0])
			windrotorcurNameArr.append('WINDROTORCUR_'+windrotorcurChosen[i].split('-')[1])
		windrotorcur = {'windrotorcurArr':windrotorcurArr,'windrotorcurNameArr':windrotorcurNameArr}

		# WINDPCOMAND
		windpcomandChosen =  self.m_listBox435.Items
		windpcomandArr = []
		windpcomandNameArr = []
		for i in range(len(windpcomandChosen)):
			windpcomandArr.append(windpcomandChosen[i].split('-')[0])
			windpcomandNameArr.append('WINDPCOMAND_'+windpcomandChosen[i].split('-')[1])
		windpcomand = {'windpcomandArr':windpcomandArr,'windpcomandNameArr':windpcomandNameArr}

		# WINDQCOMAND
		windqcomandChosen =  self.m_listBox436.Items
		windqcomandArr = []
		windqcomandNameArr = []
		for i in range(len(windqcomandChosen)):
			windqcomandArr.append(windqcomandChosen[i].split('-')[0])
			windqcomandNameArr.append('WINDQCOMAND_'+windqcomandChosen[i].split('-')[1])
		windqcomand = {'windqcomandArr':windqcomandArr,'windqcomandNameArr':windqcomandNameArr}

		# WINDAUX
		windauxChosen =  self.m_listBox437.Items
		windauxArr = []
		windauxNameArr = []
		for i in range(len(windauxChosen)):
			windauxArr.append(windauxChosen[i].split('-')[0])
			windauxNameArr.append('WINDAUX_'+windauxChosen[i].split('-')[1])
		windaux = {'windauxArr':windauxArr,'windauxNameArr':windauxNameArr}

		dict_of_channel = {'angle':angle,
						   'pelec':pelec,
						   'qelec':qelec,
						   'eterm':eterm,
						   'efd':efd,
						   'pmech':pmech,
						   'speed':speed,
						   'xadifd':xadifd,
						   'ecomp':ecomp,
						   'vothsg':vothsg,
						   'vref':vref,
						   'bsfreq':bsfreq,
						   'voltage':voltage,
						   'volang':volang,
						   'flow':flow,
						   'flowpq':flowpq,
						   'flowmva':flowmva,
						   'relay2':relay2,
						   'var':var,
						   'state':state,
						   'machineterm':machineterm,
						   'machappimp':machappimp,
						   'vuel':vuel,
						   'voel':voel,
						   'pload':pload,
						   'qload':qload,
						   'gref':gref,
						   'lcref':lcref,
						   'windvel':windvel,
						   'windturspd':windturspd,
						   'windpitch':windpitch,
						   'windaerotor':windaerotor,
						   'windrotorvol':windrotorvol,
						   'windrotorcur':windrotorcur,
						   'windpcomand':windpcomand,
						   'windqcomand':windqcomand,
						   'windaux':windaux}

		
		if self.m_textCtrl1.GetValue() =="":
			wx.MessageBox('Dyr file can not null!')
		elif len(ang)==0:
			wx.MessageBox('Choose at least one channel!')
		elif self.m_radioBtn10.GetValue()==True and self.m_comboBox1.GetValue() == '':
			wx.MessageBox('Gen number cannot null!')
		else:
			idv2py=createIDVFile(dyrPath,dict_of_channel,self.choose)
			with open('output', 'w') as f, silence(f):
				execfile(idv2py)
			r = open('output','r')
			lines = r.readlines()
			flag = 1
			errorLine = 0
			endline = 0
			for line,value in enumerate(lines):
				if "INITIAL CONDITIONS CHECK O.K." in value:
					wx.MessageBox('INITIAL CONDITIONS CHECK O.K!')
					flag = 0
				elif "ssn1.snp" in value:
					errorLine = line
				if "PTI INTERACTIVE POWER SYSTEM SIMULATOR--PSS(R)E" in value:
					endLine = line
			if flag == 1:
				error = ''
				for i in range(int(errorLine)+2,int(endLine)):
					error = error +'\n'+ lines[i]

				wx.MessageBox('There is an error in:{A}\n '.format(A=error))
			r.close()
			os.remove('output')

	def add_dyn_process_fcn( self, event ):
		pyFile = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
		dirname = os.path.dirname(pyFile)
		path = os.path.join(dirname,'dynamic_process.py')
		createIncidentFile(pyFile)
		
		execfile(path)

		call(('cmd','/c','start','',os.path.join(dirname+'\\sme.sav')))
		event.Skip()

	def add_dyn_multi_process_fcn( self, event):
		dirName = openFolder(self,'Choose the Folder contain all py files')
		os.chdir(dirName)
		pyFileNames = glob.glob('*.py')
		
		for pyFile in pyFileNames:
			pyName = os.path.basename(pyFile)
			if pyName <> 'dynamic_process.py' and pyName <> 'idv2py.py':
				path = os.path.join(dirName,'dynamic_process.py')
				pyPath = os.path.join(dirName,pyFile)
				createIncidentFile(pyPath)
				execfile(path)
				os.remove(path)
		event.Skip()	

	def onSelectAngle( self, event ):
		global busNum_Angle
		busNum_Angle = self.m_listBox3.GetSelections()
		for i in range(len(busNum_Angle)):
			obj = self.m_listBox3.GetString(busNum_Angle[i])
	
	def onSelectToMoveAngle( self, event ):
		global moveBus_Angle
		moveBus_Angle = self.m_listBox4.GetSelections()
		for i in range(len(moveBus_Angle)):
			obj = self.m_listBox4.GetString(moveBus_Angle[i])
	
	def oneAddAngle( self, event ):
		for i in range(len(busNum_Angle)):
			obj = self.m_listBox3.GetString(busNum_Angle[i])
			if not obj in self.m_listBox4.Items:
				self.selectedAngle.append(obj)
				self.m_listBox4.Append(obj)
	
	def multiAddAngle( self, event ):
		b  = self.m_listBox3.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox4.Items:
				self.m_listBox4.Append(obj)
	
	def oneMoveAngle( self, event ):
		for i in range(len(moveBus_Angle)):
			obj = self.m_listBox4.GetString(len(moveBus_Angle)-1-i)
			self.m_listBox4.Delete(moveBus_Angle[len(moveBus_Angle)-1-i])
	
	def multiMoveAngle( self, event ):
		b  = self.m_listBox4.Items
		for i in range(len(b)):
			obj = self.m_listBox3.GetString(i)
			self.m_listBox4.Delete(len(b)-1-i)
	
	def onSelectPELEC( self, event ):
		global busNum_PELEC
		busNum_PELEC = self.m_listBox31.GetSelections()
		for i in range(len(busNum_PELEC)):
			obj = self.m_listBox31.GetString(busNum_PELEC[i])
		event.Skip()
	
	def onSelectToMovePELEC( self, event ):
		global moveBus_PELEC
		moveBus_PELEC = self.m_listBox41.GetSelections()
		for i in range(len(moveBus_PELEC)):
			obj = self.m_listBox41.GetString(moveBus_PELEC[i])
	
	def oneAddPELEC( self, event ):
		for i in range(len(busNum_PELEC)):
			obj = self.m_listBox31.GetString(busNum_PELEC[i])
			if not obj in self.m_listBox41.Items:
				self.selectedPELEC.append(obj)
				self.m_listBox41.Append(obj)
	
	def multiAddPELEC( self, event ):
		b  = self.m_listBox31.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox41.Items:
				self.m_listBox41.Append(obj)
	
	def oneMovePELEC( self, event ):
		for i in range(len(moveBus_PELEC)):
			obj = self.m_listBox41.GetString(len(moveBus_PELEC)-1-i)
			self.m_listBox41.Delete(moveBus_PELEC[len(moveBus_PELEC)-1-i])
	
	def multiMovePELEC( self, event ):
		b  = self.m_listBox41.Items
		for i in range(len(b)):
			obj = self.m_listBox31.GetString(i)
			self.m_listBox41.Delete(len(b)-1-i)
	
	def onSelectQELEC( self, event ):
		global busNum_QELEC
		busNum_QELEC = self.m_listBox32.GetSelections()
		for i in range(len(busNum_QELEC)):
			obj = self.m_listBox32.GetString(busNum_QELEC[i])
		event.Skip()
	
	def onSelectToMoveQELEC( self, event ):
		global moveBus_QELEC
		moveBus_QELEC = self.m_listBox42.GetSelections()
		for i in range(len(moveBus_QELEC)):
			obj = self.m_listBox42.GetString(moveBus_QELEC[i])
	
	def oneAddQELEC( self, event ):
		for i in range(len(busNum_QELEC)):
			obj = self.m_listBox32.GetString(busNum_QELEC[i])
			if not obj in self.m_listBox42.Items:
				self.selectedQELEC.append(obj)
				self.m_listBox42.Append(obj)
	
	def multiAddQELEC( self, event ):
		b  = self.m_listBox32.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox41.Items:
				self.m_listBox42.Append(obj)
	
	def oneMoveQELEC( self, event ):
		for i in range(len(moveBus_QELEC)):
			obj = self.m_listBox42.GetString(len(moveBus_QELEC)-1-i)
			self.m_listBox42.Delete(moveBus_QELEC[len(moveBus_QELEC)-1-i])
	
	def multiMoveQELEC( self, event ):
		b  = self.m_listBox42.Items
		for i in range(len(b)):
			obj = self.m_listBox32.GetString(i)
			self.m_listBox42.Delete(len(b)-1-i)
	
	def onSelectETERM( self, event ):
		global busNum_ETERM
		busNum_ETERM = self.m_listBox33.GetSelections()
		for i in range(len(busNum_ETERM)):
			obj = self.m_listBox33.GetString(busNum_ETERM[i])
		event.Skip()
	
	def onSelectToMoveETERM( self, event ):
		global moveBus_ETERM
		moveBus_ETERM = self.m_listBox43.GetSelections()
		for i in range(len(moveBus_ETERM)):
			obj = self.m_listBox43.GetString(moveBus_ETERM[i])
	
	def oneAddETERM( self, event ):
		for i in range(len(busNum_ETERM)):
			obj = self.m_listBox33.GetString(busNum_ETERM[i])
			if not obj in self.m_listBox43.Items:
				self.selectedETERM.append(obj)
				self.m_listBox43.Append(obj)
	
	def multiAddETERM( self, event ):
		b  = self.m_listBox33.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox43.Items:
				self.m_listBox43.Append(obj)
	
	def oneMoveETERM( self, event ):
		for i in range(len(moveBus_ETERM)):
			obj = self.m_listBox43.GetString(len(moveBus_ETERM)-1-i)
			self.m_listBox43.Delete(moveBus_ETERM[len(moveBus_ETERM)-1-i])
	
	def multiMoveETERM( self, event ):
		b  = self.m_listBox43.Items
		for i in range(len(b)):
			obj = self.m_listBox33.GetString(i)
			self.m_listBox43.Delete(len(b)-1-i)
	
	def onSelectEFD( self, event ):
		global busNum_EFD
		busNum_EFD = self.m_listBox34.GetSelections()
		for i in range(len(busNum_EFD)):
			obj = self.m_listBox34.GetString(busNum_EFD[i])
		event.Skip()
	
	def onSelectToMoveEFD( self, event ):
		global moveBus_EFD
		moveBus_EFD = self.m_listBox44.GetSelections()
		for i in range(len(moveBus_EFD)):
			obj = self.m_listBox44.GetString(moveBus_EFD[i])
	
	def oneAddEFD( self, event ):
		for i in range(len(busNum_EFD)):
			obj = self.m_listBox34.GetString(busNum_EFD[i])
			if not obj in self.m_listBox44.Items:
				self.selectedEFD.append(obj)
				self.m_listBox44.Append(obj)
	
	def multiAddEFD( self, event ):
		b  = self.m_listBox34.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox44.Items:
				self.m_listBox44.Append(obj)
	
	def oneMoveEFD( self, event ):
		for i in range(len(moveBus_EFD)):
			obj = self.m_listBox44.GetString(len(moveBus_EFD)-1-i)
			self.m_listBox44.Delete(moveBus_EFD[len(moveBus_EFD)-1-i])
	
	def multiMoveEFD( self, event ):
		b  = self.m_listBox44.Items
		for i in range(len(b)):
			obj = self.m_listBox34.GetString(i)
			self.m_listBox44.Delete(len(b)-1-i)
	
	def onSelectPMECH( self, event ):
		global busNum_PMECH
		busNum_PMECH = self.m_listBox35.GetSelections()
		for i in range(len(busNum_PMECH)):
			obj = self.m_listBox35.GetString(busNum_PMECH[i])
		event.Skip()
	
	def onSelectToMovePMECH( self, event ):
		global moveBus_PMECH
		moveBus_PMECH = self.m_listBox45.GetSelections()
		for i in range(len(moveBus_PMECH)):
			obj = self.m_listBox45.GetString(moveBus_PMECH[i])
	
	def oneAddPMECH( self, event ):
		for i in range(len(busNum_PMECH)):
			obj = self.m_listBox35.GetString(busNum_PMECH[i])
			if not obj in self.m_listBox45.Items:
				self.selectedPMECH.append(obj)
				self.m_listBox45.Append(obj)

	def multiAddPMECH( self, event ):
		b  = self.m_listBox35.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox45.Items:
				self.m_listBox45.Append(obj)
	
	def oneMovePMECH( self, event ):
		for i in range(len(moveBus_PMECH)):
			obj = self.m_listBox45.GetString(len(moveBus_PMECH)-1-i)
			self.m_listBox45.Delete(moveBus_PMECH[len(moveBus_PMECH)-1-i])
	
	def multiMovePMECH( self, event ):
		b  = self.m_listBox45.Items
		for i in range(len(b)):
			obj = self.m_listBox35.GetString(i)
			self.m_listBox45.Delete(len(b)-1-i)
	
	def onSelectSPEED( self, event ):
		global busNum_SPEED
		busNum_SPEED = self.m_listBox36.GetSelections()
		for i in range(len(busNum_SPEED)):
			obj = self.m_listBox36.GetString(busNum_SPEED[i])
		event.Skip()
	
	def onSelectToMoveSPEED( self, event ):
		global moveBus_SPEED
		moveBus_SPEED = self.m_listBox46.GetSelections()
		for i in range(len(moveBus_SPEED)):
			obj = self.m_listBox46.GetString(moveBus_SPEED[i])
	
	def oneAddSPEED( self, event ):
		for i in range(len(busNum_SPEED)):
			obj = self.m_listBox36.GetString(busNum_SPEED[i])
			if not obj in self.m_listBox46.Items:
				self.selectedSPEED.append(obj)
				self.m_listBox46.Append(obj)
	
	def multiAddSPEED( self, event ):
		b  = self.m_listBox36.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox46.Items:
				self.m_listBox46.Append(obj)
	
	def oneMoveSPEED( self, event ):
		for i in range(len(moveBus_SPEED)):
			obj = self.m_listBox46.GetString(len(moveBus_SPEED)-1-i)
			self.m_listBox46.Delete(moveBus_SPEED[len(moveBus_SPEED)-1-i])
	
	def multiMoveSPEED( self, event ):
		b  = self.m_listBox46.Items
		for i in range(len(b)):
			obj = self.m_listBox36.GetString(i)
			self.m_listBox46.Delete(len(b)-1-i)
	
	def onSelectXADIFD( self, event ):
		global busNum_XADIFD
		busNum_XADIFD = self.m_listBox37.GetSelections()
		for i in range(len(busNum_XADIFD)):
			obj = self.m_listBox37.GetString(busNum_XADIFD[i])
		event.Skip()
	
	def onSelectToMoveXADIFD( self, event ):
		global moveBus_XADIFD
		moveBus_XADIFD = self.m_listBox47.GetSelections()
		for i in range(len(moveBus_XADIFD)):
			obj = self.m_listBox47.GetString(moveBus_XADIFD[i])
	
	def oneAddXADIFD( self, event ):
		for i in range(len(busNum_XADIFD)):
			obj = self.m_listBox37.GetString(busNum_XADIFD[i])
			if not obj in self.m_listBox47.Items:
				self.selectedXADIFD.append(obj)
				self.m_listBox47.Append(obj)
	
	def multiAddXADIFD( self, event ):
		b  = self.m_listBox37.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox47.Items:
				self.m_listBox47.Append(obj)
	
	def oneMoveXADIFD( self, event ):
		for i in range(len(moveBus_XADIFD)):
			obj = self.m_listBox47.GetString(len(moveBus_XADIFD)-1-i)
			self.m_listBox47.Delete(moveBus_XADIFD[len(moveBus_XADIFD)-1-i])
	
	def multiMoveXADIFD( self, event ):
		b  = self.m_listBox47.Items
		for i in range(len(b)):
			obj = self.m_listBox37.GetString(i)
			self.m_listBox47.Delete(len(b)-1-i)
	
	def onSelectECOMP( self, event ):
		global busNum_ECOMP
		busNum_ECOMP = self.m_listBox38.GetSelections()
		for i in range(len(busNum_ECOMP)):
			obj = self.m_listBox38.GetString(busNum_ECOMP[i])
		event.Skip()
	
	def onSelectToMoveECOMP( self, event ):
		global moveBus_ECOMP
		moveBus_ECOMP = self.m_listBox48.GetSelections()
		for i in range(len(moveBus_ECOMP)):
			obj = self.m_listBox48.GetString(moveBus_ECOMP[i])
	
	def oneAddECOMP( self, event ):
		for i in range(len(busNum_ECOMP)):
			obj = self.m_listBox3.GetString(busNum_ECOMP[i])
			if not obj in self.m_listBox48.Items:
				self.selectedECOMP.append(obj)
				self.m_listBox48.Append(obj)
	
	def multiAddECOMP( self, event ):
		b  = self.m_listBox38.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox48.Items:
				self.m_listBox48.Append(obj)

	def oneMoveECOMP( self, event ):
		for i in range(len(moveBus_ECOMP)):
			obj = self.m_listBox48.GetString(len(moveBus_ECOMP)-1-i)
			self.m_listBox48.Delete(moveBus_ECOMP[len(moveBus_ECOMP)-1-i])

	def multiMoveECOMP( self, event ):
		b  = self.m_listBox48.Items
		for i in range(len(b)):
			obj = self.m_listBox38.GetString(i)
			self.m_listBox48.Delete(len(b)-1-i)

	def onSelectVOTHSG( self, event ):
		global busNum_VOTHSG
		busNum_VOTHSG = self.m_listBox39.GetSelections()
		for i in range(len(busNum_VOTHSG)):
			obj = self.m_listBox39.GetString(busNum_VOTHSG[i])
		event.Skip()
	
	def onSelectToMoveVOTHSG( self, event ):
		global moveBus_VOTHSG
		moveBus_VOTHSG = self.m_listBox49.GetSelections()
		for i in range(len(moveBus_VOTHSG)):
			obj = self.m_listBox49.GetString(moveBus_VOTHSG[i])
	
	def oneAddVOTHSG( self, event ):
		for i in range(len(busNum_VOTHSG)):
			obj = self.m_listBox39.GetString(busNum_VOTHSG[i])
			if not obj in self.m_listBox49.Items:
				self.selectedVOTHSG.append(obj)
				self.m_listBox49.Append(obj)
	
	def multiAddVOTHSG( self, event ):
		b  = self.m_listBox39.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox49.Items:
				self.m_listBox49.Append(obj)
	
	def oneMoveVOTHSG( self, event ):
		for i in range(len(moveBus_VOTHSG)):
			obj = self.m_listBox49.GetString(len(moveBus_VOTHSG)-1-i)
			self.m_listBox49.Delete(moveBus_VOTHSG[len(moveBus_VOTHSG)-1-i])
	
	def multiMoveVOTHSG( self, event ):
		b  = self.m_listBox49.Items
		for i in range(len(b)):
			obj = self.m_listBox39.GetString(i)
			self.m_listBox49.Delete(len(b)-1-i)
	
	def onSelectVREF( self, event ):
		global busNum_VREF
		busNum_VREF = self.m_listBox310.GetSelections()
		for i in range(len(busNum_VREF)):
			obj = self.m_listBox310.GetString(busNum_VREF[i])
		event.Skip()
	
	def onSelectToMoveVREF( self, event ):
		global moveBus_VREF
		moveBus_VREF = self.m_listBox410.GetSelections()
		for i in range(len(moveBus_VREF)):
			obj = self.m_listBox410.GetString(moveBus_VREF[i])
	
	def oneAddVREF( self, event ):
		for i in range(len(busNum_VREF)):
			obj = self.m_listBox310.GetString(busNum_VREF[i])
			if not obj in self.m_listBox410.Items:
				self.selectedVREF.append(obj)
				self.m_listBox410.Append(obj)
	
	def multiAddVREF( self, event ):
		b  = self.m_listBox310.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox410.Items:
				self.m_listBox410.Append(obj)
	
	def oneMoveVREF( self, event ):
		for i in range(len(moveBus_VREF)):
			obj = self.m_listBox410.GetString(len(moveBus_VREF)-1-i)
			self.m_listBox410.Delete(moveBus_VREF[len(moveBus_VREF)-1-i])
	
	def multiMoveVREF( self, event ):
		b  = self.m_listBox410.Items
		for i in range(len(b)):
			obj = self.m_listBox310.GetString(i)
			self.m_listBox410.Delete(len(b)-1-i)
	
	def onSelectBSFREQ( self, event ):
		global busNum_BSFREQ
		busNum_BSFREQ = self.m_listBox311.GetSelections()
		for i in range(len(busNum_BSFREQ)):
			obj = self.m_listBox311.GetString(busNum_BSFREQ[i])
		event.Skip()
	
	def onSelectToMoveBSFREQ( self, event ):
		global moveBus_BSFREQ
		moveBus_BSFREQ = self.m_listBox411.GetSelections()
		for i in range(len(moveBus_BSFREQ)):
			obj = self.m_listBox411.GetString(moveBus_BSFREQ[i])
	
	def oneAddBSFREQ( self, event ):
		for i in range(len(busNum_BSFREQ)):
			obj = self.m_listBox311.GetString(busNum_BSFREQ[i])
			if not obj in self.m_listBox411.Items:
				self.selectedBSFREQ.append(obj)
				self.m_listBox411.Append(obj)
	
	def multiAddBSFREQ( self, event ):
		b  = self.m_listBox311.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox411.Items:
				self.m_listBox411.Append(obj)
	
	def oneMoveBSFREQ( self, event ):
		for i in range(len(moveBus_BSFREQ)):
			obj = self.m_listBox411.GetString(len(moveBus_BSFREQ)-1-i)
			self.m_listBox411.Delete(moveBus_BSFREQ[len(moveBus_BSFREQ)-1-i])
	
	def multiMoveBSFREQ( self, event ):
		b  = self.m_listBox411.Items
		for i in range(len(b)):
			obj = self.m_listBox311.GetString(i)
			self.m_listBox411.Delete(len(b)-1-i)
	
	def onSelectVOLTAGE( self, event ):
		global busNum_VOLTAGE
		busNum_VOLTAGE = self.m_listBox312.GetSelections()
		for i in range(len(busNum_VOLTAGE)):
			obj = self.m_listBox312.GetString(busNum_VOLTAGE[i])
		event.Skip()
	
	def onSelectToMoveVOLTAGE( self, event ):
		global moveBus_VOLTAGE
		moveBus_VOLTAGE = self.m_listBox412.GetSelections()
		for i in range(len(moveBus_VOLTAGE)):
			obj = self.m_listBox412.GetString(moveBus_VOLTAGE[i])
	
	def oneAddVOLTAGE( self, event ):
		for i in range(len(busNum_VOLTAGE)):
			obj = self.m_listBox312.GetString(busNum_VOLTAGE[i])
			if not obj in self.m_listBox412.Items:
				self.selectedVOLTAGE.append(obj)
				self.m_listBox412.Append(obj)
	
	def multiAddVOLTAGE( self, event ):
		b  = self.m_listBox312.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox412.Items:
				self.m_listBox412.Append(obj)

	def oneMoveVOLTAGE( self, event ):
		for i in range(len(moveBus_VOLTAGE)):
			obj = self.m_listBox412.GetString(len(moveBus_VOLTAGE)-1-i)
			self.m_listBox412.Delete(moveBus_VOLTAGE[len(moveBus_VOLTAGE)-1-i])

	def multiMoveVOLTAGE( self, event ):
		b  = self.m_listBox412.Items
		for i in range(len(b)):
			obj = self.m_listBox312.GetString(i)
			self.m_listBox412.Delete(len(b)-1-i)

	def onSelectVOLANG( self, event ):
		global busNum_VOLANG
		busNum_VOLANG = self.m_listBox313.GetSelections()
		for i in range(len(busNum_VOLANG)):
			obj = self.m_listBox313.GetString(busNum_VOLANG[i])
		event.Skip()
	
	def onSelectToMoveVOLANG( self, event ):
		global moveBus_VOLANG
		moveBus_VOLANG = self.m_listBox413.GetSelections()
		for i in range(len(moveBus_VOLANG)):
			obj = self.m_listBox413.GetString(moveBus_VOLANG[i])
	
	def oneAddVOLANG( self, event ):
		for i in range(len(busNum_VOLANG)):
			obj = self.m_listBox313.GetString(busNum_VOLANG[i])
			if not obj in self.m_listBox413.Items:
				self.selectedVOLANG.append(obj)
				self.m_listBox413.Append(obj)
	
	def multiAddVOLANG( self, event ):
		b  = self.m_listBox313.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox413.Items:
				self.m_listBox413.Append(obj)
	
	def oneMoveVOLANG( self, event ):
		for i in range(len(moveBus_VOLANG)):
			obj = self.m_listBox413.GetString(len(moveBus_VOLANG)-1-i)
			self.m_listBox413.Delete(moveBus_VOLANG[len(moveBus_VOLANG)-1-i])
	
	def multiMoveVOLANG( self, event ):
		b  = self.m_listBox413.Items
		for i in range(len(b)):
			obj = self.m_listBox313.GetString(i)
			self.m_listBox413.Delete(len(b)-1-i)
	
	def onSelectFLOW( self, event ):
		global busNum_FLOW
		busNum_FLOW = self.m_listBox314.GetSelections()
		for i in range(len(busNum_FLOW)):
			obj = self.m_listBox314.GetString(busNum_FLOW[i])
		event.Skip()
	
	def onSelectToMoveFLOW( self, event ):
		global moveBus_FLOW
		moveBus_FLOW = self.m_listBox414.GetSelections()
		for i in range(len(moveBus_FLOW)):
			obj = self.m_listBox414.GetString(moveBus_FLOW[i])
	
	def oneAddFLOW( self, event ):
		for i in range(len(busNum_FLOW)):
			obj = self.m_listBox314.GetString(busNum_FLOW[i])
			if not obj in self.m_listBox414.Items:
				self.selectedFLOW.append(obj)
				self.m_listBox414.Append(obj)
	
	def multiAddFLOW( self, event ):
		b  = self.m_listBox314.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox414.Items:
				self.m_listBox414.Append(obj)
	
	def oneMoveFLOW( self, event ):
		for i in range(len(moveBus_FLOW)):
			obj = self.m_listBox414.GetString(len(moveBus_FLOW)-1-i)
			self.m_listBox414.Delete(moveBus_FLOW[len(moveBus_FLOW)-1-i])
	
	def multiMoveFLOW( self, event ):
		b  = self.m_listBox414.Items
		for i in range(len(b)):
			obj = self.m_listBox314.GetString(i)
			self.m_listBox414.Delete(len(b)-1-i)
	
	def onSelectFLOWPQ( self, event ):
		global busNum_FLOWPQ
		busNum_FLOWPQ = self.m_listBox315.GetSelections()
		for i in range(len(busNum_FLOWPQ)):
			obj = self.m_listBox315.GetString(busNum_FLOWPQ[i])
		event.Skip()
	
	def onSelectToMoveFLOWPQ( self, event ):
		global moveBus_FLOWPQ
		moveBus_FLOWPQ = self.m_listBox415.GetSelections()
		for i in range(len(moveBus_FLOWPQ)):
			obj = self.m_listBox415.GetString(moveBus_FLOWPQ[i])
	
	def oneAddFLOWPQ( self, event ):
		for i in range(len(busNum_FLOWPQ)):
			obj = self.m_listBox315.GetString(busNum_FLOWPQ[i])
			if not obj in self.m_listBox415.Items:
				self.selectedFLOWPQ.append(obj)
				self.m_listBox415.Append(obj)
	
	def multiAddFLOWPQ( self, event ):
		b  = self.m_listBox315.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox415.Items:
				self.m_listBox415.Append(obj)
	
	def oneMoveFLOWPQ( self, event ):
		for i in range(len(moveBus_FLOWPQ)):
			obj = self.m_listBox415.GetString(len(moveBus_FLOWPQ)-1-i)
			self.m_listBox415.Delete(moveBus_FLOWPQ[len(moveBus_FLOWPQ)-1-i])
	
	def multiMoveFLOWPQ( self, event ):
		b  = self.m_listBox415.Items
		for i in range(len(b)):
			obj = self.m_listBox315.GetString(i)
			self.m_listBox415.Delete(len(b)-1-i)
	
	def onSelectFLOWMVA( self, event ):
		global busNum_FLOWMVA
		busNum_FLOWMVA = self.m_listBox317.GetSelections()
		for i in range(len(busNum_FLOWMVA)):
			obj = self.m_listBox317.GetString(busNum_FLOWMVA[i])
		event.Skip()
	
	def onSelectToMoveFLOWMVA( self, event ):
		global moveBus_FLOWMVA
		moveBus_FLOWMVA = self.m_listBox417.GetSelections()
		for i in range(len(moveBus_FLOWMVA)):
			obj = self.m_listBox417.GetString(moveBus_FLOWMVA[i])
	
	def oneAddFLOWMVA( self, event ):
		for i in range(len(busNum_FLOWMVA)):
			obj = self.m_listBox317.GetString(busNum_FLOWMVA[i])
			if not obj in self.m_listBox417.Items:
				self.selectedFLOWMVA.append(obj)
				self.m_listBox417.Append(obj)
	
	def multiAddFLOWMVA( self, event ):
		b  = self.m_listBox317.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox417.Items:
				self.m_listBox417.Append(obj)
	
	def oneMoveFLOWMVA( self, event ):
		for i in range(len(moveBus_FLOWMVA)):
			obj = self.m_listBox417.GetString(len(moveBus_FLOWMVA)-1-i)
			self.m_listBox417.Delete(moveBus_FLOWMVA[len(moveBus_FLOWMVA)-1-i])
	
	def multiMoveFLOWMVA( self, event ):
		b  = self.m_listBox417.Items
		for i in range(len(b)):
			obj = self.m_listBox317.GetString(i)
			self.m_listBox417.Delete(len(b)-1-i)
	
	def onSelectRELAY2( self, event ):
		global busNum_RELAY2
		busNum_RELAY2 = self.m_listBox318.GetSelections()
		for i in range(len(busNum_RELAY2)):
			obj = self.m_listBox318.GetString(busNum_RELAY2[i])
		event.Skip()
	
	def onSelectToMoveRELAY2( self, event ):
		global moveBus_RELAY2
		moveBus_RELAY2 = self.m_listBox418.GetSelections()
		for i in range(len(moveBus_RELAY2)):
			obj = self.m_listBox418.GetString(moveBus_RELAY2[i])
	
	def oneAddRELAY2( self, event ):
		for i in range(len(busNum_RELAY2)):
			obj = self.m_listBox318.GetString(busNum_RELAY2[i])
			if not obj in self.m_listBox418.Items:
				self.selectedRELAY2.append(obj)
				self.m_listBox418.Append(obj)
	
	def multiAddRELAY2( self, event ):
		b  = self.m_listBox318.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox418.Items:
				self.m_listBox418.Append(obj)
	
	def oneMoveRELAY2( self, event ):
		for i in range(len(moveBus_RELAY2)):
			obj = self.m_listBox418.GetString(len(moveBus_RELAY2)-1-i)
			self.m_listBox418.Delete(moveBus_RELAY2[len(moveBus_RELAY2)-1-i])
	
	def multiMoveRELAY2( self, event ):
		b  = self.m_listBox418.Items
		for i in range(len(b)):
			obj = self.m_listBox318.GetString(i)
			self.m_listBox418.Delete(len(b)-1-i)
	
	def onSelectVAR( self, event ):
		global busNum_VAR
		busNum_VAR = self.m_listBox319.GetSelections()
		for i in range(len(busNum_VAR)):
			obj = self.m_listBox319.GetString(busNum_VAR[i])
		event.Skip()
	
	def onSelectToMoveVAR( self, event ):
		global moveBus_VAR
		moveBus_VAR = self.m_listBox419.GetSelections()
		for i in range(len(moveBus_VAR)):
			obj = self.m_listBox419.GetString(moveBus_VAR[i])
	
	def oneAddVAR( self, event ):
		for i in range(len(busNum_VAR)):
			obj = self.m_listBox319.GetString(busNum_VAR[i])
			if not obj in self.m_listBox419.Items:
				self.selectedVAR.append(obj)
				self.m_listBox419.Append(obj)
	
	def multiAddVAR( self, event ):
		b  = self.m_listBox319.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox419.Items:
				self.m_listBox419.Append(obj)
	
	def oneMoveVAR( self, event ):
		for i in range(len(moveBus_VAR)):
			obj = self.m_listBox419.GetString(len(moveBus_VAR)-1-i)
			self.m_listBox419.Delete(moveBus_VAR[len(moveBus_VAR)-1-i])
	
	def multiMoveVAR( self, event ):
		b  = self.m_listBox419.Items
		for i in range(len(b)):
			obj = self.m_listBox319.GetString(i)
			self.m_listBox419.Delete(len(b)-1-i)
	
	def onSelectSTATE( self, event ):
		global busNum_STATE
		busNum_STATE = self.m_listBox320.GetSelections()
		for i in range(len(busNum_STATE)):
			obj = self.m_listBox320.GetString(busNum_STATE[i])
		event.Skip()
	
	def onSelectToMoveSTATE( self, event ):
		global moveBus_STATE
		moveBus_STATE = self.m_listBox420.GetSelections()
		for i in range(len(moveBus_STATE)):
			obj = self.m_listBox420.GetString(moveBus_STATE[i])
	
	def oneAddSTATE( self, event ):
		for i in range(len(busNum_STATE)):
			obj = self.m_listBox320.GetString(busNum_STATE[i])
			if not obj in self.m_listBox420.Items:
				self.selectedSTATE.append(obj)
				self.m_listBox420.Append(obj)
	
	def multiAddSTATE( self, event ):
		b  = self.m_listBox320.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox420.Items:
				self.m_listBox420.Append(obj)

	def oneMoveSTATE( self, event ):
		for i in range(len(moveBus_STATE)):
			obj = self.m_listBox420.GetString(len(moveBus_STATE)-1-i)
			self.m_listBox420.Delete(moveBus_STATE[len(moveBus_STATE)-1-i])
	
	def multiMoveSTATE( self, event ):
		b  = self.m_listBox420.Items
		for i in range(len(b)):
			obj = self.m_listBox320.GetString(i)
			self.m_listBox420.Delete(len(b)-1-i)
	
	def onSelectMACHINETERM( self, event ):
		global busNum_MACHINETERM
		busNum_MACHINETERM = self.m_listBox321.GetSelections()
		for i in range(len(busNum_MACHINETERM)):
			obj = self.m_listBox321.GetString(busNum_MACHINETERM[i])
		event.Skip()
	
	def onSelectToMoveMACHINETERM( self, event ):
		global moveBus_MACHINETERM
		moveBus_MACHINETERM = self.m_listBox421.GetSelections()
		for i in range(len(moveBus_MACHINETERM)):
			obj = self.m_listBox421.GetString(moveBus_MACHINETERM[i])
	
	def oneAddMACHINETERM( self, event ):
		for i in range(len(busNum_MACHINETERM)):
			obj = self.m_listBox321.GetString(busNum_MACHINETERM[i])
			if not obj in self.m_listBox421.Items:
				self.selectedMACHINETERM.append(obj)
				self.m_listBox421.Append(obj)
	
	def multiAddMACHINETERM( self, event ):
		b  = self.m_listBox321.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox421.Items:
				self.m_listBox421.Append(obj)
	
	def oneMoveMACHINETERM( self, event ):
		for i in range(len(moveBus_MACHINETERM)):
			obj = self.m_listBox421.GetString(len(moveBus_MACHINETERM)-1-i)
			self.m_listBox421.Delete(moveBus_MACHINETERM[len(moveBus_MACHINETERM)-1-i])
	
	def multiMoveMACHINETERM( self, event ):
		b  = self.m_listBox421.Items
		for i in range(len(b)):
			obj = self.m_listBox321.GetString(i)
			self.m_listBox421.Delete(len(b)-1-i)
	
	def onSelectMACHAPPIMP( self, event ):
		global busNum_MACHAPPIMP
		busNum_MACHAPPIMP = self.m_listBox322.GetSelections()
		for i in range(len(busNum_MACHAPPIMP)):
			obj = self.m_listBox322.GetString(busNum_MACHAPPIMP[i])
		event.Skip()
	
	def onSelectToMoveMACHAPPIMP( self, event ):
		global moveBus_MACHAPPIMP
		moveBus_MACHAPPIMP = self.m_listBox422.GetSelections()
		for i in range(len(moveBus_MACHAPPIMP)):
			obj = self.m_listBox422.GetString(moveBus_MACHAPPIMP[i])
	
	def oneAddMACHAPPIMP( self, event ):
		for i in range(len(busNum_MACHAPPIMP)):
			obj = self.m_listBox322.GetString(busNum_MACHAPPIMP[i])
			if not obj in self.m_listBox422.Items:
				self.selectedMACHAPPIMP.append(obj)
				self.m_listBox422.Append(obj)
	
	def multiAddMACHAPPIMP( self, event ):
		b  = self.m_listBox322.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox422.Items:
				self.m_listBox422.Append(obj)
	
	def oneMoveMACHAPPIMP( self, event ):
		for i in range(len(moveBus_MACHAPPIMP)):
			obj = self.m_listBox422.GetString(len(moveBus_MACHAPPIMP)-1-i)
			self.m_listBox422.Delete(moveBus_MACHAPPIMP[len(moveBus_MACHAPPIMP)-1-i])
	
	def multiMoveMACHAPPIMP( self, event ):
		b  = self.m_listBox422.Items
		for i in range(len(b)):
			obj = self.m_listBox322.GetString(i)
			self.m_listBox422.Delete(len(b)-1-i)
	
	def onSelectVUEL( self, event ):
		global busNum_VUEL
		busNum_VUEL = self.m_listBox323.GetSelections()
		for i in range(len(busNum_VUEL)):
			obj = self.m_listBox323.GetString(busNum_VUEL[i])
		event.Skip()
	
	def onSelectToMoveVUEL( self, event ):
		global moveBus_VUEL
		moveBus_VUEL = self.m_listBox423.GetSelections()
		for i in range(len(moveBus_VUEL)):
			obj = self.m_listBox423.GetString(moveBus_VUEL[i])
	
	def oneAddVUEL( self, event ):
		for i in range(len(busNum_VUEL)):
			obj = self.m_listBox323.GetString(busNum_VUEL[i])
			if not obj in self.m_listBox423.Items:
				self.selectedVUEL.append(obj)
				self.m_listBox423.Append(obj)
	
	def multiAddVUEL( self, event ):
		b  = self.m_listBox323.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox423.Items:
				self.m_listBox423.Append(obj)
	
	def oneMoveVUEL( self, event ):
		for i in range(len(moveBus_VUEL)):
			obj = self.m_listBox423.GetString(len(moveBus_VUEL)-1-i)
			self.m_listBox423.Delete(moveBus_VUEL[len(moveBus_VUEL)-1-i])
	
	def multiMoveVUEL( self, event ):
		b  = self.m_listBox423.Items
		for i in range(len(b)):
			obj = self.m_listBox323.GetString(i)
			self.m_listBox423.Delete(len(b)-1-i)
	
	def onSelectVOEL( self, event ):
		global busNum_VOEL
		busNum_VOEL = self.m_listBox324.GetSelections()
		for i in range(len(busNum_VOEL)):
			obj = self.m_listBox324.GetString(busNum_VOEL[i])
		event.Skip()
	
	def onSelectToMoveVOEL( self, event ):
		global moveBus_VOEL
		moveBus_VOEL = self.m_listBox424.GetSelections()
		for i in range(len(moveBus_VOEL)):
			obj = self.m_listBox424.GetString(moveBus_VOEL[i])
	
	def oneAddVOEL( self, event ):
		for i in range(len(busNum_VOEL)):
			obj = self.m_listBox324.GetString(busNum_VOEL[i])
			if not obj in self.m_listBox424.Items:
				self.selectedVOEL.append(obj)
				self.m_listBox424.Append(obj)
	
	def multiAddVOEL( self, event ):
		b  = self.m_listBox324.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox424.Items:
				self.m_listBox424.Append(obj)
	
	def oneMoveVOEL( self, event ):
		for i in range(len(moveBus_VOEL)):
			obj = self.m_listBox424.GetString(len(moveBus_VOEL)-1-i)
			self.m_listBox424.Delete(moveBus_VOEL[len(moveBus_VOEL)-1-i])
	
	def multiMoveVOEL( self, event ):
		b  = self.m_listBox424.Items
		for i in range(len(b)):
			obj = self.m_listBox324.GetString(i)
			self.m_listBox424.Delete(len(b)-1-i)
	
	def onSelectPLOAD( self, event ):
		global busNum_PLOAD
		busNum_PLOAD = self.m_listBox325.GetSelections()
		for i in range(len(busNum_PLOAD)):
			obj = self.m_listBox325.GetString(busNum_PLOAD[i])
		event.Skip()
	
	def onSelectToMovePLOAD( self, event ):
		global moveBus_PLOAD
		moveBus_PLOAD = self.m_listBox425.GetSelections()
		for i in range(len(moveBus_PLOAD)):
			obj = self.m_listBox425.GetString(moveBus_PLOAD[i])
	
	def oneAddPLOAD( self, event ):
		for i in range(len(busNum_PLOAD)):
			obj = self.m_listBox325.GetString(busNum_PLOAD[i])
			if not obj in self.m_listBox425.Items:
				self.selectedPLOAD.append(obj)
				self.m_listBox425.Append(obj)
	
	def multiAddPLOAD( self, event ):
		b  = self.m_listBox325.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox425.Items:
				self.m_listBox425.Append(obj)
	
	def oneMovePLOAD( self, event ):
		for i in range(len(moveBus_PLOAD)):
			obj = self.m_listBox425.GetString(len(moveBus_PLOAD)-1-i)
			self.m_listBox425.Delete(moveBus_PLOAD[len(moveBus_PLOAD)-1-i])
	
	def multiMovePLOAD( self, event ):
		b  = self.m_listBox425.Items
		for i in range(len(b)):
			obj = self.m_listBox325.GetString(i)
			self.m_listBox425.Delete(len(b)-1-i)
	
	def onSelectQLOAD( self, event ):
		global busNum_QLOAD
		busNum_QLOAD = self.m_listBox326.GetSelections()
		for i in range(len(busNum_QLOAD)):
			obj = self.m_listBox326.GetString(busNum_QLOAD[i])
		event.Skip()
	
	def onSelectToMoveQLOAD( self, event ):
		global moveBus_QLOAD
		moveBus_QLOAD = self.m_listBox426.GetSelections()
		for i in range(len(moveBus_QLOAD)):
			obj = self.m_listBox426.GetString(moveBus_QLOAD[i])
	
	def oneAddQLOAD( self, event ):
		for i in range(len(busNum_QLOAD)):
			obj = self.m_listBox326.GetString(busNum_QLOAD[i])
			if not obj in self.m_listBox426.Items:
				self.selectedQLOAD.append(obj)
				self.m_listBox426.Append(obj)
	
	def multiAddQLOAD( self, event ):
		b  = self.m_listBox326.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox426.Items:
				self.m_listBox426.Append(obj)
	
	def oneMoveQLOAD( self, event ):
		for i in range(len(moveBus_QLOAD)):
			obj = self.m_listBox426.GetString(len(moveBus_QLOAD)-1-i)
			self.m_listBox426.Delete(moveBus_QLOAD[len(moveBus_QLOAD)-1-i])
	
	def multiMoveQLOAD( self, event ):
		b  = self.m_listBox426.Items
		for i in range(len(b)):
			obj = self.m_listBox326.GetString(i)
			self.m_listBox426.Delete(len(b)-1-i)

	def onSelectGREF( self, event ):
		global busNum_GREF
		busNum_GREF = self.m_listBox327.GetSelections()
		for i in range(len(busNum_GREF)):
			obj = self.m_listBox327.GetString(busNum_GREF[i])
		event.Skip()
	
	def onSelectToMoveGREF( self, event ):
		global moveBus_GREF
		moveBus_GREF = self.m_listBox427.GetSelections()
		for i in range(len(moveBus_GREF)):
			obj = self.m_listBox427.GetString(moveBus_GREF[i])
	
	def oneAddGREF( self, event ):
		for i in range(len(busNum_GREF)):
			obj = self.m_listBox327.GetString(busNum_GREF[i])
			if not obj in self.m_listBox427.Items:
				self.selectedGREF.append(obj)
				self.m_listBox427.Append(obj)
	
	def multiAddGREF( self, event ):
		b  = self.m_listBox327.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox427.Items:
				self.m_listBox427.Append(obj)
	
	def oneMoveGREF( self, event ):
		for i in range(len(moveBus_GREF)):
			obj = self.m_listBox427.GetString(len(moveBus_GREF)-1-i)
			self.m_listBox427.Delete(moveBus_GREF[len(moveBus_GREF)-1-i])
	
	def multiMoveGREF( self, event ):
		b  = self.m_listBox427.Items
		for i in range(len(b)):
			obj = self.m_listBox327.GetString(i)
			self.m_listBox427.Delete(len(b)-1-i)
	
	def onSelectLCREF( self, event ):
		global busNum_LCREF
		busNum_LCREF = self.m_listBox328.GetSelections()
		for i in range(len(busNum_LCREF)):
			obj = self.m_listBox328.GetString(busNum_LCREF[i])
		event.Skip()
	
	def onSelectToMoveLCREF( self, event ):
		global moveBus_LCREF
		moveBus_LCREF = self.m_listBox428.GetSelections()
		for i in range(len(moveBus_LCREF)):
			obj = self.m_listBox428.GetString(moveBus_LCREF[i])
	
	def oneAddLCREF( self, event ):
		for i in range(len(busNum_LCREF)):
			obj = self.m_listBox328.GetString(busNum_LCREF[i])
			if not obj in self.m_listBox428.Items:
				self.selectedLCREF.append(obj)
				self.m_listBox428.Append(obj)
	
	def multiAddLCREF( self, event ):
		b  = self.m_listBox328.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox428.Items:
				self.m_listBox428.Append(obj)
	
	def oneMoveLCREF( self, event ):
		for i in range(len(moveBus_LCREF)):
			obj = self.m_listBox428.GetString(len(moveBus_LCREF)-1-i)
			self.m_listBox428.Delete(moveBus_LCREF[len(moveBus_LCREF)-1-i])
	
	def multiMoveLCREF( self, event ):
		b  = self.m_listBox429.Items
		for i in range(len(b)):
			obj = self.m_listBox329.GetString(i)
			self.m_listBox429.Delete(len(b)-1-i)
	
	def onSelectWINDVEL( self, event ):
		global busNum_WINDVEL
		busNum_WINDVEL = self.m_listBox329.GetSelections()
		for i in range(len(busNum_WINDVEL)):
			obj = self.m_listBox329.GetString(busNum_WINDVEL[i])
		event.Skip()
	
	def onSelectToMoveWINDVEL( self, event ):
		global moveBus_WINDVEL
		moveBus_WINDVEL = self.m_listBox429.GetSelections()
		for i in range(len(moveBus_WINDVEL)):
			obj = self.m_listBox429.GetString(moveBus_WINDVEL[i])
	
	def oneAddWINDVEL( self, event ):
		for i in range(len(busNum_WINDVEL)):
			obj = self.m_listBox329.GetString(busNum_WINDVEL[i])
			if not obj in self.m_listBox429.Items:
				self.selectedWINDVEL.append(obj)
				self.m_listBox429.Append(obj)
	
	def multiAddWINDVEL( self, event ):
		b  = self.m_listBox329.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox429.Items:
				self.m_listBox429.Append(obj)
	
	def oneMoveWINDVEL( self, event ):
		for i in range(len(moveBus_WINDVEL)):
			obj = self.m_listBox429.GetString(len(moveBus_WINDVEL)-1-i)
			self.m_listBox429.Delete(moveBus_WINDVEL[len(moveBus_WINDVEL)-1-i])
	
	def multiMoveWINDVEL( self, event ):
		b  = self.m_listBox429.Items
		for i in range(len(b)):
			obj = self.m_listBox329.GetString(i)
			self.m_listBox429.Delete(len(b)-1-i)
	
	def onSelectWINDTURSPD( self, event ):
		global busNum_WINDTURSPD
		busNum_WINDTURSPD = self.m_listBox330.GetSelections()
		for i in range(len(busNum_WINDTURSPD)):
			obj = self.m_listBox330.GetString(busNum_WINDTURSPD[i])
		event.Skip()
	
	def onSelectToMoveWINDTURSPD( self, event ):
		global moveBus_WINDTURSPD
		moveBus_WINDTURSPD = self.m_listBox430.GetSelections()
		for i in range(len(moveBus_WINDTURSPD)):
			obj = self.m_listBox430.GetString(moveBus_WINDTURSPD[i])
	
	def oneAddWINDTURSPD( self, event ):
		for i in range(len(busNum_WINDTURSPD)):
			obj = self.m_listBox330.GetString(busNum_WINDTURSPD[i])
			if not obj in self.m_listBox430.Items:
				self.selectedWINDTURSPD.append(obj)
				self.m_listBox430.Append(obj)
	
	def multiAddWINDTURSPD( self, event ):
		b  = self.m_listBox330.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox430.Items:
				self.m_listBox430.Append(obj)
	
	def oneMoveWINDTURSPD( self, event ):
		for i in range(len(moveBus_WINDTURSPD)):
			obj = self.m_listBox430.GetString(len(moveBus_WINDTURSPD)-1-i)
			self.m_listBox430.Delete(moveBus_WINDTURSPD[len(moveBus_WINDTURSPD)-1-i])
	
	def multiMoveWINDTURSPD( self, event ):
		b  = self.m_listBox430.Items
		for i in range(len(b)):
			obj = self.m_listBox330.GetString(i)
			self.m_listBox430.Delete(len(b)-1-i)
	
	def onSelectWINDPITCH( self, event ):
		global busNum_WINDPITCH
		busNum_WINDPITCH = self.m_listBox331.GetSelections()
		for i in range(len(busNum_WINDPITCH)):
			obj = self.m_listBox331.GetString(busNum_WINDPITCH[i])
		event.Skip()
	
	def onSelectToMoveWINDPITCH( self, event ):
		global moveBus_WINDPITCH
		moveBus_WINDPITCH = self.m_listBox431.GetSelections()
		for i in range(len(moveBus_WINDPITCH)):
			obj = self.m_listBox431.GetString(moveBus_WINDPITCH[i])
	
	def oneAddWINDPITCH( self, event ):
		for i in range(len(busNum_WINDPITCH)):
			obj = self.m_listBox331.GetString(busNum_WINDPITCH[i])
			if not obj in self.m_listBox431.Items:
				self.selectedWINDPITCH.append(obj)
				self.m_listBox431.Append(obj)
	
	def multiAddWINDPITCH( self, event ):
		b  = self.m_listBox331.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox431.Items:
				self.m_listBox431.Append(obj)
	
	def oneMoveWINDPITCH( self, event ):
		for i in range(len(moveBus_WINDPITCH)):
			obj = self.m_listBox431.GetString(len(moveBus_WINDPITCH)-1-i)
			self.m_listBox431.Delete(moveBus_WINDPITCH[len(moveBus_WINDPITCH)-1-i])
	
	def multiMoveWINDPITCH( self, event ):
		b  = self.m_listBox432.Items
		for i in range(len(b)):
			obj = self.m_listBox332.GetString(i)
			self.m_listBox432.Delete(len(b)-1-i)
	
	def onSelectWINDAEROTOR( self, event ):
		global busNum_WINDAEROTOR
		busNum_WINDAEROTOR = self.m_listBox332.GetSelections()
		for i in range(len(busNum_WINDAEROTOR)):
			obj = self.m_listBox332.GetString(busNum_WINDAEROTOR[i])
		event.Skip()
	
	def onSelectToMoveWINDAEROTOR( self, event ):
		global moveBus_WINDAEROTOR
		moveBus_WINDAEROTOR = self.m_listBox432.GetSelections()
		for i in range(len(moveBus_WINDAEROTOR)):
			obj = self.m_listBox432.GetString(moveBus_WINDAEROTOR[i])
	
	def oneAddWINDAEROTOR( self, event ):
		for i in range(len(busNum_WINDAEROTOR)):
			obj = self.m_listBox332.GetString(busNum_WINDAEROTOR[i])
			if not obj in self.m_listBox432.Items:
				self.selectedWINDAEROTOR.append(obj)
				self.m_listBox432.Append(obj)
	
	def multiAddWINDAEROTOR( self, event ):
		b  = self.m_listBox332.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox432.Items:
				self.m_listBox432.Append(obj)
	
	def oneMoveWINDAEROTOR( self, event ):
		for i in range(len(moveBus_WINDAEROTOR)):
			obj = self.m_listBox432.GetString(len(moveBus_WINDAEROTOR)-1-i)
			self.m_listBox432.Delete(moveBus_WINDAEROTOR[len(moveBus_WINDAEROTOR)-1-i])
	
	def multiMoveWINDAEROTOR( self, event ):
		b  = self.m_listBox432.Items
		for i in range(len(b)):
			obj = self.m_listBox332.GetString(i)
			self.m_listBox432.Delete(len(b)-1-i)
	
	def onSelectWINDROTORVOL( self, event ):
		global busNum_WINDROTORVOL
		busNum_WINDROTORVOL = self.m_listBox333.GetSelections()
		for i in range(len(busNum_WINDROTORVOL)):
			obj = self.m_listBox333.GetString(busNum_WINDROTORVOL[i])
		event.Skip()
	
	def onSelectToMoveWINDROTORVOL( self, event ):
		global moveBus_WINDROTORVOL
		moveBus_WINDROTORVOL = self.m_listBox433.GetSelections()
		for i in range(len(moveBus_WINDROTORVOL)):
			obj = self.m_listBox433.GetString(moveBus_WINDROTORVOL[i])
	
	def oneAddWINDROTORVOL( self, event ):
		for i in range(len(busNum_WINDROTORVOL)):
			obj = self.m_listBox333.GetString(busNum_WINDROTORVOL[i])
			if not obj in self.m_listBox433.Items:
				self.selectedWINDROTORVOL.append(obj)
				self.m_listBox433.Append(obj)
	
	def multiAddWINDROTORVOL( self, event ):
		b  = self.m_listBox333.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox433.Items:
				self.m_listBox433.Append(obj)
	
	def oneMoveWINDROTORVOL( self, event ):
		for i in range(len(moveBus_WINDROTORVOL)):
			obj = self.m_listBox433.GetString(len(moveBus_WINDROTORVOL)-1-i)
			self.m_listBox433.Delete(moveBus_WINDROTORVOL[len(moveBus_WINDROTORVOL)-1-i])
	
	def multiMoveWINDROTORVOL( self, event ):
		b  = self.m_listBox433.Items
		for i in range(len(b)):
			obj = self.m_listBox333.GetString(i)
			self.m_listBox433.Delete(len(b)-1-i)
	
	def onSelectWINDROTORCUR( self, event ):
		global busNum_WINDROTORCUR
		busNum_WINDROTORCUR = self.m_listBox334.GetSelections()
		for i in range(len(busNum_WINDROTORCUR)):
			obj = self.m_listBox334.GetString(busNum_WINDROTORCUR[i])
		event.Skip()
	
	def onSelectToMoveWINDROTORCUR( self, event ):
		global moveBus_WINDROTORCUR
		moveBus_WINDROTORCUR = self.m_listBox434.GetSelections()
		for i in range(len(moveBus_WINDROTORCUR)):
			obj = self.m_listBox434.GetString(moveBus_WINDROTORCUR[i])
	
	def oneAddWINDROTORCUR( self, event ):
		for i in range(len(busNum_WINDROTORCUR)):
			obj = self.m_listBox334.GetString(busNum_WINDROTORCUR[i])
			if not obj in self.m_listBox434.Items:
				self.selectedWINDROTORCUR.append(obj)
				self.m_listBox434.Append(obj)
	
	def multiAddWINDROTORCUR( self, event ):
		b  = self.m_listBox334.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox434.Items:
				self.m_listBox434.Append(obj)
	
	def oneMoveWINDROTORCUR( self, event ):
		for i in range(len(moveBus_WINDROTORCUR)):
			obj = self.m_listBox434.GetString(len(moveBus_WINDROTORCUR)-1-i)
			self.m_listBox434.Delete(moveBus_WINDROTORCUR[len(moveBus_WINDROTORCUR)-1-i])
	
	def multiMoveWINDROTORCUR( self, event ):
		b  = self.m_listBox434.Items
		for i in range(len(b)):
			obj = self.m_listBox334.GetString(i)
			self.m_listBox434.Delete(len(b)-1-i)
	
	def onSelectWINDPCOMAND( self, event ):
		global busNum_Angle
		busNum_WINDPCOMAND = self.m_listBox335.GetSelections()
		for i in range(len(busNum_WINDPCOMAND)):
			obj = self.m_listBox335.GetString(busNum_WINDPCOMAND[i])
		event.Skip()
	
	def onSelectToMoveWINDPCOMAND( self, event ):
		global moveBus_WINDPCOMAND
		moveBus_WINDPCOMAND = self.m_listBox435.GetSelections()
		for i in range(len(moveBus_WINDPCOMAND)):
			obj = self.m_listBox435.GetString(moveBus_WINDPCOMAND[i])
	
	def oneAddWINDPCOMAND( self, event ):
		for i in range(len(busNum_WINDPCOMAND)):
			obj = self.m_listBox335.GetString(busNum_WINDPCOMAND[i])
			if not obj in self.m_listBox435.Items:
				self.selectedWINDPCOMAND.append(obj)
				self.m_listBox435.Append(obj)
	
	def multiAddWINDPCOMAND( self, event ):
		b  = self.m_listBox335.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox435.Items:
				self.m_listBox435.Append(obj)
	
	def oneMoveWINDPCOMAND( self, event ):
		for i in range(len(moveBus_WINDPCOMAND)):
			obj = self.m_listBox435.GetString(len(moveBus_WINDPCOMAND)-1-i)
			self.m_listBox435.Delete(moveBus_WINDPCOMAND[len(moveBus_WINDPCOMAND)-1-i])
	
	def multiMoveWINDPCOMAND( self, event ):
		b  = self.m_listBox435.Items
		for i in range(len(b)):
			obj = self.m_listBox335.GetString(i)
			self.m_listBox435.Delete(len(b)-1-i)
	
	def onSelectWINDQCOMAND( self, event ):
		global busNum_WINDQCOMAND
		busNum_WINDQCOMAND = self.m_listBox336.GetSelections()
		for i in range(len(busNum_WINDQCOMAND)):
			obj = self.m_listBox336.GetString(busNum_WINDQCOMAND[i])
		event.Skip()
	
	def onSelectToMoveWINDQCOMAND( self, event ):
		global moveBus_WINDQCOMAND
		moveBus_WINDQCOMAND = self.m_listBox436.GetSelections()
		for i in range(len(moveBus_WINDQCOMAND)):
			obj = self.m_listBox436.GetString(moveBus_WINDQCOMAND[i])
	
	def oneAddWINDQCOMAND( self, event ):
		for i in range(len(busNum_WINDQCOMAND)):
			obj = self.m_listBox336.GetString(busNum_WINDQCOMAND[i])
			if not obj in self.m_listBox436.Items:
				self.selectedWINDQCOMAND.append(obj)
				self.m_listBox436.Append(obj)
	
	def multiAddWINDQCOMAND( self, event ):
		b  = self.m_listBox336.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox436.Items:
				self.m_listBox436.Append(obj)
	
	def oneMoveWINDQCOMAND( self, event ):
		for i in range(len(moveBus_WINDQCOMAND)):
			obj = self.m_listBox436.GetString(len(moveBus_WINDQCOMAND)-1-i)
			self.m_listBox436.Delete(moveBus_WINDQCOMAND[len(moveBus_WINDQCOMAND)-1-i])
	
	def multiMoveWINDQCOMAND( self, event ):
		b  = self.m_listBox436.Items
		for i in range(len(b)):
			obj = self.m_listBox336.GetString(i)
			self.m_listBox436.Delete(len(b)-1-i)
	
	def onSelectWINDAUX( self, event ):
		global busNum_WINDAUX
		busNum_WINDAUX = self.m_listBox337.GetSelections()
		for i in range(len(busNum_WINDAUX)):
			obj = self.m_listBox337.GetString(busNum_WINDAUX[i])
		event.Skip()
	
	def onSelectToMoveWINDAUX( self, event ):
		global moveBus_WINDAUX
		moveBus_WINDAUX = self.m_listBox437.GetSelections()
		for i in range(len(moveBus_WINDAUX)):
			obj = self.m_listBox437.GetString(moveBus_WINDAUX[i])
	
	def oneAddWINDAUX( self, event ):
		for i in range(len(busNum_WINDAUX)):
			obj = self.m_listBox337.GetString(busNum_WINDAUX[i])
			if not obj in self.m_listBox437.Items:
				self.selectedWINDAUX.append(obj)
				self.m_listBox437.Append(obj)
	
	def multiAddWINDAUX( self, event ):
		b  = self.m_listBox337.Items
		for i in range(len(b)):
			obj = b[i]
			if not obj in self.m_listBox437.Items:
				self.m_listBox437.Append(obj)
	
	def oneMoveWINDAUX( self, event ):
		for i in range(len(moveBus_WINDAUX)):
			obj = self.m_listBox437.GetString(len(moveBus_WINDAUX)-1-i)
			self.m_listBox437.Delete(moveBus_WINDAUX[len(moveBus_WINDAUX)-1-i])
	
	def multiMoveWINDAUX( self, event ):
		b  = self.m_listBox437.Items
		for i in range(len(b)):
			obj = self.m_listBox337.GetString(i)
			self.m_listBox437.Delete(len(b)-1-i)
	

