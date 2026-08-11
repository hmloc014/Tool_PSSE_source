import wx
import wx.grid as gridlib

########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="A Simple Grid")
        panel = wx.Panel(self)

        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(12, 8)

        # get the cell attribute for the top left row
        editor = myGrid.GetCellEditor(0,0)
        attr1 = gridlib.GridCellAttr()
        attr1.SetReadOnly(True)
        myGrid.SetColAttr(0, attr1)

        attr2 = gridlib.GridCellAttr()
        attr2.SetBackgroundColour('grey')
        myGrid.SetColAttr(0, attr2)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()