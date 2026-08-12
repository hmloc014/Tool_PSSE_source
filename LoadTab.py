# -*- coding: utf-8 -*-
import psspy
import numpy as np
import wx
import os
from decimal import *
from math import *
import copy
import csv
from ui_performance import profiled

fileNumber = 0
fileName = [[]]
PCanbang = [[]]
QCanbang = [[]]
plossVal = [[]]
misMatchVal = [[]]
PATH = ''
busCode = [[]]
busCosPhi = [[]]
busZoneName = [[]]
busAreaName = [[]]
busOwnerName = [[]]
negativeZ = [[]]
groundingZ = [[]]
zeroZ = [[]]
zeroR = [[]]
zeroX = [[]]
areaNum = [[]]
areaNumber = [[]]
areaName = [[]]
zoneNum = [[]]
zoneNumber = [[]]
zoneName = [[]]
areaCount = 0
zoneCount = 0
code = [[]]
ivalNew = [[]]
SIXPLACE = Decimal(10)**-6
FIVEPLACE = Decimal(10)**-5
FOURPLACE = Decimal(10)**-4
THREEPLACE = Decimal(10)**-3
TWOPLACE = Decimal(10)**-2
ONEPLACE = Decimal(10)**-1


def array2dict(dict_keys, dict_values):
    '''Convert array to dictionary of arrays.
    Returns dictionary as {dict_keys:dict_values}
    '''
    tmpdict = {}
    for i in range(len(dict_keys)):
        tmpdict[dict_keys[i].lower()] = dict_values[i]
    return tmpdict

# loại bỏ thông tin tương ứng tại vị trí indexfile trong mảng
def delFileInfo(indexFile = 0):
    fileName[0].pop(indexFile)
    PCanbang[0].pop(indexFile)
    QCanbang[0].pop(indexFile)
    misMatchVal[0].pop(indexFile)
    plossVal[0].pop(indexFile)
    ivalNew[0].pop(indexFile)

# lấy thông tin hiển thị trong bảng file information
def loadFileInfo(path=''):
    global fileNumber,PCanbang,QCanbang, misMatchVal,plossVal#, fileName
    PATH = path
    if PATH != '':
        nameFile = os.path.basename(PATH)
        istringsArea = ['pload','qload','pgen','qgen','ploss','qloss']
        ierr, PQLossByArea = psspy.aareareal(-1,2,istringsArea) 
        ierr, PQLossByZone = psspy.azonereal(-1,2,istringsArea) 
        ierr, misMatch = psspy.abuscplx(-1, 2, 'mismatch')
        ierr, busesNumber = psspy.abuscount(-1,2)
        ierr, machineNum = psspy.amachcount(-1, 4)
        ierr, machineBusNumber = psspy.amachint (-1,4,'NUMBER')
        ierr, pgen_val = psspy.amachreal (-1,4,'PGEN')
        ierr, qgen_val = psspy.amachreal (-1,4,'QGEN')
        misMatchAbs = []
        ival = psspy.iterat()
        # ivalNew[0].append(ival)


        for i in range(busesNumber):
            misMatchAbs.append(abs(misMatch[0][i]))

        if nameFile in fileName[0]:
            # wx.MessageBox("Replace the same name file")
            index = fileName[0].index(nameFile)
            ivalNew[0][index] = ival
            for i in range(machineNum):
                if machineBusNumber[0][i] ==923011: #bus Hoa Binh , if machineBusNumber[0][i] in swingBus:
                    PCanbang[0][index] = Decimal(pgen_val[0][i]).quantize(TWOPLACE)
                    QCanbang[0][index] = Decimal(qgen_val[0][i]).quantize(TWOPLACE)
                    misMatchVal[0][index] =  Decimal(sum(misMatchAbs)).quantize(TWOPLACE)
                    plossVal[0][index] =  Decimal(sum(PQLossByArea[4])).quantize(TWOPLACE)
                   
        else:
            fileName[0].append(nameFile)
            for i in range(machineNum):
                if machineBusNumber[0][i] == 923011: #bus Hoa Binh , if machineBusNumber[0][i] in swingBus:
                    PCanbang[0].append(Decimal(pgen_val[0][i]).quantize(TWOPLACE))  
                    QCanbang[0].append(Decimal(qgen_val[0][i]).quantize(TWOPLACE))
            ivalNew[0].append(ival)
            misMatchVal[0].append(Decimal(sum(misMatchAbs)).quantize(TWOPLACE))
            plossVal[0].append(Decimal(sum(PQLossByArea[4])).quantize(TWOPLACE))
            
        result = [fileName,PCanbang,QCanbang,misMatchVal,plossVal,ivalNew]
        return result
    else:
        wx.MessageBox("Please open an existing case first!")

# lấy thông tin hiển thị trong bảng area
def loadAreaInfo(path=''):
    PATH = path
    global areaNumber, areaName,areaCount
    if PATH != '':
        istringsArea = ['ploadld','qloadld','pgen','qgen','ploss','qloss']
        ierr, areaCount = psspy.aareacount(-1,2)
        ierr, PQLossByArea = psspy.aareareal(-1,2,istringsArea)
        ierr, areaNumber = psspy.aareaint(-1,2,'NUMBER')
        ierr, areaName = psspy.aareachar(-1,2,'AREANAME')
        
        ierr, busID = psspy.abusint(-1,2,'NUMBER')
        ierr, busTypeCode = psspy.abusint(-1,2,'TYPE')
        ierr, busAreaNum = psspy.abusint(-1,2,'AREA')
        
        swingBus = []
        swingArea = []
        pGenSwing = []

        for i,code in enumerate(busTypeCode[0]):
            if code == 3:
                psspy.bsys(1,0,[ 1.0, 500.0],0,[],1,[busID[0][i]],0,[],0,[])
                
                ierr, pgen = psspy.amachreal (1,1,'PGEN')
                swingBus.append(busID[0][i])

                if pgen[0][0]<0:
                    if not busAreaNum[0][i] in swingArea:
                        swingArea.append(busAreaNum[0][i])
                        pGenSwing.append(pgen[0][0])
                    else:
                        pGenSwing[len(pGenSwing)-1] = pGenSwing[len(pGenSwing)-1]+pgen[0][0]


        ploadArr = PQLossByArea[0][:]
        qloadArr = PQLossByArea[1][:]
        pgenArr = PQLossByArea[2][:]
        qgenArr = PQLossByArea[3][:]
        plossArr = PQLossByArea[4][:]
        qlossArr = PQLossByArea[5][:]
        cosPhi = []

        for i in range(areaCount):
            if(pgenArr[i]*qgenArr[i]!=0):
                cosPhiVal = pgenArr[i]/ sqrt(pow(pgenArr[i],2)+pow(qgenArr[i],2))
                cosPhi.append(Decimal(cosPhiVal).quantize(TWOPLACE))
            else:
                cosPhi.append(0)
            ploadArr[i] = Decimal(ploadArr[i]).quantize(TWOPLACE)
            qloadArr[i] = Decimal(qloadArr[i]).quantize(TWOPLACE)
            if areaNumber[0][i] in swingArea:
                index = swingArea.index(areaNumber[0][i])
                pgenArr[i] = Decimal(pgenArr[i]-pGenSwing[index]).quantize(TWOPLACE)
            else:
                pgenArr[i] = Decimal(pgenArr[i]).quantize(TWOPLACE)
            qgenArr[i] = Decimal(qgenArr[i]).quantize(TWOPLACE)

        matrixArea = np.array([areaNumber[0],areaName[0],pgenArr,qgenArr,ploadArr,qloadArr,cosPhi])
        matrixArea = matrixArea.transpose()

        return matrixArea
    else:
        wx.MessageBox("Please open an existing case first!")  

