import wx
import wx.grid as gridlib
class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "A key detecting grid", size=(1000,300))
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(10, 8)
        self.grid.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress) #Required for initial key press
        self.grid.Bind(gridlib.EVT_GRID_EDITOR_CREATED, self.onEditorCreated) # For subsequent key presses

    # -- Additional bits only for demonstration of isolating Text fields

        # Boolean field dislays as a CheckBox
        crbool = wx.grid.GridCellBoolRenderer()
        cebool = wx.grid.GridCellBoolEditor()
        self.grid.SetCellRenderer(1, 1, crbool)
        self.grid.SetCellEditor(1, 1, cebool)
        # Choice field
        cechoice = wx.grid.GridCellChoiceEditor(['Choice 1','Choice 2','Choice 3'], allowOthers=False)
        
        #Load special fields
        # for i in range(3):
        #     self.grid.SetCellEditor(i, 2, cechoice)
        self.grid.SetCellValue(1, 1, '1')
        
        self.grid.SetColSize(0,200)
        self.grid.SetColSize(2,200)

    # --
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizerAndFit(sizer)
        self.Show()

    def OnKeyPress(self, event):
        uk = event.UnicodeKey
        key = chr(event.UnicodeKey)
        shift = event.shiftDown
        rowsNum = self.grid.GetNumberRows()
        # rowsfrozenNum = self.grid.GetNumberFrozenRows()
        cols = self.grid.GetNumberCols()
        # colsfrozenNum = self.grid.GetNumberFrozenCols()


        row = self.grid.GetGridCursorRow()
        print("------uk-----------",uk)
        cechoice = wx.grid.GridCellChoiceEditor(["A",'B',"C"],allowOthers=False)
        # cechoice.SetParameters("A","B","C")
        print("rowsNum and row is:",rowsNum)
        print("rowsNum and row is:",cols)

        print("Shift is:",shift)
        if not shift:
            key = key.lower()
        print("Key", uk)
        if(row == rowsNum-1):
            print("Ahihiiiiiiiiiiiii")
        event.Skip()
        if uk==13:
            for i in range(3):
               self.grid.SetCellEditor(i, 2, cechoice)


    def onEditorCreated(self,event):
        #Set TextCtrl element to want all char/key events for all keys
        self.cb = event.Control
        if event.Control.ClassName == "wxTextCtrl":
            self.cb.SetWindowStyle(wx.WANTS_CHARS) # BEWARE! - Returns Tab, Enter, Arrow keys etc
            self.cb.Bind(wx.EVT_KEY_DOWN,self.OnKeyPress)
        else:
            print("Non text cell - bailing out")
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = MyForm()
    app.MainLoop()