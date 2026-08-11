# -*- coding: utf-8 -*-
import glob, os, sys

# Tạo file .sub
def createSubFile(dirname = '',zoneNumber = [],areaNumber = []):
    path = os.path.join(dirname,'area.sub')

    f = open(path,'w')
    f.write("COM\n")
    f.write("COM CONTINGENCY description file entry created by PSS(R)E Config File Builder\n")
    f.write("COM\n")
    f.write("SUBSYSTEM 'AREA'\n")
    for i in range(len(areaNumber)):
        f.writelines("  AREA {}\n".format(areaNumber[i]))
    for i in range(len(zoneNumber)):
        f.writelines("  ZONE {}\n".format(zoneNumber[i]))
    f.write("END\n")
    f.write("END\n")
    f.close

# Tạo file .mon
def createMonFile(dirname = '',busNumber = []):
    path = os.path.join(dirname,'area.mon')
    f = open(path,'w')
    f.write("COM\n")
    f.write("COM CONTINGENCY description file entry created by PSS(R)E Config File Builder\n")
    f.write("COM\n")
    for i in range(len(busNumber)):
        f.writelines("MONITOR BRANCHES FROM BUS {}\n".format(busNumber[i]))
    f.write("END")
    f.close

# Tạo file .con
def createConFile(dirname = ''):
    path = os.path.join(dirname,'area.con')
    f = open(path,'w')
    f.write("COM\n")
    f.write("COM CONTINGENCY description file entry created by PSS(R)E Config File Builder\n")
    f.write("COM\n")
    f.write("SINGLE BRANCH IN SUBSYSTEM 'AREA'\n")
    f.write("END")
    f.close

# Tạo file tính contingency tự động cho tất cả các file trong thư mục
def createAutoFile(dirname = ''):
    path = os.path.join(dirname,'autoContigency.py')

    f = open(path,'w')
    f.write("import pssepath\n")
    f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
    f.write("sys.path.append(PSSE_LOCATION)\n")
    f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
    f.write("pssepath.add_pssepath(33)\n")
    f.write("import psspy \n")
    os.chdir(dirname)
    subfileName = glob.glob('*.sub')
    subFullPath = os.path.join(dirname,subfileName[0])
    monfileName = glob.glob('*.mon')
    monFullPath = os.path.join(dirname,monfileName[0])
    confileName = glob.glob('*.con')
    conFullPath = os.path.join(dirname,confileName[0])

    fName = os.path.basename(subFullPath)
    fileName = fName[0:-4]
    fullPath = os.path.join(dirname,fileName)

    f.write('SUBFILE =r"""{a}"""\n'.format(a=subFullPath))
    f.write('MONFILE =r"""{a}"""\n'.format(a=monFullPath))
    f.write('CONFILE =r"""{a}"""\n'.format(a=conFullPath)) 
    f.write('SUBSYSTEM =r"""{a}"""\n'.format(a=fileName)) 
     
    savfileNames = glob.glob('*.sav')
    for savfile in savfileNames:
        savFilePath = os.path.join(dirname,savfile)
        ACCFILE = savfile[0:-4]
        f.write('DFXFILE =r"""{a}.dfx"""\n'.format(a=ACCFILE))
        f.write('ACCFILE =r"""{a}"""\n'.format(a=ACCFILE))
        f.write('psspy.case(r"""{}""") \n'.format(savFilePath))
        f.write('psspy.dfax([1,1], SUBFILE, MONFILE, CONFILE, DFXFILE)\n')
        f.write('psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n')
        f.write('psspy.fdns()\n')
        f.write('psspy.fnsl()\n')
        f.write('psspy.fnsl()\n')
        f.write('psspy.accc_with_dsp( 0.5,[2,0,0,1,1,1,0,0],SUBSYSTEM,DFXFILE,ACCFILE,"","")\n')
    f.close

# Tạo file tính ổn định tĩnh tự động cho tất cả các file trong thư mục
def createAutoStaticFile(dirname = '',sinkSource=[]):
    path = os.path.join(dirname,'autoContigency.py')
    f = open(path,'w')
    f.write("import pssepath\n")
    f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
    f.write("sys.path.append(PSSE_LOCATION)\n")
    f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
    f.write("pssepath.add_pssepath(33)\n")
    f.write("import psspy \n")
    os.chdir(dirname)
    subfileName = glob.glob('*.sub')
    subFullPath = os.path.join(dirname,subfileName[0])
    monfileName = glob.glob('*.mon')
    monFullPath = os.path.join(dirname,monfileName[0])
    confileName = glob.glob('*.con')
    conFullPath = os.path.join(dirname,confileName[0])

    fName = os.path.basename(subFullPath)
    fileName = fName[0:-4]
    fullPath = os.path.join(dirname,fileName)
    f.write('SUBFILE =r"""{a}"""\n'.format(a=subFullPath))
    f.write('MONFILE =r"""{a}"""\n'.format(a=monFullPath))
    f.write('CONFILE =r"""{a}"""\n'.format(a=conFullPath)) 
    # f.write('SUBSYSTEM =r"""{a}"""\n'.format(a=fileName)) 
    sink = sinkSource[1]
    sinkDefault = sinkSource[2]
    source = sinkSource[0]

    f.write('SOURCE =r"""{a}"""\n'.format(a=source))
    f.write('SINK =r"""{a}"""\n'.format(a=sink))
    f.write('SINKDEFAULT =r"""{a}"""\n'.format(a=sinkDefault))
     
    savfileNames = glob.glob('*.sav')
    for savfile in savfileNames:
        savFilePath = os.path.join(dirname,savfile)
        PVFILE = savfile[0:-4]+'-pv'
        f.write('DFXFILE =r"""{a}.dfx"""\n'.format(a=savfile[0:-4]))
        f.write('PVFILE =r"""{a}"""\n'.format(a=PVFILE))
        f.write('psspy.case(r"""{}""") \n'.format(savFilePath))
        f.write('psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n')
        f.write('psspy.fdns()\n')
        f.write('psspy.fnsl()\n')
        f.write('psspy.fnsl()\n')
        f.write('psspy.dfax([1,1], SUBFILE, MONFILE, CONFILE, DFXFILE)\n')
        f.write('psspy.pv_engine_6([0,0,0,1,1,0,0,1,0,0,1,1,4,0,0,0,1,0,0,0,0,0,1,1,0],[ 0.5, 100.0, 100.0, 10000., 0.8, 100.0,0.0,0.0],[SOURCE,SINK,SINKDEFAULT],DFXFILE,"","","",PVFILE,"")\n')
    f.close