# lấy thông tin hiển thị trong bảng zone
def loadZoneInfo(path=''):
    global zoneName, zoneNumber,zoneCount
    PATH = path
    if PATH != '':
        istringsZone = ['ploadld','qloadld','pgen','qgen','ploss','qloss']
        ierr, zoneCount = psspy.azonecount(-1,2)
        ierr, PQLossByZone = psspy.azonereal(-1,2,istringsZone)
        ierr, zoneNumber = psspy.azoneint(-1,2,'NUMBER')
        ierr, zoneName = psspy.azonechar(-1,2,'ZONENAME')

        ploadArr = PQLossByZone[0][:]
        qloadArr = PQLossByZone[1][:]
        pgenArr = PQLossByZone[2][:]
        qgenArr = PQLossByZone[3][:]
        plossArr = PQLossByZone[4][:]
        qlossArr = PQLossByZone[5][:]
        cosPhi = []

        for i in range(zoneCount):
            if(pgenArr[i]*qgenArr[i]!=0):
                cosPhiVal = pgenArr[i]/ sqrt(pow(pgenArr[i],2)+pow(qgenArr[i],2))
                cosPhi.append(Decimal(cosPhiVal).quantize(TWOPLACE))
            else:
                cosPhi.append(0)
            ploadArr[i] = Decimal(ploadArr[i]).quantize(TWOPLACE)
            qloadArr[i] = Decimal(qloadArr[i]).quantize(TWOPLACE)
            pgenArr[i] = Decimal(pgenArr[i]).quantize(TWOPLACE)
            qgenArr[i] = Decimal(qgenArr[i]).quantize(TWOPLACE)

        matrixZone = np.array([zoneNumber[0],zoneName[0],pgenArr,qgenArr,ploadArr,qloadArr,cosPhi])
        matrixZone = matrixZone.transpose()
        return matrixZone
    else:
        wx.MessageBox("Please open an existing case first!") 

# lấy thông tin hiển thị trong bảng bus
@profiled('psse.extract.bus')
def loadBusTab(path=''):
    PATH = path
    if PATH != '':
        # bus count
        ierr, busesNumber = psspy.abuscount(-1,2) #abuscount(-1,2)
        # Bus tab information
        # All Bus
        ierr, busID = psspy.abusint(-1,2,'NUMBER')
        # Bus in-service
        ierr, busIDInService = psspy.abusint(-1,1,'NUMBER')
        # Machine bus (code =2/-2)
        ierr, machineBusNumber = psspy.amachint (-1,4,'NUMBER')
        # Load bus (code =1)
        ierr, busLoad = psspy.alodbusint(-1, 1, "NUMBER")
        ierr, zoneCount = psspy.azonecount(-1,2)
        ierr, areaCount = psspy.aareacount(-1,2)
        ierr, busName = psspy.abuschar(-1,2, 'NAME')
        ierr, busBaseKV = psspy.abusreal(-1,2,'BASE')
        ierr, busZoneNum = psspy.abusint(-1,2,'ZONE')
        ierr, busAreaNum = psspy.abusint(-1,2,'AREA')
        ierr, busTypeCode = psspy.abusint(-1,2,'TYPE')
        ierr, busOwner = psspy.abusint(-1,2,'OWNER')
        ierr, busVoltage = psspy.abusreal(-1,2,'PU')
        ierr, busAngle = psspy.abusreal(-1,2,'ANGLED')
        ierr, machineNum = psspy.amachcount(-1, 4)
        ierr, pgen_val = psspy.amachreal (-1,4,'PGEN')
        ierr, qgen_val = psspy.amachreal (-1,4,'QGEN')

        busCode2 = [[]]
        busAreaName = [[]]
        busZoneName = [[]]
        busCosPhi = [[]]
        busVoltageNew = [[]]
        busAngleNew = [[]]

        # Get bus Code
        for i in range(busesNumber):
            busIDi = busID[0][i]
            busNamei = busName[0][i]
            for j in range(areaCount):
                if(busAreaNum[0][i]==areaNumber[0][j]):
                    busAreaName[0].append(areaName[0][j])
            for j in range(zoneCount):
                if(busZoneNum[0][i]==zoneNumber[0][j]):
                    busZoneName[0].append(zoneName[0][j])
            if (busID[0][i] in machineBusNumber[0]):
                index = machineBusNumber[0].index(busID[0][i])
                if (pgen_val[0][index]*qgen_val[0][index]!=0) :
                    cosPhiVal = pgen_val[0][index]/ sqrt(pow(pgen_val[0][index],2)+pow(qgen_val[0][index],2))
                    busCosPhi[0].append(cosPhiVal)
                else:
                    busCosPhi[0].append("0")
            else:
                busCosPhi[0].append("NaN")

            busOwnerName[0].append('')

            text = str(busID[0][i])
           
            busVoltageNew[0].append(Decimal(busVoltage[0][i]).quantize(TWOPLACE))
            busAngleNew[0].append(Decimal(busAngle[0][i]).quantize(TWOPLACE))

        ierr, busNormalVmax = psspy.abusreal(-1,2,'NVLMHI')
        ierr, busNormalVmin = psspy.abusreal(-1,2,'NVLMLO')
        ierr, busEmergencyVmax = psspy.abusreal(-1,2,'EVLMHI')
        ierr, busEmergencyVmin = psspy.abusreal(-1,2,'EVLMLO')
        dt = np.dtype('<S16')
        # ma trận / mảng nhiều chiều chứa thông tin bus của file hiện tại
        matrixBus = np.array([busID[0],busName[0],busBaseKV[0],busAreaNum[0],busAreaName[0] ,busZoneNum[0],busZoneName[0] ,busOwner[0],busTypeCode[0],busVoltageNew[0],busAngleNew[0],busCosPhi[0]],dtype=dt)
        matrixBus = matrixBus.transpose()
        return matrixBus
    else:
        wx.MessageBox("Please open an existing case first!")

