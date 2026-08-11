# -*- coding: utf-8 -*-
import pyodbc
import time
from Tool_V7 import MyFrame1
import glob, os, sys
import pssepath
import wx
import wx.xrc
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
import numpy as np
from DialogBox import getInput
from LoadTab import loadMachineTab
from math import *
from decimal import *
from gridSearch import CustomGridSearch
from dialogAddBranch import Add_New_Branch
from dialogAdd2Wind import Add_New_2Wind
from dialogAdd3Wind import Add_New_3Wind
from redirectOuput import silence
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadMachineTab,loadShuntTab,loadLoadTab,loadSourceLoadInfo


row = 0
col = 0
busNumber = 0
status = 1
toBus = 0
branchID = ''
branchInfoList = []
TWOPLACE = Decimal(10)**-2
FIVEPLACE = Decimal(10)**-5
    
class ConnectDatabase(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.Path = ''
        self.PathFile = [[]]
        self.parent = parent
        self.matrixBranch = []
        self.matrixMachine = []
        self.myGridBusInfo = wx.grid.Grid
        self.indexFile = 0
        self.uk = 0
        self.matrixBus = []
        self.myGridBus = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.matrixZone = []
        self.myGridArea = wx.grid.Grid
        self.matrixArea = []
        self.myGridFile = wx.grid.Grid
        self.fileInfoTranspose = []
        self.location = ''

    # lấy thông tin đường dây từ loại đường dây
    def SelectBranchInfoFromType(self,typeBr = '',voltage = 0):
        branchType = typeBr
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ= Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT LINE_MODELS_2.[BASE], LINE_MODELS_2.[TYPE], LINE_MODELS_2.[I], LINE_MODELS_2.[Ro], LINE_MODELS_2.[Xo], LINE_MODELS_2.[Go], LINE_MODELS_2.[Bo], LINE_MODELS_2.[RoZero], LINE_MODELS_2.[XoZero], LINE_MODELS_2.[GoZero], LINE_MODELS_2.[BoZero], LINE_MODELS_2.[S_MVA]
                        FROM LINE_MODELS_2 WHERE (((LINE_MODELS_2.[TYPE])='{a}') AND ((LINE_MODELS_2.[BASE])={b}));""".format(a=typeBr,b=voltage))
        # SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS; # 

        for row in cursor.fetchall():
            baseKV = row[0]
            lineType = row[1]  
            current = row[2]
            Ro = row[3]
            Xo = row[4]
            Go = row[5]
            Bo = row[6]
            RoZero = row[7]
            XoZero = row[8]
            GoZero = row[9]
            BoZero = row[10]
            S_MVA = row[11]

        return baseKV,lineType,current,Ro,Xo,Bo,RoZero,XoZero,GoZero,BoZero,S_MVA

    # lấy thông tin MBA 2 CD từ loại MBA 2 CD
    def SelectTransInfoFromType(self,typeTrans = ''):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ= Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT TRANS_MODELS_2_WIND.[TYPE], TRANS_MODELS_2_WIND.[R],TRANS_MODELS_2_WIND.[X],TRANS_MODELS_2_WIND.[RATE],
                        TRANS_MODELS_2_WIND.[R01],TRANS_MODELS_2_WIND.[X01] FROM TRANS_MODELS_2_WIND WHERE (((TRANS_MODELS_2_WIND.[TYPE])='{a}'));""".format(a=typeTrans))
        # SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS; # 
        

        for row in cursor.fetchall():
            transType = row[0]
            R = row[1]  
            X = row[2]
            Rate = row[3]
            R01 = row[4]
            X01 = row[5]      
        return transType,R,X,Rate,R01,X01

    # lấy thông tin MBA 3 CD từ loại MBA 3 CD
    def SelectTransInfoFromType2(self,typeTrans = ''):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT TRANS_MODELS_3_WIND.[TYPE], TRANS_MODELS_3_WIND.[SBASE1],TRANS_MODELS_3_WIND.[R12],TRANS_MODELS_3_WIND.[X12],
                        TRANS_MODELS_3_WIND.[R23],TRANS_MODELS_3_WIND.[X23],TRANS_MODELS_3_WIND.[R31],TRANS_MODELS_3_WIND.[X31],TRANS_MODELS_3_WIND.[PCA],
                        TRANS_MODELS_3_WIND.[PTA], TRANS_MODELS_3_WIND.[PHA] FROM TRANS_MODELS_3_WIND WHERE (((TRANS_MODELS_3_WIND.[TYPE])='{a}'));""".format(a=typeTrans))
        # SELECT LINE_MODELS.[TYPE] FROM LINE_MODELS; # 

        for row in cursor.fetchall():
            transType = row[0]
            Base = row[1]
            R12 = row[2]  
            X12 = row[3]
            R23 = row[4]  
            X23 = row[5]
            R31 = row[6]  
            X31 = row[7]
            PCA = row[8]
            PTA = row[9]
            PHA = row[10]
        return transType,Base,R12,X12,R23,X23,R31,X31,PCA,PTA,PHA

    # lấy tất cả thông tin của đường dây theo loại và cấp điện áp
    def SelectAllBranchType(self,voltage):
        os.chdir(self.location)
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT LINE_MODELS_2.[BASE], LINE_MODELS_2.[TYPE], LINE_MODELS_2.[I],LINE_MODELS_2.[Ro],LINE_MODELS_2.[Xo],LINE_MODELS_2.[S_MVA] FROM LINE_MODELS_2 WHERE ((LINE_MODELS_2.[BASE])={b});""".format(b=voltage))

        baseKV = [[]]
        lineType = [[]]
        current = [[]]
        Ro = [[]]
        Xo = [[]]
        S_MVA = [[]]

        for row in cursor.fetchall():
            baseKV[0].append(row[0])
            lineType[0].append(row[1])
            current[0].append(row[2])
            Ro[0].append(row[3])
            Xo[0].append(row[4])
            S_MVA[0].append(row[5])
        branchType = np.array([baseKV[0],lineType[0],current[0],Ro[0],Xo[0],S_MVA[0]])
        return branchType

    # lấy tất cả thông tin của MBA 3 cuộn dây theo loại và cấp điện áp 
    def SelectAllTransType(self):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT TRANS_MODELS_3_WIND.[BASE], TRANS_MODELS_3_WIND.[TYPE], TRANS_MODELS_3_WIND.[SBASE1],TRANS_MODELS_3_WIND.[R12],TRANS_MODELS_3_WIND.[X12] FROM TRANS_MODELS_3_WIND;""")

        baseKV = [[]]
        transType = [[]]
        sBase = [[]]
        R12 = [[]]
        X12 = [[]]
        for row in cursor.fetchall():
            baseKV[0].append(row[0])
            transType[0].append(row[1])
            sBase[0].append(row[2])
            R12[0].append(row[3])
            X12[0].append(row[4])
        trans3Type = np.array([baseKV[0],transType[0],sBase[0],R12[0],X12[0]])
        return trans3Type

    # lấy tất cả thông tin của MBA 2 cuộn dây theo loại và cấp điện áp
    def SelectAllTrans2WindType(self):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT TRANS_MODELS_2_WIND.[TYPE], TRANS_MODELS_2_WIND.[R],TRANS_MODELS_2_WIND.[X],TRANS_MODELS_2_WIND.[RATE],TRANS_MODELS_2_WIND.[R01],TRANS_MODELS_2_WIND.[X01] FROM TRANS_MODELS_2_WIND;""")

        transType = [[]]
        Rate = [[]]
        R = [[]]
        X = [[]]
        R01 = [[]]
        X01 = [[]]
        for row in cursor.fetchall():
            transType[0].append(row[0])   
            R[0].append(row[1])
            X[0].append(row[2])
            Rate[0].append(row[3])
            R01[0].append(row[4])
            X01[0].append(row[5])
        transType = np.array([transType[0],R[0],X[0],Rate[0],R01[0],X01[0]])
        return transType

    # lấy tất cả các loại đường dây theo cấp điện áp
    def SelectAllLineTypeByBusVoltage(self,BusNum = 0):
        psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(BusNum)],0,[],0,[])
        ierr, busBaseKV = psspy.abusreal(0,2,'BASE')

        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT LINE_MODELS_2.[TYPE] FROM LINE_MODELS_2 WHERE (((LINE_MODELS_2.[BASE])={a}));""".format(a=float(busBaseKV[0][0])))

        lineType = [[]]

        for row in cursor.fetchall():
            lineType[0].append(row[0])
        linesType = np.array([lineType[0]])
        return linesType

    # lấy tất cả các loại đường dây theo cấp điện áp
    def SelectAllTransTypeByBusVoltage(self,BusNum = 0):
        psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(BusNum)],0,[],0,[])
        ierr, busBaseKV = psspy.abusreal(0,2,'BASE')

        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT TRANS_MODELS_3_WIND.[TYPE] FROM TRANS_MODELS_3_WIND WHERE (((TRANS_MODELS_3_WIND.[BASE])={a}));""".format(a=float(busBaseKV[0][0])))

        TranType = [[]]

        for row in cursor.fetchall():
            TranType[0].append(row[0])
        TransType = np.array([TranType[0]])
        return TransType
    
    # lấy thông tin đường dây và MBA ứng với bus tìm kiếm
    def loadBusNumberEnter(self,busNum = 0):
        with open('output', 'w') as f, silence(f):
            psspy.save(self.Path)
        global busNumber
        busNumber = busNum
        # create subnumber from bus number
        psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(busNumber)],0,[],0,[])
        # branch
        ierr, fromNumber = psspy.abrnint (0, 2,2,2,1,'FROMNUMBER')
        ierr, fromName = psspy.abrnchar (0, 2,2,2,1,'FROMNAME')
        ierr, toNumber = psspy.abrnint (0, 2,2,2,1,'TONUMBER')
        ierr, toName = psspy.abrnchar (0, 2,2,2,1,'TONAME')
        ierr, busBaseKV = psspy.abusreal(0,2,'BASE')
        ierr, chargingB = psspy.abrnreal(0, 2,2,2,1,'CHARGING')
        ierr, chargingBZero = psspy.abrnreal(0, 2,2,2,1,'CHARGINGZERO')
        # print("toNumber,fromNumber: ",toNumber,fromNumber)

        for i in range(len(fromNumber[0])):
            if busNumber in fromNumber[0]:
                index = fromNumber[0].index(busNumber)
                fromNumber[0].remove(busNumber)
                fromName[0].remove(fromName[0][index])

        for i in range(len(toNumber[0])):
            if busNumber in toNumber[0]:
                index = toNumber[0].index(busNumber)
                toNumber[0].remove(busNumber)
                toName[0].remove(toName[0][index])
        for i in range(len(toNumber[0])):
            fromNumber[0].append(toNumber[0][i])
            fromName[0].append(toName[0][i])

        ierr, branchID = psspy.abrnchar (0, 2,2,2,1,'ID')
        ierr, inService = psspy.abrnint (0, 2,2,2,1,'STATUS')
        ierr, PBranch = psspy.aflowreal(0, 2,2, 2, "P")
        ierr, QBranch = psspy.aflowreal(0, 2, 2, 2, "Q")
        ierr, MVABranch = psspy.aflowreal(0, 2,2, 2, "MVA")
        ierr, lineRX = psspy.abrncplx (0, 2,2,2,1,'RX') #
        ierr, lineRXZero = psspy.abrncplx (0, 2,2,2,1,'RXZERO') #
        ierr, chargingB = psspy.abrnreal (0, 2,2,2,1,'CHARGING') # complex
        ierr, length = psspy.abrnreal (0, 2,2,2,1,'LENGTH')
        ierr, rateA = psspy.abrnreal (0, 2,2,2,1,'RATEA')

        # Sdm = sqrt(3)*V*Idm*0.001 (RateA,B,C)
        # %load = MVA/Sdm
        lineRUnit = [[]]
        lineXUnit = [[]]
        lineBUnit = [[]]
        lineR = [[]]
        lineX = [[]]
        lineR0 = [[]]
        lineX0 = [[]]

        loadPercent = [[]]
        PBranchNew = [[]]
        QBranchNew = [[]]
        typeBus = [[]]
        lengthNew = [[]]
        rateANew = [[]]
        for i in range(len(fromNumber[0])):
            lineR[0].append(Decimal(lineRX[0][i].real).quantize(FIVEPLACE))
            lineX[0].append(Decimal(lineRX[0][i].imag).quantize(FIVEPLACE))
            lineR0[0].append(Decimal(lineRXZero[0][i].real).quantize(FIVEPLACE))
            lineX0[0].append(Decimal(lineRXZero[0][i].imag).quantize(FIVEPLACE))
            lengthNew[0].append(Decimal(length[0][i]).quantize(FIVEPLACE))
            rateANew[0].append(Decimal(rateA[0][i]).quantize(FIVEPLACE))
            if (rateA[0][i]*length[0][i] != 0):
                loadPercent[0].append(round(MVABranch[0][i]*100/rateA[0][i]))
                lineRUnit[0].append(Decimal((lineRX[0][i].real)*pow((busBaseKV[0][0]),2)/(100*length[0][i])).quantize(FIVEPLACE)) # lineR unit
                lineXUnit[0].append(Decimal((lineRX[0][i].imag)*pow((busBaseKV[0][0]),2)/(100*length[0][i])).quantize(FIVEPLACE)) # lineX unit
            else:
                loadPercent[0].append(0)
                lineRUnit[0].append(0)
                lineXUnit[0].append(0)
            PBranchNew[0].append(Decimal(PBranch[0][i]).quantize(TWOPLACE))
            QBranchNew[0].append(Decimal(QBranch[0][i]).quantize(TWOPLACE))
            typeBus[0].append('Line')

        [baseKV,lineType,current,Ro,Xo,Rate] = self.SelectAllBranchType(str(busBaseKV[0][0]))
        typebr =[[]]
        

        for i in range(len(lineXUnit[0])):
            diff= []
            index = []

            for j in range(len(lineType)):
                if int(busBaseKV[0][0]) == 500:
                    if abs(float(lineXUnit[0][i])-float(Xo[j]))<=0.0001 and abs(float(lineRUnit[0][i])-float(Ro[j]))<=0.0001 and float(baseKV[j]) == busBaseKV[0][0] and abs(float(rateA[0][i])-float(Rate[j]))<0.5:
                        diff.append(abs(float(lineXUnit[0][i])-float(Xo[j])))
                        index.append(j)

                elif int(busBaseKV[0][0]) == 220:
                    if abs(float(lineXUnit[0][i])-float(Xo[j]))<=0.0001 and abs(float(lineRUnit[0][i])-float(Ro[j]))<=0.0001 and float(baseKV[j]) == busBaseKV[0][0] and abs(float(rateA[0][i])-float(Rate[j]))<0.5:
                        diff.append(abs(float(lineXUnit[0][i])-float(Xo[j])))
                        index.append(j)

                else: # Vbase = 110kV

                    if abs(float(lineXUnit[0][i])-float(Xo[j]))<=0.0001 and abs(float(lineRUnit[0][i])-float(Ro[j]))<=0.0001 and float(baseKV[j]) == busBaseKV[0][0] and abs(float(rateA[0][i])-float(Rate[j]))<0.5:
                        diff.append(abs(float(lineXUnit[0][i])-float(Xo[j])))
                        index.append(j)
                        

            if len(index) != 0:
                indexLinetype = diff.index(min(diff))
                typebr[0].append(lineType[index[indexLinetype]])
            else:
                typebr[0].append("NaN")
        # mảng thông tin đường dây nối tới bus tìm kiếm
        matrixBranch = np.array([typeBus[0],typebr[0],fromNumber[0],fromName[0],branchID[0],inService[0],PBranchNew[0],QBranchNew[0],loadPercent[0],lengthNew[0],rateANew[0],lineR[0],lineX[0],chargingB[0],lineR0[0],lineX0[0],chargingBZero[0]])

        # machine = 2-winding 
        ierr, machineBusNumber = psspy.abrnint (0, 2,3,6,1,'TONUMBER')
        ierr, machineFromBusNumber = psspy.abrnint (0, 2,3,6,1,'FROMNUMBER')
        ierr, machineName = psspy.abrnchar (0, 2,3,6,1,'TONAME')
        # ierr, name2Wind = psspy.abrnchar (0, 2,3,6,1,'XFRNAME')
        ierr, sBase1 = psspy.atrnreal(0, 2, 3, 2,1,"SBASE1" )
        ierr, P2Wind = psspy.atrnreal(0, 2, 3, 2,2,"P")
        ierr, Q2Wind = psspy.atrnreal(0, 2, 3, 2,2,"Q")
        ierr, MVA2Wind = psspy.atrnreal(0, 2, 3, 2,1,"MAXMVA")
        # ierr, PCTRATE = psspy.atrnreal(0, 2, 3, 2,2,"PCTRATE")
        # ierr, MAXPCTRATE = psspy.atrnreal(0, 2, 3, 2,1,"MAXPCTRATE")
        ierr, RXAct2Wind = psspy.atrncplx(0,2,3,2,1,"RXACT")
        ierr, status = psspy.atrnint(0,2,3, 2,1, "STATUS")
        ierr, wind2ID = psspy.atrnchar(0,2, 3,2, 1,"ID")
        ierr, RateA2Wind = psspy.atrnreal(0, 2, 3, 2,1,"RATEA")
         
        # print('machineFromBusNumber: ',machineFromBusNumber)
        if len(machineFromBusNumber[0])!=0 :
            if not busNumber in machineFromBusNumber[0]:
                machineBusNumber = machineFromBusNumber

        [baseKV ,transType, sBase,R12,X12] = self.SelectAllTransType()
        [trans2Type,R,X,Rate,R01,X01] = self.SelectAllTrans2WindType()
        typeTrans2 = [[]]
        loadPercentWind2 = [[]]
        RWind2 = [[]]
        XWind2 = [[]]
        P2WindNew = [[]]
        Q2WindNew = [[]]

        type2wind = [[]]
        typeTrans2 = [[]]
        length2Wind = [[]]
        name2Wind = [[]]
        MVA2WindNew = [[]]

        for i in range(len(machineBusNumber[0])):
            # Decimal(lineRX[0][i].real).quantize(TWOPLACE))
            P2WindNew[0].append(Decimal(P2Wind[0][i+len(machineBusNumber[0])]).quantize(TWOPLACE)) # get larger value 
            Q2WindNew[0].append(Decimal(Q2Wind[0][i+len(machineBusNumber[0])]).quantize(TWOPLACE))
            MVA2WindNew[0].append(Decimal(MVA2Wind[0][i]).quantize(TWOPLACE))
            type2wind[0].append('2-Wind')

            length2Wind[0].append('-')
            name2Wind[0].append('NONE')
            if (RateA2Wind[0][i]!=0):
                loadPercentWind2[0].append(round(MVA2Wind[0][i]*100/RateA2Wind[0][i]))
            else:
                loadPercentWind2[0].append('N/A')
            RWind2[0].append(Decimal(RXAct2Wind[0][i].real).quantize(FIVEPLACE))
            XWind2[0].append(Decimal(RXAct2Wind[0][i].imag).quantize(FIVEPLACE))

            diff2 = []
            index2 = []

            for j in range(len(trans2Type)):
                if abs(RXAct2Wind[0][i].real-float(R[j])) <=0.00001 and abs(RXAct2Wind[0][i].imag-float(X[j])) <=0.001 and abs(RateA2Wind[0][i]-float(Rate[j]))<=1:
                    index2.append(j)
                    diff2.append(RXAct2Wind[0][i].imag-float(X[j]))

            if len(index2)!=0:
                index2WindType = diff2.index(min(diff2))
                typeTrans2[0].append(trans2Type[index2[index2WindType]])
            else:
                typeTrans2[0].append("NaN")

        # mảng thông tin MBA 2 cuộn dây nối tới bus tìm kiếm
        matrixWind2  = np.array([type2wind[0],typeTrans2[0],machineBusNumber[0],machineName[0],wind2ID[0],status[0],P2WindNew[0],Q2WindNew[0],loadPercentWind2[0],MVA2Wind[0],RateA2Wind[0],RWind2[0],XWind2[0],name2Wind[0]]) #,typeTrans2[0]])

        # load infor
        ierr, loadNum = psspy.alodbusint(0, 4,"NUMBER")
        ierr, loadName = psspy.alodbuschar(0, 4,"NAME")
        # 2-winding
        # ierr, winding2Num = psspy.atrnint(0, 1, 3, 2, 1, "FROMNUMBER")
        # ierr, winding2Name = psspy.atrnchar(0, 1, 3, 2, 1, "FROMNAME")
    
        # 3-winding
        # ierr, winding3Vol = psspy.atr3real(0,1, 3, 2, 1, "VMSTAR")
        ierr, winding3Num1 = psspy.atr3int(0,1, 3, 2, 1, "WIND1NUMBER")
        # ierr, cw = psspy.atr3int(0, 1,3, 2, 1, "CW")
        ierr, winding3Num2 = psspy.atr3int(0, 1,3, 2, 1, "WIND2NUMBER")
        ierr, winding3Num3 = psspy.atr3int(0, 1, 3, 2, 1, "WIND3NUMBER")
        ierr, winding3Name1 = psspy.atr3char(0, 1,3, 2, 1, "WIND1NAME")
        ierr, winding3Name2 = psspy.atr3char(0, 1,3, 2, 1, "WIND2NAME")
        ierr, winding3Name3 = psspy.atr3char(0, 1,3, 2, 1, "WIND3NAME")
        ierr, name3Wind = psspy.atr3char(0, 1,3, 2, 1, "XFRNAME")
        ierr, P3Wind = psspy.awndreal(0, 1, 3, 3,1,"P")
        ierr, Q3Wind = psspy.awndreal(0, 1, 3, 3,1,"Q")
        ierr, MVA3Wind = psspy.awndreal(0, 1, 3,3,1,"MVA")
        n = len(MVA3Wind[0])/3 # number of 3-winding transformer
        ierr, RXAct3Wind12 = psspy.atr3cplx(0,1,3,2,1,"RX1-2ACT")
        ierr, RXAct3Wind23 = psspy.atr3cplx(0,1,3,2,1,"RX2-3ACT")
        ierr, RXAct3Wind31 = psspy.atr3cplx(0,1,3,2,1,"RX3-1ACT")
        ierr, Z01Act3Wind = psspy.atr3cplx(0,1,3,2,1,"Z01")
        ierr, Z02Act3Wind = psspy.atr3cplx(0,1,3,2,1,"Z02")
        ierr, Z03Act3Wind = psspy.atr3cplx(0,1,3,2,1,"Z03")
        ierr, status3Wind = psspy.atr3int(0,1,3, 2,1, "STATUS")
        ierr, wind3ID = psspy.atr3char(0, 1, 3,2, 1,"ID")
        ierr, wind3IDbyWind = psspy.awndchar(0, 1, 3,3, 1,"ID")
        ierr, name3WindbyWind = psspy.awndchar(0, 1,3, 3, 1, "XFRNAME")
        ierr, RateA3Wind = psspy.awndreal(0, 1, 3, 3,1,"RATEA")
        # ierr, wndNum = psspy.awndint(0, 1, 3, 3,1,"WNDNUM")
        ierr, wind1Num = psspy.awndint(0, 1, 3, 3,1,"WIND1NUMBER")
        ierr, wind2Num = psspy.awndint(0, 1, 3, 3,1,"WIND2NUMBER")
        ierr, wind3Num = psspy.awndint(0, 1, 3, 3,1,"WIND3NUMBER")

        index1 = []
        index2 = []
        index3 = []
        n = len(wind3ID[0])
        for i in range(n):
            for j in range(n):
                if wind3IDbyWind[0][j] == wind3ID[0][i] and wind1Num[0][j] == winding3Num1[0][i] and wind2Num[0][j] == winding3Num2[0][i] and wind3Num[0][j] == winding3Num3[0][i]:
                    index1.append(j)
        for i in range(n):
            for j in range(n):
                if wind3IDbyWind[0][j+n] == wind3ID[0][i] and wind1Num[0][j+n] == winding3Num1[0][i] and wind2Num[0][j+n] == winding3Num2[0][i] and wind3Num[0][j+n] == winding3Num3[0][i]:
                    index2.append(j+n)
        for i in range(n):
            for j in range(n):
                if wind3IDbyWind[0][j+2*n] == wind3ID[0][i] and wind1Num[0][j+2*n] == winding3Num1[0][i] and wind2Num[0][j+2*n] == winding3Num2[0][i] and wind3Num[0][j+2*n] == winding3Num3[0][i]:
                    index3.append(j+2*n)
        indexList = index1+index2+index3

        name3WindbyWindNew = [[]]
        wind3IDbyWindNew = [[]]
        P3WindNew = [[]]
        Q3WindNew = [[]]
        MVA3WindNew = [[]]
        RateA3WindNew = [[]]
        for i in range(len(wind3IDbyWind[0])):
            
            wind3IDbyWindNew[0].append(wind3IDbyWind[0][indexList[i]])
            P3WindNew[0].append(Decimal(P3Wind[0][indexList[i]]).quantize(TWOPLACE))
            Q3WindNew[0].append(Decimal(Q3Wind[0][indexList[i]]).quantize(TWOPLACE))
            MVA3WindNew[0].append(Decimal(MVA3Wind[0][indexList[i]]).quantize(TWOPLACE))
            RateA3WindNew[0].append(Decimal(RateA3Wind[0][indexList[i]]).quantize(TWOPLACE))
            name3WindbyWindNew[0].append(name3WindbyWind[0][indexList[i]])

        MVA3WindArrange = [[]]
        P3WindArrange = [[]]
        Q3WindArrange = [[]]
        RateA3WindArrange = [[]]
        for i in range(n):
            MVA3WindArrange[0].append(MVA3WindNew[0][i])
            MVA3WindArrange[0].append(MVA3WindNew[0][i+n])
            MVA3WindArrange[0].append(MVA3WindNew[0][i+2*n])
            P3WindArrange[0].append(P3WindNew[0][i])
            P3WindArrange[0].append(P3WindNew[0][i+n])
            P3WindArrange[0].append(P3WindNew[0][i+2*n])
            Q3WindArrange[0].append(Q3WindNew[0][i])
            Q3WindArrange[0].append(Q3WindNew[0][i+n])
            Q3WindArrange[0].append(Q3WindNew[0][i+2*n])
            RateA3WindArrange[0].append(RateA3WindNew[0][i])
            RateA3WindArrange[0].append(RateA3WindNew[0][i+n])
            RateA3WindArrange[0].append(RateA3WindNew[0][i+2*n])

        wind3 = [[]]
        wind3Name = [[]]
        RWind3 = [[]]
        XWind3 = [[]]
        typeWind3 = [[]]
        wind3IDFinal = [[]]  
        status3WindFinal = [[]]
        MVA3WindFinal = [[]]
        P3WindFinal = [[]]
        Q3WindFinal = [[]]
        Rate3WindFinal = [[]]
        for i in range(len(winding3Num2[0])):
            if int(busNumber) == int(winding3Num1[0][i]):
                wind3[0].append(winding3Num2[0][i])
                typeWind3[0].append('3-Wind 1-2')
                wind3[0].append(winding3Num3[0][i])
                typeWind3[0].append('3-Wind 1-3')
                wind3Name[0].append(winding3Name2[0][i])
                wind3Name[0].append(winding3Name3[0][i])

                RWind3[0].append(Decimal(RXAct3Wind12[0][i].real).quantize(FIVEPLACE))
                XWind3[0].append(Decimal(RXAct3Wind12[0][i].imag).quantize(FIVEPLACE))
                RWind3[0].append(Decimal(RXAct3Wind31[0][i].real).quantize(FIVEPLACE))
                XWind3[0].append(Decimal(RXAct3Wind31[0][i].imag).quantize(FIVEPLACE))
                wind3IDFinal[0].append(wind3ID[0][i])
                wind3IDFinal[0].append(wind3ID[0][i])
                MVA3WindFinal[0].append(MVA3WindArrange[0][0+3*i])
                MVA3WindFinal[0].append(MVA3WindArrange[0][2+3*i])
                P3WindFinal[0].append(P3WindArrange[0][0+3*i])
                P3WindFinal[0].append(P3WindArrange[0][2+3*i])
                Q3WindFinal[0].append(Q3WindArrange[0][0+3*i])
                Q3WindFinal[0].append(Q3WindArrange[0][2+3*i])
                Rate3WindFinal[0].append(RateA3WindArrange[0][0+3*i])
                Rate3WindFinal[0].append(RateA3WindArrange[0][2+3*i])
                if (status3Wind[0][i])==1:
                    status3WindFinal[0].append(1)
                    status3WindFinal[0].append(1)
                else:
                    status3WindFinal[0].append(0)
                    status3WindFinal[0].append(0)

            elif int(busNumber) == int(winding3Num2[0][i]):
                wind3[0].append(winding3Num1[0][i])
                typeWind3[0].append('3-Wind 1-2')
                wind3[0].append(winding3Num3[0][i])
                typeWind3[0].append('3-Wind 2-3')
                wind3Name[0].append(winding3Name1[0][i])
                wind3Name[0].append(winding3Name3[0][i])
                
                RWind3[0].append(Decimal(RXAct3Wind12[0][i].real).quantize(FIVEPLACE))
                XWind3[0].append(Decimal(RXAct3Wind12[0][i].imag).quantize(FIVEPLACE))
                RWind3[0].append(Decimal(RXAct3Wind23[0][i].real).quantize(FIVEPLACE))
                XWind3[0].append(Decimal(RXAct3Wind23[0][i].imag).quantize(FIVEPLACE))
                wind3IDFinal[0].append(wind3ID[0][i])
                wind3IDFinal[0].append(wind3ID[0][i])
                MVA3WindFinal[0].append(MVA3WindArrange[0][0+3*i])
                MVA3WindFinal[0].append(MVA3WindArrange[0][1+3*i])
                P3WindFinal[0].append(P3WindArrange[0][0+3*i])
                P3WindFinal[0].append(P3WindArrange[0][1+3*i])
                Q3WindFinal[0].append(Q3WindArrange[0][0+3*i])
                Q3WindFinal[0].append(Q3WindArrange[0][1+3*i])
                Rate3WindFinal[0].append(RateA3WindArrange[0][0+3*i])
                Rate3WindFinal[0].append(RateA3WindArrange[0][1+3*i])
                if (status3Wind[0][i])==1:
                    status3WindFinal[0].append(1)
                    status3WindFinal[0].append(1)
                else:
                    status3WindFinal[0].append(0)
                    status3WindFinal[0].append(0)

            else:
                wind3[0].append(winding3Num1[0][i])
                typeWind3[0].append('3-Wind 1-3')
                wind3[0].append(winding3Num2[0][i])
                typeWind3[0].append('3-Wind 2-3')
                wind3Name[0].append(winding3Name1[0][i])
                wind3Name[0].append(winding3Name2[0][i])
                RWind3[0].append(Decimal(RXAct3Wind31[0][i].real).quantize(FIVEPLACE))
                XWind3[0].append(Decimal(RXAct3Wind31[0][i].imag).quantize(FIVEPLACE))
                RWind3[0].append(Decimal(RXAct3Wind23[0][i].real).quantize(FIVEPLACE))
                XWind3[0].append(Decimal(RXAct3Wind23[0][i].imag).quantize(FIVEPLACE))
                wind3IDFinal[0].append(wind3ID[0][i])
                wind3IDFinal[0].append(wind3ID[0][i])
                MVA3WindFinal[0].append(MVA3WindArrange[0][2+3*i])
                MVA3WindFinal[0].append(MVA3WindArrange[0][1+3*i])
                P3WindFinal[0].append(P3WindArrange[0][2+3*i])
                P3WindFinal[0].append(P3WindArrange[0][1+3*i])
                Q3WindFinal[0].append(Q3WindArrange[0][2+3*i])
                Q3WindFinal[0].append(Q3WindArrange[0][1+3*i])
                Rate3WindFinal[0].append(RateA3WindArrange[0][2+3*i])
                Rate3WindFinal[0].append(RateA3WindArrange[0][1+3*i])
                if (status3Wind[0][i])==1:
                    status3WindFinal[0].append(1)
                    status3WindFinal[0].append(1)
                else:
                    status3WindFinal[0].append(0)
                    status3WindFinal[0].append(0)

        # # fixed shunt
        # check Vbase of 3 winding
        baseKVWind3 = [[]]
        loadPercentWind3 = [[]]
        typeTrans3 = [[]]
        Z01Wind3Final = [[]]
        Z02Wind3Final = [[]]
        Z03Wind3Final = [[]]
        name3WindFinal = [[]]

        if len(wind3[0])>0:
            for i in range(len(wind3[0])):
                psspy.bsys(i+1,0,[ 1.0, 500.],0,[],1,[int(wind3[0][i])],0,[],0,[])
                ierr, busBaseKVWind3 = psspy.abusreal(i+1,2,'BASE')
                baseKVWind3[0].append(busBaseKVWind3[0][0])

                if (Rate3WindFinal[0][i]!=0):
                    loadPercentWind3[0].append(round(MVA3WindFinal[0][i]*100/Rate3WindFinal[0][i]))
                else:
                    loadPercentWind3[0].append('N/A')

        for i in range(len(winding3Num1[0])):
            Z01Wind3Final[0].append(Z01Act3Wind[0][i])
            Z01Wind3Final[0].append(Z01Act3Wind[0][i])
            Z02Wind3Final[0].append(Z02Act3Wind[0][i])
            Z02Wind3Final[0].append(Z02Act3Wind[0][i])
            Z03Wind3Final[0].append(Z03Act3Wind[0][i])
            Z03Wind3Final[0].append(Z03Act3Wind[0][i])
            name3WindFinal[0].append(name3Wind[0][i])
            name3WindFinal[0].append(name3Wind[0][i])

            psspy.bsys(i+1,0,[ 1.0, 500.],0,[],1,[int(winding3Num1[0][i])],0,[],0,[])
            ierr, busBaseKVWind3_W1 = psspy.abusreal(i+1,2,'BASE')
            index = []
            diff = []
            for j in range(len(transType)):
                if float(baseKV[j])== busBaseKVWind3_W1[0][0] and abs(RXAct3Wind12[0][i].real-float(R12[j])) <=0.0001 and abs(RXAct3Wind12[0][i].imag-float(X12[j])) <=0.001:
                    index.append(j)
                    diff.append(abs(RXAct3Wind12[0][i].imag-float(X12[j])))

            if len(index)!=0:
                index3WindType = diff.index(min(diff))
                typeTrans3[0].append(transType[index[index3WindType]])
                typeTrans3[0].append(transType[index[index3WindType]])
            else:
                typeTrans3[0].append("NaN")
                typeTrans3[0].append("NaN")

        # mảng thông tin MBA 3 cuộn dây nối tới bus tìm kiếm
        matrixWind3 = np.array([typeWind3[0],typeTrans3[0],wind3[0],wind3Name[0],wind3IDFinal[0],status3WindFinal[0],P3WindFinal[0],Q3WindFinal[0],loadPercentWind3[0], MVA3WindFinal[0],Rate3WindFinal[0],RWind3[0],XWind3[0],name3WindFinal[0],Z01Wind3Final[0],Z02Wind3Final[0],Z03Wind3Final[0]])

        return  matrixBranch.transpose(),matrixWind2.transpose(),matrixWind3.transpose()#[branchNumber[0],branchName[0], machineBusNumber[0],machineName[0],wind3[0],wind3Name[0]]

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng đường dây+MBA, hiển thị righ click tab gồm 3 chức năng: thêm, bật/tắt, xóa
    def on_cell_right_click_grid_bus( self, event ):
        menus = [(wx.NewId(), "Add New", self.addNew),
                 (wx.NewId(), "Turn On/Off", self.turnOnOff),
                 (wx.NewId(), "Delete", self.deleteBranch)]
                #  (wx.NewId(), "Line Tab", self.lineTab)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.gridBusInfo.PopupMenu(popup_menu, self.gridBusInfo.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return

    # thêm mới dz, MBA 2 CD, MBA 3 CD
    def addNew(self, event):
        if typeElement == "Line":
            self.AddNewBranch(event)
        elif typeElement == '2-Wind':
            self.AddNew2Wind(event)
        else:
            self.AddNew3Wind(event)
    
    # Thêm mới DZ
    def AddNewBranch(self,event):
        addBranchDialog = Add_New_Branch(self.parent)
        fromBusNumList = []
        fromBusNameList = []
        voltageList = []
        # print('index file is:',self.indexFile)
        for i in range(len(self.matrixBus[self.indexFile])):
            fromBusNumList.append(str(self.matrixBus[self.indexFile][i,0])+'-'+str(self.matrixBus[self.indexFile][i,1]))
            a = self.matrixBus[self.indexFile][i,2]
            if not a in voltageList: 
                voltageList.append(self.matrixBus[self.indexFile][i,2])
        
        VoltageLevel = self.parent.UdmInput.GetValue()

        # [baseKV,lineType,current,Ro,Xo] = self.SelectAllBranchType(VoltageLevel)
        [lineType] = self.SelectAllLineTypeByBusVoltage(busNumber)
    
        addBranchDialog.fromBusNum.SetItems(fromBusNumList)
        
        addBranchDialog.toBusNum.SetItems(fromBusNumList)
        addBranchDialog.comboBoxVoltageLevel.SetItems(voltageList)
        if str(busNumber) != '':
            addBranchDialog.fromBusNum.SetValue(str(busNumber))
            addBranchDialog.comboBoxVoltageLevel.SetValue(str(VoltageLevel))
        addBranchDialog.comboBoxType.SetItems(lineType.tolist())
        addBranchDialog.flagSynch = self.parent.flagSynch
        addBranchDialog.macroFile = self.parent.macroFile
        addBranchDialog.Path = self.Path
        addBranchDialog.PathFile = self.PathFile
        addBranchDialog.ShowModal()
        if not addBranchDialog.onClose(event):
            event.Skip()
        elif self.parent.flagUpdate == 1:
            self.UpdatedBranchData(event)
        elif self.parent.flagPaste == 0:
            self.parent.busNumberEnter_Fcn(event)
            self.loadBusNumberEnter(busNumber)

    # Thêm mới MBA 2 CD
    def AddNew2Wind(self,event):
        add2WindDialog = Add_New_2Wind(self.parent)
        fromBusNumList = []
        toBusNumList = []
        for i in range(len(self.matrixBus[self.indexFile])):
            fromBusNumList.append(str(self.matrixBus[self.indexFile][i,0])+'-'+str(self.matrixBus[self.indexFile][i,1]))
        for i in range(len(self.matrixMachine[self.indexFile])):
            toBusNumList.append(str(self.matrixMachine[self.indexFile][i,0])+'-'+str(self.matrixMachine[self.indexFile][i,1]))
        [trans2Type,R,X,Rate,R01,X01] = self.SelectAllTrans2WindType()
    
        add2WindDialog.fromBusNum.SetItems(fromBusNumList)
        if str(busNumber)!='':
            add2WindDialog.fromBusNum.SetValue(str(busNumber))
        add2WindDialog.toBusNum.SetItems(toBusNumList)
        add2WindDialog.comboBoxType.SetItems(trans2Type.tolist())
        add2WindDialog.flagSynch = self.parent.flagSynch
        add2WindDialog.textCtrl_ID.SetValue(str(1))
        add2WindDialog.macroFile = self.parent.macroFile
        add2WindDialog.Path = self.Path
        add2WindDialog.PathFile = self.PathFile
        add2WindDialog.ShowModal()
        if not add2WindDialog.onClose(event):
            event.Skip()
        elif self.parent.flagUpdate == 1:
            self.UpdatedBranchData(event)
        elif self.parent.flagPaste == 0:
            self.parent.busNumberEnter_Fcn(event)
            self.loadBusNumberEnter(busNumber)

    # Thêm mới MBA 3 CD
    def AddNew3Wind(self,event):
        add3WindDialog = Add_New_3Wind(self.parent)
        fromBusNumList = []
        for i in range(len(self.matrixBus[self.indexFile])):
            fromBusNumList.append(str(self.matrixBus[self.indexFile][i,0])+'-'+str(self.matrixBus[self.indexFile][i,1]))

        [baseKV ,transType, sBase,R12,X12] = self.SelectAllTransType()
    
        add3WindDialog.fromBusNum.SetItems(fromBusNumList)
        add3WindDialog.toSecondBusNum.SetItems(fromBusNumList)
        add3WindDialog.toThirdBusNum.SetItems(fromBusNumList)

        if str(busNumber) != '':
            for s in fromBusNumList:
                    if str(busNumber) == s.split('-')[0]:
                        add3WindDialog.fromBusNum.SetValue(s)
                        add3WindDialog.textCtrl_Name.SetValue(str(s.split('-')[1]))
                        break
            # add3WindDialog.fromBusNum.SetValue(str(busNumber))
            # add3WindDialog.fromBusNum.SetValue(str(busNumber))
            secondBus = ''
            thirdBus = ''
            if len(str(busNumber)) == 5:
                secondBus = '2{}'.format(busNumber)
                thirdBus ='3{}'.format(busNumber)
            # print(' secondBus and thirdBus are: ',thirdBus in fromBusNumList )
            # print(' secondBus and thirdBus are: ',fromBusNumList )
                for s in fromBusNumList:
                    if secondBus in s:
                        add3WindDialog.toSecondBusNum.SetValue(secondBus)
                        # break
                    if thirdBus in s:
                        add3WindDialog.toThirdBusNum.SetValue(thirdBus)
                        break
            elif str(busNumber)[0] == '2':
                secondBus = '1{}'.format(str(busNumber)[1:])
                thirdBus ='4{}'.format(str(busNumber)[1:])
                for s in fromBusNumList:
                    if secondBus in s:
                        add3WindDialog.toSecondBusNum.SetValue(secondBus)
                        # break
                    if thirdBus in s:
                        add3WindDialog.toThirdBusNum.SetValue(thirdBus)
                        break

        add3WindDialog.comboBoxType.SetItems(transType.tolist())
        add3WindDialog.flagSynch = self.parent.flagSynch
        add3WindDialog.macroFile = self.parent.macroFile
        add3WindDialog.Path = self.Path
        add3WindDialog.PathFile = self.PathFile
        add3WindDialog.ShowModal()
        if not add3WindDialog.onClose(event):
            event.Skip()
        elif self.parent.flagUpdate == 1:
            self.UpdatedBranchData(event)
        elif self.parent.flagPaste == 0:
            self.parent.busNumberEnter_Fcn(event)
            self.loadBusNumberEnter(busNumber)
       
    # Bật/tắt DZ, MBA 2 CD, MBA 3 CD
    def turnOnOff(self, event):

        if typeElement == 'Line':
            self.Turn_On_Off_Branch(busNumber,toBus,branchID,status)
        elif typeElement == '2-Wind':
            self.Turn_On_Off_2Wind(status,toBus,branchID,nameElement)
        elif '3-Wind' in typeElement:
            self.Turn_On_Off_3Wind(row,status,typeElement,toBus,branchID,nameElement)
        
        if self.parent.flagUpdate == 1:
            self.UpdatedBranchData(event)
        elif self.parent.flagPaste == 0:
            self.parent.busNumberEnter_Fcn(event)
            self.loadBusNumberEnter(busNumber)
    
    # Xóa DZ
    def DeleteBranch(self,fromBus=0, toBus=0,branchId=''):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.purgbrn(fromBus,toBus,branchId)
                psspy.save(path)
        else:
            psspy.purgbrn(fromBus,toBus,branchId)
            psspy.save(self.Path)
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("""psspy.purgbrn({a},{b},'{c}')\n""".format(a=int(fromBus),b=int(toBus),c=branchId))
            f.close()

    # Xóa MBA 3 CD
    def Delete3Wind(self,fromBus=0, toBus=0,branchId=''):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                self.Delete3WindFcn(fromBus,toBus,branchId)
                psspy.save(path)
        else:
            self.Delete3WindFcn(fromBus,toBus,branchId)
            psspy.save(self.Path)

    def Delete3WindFcn(self,fromBus=0, toBus=0,branchId=''):
        if "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
            psspy.purg3wnd(int(fromBus),int(toBus),int(toBusLower),branchId)
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.purg3wnd({a},{b},{c},'{d}')\n""".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId))
                f.close()
            
        elif "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
            psspy.purg3wnd(int(toBus),int(fromBus),int(toBusLower),branchId)
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.purg3wnd({a},{b},{c},'{d}')\n""".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId))
                f.close()

        elif "2-3" in typeElement and '1-3' in typeElementUpper:# busnumber is wind-3
            psspy.purg3wnd(int(toBusUpper),int(toBus),int(fromBus),branchId)
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.purg3wnd({a},{b},{c},'{d}')\n""".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchId))
                f.close()

        elif "2-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-2
            psspy.purg3wnd(int(toBusUpper),int(fromBus),int(toBus),branchId)
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.purg3wnd({a},{b},{c},'{d}')\n""".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchId))
                f.close()

        elif "1-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-1
            psspy.purg3wnd(int(fromBus),int(toBusUpper),int(toBus),branchId)
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.purg3wnd({a},{b},{c},'{d}')\n""".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchId))
                f.close()

        elif "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
            psspy.purg3wnd(int(toBus),int(toBusLower),int(fromBus),branchId)
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.purg3wnd({a},{b},{c},'{d}')\n""".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchId))
                f.close()
    
    # Bật/tắt dz
    def Turn_On_Off_Branch(self, fromBus=0, toBus=0, branchId='',status = ''):
        if str(status) == "1" :
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.branch_chng(int(fromBus),int(toBus),branchId,INTGAR1=0)
                    psspy.save(path)
            else:
                psspy.branch_chng(int(fromBus),int(toBus),branchId,INTGAR1=0)
                psspy.save(self.Path)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.branch_chng({a},{b},'{c}',INTGAR1=0)\n".format(a=int(fromBus),b=int(toBus),c=branchId))
                f.close()

        elif str(status) == "0" :
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.branch_chng(int(fromBus),int(toBus),branchId,INTGAR1=1)
                    psspy.save(path)
            else:
                psspy.branch_chng(int(fromBus),int(toBus),branchId,INTGAR1=1)
                psspy.save(self.Path)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.branch_chng({a},{b},'{c}',INTGAR1=1)\n".format(a=int(fromBus),b=int(toBus),c=branchId))
                f.close()
    
    # Bật/tắt MBA 2 CD
    def Turn_On_Off_2Wind(self,status=0, toBus=0, branchId='',nameElement = ''):
        fromBus = busNumber
        if str(status) == "1" :
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.two_winding_chng_4(int(fromBus),int(toBus),branchId,INTGAR1=0,CHARAR1=nameElement)
                    psspy.save(path)
            else:
                psspy.two_winding_chng_4(int(fromBus),int(toBus),branchId,INTGAR1=0,CHARAR1=nameElement)
                psspy.save(self.Path)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR1=0,CHARAR1={d})\n".format(a=int(fromBus),b=int(toBus),c=branchId,d=nameElement))
                f.close()

        elif str(status) == "0" :
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.two_winding_chng_4(int(fromBus),int(toBus),branchId,INTGAR1=1,CHARAR1=nameElement) 
                    psspy.save(path)
            else:
                psspy.two_winding_chng_4(int(fromBus),int(toBus),branchId,INTGAR1=1,CHARAR1=nameElement) 
                psspy.save(self.Path)
            # ghi vào file record macro
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR1=1,CHARAR1={d})\n".format(a=int(fromBus),b=int(toBus),c=branchId,d=nameElement))
                f.close()

    # Bật/tắt MBA 3 CD
    def Turn_On_Off_3Wind(self,row = 0, status = 0,typeElement ='', toBus =0, branchId ='',nameElement = ''):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                self.Turn_On_Off_3Wind_Fcn(row, status,typeElement, toBus, branchId,nameElement)
                psspy.save(path)
        else:
            self.Turn_On_Off_3Wind_Fcn(row, status,typeElement, toBus, branchId,nameElement)
            psspy.save(self.Path)

    def Turn_On_Off_3Wind_Fcn(self,row = 0, status = 0,typeElement ='', toBus =0, branchId ='',nameElement = ''):
        fromBus = busNumber
        toBusUpperNew = self.parent.gridBusInfo.GetCellValue(row-1,2)
        toBusLowerNew = self.parent.gridBusInfo.GetCellValue(row+1,2)
        typeElementUpper = self.parent.gridBusInfo.GetCellValue(row-1,0)
        typeElementLower = self.parent.gridBusInfo.GetCellValue(row+1,0)
        toBusLower = toBusLowerNew
        toBusUpper = toBusUpperNew

        if str(status) == "1" and "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
            # psspy.three_wnd_imped_chng_3(17010,217010,317010,r"""2""",[_i,_i,_i,_i,_i,_i,_i,0,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""LAICHAU5_AT2""",""])
            psspy.three_wnd_imped_chng_3(int(fromBus),int(toBus),int(toBusLower),branchId,INTGAR8=0,CHARAR1=nameElement)
            # ghi vào file record macro
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "1" and "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
            psspy.three_wnd_imped_chng_3(int(toBus),int(fromBus),int(toBusLower),branchId,INTGAR8=0,CHARAR1=nameElement)
            # ghi vào file record macro
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "1" and "2-3" in typeElement and '1-3' in typeElementUpper:# busnumber is wind-3
            psspy.three_wnd_imped_chng_3(int(toBusUpper),int(toBus),int(fromBus),branchId,INTGAR8=0,CHARAR1=nameElement)
            # ghi vào file record macro
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "1" and "2-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-2
            psspy.three_wnd_imped_chng_3(int(toBusUpper),int(fromBus),int(toBus),branchId,INTGAR8=0,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "1" and "1-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-1
            psspy.three_wnd_imped_chng_3(int(fromBus),int(toBusUpper),int(toBus),branchId,INTGAR8=0,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "1" and "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
            psspy.three_wnd_imped_chng_3(int(toBus),int(toBusLower),int(fromBus),branchId,INTGAR8=0,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchId,e=nameElement))
                f.close()

            # turn on
        elif str(status) == "0" and "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
            psspy.three_wnd_imped_chng_3(int(fromBus),int(toBus),int(toBusLower),branchId,INTGAR8=1,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "0" and "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
            psspy.three_wnd_imped_chng_3(int(toBus),int(fromBus),int(toBusLower),branchId,INTGAR8=1,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "0" and "2-3" in typeElement and '1-3' in typeElementUpper:# busnumber is wind-3
            psspy.three_wnd_imped_chng_3(int(toBusUpper),int(toBus),int(fromBus),branchId,INTGAR8=1,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "0" and "2-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-2
            psspy.three_wnd_imped_chng_3(int(toBusUpper),int(fromBus),int(toBus),branchId,INTGAR8=1,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "0" and "1-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-1
            psspy.three_wnd_imped_chng_3(int(fromBus),int(toBusUpper),int(toBus),branchId,INTGAR8=1,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchId,e=nameElement))
                f.close()

        elif str(status) == "0" and "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
            psspy.three_wnd_imped_chng_3(int(toBus),int(toBusLower),int(fromBus),branchId,INTGAR8=1,CHARAR1=nameElement)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8=0,CHARAR1='{e}')\n""".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchId,e=nameElement))
                f.close()

    # thay đổi chiều dài dây
    def changeLength(self,event,typeBr='',lenBr=0,toBus=0,branchID = ''):
        if typeBr != "NaN":
            VoltageLevel = int(float(self.parent.UdmInput.GetValue()))
            # Lấy thông số chuẩn từ CSDL
            BrachParams = self.SelectBranchInfoFromType(typeBr,int(VoltageLevel))
            baseKV = int(BrachParams[0])
            lineType = str(BrachParams[1])
            I = int(BrachParams[2])
            Ro = float(BrachParams[3])
            Xo = float(BrachParams[4])
            Bo = float(BrachParams[5])
            RoZero = float(BrachParams[6])
            XoZero = float(BrachParams[7])
            GoZero = float(BrachParams[8])
            BoZero = float(BrachParams[9])
            # tính lại thông số với chiều dài mới
            S_MVA = float(BrachParams[10]) #sqrt(3)*I*baseKV*0.001
            PBase = 100 #MVA
            Resistor_R = PBase*float(lenBr)*Ro/pow(baseKV,2)
            Reactor_X = PBase*float(lenBr)*Xo/pow(baseKV,2)
            Charging_B = pow(baseKV,2)*Bo*float(lenBr)/(PBase*1000000)
            Resistor_R_Zero = PBase*float(lenBr)*RoZero/pow(baseKV,2)
            Reactor_X_Zero = PBase*float(lenBr)*XoZero/pow(baseKV,2)
            Charging_B_Zero = pow(baseKV,2)*BoZero*float(lenBr)/(PBase*1000000)
            RateA = RateB = RateC = S_MVA
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.branch_chng(int(busNumber),int(toBus),branchID,INTGAR2=int(toBus),
                                                                REALAR1 =Resistor_R,
                                                                REALAR2 =Reactor_X,
                                                                REALAR3 =Charging_B,
                                                                REALAR4 =RateA,
                                                                REALAR5 =RateB,
                                                                REALAR6 =RateC,
                                                                REALAR11 =float(lenBr))
                    psspy.seq_branch_data_3(int(busNumber),int(toBus),branchID,0,[Resistor_R_Zero,Reactor_X_Zero,Charging_B_Zero,0.0,0.0,0.0,0.0,0.0]) # not an protected branch
                    psspy.save(path)
            else:
                psspy.branch_chng(int(busNumber),int(toBus),branchID,INTGAR2=int(toBus),
                                                                REALAR1 =Resistor_R,
                                                                REALAR2 =Reactor_X,
                                                                REALAR3 =Charging_B,
                                                                REALAR4 =RateA,
                                                                REALAR5 =RateB,
                                                                REALAR6 =RateC,
                                                                REALAR11 =float(lenBr))
                psspy.seq_branch_data_3(int(busNumber),int(toBus),branchID,0,[Resistor_R_Zero,Reactor_X_Zero,Charging_B_Zero,0.0,0.0,0.0,0.0,0.0]) # not an protected branch
                psspy.save(self.Path)
            
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
            # ghi vào file record macro
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.branch_chng({a},{b},'{c}',INTGAR2={b},REALAR1 ={d},REALAR2 ={e},REALAR3 ={f},REALAR4 ={g},REALAR5 ={h},REALAR6 ={i},REALAR11 ={j})\n".format(a=int(busNumber),b=int(toBus),c=branchID,d=Resistor_R,e=Reactor_X,f=Charging_B,g=RateA,h=RateB,i=RateC,j=float(lenBr)))
                f.writelines("psspy.seq_branch_data_3({a},{b},'{c}',0,[{k},{l},{m},0.0,0.0,0.0,0.0,0.0])\n".format(a=int(busNumber),b=int(toBus),c=branchID,k=Resistor_R_Zero,l=Reactor_X_Zero,m=Charging_B_Zero))
                f.close()
        else:
            print("Please select type for this branch first!")
            event.Skip()

    # thay đổi loại đường dây, MBA 2 CD, MBA 3 CD
    def changeType(self,newType=''):
        global typeBr
        typeBr = newType
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if typeElement == "Line":
                    self.changeTypeLine(lengthBr,typeBr,toBus,branchID)
                elif typeElement == '2-Wind':
                    self.changeType2Wind(typeBr)
                elif '3-Wind' in typeElement:
                    self.changeType3Wind(typeBr)
                psspy.save(path)
        else:
            if typeElement == "Line":
                self.changeTypeLine(lengthBr,typeBr,toBus,branchID)
            elif typeElement == '2-Wind':
                self.changeType2Wind(typeBr)
            elif '3-Wind' in typeElement:
                self.changeType3Wind(typeBr)
            psspy.save(self.Path)

    # thay đổi loại tiết diện đường dây
    def changeTypeLine(self,lenBr=0,typeBr='',toBus = 0,branchID=''):
        VoltageLevel = int(float(self.parent.UdmInput.GetValue()))
        BrachParams = self.SelectBranchInfoFromType(typeBr,int(VoltageLevel))
        baseKV = int(BrachParams[0])
        lineType = str(BrachParams[1])
        I = int(BrachParams[2])
        Ro = float(BrachParams[3])
        Xo = float(BrachParams[4])
        Bo = float(BrachParams[5])
        RoZero = float(BrachParams[6])
        XoZero = float(BrachParams[7])
        GoZero = float(BrachParams[8])
        BoZero = float(BrachParams[9])
        S_MVA = float(BrachParams[10])

        # S_MVA = sqrt(3)*I*baseKV*0.001
        PBase = 100 #MVA
        Resistor_R = PBase*float(lenBr)*Ro/pow(baseKV,2)
        Reactor_X = PBase*float(lenBr)*Xo/pow(baseKV,2)
        Charging_B = pow(baseKV,2)*Bo*float(lenBr)/(PBase*1000000)
        Resistor_R_Zero = PBase*float(lenBr)*RoZero/pow(baseKV,2)
        Reactor_X_Zero = PBase*float(lenBr)*XoZero/pow(baseKV,2)
        Charging_B_Zero = pow(baseKV,2)*BoZero*float(lenBr)/(PBase*1000000)
        RateA = RateB = RateC = S_MVA

        psspy.branch_chng(int(busNumber),int(toBus),branchID,INTGAR2=int(toBus),
                                                            REALAR1 =Resistor_R,
                                                            REALAR2 =Reactor_X,
                                                            REALAR3 =Charging_B,
                                                            REALAR4 =RateA,
                                                            REALAR5 =RateB,
                                                            REALAR6 =RateC,
                                                            REALAR11 =float(lenBr))
        psspy.seq_branch_data_3(int(busNumber),int(toBus),branchID,0,[Resistor_R_Zero,Reactor_X_Zero,Charging_B_Zero,0.0,0.0,0.0,0.0,0.0]) # not an protected branch
    
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.branch_chng({a},{b},'{c}',INTGAR2={b},REALAR1 ={d},REALAR2 ={e},REALAR3 ={f},REALAR4 ={g},REALAR5 ={h},REALAR6 ={i},REALAR11 ={j})\n".format(a=int(busNumber),b=int(toBus),c=branchID,d=Resistor_R,e=Reactor_X,f=Charging_B,g=RateA,h=RateB,i=RateC,j=float(lenBr)))
            f.writelines("psspy.seq_branch_data_3({a},{b},'{c}',0,[{k},{l},{m},0.0,0.0,0.0,0.0,0.0])\n".format(a=int(busNumber),b=int(toBus),c=branchID,k=Resistor_R_Zero,l=Reactor_X_Zero,m=Charging_B_Zero))
            f.close()

    # thay đổi loại MBA 2 CD
    def changeType2Wind(self,transType=''):
        try:
            if transType != "NaN":
                VoltageLevel = int(float(self.parent.VoltageInput.GetValue()))
                transParams = self.SelectTransInfoFromType(typeBr) #typeBr
                # baseKV,lineType,current,Ro,Xo,Bo,RoZero,XoZero,GoZero,BoZero
                transType = str(transParams[0])
                R = float(transParams[1])  
                X = float(transParams[2])
                Rate = float(transParams[3])
                R01 = float(transParams[4])
                X01 = float(transParams[5])

                psspy.two_winding_chng_4(int(busNumber),int(toBus),branchID,[int(status),1,1,0,0,0,17,0,int(busNumber),0,1,0,1,1,1],# [_i,_i,_i,_i,_i,_i,_i,_i,int(FromBusNum),_i,_i,0,_i,_i,_i],
                                                    [R,X,100.0,1.0,0.0,0.0,1.0,0.0,Rate,Rate,Rate,1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],
                                                    ["NONE",""])
                psspy.seq_two_winding_data_3(int(busNumber),int(toBus),branchID,INTGAR1=2,
                                                                            REALAR3 =R01,
                                                                            REALAR4 =X01)
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',[{d},1,1,0,0,0,17,0,{a},0,1,0,1,1,1],[{e},{f},100.0,1.0,0.0,0.0,1.0,0.0,{g},{g},{g},1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],['NONE',''])\n".format(a=int(busNumber),b=int(toBus),c=branchID,d=int(status),e=R,f=X,g=Rate))
                    f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',INTGAR1=2,REALAR3 ={h},REALAR4 ={i})\n".format(a=int(busNumber),b=int(toBus),c=branchID,h=R01,i=X01))
                    f.close()
            else:
                wx.MessageBox("Please select type for this 2-Wind first!")
        except:
            print('Error in changeType 2 wind, please check again!')

    # thay đổi loại MBA 3 CD
    def changeType3Wind(self,transType=''):
        try:
            if transType != "NaN":
                VoltageLevel = int(float(self.parent.VoltageInput.GetValue()))
                transParams = self.SelectTransInfoFromType2(typeBr)
                # baseKV,lineType,current,Ro,Xo,Bo,RoZero,XoZero,GoZero,BoZero
                transType = str(transParams[0])
                Base = float(transParams[1]) 
                R12 = float(transParams[2]) 
                X12 = float(transParams[3])
                R23 = float(transParams[4])  
                X23 = float(transParams[5])
                R31 = float(transParams[6])  
                X31 = float(transParams[7])
                PCA = float(transParams[8])
                PTA = float(transParams[9])  
                PHA = float(transParams[10])
                a = 0.5*(R12-R23+R31)
                b = 0.5*(R12+R23-R31)
                c = 0.5*(R23+R31-R12)
                d = 0.5*(X12-X23+X31)
                e = 0.5*(X12+X23-X31)
                f = 0.5*(X23+X31-X12)
         
                R01 = a
                X01 = d
                R02 = b
                X02 = e
                R03 = c
                X03 = f
            fromBus = busNumber
                                        
            if str(status) == "1" and "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
                psspy.three_wnd_imped_chng_3(int(fromBus),int(toBus),int(toBusLower),branchID,
                                                            [1,0,0,0,1,1,1,1,int(fromBus),int(fromBus),int(toBus),int(toBusLower)],
                                                            [R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],
                                                            [nameElement,''])
                psspy.seq_three_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchID,INTGAR3=2, REALAR3 =R01,REALAR4 =X01,REALAR7 =R02,REALAR8 =X02,REALAR11 =R03,REALAR12 =X03) 
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchID,1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchID,2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchID,3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
            
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',[1,0,0,0,1,1,1,1,{a},{a},{b},{c}],[{e},{f},{g},{h},{i},{j},100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],['{k}',''])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchID,e=R12,f=X12,g=R23,h=X23,i=R31,j=X31,k=nameElement))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3=2,REALAR3 ={l},REALAR4 ={m},REALAR7 ={n},REALAR8 ={o},REALAR11 ={p},REALAR12 ={q})\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchID,l=R01,m=X01,n=R02,o=X02,p=R03,q=X03))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{r},{r},{r},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchID,r=PCA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{s},{s},{s},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchID,s=PTA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{t},{t},{t},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchID,t=PHA))
                    f.close()
            
            elif str(status) == "1" and "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
                psspy.three_wnd_imped_chng_3(int(toBus),int(fromBus),int(toBusLower),branchID,
                                                            [1,0,0,0,1,1,1,1,int(toBus),int(toBus),int(fromBus),int(toBusLower)],
                                                            [R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],
                                                            [nameElement,''])
                psspy.seq_three_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchID,INTGAR3=2, REALAR3 =R01,REALAR4 =X01,REALAR7 =R02,REALAR8 =X02,REALAR11 =R03,REALAR12 =X03) 
                psspy.three_wnd_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchID,1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchID,2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchID,3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',[1,0,0,0,1,1,1,1,{a},{a},{b},{c}],[{e},{f},{g},{h},{i},{j},100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],['{k}',''])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchID,e=R12,f=X12,g=R23,h=X23,i=R31,j=X31,k=nameElement))

                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3=2,REALAR3 ={l},REALAR4 ={m},REALAR7 ={n},REALAR8 ={o},REALAR11 ={p},REALAR12 ={q})\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchID,l=R01,m=X01,n=R02,o=X02,p=R03,q=X03))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{r},{r},{r},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchID,r=PCA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{s},{s},{s},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchID,s=PTA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{t},{t},{t},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchID,t=PHA))
                    f.close()

            elif str(status) == "1" and "2-3" in typeElement and '1-3' in typeElementUpper:# busnumber is wind-3
                psspy.three_wnd_imped_chng_3(int(toBusUpper),int(toBus),int(fromBus),branchID,
                                                            [1,0,0,0,1,1,1,1,int(toBusUpper),int(toBusUpper),int(toBus),int(fromBus)],
                                                            [R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],
                                                            [nameElement,''])
                psspy.seq_three_winding_data_3(int(toBusUpper),int(toBus),int(fromBus),branchID,INTGAR3=2, REALAR3 =R01,REALAR4 =X01,REALAR7 =R02,REALAR8 =X02,REALAR11 =R03,REALAR12 =X03) 
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(toBus),int(fromBus),branchID,1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(toBus),int(fromBus),branchID,2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(toBus),int(fromBus),branchID,3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])

                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',[1,0,0,0,1,1,1,1,{a},{a},{b},{c}],[{e},{f},{g},{h},{i},{j},100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],['{k}',''])\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchID,e=R12,f=X12,g=R23,h=X23,i=R31,j=X31,k=nameElement))

                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3=2,REALAR3 ={l},REALAR4 ={m},REALAR7 ={n},REALAR8 ={o},REALAR11 ={p},REALAR12 ={q})\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchID,l=R01,m=X01,n=R02,o=X02,p=R03,q=X03))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{r},{r},{r},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchID,r=PCA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{s},{s},{s},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchID,s=PTA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{t},{t},{t},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchID,t=PHA))
                    f.close()

            elif str(status) == "1" and "2-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-2
                psspy.three_wnd_imped_chng_3(int(toBusUpper),int(fromBus),int(toBus),branchID,
                                                            [1,0,0,0,1,1,1,1,int(toBusUpper),int(toBusUpper),int(fromBus),int(toBus)],
                                                            [R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],
                                                            [nameElement,''])
                psspy.seq_three_winding_data_3(int(toBusUpper),int(fromBus),int(toBus),branchID,INTGAR3=2, REALAR3 =R01,REALAR4 =X01,REALAR7 =R02,REALAR8 =X02,REALAR11 =R03,REALAR12 =X03) 
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(fromBus),int(toBus),branchID,1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(fromBus),int(toBus),branchID,2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(fromBus),int(toBus),branchID,3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',[1,0,0,0,1,1,1,1,{a},{a},{b},{c}],[{e},{f},{g},{h},{i},{j},100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],['{k}',''])\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchID,e=R12,f=X12,g=R23,h=X23,i=R31,j=X31,k=nameElement))

                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3=2,REALAR3 ={l},REALAR4 ={m},REALAR7 ={n},REALAR8 ={o},REALAR11 ={p},REALAR12 ={q})\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchID,l=R01,m=X01,n=R02,o=X02,p=R03,q=X03))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{r},{r},{r},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchID,r=PCA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{s},{s},{s},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchID,s=PTA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{t},{t},{t},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchID,t=PHA))
                    f.close()

            elif str(status) == "1" and "1-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-1
                psspy.three_wnd_imped_chng_3(int(fromBus),int(toBusUpper),int(toBus),branchID,
                                                            [1,0,0,0,1,1,1,1,int(fromBus),int(fromBus),int(toBusUpper),int(toBus)],
                                                            [R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],
                                                            [nameElement,''])
                psspy.seq_three_winding_data_3(int(fromBus),int(toBusUpper),int(toBus),branchID,INTGAR3=2, REALAR3 =R01,REALAR4 =X01,REALAR7 =R02,REALAR8 =X02,REALAR11 =R03,REALAR12 =X03) 
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBusUpper),int(toBus),branchID,1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBusUpper),int(toBus),branchID,2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBusUpper),int(toBus),branchID,3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',[1,0,0,0,1,1,1,1,{a},{a},{b},{c}],[{e},{f},{g},{h},{i},{j},100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],['{k}',''])\n".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchID,e=R12,f=X12,g=R23,h=X23,i=R31,j=X31,k=nameElement))

                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3=2,REALAR3 ={l},REALAR4 ={m},REALAR7 ={n},REALAR8 ={o},REALAR11 ={p},REALAR12 ={q})\n".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchID,l=R01,m=X01,n=R02,o=X02,p=R03,q=X03))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{r},{r},{r},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchID,r=PCA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{s},{s},{s},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchID,s=PTA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{t},{t},{t},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchID,t=PHA))
                    f.close()

            elif str(status) == "1" and "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
                psspy.three_wnd_imped_chng_3(int(toBus),int(toBusLower),int(fromBus),branchID,
                                                            [1,0,0,0,1,1,1,1,int(toBus),int(toBus),int(toBusLower),int(fromBus)],
                                                            [R12,X12,R23,X23,R31,X31,100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],
                                                            [nameElement,''])
                psspy.seq_three_winding_data_3(int(toBus),int(toBusLower),int(fromBus),branchID,INTGAR3=2, REALAR3 =R01,REALAR4 =X01,REALAR7 =R02,REALAR8 =X02,REALAR11 =R03,REALAR12 =X03) 
                psspy.three_wnd_winding_data_3(int(toBus),int(toBusLower),int(fromBus),branchID,1,[17,0,0,1,0],[1.0,0.0,0.0,PCA,PCA,PCA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBus),int(toBusLower),int(fromBus),branchID,2,[17,0,0,1,0],[1.0,0.0,0.0,PTA,PTA,PTA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBus),int(toBusLower),int(fromBus),branchID,3,[17,0,0,1,0],[1.0,0.0,0.0,PHA,PHA,PHA,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',[1,0,0,0,1,1,1,1,{a},{a},{b},{c}],[{e},{f},{g},{h},{i},{j},100.0,100.0,100.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0],['{k}',''])\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchID,e=R12,f=X12,g=R23,h=X23,i=R31,j=X31,k=nameElement))

                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3=2,REALAR3 ={l},REALAR4 ={m},REALAR7 ={n},REALAR8 ={o},REALAR11 ={p},REALAR12 ={q})\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchID,l=R01,m=X01,n=R02,o=X02,p=R03,q=X03))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{r},{r},{r},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchID,r=PCA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{s},{s},{s},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchID,s=PTA))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{t},{t},{t},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchID,t=PHA))
                    f.close()

            else:
                wx.MessageBox("Please select type for this 3-Wind first!")
        except:
            print('Error in changeType 3 wind, please check again!')
    
    # thay đổi tên MBA 3 CD
    def changeName3Wind(self,cellNewVal=''):
        fromBus = busNumber
        if str(status) == "1" and "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
            psspy.three_wnd_imped_chng_3(int(fromBus),int(toBus),int(toBusLower),branchID,CHARAR1 = cellNewVal)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""
                psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 = '{e}')\n
                """.format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchID,e=cellNewVal))
                f.close()

        elif str(status) == "1" and "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
            psspy.three_wnd_imped_chng_3(int(toBus),int(fromBus),int(toBusLower),branchID,CHARAR1 = cellNewVal)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""
                psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 = '{e}')\n
                """.format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchID,e=cellNewVal))
                f.close()

        elif str(status) == "1" and "2-3" in typeElement and '1-3' in typeElementUpper:# busnumber is wind-3
            psspy.three_wnd_imped_chng_3(int(toBusUpper),int(toBus),int(fromBus),branchID,CHARAR1 = cellNewVal)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""
                psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 = '{e}')\n
                """.format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchID,e=cellNewVal))
                f.close()

        elif str(status) == "1" and "2-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-2
            psspy.three_wnd_imped_chng_3(int(toBusUpper),int(fromBus),int(toBus),branchID,CHARAR1 = cellNewVal)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""
                psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 = '{e}')\n
                """.format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchID,e=cellNewVal))
                f.close()

        elif str(status) == "1" and "1-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-1
            psspy.three_wnd_imped_chng_3(int(fromBus),int(toBusUpper),int(toBus),branchID,CHARAR1 = cellNewVal)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""
                psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 = '{e}')\n
                """.format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchID,e=cellNewVal))
                f.close()

        elif str(status) == "1" and "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
            psspy.three_wnd_imped_chng_3(int(toBus),int(toBusLower),int(fromBus),branchID, CHARAR1 = cellNewVal)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""
                psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 ='{e}')\n
                """.format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchID,e=cellNewVal))
                f.close()              
        else:
            print("Please select type for this branch first!")

    # thay đổi ID MBA 3 CD
    def changeID3Wind(self,row=0, branchId ='',newBranchID = ''):
        fromBus = busNumber
        toBusUpperNew = self.parent.gridBusInfo.GetCellValue(row-1,2)
        toBusLowerNew = self.parent.gridBusInfo.GetCellValue(row+1,2)
        toBus = self.parent.gridBusInfo.GetCellValue(row,2)
        typeElementUpper = self.parent.gridBusInfo.GetCellValue(row-1,0)
        typeElementLower = self.parent.gridBusInfo.GetCellValue(row+1,0)
        typeElement = self.parent.gridBusInfo.GetCellValue(row,0)

        toBusLower = toBusLowerNew
        toBusUpper = toBusUpperNew

        if "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
            psspy.mbid3wnd(int(fromBus),int(toBus),int(toBusLower),branchId,newBranchID)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=newBranchID))
                f.close()

        elif "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
            psspy.mbid3wnd(int(toBus),int(fromBus),int(toBusLower),branchId,newBranchID)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId,e=newBranchID))
                f.close()

        elif "2-3" in typeElement and '1-3' in typeElementUpper:# busnumber is wind-3
            psspy.mbid3wnd(int(toBusUpper),int(toBus),int(fromBus),branchId,newBranchID)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchId,e=newBranchID))
                f.close()

        elif "2-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-2
            psspy.mbid3wnd(int(toBusUpper),int(fromBus),int(toBus),branchId,newBranchID)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchId,e=newBranchID))
                f.close()

        elif "1-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-1
            psspy.mbid3wnd(int(fromBus),int(toBusUpper),int(toBus),branchId,newBranchID)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=int(fromBus),b=int(toBusUpper),c=int(toBus),d=branchId,e=newBranchID))
                f.close()

        elif "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
            psspy.mbid3wnd(int(toBus),int(toBusLower),int(fromBus),branchId,newBranchID)
            
            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchId,e=newBranchID))
                f.close()
    
    # thay đổi ID của DZ và MBA 2 CD tương tự nhau, MBA 3 CD
    def changeID(self,row=0,typeElement='',toBus=0,oldID='',newID=''):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if typeElement == "Line" or typeElement == '2-Wind':
                    psspy.mbidbrn(int(busNumber),int(toBus),str(oldID),str(newID))
                elif '3-Wind' in typeElement:
                    self.changeID3Wind(row,str(oldID),str(newID))
                psspy.save(path)
        else:
            if typeElement == "Line" or typeElement == '2-Wind':
                psspy.mbidbrn(int(busNumber),int(toBus),str(oldID),str(newID))
            elif '3-Wind' in typeElement:
                self.changeID3Wind(row,str(oldID),str(newID))
            psspy.save(self.Path)

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            if typeElement == "Line" or typeElement == '2-Wind':
                f.writelines("""psspy.mbidbrn({a},{b},'{c}','{d}')\n""".format(a=int(busNumber),b=int(toBus),c=str(oldID),d=str(newID)))
            f.close()

    # thay đổi định mức MBA 3 CD
    def changeRate3Wind(self, row=0,branchId='',rate=0.0):
        fromBus = busNumber
        toBusLowerNew = self.parent.gridBusInfo.GetCellValue(row+1,2)
        toBus = self.parent.gridBusInfo.GetCellValue(row,2)
        typeElementLower = self.parent.gridBusInfo.GetCellValue(row+1,0)
        typeElement = self.parent.gridBusInfo.GetCellValue(row,0)
        toBusLower = toBusLowerNew
        
        if row != 0:
            toBusUpperNew = self.parent.gridBusInfo.GetCellValue(row-1,2)
            typeElementUpper = self.parent.gridBusInfo.GetCellValue(row-1,0)
            toBusUpper = toBusUpperNew

            if "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchId,1,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchId,2,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=rate))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=rate))
                    f.close()

            elif "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
                psspy.three_wnd_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchId,1,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchId,2,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])

                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId,e=rate))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId,e=rate))
                    f.close()

            elif "2-3" in typeElement and '1-3' in typeElementUpper:# busnumber is wind-3
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(toBus),int(fromBus),branchId,1,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(toBus),int(fromBus),branchId,2,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])

                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchId,e=rate))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(toBus),c=int(fromBus),d=branchId,e=rate))
                    f.close()

            elif "2-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-2
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(fromBus),int(toBus),branchId,1,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBusUpper),int(fromBus),int(toBus),branchId,2,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchId,e=rate))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBusUpper),b=int(fromBus),c=int(toBus),d=branchId,e=rate))
                    f.close()

            elif "1-3" in typeElement and '1-2' in typeElementUpper:# busnumber is wind-1
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBusUpper),int(toBus),branchId,3,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=rate))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=rate))
                    f.close()

            elif "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
                psspy.three_wnd_winding_data_3(int(toBus),int(toBusLower),int(fromBus),branchId,3,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
        
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchId,e=rate))
                    f.close()
        
        else:
            if "1-2" in typeElement and '1-3' in typeElementLower: # busnumber is wind-1
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchId,1,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(fromBus),int(toBus),int(toBusLower),branchId,2,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                
                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=rate))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(fromBus),b=int(toBus),c=int(toBusLower),d=branchId,e=rate))
                    f.close()

            elif "1-2" in typeElement and '2-3' in typeElementLower:# busnumber is wind-2
                psspy.three_wnd_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchId,1,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])
                psspy.three_wnd_winding_data_3(int(toBus),int(fromBus),int(toBusLower),branchId,2,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])

                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId,e=rate))
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(fromBus),c=int(toBusLower),d=branchId,e=rate))
                    f.close()

            elif "1-3" in typeElement and '2-3' in typeElementLower:# busnumber is wind-3
                psspy.three_wnd_winding_data_3(int(toBus),int(toBusLower),int(fromBus),branchId,3,[17,0,0,1,0],[1.0,0.0,0.0,rate,rate,rate,1.1,0.9,1.1,0.9,0.0,0.0,0.0])

                if self.parent.macroFile != '':
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,[17,0,0,1,0],[1.0,0.0,0.0,{e},{e},{e},1.1,0.9,1.1,0.9,0.0,0.0,0.0])\n".format(a=int(toBus),b=int(toBusLower),c=int(fromBus),d=branchId,e=rate))
                    f.close()
    
    # thay đổi định mức của DZ, MBA 2 CD, MBA 3 CD
    def changeRate(self,row=0,typeElement='',toBus=0,branchID='',rate=''):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if typeElement == "Line":
                    # psspy.branch_chng(17012,19010,r"""1""",[_i,_i,_i,_i,_i,_i],[_f,_f,_f, 2000.0,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
                    psspy.branch_chng(int(busNumber),int(toBus),str(branchID),REALAR4=float(rate),REALAR5=float(rate),REALAR6=float(rate))
                elif typeElement == '2-Wind':
                    R = self.parent.gridBusInfo.GetCellValue(row,11)
                    X = self.parent.gridBusInfo.GetCellValue(row,12)
                    # psspy.two_winding_chng_4(19030,919051,r"""2""",[_i,_i,_i,_i,_i,_i,_i,_i,19030,_i,_i,0,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f, 333.0,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[r"""NONE""",""])
                    psspy.two_winding_chng_4(int(busNumber),int(toBus),str(branchID),[int(status),1,1,0,0,0,17,0,int(busNumber),0,1,0,1,1,1],# [_i,_i,_i,_i,_i,_i,_i,_i,int(FromBusNum),_i,_i,0,_i,_i,_i],
                                            [float(R),float(X),100.0,1.0,0.0,0.0,1.0,0.0,float(rate),float(rate),float(rate),1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],
                                            ["NONE",""])

                elif '3-Wind' in typeElement:
                    self.changeRate3Wind(row,str(branchID),float(rate))
                psspy.save(path)
        else:
            if typeElement == "Line":
                psspy.branch_chng(int(busNumber),int(toBus),str(branchID),REALAR4=float(rate),REALAR5=float(rate),REALAR6=float(rate))
            elif typeElement == '2-Wind':
                R = self.parent.gridBusInfo.GetCellValue(row,11)
                X = self.parent.gridBusInfo.GetCellValue(row,12)
                psspy.two_winding_chng_4(int(busNumber),int(toBus),str(branchID),[int(status),1,1,0,0,0,17,0,int(busNumber),0,1,0,1,1,1],# [_i,_i,_i,_i,_i,_i,_i,_i,int(FromBusNum),_i,_i,0,_i,_i,_i],
                                        [float(R),float(X),100.0,1.0,0.0,0.0,1.0,0.0,float(rate),float(rate),float(rate),1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],
                                        ["NONE",""])
            elif '3-Wind' in typeElement:
                self.changeRate3Wind(row,str(branchID),float(rate))
            psspy.save(self.Path)

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            if typeElement == "Line":
                f.writelines("psspy.branch_chng({a},{b},'{c}',REALAR4={d},REALAR5={d},REALAR6={d})\n".format(a=int(busNumber),b=int(toBus),c=str(branchID),d=float(rate)))
            elif typeElement == '2-Wind':
                R = self.parent.gridBusInfo.GetCellValue(row,11)
                X = self.parent.gridBusInfo.GetCellValue(row,12)
                f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',[{d},1,1,0,0,0,17,0,{a},0,1,0,1,1,1],[{e},{f},100.0,1.0,0.0,0.0,1.0,0.0,{g},{g},{g},1.0,1.0,1.0,1.0,0.0,0.0,1.1,0.9,1.1,0.9,0.0,0.0,0.0],['NONE',''])\n".format(a=int(busNumber),b=int(toBus),c=str(branchID),d=int(status),e=float(R),f=float(X),g=float(rate)))
            f.close()

    # xóa DZ
    def deleteBranch(self, event):
        fromBus = busNumber
        if typeElement == 'Line' or typeElement == '2-Wind':
            self.DeleteBranch(int(fromBus),int(toBus),branchID)
        else:
            self.Delete3Wind(int(fromBus),int(toBus),branchID)
        
        if self.parent.flagUpdate == 1:
            self.UpdatedBranchData(event)
        else:
            self.parent.busNumberEnter_Fcn(event)
            self.loadBusNumberEnter(busNumber)
    
    # chức năng thực hiện tại ô được chọn của bảng đường dây + MBA
    def on_selected_cell_grid_bus( self, event ):
        try:
            global row,col,cellValue,status,toBus,toBusUpper,toBusLower,branchID,typeBr,lengthBr,typeElement,typeElementLower,typeElementUpper,nameElement
            global cellVal,statusUpper,branchIDUpper,typeBrUpper,lengthBrUpper,rate,rateUpper, nameElementUpper,toBusUpUpper,typeElement
            row = event.GetRow()
            col = event.GetCol()

            cellValue = self.parent.gridBusInfo.GetCellValue(row,col)
            status = self.parent.gridBusInfo.GetCellValue(row,5) #12
            toBus = self.parent.gridBusInfo.GetCellValue(row,2)
            typeElement = self.parent.gridBusInfo.GetCellValue(row,0)
            if row != 0:
                toBusUpper = self.parent.gridBusInfo.GetCellValue(row-1,2)
                toBusLower = self.parent.gridBusInfo.GetCellValue(row+1,2)
                typeElementUpper = self.parent.gridBusInfo.GetCellValue(row-1,0)
                typeElementLower = self.parent.gridBusInfo.GetCellValue(row+1,0)
                cellVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
                statusUpper = self.parent.gridBusInfo.GetCellValue(row-1,5) #12
                branchIDUpper = self.parent.gridBusInfo.GetCellValue(row-1,4)
                typeBrUpper = self.parent.gridBusInfo.GetCellValue(row-1,1)
                lengthBrUpper = self.parent.gridBusInfo.GetCellValue(row-1,9)
                rateUpper = self.parent.gridBusInfo.GetCellValue(row-1,10)
                nameElementUpper = self.parent.gridBusInfo.GetCellValue(row-1,13)
                
            if row !=1 and row!=0:
                toBusUpUpper = self.parent.gridBusInfo.GetCellValue(row-2,2)

            rate = self.parent.gridBusInfo.GetCellValue(row,10)
            toBus = self.parent.gridBusInfo.GetCellValue(row,2)
            branchID = self.parent.gridBusInfo.GetCellValue(row,4)
            typeBr = self.parent.gridBusInfo.GetCellValue(row,1)
            lengthBr = self.parent.gridBusInfo.GetCellValue(row,9)
            typeElement = self.parent.gridBusInfo.GetCellValue(row,0)
            nameElement = self.parent.gridBusInfo.GetCellValue(row,13)
        except:
            print('Error in on_selected_cell_grid_bus, please check again!') 

    # thay đổi R của DZ
    def changeR(self,toBus,branchID,newR):
        fromBus = busNumber
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.branch_chng(fromBus,toBus,branchID,REALAR1= newR)
                psspy.save(path)
        else:
            psspy.branch_chng(fromBus,toBus,branchID,REALAR1= newR)
            psspy.save(self.Path)
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.branch_chng({a},{b},'{c}',REALAR1={d})\n".format(a=int(fromBus),b=int(toBus),c=str(branchID),d=float(newR)))
            f.close()

    # thay đổi X của DZ
    def changeX(self,toBus,branchID,newX):
        fromBus = busNumber
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.branch_chng(fromBus,toBus,branchID,REALAR2= newX)
                psspy.save(path)
        else:
            psspy.branch_chng(fromBus,toBus,branchID,REALAR2= newX)
            psspy.save(self.Path)
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.branch_chng({a},{b},'{c}',REALAR2={d})\n".format(a=int(fromBus),b=int(toBus),c=str(branchID),d=float(newX)))
            f.close()

    # thay đổi charging B của DZ
    def changeChargingB(self,toBus,branchID,newX):
        fromBus = busNumber
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.branch_chng(fromBus,toBus,branchID,REALAR3= newX)
                psspy.save(path)
        else:
            psspy.branch_chng(fromBus,toBus,branchID,REALAR3= newX)
            psspy.save(self.Path)
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.branch_chng({a},{b},'{c}',REALAR3={d})\n".format(a=int(fromBus),b=int(toBus),c=str(branchID),d=float(newX)))
            f.close()

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng đường dây+MBA
    def on_cell_change_grid_bus( self, event ):

        cellNewVal = self.parent.gridBusInfo.GetCellValue(row,col)

        if col ==5 and self.uk == 13: #col==12 or 
            if typeElementUpper == 'Line':
                self.Turn_On_Off_Branch(busNumber,toBusUpper,branchIDUpper,statusUpper)
                if self.parent.flagUpdate == 1:
                    self.UpdatedBranchData(event)
                elif self.parent.flagPaste == 0:
                    self.parent.busNumberEnter_Fcn(event)
                    self.loadBusNumberEnter(busNumber)
            elif typeElementUpper == '2-Wind':
                self.Turn_On_Off_2Wind(statusUpper,toBusUpper,branchIDUpper,nameElementUpper)
                if self.parent.flagUpdate == 1:
                    self.UpdatedBranchData(event)
                elif self.parent.flagPaste == 0:
                    self.parent.busNumberEnter_Fcn(event)
                    self.loadBusNumberEnter(busNumber)
            elif '3-Wind' in typeElementUpper:
                celVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
                self.Turn_On_Off_3Wind(row-1, int(statusUpper),typeElementUpper,toBusUpper,branchIDUpper,nameElementUpper)
                if self.parent.flagUpdate == 1:
                    self.UpdatedBranchData(event)
                elif self.parent.flagPaste == 0:
                    self.parent.busNumberEnter_Fcn(event)
                    self.loadBusNumberEnter(busNumber)
        elif col == 5:
            self.turnOnOff(event)
        elif col == 1: # change type
            self.changeType(cellNewVal)
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 4 and self.uk ==13: # change ID with Enter
            cellVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
            self.changeID(row-1,typeElementUpper,toBusUpper,branchIDUpper,cellVal)
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 4: # change ID without Enter
            self.changeID(row,typeElement,toBus,cellValue,cellNewVal)
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 9 and typeElementUpper == 'Line' and self.uk ==13:
            cellVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
            self.changeLength(event,typeBrUpper,float(cellVal),toBusUpper,branchIDUpper)
        elif col == 9 and typeElement == 'Line'  and self.uk !=13 :
            self.changeLength(event,typeBr,float(cellNewVal),toBus,branchID)
        elif col == 10 and self.uk ==13: # change Rate with Enter
            cellVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
            self.changeRate(row-1,typeElementUpper,toBusUpper,branchIDUpper,cellVal)
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 10: # change Rate without Enter
            self.changeRate(row,typeElement,toBus,branchID,cellNewVal)
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 11 and typeElement == 'Line' and  self.uk ==13: # change branch R with Enter
            cellVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
            self.changeR(int(toBusUpper),str(branchIDUpper),float(cellVal))
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 11 and typeElement == 'Line': # change branch R
            self.changeR(int(toBus),str(branchID),float(cellNewVal))
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 12 and typeElement == 'Line' and self.uk ==13: # change branch X with Enter
            cellVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
            self.changeX(int(toBusUpper),str(branchIDUpper),float(cellVal))
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 12 and typeElement == 'Line': # change branch X
            self.changeX(int(toBus),str(branchID),float(cellNewVal))
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 13 and typeElement == 'Line' and self.uk ==13: # change branch ChargingB with Enter
            cellVal = self.parent.gridBusInfo.GetCellValue(row-1,col)
            self.changeChargingB(int(toBusUpper),str(branchIDUpper),float(cellVal))
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 13 and typeElement == 'Line': # change branch X
            self.changeChargingB(int(toBus),str(branchID),float(cellNewVal))
            if self.parent.flagUpdate == 1:
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0:
                self.parent.busNumberEnter_Fcn(event)
                self.loadBusNumberEnter(busNumber)
        elif col == 13 and '3-Wind' in typeElement:
            self.changeName3Wind(cellNewVal)
            if self.parent.flagUpdate == 1: # cập nhật từng bước
                self.UpdatedBranchData(event)
            elif self.parent.flagPaste == 0: # cập nhật sau và  ô cuối cùng trong vùng paste 
                #sẽ thực hiện cập nhật, các ô trung gian bỏ qua
                self.loadBusNumberEnter(busNumber)

    # Update all
    def Reload_Fcn( self, event ):
        try:
            self.parent.busNumberEnter_Fcn(event)
            self.loadBusNumberEnter(busNumber)
            self.UpdatedBranchData(event)
            event.Skip()
        except:
            print('Error in reload_fcn, please check again!')
            event.Skip()

    # cập nhật thông tin bảng đường dây, MBA
    def UpdatedBranchData(self,event):
        # cập nhật đồng thời nhiều file
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                self.onUpdateBranch(event,i,path)
            self.parent.busNumberEnter_Fcn(event)
        # chỉ cập nhật cho file đang làm việc
        else:
            self.onUpdateBranch(event,self.indexFile,self.Path)
            self.parent.busNumberEnter_Fcn(event)

    # tính TLCS, cập nhật lại TLCS ở bảng thông tin file khi chọn chức năng cập nhật từng bước (flagUpdate == 1) hoặc chọn reload (flagReload == 1)
    def onUpdateBranch(self, event,indexfile,path ):
        self.indexFile = indexfile
        self.Path = path
        if self.parent.flagUpdate == 1 or self.parent.flagReload == 1:
            self.parent.Power_Flow_Selected_Cal_Fcn_ALL(event,path)
            fileInfo = loadFileInfo(self.Path)
            fileInfo1 = [fileInfo[0][0],fileInfo[1][0],fileInfo[2][0],fileInfo[3][0],fileInfo[4][0],fileInfo[5][0]]
            fileInfoArray = np.array(fileInfo1)
            fileInfoTranspose = fileInfoArray.transpose()
        for row in range(len(fileInfoTranspose)):
                for column in range(len(fileInfoTranspose[0])):
                    self.myGridFile.SetCellValue(row,column,str(fileInfoTranspose[row][column]))
