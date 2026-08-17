from Tool_V3 import MyFrame1
import wx
import wx.xrc

class CustomMyframe1(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)

    def Close_PSSE( self, event ):
        wx.MessageBox("Close PSSE Case ?")
        self.Close()

    def onClose( self, event ):
        event.Skip() 

if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = CustomMyframe1(None)
    frame.SetIcon(wx.Icon("icon4.png"))
    frame.Show(True)
    app.MainLoop()