def array2dict(dict_keys, dict_values):
    tmpdict = {}
    for i in range(len(dict_keys)):
        tmpdict[dict_keys[i].lower()] = dict_values[i]
    return tmpdict

# lấy thông tin hiển thị cho bảng MBA 2 cuộn dây
@profiled('psse.extract.transformer_2wind')
def load2windTab(path=''):
    sid = -1
    owner = 1
    ties = 3 #1
    flag = 2 #1
    entry = 1
     
    PATH = path
    if PATH != '':
        # machine = 2-winding 
        # integer
        istring = ['FROMNUMBER','TONUMBER','STATUS','NTPOSN','CNXCOD']
        ierr, intVal = psspy.atrnint (sid,owner,ties,flag,entry,istring)
        i2wind = array2dict(istring,intVal)
        # real 
        astring = ['RATEA','RATIO','NOMV1']
        ierr, realVal = psspy.atrnreal (sid,owner,ties,flag,entry,astring)
        r2wind = array2dict(astring,realVal)
        # complex
        cstring = ['RXACT','RXNOM','RXZERO','Z01']
        ierr, cplxVal = psspy.atrncplx (sid,owner,ties,flag,entry,cstring)
        c2wind = array2dict(cstring,cplxVal)
        # charecter
        chrstring = ['ID','FROMNAME','TONAME']
        ierr, charVal = psspy.atrnchar (sid,owner,ties,flag,entry,chrstring)
        chr2wind = array2dict(chrstring,charVal)
        dt = np.dtype('<S16')

        RAct = []
        XAct= []
        Rnom = []
        Xnom =[]
        R01 = []
        X01 = []
        RZero = []
        XZero = []
        wind1nom = []
        wind1ratio = []
        for i in range(len(c2wind['rxact'])):
            RAct.append(Decimal(c2wind['rxact'][i].real).quantize(FIVEPLACE))
            XAct.append(Decimal(c2wind['rxact'][i].imag).quantize(FIVEPLACE))
            Rnom.append(Decimal(c2wind['rxnom'][i].real).quantize(FIVEPLACE))
            Xnom.append(Decimal(c2wind['rxnom'][i].imag).quantize(FIVEPLACE))
            R01.append(Decimal(c2wind['z01'][i].real).quantize(FIVEPLACE))
            X01.append(Decimal(c2wind['z01'][i].imag).quantize(FIVEPLACE))
            RZero.append(Decimal(c2wind['rxzero'][i].real).quantize(FIVEPLACE))
            XZero.append(Decimal(c2wind['rxzero'][i].imag).quantize(FIVEPLACE))
            wind1nom.append(Decimal(r2wind['nomv1'][i]).quantize(FIVEPLACE))
            wind1ratio.append(Decimal(r2wind['ratio'][i]).quantize(FIVEPLACE))

        matrix2wind = np.array([i2wind['fromnumber'],chr2wind['fromname'],i2wind['tonumber'],chr2wind['toname'],chr2wind['id'],i2wind['status'],i2wind['ntposn'],RAct,XAct,r2wind['ratea'],wind1ratio,wind1nom,Rnom,Xnom,i2wind['cnxcod'],R01,X01],dtype=dt)
        matrix2wind = matrix2wind.transpose()
        return matrix2wind
    else:
        wx.MessageBox("Please open an existing case first!")