# tạo file dyn22.py từ file dyn22.idv
def createDyn22File(idvFile = '',params =[],option = []):
    [CONs,STATEs,VARs,ICONs] = params
    dirname = os.path.dirname(idvFile)
    ssn0 = dirname+'\\ssn0'
    ssn1 = dirname+'\\ssn1'
    gop = dirname+'\\gop'
    f = open(idvFile,'r')
    lines = f.readlines()

    flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = flag7 = flag8 = flag9 = 0
    flag10 = flag11 = flag12 = flag13 = flag14 = flag15 = flag16 = flag17 = flag18 =0
    flag19 = flag20 = flag21 = flag22 = flag23 = flag24 = flag25 = flag26 = flag27 = 0
    flag28 = flag29 = flag30 = flag31 = flag32 = flag33 = flag34 = flag35 = flag36 = flag37 =0

    angleArr = []
    angleIdArr = []
    angleNameArr = []

    pelecArr = []
    pelecIdArr = []
    pelecNameArr = []

    qelecArr = []
    qelecIdArr = []
    qelecNameArr = []

    etermArr = []
    etermIdArr = []
    etermNameArr = []

    efdArr = []
    efdIdArr = []
    efdNameArr = []

    pmechArr = []
    pmechIDArr = []
    pmechNameArr = []

    speedArr = []
    speedIDArr = []
    speedNameArr = []

    xadifdArr = []
    xadifdIDArr = []
    xadifdNameArr = []

    ecompArr = []
    ecompIDArr = []
    ecompNameArr = []

    vothsgArr = []
    vothsgIDArr = []
    vothsgNameArr = []

    vrefArr = []
    vrefIdArr = []
    vrefNameArr = []

    bsfreqArr = []
    bsfreqNameArr = []

    voltageArr = []
    voltageNameArr = []

    voltAndAngleArr = []
    voltAndAngleNameArr = []

    flowFrombus = []
    flowTobus = []
    flowID = []
    flowName = []

    flowPQFrombus = []
    flowPQTobus = []
    flowPQID = []
    flowPQName = []

    flowMVAFrombus = []
    flowMVATobus = []
    flowMVAID = []
    flowMVAName = []

    relay2Frombus = []
    relay2Tobus = []
    relay2ID = []
    relay2Name = []

    varArr = []
    varNameArr = []

    stateArr = []
    stateNameArr = []

    machItermArr = []
    machItermIdArr = []
    machItermNameArr = []

    machAppIMPArr = []
    machAppIMPIdArr = []
    machAppIMPNameArr = []

    vuelArr = []
    vuelIdArr = []
    vuelNameArr = []

    voelArr = []
    voelIdArr = []
    voelNameArr = []

    ploadArr = []
    ploadIdArr = []
    ploadNameArr = []

    qloadArr = []
    qloadIdArr = []
    qloadNameArr = []    

    grefArr = []
    grefIdArr = []
    grefNameArr = []

    lcrefArr = []
    lcrefIdArr = []
    lcrefNameArr = []

    windVelArr = []
    windVelIdArr = []
    windVelNameArr = []

    windTurSpdArr = []
    windTurSpdIdArr = []
    windTurSpdNameArr = []

    windPitchArr = []
    windPitchIdArr = []
    windPitchNameArr = []

    windAeroTorArr = []
    windAeroTorIdArr = []
    windAeroTorNameArr = []

    windRotorVolArr = []
    windRotorVolIdArr = []
    windRotorVolNameArr = []

    windRotorCurArr = []
    windRotorCurIdArr = []
    windRotorCurNameArr = []

    windPComandArr = []
    windPComandIdArr = []
    windPComandNameArr = []

    windQComandArr = []
    windQComandIdArr = []
    windQComandNameArr = []

    windAuxArr = []
    windAuxIdArr = []
    windAuxNameArr = []


    for i,line in enumerate(lines):
        #===> 1: 938044,,ANGLE_VUNGANG3#4
        if line == '1\n':
            flag1 = 1
        if flag1 ==1 and len(line.split(','))>1:
            items = line.split(',')
            angleArr.append(items[0])
            angleIdArr.append(items[1])
            angleNameArr.append(items[2])
        #===> 2: 938044,,PELEC_VUNGANG3#4
        if line == '2\n' :
            flag2 = 1
        if flag2 ==1 and len(line.split(','))>1 :  
            items = line.split(',')
            pelecArr.append(items[0])
            pelecIdArr.append(items[1])
            pelecNameArr.append(items[2])
        #===> 3: 938044,,QELEC_VUNGANG3#4
        if line == '3\n':
            flag3 = 1
        if flag3 ==1 and len(line.split(','))>1  :
            items = line.split(',')
            qelecArr.append(items[0])
            qelecIdArr.append(items[1])
            qelecNameArr.append(items[2])
        #===> 4: 938044,1,ETERM_VUNGANG3#4
        if line == '4\n':
            flag4 = 1
        if flag4 ==1 and len(line.split(','))>1:
            items = line.split(',')
            etermArr.append(items[0])
            etermIdArr.append(items[1])
            etermNameArr.append(items[2])
        #===> 5: 938044,1,EFD_VUNGANG3#4
        if line == '5\n':
            flag5 = 1
        if flag5 ==1 and len(line.split(','))>1  :
            items = line.split(',')
            efdArr.append(items[0])
            efdIdArr.append(items[1])
            efdNameArr.append(items[2])
        #===> 6: 938044,1,PMECH_VUNGANG3#4
        if line == '6\n':
            flag6 = 1
        if flag6 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            pmechArr.append(items[0])
            pmechIDArr.append(items[1])
            pmechNameArr.append(items[2])
        #===> 7: 938044,1,SPEED_VUNGANG3#4
        if line == '7\n' and lines[i-1]!= 'dlst\n':
            flag7 = 1
        if flag7 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            speedArr.append(items[0])
            speedIDArr.append(items[1])
            speedNameArr.append(items[2])
        #===> 8: 938044,1,XADIFD_VUNGANG3#4
        if line == '8\n':
            flag8 = 1
        if flag8 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            xadifdArr.append(items[0])
            xadifdIDArr.append(items[1])
            xadifdNameArr.append(items[2])
        #===> 9: 938044,1,ECOMP_VUNGANG3#4
        if line == '9\n':
            flag9 = 1
        if flag9 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            ecompArr.append(items[0])
            ecompIDArr.append(items[1])
            ecompNameArr.append(items[2])
        #===> 10: 938044,1,VOTHSG_VUNGANG3#4
        if line == '10\n':
            flag10 = 1
        if flag10 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            vothsgArr.append(items[0])
            vothsgIDArr.append(items[1])
            vothsgNameArr.append(items[2])
        #===> 11: 938044,1,VREF_VUNGANG3#4
        if line == '11\n':
            flag11 = 1
        if flag11 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            vrefArr.append(items[0])
            vrefIdArr.append(items[1])
            vrefNameArr.append(items[2])
        #===> 12: 38070,BSFREQ_VUNGANG3
        if line == '12\n':
            flag12 = 1
        if flag12 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            bsfreqArr.append(items[0])
            bsfreqNameArr.append(items[1])
        #===> 13: 38070,VOLTAGE_VUNGANG3
        if line == '13\n':
            flag13 = 1
        if flag13 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            voltageArr.append(items[0])
            voltageNameArr.append(items[1])
        #===> 14: 938044,voltAndAngLE_VUNGANG3#4
        if line == '14\n':
            flag14 = 1
        if flag14 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            voltAndAngleArr.append(items[0])
            voltAndAngleNameArr.append(items[1])
        #===> 15: 38070,37010,1,FLOW_VUNGANG3_THANHHOA#1
        if line == '15\n':
            flag15 = 1
        if flag15 ==1 and len(line.split(','))>1 :
            branchItems = line.split(',')
            flowFrombus.append(branchItems[0])
            flowTobus.append(branchItems[1])
            flowID.append(branchItems[2])
            flowName.append(branchItems[3])
        #===> 16: 38070,37010,1,FLOWPQ_VUNGANG3_THANHHOA#1
        if line == '16\n':
            flag16 = 1
        if flag16 ==1 and len(line.split(','))>1 :
            branchItems = line.split(',')
            flowPQFrombus.append(branchItems[0])
            flowPQTobus.append(branchItems[1])
            flowPQID.append(branchItems[2])
            flowPQName.append(branchItems[3])
        #===> 17: 38070,37010,1,FLOWMVA_VUNGANG3_THANHHOA#1
        if line == '17\n':
            flag17 = 1
        if flag17 ==1 and len(line.split(','))>1 :
            branchItems = line.split(',')
            flowMVAFrombus.append(branchItems[0])
            flowMVATobus.append(branchItems[1])
            flowMVAID.append(branchItems[2])
            flowMVAName.append(branchItems[3])
        #===> 18: 38070,37010,1,RELAY2_VUNGANG3_THANHHOA#1
        if line == '18\n':
            flag18 = 1
        if flag18 ==1 and len(line.split(','))>1 :
            branchItems = line.split(',')
            relay2Frombus.append(branchItems[0])
            relay2Tobus.append(branchItems[1])
            relay2ID.append(branchItems[2])
            relay2Name.append(branchItems[3])
        #===> 19: 938044,VAR_VUNGANG3#4
        if line == '19\n':
            flag19 = 1
        if flag19 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            varArr.append(items[0])
            varNameArr.append(items[1])
        #===> 20: 938044,STATE_VUNGANG3#4
        if line == '20\n':
            flag20 = 1
        if flag20 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            stateArr.append(items[0])
            stateNameArr.append(items[1])
        #===> 21: 938044,1,MACHITERM_VUNGANG3#4
        if line == '21\n':
            flag21 = 1
        if flag21 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            machItermArr.append(items[0])
            machItermIdArr.append(items[1])
            machItermNameArr.append(items[2])
        #===> 22: 938044,1,MACHAPPIMP_VUNGANG3#4
        if line == '22\n':
            flag22 = 1
        if flag22 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            machAppIMPArr.append(items[0])
            machAppIMPIdArr.append(items[1])
            machAppIMPNameArr.append(items[2])
        #===> 23: 938044,1,VUEL_VUNGANG3#4
        if line == '23\n':
            flag23 = 1
        if flag23 ==1 and len(line.split(','))>1  :
            items = line.split(',')
            vuelArr.append(items[0])
            vuelIdArr.append(items[1])
            vuelNameArr.append(items[2])
        #===> 24: 938044,1,VOEL_VUNGANG3#4
        if line == '24\n':
            flag24 = 1
        if flag24 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            voelArr.append(items[0])
            voelIdArr.append(items[1])
            voelNameArr.append(items[2])
        #===> 25: 112001,1,PLOAD_DONGMO1#4
        if line == '25\n':
            flag25 = 1
        if flag25 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            ploadArr.append(items[0])
            ploadIdArr.append(items[1])
            ploadNameArr.append(items[2])
        #===> 26: 112001,1,QLOAD_DONGMO1#4
        if line == '26\n':
            flag26 = 1
        if flag26 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            qloadArr.append(items[0])
            qloadIdArr.append(items[1])
            qloadNameArr.append(items[2])
        #===> 27: 938044,1,GREF_VUNGANG3#4
        if line == '27\n':
            flag27 = 1
        if flag27 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            grefArr.append(items[0])
            grefIdArr.append(items[1])
            grefNameArr.append(items[2])
        #===> 28: 938044,1,LCREF_VUNGANG3#4
        if line == '28\n':
            flag28 = 1
        if flag28 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            lcrefArr.append(items[0])
            lcrefIdArr.append(items[1])
            lcrefNameArr.append(items[2])
        #===> 29: 938044,1,WINDVEL_VUNGANG3#4
        if line == '29\n':
            flag29 = 1
        if flag29 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            windVelArr.append(items[0])
            windVelIdArr.append(items[1])
            windVelNameArr.append(items[2])
        #===> 30: 938044,1,WINDTURSPD_VUNGANG3#4
        if line == '30\n':
            flag30 = 1
        if flag30 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            windTurSpdArr.append(items[0])
            windTurSpdIdArr.append(items[1])
            windTurSpdNameArr.append(items[2])
        #===> 31: 938044,1,WINDPITCH_VUNGANG3#4
        if line == '31\n':
            flag31 = 1
        if flag31 ==1 and len(line.split(','))>1  :
            items = line.split(',')
            windPitchArr.append(items[0])
            windPitchIdArr.append(items[1])
            windPitchNameArr.append(items[2])
        #===> 32: 938044,1,WINDAEROTOR_VUNGANG3#4
        if line == '32\n':
            flag32 = 1
        if flag32 ==1 and len(line.split(','))>1  :
            items = line.split(',')
            windAeroTorArr.append(items[0])
            windAeroTorIdArr.append(items[1])
            windAeroTorNameArr.append(items[2])
        #===> 33: 938044,1,WINDROTORVOL_VUNGANG3#4
        if line == '33\n':
            flag33 = 1
        if flag33 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            windRotorVolArr.append(items[0])
            windRotorVolIdArr.append(items[1])
            windRotorVolNameArr.append(items[2])
        #===> 34: 938044,1,WINDROTORCUR_VUNGANG3#4
        if line == '34\n':
            flag34 = 1
        if flag34 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            windRotorCurArr.append(items[0])
            windRotorCurIdArr.append(items[1])
            windRotorCurNameArr.append(items[2])
        #===> 35: 938044,1,WINDPCOMAND_VUNGANG3#4
        if line == '35\n':
            flag35 = 1
        if flag35 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            windPComandArr.append(items[0])
            windPComandIdArr.append(items[1])
            windPComandNameArr.append(items[2])
        #===> 36: 938044,1,WINDQCOMAND_VUNGANG3#4
        if line == '36\n':
            flag36 = 1
        if flag36 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            windQComandArr.append(items[0])
            windQComandIdArr.append(items[1])
            windQComandNameArr.append(items[2])
        #===> 37: 938044,1,WINDAUX_VUNGANG3#4
        if line == '37\n':
            flag37 = 1
        if flag37 ==1 and len(line.split(','))>1 :
            items = line.split(',')
            windAuxArr.append(items[0])
            windAuxIdArr.append(items[1])
            windAuxNameArr.append(items[2])

        if line == '\n':
            flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = flag7 = flag8 = flag9 = 0
            flag10 = flag11 = flag12 = flag13 = flag14 = flag15 = flag16 = flag17 = flag18 =0
            flag19 = flag20 = flag21 = flag22 = flag23 = flag24 = flag25 = flag26 = flag27 = 0
            flag28 = flag29 = flag30 = flag31 = flag32 = flag33 = flag34 = flag35 = flag36 = flag37 =0

    # create file

    f = open('dyn_22.py','w')
    f.write("import pssepath\n")
    f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
    f.write("sys.path.append(PSSE_LOCATION)\n")
    f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
    f.write("pssepath.add_pssepath(33)\n")
    f.write("import psspy \n")
    if option[0] == 1:
        f.write('psspy.set_relang(1,{b},r"""{c}""")\n'.format(b=option[1][0],c=option[1][1]))
    elif option[0] == 2:
        f.write('psspy.set_relang(1,0,"")\n'.format(a=option[0]))
    elif option[0] == 3:
        f.write('psspy.set_relang(1,-1,"")\n'.format(a=option[0]))

    for i in range(len(angleArr)):
        f.write('psspy.machine_array_channel([-1,1,{a}],r"""1""",r"""{b}""")\n'.format(a=angleArr[i],b=angleNameArr[i][:-1]))
    for i in range(len(pelecArr)):
        f.write('psspy.machine_array_channel([-1,2,{a}],r"""1""",r"""{b}""")\n'.format(a=pelecArr[i],b=pelecNameArr[i][:-1]))
    for i in range(len(qelecArr)):
        f.write('psspy.machine_array_channel([-1,3,{a}],r"""1""",r"""{b}""")\n'.format(a=qelecArr[i],b=qelecNameArr[i][:-1]))
    for i in range(len(etermArr)):
        f.write('psspy.machine_array_channel([-1,4,{a}],r"""1""",r"""{b}""")\n'.format(a=etermArr[i],b=etermNameArr[i][:-1]))
    for i in range(len(efdArr)):
        f.write('psspy.machine_array_channel([-1,5,{a}],r"""1""",r"""{b}""")\n'.format(a=efdArr[i],b=efdNameArr[i][:-1]))
    for i in range(len(pmechArr)):
        f.write('psspy.machine_array_channel([-1,6,{a}],r"""1""",r"""{b}""")\n'.format(a=pmechArr[i],b=pmechNameArr[i][:-1]))
    for i in range(len(speedArr)):
        f.write('psspy.machine_array_channel([-1,7,{a}],r"""1""",r"""{b}""")\n'.format(a=speedArr[i],b=speedNameArr[i][:-1]))
    for i in range(len(xadifdArr)):
        f.write('psspy.machine_array_channel([-1,8,{a}],r"""1""",r"""{b}""")\n'.format(a=xadifdArr[i],b=xadifdNameArr[i][:-1]))
    for i in range(len(ecompArr)):
        f.write('psspy.machine_array_channel([-1,9,{a}],r"""1""",r"""{b}""")\n'.format(a=ecompArr[i],b=ecompNameArr[i][:-1]))
    for i in range(len(vothsgArr)):
        f.write('psspy.machine_array_channel([-1,10,{a}],r"""1""",r"""{b}""")\n'.format(a=vothsgArr[i],b=vothsgNameArr[i][:-1]))
    for i in range(len(vrefArr)):
        f.write('psspy.machine_array_channel([-1,11,{a}],r"""1""",r"""{b}""")\n'.format(a=vrefArr[i],b=vrefNameArr[i][:-1]))
    # 12
    for i in range(len(bsfreqArr)):
        f.write('psspy.bus_frequency_channel([-1,{a}],r"""{b}""")\n'.format(a=bsfreqArr[i],b=bsfreqNameArr[i][:-1]))
    for i in range(len(voltageArr)):
        f.write('psspy.voltage_channel([-1,-1,-1,{a}],r"""{b}""")\n'.format(a=voltageArr[i],b=voltageNameArr[i][:-1]))
    for i in range(len(voltAndAngleArr)):
        f.write('psspy.voltage_and_angle_channel([-1,-1,-1,{a}],r"""{b}""")\n'.format(a=voltAndAngleArr[i],b=voltAndAngleNameArr[i][:-1]))
    for i in range(len(flowName)):
        f.write('psspy.branch_p_channel([-1,-1,-1,{a},{b}],r"""{c}""",r"""{d}""")\n'.format(a=flowFrombus[i],b=flowTobus[i],c=flowID[i],d=flowName[i][:-1]))   
    # 16
    for i in range(len(flowPQName)):
        f.write('psspy.branch_p_and_q_channel([-1,-1,-1,{a},{b}],r"""{c}""",r"""{d}""")\n'.format(a=flowPQFrombus[i],b=flowPQTobus[i],c=flowPQID[i],d=flowPQName[i][:-1]))   
    for i in range(len(flowMVAName)):
        f.write('psspy.branch_mva_channel([-1,-1,-1,{a},{b}],r"""{c}""",r"""{d}""")\n'.format(a=flowMVAFrombus[i],b=flowMVATobus[i],c=flowMVAID[i],d=flowMVAName[i][:-1]))   
    for i in range(len(relay2Name)):
        f.write('psspy.branch_app_r_x_channel([-1,-1,-1,{a},{b}],r"""{c}""",r"""{d}""")\n'.format(a=relay2Frombus[i],b=relay2Tobus[i],c=relay2ID[i],d=relay2Name[i][:-1]))   
    # 19
    for i in range(len(varArr)):
        f.write('psspy.var_channel([-1,{a}],r"""{b}""")\n'.format(a=varArr[i],b=varNameArr[i][:-1]))
    for i in range(len(stateArr)):
        f.write('psspy.state_channel([-1,{a}],r"""{b}""")\n'.format(a=stateArr[i],b=stateNameArr[i][:-1]))
    # 21, psspy.machine_iterm_channel([-1,-1,-1,938044],r"""1""",r"""MACHITERM_VUNGANG3#4""")
    for i in range(len(machItermArr)):
        f.write('psspy.machine_iterm_channel([-1,-1,-1,{a}],r"""1""",r"""{b}""")\n'.format(a=machItermArr[i],b=machItermNameArr[i][:-1]))   
    for i in range(len(machAppIMPArr)):
        f.write('psspy.machine_app_r_x_channel([-1,-1,-1,{a}],r"""1""",r"""{b}""")\n'.format(a=machAppIMPArr[i],b=machAppIMPNameArr[i][:-1]))
    for i in range(len(vuelArr)):
        f.write('psspy.machine_array_channel([-1,12,{a}],r"""1""",r"""{b}""")\n'.format(a=vuelArr[i],b=vuelNameArr[i][:-1]))
    for i in range(len(voelArr)):
        f.write('psspy.machine_array_channel([-1,13,{a}],r"""1""",r"""{b}""")\n'.format(a=voelArr[i],b=voelNameArr[i][:-1]))
    # 25
    for i in range(len(ploadArr)):
        f.write('psspy.load_array_channel([-1,1,{a}],r"""1""",r"""{b}""")\n'.format(a=ploadArr[i],b=ploadNameArr[i][:-1]))
    for i in range(len(qloadArr)):
        f.write('psspy.load_array_channel([-1,2,{a}],r"""1""",r"""{b}""")\n'.format(a=qloadArr[i],b=qloadNameArr[i][:-1]))
    # 27
    for i in range(len(grefArr)):
        f.write('psspy.machine_array_channel([-1,14,{a}],r"""1""",r"""{b}""")\n'.format(a=grefArr[i],b=grefNameArr[i][:-1]))
    for i in range(len(lcrefArr)):
        f.write('psspy.machine_array_channel([-1,15,{a}],r"""1""",r"""{b}""")\n'.format(a=lcrefArr[i],b=lcrefNameArr[i][:-1]))
    for i in range(len(windVelArr)):
        f.write('psspy.machine_array_channel([-1,16,{a}],r"""1""",r"""{b}""")\n'.format(a=windVelArr[i],b=windVelNameArr[i][:-1]))
    for i in range(len(windTurSpdArr)):
        f.write('psspy.machine_array_channel([-1,17,{a}],r"""1""",r"""{b}""")\n'.format(a=windTurSpdArr[i],b=windTurSpdNameArr[i][:-1]))
    for i in range(len(windPitchArr)):
        f.write('psspy.machine_array_channel([-1,18,{a}],r"""1""",r"""{b}""")\n'.format(a=windPitchArr[i],b=windPitchNameArr[i][:-1]))
    for i in range(len(windAeroTorArr)):
        f.write('psspy.machine_array_channel([-1,19,{a}],r"""1""",r"""{b}""")\n'.format(a=windAeroTorArr[i],b=windAeroTorNameArr[i][:-1]))
    for i in range(len(windRotorVolArr)):
        f.write('psspy.machine_array_channel([-1,20,{a}],r"""1""",r"""{b}""")\n'.format(a=windRotorVolArr[i],b=windRotorVolNameArr[i][:-1]))
    for i in range(len(windRotorCurArr)):
        f.write('psspy.machine_array_channel([-1,21,{a}],r"""1""",r"""{b}""")\n'.format(a=windRotorCurArr[i],b=windRotorCurNameArr[i][:-1]))
    for i in range(len(windPComandArr)):
        f.write('psspy.machine_array_channel([-1,22,{a}],r"""1""",r"""{b}""")\n'.format(a=windPComandArr[i],b=windPComandNameArr[i][:-1]))
    for i in range(len(windQComandArr)):
        f.write('psspy.machine_array_channel([-1,23,{a}],r"""1""",r"""{b}""")\n'.format(a=windQComandArr[i],b=windQComandNameArr[i][:-1]))
    for i in range(len(windAuxArr)):
        f.write('psspy.machine_array_channel([-1,24,{a}],r"""1""",r"""{b}""")\n'.format(a=windAuxArr[i],b=windAuxNameArr[i][:-1]))

    num = len(angleArr)+len(pelecArr)+len(qelecArr)+len(etermArr) + len(efdArr)+ len(pmechArr) + len(speedArr) + len(xadifdArr)+ len(ecompArr)+ len(vothsgArr) \
            + len(vrefArr)+ len(bsfreqArr) + len(voltageArr) + len(voltAndAngleArr)+len(flowName) + len(flowPQFrombus) + len(flowMVAFrombus) + len(relay2Frombus) \
            + len(varArr) + len(stateArr) + len(machItermArr) + len(machAppIMPArr) + len(vuelArr) + len(voelArr) + len(ploadArr) + len(qloadArr) + len(grefArr)\
            + len(lcrefArr) + len(windVelArr) + len(windTurSpdArr) + len(windPitchArr) + len(windAeroTorArr) + len(windRotorVolArr) + len(windRotorCurArr)\
            + len(windPComandArr) + len(windQComandArr) + len(windAuxArr) 

    f.write('psspy.snap([{a},{b},{c},{d},{n}],r"""{ssn1}""")\n'.format(a=CONs,b=STATEs,c=VARs,d=ICONs,n=num,ssn1 = ssn1))
    f.write('psspy.strt(0,r"""{gop}""")\n'.format(gop=gop))
    f.write('psspy.snap([{a},{b},{c},{d},{n}],r"""{ssn0}""")\n'.format(a=CONs,b=STATEs,c=VARs,d=ICONs,n=num,ssn0=ssn0))
    f.write('psspy.report_output(4,"",[0,0])\n')
    f.write('psspy.close_report()\n')
    f.close

