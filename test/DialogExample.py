import wx
  
class MyDialog(wx.Dialog): 
   def __init__(self, parent, title): 
      super(MyDialog, self).__init__(parent, title = title, size = (250,150)) 
      panel = wx.Panel(self) 
      self.btn = wx.Button(panel, wx.ID_OK, label = "ok", size = (50,20), pos = (75,50))
		
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title, size = (250,150))  
      self.InitUI() 
         
   def InitUI(self):    
      panel = wx.Panel(self) 
      btn = wx.Button(panel, label = "Modal Dialog", pos = (75,10)) 
      btn1 = wx.Button(panel, label = "Modeless Dialog", pos = (75,40)) 
      btn2 = wx.Button(panel, label = "MessageBox", pos = (75,70))
      cb1 = wx.ComboBox()
      
      btn.Bind(wx.EVT_BUTTON, self.OnModal)
		
      a = btn1.Bind(wx.EVT_BUTTON, self.OnModeless) 
      print a 
      btn2.Bind(wx.EVT_BUTTON, self.Onmsgbox) 
      self.Centre() 
      self.Show(True) 
		
   def OnModal(self, event): 
      a = MyDialog(self, "Dialog").ShowModal() 
      print a 
		
   def OnModeless(self, event): 
      a = MyDialog(self, "Dialog").Show()
		
   def Onmsgbox(self, event): 
      wx.MessageBox("This is a Message Box", "Message" ,wx.OK | wx.ICON_INFORMATION)  
		
ex  =  wx.App() 
Mywin(None,'MenuBar demo') 
ex.MainLoop()