# lấy thông tin hiển thị cho bảng MBA 3 cuộn dây
@profiled('psse.extract.transformer_3wind')
def load3windTab(path=''):
    sid = -1
    owner = 1
    ties = 3 #1
    flag = 2 #1
    flag_wnd = 3 #1
    entry = 1
     
    PATH = path
    if PATH != '':
        # machine = 2-winding 
        # integer
        istring = ['WIND1NUMBER','WIND2NUMBER','WIND3NUMBER','STATUS','CNXCOD']
        ierr, intVal = psspy.atr3int (sid,owner,ties,flag,entry,istring)
        i3wind = array2dict(istring,intVal)
        # real 
        astring = ['VMSTAR','ANSTAR']
        ierr, realVal = psspy.atr3real (sid,owner,ties,flag,entry,astring)
        r3wind = array2dict(astring,realVal)
        # complex
        cstring = ['RX1-2ACT','RX1-2NOM','RX2-3ACT','RX2-3NOM','RX3-1ACT','RX3-1NOM','Z01','Z02','Z03']
        ierr, cplxVal = psspy.atr3cplx (sid,owner,ties,flag,entry,cstring)
        c3wind = array2dict(cstring,cplxVal)
        # charecter
        chrstring = ['ID','WIND1NAME','WIND2NAME','WIND3NAME','XFRNAME']
        ierr, charVal = psspy.atr3char (sid,owner,ties,flag,entry,chrstring)
        chr3wind = array2dict(chrstring,charVal)

        a3windstring = ['RATEA','RATEB','RATEC','RATIO']
        ierr, real3windVal = psspy.awndreal (sid,owner,ties,flag_wnd,entry,a3windstring)
        r3windVal = array2dict(a3windstring, real3windVal)

        dt = np.dtype('<S16')
        rateAW12 = []
        rateAW23 = []
        rateAW31 = []
        ratio12 = []
        ratio23 = []
        ratio31 = []
        busNum = []
        busNumberPrevious = 0
        for busNumber in i3wind['wind1number']:

            if busNumber != busNumberPrevious:
                # print(busNumber)
                psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[busNumber],0,[],0,[])
                ierr, RateA3Wind = psspy.awndreal(0, 1,3, 3,1,"RATEA")
                ierr, RatioA3Wind = psspy.awndreal(0, 1,3, 3,1,"RATIO")
                ierr, wind3IDbyWind = psspy.awndchar(0, 1, 3,3, 1,"ID")
                ierr, wind3ID = psspy.atr3char(0, 1, 3,2, 1,"ID")
                ierr, winding3Num1 = psspy.atr3int(0,1, 3, 2, 1, "WIND1NUMBER")
                ierr, winding3Num2 = psspy.atr3int(0,1, 3, 2, 1, "WIND2NUMBER")
                ierr, winding3Num3 = psspy.atr3int(0,1, 3, 2, 1, "WIND3NUMBER")
                ierr, wind1Num = psspy.awndint(0, 1, 3, 3,1,"WIND1NUMBER")
                ierr, wind2Num = psspy.awndint(0, 1, 3, 3,1,"WIND2NUMBER")
                ierr, wind3Num = psspy.awndint(0, 1, 3, 3,1,"WIND3NUMBER")

                n = len(wind3ID[0])
                for i in range(n):
                    for j in range(n):
                        if wind3IDbyWind[0][j] == wind3ID[0][i] and busNumber == wind1Num[0][j] == winding3Num1[0][i] and wind2Num[0][j] == winding3Num2[0][i] and wind3Num[0][j] == winding3Num3[0][i]:
                            rateAW12.append(RateA3Wind[0][j])
                            rateAW23.append(RateA3Wind[0][j+n])
                            rateAW31.append(RateA3Wind[0][j+2*n])
                            ratio12.append(RatioA3Wind[0][j])
                            ratio23.append(RatioA3Wind[0][j+n])
                            ratio31.append(RatioA3Wind[0][j+2*n])
                            busNum.append(busNumber)
                         
                        
            busNumberPrevious = busNumber
        
        W12R = []
        W12X= []
        W23R = []
        W23X =[]
        W31R = []
        W31X =[]
        R01 = []
        X01 = []
        R02 = []
        X02 = []
        R03 = []
        X03 = []
        Vol = []
        Ang = []

        for i in range(len(c3wind['rx1-2act'])):
            W12R.append(Decimal(c3wind['rx1-2act'][i].real).quantize(FIVEPLACE))
            W12X.append(Decimal(c3wind['rx1-2act'][i].imag).quantize(FIVEPLACE))
            W23R.append(Decimal(c3wind['rx2-3act'][i].real).quantize(FIVEPLACE))
            W23X.append(Decimal(c3wind['rx2-3act'][i].imag).quantize(FIVEPLACE))
            W31R.append(Decimal(c3wind['rx3-1act'][i].real).quantize(FIVEPLACE))
            W31X.append(Decimal(c3wind['rx3-1act'][i].imag).quantize(FIVEPLACE))
            R01.append(Decimal(c3wind['z01'][i].real).quantize(SIXPLACE))
            X01.append(Decimal(c3wind['z01'][i].imag).quantize(SIXPLACE))
            R02.append(Decimal(c3wind['z02'][i].real).quantize(SIXPLACE))
            X02.append(Decimal(c3wind['z02'][i].imag).quantize(SIXPLACE))
            R03.append(Decimal(c3wind['z03'][i].real).quantize(SIXPLACE))
            X03.append(Decimal(c3wind['z03'][i].imag).quantize(SIXPLACE))
            Vol.append(Decimal(r3wind['vmstar'][i].imag).quantize(FIVEPLACE))
            Ang.append(Decimal(r3wind['anstar'][i].imag).quantize(FIVEPLACE))

        matrix3wind = np.array([i3wind['wind1number'],chr3wind['wind1name'],i3wind['wind2number'],chr3wind['wind2name'],i3wind['wind3number'],chr3wind['wind3name'],chr3wind['xfrname'],chr3wind['id'],i3wind['status'],W12R,W12X,W23R,W23X,W31R,W31X,Vol,Ang,i3wind['cnxcod'],R01,X01,R02,X02,R03,X03,rateAW12,rateAW23,rateAW31,ratio12,ratio23,ratio31],dtype=dt)
        matrix3wind = matrix3wind.transpose()
        return matrix3wind
    else:
        wx.MessageBox("Please open an existing case first!")

