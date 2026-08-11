import wx
import wx.grid as  gridlib
class MyForm(wx.Frame):
    def __init__(self):
        ##
        # constructor to create the basic frame
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tool")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(panel)
        rows = 4
        column = 600000
        self.grid.CreateGrid(column, rows)
        self.count = 0
        # change a couple column labels
        self.grid.SetColLabelValue(0, "Timestamp")
        self.grid.SetColLabelValue(1, "CMD")
        self.grid.SetColLabelValue(2, "Address")
        self.grid.SetColLabelValue(3, "Data")

        # Few More operations to calculate CMD,Timestamp field


        for i in range(10**5):
            self.count += 1
            self.grid.SetCellValue(self.count,1,'CMD4')
            self.grid.SetCellValue(self.count,0,str(self.count))
            self.grid.SetCellValue(self.count, 2, "Extracted Address")
            self.grid.SetCellValue(self.count, 3, "Extracted Data")
            quo,rem = divmod(self.count,1000)
            if rem == 0:
                self.grid.MoveCursorDownBlock(expandSelection=False)
                wx.Yield()
        # change the row labels

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)

        self.grid.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.on_cell_change )
    
    def on_cell_change(self, event):
        print('This is on cell change')
        for i in range(10**5):
            # print(i)
            self.count += 1
            self.grid.SetCellValue(self.count,1,'ABCD')
            self.grid.SetCellValue(self.count,0,str(self.count))
            self.grid.SetCellValue(self.count, 2, "Extracted Address 1234 ")
            self.grid.SetCellValue(self.count, 3, "Extracted Data")

if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    frame.Show()
    app.MainLoop()