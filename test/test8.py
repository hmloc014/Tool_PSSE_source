#-----------------------------------------------------------------------------
# Name:        GridCombo.py
# Purpose:     Dynamic list updating with a wx.grid.GridCellChoiceEditor
#
# Author:      Thomas M Wetherbee
#
# Created:     2009/04/27
# RCS-ID:      $Id: GridCombo.py $
# Copyright:   (c) 2009
# Licence:     Distributed under the terms of the GNU General Public License
#-----------------------------------------------------------------------------
#!/usr/bin/env python


'''
Dynamic list updating with a wx.grid.GridCellChoiceEditor.

This example shows how to dynamically update the choices in a 
GridCellChoiceEditor. This simple example creates a two column
grid where the top row in each column is a wx.grid.GridCellChoiceEditor.
The choices listed in the editor are created on the fly, and may change
with each selection. Text entered into the GridCellChoiceEditor cell 
is appended as an additional choice.

In addition to appending new choices, this example also shows how to get
the selection index and client data from the choice.

Cell editor interactions are printed for every step.

This example is deliberately simple, lacking sizers and other useful but 
confusing niceties.

Theory:
    
The GridCellChoiceEditor uses an underlying ComboBox to do the editing.
This underlying ComboBox is created when the cell editor is created. Normally
the ComboBox is completely hidden, but in this example we retrieve a reference 
to the ComboBox and use it to load choices and retrieve index and client data.

The example starts with a GridCellChoiceEditor attached to the two top cells of
the grid. When the GridCellChoiceEditor is invoked for the first time, two 
choice items are added to the choice list along with their associated user
data. The items are ('spam', 42) and ('eggs', 69), where spam is the text to
display and 42 is the associated client data. In this example 'spam' has an
index of 0 while eggs, being the second item of the list, has an index of 1.

Note that the index and user data are not required. The demonstrated method
works fine without either, but sometimes it is useful to know the index of a
selection, especially when the user is allowed to create choices. For example,
we might have the list ['spam', 'eggs', 'spam', 'spam'] where the three spam
items are different objects. In this case simply returning the item value
'spam' is ambiguous. We need to know the index, or perhaps some associated
client data.

In our example, when the user enters a new choice, the choice is appended to
the end of the choice list. A unique integer number is created for each new
choice, in succession, with the first number being 100. This number is used
for client data.

In this example we bind directly to the ComboBox events, rather than getting
the events through the frame. This is done to keep the grid from eating the
events. The difference in binding can be seen in the two binding methods:
    
    self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)
    self.button.Bind(wx.EVT_BUTTON, self.OnButton)
    
The latter method binds directly to the widget, where the first method
receives the event up the chain through the parent.

Note that this example does not save the new choice list: it persists only
for the life of the program. In a real application, you will probably want
to save this list and reload it the next time the program runs.
'''

import wx
import wx.grid

##modules ={}
count = 0