# lấy thông tin hiển thị cho bảng nguồn
@profiled('psse.extract.source')
def loadMachineTab(path=''):
    PATH = path
    if PATH != '':
        global machineNum, machineBusNumber, machineName, pgen_val, qgen_val, pmax_val, pmin_val, qmax_val, qmin_val
        # Machine number
        ierr, machineNum = psspy.amachcount(-1, 4)
        ierr, machineBusNumber = psspy.amachint (-1,4,'NUMBER')
        ierr, machineName = psspy.amachchar(-1,4,'NAME')
        ierr, machineId = psspy.amachchar(-1,4,'ID')
        ierr, inservice = psspy.amachint (-1,4,'STATUS')
        ierr, pgen_val = psspy.amachreal (-1,4,'PGEN')
        ierr, pmax_val = psspy.amachreal (-1,4,'PMAX')       
        ierr, qgen_val = psspy.amachreal (-1,4,'QGEN')
        ierr, qmax_val = psspy.amachreal (-1,4,'QMAX')
        ierr, mbase_val = psspy.amachreal (-1,4,'MBASE')
        ierr, subtransientX = psspy.amachreal (-1,4,'XSUBTR')
        ierr, transientX = psspy.amachreal (-1,4,'XTRANS')
        ierr, synchronousX = psspy.amachreal (-1,4,'XSYNCH')
        ierr, negativeZ = psspy.amachcplx(-1,4,'ZNEG') # complex
        ierr, zeroZ = psspy.amachcplx(-1,4,'ZZERO') # complex
        ierr, groundingZ = psspy.amachcplx(-1,4,'ZGRND') # complex
        ierr, plantVsched = psspy.agenbusreal(-1,4,'VSPU')
        ierr, plantNum = psspy.agenbusint(-1,4,'NUMBER')
        ierr, plantArea = psspy.agenbusint(-1,4,'AREA')
        ierr, plantZone = psspy.agenbusint(-1,4,'ZONE')
        ierr, plantBase = psspy.agenbusreal(-1,4,'BASE')
        ierr, plantActualVoltage = psspy.agenbusreal(-1,4,'KV')
        ierr, macImpedance = psspy.amachcplx(-1,4,"ZSORCE")

        genArea = [[]]
        genZone = [[]]
        genBaseKV = [[]]
        genActualKV = [[]]
        vsched = [[]]
        pgen_valNew =[[]]
        pgen_percent = [[]]
        qgen_valNew =[[]]
        qgen_percent = [[]]
        genAreaName = [[]]
        genZoneName = [[]]
        cosPhi = [[]]
        mbase_valNew = [[]]
        subtransientXNew = [[]]
        transientXNew = [[]]
        synchronousXNew = [[]]
        negativeXNew = [[]]
        zeroXNew = [[]]
        xSource = [[]]

        for i in range(machineNum):
            # Decimal(pgen_val[0][i]).quantize(TWOPLACE)
            pgen_valNew[0].append(Decimal(pgen_val[0][i]).quantize(TWOPLACE))
            qgen_valNew[0].append(Decimal(qgen_val[0][i]).quantize(TWOPLACE))
            mbase_valNew[0].append(Decimal(mbase_val[0][i]).quantize(ONEPLACE))
            subtransientXNew[0].append(Decimal(subtransientX[0][i]).quantize(THREEPLACE))
            transientXNew[0].append(Decimal(transientX[0][i]).quantize(THREEPLACE))
            synchronousXNew[0].append(Decimal(synchronousX[0][i]).quantize(THREEPLACE))
            negativeXNew[0].append(Decimal(negativeZ[0][i].imag).quantize(THREEPLACE))
            zeroXNew[0].append(Decimal(zeroZ[0][i].imag).quantize(THREEPLACE))
            if float(pmax_val[0][i]) != 0: 
                pgen_percent[0].append(abs(Decimal(pgen_val[0][i]*100/pmax_val[0][i]).quantize(TWOPLACE)))
            else:
                pgen_percent[0].append(0)

            if float(qmax_val[0][i]) != 0: 
                qgen_percent[0].append(abs(Decimal(qgen_val[0][i]*100/qmax_val[0][i]).quantize(TWOPLACE)))
            else:
                qgen_percent[0].append(0)
            
            if float(qgen_val[0][i])*float(pgen_val[0][i]) != 0: 
                cosPhi[0].append(abs(Decimal(pgen_val[0][i]/sqrt(pow(pgen_val[0][i],2)+pow(qgen_val[0][i],2))).quantize(TWOPLACE)))
            else:
                cosPhi[0].append(0)

            for j in range(len(plantNum[0])):
                if int(machineBusNumber[0][i]) == int(plantNum[0][j]):
                    genArea[0].append(plantArea[0][j])
                    genZone[0].append(plantZone[0][j])
                    genBaseKV[0].append(Decimal(plantBase[0][j]).quantize(ONEPLACE))
                    genActualKV[0].append(Decimal(plantActualVoltage[0][j]).quantize(ONEPLACE))
                    vsched[0].append(Decimal(plantVsched[0][j]).quantize(TWOPLACE))
                    

        for i in range(machineNum):
            
            xSource[0].append(Decimal(macImpedance[0][i].imag).quantize(FOURPLACE))
            for j in range(areaCount):
                if(int(genArea[0][i])==int(areaNumber[0][j])):
                    genAreaName[0].append(areaName[0][j])
            if not int(genArea[0][i]) in areaNumber[0]:
                genAreaName[0].append(' ')
            for j in range(zoneCount):
                if(genZone[0][i]==zoneNumber[0][j]):
                    genZoneName[0].append(zoneName[0][j])
            if not int(genZone[0][i]) in zoneNumber[0]:
                genZoneName[0].append(' ')
        # Create bus tab S
        matrixGen = np.array([machineBusNumber[0],machineName[0],genArea[0],genAreaName[0],genZone[0],genZoneName[0],machineId[0],inservice[0],
                        genBaseKV[0],genActualKV[0], vsched[0] , pgen_valNew[0],pmax_val[0],pgen_percent[0],qgen_valNew[0],qmax_val[0], qgen_percent[0],
                        cosPhi[0], mbase_val[0],subtransientXNew[0],transientXNew[0],synchronousXNew[0],negativeXNew[0],zeroXNew[0],xSource[0],])
        matrixGen = matrixGen.transpose()

        return matrixGen
    else:
        wx.MessageBox("Please open an existing case first!") 

# lấy thông tin hiển thị cho phần thông tin nguồn, tải 3 miền và toàn quốc trong trang nguồn
@profiled('psse.extract.source_load_totals')
def loadSourceLoadInfo(path=''):
    ierr,loadTotal = psspy.azonereal(-1,2,'PLOADLD')
    ierr,genTotal = psspy.azonereal(-1,2,'PGEN')
    # miền Bắc + nước ngoài
    zoneNum = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,99]

    psspy.zsys(1,len(zoneNum),zoneNum)
    ierr,pgenNorth = psspy.azonereal(1,2,'PGEN')
    ierr,loadNorth = psspy.azonereal(1,2,'PLOADLD')
    totalPgenNorth = 0
    totalLoadNorth = 0
    for i in range(len(pgenNorth[0])):
        totalPgenNorth+=pgenNorth[0][i]
    for i in range(len(loadNorth[0])):
        totalLoadNorth+=loadNorth[0][i]
    
    # miền Trung
    zoneNum = [50,51,52,53,54,55,56,57,58,59,60,61,62]
    psspy.zsys(1,len(zoneNum),zoneNum)
    ierr,pgenCentral = psspy.azonereal(1,2,'PGEN')
    ierr,loadCentral = psspy.azonereal(1,2,'PLOADLD')
    
    totalPgenCentral = 0
    totalLoadCentral = 0
    for i in range(len(pgenCentral[0])):
        totalPgenCentral+=pgenCentral[0][i]
    for i in range(len(loadCentral[0])):
        totalLoadCentral+=loadCentral[0][i]

    # miền Nam
    zoneNum = [70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91]
    psspy.zsys(1,len(zoneNum),zoneNum)

    ierr,pgenSouth = psspy.azonereal(1,2,'PGEN')
    ierr,loadSouth = psspy.azonereal(1,2,'PLOADLD')
    totalPgenSouth = 0
    totalLoadSouth = 0
    for i in range(len(pgenSouth[0])):
        totalPgenSouth+=pgenSouth[0][i]
    for i in range(len(loadSouth[0])):
        totalLoadSouth+=loadSouth[0][i]

    totalPgen = totalPgenNorth+totalPgenCentral+totalPgenSouth
    totalLoad = totalLoadNorth+totalLoadCentral+totalLoadSouth

    areaNum = [16,17,40,41,70,26,27,28,29,50,51,52,80,36,37,38,39,60,61,62,63,90,100,110,120]
    
    ierr, busID = psspy.abusint(-1,2,'NUMBER')
    ierr, busTypeCode = psspy.abusint(-1,2,'TYPE')
    ierr, busAreaNum = psspy.abusint(-1,2,'AREA')
    swingBus = []
    swingArea = []
    pGenSwing = []
    pmaxSwing = []

    for i,code in enumerate(busTypeCode[0]):
        if code == 3:
            psspy.bsys(1,0,[ 1.0, 500.0],0,[],1,[busID[0][i]],0,[],0,[])
            ierr, pmax = psspy.amachreal (1,1,'PMAX')
            ierr, pgen = psspy.amachreal (1,1,'PGEN')
            swingBus.append(busID[0][i])

            if pgen[0][0]<0:
                if not busAreaNum[0][i] in swingArea:
                    swingArea.append(busAreaNum[0][i])
                    pGenSwing.append(pgen[0][0])
                    pmaxSwing.append(pmax[0][0])
                else:
                    pGenSwing[len(pGenSwing)-1] = pGenSwing[len(pGenSwing)-1]+pgen[0][0]
                    pmaxSwing[len(pmaxSwing)-1] = pmaxSwing[len(pmaxSwing)-1]+pmax[0][0]

    pgenSelect = []
    for area in areaNum:
        psspy.asys(1,1,area)
        ierr, pgenArea = psspy.aareareal(1,2,'PGEN')
        if len(pgenArea[0]) != 0:
            
            pgen = pgenArea[0][0]
            if area in swingArea:
                index = swingArea.index(area)
                pgen = pgenArea[0][0]-pGenSwing[index]
            pgenSelect.append(pgen)
        else:
            pgenSelect.append(0)

    pmaxArea = []

    # nếu area có chứa swing bus thì Pmax của area phải trừ đi Pmax của nút swing
    for i,area in enumerate(areaNum):
        psspy.bsys(2,0,[ 1.0, 500.0],1,[area],0,[],0,[],0,[])
        ierr, pmaxSelect = psspy.amachreal (2,1,'PMAX')
        pgen= pgenSelect[i]
        pmax  = 0

        for i in range(len(pmaxSelect[0])):
            pmax+=pmaxSelect[0][i]
        if area in swingArea:
            index = swingArea.index(area)
            pmax-=pmaxSwing[index]
        pmaxArea.append(pmax)

    ratio = []
    for i in range(len(pmaxArea)):
        if pmaxArea[i] !=0:
            ratio.append(pgenSelect[i]/pmaxArea[i])
        else:
            ratio.append('NaN')

    result = [totalPgen,totalLoad, totalPgenNorth,totalLoadNorth,totalPgenCentral,totalLoadCentral,totalPgenSouth,totalLoadSouth,ratio]

    return result
    