# tạo file chia đoạn đường dây (line tab)
def createLineTabFile(dirName='',fromBus=0,toBus=0,id2='',voltage=0.0,segments=[]):

    outName = dirName + '\\'+'lineTab.py'
    f = open(outName,'w')
    f.write("import pssepath\n")
    f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
    f.write("sys.path.append(PSSE_LOCATION)\n")
    f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
    f.write("pssepath.add_pssepath(33)\n")
    f.write("import psspy \n")
    # chia 8 đoạn
    if len(segments) == 9:
        midBus1 = segments[4] # 5 
        midBus2 = segments[2] # 3
        midBus3 = segments[1] # 2
        midBus4 = segments[3] # 4
        midBus5 = segments[6] # 7
        midBus6 = segments[5] # 6
        midBus7 = segments[7] # 8
        midBus0 = segments[0] # 1
        midBus8 = segments[8] # 9
        f.write('psspy.ltap({fromBus},{toBus},r"""{id}""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=fromBus,toBus=toBus,id=id2,mid=midBus1,id2=midBus1,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus1,toBus=fromBus,mid=midBus2,id2=midBus2,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus2,toBus=fromBus,mid=midBus3,id2=midBus3,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus1,toBus=midBus2,mid=midBus4,id2=midBus4,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus1,toBus=toBus,mid=midBus5,id2=midBus5,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus1,toBus=midBus5,mid=midBus6,id2=midBus6,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus5,toBus=toBus,mid=midBus7,id2=midBus7,voltage=voltage))

        f.write('psspy.splt({fromBus},{toBus},r"""{id}""", {voltage})\n'.format(fromBus=fromBus,toBus=midBus0,id=1,voltage=voltage))
        f.write('psspy.movebrn({fromBus},{toBus},r"""{id}""", {mid},r"""{id2}""")\n'.format(fromBus=midBus3,toBus=fromBus,id=id2,mid=midBus0,id2=1))
        f.write('psspy.splt({fromBus},{toBus},r"""{id}""", {voltage})\n'.format(fromBus=toBus,toBus=midBus8,id=1,voltage=voltage))
        f.write('psspy.movebrn({fromBus},{toBus},r"""{id}""", {mid},r"""{id2}""")\n'.format(fromBus=midBus7,toBus=toBus,id=1,mid=midBus8,id2=1))

        f.write('psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n')
        f.write('psspy.fdns()\n')
        f.write('psspy.fnsl()\n')
        f.write('psspy.fnsl()\n')
    # chia 16 đoạn
    elif len(segments) == 17:
        midBus0 = segments[0] # 1
        midBus1 = segments[8] # 9 
        midBus2 = segments[4] # 5
        midBus3 = segments[2] # 3
        midBus4 = segments[1] # 2
        midBus5 = segments[3] # 4
        midBus6 = segments[6] # 7
        midBus7 = segments[5] # 6
        midBus8 = segments[7] # 8
        midBus9 = segments[12] # 13
        midBus10 = segments[10] # 11 
        midBus11 = segments[9] # 10
        midBus12 = segments[11] # 12
        midBus13 = segments[14] # 15
        midBus14 = segments[13] # 14
        midBus15 = segments[15] # 16
        midBus16 = segments[16] # 17

        f.write('psspy.ltap({fromBus},{toBus},r"""{id}""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=fromBus,toBus=toBus,id=id2,mid=midBus1,id2=midBus1,voltage=voltage))

        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=fromBus,toBus=midBus1,mid=midBus2,id2=midBus2,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus2,toBus=fromBus,mid=midBus3,id2=midBus3,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus3,toBus=fromBus,mid=midBus4,id2=midBus4,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.0001,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=fromBus,toBus=midBus4,mid=midBus0,id2=0,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus3,toBus=midBus2,mid=midBus5,id2=midBus5,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus2,toBus=midBus1,mid=midBus6,id2=midBus6,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus2,toBus=midBus6,mid=midBus7,id2=midBus7,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus6,toBus=midBus1,mid=midBus8,id2=midBus8,voltage=voltage))

        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus1,toBus=toBus,mid=midBus9,id2=midBus9,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus1,toBus=midBus9,mid=midBus10,id2=midBus10,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus1,toBus=midBus10,mid=midBus11,id2=midBus11,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus10,toBus=midBus9,mid=midBus12,id2=midBus12,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus9,toBus=toBus,mid=midBus13,id2=midBus13,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus9,toBus=midBus13,mid=midBus14,id2=midBus14,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus13,toBus=toBus,mid=midBus15,id2=midBus15,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.9999,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus15,toBus=toBus,mid=midBus16,id2=midBus16,voltage=voltage))
        f.write('psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n')
        f.write('psspy.fdns()\n')
        f.write('psspy.fnsl()\n')
        f.write('psspy.fnsl()\n')
    f.close()

