import wx
import wx.grid

class MainTable(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
#Insert functions and SQL queries...

class dspdtb(wx.Frame):
    def __init__(self): #, title, parent=None, style = wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLOSE_BOX | wx.CAPTION | wx.TRANSPARENT_WINDOW):
        wx.Frame.__init__(self, None, wx.ID_ANY, "A key detecting grid", size=(1000,300)) #(self, parent=parent, title=title)
#More stuff below...
        panel = wx.Panel(self, wx.ID_ANY)

        # btn2 = BP.ButtonInfo(titleBar, wx.ID_ANY, wx.Bitmap("button5 a.png", wx.BITMAP_TYPE_PNG))
        # titleBar.AddButton(btn2)
        # btn2.SetBitmap(wx.Bitmap("button5 b.png", wx.BITMAP_TYPE_PNG), status="Pressed")
        # self.Bind(wx.EVT_BUTTON, self.Removal, btn2)

#Still more stuff below...
        vSizer = wx.BoxSizer( wx.HORIZONTAL )
        grid = MainTable(panel)
        # vSizer.Add(titleBar, 0, wx.EXPAND)
        vSizer.Add((20, 20))
        vSizer.Add(grid, 0, wx.ALL | wx.CENTRE, 50)
        # titleBar.DoLayout()
        vSizer.Layout()
        #toolbar end
        self.Show()
        self.Maximize(True)

#Insert other functions here...

    def Removal(self, event):
        global l_a
        t = len(l_a)
        n = 0
        chk = wx.MessageBox('Do you wanna delete the selected items?', 'Confirm Deletion', wx.YES_NO)
        if chk==2:
            while(n<t):
                sasa = l_a[n]
                print (sasa)
                try: 
                    mycursor.execute("DELETE FROM ip_config WHERE id=%s;", (sasa,))
                except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(err))
                mydb.commit()
                n+=1
            wx.MessageBox('Rows now deleted, the table will now reload.', 'Deletion Completed', wx.OK)
        l_a=[]
        MainTable.ForceRefresh()

if __name__ == "__main__":
    app = wx.App(False)
    frame = dspdtb()
    # frame.SetIcon(wx.Icon("icon4.png"))
    frame.Show(True)
    app.MainLoop()
