# -*- coding: utf-8 -*- 
from Tool_V3 import MyFrame1
import pyodbc
import glob, os, sys
import pssepath
import wx
import wx.xrc
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
from ChangeBusTab import change,addNew
import numpy as np
from DialogBox import getInput
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadShuntTab
from math import *
from decimal import *
from dialogSearchDyn import SearchDyn
from ui_performance import batched_grid_update, profiled

cellValue = 0
cellVal = 0
row = 0
col = 0
busNum = 0
busName = ''
busArea = 0
busZone = 0
busID = ''
machineStatus = 0
pgen = 0.0
qgen = 0.0
pmax = 0.0
qmax = 0.0
busNumUpper = 0
busNameUpper= ''
busAreaUpper=0
busZoneUpper=0
busIDUpper =''
machineStatusUpper = 0
pgenUpper = 0.0
qgenUpper = 0.0
pmaxUpper = 0.0
qmaxUpper = 0.0

TWOPLACE = Decimal(10)**-2
    
class CustomGridDyn(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.Path = ''
        self.indexFile = 0
        self.uk = 0
        self.PathFile = [[]]
        self.parent = parent
        self.fileInfoTranspose = []
        self.matrixBus = []
        self.matrixArea = []
        self.matrixZone = []
        self.matrixShunt = []
        self.matrixGen = []
        self.myGridSource = wx.grid.Grid
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridShunt = wx.grid.Grid
        self.myGridDyn = wx.grid.Grid
    
    # chức năng thực hiện tại ô được chọn của bảng dynamic
    def on_selected_cell_grid_dyn( self, event ):
        global row,col,cellValue
        row = event.GetRow()
        col = event.GetCol()
        cellValue = self.myGridDyn.GetCellValue(row,col)

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng dynamic
    def on_cell_change_grid_dyn( self, event ):
        cell = event.GetEventObject()
        row1 = cell.GetGridCursorRow()
        col1 = cell.GetGridCursorCol()
        cellVal = self.myGridDyn.GetCellValue(row1,col1)
        modelType = self.myGridDyn.GetCellValue(row1,1)
        busNum = self.myGridDyn.GetCellValue(row1,0)
        busID = self.myGridDyn.GetCellValue(row1,2)
        numList = self.matrixGen[self.indexFile][:,0] 

        if col == 1:
            if int(busNum) in numList:
                index = np.where(numList == int(busNum))
                pmax = float(self.myGridSource.GetCellValue(index[0][0],12))
                area = int(self.myGridSource.GetCellValue(index[0][0],2))

                TD = [16,26,36,43,53,63]
                ND = [17,18,19,42,27,28,29,52,37,38,39,62] # sinh khoi, LNG, ND
                WD = [41,51,61]
                SL = [40,50,60,70,80,90,100,110,120]
                # 16(TD),17(NT),18(NK),19(HN),40(PV),41(W),42(SK),43(TDTN) mien bac
                # 26(TD),27(NT),28(NK),29(HN),50(PV),51(W),52(SK),53(TDTN) mien trung
                # 36(TD),37(NT),38(NK),39(HN),60(PV),61(W),62(SK),63(TDTN) mien nam
                # 70,80,90,100,110,120 (DMT)
                # 1 so nguon phia bac dat trong area luoi bac 110 va luoi bac 220 (10,11,12) se k xet
                sourceType = ""
                if area in TD:
                    sourceType = "TD"
                elif area in ND:
                    sourceType = 'ND'
                elif area in WD: 
                    sourceType = 'TYPE3'
                else:
                    sourceType = 'TYPE4'

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
                labelGEWTECU1 = ['','','','','','','','','','Remote Bus','PFAFlg','VARFlg','APCFlg','PQFlg','Qdroof FromBus','Qdroof ToBus','Qdroof ID','Tfv','Kpv','Kiv','Rc','Xc','Tfp','Kpp','Kip','Pmax','Pmin','Qmax','Qmin','IPmax','Trv','RPmax','RPmin','Tpowwer','KQu','Vmincl','Vmaxcl','KV','XLmin',\
                                'XLmax','Tv','Tp','Fn','Tpav','FRa','FRb','FRc','FRd','PFRa','PFRb','PFRc','PFRd','PFRmax','PFRmin','Tw','Tlvpl','Vlvpl','SPDW1','SPDWmax','SPDWmin','SPDlow','WTTHRES','EBST','KDBR','PDBRmax','IMAXtd','IPHL','IQHL','Tlpqd','Kqd','Xqd','Kwi','DBwi','TLPwi','TWOwi','URLwi','DRLwi','PMXwi','PMNwi','VERmx','VERmn','Vfrz','QZPmx','QZPmn']
                labelGEWT2MU1 = ['','','','','','','','','','H','DAMP','HTfrac','FREQ','DSHAFT']
                labelGEWTPTU1 = ['','','','','','','','','','','','Tp','Kppt','Kipt','Kpc','Kic','0min','0max','d0/dtmin','d0/dtmax','Pref']
                labelGEWTARU1 = ['','','','','','','','','','','LamdaMax','LamdaMin','PITCHmax','PITCHmin','Ta','P','Raddius','GBRatio','SYNCHR']
                labelGEWTGDU1 = ['','','','','','','','','','','T1G','Tg','MAXg','T1r','T2r','Max']

                labelTypes = [labelGENROU,labelGENSAL,labelESST1A,labelESST4B,labelEXAC4,labelTGOV1,labelHYGOV,labelGAST,labelPSS2A,labelPVGU1,labelPVEU,labelPANELU1,labelIRRADU1,labelGEWTGCU1,labelGEWTECU1,labelGEWT2MU1,labelGEWTPTU1,labelGEWTARU1,labelGEWTGDU1]
                modelTypes = ['GENROU','GENSAL','ESST1A','ESST4B','EXAC4','TGOV1','HYGOV','GAST','PSS2A','PVGU1','PVEU1','PANELU1','IRRADU1','GEWTGCU1','GEWTECU1','GEWT2MU1','GEWTPTU1','GEWTARU1','GEWTGDU1']

                choice = []
                params = []
                closestVal = 0
                
                modelType = cellVal
                modelType = modelType[1:-1]

                if modelType in modelTypes[:2]:
                    choice = modelTypes[:2]
                    pmaxArr = self.SelectPmax(sourceType,modelType,1)
                    if len(pmaxArr) == 0:
                        wx.MessageBox('There is no Pmax value suitable with this model in database!')
                        self.myGridDyn.SetCellValue(row,col,cellValue)
                    else:
                        closestVal = min(pmaxArr,key = lambda x:abs(float(x)-pmax))
                        params = self.selectGenModel(sourceType,closestVal,modelType)
                        self.updateValue(modelTypes,modelType,labelTypes,params,row1)
                elif modelType in modelTypes[2:5]:
                    pmaxArr = self.SelectPmax(sourceType,modelType,2)
                    if len(pmaxArr) == 0:
                        wx.MessageBox('There is no Pmax value suitable with this model in database!')
                        self.myGridDyn.SetCellValue(row,col,cellValue)
                    else:
                        closestVal = min(pmaxArr,key = lambda x:abs(float(x)-pmax))
                        params = self.selectAVRModel(sourceType,closestVal,modelType)
                        self.updateValue(modelTypes,modelType,labelTypes,params,row1)
                elif modelType in modelTypes[5:8]:
                    pmaxArr = self.SelectPmax(sourceType,modelType,3)
                    if len(pmaxArr) == 0:
                        wx.MessageBox('There is no Pmax value suitable with this model in database!')
                        self.myGridDyn.SetCellValue(row,col,cellValue)
                    else:
                        closestVal = min(pmaxArr,key = lambda x:abs(float(x)-pmax))
                        params = self.selectGOVModel(sourceType,closestVal,modelType)
                        self.updateValue(modelTypes,modelType,labelTypes,params,row1)
                elif modelType == modelTypes[8]:
                    pmaxArr = self.SelectPmax(sourceType,modelType,4)
                    if len(pmaxArr) == 0:
                        wx.MessageBox('There is no Pmax value suitable with this model in database!')
                        self.myGridDyn.SetCellValue(row,col,cellValue)
                    else:
                        closestVal = min(pmaxArr,key = lambda x:abs(float(x)-pmax))
                        params = self.selectPSSModel(sourceType,closestVal,modelType)
                        self.updateValue(modelTypes,modelType,labelTypes,params,row1)
                elif modelType in modelTypes[9:]:
                    pmaxArr = self.SelectPmax(sourceType,modelType,0)
                    if len(pmaxArr) == 0:
                        wx.MessageBox('There is no Pmax value suitable with this model in database!')
                        self.myGridDyn.SetCellValue(row,col,cellValue)
                    else:
                        closestVal = min(pmaxArr,key = lambda x:abs(float(x)-pmax))
                        params = self.selectRenewModel(sourceType,closestVal,modelType)
                        self.updateValue(modelTypes,modelType,labelTypes,params,row1)
                for i in range(100):
                    self.myGridDyn.SetCellTextColour(row1,i,wx.Colour(0,0,0))
                self.set_restriction(modelType,row1) 
            else:
                wx.MessageBox('This gen number is not existing in the sav file!')
        else:
            for i in range(100):
                self.myGridDyn.SetCellTextColour(row1,i,wx.Colour(0,0,0))
            self.set_restriction(modelType,row1) 
            event.Skip()

    def updateValue(self,modelTypes=[],modelType='',labelTypes=[],params=[],row1=0):
        index = modelTypes.index(modelType)
        label = labelTypes[index]
        for i in range(len(label)):
            self.myGridDyn.SetCellValue(row1-1,i,'')
        for i in range(len(params)):
            self.myGridDyn.SetCellValue(row1,i+3,'')
        for i in range(len(label)):
            self.myGridDyn.SetCellValue(row1-1,i,label[i])
        for i in range(len(params)):
            self.myGridDyn.SetCellValue(row1,i+3,str(params[i]))

    # tạo lựa chọn cho các mô hình
    def returnType(self,modelTypes,modelType):
        modelTypes = ['GENROU','GENSAL','ESST1A','ESST4B','EXAC4','TGOV1','HYGOV','GAST','PSS2A','PVGU1','PVEU1','PANELU1','IRRADU1','GEWTGCU1','GEWTECU1','GEWT2MU1','GEWTPTU1','GEWTARU1','GEWTGDU1']
        choice = []
        if modelType in modelTypes[:2]:
            choice = ["'GENROU'","'GENSAL'"]
        elif modelType in modelTypes[2:5]:
            choice = ["'ESST1A'","'ESST4B'","'EXAC4'"]
        elif modelType in modelTypes[5:7]:
            choice = ["'TGOV1'","'HYGOV'","'GAST'"]
        elif modelType == modelTypes[8]:
            choice = ["'PSS2A'"]
        elif modelType in modelTypes[9:]:
            choice = ["'{}'".format(modelType)]

        return choice

    def on_cell_right_click_grid_dyn( self, event ):
        event.Skip()

    # kết nối csdl, chọn quy mô nguồn từ loại nguồn và loại mô hình
    def SelectPmax(self,planType='',model='',flag = 0):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        pmaxArr = []
        if flag == 1:
            cursor.execute("""SELECT DYNAMIC_GEN.[SCALE] FROM DYNAMIC_GEN 
                        WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
        elif flag == 2:
            cursor.execute("""SELECT DYNAMIC_AVR.[SCALE] FROM DYNAMIC_AVR 
                        WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
        elif flag == 3:
            cursor.execute("""SELECT DYNAMIC_GOV.[SCALE] FROM DYNAMIC_GOV 
                        WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
        elif flag == 4:
            cursor.execute("""SELECT DYNAMIC_PSS.[SCALE] FROM DYNAMIC_PSS 
                        WHERE (((DYNAMIC_PSS.[PLAN_TYPE])='{a}') AND (DYNAMIC_PSS.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))
        else:
            cursor.execute("""SELECT DYNAMIC_RENEW.[SCALE] FROM DYNAMIC_RENEW 
                        WHERE (((DYNAMIC_RENEW.[PLAN_TYPE])='{a}') AND (DYNAMIC_RENEW.[TYPE])='{b}');""".format(a=str(planType),b = str(model)))

        for row in cursor.fetchall():
            if not float(row[0]) in pmaxArr:
                pmaxArr.append(float(row[0]))
            else:
                next
        return pmaxArr

    # Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ kích từ theo loại nguồn, theo quy mô và theo loại mô hình (ESST4B/ESST1A/EXAC4)
    def selectAVRModel(self,planType='',pmax =0.0,model2=''):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        if model2 == "ESST4B":
            # label = ['TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
            cursor.execute("""SELECT DYNAMIC_AVR.[TR], DYNAMIC_AVR.[KPR], DYNAMIC_AVR.[KIR], DYNAMIC_AVR.[VRMAX],DYNAMIC_AVR.[VRMAX],
                            DYNAMIC_AVR.[VRMIN],DYNAMIC_AVR.[TA],DYNAMIC_AVR.[KPM],DYNAMIC_AVR.[KIM],DYNAMIC_AVR.[VMMAX],DYNAMIC_AVR.[VMMIN],
                            DYNAMIC_AVR.[KG],DYNAMIC_AVR.[KP],DYNAMIC_AVR.[KI],DYNAMIC_AVR.[VBMAX],DYNAMIC_AVR.[KC],DYNAMIC_AVR.[XL],DYNAMIC_AVR.[THETAP] FROM DYNAMIC_AVR 
                            WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[SCALE])={b} AND (DYNAMIC_AVR.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model2)))
        elif model2 == "EXAC4":
            # label = ["TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
            cursor.execute("""SELECT DYNAMIC_AVR.[TR], DYNAMIC_AVR.[VIMAX], DYNAMIC_AVR.[VIMIN], DYNAMIC_AVR.[TC],DYNAMIC_AVR.[TB],
                            DYNAMIC_AVR.[KA],DYNAMIC_AVR.[TA],DYNAMIC_AVR.[VRMAX],DYNAMIC_AVR.[VRMIN],DYNAMIC_AVR.[KC] FROM DYNAMIC_AVR 
                                WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[SCALE])={b} AND (DYNAMIC_AVR.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model2)))    
        elif model2 == 'ESST1A':
            cursor.execute("""SELECT * FROM DYNAMIC_AVR 
                                WHERE (((DYNAMIC_AVR.[PLAN_TYPE])='{a}') AND (DYNAMIC_AVR.[SCALE])={b} AND (DYNAMIC_AVR.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model2)))    

        values = []
        for row in cursor.fetchall():
            for i in range(len(row)):
                values.append(row[i])
            break
        return values

    # Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ máy phát theo loại nguồn, theo quy mô và theo loại mô hình (GENROU/GENSAL)
    def selectGenModel(self,planType='',pmax =0.0,model1=''):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        values = []
        if model1 == "GENROU":
            
            cursor.execute("""SELECT DYNAMIC_GEN.[T'do], DYNAMIC_GEN.[T''do], DYNAMIC_GEN.[T'qo], DYNAMIC_GEN.[T''qo],DYNAMIC_GEN.[H],
                            DYNAMIC_GEN.[D],DYNAMIC_GEN.[Xd],DYNAMIC_GEN.[Xq],DYNAMIC_GEN.[X'd],DYNAMIC_GEN.[X'q],DYNAMIC_GEN.[X''d],
                            DYNAMIC_GEN.[X1],DYNAMIC_GEN.[S10],DYNAMIC_GEN.[S12] FROM DYNAMIC_GEN 
                            WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[SCALE])={b} AND (DYNAMIC_GEN.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model1)))
        elif model1 == "GENSAL":
            cursor.execute("""SELECT DYNAMIC_GEN.[T'do], DYNAMIC_GEN.[T''do], DYNAMIC_GEN.[T''qo],DYNAMIC_GEN.[H],
                                DYNAMIC_GEN.[D],DYNAMIC_GEN.[Xd],DYNAMIC_GEN.[Xq],DYNAMIC_GEN.[X'd],DYNAMIC_GEN.[X''d],
                                DYNAMIC_GEN.[X1],DYNAMIC_GEN.[S10],DYNAMIC_GEN.[S12] FROM DYNAMIC_GEN
                                WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (DYNAMIC_GEN.[SCALE])={b} AND (DYNAMIC_GEN.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model1)))

        for row in cursor.fetchall():
            for i in range(len(row)):
                values.append(row[i])
            break
        return values

    # Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ điều tốc theo loại nguồn, theo quy mô và theo loại mô hình (TGOV1/HYGOV/GAST)
    def selectGOVModel(self,planType='',pmax=0.0 ,model3=''):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        #TGOV1: label = ['R','T1','VMAX','VMIN','T2','T3','Dt']
        if model3 == "TGOV1":
            cursor.execute("""SELECT DYNAMIC_GOV.[R], DYNAMIC_GOV.[T1], DYNAMIC_GOV.[VMAX], DYNAMIC_GOV.[VMIN],DYNAMIC_GOV.[T2],
                            DYNAMIC_GOV.[T3],DYNAMIC_GOV.[DT] FROM DYNAMIC_GOV 
                            WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[SCALE])={b} AND (DYNAMIC_GOV.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model3)))
        #HYGOV: label = ["R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
        elif model3 == "HYGOV":
            cursor.execute("""SELECT DYNAMIC_GOV.[R], DYNAMIC_GOV.[R2], DYNAMIC_GOV.[TR], DYNAMIC_GOV.[TF],DYNAMIC_GOV.[TG],
                            DYNAMIC_GOV.[VELM],DYNAMIC_GOV.[GMAX],DYNAMIC_GOV.[GMIN],DYNAMIC_GOV.[TW],DYNAMIC_GOV.[AT],DYNAMIC_GOV.[DTURB],DYNAMIC_GOV.[QNL] 
                            FROM DYNAMIC_GOV WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[SCALE])={b} AND (DYNAMIC_GOV.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model3)))
        #GAST: label = ["R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
        elif model3 == 'GAST':
            cursor.execute("""SELECT DYNAMIC_GOV.[R], DYNAMIC_GOV.[T1], DYNAMIC_GOV.[T2], DYNAMIC_GOV.[T3],DYNAMIC_GOV.[AT_GAST],
                            DYNAMIC_GOV.[KT],DYNAMIC_GOV.[VMAX],DYNAMIC_GOV.[VMIN],DYNAMIC_GOV.[DTURB] FROM DYNAMIC_GOV 
                                WHERE (((DYNAMIC_GOV.[PLAN_TYPE])='{a}') AND (DYNAMIC_GOV.[SCALE])={b} AND (DYNAMIC_GOV.[TYPE])='{c}');""".format(a=str(planType),b=str(pmax),c=str(model3)))
        values = []
        for row in cursor.fetchall():
            for i in range(len(row)):
                values.append(row[i])
            break
        return values

    # Kết nối với cơ sở dữ liệu, lựa chọn thông số bộ ổn định theo loại nguồn và theo quy mô
    def selectPSSModel(self,planType='',pmax =0.0,model4=''):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        # label = ['IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
        cursor.execute("""SELECT DYNAMIC_PSS.[IC1], DYNAMIC_PSS.[REMBUS1], DYNAMIC_PSS.[IC2], DYNAMIC_PSS.[REMBUS2],DYNAMIC_PSS.[M],
                        DYNAMIC_PSS.[N],DYNAMIC_PSS.[TW1],DYNAMIC_PSS.[TW2],DYNAMIC_PSS.[T6],DYNAMIC_PSS.[TW3],DYNAMIC_PSS.[TW4],DYNAMIC_PSS.[T7],
                        DYNAMIC_PSS.[Ks2],DYNAMIC_PSS.[Ks3],DYNAMIC_PSS.[T8],DYNAMIC_PSS.[T9],DYNAMIC_PSS.[Ks1],DYNAMIC_PSS.[T1],DYNAMIC_PSS.[T2],
                        DYNAMIC_PSS.[T3],DYNAMIC_PSS.[T4],DYNAMIC_PSS.[VSTMAX],DYNAMIC_PSS.[VATMIN] FROM DYNAMIC_PSS 
                            WHERE (((DYNAMIC_PSS.[PLAN_TYPE])='{a}') AND (DYNAMIC_PSS.[SCALE])={b});""".format(a=str(planType),b=str(pmax)))
        values = []
        for row in cursor.fetchall():
            for i in range(len(row)):
                values.append(row[i])
            break
        return values

    # Kết nối với cơ sở dữ liệu, lựa chọn thông số mô hình NLTT
    def selectRenewModel(self,planType='',pmax =0):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT DYNAMIC_RENEW.[TYPE] FROM DYNAMIC_RENEW WHERE (((DYNAMIC_RENEW.[PLAN_TYPE])='{a}'));""".format(a=str(planType)))
        renewType = []

        for row in cursor.fetchall():
            if not row[0] in renewType:
                renewType.append(row[0])
        return renewType
    
    # Đặt điều kiện ràng buộc để xác định những giá trị nằm ngoài vùng giới hạn cho phép
    def set_restriction(self,model='',row=0):
        if model == 'GENSAL':
            # labelGENSAL = ['','','',"T'do",'T"do','T"qo','H','D','Xd','Xq',"X'd",'X"d','X1','S(1.0)','S(1.2)']
            T1do = float(self.myGridDyn.GetCellValue(row,3))
            T2do = float(self.myGridDyn.GetCellValue(row,4))
            T2qo = float(self.myGridDyn.GetCellValue(row,5))
            H = float(self.myGridDyn.GetCellValue(row,6))
            D = float(self.myGridDyn.GetCellValue(row,7))
            Xd = float(self.myGridDyn.GetCellValue(row,8))
            Xq = float(self.myGridDyn.GetCellValue(row,9))
            X1d = float(self.myGridDyn.GetCellValue(row,10))
            X2d = float(self.myGridDyn.GetCellValue(row,11))
            X1 = float(self.myGridDyn.GetCellValue(row,12))
            S10 = float(self.myGridDyn.GetCellValue(row,13))
            S12 = float(self.myGridDyn.GetCellValue(row,14))

            # 0.5*Xd - X'd  > 0
            dk1 = 0.5*Xd - X1d 
            if dk1 <= 0:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
            
            # Xd - Xq > 0
            dk2 = Xd - Xq
            if dk2 <= 0:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)

            # Xq - X'd > 0
            dk3 = Xq - X1d
            if dk3 <= 0:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)

            # dk4 > 0
            dk4 = X1d - X2d
            if dk4 <= 0:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
            
            # dk5 > 0
            dk5 = X2d - X1
            if dk5 <= 0:
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)

            # add 
            DELT = 0.01
            # 1<H<10
            if H<=1 or H>=10:
                self.myGridDyn.SetCellTextColour(row,6, wx.RED)

            # 0<=D<3
            if D<0 or D>=3:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)

            # 1<T1do<10
            if T1do <=1 or T1do >=10:
                self.myGridDyn.SetCellTextColour(row,3, wx.RED)

            # 0.2 <= T1qo <= 1.5

            # 4*DELT <T2do <0.2
            if T2do <= 0.04 or T2do >=0.2:
                self.myGridDyn.SetCellTextColour(row,4, wx.RED)

            # 4*DELT <T2qo <0.2
            if T2qo <= 0.04 or T2qo >=0.2:
                self.myGridDyn.SetCellTextColour(row,5, wx.RED)

            # Xd <2.5
            if Xd >=2.5:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)

            # S10 > 0
            if S10 <=0:
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)

            # S10 > S12
            if (S10 - S12) <= 0:
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)
                self.myGridDyn.SetCellTextColour(row,14, wx.RED)

        elif model == 'GENROU':
            # labelGENROU = ['','','',"T'do",'T"do',"T'qo",'T"qo','H','D','Xd','Xq',"X'd","X'q",'X"d','X1','S(1.0)','S(1.2)']
            T1do = float(self.myGridDyn.GetCellValue(row,3))
            T2do = float(self.myGridDyn.GetCellValue(row,4))
            T1qo = float(self.myGridDyn.GetCellValue(row,5))
            T2qo = float(self.myGridDyn.GetCellValue(row,6))
            H = float(self.myGridDyn.GetCellValue(row,7))
            D = float(self.myGridDyn.GetCellValue(row,8))
            Xd = float(self.myGridDyn.GetCellValue(row,9))
            Xq = float(self.myGridDyn.GetCellValue(row,10))
            X1d = float(self.myGridDyn.GetCellValue(row,11))
            X1q = float(self.myGridDyn.GetCellValue(row,12))
            X2d = float(self.myGridDyn.GetCellValue(row,13))
            X1 = float(self.myGridDyn.GetCellValue(row,14))
            S10 = float(self.myGridDyn.GetCellValue(row,15))
            S12 = float(self.myGridDyn.GetCellValue(row,16))
            # X2d = IMAG 
            # 0.5*Xd - X'd  > 0
            dk1 = 0.5*Xd - X1d 
            if dk1 <= 0:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
            
            # Xd - Xq > 0
            dk2 = Xd - Xq
            if dk2 <= 0:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)

            # Xq - X'd > 0
            dk3 = Xq - X1d
            if dk3 <= 0:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)

            # dk4 > 0
            dk4 = X1d - X2d
            if dk4 <= 0:
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)
            
            # dk5 > 0
            dk5 = X2d - X1
            if dk5 <= 0:
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)
                self.myGridDyn.SetCellTextColour(row,14, wx.RED)

            # add 
            DELT = 0.01
            # 1<H<10
            if H<=1 or H>=10:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)

            # 0<=D<3
            if D<0 or D>=3:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)

            # 1<T1do<10
            if T1do <=1 or T1do >=10:
                self.myGridDyn.SetCellTextColour(row,3, wx.RED)

            # 0.2 <= T1qo <= 1.5
            if T1qo < 0.2 or T1qo > 1.5:
                self.myGridDyn.SetCellTextColour(row,5, wx.RED)

            # 4*DELT <T2do <0.2
            if T2do <= 0.04 or T2do >=0.2:
                self.myGridDyn.SetCellTextColour(row,4, wx.RED)

            # 4*DELT <T2qo <0.2
            if T2qo <= 0.04 or T2qo >=0.2:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)

            # Xd <2.5
            if Xd >=2.5:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)

            # S10 > 0
            if S10 <=0:
                self.myGridDyn.SetCellTextColour(row,15, wx.RED)

            # S10 > S12
            if (S10 - S12) <= 0:
                self.myGridDyn.SetCellTextColour(row,15, wx.RED)
                self.myGridDyn.SetCellTextColour(row,16, wx.RED)

            # X1q < Xq
            if (Xq - X1q) <= 0:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)

            # X1d < X1q
            if (X1q < X1d) <= 0:
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)

            # X2d < X1q
            if (X1q < X2d) <= 0:
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)

        elif model == 'ESST4B':
            # labelESST4B = ['','','','TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
            TR = float(self.myGridDyn.GetCellValue(row,3))
            KPR = float(self.myGridDyn.GetCellValue(row,4))
            KIR = float(self.myGridDyn.GetCellValue(row,5))
            VRMAX = float(self.myGridDyn.GetCellValue(row,6))
            VRMIN = float(self.myGridDyn.GetCellValue(row,7))
            TA = float(self.myGridDyn.GetCellValue(row,8))
            KPM = float(self.myGridDyn.GetCellValue(row,9))
            KIM = float(self.myGridDyn.GetCellValue(row,10))
            VMMAX = float(self.myGridDyn.GetCellValue(row,11))
            VMMIN = float(self.myGridDyn.GetCellValue(row,12))
            KG = float(self.myGridDyn.GetCellValue(row,13))
            KP = float(self.myGridDyn.GetCellValue(row,14))
            KI = float(self.myGridDyn.GetCellValue(row,15))
            VBMAX = float(self.myGridDyn.GetCellValue(row,16))
            KC = float(self.myGridDyn.GetCellValue(row,17))
            XL = float(self.myGridDyn.GetCellValue(row,18))
            THETAP = float(self.myGridDyn.GetCellValue(row,19))

            if TR<0 or TR >0.5:
                self.myGridDyn.SetCellTextColour(row,3, wx.RED)
            if KPR<0 or KPR >75:
                self.myGridDyn.SetCellTextColour(row,4, wx.RED)
            if KIR<0 or KIR >75:
                self.myGridDyn.SetCellTextColour(row,5, wx.RED)
            if VRMAX<0.8 or VRMAX>10:
                self.myGridDyn.SetCellTextColour(row,6, wx.RED)
            if VRMIN<-6 or VRMIN>0:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)
            if TA<0 or TA >=1:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)
            if KPM<0 or KPM >1.2:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
            if KIM<0 or KIM >18:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
            if VMMAX<0.8 or VMMAX >118:
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
            if VMMIN<-118.8 or VMMIN >0:
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)
            if KG<0 or KG>=1.1:
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)
            if KP<1 or KP>=10:
                self.myGridDyn.SetCellTextColour(row,14, wx.RED)
            if KI<0 or KI >1.1:
                self.myGridDyn.SetCellTextColour(row,15, wx.RED)
            if VBMAX<=1 or VBMAX >=20:
                self.myGridDyn.SetCellTextColour(row,16, wx.RED)
            if KC<0 or KC >=1:
                self.myGridDyn.SetCellTextColour(row,17, wx.RED)
            if XL<0 or XL >=0.5:
                self.myGridDyn.SetCellTextColour(row,18, wx.RED)
            if THETAP<=-90 or THETAP >=90:
                self.myGridDyn.SetCellTextColour(row,19, wx.RED)

        elif model == 'EXAC4':
            # labelEXAC4 = ['','','',"TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
            TR = float(self.myGridDyn.GetCellValue(row,3))
            VIMAX = float(self.myGridDyn.GetCellValue(row,4))
            VIMIN = float(self.myGridDyn.GetCellValue(row,5))
            TC = float(self.myGridDyn.GetCellValue(row,6))
            TB = float(self.myGridDyn.GetCellValue(row,7))
            KA = float(self.myGridDyn.GetCellValue(row,8))
            TA = float(self.myGridDyn.GetCellValue(row,9))
            VRMAX = float(self.myGridDyn.GetCellValue(row,10))
            VRMIN = float(self.myGridDyn.GetCellValue(row,11))
            KC = float(self.myGridDyn.GetCellValue(row,12))

            if TR<0 or TR >0.1:
                self.myGridDyn.SetCellTextColour(row,3, wx.RED)
            if VIMAX<=0 or VIMAX >0.2:
                self.myGridDyn.SetCellTextColour(row,4, wx.RED)
            if VIMIN<=-0.2 or VIMIN >0:
                self.myGridDyn.SetCellTextColour(row,5, wx.RED)
            if TC<0 or TC >=10:
                self.myGridDyn.SetCellTextColour(row,6, wx.RED)
            if TB<=0.04 or TB >=20:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)
            if KA<=50 or KA >1000:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)
            if TA<0 or TA >=0.5:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
            if VRMAX<3 or VRMAX >8:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
            if VRMIN<-8 or VRMIN >-3:
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
            if KC<0 or KC >0.3:
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)

        # GOV
        elif model == 'TGOV1':
        # labelTGOV1 = ['','','','R','T1','VMAX','VMIN','T2','T3','Dt']
            R = float(self.myGridDyn.GetCellValue(row,3))
            T1 = float(self.myGridDyn.GetCellValue(row,4))
            VMAX = float(self.myGridDyn.GetCellValue(row,5))
            VMIN = float(self.myGridDyn.GetCellValue(row,6))
            T2 = float(self.myGridDyn.GetCellValue(row,7))
            T3 = float(self.myGridDyn.GetCellValue(row,8))
            Dt = float(self.myGridDyn.GetCellValue(row,9))
            
            if R<=0 or R >=0.1:
                self.myGridDyn.SetCellTextColour(row,3, wx.RED)
            if T1<=0.04 or T1>=0.5:
                self.myGridDyn.SetCellTextColour(row,4, wx.RED)
            if VMAX<=0.5 or VMAX >=1.2 or VMAX <= VMIN:
                self.myGridDyn.SetCellTextColour(row,5, wx.RED)
            if VMIN<0 or VMIN >=1.0 or VMIN>=VMAX:
                self.myGridDyn.SetCellTextColour(row,6, wx.RED)
            if T2<=0 or T3<2*T2:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)
            if T3<=0.04 or T3 >=10.0 or T3<2*T2:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)
            if Dt<0 or Dt >=0.5:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)

        elif model == 'HYGOV':
        # labelHYGOV = ['','','',"R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
            R = float(self.myGridDyn.GetCellValue(row,3))
            r = float(self.myGridDyn.GetCellValue(row,4))
            Tr = float(self.myGridDyn.GetCellValue(row,5))
            Tf = float(self.myGridDyn.GetCellValue(row,6))
            Tg = float(self.myGridDyn.GetCellValue(row,7))
            VELM = float(self.myGridDyn.GetCellValue(row,8))
            GMAX = float(self.myGridDyn.GetCellValue(row,9))
            GMIN = float(self.myGridDyn.GetCellValue(row,10))
            TW = float(self.myGridDyn.GetCellValue(row,11))
            At = float(self.myGridDyn.GetCellValue(row,12))
            Dturb = float(self.myGridDyn.GetCellValue(row,13))
            qNL = float(self.myGridDyn.GetCellValue(row,14))

            if R<=0 or R >=0.1 or R>r:
                self.myGridDyn.SetCellTextColour(row,3, wx.RED)
            if r<=0 or r>=2 or r<R:
                self.myGridDyn.SetCellTextColour(row,4, wx.RED)
            if Tr<=0.04 or Tr >=30:
                self.myGridDyn.SetCellTextColour(row,5, wx.RED)
            if Tf<=0.04 or Tf >=0.1:
                self.myGridDyn.SetCellTextColour(row,6, wx.RED)
            if Tg<=0.04 or Tg >=1.0:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)
            if VELM<=0 or VELM >=0.3:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)
            if GMAX<=0 or GMAX >1 or GMAX<=GMIN:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
            if GMIN<=0 or GMIN >1 or GMAX<=GMIN:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
            if TW<=0.5 or TW >=3.0:
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
            if At<=0.8 or At >=1.5:
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)
            if Dturb<0 or Dturb >=0.5 :
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)
            if qNL<=0 or qNL>0.15:
                self.myGridDyn.SetCellTextColour(row,14, wx.RED)

        elif model == 'GAST':
        # labelGAST = ['','','',"R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
            R = float(self.myGridDyn.GetCellValue(row,3))
            T1 = float(self.myGridDyn.GetCellValue(row,4))
            T2 = float(self.myGridDyn.GetCellValue(row,5))
            T3 = float(self.myGridDyn.GetCellValue(row,6))
            AT = float(self.myGridDyn.GetCellValue(row,7))
            KT = float(self.myGridDyn.GetCellValue(row,8))
            VMAX = float(self.myGridDyn.GetCellValue(row,9))
            VMIN = float(self.myGridDyn.GetCellValue(row,10))
            Dturb = float(self.myGridDyn.GetCellValue(row,11))

            if R<=0 or R >=0.1:
                self.myGridDyn.SetCellTextColour(row,3, wx.RED)
            if T1<=0.04 or T1 >=0.5:
                self.myGridDyn.SetCellTextColour(row,4, wx.RED)
            if T2<=0.04 or T2 >=0.5:
                self.myGridDyn.SetCellTextColour(row,5, wx.RED)
            if T3<=0.04 or T3 >=5.0:
                self.myGridDyn.SetCellTextColour(row,6, wx.RED)
            if AT<=0 or AT >1:
                self.myGridDyn.SetCellTextColour(row,7, wx.RED)
            if AT<=0 or AT >=5.0:
                self.myGridDyn.SetCellTextColour(row,8, wx.RED)
            if VMAX<=0.5 or VMAX >=1.2 or VMAX<=VMIN:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
            if VMIN<0 or VMIN >=1.0 or VMAX<=VMIN:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
            if Dturb<0 or Dturb >=0.5 :
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
        # PSS
        elif model == 'PSS2A':
            # labelPSS2A = ['IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
            T1 = float(self.myGridDyn.GetCellValue(row,20))
            T2 = float(self.myGridDyn.GetCellValue(row,21))
            T3 = float(self.myGridDyn.GetCellValue(row,22))
            T4 = float(self.myGridDyn.GetCellValue(row,23))
            T6 = float(self.myGridDyn.GetCellValue(row,11))
            T7 = float(self.myGridDyn.GetCellValue(row,14))
            T8 = float(self.myGridDyn.GetCellValue(row,17))
            T9 = float(self.myGridDyn.GetCellValue(row,18))
            TW1 = float(self.myGridDyn.GetCellValue(row,9))
            TW2 = float(self.myGridDyn.GetCellValue(row,10))
            TW3 = float(self.myGridDyn.GetCellValue(row,12))
            TW4 = float(self.myGridDyn.GetCellValue(row,13))
            VSTMAX = float(self.myGridDyn.GetCellValue(row,24))
            VATMIN = float(self.myGridDyn.GetCellValue(row,25))

            if TW1<1.5 or TW1 > 15:
                self.myGridDyn.SetCellTextColour(row,9, wx.RED)
            if TW2<1.5 or TW2 > 15:
                self.myGridDyn.SetCellTextColour(row,10, wx.RED)
            if TW3<1.5 or TW3 > 15:
                self.myGridDyn.SetCellTextColour(row,12, wx.RED)
            if TW4<1.5 or TW4 > 15:
                self.myGridDyn.SetCellTextColour(row,13, wx.RED)
            if T1<0.02 or T1 > 2.0:
                self.myGridDyn.SetCellTextColour(row,20, wx.RED)
            if T3<0.02 or T3 > 2.0:
                self.myGridDyn.SetCellTextColour(row,22, wx.RED)
            if T2<0.02 or T2 > 6.0:
                self.myGridDyn.SetCellTextColour(row,21, wx.RED)
            if T4<0.02 or T4 > 6.0:
                self.myGridDyn.SetCellTextColour(row,23, wx.RED)
            if T6<=0.02:
                self.myGridDyn.SetCellTextColour(row,11, wx.RED)
            if T7<=0.02:
                self.myGridDyn.SetCellTextColour(row,14, wx.RED)
            if T8<=0.02 or T8 > 2.0:
                self.myGridDyn.SetCellTextColour(row,17, wx.RED)
            if VSTMAX<=0 or VSTMAX>=0.99:
                self.myGridDyn.SetCellTextColour(row,24, wx.RED)
            if VATMIN<-0.3 or VATMIN> 0:
                self.myGridDyn.SetCellTextColour(row,25, wx.RED)
    
    # tìm kiếm thông tin từ ô Number trong bảng dynamic
    @profiled('search.dynamic_number')
    @batched_grid_update('myGridDyn')
    def dynNumberEnter_Fcn(self,event):
        genNum = self.parent.search_dyn.GetValue()
        result = []
        indexNum = []

        if genNum != '':
            rows = self.myGridDyn.GetNumberRows()
            cols = self.myGridDyn.GetNumberCols()

            for i in range(rows):
                if str(genNum) in str(self.myGridDyn.GetCellValue(i,0)):
                    val = []
                    label = []
                    for j in range(cols):
                        label.append(self.myGridDyn.GetCellValue(i-1,j))
                        val.append(self.myGridDyn.GetCellValue(i,j))
                    result.append(label)
                    result.append(val)
                    indexNum.append(i)

            if len(result)!=0:
                # change cursor to the source row
                self.myGridDyn.SetGridCursor(indexNum[0],0)
                
                # change viewPort to the source row
                self.myGridDyn.MakeCellVisible(indexNum[0],0)
                dialog = SearchDyn(self.parent)
                
                for i in range(len(result)):
                    for j in range(100):
                        dialog.gridDynSearch.SetCellValue(i,j,result[i][j])
                dialog.ShowModal()