class Frame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, id=-1, name='', parent=None,
              pos=wx.Point(10, 10), size=wx.Size(800, 800),
              style=wx.DEFAULT_FRAME_STYLE, title='Spam & Eggs')
        self.SetClientSize(wx.Size(800, 800))

        self.scrolledWindow1 = wx.ScrolledWindow(id=-1,
              name='scrolledWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(800, 800), style=wx.HSCROLL | wx.VSCROLL)

        self.grid1 = wx.grid.Grid(id=-1, name='grid1',
              parent=self.scrolledWindow1, pos=wx.Point(0, 0),
              size=wx.Size(800, 800), style=0)

        attr = wx.grid.GridCellAttr()
        attr.SetBackgroundColour('light blue')
        
        self.grid1.CreateGrid(12000, 100)
        for i in range(12000):
            if i%2==0:
                self.grid1.SetRowAttr(i, attr)

        #Create the GridCellChoiceEditor with a blank list. Items will
        #be added later at runtime. "allowOthers" allows the user to
        #create new selection items on the fly.
        tChoiceEditor = wx.grid.GridCellChoiceEditor([], allowOthers=True)

        #Assign the cell editors for the top row (row 0). Note that on a
        #larger grid you would loop through the cells or set a default.
        self.grid1.SetCellEditor(0, 0, tChoiceEditor)
        self.grid1.SetCellEditor(0, 1, tChoiceEditor)
        
        #Create a starter list to seed the choices. In this list the item
        #format is (item, ClientData), where item is the string to display
        #in the drop list, and ClientData is a behind-the-scenes piece of
        #data to associate with this item. A seed list is optional.
        #If this were a real application, you would probably load this list
        #from a file.
        self.grid1.list = [('spam', 42), ('eggs', 69)]
        
        #Show the first item of the list in each ChoiceEditor cell. The
        #displayed text is optional. You could leave these cells blank, or
        #display 'Select...' or something of that nature.
        self.grid1.SetCellValue(0, 0, self.grid1.list[0][0])
        self.grid1.SetCellValue(0, 1, self.grid1.list[0][0])
        
        #The counter below will be used to automatically generate a new
        #piece of unique client data for each new item. This isn't very
        #useful, but it does let us demonstrate client data. Typically
        #you would use something meaningful for client data, such as a key
        #or id number.
        self.grid1.counter = 100
        
        #The following two objects store the client data and item index
        #from a choice selection. Client data and selection index are not
        #directly exposed to the grid object. We will get this information by
        #directly accessing the underlying ComboBox object created by the
        #GridCellChoiceEditor. 
        self.grid1.data = None
        self.grid1.index = None


        self.grid1.Bind(wx.grid.EVT_GRID_CELL_CHANGE,
              self.OnGrid1GridCellChange)

        self.grid1.Bind( wx.grid.EVT_GRID_SELECT_CELL,
              self.OnGrid1Selected)
              
        self.grid1.Bind(wx.grid.EVT_GRID_EDITOR_CREATED,
              self.OnGrid1GridEditorCreated)

        self.grid1.Bind(wx.grid.EVT_GRID_EDITOR_HIDDEN,
              self.OnGrid1GridEditorHidden)


    #This method fires when a grid cell changes. We are simply showing
    #what has changed and any associated index and client data. Typically
    #this method is where you would put your real code for processing grid
    #cell changes.
    def OnGrid1GridCellChange(self, event):
        # try:
        # GEN
        labelGENROU = ['','','',"T'do",'T"do',"T'qo",'T"qo','H','D','Xd','Xq',"X'd","X'q",'X"d','X1','S(1.0)','S(1.2)']
        labelGENSAL = ['','','',"T'do",'T"do','T"qo','H','D','Xd','Xq',"X'd",'X"d','X1','S(1.0)','S(1.2)']
        # AVR
        labelESST1A = ['','','']
        labelESST4B = ['','','','TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
        labelEXAC4 = ['','','',"TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
        # GOV
        labelTGOV1 = ['','','','R','T1','VMAX','VMIN','T2','T3','Dt']
        labelHYGOV = ['','','',"R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
        labelGAST = ['','','',"R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
        # PSS
        labelPSS2A = ['','','','IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
        # Solar
        labelPVGU1 = ['','','','','','','','','','TlqCmd','TlpCmd','VLVPL1','VLVPL2','GLVPL','VHVRCR','CURHVRCR','Rip_LVPL','T_LVPL']
        labelPVEU = ['','','','','','','','','','Remote Bus','PFAFLG','VARFLG','PQFLG','Tw','Kpv','Kiv','Kpp','Kip','Kf','Tf','Qmx','Qmn','IPmax','Trv','dPMX','dPMN','Tpower','KQi','Vmincl','Vmaxcl','KVi','Tv','Tp','ImaxTD','IphI','IqhI','PMX']
        labelPANELU1 = ['','','','','','','','','','PDCMAX200','PDCMAX400','PDCMAX600','PDCMAX800','PDCMAX1000']
        labelIRRADU1 = ['','','','','','','','','','Inservice flag','TIME1','IRRADIANCE1','TIME2','IRRADIANCE2','TIME3','IRRADIANCE3','TIME4','IRRADIANCE4','TIME5','IRRADIANCE5','TIME6','IRRADIANCE6','TIME7','IRRADIANCE7','TIME8','IRRADIANCE8','TIME9','IRRADIANCE9','TIME10','IRRADIANCE10']
        # Wind
        labelGEWTGCU1 = ['','','','','','','','','','WTs originNum','Full ConvFlag','Prate','Xeq','Vlvpl1','Vlvpl2','Glvpl','Vhvrcr2','CURhvrcr2','Vlvacr1','VLVACR2','Rip_LVPL','T_LVPL','LVPL1stV','LVPL1stP','LVPL2ndV','LVPL2ndP','LVPL3rdV','LVPL3rdP','Impedance']
        labelGEWTECU1 = ['','','','','','','','','','Remote Bus','PFAFlg','VARFlg','APCFlg','FRFlg','PQFlg','Qdroof FromBus','Qdroof ToBus','Qdroof ID','Tfv','Kpv','Kiv','Rc','Xc','Tfp','Kpp','Kip','Pmax','Pmin','Qmax','Qmin','IPmax','Trv','RPmax','RPmin','Tpowwer','KQu','Vmincl','Vmaxcl','KV','XLmin',\
                        'XLmax','Tv','Tp','Fn','Tpav','FRa','FRb','FRc','FRd','PFRa','PFRb','PFRc','PFRd','PFRmax','PFRmin','Tw','Tlvpl','Vlvpl','SPDW1','SPDWmax','SPDWmin','SPDlow','WTTHRES','EBST','KDBR','PDBRmax','IMAXtd','IPHL','IQHL','Tlpqd','Kqd','Xqd','Kwi','DBwi','TLPwi','TWOwi','URLwi','DRLwi','PMXwi','PMNwi','VERmx','VERmn','Vfrz','QZPmx','QZPmn']
        labelGEWT2MU1 = ['','','','','','','','','','H','DAMP','HTfrac','FREQ','DSHAFT']
        labelGEWTPTU1 = ['','','','','','','','','','','','Tp','Kppt','Kipt','Kpc','Kic','0min','0max','d0/dtmin','d0/dtmax','Pref']
        labelGEWTARU1 = ['','','','','','','','','','','LamdaMax','LamdaMin','PITCHmax','PITCHmin','Ta','P','Raddius','GBRatio','SYNCHR']
        labelGEWTGDU1 = ['','','','','','','','','','','T1G','Tg','MAXg','T1r','T2r','Max']

        labelTypes = [labelGENROU,labelGENSAL,labelESST1A,labelESST4B,labelEXAC4,labelTGOV1,labelHYGOV,labelGAST,labelPSS2A,labelPVGU1,labelPVEU,labelPANELU1,labelIRRADU1,labelGEWTGCU1,labelGEWTECU1,labelGEWT2MU1,labelGEWTPTU1,labelGEWTARU1,labelGEWTGDU1]
        modelTypes = ['GENROU','GENSAL','ESST1A','ESST4B','EXAC4','TGOV1','HYGOV','GAST','PSS2A','PVGU1','PVEU1','PANELU1','IRRADU1','GEWTGCU1','GEWTECU1','GEWT2MU1','GEWTPTU1','GEWTARU1','GEWTGDU1']

        Row = event.GetRow()
        Col = event.GetCol()
        rows = self.grid1.GetNumberRows()
        cols = self.grid1.GetNumberCols()
        global count
        count = count + 1
        #All cells have a value, regardless of the editor.
        print 'Changed cell: (%u, %u)' % (Row, Col)
        print 'value: %s' % self.grid1.GetCellValue(Row, Col)

        listAttr = ['1','2','3','4','5']
        lst = ["A","B","C"]
        modelTypes = ["'GENROU'","'GENSAL'","'ESST1A'","'ESST4B'","'EXAC4'","'TGOV1'","'HYGOV'","'GAST'","'PSS2A'","'PVGU1'","'PVEU1'","'PANELU1'","'IRRADU1'","'GEWTGCU1'","'GEWTECU1'","'GEWT2MU1'","'GEWTPTU1'","'GEWTARU1'","'GEWTGDU1'"]
        
        dyrFile = ''
        if count%2==0:
            dyrFile = r"D:\Hang\3. Programs\temp\dynamic\2030.dyr"
        elif count%2==1:
            dyrFile = r"D:\Hang\3. Programs\temp\dynamic\2030_new - Copy.dyr"

        # Boolean field dislays as a CheckBox
        # crbool = wx.grid.GridCellBoolRenderer()
        # cebool = wx.grid.GridCellBoolEditor()
        # tChoiceEditor =wx.grid.GridCellChoiceEditor([],allowOthers=True)
        # dyrFile = input('dyrFile:')
        listAttr = ['m','v','r','g']
        lst = ['a','b','c','d']
        # celChoice =wx.grid.GridCellChoiceEditor(listAttr,allowOthers=True)
        # if tChoiceEditor:
        tChoiceEditor = wx.grid.GridCellChoiceEditor(lst,allowOthers = True)
        
        f = open(dyrFile,'r')
        lines = f.readlines()
        for i,line in enumerate(lines):
            line = line.split()
            if len(line)!=0:
                model = line[1]
                indexType = modelTypes.index(model)
                label = labelTypes[indexType]
                tChoiceEditor.IncRef()
                
                for j in range(len(label)):
                    self.grid1.SetCellValue(2*i,j,str(label[j]))
                    
                for j in range(len(line)):
                    self.grid1.SetCellValue(2*i+1,j,str(line[j]))
                
                j=i%10+count
                if count+j>17:
                    count = 0
                lst.append(modelTypes[j])
                listAttr.append(modelTypes[i%10])
            
                # tChoiceEditor = wx.grid.GridCellChoiceEditor(lst,allowOthers = True)
                self.grid1.SetCellEditor(i,3, tChoiceEditor)
                
                self.grid1.SetCellValue(i,3, lst[0])

                # self.grid1.SetCellEditor(i,4, celChoice)
                self.grid1.SetCellValue(i,4, listAttr[3])
            # n = tChoiceEditor.GetRefCount()
            # print('----n :',n)
        #Assign the cell editors for the top row (row 0). Note that on a
        #larger grid you would loop through the cells or set a default.



        # print('----------------Count is:',count)
        # for i in range(200+count):
        #     # tChoiceEditor.Destroy()
        #     j=i%10+count
        #     if count+j>17:
        #         count = 0
        #     lst.append(modelTypes[j])
        #     listAttr.append(modelTypes[i%10])
            # print('------------------lst is:',lst)
            # crbool.IncRef()
            # cebool.IncRef()

            # self.grid1.SetCellRenderer(i, 2, crbool)
            # self.grid1.SetCellEditor(i, 2, cebool)
            # self.grid1.SetCellValue(i, 2, '1')
        
        
        #an index and client data.
        if Row == 0:
            print 'index: %u' % self.grid1.index
            print 'data: %s' % self.grid1.data
        
        print ''            #blank line to make it pretty.
        event.Skip()
        # except:
        #     wx.MessageBox('on change error')
    
    #This method fires when the underlying GridCellChoiceEditor ComboBox
    #is done with a selection.
    def OnGrid1Selected(self,event):
        event.Skip()
        
    def OnGrid1ComboBox(self, event):
        #Save the index and client data for later use.
        self.grid1.index = self.comboBox.GetSelection()
        self.grid1.data = self.comboBox.GetClientData(self.grid1.index)
        
        print 'ComboBoxChanged: %s' % self.comboBox.GetValue()
        print 'ComboBox index: %u' % self.grid1.index 
        print 'ComboBox data: %u\n' % self.grid1.data
        event.Skip()


    #This method fires when any text editing is done inside the text portion
    #of the ComboBox. This method will fire once for each new character, so
    #the print statements will show the character by character changes.
    def OnGrid1ComboBoxText(self, event):
        #The index for text changes is always -1. This is how we can tell
        #that new text has been entered, as opposed to a simple selection
        #from the drop list. Note that the index will be set for each character,
        #but it will be -1 every time, so the final result of text changes is
        #always an index of -1. The value is whatever text that has been 
        #entered. At this point there is no client data. We will have to add
        #that later, once all of the text has been entered.
        self.grid1.index = self.comboBox.GetSelection()
        
        print 'ComboBoxText: %s' % self.comboBox.GetValue()
        print 'ComboBox index: %u\n' % self.grid1.index
        event.Skip()


    #This method fires after editing is finished for any cell. At this point
    #we know that any added text is complete, if there is any.
    def OnGrid1GridEditorHidden(self, event):
        Row = event.GetRow()
        Col = event.GetCol()
        
        #If the following conditions are true, it means that new text has 
        #been entered in a GridCellChoiceEditor cell, in which case we want
        #to append the new item to our selection list.
        if Row == 0 and self.grid1.index == -1:
            #Get the new text from the grid cell
            item = self.comboBox.GetValue()
            
            #The new item will be appended to the list, so its new index will
            #be the same as the current length of the list (origin zero).
            self.grid1.index = self.comboBox.GetCount()
            
            #Generate some unique client data. Remember this counter example
            #is silly, but it makes for a reasonable demonstration. Client
            #data is optional. If you can use it, this is where you attach
            #your real client data.
            self.grid1.data = self.grid1.counter
            
            #Append the new item to the selection list. Remember that this list
            #is used by all cells with the same editor, so updating the list
            #here updates it for every cell using this editor.
            self.comboBox.Append(item, self.grid1.data)
            
            #Update the silly client data counter
            self.grid1.counter = self.grid1.counter + 1
        
        print 'OnGrid1EditorHidden: (%u, %u)\n' % (Row, Col)

        event.Skip()

    #This method fires when a cell editor is created. It appears that this
    #happens only on the first edit using that editor.
    def OnGrid1GridEditorCreated(self, event):
        Row = event.GetRow()
        Col = event.GetCol()
        
        print 'OnGrid1EditorCreated: (%u, %u)\n' % (Row, Col)
        
        #In this example, all cells in row 0 are GridCellChoiceEditors,
        #so we need to setup the selection list and bindings. We can't
        #do this in advance, because the ComboBox control is created with
        #the editor.
        if Row == 0:
            #Get a reference to the underlying ComboBox control.
            self.comboBox = event.GetControl()
            
            #Bind the ComboBox events.
            self.comboBox.Bind(wx.EVT_COMBOBOX, self.OnGrid1ComboBox)
            self.comboBox.Bind(wx.EVT_TEXT, self.OnGrid1ComboBoxText)
            
            #Load the initial choice list.
            for (item, data) in self.grid1.list:
                self.comboBox.Append(item, data)
        
        event.Skip()
        