# lấy thông tin hiển thị cho bảng phụ tải
@profiled('psse.extract.load')
def loadLoadTab(path=''):
    PATH = path
    if PATH != '':
        ierr, loadBusBaseKV = psspy.alodbusreal(-1, 4, "BASE")
        ierr, loadBusActualKV = psspy.alodbusreal(-1, 4, "KV")
        ierr, loadNumber = psspy.aloadint(-1, 4, "NUMBER")
        ierr, loadName = psspy.aloadchar(-1, 4, "NAME")
        ierr, loadID = psspy.aloadchar(-1, 4, "ID")
        ierr, loadArea =  psspy.aloadint(-1, 4, "AREA")
        ierr, loadZone =  psspy.aloadint(-1, 4, "ZONE")
        ierr, loadStatus =  psspy.aloadint(-1, 4, "STATUS")
        ierr, loadMVAComplex =  psspy.aloadcplx(-1, 4, "MVAACT")
        ierr, loadActualMVA =  psspy.aloadreal(-1, 4, "MVAACT")
        ierr, loadNominalMVA =  psspy.aloadreal(-1, 4, "MVANOM")
        loadP = [[]]
        loadQ = [[]]
        cosPhi = [[]]
        loadActualMVANew = [[]]
        loadAreaName = [[]]
        loadZoneName = [[]]

        for i in range(len(loadNumber[0])):
            loadActualMVANew[0].append(Decimal(loadActualMVA[0][i]).quantize(FOURPLACE))
            p = loadMVAComplex[0][i].real
            q = loadMVAComplex[0][i].imag
            loadP[0].append(Decimal(p).quantize(FOURPLACE))
            loadQ[0].append(Decimal(q).quantize(FOURPLACE))
            if (p*q != 0):
                cosPhi[0].append(Decimal(p/sqrt(pow(p,2)+pow(q,2))).quantize(TWOPLACE))
            else:
                cosPhi[0].append(0)

        for i in range(len(loadNumber[0])):
            for j in range(areaCount):
                if(int(loadArea[0][i])==int(areaNumber[0][j])):
                    loadAreaName[0].append(areaName[0][j])
            for j in range(zoneCount):
                if(loadZone[0][i]==zoneNumber[0][j]):
                    loadZoneName[0].append(zoneName[0][j])

        # mảng nhiều chiều chứa thông tin phụ tải
        matrixLoad = np.array([loadNumber[0],loadName[0],loadArea[0],loadAreaName[0],loadZone[0],loadZoneName[0],loadID[0],
                            loadStatus[0],loadP[0],loadQ[0],cosPhi[0],loadActualMVANew[0]])
        matrixLoad = matrixLoad.transpose()
        return matrixLoad

    else:
        wx.MessageBox("Please open an existing case first!") 

