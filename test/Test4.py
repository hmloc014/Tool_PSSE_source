
import wx
import wx.lib.inspection
from wx.lib.scrolledpanel import ScrolledPanel

class MyFrame( wx.Frame ):

    # TODO: add all class variables here for convention
    tin         = None

    hsizer      = None

    def __init__( self, parent, ID, title ):
        wx.Frame.__init__( self, parent, ID, title,
                     wx.DefaultPosition, wx.Size( 100, 50 ) )

        self.InitWidgets()
        self.InitBindings()
        self.InitFinish()


    def InitWidgets( self ):
        self.hsizer = wx.BoxSizer( wx.HORIZONTAL )

        # Add the TextCtrl
        vsizer = wx.BoxSizer( wx.VERTICAL )
        self.tin = wx.TextCtrl( self, style=wx.TE_MULTILINE )
        vsizer.Add( self.tin, 0, wx.ALL  )

        self.tin1 = wx.TextCtrl( self,style=wx.TE_MULTILINE)
        vsizer.Add( self.tin1, 0, wx.ALL  )

        self.tin3 = wx.TextCtrl( self, style=wx.TE_DONTWRAP|wx.TE_MULTILINE )
        vsizer.Add( self.tin3, 1, wx.ALL  )
        self.hsizer.Add( vsizer, 3, wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=20 )

        # Add ScrolledPanel widget
        self.hsizer.Add( wx.Size( 500, -1 ), 1 )
        vsizer2 = wx.BoxSizer( wx.VERTICAL )
        self.test_panel = ScrolledPanel( self )
        self.test_panel.SetupScrolling()

        # Setup static text ( label ) tvs is the 
        # vertical sizer inside the panel
        self.tvs = wx.BoxSizer( wx.VERTICAL )
        self.tin2 = wx.TextCtrl( self.test_panel )

        self.tvs.Add( self.tin2, 0, wx.EXPAND )
        vsizer2.Add( self.test_panel, 1, wx.EXPAND  )
        self.hsizer.Add( vsizer2, 3, wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=20 )

        # Add Spacer
        self.hsizer.Add( wx.Size( 500, -1 ), 1 ) 

    def InitBindings( self ):
        self.tin.Bind( wx.EVT_TEXT, self.TextChange )
        self.tin1.Bind( wx.EVT_TEXT, self.TextChange1 ) 
        self.tin2.Bind( wx.EVT_TEXT, self.TextChange2 ) 
        self.tin3.Bind( wx.EVT_TEXT, self.TextChange3 )

    def InitFinish( self ):

        # Setup sizers and frame
        self.SetAutoLayout( True )
        self.test_panel.SetAutoLayout( True )
        self.test_panel.SetSizer( self.tvs )
        self.SetSizer( self.hsizer )
        self.Layout()
        self.Update()
        self.Maximize()

    def TextChange( self, event ):
        print('this is on Text change')
        #self.CopyValues()
        self.tin1.Label = 'mmmmm'
        self.tin3.Label = 'aaaaaaa'

        # self.Layout()
        # self.Update()
        # self.test_panel.Refresh()
        # self.test_panel.Update()
        # print('tin1 : ',self.tin1.GetValue().split( "\n" ))

    def TextChange1( self, event ):
        print('this is on Text change 1')
        #self.CopyValues()
        self.tin3.Label = 'abc'
        self.tin.Label = 'cdf'
        # self.Layout()
        # self.Update()
        # self.test_panel.Refresh()
        # self.test_panel.Update()
        # print('tin3 : ',self.tin3.GetValue().split( "\n" ))
        content = self.tin3
        content.Value = ''
        r = open(r'D:\Hang\3. Programs\Tool-PSSE-2\output.txt','r')
        lines = r.readlines()
        for line in lines:
            content.Value = content.Value +'\n'+ line

    def TextChange3( self, event ):
        print('this is on Text change 2')
        #self.CopyValues()
        self.tin.Label = (self.tin3.GetValue())
        self.tin1.Label = (self.tin3.GetValue())
        # self.Layout()
        # self.Update()
        # self.test_panel.Refresh()
        # self.test_panel.Update()
        # print('tin : ',self.tin.GetValue().split( "\n" ))

    def TextChange2( self, event ):
        print('this is on Text change 2')
        #self.CopyValues()
        self.tin.Label = (self.tin2.GetValue())
        # self.Layout()
        # self.Update()
        # self.test_panel.Refresh()
        # self.test_panel.Update()
        # print('tin : ',self.tin.GetValue().split( "\n" ))

class MyApp( wx.App ):

    fr = None

    def OnInit( self ):
        self.fr = MyFrame( None, -1, "TitleX" )
        self.fr.Show( True )
        self.SetTopWindow( self.fr )
        return True

app = MyApp( 0 )
app.MainLoop()

def main():

    win = 1
if ( __name__ == "__main__" ):
    main()  