# tạo file chia đoạn khi có middle bus
def createLineTabFile3Bus(dirName='',fromBus=0,middle=0,id1='',toBus=0,id2='',voltage=0.0,segments=[]):

    if len(segments)==17:
        outName = dirName + '\\'+'lineTab.py'
        f = open(outName,'w')
        f.write("import pssepath\n")
        f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
        f.write("sys.path.append(PSSE_LOCATION)\n")
        f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
        f.write("pssepath.add_pssepath(33)\n")
        f.write("import psspy \n")
        midBus0 = segments[0] # 1
        midBus1 = segments[8] # 9 
        midBus2 = segments[4] # 5
        midBus3 = segments[2] # 3
        midBus4 = segments[1] # 2
        midBus5 = segments[3] # 4
        midBus6 = segments[6] # 7
        midBus7 = segments[5] # 6
        midBus8 = segments[7] # 8
        midBus9 = segments[12] # 13
        midBus10 = segments[10] # 11 
        midBus11 = segments[9] # 10
        midBus12 = segments[11] # 12
        midBus13 = segments[14] # 15
        midBus14 = segments[13] # 14
        midBus15 = segments[15] # 16
        midBus16 = segments[16] # 17

        # f.write('psspy.ltap({fromBus},{toBus},r"""{id}""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=fromBus,toBus=toBus,id=id2,mid=midBus1,id2=midBus1,voltage=voltage))

        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=fromBus,toBus=middle,mid=midBus2,id2=midBus2,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus2,toBus=fromBus,mid=midBus3,id2=midBus3,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus3,toBus=fromBus,mid=midBus4,id2=midBus4,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.0001,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=fromBus,toBus=midBus4,mid=midBus0,id2=0,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus3,toBus=midBus2,mid=midBus5,id2=midBus5,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus2,toBus=middle,mid=midBus6,id2=midBus6,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus2,toBus=midBus6,mid=midBus7,id2=midBus7,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus6,toBus=middle,mid=midBus8,id2=midBus8,voltage=voltage))

        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=middle,toBus=toBus,mid=midBus9,id2=midBus9,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=middle,toBus=midBus9,mid=midBus10,id2=midBus10,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=middle,toBus=midBus10,mid=midBus11,id2=midBus11,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus10,toBus=midBus9,mid=midBus12,id2=midBus12,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus9,toBus=toBus,mid=midBus13,id2=midBus13,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus9,toBus=midBus13,mid=midBus14,id2=midBus14,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.5,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus13,toBus=toBus,mid=midBus15,id2=midBus15,voltage=voltage))
        f.write('psspy.ltap({fromBus},{toBus},r"""1""", 0.9999,{mid},r"""{id2}""",{voltage})\n'.format(fromBus=midBus15,toBus=toBus,mid=midBus16,id2=midBus16,voltage=voltage))
        f.write('psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n')
        f.write('psspy.fdns()\n')
        f.write('psspy.fnsl()\n')
        f.write('psspy.fnsl()\n')
    f.close()