# lấy thông tin hiển thị cho bảng kháng, tụ, gom chung fixed shunt và switched shunt
@profiled('psse.extract.shunt')
def loadShuntTab(path=''):
    PATH = path
    if PATH != '':
        # fixed shunt
        ierr, shuntBusNum = psspy.afxshntbusint(-1,4,"NUMBER")
        ierr, shuntBusName = psspy.afxshntbusint(-1,4,"NAME")
        ierr, shuntType = psspy.afxshntbusint(-1,4,"TYPE")
        ierr, shuntBusArea = psspy.afxshntbusint(-1,4,"AREA")
        ierr, shuntBusZone = psspy.afxshntbusint(-1,4,"ZONE")
        ierr, shuntBusStatus = psspy.afxshntbusint(-1,4,"STATUS")
        ierr, shuntBusBase = psspy.afxshntbusreal(-1,4,"BASE")

        ierr, shuntNum = psspy.afxshuntint(-1,4,"NUMBER")
        ierr, shuntID = psspy.afxshuntchar(-1,4,"ID")
        ierr, shuntName = psspy.afxshuntchar(-1,4,"NAME")
        ierr, shuntStatus = psspy.afxshuntint(-1,4,"STATUS")
        ierr, shuntGBAct = psspy.afxshuntreal(-1,4,"SHUNTACT")
        ierr, shuntGBNom = psspy.afxshuntreal(-1,4,"SHUNTNOM")
        ierr, shuntGBNomCplx = psspy.afxshuntcplx(-1,4,"SHUNTNOM")
        ierr, shuntGBZero = psspy.afxshuntreal(-1,4,"GBZERO")

        shuntArea = [[]]
        shuntAreaName = [[]]
        shuntZone = [[]]
        shuntZoneName = [[]]
        shuntBaseKV = [[]]
        shuntType = [[]]
        shuntGBReal = [[]]

        for i in range(len(shuntNum[0])):
            for j in range(len(shuntBusNum[0])):
                if int(shuntNum[0][i]) == int(shuntBusNum[0][j]):
                    shuntArea[0].append(shuntBusArea[0][j])
                    shuntZone[0].append(shuntBusZone[0][j])
                    shuntBaseKV[0].append(Decimal(shuntBusBase[0][j]).quantize(ONEPLACE))
                    shuntGBReal[0].append(shuntGBNomCplx[0][i].imag)

        for i in range(len(shuntNum[0])):
            shuntType[0].append('Fixed')
            for j in range(areaCount):
                if(int(shuntArea[0][i])==int(areaNumber[0][j])):
                    shuntAreaName[0].append(areaName[0][j])
            for j in range(zoneCount):
                if(shuntZone[0][i]==zoneNumber[0][j]):
                    shuntZoneName[0].append(zoneName[0][j])

        matrix = np.array([shuntType[0],shuntNum[0],shuntName[0],shuntArea[0],shuntAreaName[0],shuntZone[0],
                                            shuntZoneName[0],shuntID[0],shuntStatus[0],shuntBaseKV[0],shuntGBAct[0],shuntGBReal[0],shuntGBZero[0]])
        matrixFixed = matrix.transpose()

        # Switched shunt
        ierr, swNumber = psspy.aswshint(-1, 4,'NUMBER')
        ierr, swName = psspy.aswshchar(-1, 4,'NAME')
        ierr, swArea = psspy.aswshint(-1, 4,'AREA')
        ierr, swZone = psspy.aswshint(-1, 4,'ZONE')
        ierr, swStatus = psspy.aswshint(-1, 4,'STATUS')
        ierr, swBaseKV = psspy.aswshreal(-1, 4,'BASE')
        ierr, swBSwNom = psspy.aswshreal(-1, 4,'BSWNOM')
        ierr, swBSwAct = psspy.aswshreal(-1, 4,'BSWACT')
        ierr, swBSwZero = psspy.aswshreal(-1, 4,'BSWZERO')
        swAreaName =[[]]
        swZoneName = [[]]
        swType = [[]]
        swID = [[]]
        for i in range(len(swNumber[0])):
            swType[0].append('Switched')
            swID[0].append('-')
            for j in range(areaCount):
                if(int(swArea[0][i])==int(areaNumber[0][j])):
                    swAreaName[0].append(areaName[0][j])
            for j in range(zoneCount):
                if(swZone[0][i]==zoneNumber[0][j]):
                    swZoneName[0].append(zoneName[0][j])

        matrixSw = np.array([swType[0],swNumber[0],swName[0],swArea[0],swAreaName[0],swZone[0],swZoneName[0],swID[0],swStatus[0],swBaseKV[0],swBSwAct[0],swBSwNom[0],swBSwZero[0]])
        matrixSWSht = matrixSw.transpose()
        matrixShunt = matrixFixed.tolist()+matrixSWSht.tolist()
        # mảng combine fixed shunt và switched shunt
        matrixShunt = np.array(matrixShunt)

        return matrixShunt

    else:
        wx.MessageBox("Please open an existing case first!") 

# chọn zone từ area
def select_zone_from_area(areaNum=0, matrixBus=[],matrixZone = []):
    zoneList = [] 
    matrixZoneNew= []
    for i in range(len(matrixBus)):
        if (matrixBus[i][3] == areaNum):
            if not matrixBus[i][5] in zoneList:
                zoneList.append(matrixBus[i][5])

    for i in range(len(matrixZone)):
        if (str(matrixZone[i][0]) in zoneList):
            matrixZoneNew.append(matrixZone[i][:])
    return matrixZoneNew

# lấy thông tin bus từ mảng chứa thông tin bus
def select_bus_from_matrixBus(busNum=0, matrixBus=[]):
    for i in range(len(matrixBus)):
        if (int(matrixBus[i][0]) == busNum):
            return matrixBus[i][:]

# tìm kiếm bus theo lựa chọn
def searchByChoice(choiceID=0, text='',matrixBus = []):
    choiceID = choiceID
    choiceString = text  
    busList = [] 
    matrixBusNew= []

    # id = 0: busID
    # id = 1: busName
    # id = 2: base KV
    # id = 3: area Num
    # id = 4: area name
    # id = 5: zone num
    # id = 6: zone name
    # id = 7: code

    for i in range(len(matrixBus[0])):
        if (str(matrixBus[0][i][choiceID]) == choiceString):
            return matrixBus[0][i][:]

# trả về thông tin đường dây, MBA 2 cd, 3 cd từ bus tìm kiếm
def loadBusNumberEnter(busNum = 0):
        busNumber = busNum
        # create subnumber from bus number
        psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(busNumber)],0,[],0,[])
        # branch
         
        ierr, toNumber = psspy.abrnint (0, 2,2,2,1,'TONUMBER')
        ierr, toName = psspy.abrnchar (0, 2,2,2,1,'TONAME')

        if busNumber in toNumber[0]:
            index = toNumber[0].index(busNumber)
            toNumber[0].remove(busNumber)
            toName[0].remove(toName[0][index])
        # machine = 2-winding 
        ierr, machineBusNumber = psspy.abrnint (0, 2,3,6,1,'TONUMBER')
        ierr, machineName = psspy.abrnchar (0, 2,3,6,1,'TONAME')

        # load infor
        ierr, loadNum = psspy.alodbusint(0, 4,"NUMBER")
        ierr, loadName = psspy.alodbuschar(0, 4,"NAME")
        # 2-winding

        # 3-winding
        ierr, winding3Num1 = psspy.atr3int(0, 1, 3, 2, 1, "WIND1NUMBER")
        ierr, winding3Num2 = psspy.atr3int(0, 1, 3, 2, 1, "WIND2NUMBER")
        ierr, winding3Num3 = psspy.atr3int(0, 1, 3, 2, 1, "WIND3NUMBER")
        ierr, winding3Name1 = psspy.atr3char(0, 1, 3, 2, 1, "WIND1NAME")
        ierr, winding3Name2 = psspy.atr3char(0, 1, 3, 2, 1, "WIND2NAME")
        ierr, winding3Name3 = psspy.atr3char(0, 1, 3, 2, 1, "WIND3NAME")
        wind3 = [[]]
        wind3Name = [[]]
                
        if busNumber in winding3Num1[0]:
            wind3 = np.array([winding3Num2[0],winding3Num3[0]])
            wind3Name = np.array([winding3Name2[0],winding3Name3[0]])

        elif busNumber in winding3Num2[0]:
            wind3 = np.array([winding3Num1[0],winding3Num3[0]])
            wind3Name = np.array([winding3Name1[0],winding3Name3[0]])

        else:
            wind3 = np.array([winding3Num1[0],winding3Num2[0]])
            wind3Name = np.array([winding3Name1[0],winding3Name2[0]])

        busNumber = [[]]
        busName = [[]]
        busNumber = np.array([toNumber[0],machineBusNumber[0],wind3[0]])
        busName = np.array([toNumber[0],machineBusNumber[0],wind3Name[0]])

        return [busNumber[0],busName[0], machineBusNumber[0],machineName[0],wind3[0],wind3Name[0]]

