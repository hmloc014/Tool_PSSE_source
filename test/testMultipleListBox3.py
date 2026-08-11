import wx

########################################################################
class Car:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, id, model, make, year):
        """Constructor"""
        self.id = id
        self.model = model
        self.make = make
        self.year = year       


########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Multiple ListBox Example", size=(440,300))

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        ford = Car(0, "Ford", "F-150", "2008")
        chevy = Car(1, "Chevrolet", "Camaro", "2010")
        nissan = Car(2, "Nissan", "370Z", "2005")
        fiat = Car(2, "Fiat", "F7Z", "2005")
        fiat2 = Car(2, "Fiat", "punto", "2005")

        sampleList = []

        lb = wx.ListBox(panel,
                        size=(200, 150),
                        style = wx.LB_EXTENDED,
                        choices=sampleList)
        self.oneadd = wx.Button(panel,-1, ">", pos=(110, 180))
        self.multiadd = wx.Button(panel, -1,">>",pos=(200, 180))
        self.oneMove = wx.Button(panel,-1, "<", pos=(110, 210))
        self.multiMove = wx.Button(panel, -1,"<<",pos=(200, 210))

        lb2 = wx.ListBox(panel,
                size=(200, 150),
                style = wx.LB_EXTENDED,
                choices=sampleList)

        self.lb = lb
        self.lb2 = lb2
        list1 = ['a','b','c','d']

        # lb2.Append(ford.make, ford)
        for i in range(len(list1)):
            lb.Append(list1[i])
        # lb.Append(fiat.make, fiat)
        # lb.Append(fiat2.make, fiat2)
        # lb.Append(nissan.make, nissan)
        lb.Bind(wx.EVT_LISTBOX, self.onSelect)
        lb2.Bind(wx.EVT_LISTBOX, self.onSelectToMove)
        self.oneadd.Bind( wx.EVT_BUTTON, self.oneAdd_Fcn )
        self.multiadd.Bind( wx.EVT_BUTTON, self.multipleAdd_Fcn )
        self.oneMove.Bind( wx.EVT_BUTTON, self.oneMove_Fcn )
        self.multiMove.Bind( wx.EVT_BUTTON, self.multiMove_Fcn )
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer.Add(lb, 0, wx.ALL, 5)

        sizer.Add(lb2, 0, wx.ALL, 5)
        panel.SetSizer(sizer)

    #----------------------------------------------------------------------
    def onSelect(self, event):
        """"""
        # print "You selected: " + self.lb.GetStringSelections()
        global a
        a=self.lb.GetSelections()
        print(len(a))
        print("a is: ",a)
        for i in range(len(a)):
            print(a[i])
            obj = self.lb.GetString(a[i])
            print("obj in onselect is:",obj)
            # text = """
            # The object's attributes are:
            # %s  %s    %s  %s

            # """ % (obj.id, obj.make, obj.model, obj.year)
            # print text

    def onSelectToMove(self, event):
        """"""
        # print "You selected: " + self.lb.GetStringSelections()
        global move
        move = self.lb2.GetSelections()
        print('________________select to move___________')
        print('len(move) is: ',len(move))
        print('move is: ',move)
        for i in range(len(move)):
            
            obj = self.lb2.GetString(move[i])
            print('{a}: index value is: {b}, obj is:{c}'.format(a=i,b=move[i],c=obj))
            # text = """
            # The object's attributes are:
            # %s  %s    %s  %s

            # """ % (obj.make, obj.model)
            # print text

    def oneAdd_Fcn(self,event):
        print('This is oneAdd, self.lb2.Items are',self.lb2.Items)
        for i in range(len(a)):
            obj = self.lb.GetString(a[i])
            print("obj: ",obj)
            # print("obj.make: ",obj.make)
            if not obj in self.lb2.Items:
                self.lb2.Append(obj)

    def multipleAdd_Fcn(self,event):
        print('This is multipleAdd')
        b  = self.lb.Items
        print(b)

        for i in range(len(b)):
            obj = b[i]
            # print("obj.model: ",obj.model)
            # print("obj.make: ",obj.make)
            if not obj in self.lb2.Items:
                self.lb2.Append(obj)
    
    def oneMove_Fcn(self,event):
        print('This is oneMOve')
        for i in range(len(move)):
            print("len move is: ",len(move))
            print("i is: ",i)
            obj = self.lb2.GetString(len(move)-1-i)
            print("obj: ",obj)
            print("move[len(move)-i]: ",len(move)-1-i)
            # print("obj.make: ",obj.make)
            self.lb2.Delete(move[len(move)-1-i])

    def multiMove_Fcn(self,event):
        print('This is multipleMove')
        b  = self.lb2.Items
        print(b)

        for i in range(len(b)):
            obj = self.lb.GetString(i)
            print("obj: ",obj)
            # print("obj.make: ",obj.make)
            self.lb2.Delete(len(b)-1-i)

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()