# tạo file sub, mon, con để tính giới hạn truyền tải liên miền
def createSubMonConForStaticStability():
    sub = open("savnw_Sub.sub",'w')
    sub.write('DINH NGHIA SUBSYSTEM\n')
    sub.write('-----------------------------------\n')
    sub.write('SUBSYSTEM NGUON-BAC\n')
    sub.write('AREA 16\n')
    sub.write('AREA 17\n')
    sub.write('END\n')
    sub.write('------------------------------------\n')
    sub.write('SUBSYSTEM NGUON-BACTRUNG\n')
    sub.write('AREA 16\n')
    sub.write('AREA 17\n')
    sub.write('AREA 26\n')
    sub.write('AREA 27\n')
    sub.write('AREA 28\n')
    sub.write('END\n')
    sub.write('------------------------------------\n')
    sub.write('SUBSYSTEM NGUON-TRUNG\n')
    sub.write('AREA 26\n')
    sub.write('AREA 27\n')
    sub.write('AREA 28\n')
    sub.write('END\n')
    sub.write('\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM NGUON-NAM\n')
    sub.write('AREA 36\n')
    sub.write('AREA 37\n')
    sub.write('AREA 38\n')
    sub.write('AREA 60\n')
    sub.write('AREA 61\n')
    sub.write('AREA 62\n')
    sub.write('END\n')
    sub.write('------------------------------------\n')
    sub.write('SUBSYSTEM NGUON-TRUNGNAM\n')
    sub.write('AREA 26\n')
    sub.write('AREA 27\n')
    sub.write('AREA 28\n')
    sub.write('AREA 36\n')
    sub.write('AREA 37\n')
    sub.write('AREA 38\n')
    sub.write('AREA 60\n')
    sub.write('AREA 61\n')
    sub.write('AREA 62\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM NGUON-VN\n')
    sub.write('AREA 16\n')
    sub.write('AREA 17\n')
    sub.write('AREA 26\n')
    sub.write('AREA 27\n')
    sub.write('AREA 28\n')
    sub.write('AREA 36\n')
    sub.write('AREA 37\n')
    sub.write('AREA 38\n')	
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM LUOI-BAC\n')
    sub.write('AREA 10\n')
    sub.write('AREA 11\n')
    sub.write('AREA 12\n')
    sub.write('AREA 15\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM LUOI-BACTRUNG\n')
    sub.write('AREA 10\n')
    sub.write('AREA 11\n')
    sub.write('AREA 12\n')
    sub.write('AREA 15\n')
    sub.write('AREA 20\n')
    sub.write('AREA 21\n')
    sub.write('AREA 22\n')
    sub.write('AREA 25\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('\n')
    sub.write('SUBSYSTEM LUOI-TRUNG\n')
    sub.write('AREA 20\n')
    sub.write('AREA 21\n')
    sub.write('AREA 22\n')
    sub.write('AREA 25\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM LUOI-NAM\n')
    sub.write('AREA 30\n')
    sub.write('AREA 31\n')
    sub.write('AREA 32\n')
    sub.write('AREA 35\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('\n')
    sub.write('SUBSYSTEM LUOI-TRUNGNAM\n')
    sub.write('AREA 20\n')
    sub.write('AREA 21\n')
    sub.write('AREA 22\n')
    sub.write('AREA 25\n')
    sub.write('AREA 30\n')
    sub.write('AREA 31\n')
    sub.write('AREA 32\n')
    sub.write('AREA 35\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('\n')
    sub.write('SUBSYSTEM LUOI-VN\n')
    sub.write('AREA 10\n')
    sub.write('AREA 11\n')
    sub.write('AREA 12\n')
    sub.write('AREA 15\n')
    sub.write('AREA 20\n')
    sub.write('AREA 21\n')
    sub.write('AREA 22\n')
    sub.write('AREA 25\n')
    sub.write('AREA 30\n')
    sub.write('AREA 31\n')
    sub.write('AREA 32\n')
    sub.write('AREA 35\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM HT-BAC\n')
    sub.write('AREAS 10 11\n')
    sub.write(' JOIN "GROUP 1"\n')
    sub.write(' AREAS 12 15\n')
    sub.write(' AREAS 16 17\n')
    sub.write(' END\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM HT-TRUNG\n')
    sub.write('AREAS 20 21\n')
    sub.write(' JOIN "GROUP 2"\n')
    sub.write(' AREAS 22 25\n')
    sub.write(' AREAS 26 27\n')
    sub.write(' END\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('SUBSYSTEM HT-NAM\n')
    sub.write('AREAS 30 31\n')
    sub.write(' JOIN "GROUP 3"\n')
    sub.write(' AREAS 32 35\n')
    sub.write(' AREAS 36 37\n')
    sub.write(' END\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('\n')
    sub.write('SUBSYSTEM LUOI-CAM\n')
    sub.write(' AREA 33\n')
    sub.write('END\n')
    sub.write('---------------------------------\n')
    sub.write('\n')
    sub.write('SUBSYSTEM LUOI-VN-TT\n')
    sub.write('AREAS 12 15\n')
    sub.write(' JOIN "GROUP 7"\n')
    sub.write(' AREAS 22 25\n')
    sub.write(' AREAS 32 35\n')
    sub.write('\n')
    sub.write(' END\n')
    sub.write('END\n')
    sub.write('\n')
    sub.write('END\n')
    sub.close()
    ################### Mon
    mon = open("savnw_Mon.mon",'w')
    mon.write('MONITOR BRANCHES\n')
    mon.write('38060 38061\n')
    mon.write('38060 38062\n')
    mon.write('38060 38050 1\n')
    mon.write('38060 38050 2\n')
    mon.write('38070 37010 1\n')
    mon.write('38070 37010 2\n')
    mon.write('33030 34060 1\n')
    mon.write('33030 23230 1\n')
    mon.write('36020 33030 1\n')
    mon.write('36010 36020 1\n')
    mon.write('238017 251019\n')
    mon.write('238060 251017 1\n')
    mon.write('60090 60093\n')
    mon.write('60050 76162 1\n')
    mon.write('60050 76164 1\n')
    mon.write('57010 57011\n')
    mon.write('60050 74010 1\n')
    mon.write('60050 74010 2\n')
    mon.write('257010 273023 1\n')
    mon.write('257010 257031 1\n')
    # mon.write(';33030 33031 1\n')
    # mon.write(';33030 33033 1\n')
    # mon.write(';38050 38052 1\n')
    # mon.write(';38050 38054 1\n')
    # mon.write(';38060 38050 1\n')
    # mon.write(';38051 53254 1\n')
    # mon.write(';38061 53252 1\n')
    # mon.write(';53070 53253 1\n')
    # mon.write(';54010 53251 1\n')
    # mon.write(';60094 53070 1\n')
    # mon.write(';60092 54010 1\n')
    # mon.write(';57011 77010 1\n')
    # mon.write(';60093 70132 1\n')
    # mon.write(';70131 76150 1\n')
    # mon.write(';76160 77010 1\n')
    # mon.write(';60095 76160 1\n')
    # mon.write(';60095 76160 2\n')
    # mon.write(';57011 77010 1\n')
    # mon.write(';60093 70132 1\n')
    # mon.write(';257010 273011 2\n')
    # mon.write(';257010 273011 1\n')
    # mon.write(';53252 38061\n') 
    # mon.write(';53254 38051\n')
    # mon.write(';238060 250005 1\n')
    # mon.write(';238017 250019 1\n')
    # mon.write('\n')
    # mon.write(';285031 285039 1\n')
    # mon.write(';285031 285039 2\n')
    mon.write('\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE CAMPHUCHIA1 RATING 5 MW\n')
    mon.write('MONITOR TIES FROM AREA 32 TO AREA 33\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE CAMPHUCHIA2 RATING 5 MW\n')
    mon.write('MONITOR TIES FROM AREA 33 TO AREA 32\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE CAMPHUCHIA3 RATING 5 MW\n')
    mon.write('285031 285039 1\n')
    mon.write('285031 285039 2\n')
    mon.write('END\n')
    mon.write('\n')
    mon.write('------------------------------------------\n')
    mon.write('; MONITOR INTERFACE BAC->TRUNG1 RATING 10 MW\n')
    mon.write('; MONITOR TIES FROM AREA 15 TO AREA 25\n')
    mon.write('; END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE BAC->TRUNG2 RATING 10 MW\n')
    mon.write('MONITOR TIES FROM SUBSYSTEM LUOI-BAC TO SUBSYSTEM LUOI-TRUNG\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE BAC<-TRUNG3 RATING 10 MW\n')
    mon.write('MONITOR TIES FROM SUBSYSTEM LUOI-TRUNG TO SUBSYSTEM LUOI-BAC\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE DSOI->DNANG RATING 5 MW\n')
    mon.write('53070 53253 1\n')
    mon.write('54010 53251 1\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE TRUNG->NAM1 RATING 10 MW\n')
    mon.write('60095 76160 1\n')
    mon.write('60095 76160 2\n')
    mon.write('57011 77010 1\n')
    mon.write('60093 70132 1\n')
    mon.write('257010 273011 1\n')
    mon.write('257010 273011 2\n')
    mon.write('262017 270011 1\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('MONITOR INTERFACE TRUNG->NAM2 RATING 10 MW\n')
    mon.write('MONITOR TIES FROM SUBSYSTEM LUOI-TRUNG TO SUBSYSTEM LUOI-NAM\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 36020 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 38060 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 38050 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 32010 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 36010 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 33030 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 32010 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 31010 1\n')
    mon.write('MONITOR VOLTAGE RANGE BUS 38070 1\n')
    mon.write('\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('\n')
    mon.write('MONITOR VOLTAGE DEVIATION KV 500 1\n')
    mon.write('END\n')
    mon.write('------------------------------------------\n')
    mon.write('\n')
    mon.write('END\n')
    mon.close()
    ######################## con file
    con = open("savnw_Con.con",'w')
    con.write('CONTINGENCY VUNGANG-HATINH\n')
    con.write('TRIP LINE FROM BUS 38060 TO BUS 38050\n')
    con.write('END\n')
    con.write('\n')
    con.write('CONTINGENCY HATINH-NGHISON\n')
    con.write('TRIP LINE FROM BUS 38050 TO BUS 36010\n')
    con.write('END\n')
    con.write('\n')
    con.write('CONTINGENCY QUYNHLAP-THANHHOA\n')
    con.write('TRIP LINE FROM BUS 37010 TO BUS 36020\n')
    con.write('END\n')
    con.write('\n')
    con.write('CONTINGENCY THANHHOA-NAMDINH\n')
    con.write('TRIP LINE FROM BUS 36020 TO BUS 32010\n')
    con.write('END\n')
    con.write('\n')
    con.write('CONTINGENCY VUNGANG3-QUYNHLAP\n')
    con.write('TRIP LINE FROM BUS 38070 TO BUS 37010\n')
    con.write('END\n')
    con.write('\n')
    con.write('END\n')
    con.close()

# tạo file python tạo sự cố từ file python sự cố đã có
def createIncidentFile(pyFile):
    dirname = os.path.dirname(pyFile)
    path = os.path.join(dirname,'dynamic_process.py')
    prgfile = '{}.txt'.format(pyFile[:-3])
    outfile = dirname + '\\gop.out'
    outfile1 = '{}.out'.format(pyFile[:-3])
    f = open(path,'w')
    f.write("from __future__ import with_statement\n")
    f.write("from __future__ import division\n")
    f.write("from contextlib import contextmanager\n")
    f.write("import os, sys\n")

    f.write("import pssepath\n")
    # f.write("import pssepy\n")
    f.write("import shutil\n")
    f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
    f.write("sys.path.append(PSSE_LOCATION)\n")
    f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
    f.write("pssepath.add_pssepath(33)\n")
    f.write("from psspy import *\n")
    f.write("import redirect\n")
    f.write("from math import *\n")
    f.write("from csv import *\n")

    f.write("from dyntools import *\n")
    f.write("_i = getdefaultint()\n")
    f.write("_f = getdefaultreal()\n")
    f.write("_s = getdefaultchar()\n")
    f.write("psseinit(50000)\n")
    f.write("def get_nchan():\n")
    f.write("    N = 1000\n")
    f.write("    ierr, rval = psspy.chnval(N)\n")
    f.write("    while ierr == 2:\n")
    f.write("        N   -= 1\n")
    f.write("        ierr, rval = psspy.chnval(N)\n")
    f.write("    return N\n")
    f.write("psspy.dynamicsmode(1)\n")

    r = open(pyFile,'r')
    for line in r:
        if 'gop.out' in line:
            line = line.replace('gop.out',outfile)
        f.write(line)
    r.close()

    f.write("nchan = get_nchan()\n")
    f.write("nchan += 1\n")
    f.write('chnobj = CHNF(r"""{}""")\n'.format(outfile))
    f.write('chnobj.txtout(channels = range(1,nchan),txtfile = r"""{}""")\n'.format(prgfile))
    f.write("shutil.copy(r'{a}',r'{b}')\n".format(a=outfile,b=outfile1))
    # f.write("psspy.delete_all_plot_channels()\n")
    f.close()

# tạo file dyn2.py từ dyn2.idv
def createIDVFile(dyrPath, channel, relang):
    
    dirname = os.path.dirname(dyrPath)
    idv2py = os.path.join(dirname,'idv2py.py')
    outname = os.path.join(dirname,'sme.sav')
    cc1name =  dirname + '\\'+ 'CC1'
    ct1name =  dirname + '\\'+ 'CT1'
    cmp1name =  dirname + '\\'+ 'CMP1'

    f = open(idv2py,'w')
    f.write("from __future__ import with_statement\n")
    f.write("from __future__ import division\n")
    f.write("from contextlib import contextmanager\n")
    f.write("import os, sys\n")

    f.write("import pssepath\n")
    f.write("import psspy\n")
    f.write("import shutil\n")
    f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
    f.write("sys.path.append(PSSE_LOCATION)\n")
    f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
    f.write("pssepath.add_pssepath(33)\n")
    f.write("from psspy import *\n")
    f.write("import redirect\n")
    f.write("from math import *\n")
    f.write("from csv import *\n")

    f.write("from dyntools import *\n")
    f.write("_i = getdefaultint()\n")
    f.write("_f = getdefaultreal()\n")
    f.write("_s = getdefaultchar()\n")
    f.write("psseinit(50000)\n")
    f.write("def get_nchan():\n")
    f.write("    N = 1000\n")
    f.write("    ierr, rval = psspy.chnval(N)\n")
    f.write("    while ierr == 2:\n")
    f.write("        N   -= 1\n")
    f.write("        ierr, rval = psspy.chnval(N)\n")
    f.write("    return N\n")
    f.write("psspy.dynamicsmode(1)\n")
    f.write("psspy.fnsl()\n")
    f.write("psspy.fnsl()\n")
    f.write("psspy.fnsl()\n")
    f.write("psspy.ordr(0)\n")
    f.write("psspy.fnsl()\n")
    f.write("psspy.conl(0,1,1,STATUS1=0)\n")
    f.write("psspy.conl(1,1,2,LOADIN1 = 100.0,LOADIN2 = 0.0,LOADIN3 = 0.0,LOADIN4=100.0)\n")
    f.write("psspy.conl(1,1,3)\n")
    f.write("psspy.cong(0)\n")
    f.write("psspy.ordr(0)\n")
    f.write("psspy.fact()\n")
    f.write("psspy.tysl(0)\n")
    f.write("psspy.save(r'{out}')\n".format(out=outname))
    f.write("psspy.fact()\n")
    f.write("psspy.dynamicsmode(0)\n")
    f.write("psspy.dyre_new([1,1,1,1],r'{dyr}',r'{cc1}',r'{ct1}',r'{cmp1}' )\n".format(dyr=dyrPath,cc1=cc1name,ct1=ct1name,cmp1=cmp1name))
    f.write("psspy.set_relang(1,{},'')\n".format(relang))
    # angle
    if len(channel['angle']['angleArr'])!=0:
        for i in range(len(channel['angle']['angleArr'])):
            f.write('psspy.machine_array_channel([-1,1,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['angle']['angleArr'][i],b=channel['angle']['angleNameArr'][i][:-1]))
    # pelec
    if len(channel['pelec']['pelecArr'])!=0:
        for i in range(len(channel['pelec']['pelecArr'])):
            f.write('psspy.machine_array_channel([-1,2,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['pelec']['pelecArr'][i],b=channel['pelec']['pelecNameArr'][i][:-1]))
    # qelec
    if len(channel['qelec']['qelecArr'])!=0:
        for i in range(len(channel['qelec']['qelecArr'])):
            f.write('psspy.machine_array_channel([-1,3,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['qelec']['qelecArr'][i],b=channel['qelec']['qelecNameArr'][i][:-1]))
    # eterm
    if len(channel['eterm']['etermArr'])!=0:
        for i in range(len(channel['eterm']['etermArr'])):
            f.write('psspy.machine_array_channel([-1,4,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['eterm']['etermArr'][i],b=channel['eterm']['etermNameArr'][i][:-1]))
    # efd
    if len(channel['efd']['efdArr'])!=0:
        for i in range(len(channel['efd']['efdArr'])):
            f.write('psspy.machine_array_channel([-1,5,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['efd']['efdArr'][i],b=channel['efd']['efdNameArr'][i][:-1]))
    # pmech
    if len(channel['pmech']['pmechArr'])!=0:
        for i in range(len(channel['pmech']['pmechArr'])):
            f.write('psspy.machine_array_channel([-1,6,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['pmech']['pmechArr'][i],b=channel['pmech']['pmechNameArr'][i][:-1]))
    # speed
    if len(channel['speed']['speedArr'])!=0:
        for i in range(len(channel['speed']['speedArr'])):
            f.write('psspy.machine_array_channel([-1,7,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['speed']['speedArr'][i],b=channel['speed']['speedNameArr'][i][:-1]))
    # xadifd
    if len(channel['xadifd']['xadifdArr'])!=0:
        for i in range(len(channel['xadifd']['xadifdArr'])):
            f.write('psspy.machine_array_channel([-1,8,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['xadifd']['xadifdArr'][i],b=channel['xadifd']['xadifdNameArr'][i][:-1]))
    # ecomp
    if len(channel['ecomp']['ecompArr'])!=0:
        for i in range(len(channel['ecomp']['ecompArr'])):
            f.write('psspy.machine_array_channel([-1,9,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['ecomp']['ecompArr'][i],b=channel['ecomp']['ecompNameArr'][i][:-1]))
    # vothsg
    if len(channel['vothsg']['vothsgArr'])!=0:
        for i in range(len(channel['vothsg']['vothsgArr'])):
            f.write('psspy.machine_array_channel([-1,10,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['vothsg']['vothsgArr'][i],b=channel['vothsg']['vothsgNameArr'][i][:-1]))
    # vref
    if len(channel['vref']['vrefArr'])!=0:
        for i in range(len(channel['vref']['vrefArr'])):
            f.write('psspy.machine_array_channel([-1,11,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['vref']['vrefArr'][i],b=channel['vref']['vrefNameArr'][i][:-1]))
    # bsfreq
    if len(channel['bsfreq']['bsfreqArr'])!=0:
        for i in range(len(channel['bsfreq']['bsfreqArr'])):
            f.write('psspy.bus_frequency_channel([-1,{a}],r"""{b}""")\n'.format(a=channel['bsfreq']['bsfreqArr'][i],b=channel['bsfreq']['bsfreqNameArr'][i][:-1]))
    # voltage
    if len(channel['voltage']['voltageArr'])!=0:
        for i in range(len(channel['voltage']['voltageArr'])):
            f.write('psspy.voltage_channel([-1,-1,-1,{a}],r"""{b}""")\n'.format(a=channel['voltage']['voltageArr'][i],b=channel['voltage']['voltageNameArr'][i][:-1]))
    # volang
    if len(channel['volang']['volangArr'])!=0:
        for i in range(len(channel['volang']['volangArr'])):
            f.write('psspy.voltage_and_angle_channel([-1,-1,-1,{a}],r"""{b}""")\n'.format(a=channel['volang']['volangArr'][i],b=channel['volang']['volangNameArr'][i][:-1]))
    # var
    if len(channel['var']['varArr'])!=0:
        for i in range(len(channel['var']['varArr'])):
            f.write('psspy.var_channel([-1,{a}],r"""{b}""")\n'.format(a=channel['var']['varArr'][i],b=channel['var']['varNameArr'][i][:-1]))
    # state
    if len(channel['state']['stateArr'])!=0:
        for i in range(len(channel['state']['stateArr'])):
            f.write('psspy.state_channel([-1,{a}],r"""{b}""")\n'.format(a=channel['state']['stateArr'][i],b=channel['state']['stateNameArr'][i][:-1]))
    # machineterm
    if len(channel['machineterm']['machinetermArr'])!=0:
        for i in range(len(channel['machineterm']['machinetermArr'])):
            f.write('psspy.machine_iterm_channel([-1,-1,-1,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['machineterm']['machinetermArr'][i],b=channel['machineterm']['machinetermNameArr'][i][:-1]))
    # machappimp
    if len(channel['machappimp']['machappimpArr'])!=0:
        for i in range(len(channel['machappimp']['machappimpArr'])):
            f.write('psspy.machine_app_r_x_channel([-1,-1,-1,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['machappimp']['machappimpArr'][i],b=channel['machappimp']['machappimpNameArr'][i][:-1]))
    # vuel
    if len(channel['vuel']['vuelArr'])!=0:
        for i in range(len(channel['vuel']['vuelArr'])):
            f.write('psspy.machine_array_channel([-1,12,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['vuel']['vuelArr'][i],b=channel['vuel']['vuelNameArr'][i][:-1]))
    # voel
    if len(channel['voel']['voelArr'])!=0:
        for i in range(len(channel['voel']['voelArr'])):
            f.write('psspy.machine_array_channel([-1,13,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['voel']['voelArr'][i],b=channel['voel']['voelNameArr'][i][:-1]))
    # pload
    if len(channel['pload']['ploadArr'])!=0:
        for i in range(len(channel['pload']['ploadArr'])):
            f.write('psspy.load_array_channel([-1,1,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['pload']['ploadArr'][i],b=channel['pload']['ploadNameArr'][i][:-1]))
    # qload
    if len(channel['qload']['qloadArr'])!=0:
        for i in range(len(channel['qload']['qloadArr'])):
            f.write('psspy.load_array_channel([-1,2,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['qload']['qloadArr'][i],b=channel['qload']['qloadNameArr'][i][:-1]))
    # gref
    if len(channel['gref']['grefArr'])!=0:
        for i in range(len(channel['gref']['grefArr'])):
            f.write('psspy.machine_array_channel([-1,14,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['gref']['grefArr'][i],b=channel['gref']['grefNameArr'][i][:-1]))
    # lcref
    if len(channel['lcref']['lcrefArr'])!=0:
        for i in range(len(channel['lcref']['lcrefArr'])):
            f.write('psspy.machine_array_channel([-1,15,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['lcref']['lcrefArr'][i],b=channel['lcref']['lcrefNameArr'][i][:-1]))
    # windvel
    if len(channel['windvel']['windvelArr'])!=0:
        for i in range(len(channel['windvel']['windvelArr'])):
            f.write('psspy.machine_array_channel([-1,16,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windvel']['windvelArr'][i],b=channel['windvel']['windvelNameArr'][i][:-1]))
    # windturspd
    if len(channel['windturspd']['windturspdArr'])!=0:
        for i in range(len(channel['windturspd']['windturspdArr'])):
            f.write('psspy.machine_array_channel([-1,17,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windturspd']['windturspdArr'][i],b=channel['windturspd']['windturspdNameArr'][i][:-1]))
    # windpitch
    if len(channel['windpitch']['windpitchArr'])!=0:
        for i in range(len(channel['windpitch']['windpitchArr'])):
            f.write('psspy.machine_array_channel([-1,18,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windpitch']['windpitchArr'][i],b=channel['windpitch']['windpitchNameArr'][i][:-1]))
    # windaerotor
    if len(channel['windaerotor']['windaerotorArr'])!=0:
        for i in range(len(channel['windaerotor']['windaerotorArr'])):
            f.write('psspy.machine_array_channel([-1,19,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windaerotor']['windaerotorArr'][i],b=channel['windaerotor']['windaerotorNameArr'][i][:-1]))
    # windrotorvol
    if len(channel['windrotorvol']['windrotorvolArr'])!=0:
        for i in range(len(channel['windrotorvol']['windrotorvolArr'])):
            f.write('psspy.machine_array_channel([-1,20,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windrotorvol']['windrotorvolArr'][i],b=channel['windrotorvol']['windrotorvolNameArr'][i][:-1]))
    # windrotorcur
    if len(channel['windrotorcur']['windrotorcurArr'])!=0:
        for i in range(len(channel['windrotorcur']['windrotorcurArr'])):
            f.write('psspy.machine_array_channel([-1,21,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windrotorcur']['windrotorcurArr'][i],b=channel['windrotorcur']['windrotorcurNameArr'][i][:-1]))
    # windpcomand
    if len(channel['windpcomand']['windpcomandArr'])!=0:
        for i in range(len(channel['windpcomand']['windpcomandArr'])):
            f.write('psspy.machine_array_channel([-1,22,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windpcomand']['windpcomandArr'][i],b=channel['windpcomand']['windpcomandNameArr'][i][:-1]))
    # windqcomand
    if len(channel['windqcomand']['windqcomandArr'])!=0:
        for i in range(len(channel['windqcomand']['windqcomandArr'])):
            f.write('psspy.machine_array_channel([-1,23,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windqcomand']['windqcomandArr'][i],b=channel['windqcomand']['windqcomandNameArr'][i][:-1]))
    # windaux
    if len(channel['windaux']['windauxArr'])!=0:
        for i in range(len(channel['windaux']['windauxArr'])):
            f.write('psspy.machine_array_channel([-1,24,{a}],r"""1""",r"""{b}""")\n'.format(a=channel['windaux']['windauxArr'][i],b=channel['windaux']['windauxNameArr'][i][:-1]))

    gop = dirname+'\\gop.out'
    f.write('psspy.strt(0,r"""{gop}""")\n'.format(gop=gop))
    f.write('psspy.report_output(4,"",[0,0])\n')
    f.write('psspy.close_report()\n')
    f.close
    return idv2py

