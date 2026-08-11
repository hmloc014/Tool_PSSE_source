import wx
import wx.grid as grid
 
 
 
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title =title, size = (800,600))
 
 
 
 
        self.panel = MyPanel(self)
 
 
class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
 
 
        mygrid = grid.Grid(self)
        mygrid.CreateGrid(26,9)
 
        mygrid.SetCellValue(1,1, "Hello")
        mygrid.SetCellFont(1,1, wx.Font(15, wx.ROMAN, wx.ITALIC, wx.NORMAL))
 
 
        mygrid.SetCellValue(5,5,"Green Color")
        mygrid.SetCellBackgroundColour(5,5, wx.RED)
        mygrid.SetCellTextColour(5,5,wx.WHITE)
 
 
        mygrid.SetCellValue(8,3, "Read Only")
        mygrid.SetReadOnly(8,3,True)
 
        mygrid.SetCellEditor(6, 0, grid.GridCellNumberEditor(1, 20))
        mygrid.SetCellValue(6, 0, "2")
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mygrid, 1, wx.EXPAND)
        self.SetSizer(sizer)
 
 
 
 
 
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Grid Or Tables Part Two")
        self.frame.Show()
        return True
 
 
 
app = MyApp()
app.MainLoop()