# lọc bus từ zone được chọn
def select_bus_from_zone(zoneNum=0, matrixBus=[]):
    busList = [] 
    matrixBusNew= []
    for i in range(len(matrixBus)):
        if (int(matrixBus[i][5]) == int(zoneNum)):
            matrixBusNew.append(matrixBus[i][:])
    return matrixBusNew

# lọc MBA 2 cd từ zone được chọn
def select_2Wind_from_zone(zoneNum=0, matrixBus=[],matrix2Wind = []):
    busList = [] 
    matrix2WindNew= []
    for i in range(len(matrixBus)):
        if (matrixBus[i][5] == zoneNum):
            if not matrixBus[i][5] in busList:
                busList.append(matrixBus[i][0])
    for i in range(len(matrix2Wind)):
        if (str(matrix2Wind[i][0]) in busList or str(matrix2Wind[i][2]) in busList):
            matrix2WindNew.append(matrix2Wind[i][:])
    return matrix2WindNew

# lọc MBA 3 CD từ zone được chọn
def select_3Wind_from_zone(zoneNum=0, matrixBus=[],matrix3Wind = []):
    busList = [] 
    matrix3WindNew= []
    for i in range(len(matrixBus)):
        if (matrixBus[i][5] == zoneNum):
            if not matrixBus[i][5] in busList:
                busList.append(matrixBus[i][0])
    for i in range(len(matrix3Wind)):
        if (str(matrix3Wind[i][0]) in busList or str(matrix3Wind[i][2]) in busList or str(matrix3Wind[i][4]) in busList):
            matrix3WindNew.append(matrix3Wind[i][:])
    return matrix3WindNew

# lọc nguồn từ zone được chọn
def select_source_from_zone(zoneNum=0, matrixSource=[]):
    sourceList = [] 
    matrixSourceNew= []

    for i in range(len(matrixSource)):
        if (int(matrixSource[i][4]) == int(zoneNum)):
            matrixSourceNew.append(matrixSource[i][:])
    return matrixSourceNew

# lọc tải từ zone được chọn
def select_load_from_zone(row= 0,zoneNum=0, matrixLoad=[], mygridLoad = wx.grid.Grid):
    loadList = [] 
    matrixLoadNew= []

    for i in range(len(matrixLoad)):
        if (int(matrixLoad[i][4]) == int(zoneNum)):
            matrixLoadNew.append(matrixLoad[i][:])
    
    PLoad = mygridLoad.GetCellValue(row,4)
    QLoad = mygridLoad.GetCellValue(row,5)
    CosPhi = mygridLoad.GetCellValue(row,6)
    return [PLoad,QLoad,CosPhi,matrixLoadNew]

# lọc kháng/tụ từ zone được chọn
def select_shunt_from_zone(zoneNum=0, matrixShunt=[]):
    shuntList = [] 
    matrixShuntNew= []
    for i in range(len(matrixShunt)):
        if (int(matrixShunt[i][5]) == int(zoneNum)):
            matrixShuntNew.append(matrixShunt[i][:])
    return matrixShuntNew

# lọc bus từ area được chọn
def select_bus_from_area(areaNum=0, matrixBus=[]):
    busList = [] 
    matrixBusNew= []
    for i in range(len(matrixBus)):
        if (str(matrixBus[i][3]) == areaNum):
            matrixBusNew.append(matrixBus[i][:])
    return matrixBusNew
    
# lọc MBA 2 CD từ area được chọn
def select_2Wind_from_area(areaNum=0, matrixBus=[], matrix2Wind = []):
    busList = [] 
    matrix2WindNew= []
    for i in range(len(matrixBus)):
        if (matrixBus[i][3] == areaNum):
            if not matrixBus[i][3] in busList:
                busList.append(matrixBus[i][0])
    for i in range(len(matrix2Wind)):
        if (str(matrix2Wind[i][0]) in busList) or (str(matrix2Wind[i][2]) in busList) :
            matrix2WindNew.append(matrix2Wind[i][:])
    return matrix2WindNew

# lọc MBA 3 CD từ area được chọn
def select_3Wind_from_area(areaNum=0, matrixBus=[], matrix3Wind = []):
    busList = [] 
    matrix3WindNew= []
    for i in range(len(matrixBus)):
        if (matrixBus[i][3] == areaNum):
            if not matrixBus[i][3] in busList:
                busList.append(matrixBus[i][0])
    for i in range(len(matrix3Wind)):
        if (str(matrix3Wind[i][0]) in busList or str(matrix3Wind[i][2]) in busList or str(matrix3Wind[i][4]) in busList):
            matrix3WindNew.append(matrix3Wind[i][:])
    return matrix3WindNew

# lọc nguồn từ area được chọn
def select_source_from_area(areaNum=0, matrixSource=[]):
    sourceList = [] 
    matrixSourceNew= []

    for i in range(len(matrixSource)):
        if (int(matrixSource[i][2]) == int(areaNum)):
            matrixSourceNew.append(matrixSource[i][:])
    return matrixSourceNew

# lọc tải từ area được chọn
def select_load_from_area(row= 0,areaNum=0, matrixLoad=[], mygridLoad = wx.grid.Grid):
    loadList = [] 
    matrixLoadNew= []

    for i in range(len(matrixLoad)):
        if (int(matrixLoad[i][2]) == int(areaNum)):
            matrixLoadNew.append(matrixLoad[i][:])
    
    PLoad = mygridLoad.GetCellValue(row,4)
    QLoad = mygridLoad.GetCellValue(row,5)
    CosPhi = mygridLoad.GetCellValue(row,6)
    return [PLoad,QLoad,CosPhi,matrixLoadNew]

# lọc kháng/tụ từ area được chọn
def select_shunt_from_area(areaNum=0, matrixShunt=[]):
    shuntList = [] 
    matrixShuntNew= []
    for i in range(len(matrixShunt)):
        if (int(matrixShunt[i][3]) == int(areaNum)):
            matrixShuntNew.append(matrixShunt[i][:])
    return matrixShuntNew
