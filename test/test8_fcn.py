from test8 import Frame1
import wx
import wx.xrc
from test81_fcn import CustomMyframe12

matrix = []

class CustomMyframe1(Frame1):
    def __init__ (self,parent):
        Frame1.__init__ (self,parent)

    def OnGrid1GridCellChange(self, event):
        print('This is test8 func!')
        custom = CustomMyframe12(self)
        custom.grid = self.grid1
        rows = self.grid1.GetNumberRows()
        cols = self.grid1.GetNumberCols()
        global matrix
        print('-------------------This is test8 func!',rows,cols,self.grid1.GetCellValue(9,1))
        for i in range(100):
            for j in range(cols):
                
                if self.grid1.GetCellValue(2*i,j) !='':
                    matrix.append(self.grid1.GetCellValue(2*i,j))
                    print('-----------',self.grid1.GetCellValue(2*i,j))
        custom.OnGrid1GridCellChange(event)
        

    def OnGrid1Selected(self,event):
        custom = CustomMyframe12(self)
        custom.grid = self.grid1
        custom.matrix = matrix
        custom.OnGrid1Selected(event)    


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CustomMyframe1(None)
    frame.Show(True)
    app.MainLoop()