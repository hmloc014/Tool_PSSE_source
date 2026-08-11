from test8 import Frame1
import wx
import wx.xrc

count = 0

class CustomMyframe12(Frame1):
    def __init__ (self,parent):
        Frame1.__init__ (self,parent)
        self.grid = wx.grid.Grid
        self.matrix = []
        # count = 0

    def OnGrid1Selected(self,event):
        global row,col,val 
        row = event.GetRow()
        col = event.GetCol()
        value = self.grid.GetCellValue(row,col)
        print('This is test8 func in CustomMyframe12, row, col, value are: !',row,col,value)

    def OnGrid1GridCellChange(self, event):
        print('This is test8 func in CustomMyframe12 !')
        print('matrix size is: ',self.matrix)
        self.grid.SetCellValue(1,1,'Nguyen thanh hang')
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
        rows = self.grid.GetNumberRows()
        cols = self.grid.GetNumberCols()
        global count
        count = count + 1
        #All cells have a value, regardless of the editor.
        print 'Changed cell: (%u, %u)' % (Row, Col)
        print 'value: %s' % self.grid.GetCellValue(Row, Col)

        listAttr = ['1','2','3','4','5']
        lst = ["A","B","C"]
        modelTypes = ["'GENROU'","'GENSAL'","'ESST1A'","'ESST4B'","'EXAC4'","'TGOV1'","'HYGOV'","'GAST'","'PSS2A'","'PVGU1'","'PVEU1'","'PANELU1'","'IRRADU1'","'GEWTGCU1'","'GEWTECU1'","'GEWT2MU1'","'GEWTPTU1'","'GEWTARU1'","'GEWTGDU1'"]
        
        dyrFile = ''
        if count%2==0:
            dyrFile = r"D:\Hang\3. Programs\temp\dynamic\2030.dyr"
        elif count%2==1:
            dyrFile = r"D:\Hang\3. Programs\temp\dynamic\2030_new - Copy.dyr"

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
                    self.grid.SetCellValue(2*i,j,str(label[j]))
                    
                for j in range(len(line)):
                    self.grid.SetCellValue(2*i+1,j,str(line[j]))
                
                j=i%10+count
                if count+j>17:
                    count = 0
                lst.append(modelTypes[j])
                listAttr.append(modelTypes[i%10])
            
                # tChoiceEditor = wx.grid.GridCellChoiceEditor(lst,allowOthers = True)
                self.grid.SetCellEditor(i,3, tChoiceEditor)
                
                self.grid.SetCellValue(i,3, lst[0])

                # self.grid1.SetCellEditor(i,4, celChoice)
                self.grid.SetCellValue(i,4, listAttr[3])
 
        #an index and client data.
        if Row == 0:
            print 'index: %u' % self.grid.index
            print 'data: %s' % self.grid.data
        
        print ''            #blank line to make it pretty.
        event.Skip()
