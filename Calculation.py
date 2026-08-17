# -*- coding: utf-8 -*- 
from DialogBox import getInput, openFile, openFolder, saveFile
from Create_Sub_Mon_Con_Files import createSubFile, createMonFile, createConFile,createAutoFile,createDyn22File
from Create_Sub_Mon_Con_Files import createAutoStaticFile,createLineTabFile,createLineTabFile3Bus,createSubMonConForStaticStability,createIncidentFile
from dialogSubSystem import Select_Source_Sink
from dialogChooseIDVFile import Select_Idv_File
from createIDVFile import Create_New_Idv
from dialogSimulationOption import Simulation_option
from lineTapDialog import Line_Tab
from lineTabShuntRector import Line_Tab_Shunt_Reactor
from chooseBusZoneAreaDialog import Choose_Bus_Zone_Area
from chooseBusDialog import Choose_Bus
import codecs, glob, os, sys
import pssepath
import wx
import wx.xrc
import pssarrays
from subprocess import call
from openpyxl import load_workbook
from Tool_V2 import MyFrame1
from n1_sav import as_text, apply_outage, resolve_contingency, safe_filename, three_winding_inventory
import dyntools
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
from redirectOuput import silence
# import docx
from docx.enum.section import WD_ORIENT
from docx.shared import Pt
import pandas as pd
from ui_performance import profiled

class Calculation(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.Path = ''
        self.PathFile = [[]]
        self.parent = parent
        self.PathOrigin = ''
        self.matrixBus = []
        self.matrixArea = []
        self.matrixZone = []
        self.matrixGen = []
        self.indexFile = 0

    # tính contingency, tạo mới sub, mon, con file
    def Create_New_DFX_Fcn( self, event ):
        PATH = self.Path
        PATHFILE = self.PathFile
        areaListFull = []
        for i in range(len(self.matrixArea[self.indexFile])):
            areaListFull.append(str(self.matrixArea[self.indexFile][i,0])+'-'+str(self.matrixArea[self.indexFile][i,1]))
        zoneListFull = []
        for i in range(len(self.matrixZone[self.indexFile])):
            zoneListFull.append(str(self.matrixZone[self.indexFile][i,0])+'-'+str(self.matrixZone[self.indexFile][i,1]))  
        busListFull = []
        for i in range(len(self.matrixBus[self.indexFile])):
            busListFull.append(str(self.matrixBus[self.indexFile][i,0])+'-'+str(self.matrixBus[self.indexFile][i,1]))
        
        # tạo dialog để người dùng chọn bus, zone, area
        dialog = Choose_Bus_Zone_Area(self.parent)
        dialog.lbArea.SetItems(areaListFull)
        dialog.lbZone.SetItems(zoneListFull)
        dialog.lbBus.SetItems(busListFull)
        dialog.lbAreaChoices = areaListFull
        dialog.lbZoneChoices = zoneListFull
        dialog.lbBusChoices = busListFull
        dialog.ShowModal()

        # trả về list của area, zone và bus number  được chọn
        [areaList,zoneList,busNumberList] = dialog.ContigencyCalculation(event )

        if PATH <> '':   
            dirName = openFolder(self,"Choose the folder contain sub, mon, con files." )
            
            if dialog.flag == 1:
                # tạo file sub, mon, con
                createSubFile(dirName,zoneList,areaList)
                createMonFile(dirName,busNumberList)
                createConFile(dirName)

                dDir = os.path.dirname(self.PathOrigin)
                dFile = os.path.basename(self.PathOrigin[0:-4])
                wildcard = "PSS/E files (*.acc)|*.acc|All files|*"
                # outputPath = saveFile(self,"Output file name:",wildcard, dDir,dFile)
                outputPath = self.PathOrigin[0:-4]+'.acc'

                if ( outputPath <> ''):
                    os.chdir(dirName)
                    for file in glob.glob("*.sub"):
                        subFile = dirName +'\\'+ file
                        monFile = dirName +'\\'+ file[0:-4] + '.mon'
                        conFile = dirName +'\\'+ file[0:-4] + '.con'
                        dfxFile = dirName +'\\'+ file[0:-4] + '.dfx'
                        psspy.dfax([1,1], subFile, monFile,conFile,dfxFile)
                        psspy.accc_with_dsp( 0.5,[2,0,0,1,1,1,0,0],file[0:-4],dfxFile,outputPath,"","")

                        wx.MessageBox("AC Contingency analysis results {a} are ready for graphical display".format(a=outputPath))
                # tính toán contingency cho file được chọn
            else:
                event.Skip()
        else:
            wx.MessageBox("Please open an existing case first!")

    # tính contingency chọn từ file có sẵn
    def Choose_Available_DFX_Fcn( self, event ):
        PATH = self.PathOrigin
        PATHFILE = self.PathFile
        if PATH != '':   
            dirNameOrigin = openFile(self,'Choose the created sub/mon/con files', "Sub/Mon/Con files (*.sub)|*.sub|*.mon|*.con|All files|*")
            dirName = os.path.dirname(dirNameOrigin)
            dDir = os.path.dirname(PATH)
            dFile = os.path.basename(PATH)
            wildcard = "PSS/E files (*.acc)|*.acc|All files|*"
            outputPath =  PATH[:-4]+'.acc' 

            if ( outputPath != ''):
                os.chdir(dirName)
                for file in glob.glob("*.sub"):
                    subFile = dirName +'\\'+ file
                    monFile = dirName +'\\'+ file[0:-4] + '.mon'
                    conFile = dirName +'\\'+ file[0:-4] + '.con'
                    dfxFile = dirName +'\\'+ file[0:-4] + '.dfx'
                    psspy.dfax([1,1], subFile, monFile,conFile,dfxFile)
                    psspy.accc_with_dsp( 0.5,[2,0,0,1,1,1,0,0],file[0:-4],dfxFile,outputPath,"","")
                    rlst = pssarrays.accc_summary(outputPath)
                    wx.MessageBox("AC Contingency analysis results {a} are ready for graphical display".format(a=outputPath))
        else:
            wx.MessageBox("Please open an existing case first!")

    # tính contingency tự động cho tất cả các file
    def Auto_Contigencies_Fcn( self, event ):
        psspy.psseinit(2000)
        PATH = self.Path
        PATHFILE = self.PathFile
        dirName = openFolder(self,'Choose the Folder contain all sav and sub,mon,con files')
        # tạo file python tự động
        createAutoFile(dirName)
        pyPath = os.path.join(dirName,'autoContigency.py')
        # thực thi file python tự động
        execfile(pyPath)
        wx.MessageBox("Calculation Finish!")

    # tính toán ngắn mạch phân bố
    def Distribution_Short_Circuit_Cal_Fcn(self,event):
        dirName = os.path.dirname(self.PathOrigin)
        busNum = []
        for i in range(len(self.matrixBus[self.indexFile][:,0])):
            busNum.append(str(self.matrixBus[self.indexFile][i,0])+'-'+self.matrixBus[self.indexFile][i,1])

        # tạo dialog để người dùng nhập các giá trị input như from bus, to bus, id, số đoạn chia
        dialog = Line_Tab(self.parent)
        dialog.fromBus.SetItems(map(str,busNum))
        dialog.Middle.SetItems(map(str,busNum))
        dialog.toBus.SetItems(map(str,busNum))
        dialog.ShowModal()

        if dialog.flag == 1:
            result = dialog.Next(event)
            
            [fromBus,middle,id1,toBus,id2,segments,tabLineType] = result
            ierr,voltage = psspy.busdat(int(fromBus),'BASE')
            # chia 8 đoạn
            if tabLineType == 2:    
                ierr, rval = psspy.brncur(fromBus,toBus,id2)
                if ierr == 1:
                    wx.MessageBox('Bus not found')
                elif ierr == 2:
                    wx.MessageBox('Branch not found')
                elif ierr == 3:
                    wx.MessageBox('Branch out of service')
                else:
                    segmentsBus = []
                    count =0
                    for i in range(1,1000):
                        if not i in busNum:
                            segmentsBus.append(i)
                        if count < segments:
                            count+=1
                        else:
                            break
                    # tạo file python thực hiện chức năng line tab, chia đường dây thành 8/16 đoạn như yêu cầu
                    createLineTabFile(dirName,fromBus,toBus,id2,voltage,segmentsBus)
                    pyPath = os.path.join(dirName,'lineTab.py')
                    # thực thi file linetab, hoàn thành việc chia đoạn đường dây
                    execfile(pyPath)

                    # ngắn mạch tóm tắt
                    with open('output', 'w') as f, silence(f):
                        psspy.bsys(1,0,[0.0,0.0],0,[],segments+1,segmentsBus,0,[],0,[])
                        psspy.ascc(1,0,[1,0,0,0,1,3,0,0,0,0],"","")
                    r = open('output','r')
                    lines = r.readlines()
                    if middle != "":
                        outName = os.path.basename(self.PathOrigin)[0:-4]+'-{a}-{b}-{c}'.format(a = fromBus,b=middle,c=toBus)
                    else:
                        outName = os.path.basename(self.PathOrigin)[0:-4]+'-{a}-{c}'.format(a = fromBus,c=toBus)

                    fileName = dirName+"\\{}-tomtat.txt".format(outName)
                    f = open(fileName,'w')
                    flag = 0
                    resultLine = 0

                    for line,value in enumerate(lines):
                        if 'ONE PHASE' in value:
                            flag = 1
                            resultLine = line
                        if flag == 1:
                            f.writelines(value)
                    result = ''
                    for i in range(resultLine,len(lines)-1):
                        result = result +'\n'+ lines[i]

                    wx.MessageBox('Result  is:{A}\n '.format(A=result))
                    r.close()
                    os.remove("output")
                    f.close()
                    wx.MessageBox("Result has been saved in {b}.".format(b=fileName))

                    # ngắn mạch chi tiết
                    with open('output', 'w') as f, silence(f):
                        psspy.bsys(1,0,[0.0,0.0],0,[],segments+1,segmentsBus,0,[],0,[])
                        psspy.ascc(1,0,[1,0,0,0,1,2,0,1,0,0],"","")
                    r = open('output','r')
                    lines = r.readlines()

                    if middle != "":
                        outName = os.path.basename(self.PathOrigin)[0:-4]+'-{a}-{b}-{c}'.format(a = fromBus,b=middle,c=toBus)
                    else:
                        outName = os.path.basename(self.PathOrigin)[0:-4]+'-{a}-{c}'.format(a = fromBus,c=toBus)

                    fileName = dirName+"\\{}-chitiet.txt".format(outName)
                    f = open(fileName,'w')
                    flag = 0
                    newarr = []
                    name = []
                    voltage = []
                    onePhase = []
                    threePhase = []
                    right = []
                    rightBus = []

                    for line,value in enumerate(lines):
                        if 'PSS(R)E  SHORT  CIRCUIT  OUTPUT' in value:
                            flag = 1
                        if flag == 1:
                            f.writelines(value)
                            params = value.split()

                            if 'AT BUS' in value:
                                newarr.append(params[2])
                                name.append(params[3])
                                voltage.append(params[4])

                            if 'AMP/OHM' in value:
                                right.append(params[11])
                                rightBus.append(params[0])

                            if 'TOTAL  FAULT  CURRENT' in value:
                                onePhase.append(params[6])
                                threePhase.append(params[4])
                    # tạo mảng chứa các giá trị resume
                    s1 = s2 = s3 = s4 = s5 = s6 = ''
                    for i in range(len(newarr)):
                        if i == 0:
                            s1 = s1+str(newarr[i]).ljust(9,' ') # Mã bus đang quan sát
                            s2 = s2+str(rightBus[2*i+1]).ljust(9,' ') # From bus của bus quan sát
                            s3 = s3+str(right[2*i+1]).ljust(9,' ')  # Dòng ngắn mạch của phía from bus của bus quan sát
                            s4 = s4+str(rightBus[2*i]).ljust(9,' ') # To bus của bus quan sát
                            s5 = s5+str(right[2*i]).ljust(9,' ')    # Dòng ngắn mạch của phía to bus của bus quan sát
                            s6 = s6+str(onePhase[i]).ljust(9,' ')   # Dòng ngắn mạch tổng hợp tại bus quan sát
                        else:
                            s1 = s1+str(newarr[i]).ljust(9,' ')
                            s2 = s2+str(rightBus[2*i]).ljust(9,' ')
                            s3 = s3+str(right[2*i]).ljust(9,' ')
                            s4 = s4+str(rightBus[2*i+1]).ljust(9,' ')
                            s5 = s5+str(right[2*i+1]).ljust(9,' ')
                            s6 = s6+str(onePhase[i]).ljust(9,' ')
                    f.writelines('#'*140+'\n')
                    f.writelines('#' +' '*70+'RESUME'+' '*70+'\n')
                    f.writelines('#'*140+'\n')
                    f.writelines('\n')
                    f.writelines('Parameters:\n')
                    f.writelines('\n')
                    f.writelines('- From Bus: {}\n'.format(dialog.fromBus.GetValue()))
                    f.writelines('- Middle Bus: {}\n'.format(dialog.Middle.GetValue()))
                    f.writelines('- ID: {}\n'.format(dialog.textCtrl_ID1.GetValue()))
                    f.writelines('- To Bus: {}\n'.format(dialog.toBus.GetValue()))
                    f.writelines('- ID: {}\n'.format(dialog.textCtrl_ID2.GetValue()))
                    f.writelines('- Segment numbers: {}\n'.format(dialog.textCtrl_Number.GetValue()))
                    f.writelines('\n')
                    f.writelines('BUS:     '+s1+'\n'+'FR BUS:  '+s2+'\n'+'I(AMPS): '+s3+'\n'+'TO BUS:  '+s4+'\n'+'I(AMPS): '+s5+'\n'+'TOTAL:   '+s6+'\n')
                    r.close()
                    os.remove("output")
                    f.close()
                    wx.MessageBox("Result has been saved in {b}.".format(b=fileName))
                    
            elif tabLineType == 3:   # chia 16 đoạn
                ierr1, rval1 = psspy.brncur(fromBus,middle,id1)
                ierr2, rval2 = psspy.brncur(fromBus,toBus,id2)
                if ierr1 == 1 or ierr2 == 1:
                    wx.MessageBox('Bus not found')
                elif ierr1 == 2 or ierr2 == 2:
                    wx.MessageBox('Branch not found')
                elif ierr1 == 3 or ierr2 == 3:
                    wx.MessageBox('Branch out of service')
                elif segments != 16 :
                    wx.MessageBox('This case apply only for 16 segments')
                else:
                    segmentsBus = []
                    count =0
                    for i in range(1,1000):
                        if not i in busNum:
                            segmentsBus.append(i)
                        if count < segments:
                            count+=1
                        else:
                            break
                    segmentsBus[8]= middle
                    # tạo file line tab cho đoạn có cả Frombus, Middle bus và To bus
                    createLineTabFile3Bus(dirName,fromBus,middle,id1,toBus,id2,voltage,segmentsBus)
                    pyPath = os.path.join(dirName,'lineTab.py')
                    execfile(pyPath)

                    # ngắn mạch tóm tắt
                    with open('output', 'w') as f, silence(f):
                        psspy.bsys(1,0,[0.0,0.0],0,[],segments+1,segmentsBus,0,[],0,[])
                        psspy.ascc(1,0,[1,0,0,0,1,3,0,0,0,0],"","")
                    r = open('output','r')
                    lines = r.readlines()
                    outName = os.path.basename(self.PathOrigin)[0:-4]
                    fileName = dirName+"\\{}-tomtat.txt".format(outName)
                    f = open(fileName,'w')
                    flag = 0
                    resultLine = 0

                    for line,value in enumerate(lines):
                        if 'ONE PHASE' in value:
                            flag = 1
                            resultLine = line
                        if flag == 1:
                            f.writelines(value)
                    result = ''
                    for i in range(resultLine,len(lines)-1):
                        result = result +'\n'+ lines[i]

                    wx.MessageBox('Result  is:{A}\n '.format(A=result))
                    r.close()
                    os.remove("output")
                    f.close()
                    wx.MessageBox("Result has been saved in {b}.".format(b=fileName))

                    # ngắn mạch chi tiet
                    with open('output', 'w') as f, silence(f):
                        psspy.bsys(1,0,[0.0,0.0],0,[],segments+1,segmentsBus,0,[],0,[])
                        psspy.ascc(1,0,[1,0,0,0,1,2,0,1,0,0],"","")
                    r = open('output','r')
                    lines = r.readlines()
                    outName = os.path.basename(self.PathOrigin)[0:-4]
                    fileName = dirName+"\\{}-chitiet.txt".format(outName)
                    f = open(fileName,'w')
                    flag = 0
                    newarr = []
                    name = []
                    voltage = []
                    onePhase = []
                    threePhase = []
                    right = []
                    rightBus = []

                    for line,value in enumerate(lines):
                        if 'PSS(R)E  SHORT  CIRCUIT  OUTPUT' in value:
                            flag = 1
                        if flag == 1:
                            f.writelines(value)
                            params = value.split()

                            if 'AT BUS' in value:
                                newarr.append(params[2])
                                name.append(params[3])
                                voltage.append(params[4])
                            
                            if 'AMP/OHM' in value:
                                right.append(params[11])
                                rightBus.append(params[0])

                            if 'TOTAL  FAULT  CURRENT' in value:
                                onePhase.append(params[6])
                                threePhase.append(params[4])

                    # tạo mảng chứa các giá trị resume
                    s1 = s2 = s3 = s4 = s5 = s6 = ''
                    for i in range(len(newarr)):
                        if i == 0:
                            s1 = s1+str(newarr[i]).ljust(9,' ') # Mã bus đang quan sát
                            s2 = s2+str(rightBus[2*i+1]).ljust(9,' ')  # From bus của bus quan sát
                            s3 = s3+str(right[2*i+1]).ljust(9,' ')  # Dòng ngắn mạch của phía from bus của bus quan sát
                            s4 = s4+str(rightBus[2*i]).ljust(9,' ') # To bus của bus quan sát
                            s5 = s5+str(right[2*i]).ljust(9,' ')    # Dòng ngắn mạch của phía to bus của bus quan sát
                            s6 = s6+str(onePhase[i]).ljust(9,' ')   # Dòng ngắn mạch tổng hợp tại bus quan sát
                        else:
                            s1 = s1+str(newarr[i]).ljust(9,' ')
                            s2 = s2+str(rightBus[2*i]).ljust(9,' ')
                            s3 = s3+str(right[2*i]).ljust(9,' ')
                            s4 = s4+str(rightBus[2*i+1]).ljust(9,' ')
                            s5 = s5+str(right[2*i+1]).ljust(9,' ')
                            s6 = s6+str(onePhase[i]).ljust(9,' ')
                    f.writelines('#'*140+'\n')
                    f.writelines('#' +' '*70+'RESUME'+' '*70+'\n')
                    f.writelines('#'*140+'\n')
                    f.writelines('BUS:     '+s1+'\n'+'FR BUS:  '+s2+'\n'+'I(AMPS): '+s3+'\n'+'TO BUS:  '+s4+'\n'+'I(AMPS): '+s5+'\n'+'TOTAL:   '+s6+'\n')
                    r.close()
                    os.remove("output")
                    f.close()
                    wx.MessageBox("Result has been saved in {b}.".format(b=fileName))
        else:
            event.Skip()

    # tính ngắn mạch phân bố từ file có sẵn, cần thêm phần connect với PSSE vào file python có sẵn
    def Distribution_Short_Circuit_From_File_Fcn(self,event):
        PATH = self.Path
        if PATH != '':
            # file python line tab
            pyFile = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
            dirname = os.path.dirname(pyFile)
            path = os.path.join(dirname,'distribution_shortCircuit.py')
            f = open(path,'w')
            f.write("import pssepath\n")
            f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
            f.write("sys.path.append(PSSE_LOCATION)\n")
            f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
            f.write("pssepath.add_pssepath(33)\n")
            f.write("import psspy \n")
            r = open(pyFile,'r')

            for line in r:
                if not ('import' in line or  'PSSE_LOCATION' in line or 'add_pssepath(33)' in line):
                    f.write(line)
                if "flat_2" in line:
                    break 
            f.write('psspy.fnsl(options1=0,options5=0)\n')
            f.close()
            execfile(path)
            # os.remove(path)

            # file python tính ngắn mạch
            pyFile2 = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
            dirname2 = os.path.dirname(pyFile2)
            path2 = os.path.join(dirname2,'distribution_shortCircuit.py')
            f = open(path2,'w')
            f.write("import pssepath\n")
            f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
            f.write("sys.path.append(PSSE_LOCATION)\n")
            f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
            f.write("pssepath.add_pssepath(33)\n")
            f.write("import psspy \n")

            r = open(pyFile2,'r')
            for line in r:
                f.write(line)
            f.close()
            r.close()
            
            with open('output', 'w') as f, silence(f):
                execfile(path2)
            r = open('output','r')
            lines = r.readlines()

            # hiển thị kết quả tóm tắt
            dirName = os.path.dirname(self.PathOrigin)
            outName = os.path.basename(self.PathOrigin)[0:-4]
            fileName = dirName+"\\{}-tomtat.txt".format(outName)
            f = open(fileName,'w')
            flag = 0
            for line,value in enumerate(lines):
                if "ONE PHASE" in value:
                    flag = 1
                if flag == 1:
                    # content.append(value)
                    f.writelines(value)
            r.close()
            os.remove("output")
            wx.MessageBox("Result has been saved in {b}.".format(b=fileName))

            # tạo file tính ngắn mạch chi tiết
            pyFile3 = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
            dirname3 = os.path.dirname(pyFile2)
            path3 = os.path.join(dirname3,'distribution_shortCircuit.py')
            f = open(path3,'w')
            f.write("import pssepath\n")
            f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
            f.write("sys.path.append(PSSE_LOCATION)\n")
            f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
            f.write("pssepath.add_pssepath(33)\n")
            f.write("import psspy \n")

            r = open(pyFile3,'r')
            for line in r:
                f.write(line)
            f.close()
            r.close()
            
            with open('output', 'w') as f, silence(f):
                execfile(path3)
            r = open('output','r')
            lines = r.readlines()
            dirName = os.path.dirname(self.PathOrigin)
            outName = os.path.basename(self.PathOrigin)[0:-4]
            # hiển thị kết quả chi tiết với phần tổng hợp phía cuối
            fileName = dirName+"\\{}-chitiet.txt".format(outName)
            f = open(fileName,'w')
            flag = 0
            newarr = []
            name = []
            voltage = []
            onePhase = []
            threePhase = []
            right = []
            rightBus = []
            s1 = s2 = s3 = s4 = s5 = s6 = ''
            for line,value in enumerate(lines):
                if "PSS(R)E  SHORT  CIRCUIT  OUTPUT" in value:
                    flag = 1
                if flag == 1:
                    f.writelines(value)
                    params = value.split()

                    if 'AT BUS' in value:
                        newarr.append(params[2])
                        name.append(params[3])
                        voltage.append(params[4])

                    if 'AMP/OHM' in value:
                        right.append(params[11])
                        rightBus.append(params[0])

                    if 'TOTAL  FAULT  CURRENT' in value:
                        onePhase.append(params[6])
                        threePhase.append(params[4])

            for i in range(len(newarr)):
                if i == 0:
                    s1 = s1+str(newarr[i]).ljust(9,' ')
                    s2 = s2+str(rightBus[2*i+1]).ljust(9,' ')
                    s3 = s3+str(right[2*i+1]).ljust(9,' ')
                    s4 = s4+str(rightBus[2*i]).ljust(9,' ')
                    s5 = s5+str(right[2*i]).ljust(9,' ')
                    s6 = s6+str(onePhase[i]).ljust(9,' ')
                else:
                    s1 = s1+str(newarr[i]).ljust(9,' ')
                    s2 = s2+str(rightBus[2*i]).ljust(9,' ')
                    s3 = s3+str(right[2*i]).ljust(9,' ')
                    s4 = s4+str(rightBus[2*i+1]).ljust(9,' ')
                    s5 = s5+str(right[2*i+1]).ljust(9,' ')
                    s6 = s6+str(onePhase[i]).ljust(9,' ')
            f.writelines('#'*140+'\n')
            f.writelines('#' +' '*70+'RESUME'+' '*70+'\n')
            f.writelines('#'*140+'\n')
            f.writelines('BUS:     '+s1+'\n'+'FR BUS:  '+s2+'\n'+'I(AMPS): '+s3+'\n'+'TO BUS:  '+s4+'\n'+'I(AMPS): '+s5+'\n'+'TOTAL:   '+s6+'\n')
            r.close()
            os.remove("output")
            wx.MessageBox("Result has been saved in {b}.".format(b=fileName))
            os.remove(path3)

        else:
            wx.MessageBox("Please open an existing case first!")

    # tính ngắn mạch bằng cách tạo mới file python từ các bus được chọn
    def Short_Circuit_Cal_New_Fcn(self,event):
        PATH = self.Path
        PATHFILE = self.PathFile
        if PATH != '':
            busListFull = []
            for i in range(len(self.matrixBus[self.indexFile])):
                busListFull.append(str(self.matrixBus[self.indexFile][i,0])+'-'+str(self.matrixBus[self.indexFile][i,1]))
            # tạo dialog để người tính toán chọn các bus cần quan sát
            dialog = Choose_Bus(self.parent)
            dialog.lbBus.SetItems(busListFull)
            dialog.lbBusChoices = busListFull
            dialog.ShowModal()
            if dialog.flag == 1:
                busList = dialog.Calculation(event )

                dirname = os.path.dirname(self.PathOrigin)
                path = os.path.join(dirname,'shortCircuit.py')
                f = open(path,'w')
                f.write("import pssepath\n")
                f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
                f.write("sys.path.append(PSSE_LOCATION)\n")
                f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
                f.write("pssepath.add_pssepath(33)\n")
                f.write("import psspy \n")
                f.write("psspy.bsys(1,0,[0.0,0.0],0,[],{n},{busList},0,[],0,[])\n".format(n=len(busList),busList=busList))
                f.write('psspy.ascc(1,0,[1,0,0,0,1,2,0,1,0,0],"","")\n')
                f.close()

                with open('output', 'w') as f, silence(f):
                    psspy.bsys(1,0,[0.0,0.0],0,[],len(busList),busList,0,[],0,[])
                    psspy.ascc(1,0,[1,0,0,0,1,2,0,1,0,0],"","")
                r = open('output','r')
                lines = r.readlines()
                outName = self.PathOrigin[0:-4]
                fileName = "{}-ShortCircuitResult.txt".format(outName)
                f = open(fileName,'w')
                flag = 0
                newarr = []
                name = []
                voltage = []
                onePhase = []
                threePhase = []
                fromBus = []
                onePhaseDetail = []
                threePhaseDetail = []
                mydict = {'FromBus': [],'AtBus':[],'onePhase':[],'threePhase': []}

                
                for line,value in enumerate(lines):
                    if "PSS(R)E  SHORT  CIRCUIT  OUTPUT" in value:
                        flag = 1
                    if flag == 1:
                        f.writelines(value)
                        params = value.split()

                        if 'AT BUS' in value:
                            newarr.append(params[2])
                            # print('----newarr------',newarr)
                            name.append(params[3])
                            voltage.append(params[4])
                            flagAtBus = 1
                            if len(newarr)>1:
                                mydict['AtBus'].append(newarr[len(newarr)-2])
                                mydict['FromBus'].append(fromBus)
                                mydict['onePhase'].append(onePhaseDetail)
                                mydict['threePhase'].append(threePhaseDetail)
                            onePhaseDetail = []
                            threePhaseDetail = []
                            fromBus = []
                        if 'Output completed' in value:
                            mydict['AtBus'].append(newarr[len(newarr)-1])
                            mydict['FromBus'].append(fromBus)
                            mydict['onePhase'].append(onePhaseDetail)
                            mydict['threePhase'].append(threePhaseDetail)

                        if "AMP/OHM" in value:
                            fromBus.append(params[0])
                            if not ']'in params[1][1:]:
                                onePhaseDetail.append(params[11])
                                threePhaseDetail.append(params[6])
                            else:
                                onePhaseDetail.append(params[10])
                                threePhaseDetail.append(params[5])

                        if "AMP/" in value and "3WNDTR" in value:
                            if not ']'in params[1][1:]:
                                fromBus.append('3WNDTR '+params[1][1:])
                                onePhaseDetail.append(params[9])
                                threePhaseDetail.append(params[7])
                            else:
                                fromBus.append('3WNDTR '+params[1][1:len(params[1])-1])
                                onePhaseDetail.append(params[8])
                                threePhaseDetail.append(params[6])


                        if 'TOTAL  FAULT  CURRENT' in value:
                            onePhase.append(params[6])
                            threePhase.append(params[4])
                
                # tóm tắt kết quả

                f.writelines('####################################################################\n')
                f.writelines('#                               RESUME                              \n')
                f.writelines('####################################################################\n')
                f.writelines('BUS'.ljust(15,' ')+'BUS NAME '.ljust(30,' ')+'THREE PHASE'.ljust(15,' ')+'ONE PHASE'+'\n')
                resume = ('BUS'.ljust(15,' ')+'BUS NAME '.ljust(40,' ')+'THREE PHASE'.ljust(15,' ')+'ONE PHASE'+'\n')
                for i in range(len(newarr)):
                    f.writelines(str(newarr[i]).ljust(15,' ')+str(name[i]).ljust(14,' ')+str(voltage[i]).ljust(17,' ')+str(threePhase[i]).ljust(7,' ')+str(onePhase[i]).rjust(15,' ') +'\n')
                    s=str(newarr[i]).ljust(15,' ')+str(name[i]).ljust(14,' ')+str(voltage[i]).ljust(20,' ')+str(threePhase[i])+str(onePhase[i]).rjust(15,' ') +'\n'
                    resume = resume+s
                wx.MessageBox(resume)
                
                for i in range(len(newarr)):
                    f.writelines('AT BUS: {} \n'.format(newarr[i]))
                    f.writelines('BUS'.ljust(22,' ')+'THREE PHASE'.ljust(22,' ')+'ONE PHASE'+'\n')
                    for j in range(len(mydict['FromBus'][i])):
                        f.writelines(str(mydict['FromBus'][i][j]).ljust(22,' ')+str(mydict['threePhase'][i][j]).ljust(22,' ')+str(mydict['onePhase'][i][j])+'\n')

                r.close()
                os.remove("output")
                f.close()

                wx.MessageBox("Result has been saved in {b}.".format(b=fileName))
            else:
                even.Skip()
        else:
            wx.MessageBox("Please open an existing case first!")
    
    # tính ngắn mạch từ file có sẵn, cần bổ sung phần thư viện kết nối với PSSE
    def Short_Circuit_Cal_From_File_Fcn(self,event):
        PATH = self.Path
        PATHFILE = self.PathFile
        flagResume = 0
        if PATH <> '':
            pyFile = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
            dirname = os.path.dirname(pyFile)
            path = dirname+'\\shortCircuitFromFile.py'
            f = open(path,'w')
            f.write("import pssepath\n")
            f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
            f.write("sys.path.append(PSSE_LOCATION)\n")
            f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
            f.write("pssepath.add_pssepath(33)\n")
            f.write("import psspy \n")
            r = open(pyFile,'r')
            flagSort = 0
            sortArr = []
            for line in r:
                if not ('import' in line or  'PSSE_LOCATION' in line or 'add_pssepath(33)' in line) and flagSort==0:
                    f.write(line)
                if 'psspy.ascc(1,0,[1,0,0,0,1,3,0,1,0,0],"","")' in line or 'psspy.ascc(1,0,[1,0,0,0,1,3,0,0,0,0],"","")' in line:
                    flagResume = 1
                if "SORT" in line:
                    flagSort = 1
                if flagSort ==1:
                    a = line.replace('\n','')
                    if not 'SORT' in a:
                        sortArr.append(int(a))
            r.close()
            f.close()

            with open('output', 'w') as f, silence(f):
                execfile(path)
            r = open('output','r')
            lines = r.readlines()
            outName = self.PathOrigin[0:-4]
            fileName = "{}-ShortCircuitResult.txt".format(outName)
            f = open(fileName,'w')
            flag = 0
            newarr = []
            name = []
            voltage = []
            onePhase = []
            threePhase = []
            fromBus = []
            onePhaseDetail = []
            threePhaseDetail = []
            mydict = {'FromBus': [],'AtBus':[],'onePhase':[],'threePhase': []}
            # Write to terminal
            content = self.parent.terminalText
            content.Value = ''
            if flagResume == 0:
                for line,value in enumerate(lines):
                    if "PSS(R)E  SHORT  CIRCUIT  OUTPUT" in value:
                        flag = 1
                    if flag == 1:
                        f.writelines(value)
                        params = value.split()

                        if 'AT BUS' in value:
                            newarr.append(int(params[2]))
                            name.append(params[3])
                            voltage.append(params[4])
                            if len(newarr)>1:
                                mydict['AtBus'].append(newarr[len(newarr)-2])
                                mydict['FromBus'].append(fromBus)
                                mydict['onePhase'].append(onePhaseDetail)
                                mydict['threePhase'].append(threePhaseDetail)
                                onePhaseDetail = []
                                threePhaseDetail = []
                                fromBus = []
                        if 'Output completed' in value:
                            mydict['AtBus'].append(newarr[len(newarr)-1])
                            mydict['FromBus'].append(fromBus)
                            mydict['onePhase'].append(onePhaseDetail)
                            mydict['threePhase'].append(threePhaseDetail)

                        if "AMP/OHM" in value:
                            fromBus.append(params[0])
                            if not ']'in params[1][1:]:
                                onePhaseDetail.append(params[11])
                                threePhaseDetail.append(params[6])
                            else:
                                onePhaseDetail.append(params[10])
                                threePhaseDetail.append(params[5])
                        if "AMP/" in value and "3WNDTR" in value:
                            if not ']'in params[1][1:]:
                                fromBus.append('3WNDTR '+params[1][1:])
                                onePhaseDetail.append(params[9])
                                threePhaseDetail.append(params[7])
                            else:
                                fromBus.append('3WNDTR '+params[1][1:len(params[1])-1])
                                onePhaseDetail.append(params[8])
                                threePhaseDetail.append(params[6])

                        if 'TOTAL  FAULT  CURRENT' in value:
                            onePhase.append(params[6])
                            threePhase.append(params[4])
                
                # tóm tắt kết quả
                f.writelines('####################################################################\n')
                f.writelines('#                              RESUME                               \n')
                f.writelines('####################################################################\n')
                f.writelines('BUS'.ljust(15,' ')+'BUS NAME '.ljust(30,' ')+'THREE PHASE'.ljust(15,' ')+'ONE PHASE'+'\n')
                resume = ('BUS'.ljust(15,' ')+'BUS NAME '.ljust(40,' ')+'THREE PHASE'.ljust(15,' ')+'ONE PHASE'+'\n')
                for i in range(len(newarr)):
                    n = len(name[i])
                    f.writelines(str(newarr[i]).ljust(15,' ')+str(name[i]).ljust(14,' ')+str(voltage[i]).ljust(17,' ')+str(threePhase[i]).ljust(7,' ')+str(onePhase[i]).rjust(15,' ') +'\n')
                    s=str(newarr[i]).ljust(15,' ')+str(name[i]).ljust(14,' ')+str(voltage[i]).ljust(20,' ')+str(threePhase[i])+str(onePhase[i]).rjust(15,' ') +'\n'
                    resume = resume + s
                wx.MessageBox(resume)
                f.writelines('BUS'.ljust(22,' ')+'THREE PHASE (kA)'.ljust(22,' ')+'ONE PHASE (kA)'+'\n')
                f.writelines('\n')
                for i in sortArr:
                    if i in newarr:
                        f.writelines(str(i).ljust(22,' ')+str(float(threePhase[newarr.index(i)])/1000).ljust(22,' ')+str(float(onePhase[newarr.index(i)])/1000)+'\n')
                        
                        for j in range(len(mydict['FromBus'][newarr.index(i)])):
                            threeP = (float(threePhase[newarr.index(i)]) - float(mydict['threePhase'][newarr.index(i)][j]))/1000
                            oneP = (float(onePhase[newarr.index(i)]) - float(mydict['onePhase'][newarr.index(i)][j]))/1000
                            f.writelines(str(mydict['FromBus'][newarr.index(i)][j]).ljust(22,' ')+str(threeP).ljust(22,' ')+str(oneP)+'\n')
                        f.writelines('\n')
                    else:
                        print('Bus {} is not exist.'.format(i))

                r.close()
                f.close() 
                wx.MessageBox("Result has been saved in {b}.".format(b=fileName))
                os.remove("output") 
                os.remove(path)
            else:
                for line,value in enumerate(lines):
                    if 'PTI INTERACTIVE POWER SYSTEM SIMULATOR--PSS(R)E' in value:
                        flag = 1
                    if flag == 1:
                        f.writelines(value)
                r.close()
                f.close()
                os.remove("output") 
                os.remove(path)
            r = open(fileName,'r')
            lines = r.readlines()
            for line,value in enumerate(lines):
                if value != '\n':
                    # print(line)
                    content.Value = content.Value +'\n'+ value#.encode('utf8')

        else:
            wx.MessageBox("Please open an existing case first!")

    # tính ngắn mạch cho tất cả các file, tổng hợp thành 1 file txt có phần resume ở cuối
    def Short_Circuit_Cal_All_Cases_Fcn_Export_Word(self,event):
        psspy.psseinit(2000)
        PATH = self.Path
        PATHFILE = self.PathFile
        pyFile = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
        dirname = os.path.dirname(pyFile)
        path_result_1 = os.path.join(dirname,'Phu_Luc_Ngan_Mach.txt')
        fResult = open(path_result_1,'w')

        savFolder = openFolder(self,'Choose the Folder contain all sav files')
        os.chdir(savFolder)
        savFileNames = glob.glob('*.sav')
        # bổ sung phần kết nối PSSE cho file python
        
        path = os.path.join(dirname,'shortCircuitAllCase.py')
        f = open(path,'w')
        f.write("import pssepath\n")
        f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
        f.write("sys.path.append(PSSE_LOCATION)\n")
        f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
        f.write("pssepath.add_pssepath(33)\n")
        f.write("import psspy \n")
        r = open(pyFile,'r')
        for line in r:
            if not ('import' in line or  'PSSE_LOCATION' in line or 'add_pssepath(33)' in line):
                f.write(line)
        f.close()
        newarr = []
        name = []
        voltage = []
        onePhase = []
        threePhase = []
        fileName = []
        count = []
        for savFile in savFileNames:
            
            psspy.case(savFile)
            flag = 0
            outFile = 'output'
            with open(outFile, 'w') as out, silence(out):
                execfile(path)
            read = open(outFile,'r')
            lines = read.readlines()
            outName = os.path.basename(savFile) #[0:-6]
            fResult.write("### {} \n".format(outName))
            fileName.append(outName)
            # fileName = "{}-ShortCircuitResult.txt".format(outName)
            result = u'' #open(fileName,'w')
            for line,value in enumerate(lines):
                if "PSS(R)E  SHORT  CIRCUIT  OUTPUT" in value:
                    flag = 1
                if flag == 1:
                    result = result+u'{}'.format(value)#+'\n' #.writelines(value)
                    params = value.split()
                    if 'AT BUS' in value:
                        newarr.append(params[2])
                        name.append(params[3])
                        voltage.append(params[4])

                    if 'TOTAL  FAULT  CURRENT' in value:
                        onePhase.append(params[6])
                        threePhase.append(params[4])
                    fResult.write(value)
            count.append(len(onePhase))
            read.close()
            os.remove(outFile)
        # tổng hợp kết quả
        fResult.write('####################################################################\n')
        fResult.write('#                              RESUME                               \n')
        fResult.write('####################################################################\n')

        for t,file in enumerate(fileName):
            s= '## File: {} \n'.format(file)
            s = s+('BUS'.ljust(15,' ')+'BUS NAME '.ljust(30,' ')+'THREE PHASE'.ljust(15,' ')+'ONE PHASE'+'\n')
            
            if t==0:
                x = 0
            else:
                x=count[t-1]
            for i in range(x,count[t]):
                n = len(name[i])
                s= s+(str(newarr[i]).ljust(15,' ')+str(name[i]).ljust(14,' ')+str(voltage[i]).ljust(17,' ')+str(threePhase[i]).ljust(7,' ')+str(onePhase[i]).rjust(15,' ') +'\n')
            fResult.write(s)
        fResult.close()

        wx.MessageBox("Result has been saved in {b}.".format(b=path_result_1))

    # tính ngắn mạch cho all files trong thư mục, mỗi file ghi kết quả ra một file txt
    def Short_Circuit_Cal_All_Cases_Fcn_Export_Txt(self,event):
        psspy.psseinit(2000)
        PATH = self.Path
        PATHFILE = self.PathFile
        # if PATH <> '':

        pyFile = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")

        savFolder = openFolder(self,'Choose the Folder contain all sav files')
        os.chdir(savFolder)
        savFileNames = glob.glob('*.sav')

        dirname = os.path.dirname(pyFile)
        path = os.path.join(dirname,'shortCircuitAllCase.py')
        f = open(path,'w')
        f.write("import pssepath\n")
        f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
        f.write("sys.path.append(PSSE_LOCATION)\n")
        f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
        f.write("pssepath.add_pssepath(33)\n")
        f.write("import psspy \n")
        r = open(pyFile,'r')
        for line in r:
            if not ('import' in line or  'PSSE_LOCATION' in line or 'add_pssepath(33)' in line):
                f.write(line)
        f.close()
        for i,savfile in enumerate(savFileNames):
            psspy.case(savfile)
            flag = 0
            outFile = 'output{}'.format(i)
            with open(outFile, 'w') as out, silence(out):
                execfile(path)
            read = open(outFile,'r')
            lines = read.readlines()
            outName = savfile[0:-6]
            fileName = "{}-ShortCircuitResult.txt".format(outName)
            result = open(fileName,'w')
            for line,value in enumerate(lines):
                if "PSS(R)E  SHORT  CIRCUIT  OUTPUT" in value:
                    flag = 1
                if flag == 1:
                    result.writelines(value)
            read.close()
            os.remove(outFile)
        wx.MessageBox("Calculation Finish")

    # tính toán TLCS cho all file trong thư mục
    def Power_Flow_Cal_Fcn(self,event):
        PATH = self.Path
        PATHFILE = self.PathFile
        content = self.parent.terminalText
        content.Value = ''
        
        if PATHFILE != '':
            for savfile in PATHFILE:
                with open('output', 'w') as f, silence(f):
                    psspy.case(savfile)
                    self.PowerFlow(event)
                r = open('output','r')
                lines = r.readlines()
                for line in lines:
                    content.Value = content.Value + '\n'+line
        else:
            wx.MessageBox("Please open an existing case first!")

    # Tính toán TLCS cho file được chọn
    @profiled('psse.power_flow_selected')
    def Power_Flow_Selected_Cal_Fcn( self, event,path ):
        PATH = path 
        content = self.parent.terminalText
        content.Value = ''
        with open('output', 'w') as f, silence(f):
            if PATH != '':
                psspy.case(PATH)
                self.PowerFlow(event)
            else:
                wx.MessageBox("Please open an existing case first!")
        r = open('output','r')
        lines = r.readlines()
        for line in lines:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            if line != '\n':
                content.Value = content.Value + line.encode('utf-8') # loi 'utf8' codec can't decode byte 0xd0 in position 8: invalid continuation byte
                # la do trong file sav co ten nut de tieng viet --> chinh lai file sav

    # Run exactly one flat start, one FDNS and one FNSL for the current case.
    @profiled('psse.power_flow_once')
    def Power_Flow_Once_Cal_Fcn(self, event, path):
        content = self.parent.terminalText
        content.Value = ''
        if path == '':
            wx.MessageBox("Please open an existing case first!")
            return False

        with open('output', 'w') as f, silence(f):
            psspy.case(path)
            psspy.flat_2([0,0,0,0,0,0,0,0], [0.0,0.0])
            psspy.fdns()
            psspy.fnsl()

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile, 'a')
            f.writelines("psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n")
            f.writelines("psspy.fdns()\n")
            f.writelines("psspy.fnsl()\n")
            f.close()

        r = open('output', 'r')
        lines = r.readlines()
        r.close()
        for line in lines:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            if line != '\n':
                content.Value = content.Value + line.encode('utf-8')
        return True

    # tính ổn định động
    def Dynamic_Stability_Cal_Fcn( self, event ):
        PATH = self.Path
        if PATH != '':
            dialog = Select_Idv_File(self.parent)
            dialog.ShowModal()
            choose = dialog.choose*dialog.flag
            if choose ==1: # tạo file dyn_1.py
                idv1 = openFile(self,'Select the dyn_1.idv:', "Idv files (*.idv)|*.idv|All files|*")
                dirname = os.path.dirname(idv1)
                f = open(idv1, 'r')
                lines = f.readlines()
                outname = ''
                for line in lines:
                    if 'save' in line:
                        outname = dirname+'\\'+ outname+line[5:]
                
                psspy.fnsl()
                psspy.fnsl()
                psspy.fnsl()
                psspy.ordr(0)
                psspy.fnsl()
                psspy.conl(0,1,1,STATUS1=0)
                psspy.conl(1,1,2,LOADIN1 = 100.0,LOADIN2 = 0.0,LOADIN3 = 0.0,LOADIN4=100.0)
                psspy.conl(1,1,3)
                psspy.cong(0)
                psspy.ordr(0)
                psspy.fact()
                psspy.tysl(0)
                psspy.save(outname)
                self.Dynamic_Stability_Cal_Fcn(event)
            elif choose == 2:
                # tạo file dyn_21.py
                idv2 = openFile(self,'Select the dyn_21.idv:', "Idv files (*.idv)|*.idv|All files|*")
                dirname = os.path.dirname(idv2)
                f = open(idv2, 'r')
                lines = f.readlines()
                dyrname = ''
                for line in lines:
                    index = line.find('.dyr')
                    if index !=-1:
                        dyrname = dirname + '\\'+ line[:index]+'.dyr'

                cc1name =  dirname + '\\'+ 'CC1'
                ct1name =  dirname + '\\'+ 'CT1'
                cmp1name =  dirname + '\\'+ 'CMP1'
                # ghi kết quả chạy ra vào file output21
                with open('output21', 'w') as f, silence(f):
                    psspy.fact()
                    psspy.dynamicsmode(0)
                    psspy.dyre_new([1,1,1,1],dyrname,cc1name,ct1name,cmp1name )
                    psspy.set_relang(1,0,"")
                f.close()
                r = open('output21','r')
                lines = r.readlines()
                flagWrite = 0
                for line in lines:
                    if 'Out of file data--switch to terminal input mode' in line:
                        flagWrite = 1
                    if flagWrite == 1:
                        print(line)
                r.close()
                self.Dynamic_Stability_Cal_Fcn(event)
            elif choose == 4: # bổ sung thêm file dyr (thường bổ sung cho nguồn NLTT)
                dyr_add = openFile(self,'Select the additional dyr file:', "Dyr files (*.dyr)|*.dyr|All files|*")
                if dyr_add != '':
                    if os.path.exists('output21'):
                        r = open('output21','r')
                        lines = r.readlines()

                        index = 0
                        for lineNum,line in enumerate(lines):
                            if "NEXT AVAILABLE ADDRESSES ARE" in line:
                                index = int(lineNum)
                        [CONs,STATEs,VARs,ICONs] = lines[index+2].split()
                        params = [int(CONs),int(STATEs),int(VARs),int(ICONs)] 
                        r.close()
                        # ghi kết quả vào file output21 để kiểm tra add có thành công không?
                        with open('output21', 'a') as f, silence(f):
                            psspy.dyre_add(params,dyr_add,"","")
                        f.close()
                        r = open('output21','r')
                        lines = r.readlines()
                        flag = 0
                        index = 0
                        for line,val in enumerate(lines):
                            if 'No dynamics data in memory' in val:
                                wx.MessageBox('No dynamic data in memory!')
                                break
                            elif 'NEXT AVAILABLE ADDRESSES ARE' in val:
                                index = line
                                # break 
                        [CONs,STATEs,VARs,ICONs] = lines[index+2].split()
                        params = [int(CONs),int(STATEs),int(VARs),int(ICONs)] 
                        r.close()
                    else:
                        wx.MessageBox('No dynamic data in memory!')
                self.Dynamic_Stability_Cal_Fcn(event)
            elif choose == 3: # tạo file dyn_22.py
                genNumList = []
                for i in range(len(self.matrixGen[self.indexFile])):
                    genNumList.append(str(self.matrixGen[self.indexFile][i,0])+'-'+str(self.matrixGen[self.indexFile][i,23]))
                dialogOption = Simulation_option(self.parent)
                # tạo dialog để set relative Machine angle, mặc định là: relative to average angle
                dialogOption.comboBox_GenNum.SetItems(genNumList)
                dialogOption.ShowModal()
                chooseItem = dialogOption.Next(event)
                busNum = str(dialogOption.comboBox_GenNum.GetValue()).split('-')
                option = [chooseItem,busNum]

                if os.path.exists('output21'):
                    r = open('output21','r')
                    lines = r.readlines()

                    index = 0
                    for lineNum,line in enumerate(lines):
                        if "NEXT AVAILABLE ADDRESSES ARE" in line:
                            index = int(lineNum)
                    [CONs,STATEs,VARs,ICONs] = lines[index+2].split()
                    params = [int(CONs)-1,int(STATEs)-1,int(VARs)-1,int(ICONs)-1] 
                    r.close()
                    # tạo file dyn_22.py
                    idv22 = openFile(self,'Select the dyn_22.idv:', "Idv files (*.idv)|*.idv|All files|*")
                    createDyn22File(idv22,params,option)
                    # ghi kết quả vào file output22
                    with open('output22', 'w') as f, silence(f):
                        execfile('dyn_22.py')
                    r = open('output22','r')
                    lines = r.readlines()
                    flag = 1
                    errorLine = 0
                    endline = 0
                    # Kiểm tra xem initial có ok k?
                    for line,value in enumerate(lines):
                        if "INITIAL CONDITIONS CHECK O.K." in value:
                            wx.MessageBox('INITIAL CONDITIONS CHECK O.K!')
                            flag = 0
                        elif "ssn1.snp" in value:
                            errorLine = line
                        if "PTI INTERACTIVE POWER SYSTEM SIMULATOR--PSS(R)E" in value:
                            endLine = line
                    if flag == 1:
                        error = ''
                        for i in range(int(errorLine)+2,int(endLine)):
                            error = error +'\n'+ lines[i]

                        wx.MessageBox('There is an error in:{A}\n '.format(A=error))
                    r.close()

                else:
                    wx.MessageBox('Please run dyn_21.idv first!')
                if os.path.exists("output21"):
                    os.remove("output21")
                if os.path.exists("output22"):
                    os.remove("output22")
                if os.path.exists("dyn_22.py"):
                    os.remove('dyn_22.py')
                self.Dynamic_Stability_Cal_Fcn(event)
            elif choose == 5: # chạy file sự cố có sẵn
                pyFile = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
                dirname = os.path.dirname(pyFile)
                path = os.path.join(dirname,'dynamic_process.py')
                createIncidentFile(pyFile)
                
                execfile(path)

                call(('cmd','/c','start','',os.path.join(dirname+'\\sme.sav')))
                # call(('cmd','/c','start','',os.path.join(dirname+'\\dynamic_process.txt')))
            elif choose == 6: # chạy nhiều sự cố cùng lúc, (chạy tất cả các file python sự cố trong thư mục, trả về file out tương ứng)
                dirName = openFolder(self,'Choose the Folder contain all py files')
                os.chdir(dirName)
                pyFileNames = glob.glob('*.py')
                
                for pyFile in pyFileNames:
                    pyName = os.path.basename(pyFile)
                    if pyName != 'dynamic_process.py' and pyName != 'idv2py.py':
                        path = os.path.join(dirName,'dynamic_process.py')
                        pyPath = os.path.join(dirName,pyFile)
                        createIncidentFile(pyPath)
                        execfile(path)
                        os.remove(path)

    # tính ổn định động bằng cách tạo mới file IDV, người tính chọn những channel cần quan sát, tool sẽ tự tạo các file idv 
    def Dynamic_Stability_Cal_By_Create_New_IDV_Fcn( self, event ):
        dialog = Create_New_Idv(self.parent)
        busNumList = []
        # lấy ra list của busnum để thêm vào các dialog cho người dùng chọn kênh quan sát
        for i in range(len(self.matrixBus[self.indexFile])):
            busNumList.append(str(self.matrixBus[self.indexFile][i,0])+'-'+str(self.matrixBus[self.indexFile][i,1]))

        #angle
        dialog.m_listBox3.SetItems(busNumList)
        dialog.m_listBox3Choices = busNumList
        dialog.m_listBox4Choices = busNumList
        #pelec
        dialog.m_listBox31.SetItems(busNumList)
        dialog.m_listBox31Choices = busNumList
        dialog.m_listBox41Choices = busNumList
        #qelec
        dialog.m_listBox32.SetItems(busNumList)
        dialog.m_listBox32Choices = busNumList
        dialog.m_listBox42Choices = busNumList
        #eterm 
        dialog.m_listBox33.SetItems(busNumList)
        dialog.m_listBox33Choices = busNumList
        dialog.m_listBox43Choices = busNumList
        #EFD
        dialog.m_listBox34.SetItems(busNumList)
        dialog.m_listBox34Choices = busNumList
        dialog.m_listBox44Choices = busNumList
        #PMECH
        dialog.m_listBox35.SetItems(busNumList)
        dialog.m_listBox35Choices = busNumList
        dialog.m_listBox45Choices = busNumList
        #SPEED
        dialog.m_listBox36.SetItems(busNumList)
        dialog.m_listBox36Choices = busNumList
        dialog.m_listBox46Choices = busNumList
        #XADIFD
        dialog.m_listBox37.SetItems(busNumList)
        dialog.m_listBox37Choices = busNumList
        dialog.m_listBox47Choices = busNumList
        #ECOMP
        dialog.m_listBox38.SetItems(busNumList)
        dialog.m_listBox38Choices = busNumList
        dialog.m_listBox48Choices = busNumList
        #VOTHSR
        dialog.m_listBox39.SetItems(busNumList)
        dialog.m_listBox39Choices = busNumList
        dialog.m_listBox49Choices = busNumList
        #VREF
        dialog.m_listBox310.SetItems(busNumList)
        dialog.m_listBox310Choices = busNumList
        dialog.m_listBox410Choices = busNumList
        #BSFREQ
        dialog.m_listBox311.SetItems(busNumList)
        dialog.m_listBox311Choices = busNumList
        dialog.m_listBox411Choices = busNumList
        #VOLTAGE
        dialog.m_listBox312.SetItems(busNumList)
        dialog.m_listBox312Choices = busNumList
        dialog.m_listBox412Choices = busNumList
        #VOL & ANG 
        dialog.m_listBox313.SetItems(busNumList)
        dialog.m_listBox313Choices = busNumList
        dialog.m_listBox413Choices = busNumList
        # Flow
        dialog.m_listBox314.SetItems(busNumList)
        dialog.m_listBox314Choices = busNumList
        dialog.m_listBox414Choices = busNumList
        # FlowPQ
        dialog.m_listBox315.SetItems(busNumList)
        dialog.m_listBox315Choices = busNumList
        dialog.m_listBox415Choices = busNumList
        # FlowMVA
        dialog.m_listBox317.SetItems(busNumList)
        dialog.m_listBox317Choices = busNumList
        dialog.m_listBox417Choices = busNumList
        # RELAY2
        dialog.m_listBox318.SetItems(busNumList)
        dialog.m_listBox318Choices = busNumList
        dialog.m_listBox418Choices = busNumList
        # VAR
        dialog.m_listBox319.SetItems(busNumList)
        dialog.m_listBox319Choices = busNumList
        dialog.m_listBox419Choices = busNumList
        # STATE
        dialog.m_listBox320.SetItems(busNumList)
        dialog.m_listBox320Choices = busNumList
        dialog.m_listBox420Choices = busNumList
        # MACHITERM
        dialog.m_listBox321.SetItems(busNumList)
        dialog.m_listBox321Choices = busNumList
        dialog.m_listBox421Choices = busNumList
        # MACHAPPIMP
        dialog.m_listBox322.SetItems(busNumList)
        dialog.m_listBox322Choices = busNumList
        dialog.m_listBox422Choices = busNumList
        # VUEL
        dialog.m_listBox323.SetItems(busNumList)
        dialog.m_listBox323Choices = busNumList
        dialog.m_listBox423Choices = busNumList
        # VOEL
        dialog.m_listBox324.SetItems(busNumList)
        dialog.m_listBox324Choices = busNumList
        dialog.m_listBox424Choices = busNumList
        # PLOAD
        dialog.m_listBox325.SetItems(busNumList)
        dialog.m_listBox325Choices = busNumList
        dialog.m_listBox425Choices = busNumList
        # QLOAD
        dialog.m_listBox326.SetItems(busNumList)
        dialog.m_listBox326Choices = busNumList
        dialog.m_listBox426Choices = busNumList
        # GREF
        dialog.m_listBox327.SetItems(busNumList)
        dialog.m_listBox327Choices = busNumList
        dialog.m_listBox427Choices = busNumList
        # LCREF
        dialog.m_listBox328.SetItems(busNumList)
        dialog.m_listBox328Choices = busNumList
        dialog.m_listBox428Choices = busNumList
        # WINDVEL
        dialog.m_listBox329.SetItems(busNumList)
        dialog.m_listBox329Choices = busNumList
        dialog.m_listBox429Choices = busNumList
        # WINDTURSPD
        dialog.m_listBox330.SetItems(busNumList)
        dialog.m_listBox330Choices = busNumList
        dialog.m_listBox430Choices = busNumList
        # WINDPITCH
        dialog.m_listBox331.SetItems(busNumList)
        dialog.m_listBox331Choices = busNumList
        dialog.m_listBox431Choices = busNumList
        # WINDAEROTOR
        dialog.m_listBox332.SetItems(busNumList)
        dialog.m_listBox332Choices = busNumList
        dialog.m_listBox432Choices = busNumList
        # WINDROTORVOL
        dialog.m_listBox333.SetItems(busNumList)
        dialog.m_listBox333Choices = busNumList
        dialog.m_listBox433Choices = busNumList
        #WINDROTORCUR
        dialog.m_listBox334.SetItems(busNumList)
        dialog.m_listBox334Choices = busNumList
        dialog.m_listBox434Choices = busNumList
        # WINDPCOMAND
        dialog.m_listBox335.SetItems(busNumList)
        dialog.m_listBox335Choices = busNumList
        dialog.m_listBox435Choices = busNumList
        # WINDQCOMAND
        dialog.m_listBox336.SetItems(busNumList)
        dialog.m_listBox336Choices = busNumList
        dialog.m_listBox436Choices = busNumList
        # WINDAUX
        dialog.m_listBox337.SetItems(busNumList)
        dialog.m_listBox337Choices = busNumList
        dialog.m_listBox437Choices = busNumList

        dialog.m_comboBox1Choices = busNumList
        dialog.m_comboBox1.SetItems(busNumList)
        
        dialog.ShowModal()

    # tính ổn định tĩnh cho tất cả các file trong thư mục
    def Auto_Static_Stability_Cal_Fcn( self, event ):
        # init để không cần mở file psse vào tool mà vẫn chạy được chức năng tính toán
        psspy.psseinit(2000)
        # lấy thông tin đường dẫn của thư mục
        dirName = openFolder(self,'Choose the Folder contain all sav and sub,mon,con files')
        os.chdir(dirName)
        subFileName = glob.glob('*.sub')
        subFullPath = os.path.join(dirName,subFileName[0])

        f = open(subFullPath,'r')
        lines = f.readlines()
        subSystem = []
        for line in lines:
            line = line.split()
            if len(line)!=0 and line[0]=='SUBSYSTEM':
                subSystem.append(str(line[1]))

        # tạo dialog để chọn sink, source
        dialog = Select_Source_Sink(self.parent)
        dialog.Source.SetItems(subSystem)
        dialog.Sink.SetItems(subSystem)
        dialog.ShowModal()

        if dialog.flag == 1:

            result = dialog.SelectSinkSource(event)

            if len(result)!=0:
                result.append(subSystem[1])

            createAutoStaticFile(dirName,result)
            pyPath = os.path.join(dirName,'autoContigency.py')
            with open('output', 'w') as f, silence(f):
                execfile(pyPath)
            
            r = open('output','r')
            lines = r.readlines()
            flag = 1
            case = []
            for line,value in enumerate(lines):
                if 'The Saved Case in file' in value:
                    case.append(value)
                if "ERROR:" in value:
                    errorLine = line
                    flag = 0
                    error = ''
                    for i in range(int(errorLine)-4,int(errorLine)):
                        error = error +'\n'+ lines[i]
                    wx.MessageBox('There is an error in:\n{A}\n {B}'.format(A=case[len(case)-1],B=error))
                    
                    break
            if flag == 1:
                wx.MessageBox('Static Stability Calculation Finish!')
            r.close()
            os.remove('output')
        else:
            event.Skip()

    # tính ổn định tĩnh cho file được chọn
    def Static_Stability_Cal_Selected_Case_Fcn( self, event ):
        PATH = self.Path
        if PATH !='':
            dirName = openFolder(self,'Choose the Folder contain all sub,mon,con files')
            os.chdir(dirName)

            subFileName = glob.glob('*.sub')
            subFullPath = os.path.join(dirName,subFileName[0])
            monfileName = glob.glob('*.mon')
            monFullPath = os.path.join(dirName,monfileName[0])
            confileName = glob.glob('*.con')
            conFullPath = os.path.join(dirName,confileName[0])

            dfxFile = self.PathOrigin[0:-4]+'.dfx'
            pvFile = self.PathOrigin[0:-4]+'-pv'

            f = open(subFullPath,'r')
            lines = f.readlines()
            subSystem = []
            for line in lines:
                line = line.split()
                if len(line)!=0 and line[0]=='SUBSYSTEM':
                    subSystem.append(str(line[1]))

            dialog = Select_Source_Sink(self.parent)
            dialog.Source.SetItems(subSystem)
            dialog.Sink.SetItems(subSystem)
            dialog.ShowModal()

            if dialog.flag == 1:

                result = dialog.SelectSinkSource(event)

                if len(result)!=0:
                    result.append(subSystem[1]) #source,sink,sinkDefault
                    with open('output', 'w') as f, silence(f):
                        self.PowerFlow(event)
                        psspy.dfax([1,1],subFullPath,monFullPath,conFullPath,dfxFile)
                        psspy.pv_engine_6([0,0,0,1,1,0,0,1,0,0,1,1,4,0,0,0,1,0,0,0,0,0,1,1,0],[ 0.5, 100.0, 100.0, 10000., 0.8, 100.0,0.0,0.0],[result[0],result[1],result[2]],dfxFile,"","","",pvFile,"")
                    r = open('output','r')
                    lines = r.readlines()
                    flag = 1

                    for line,value in enumerate(lines):
                        if "ERROR:" in value:
                            errorLine = line
                            flag = 0
                            error = ''
                            for i in range(int(errorLine)-4,int(errorLine)):
                                error = error +'\n'+ lines[i]
                            wx.MessageBox('There is an error in:{A}\n '.format(A=error))
                            break
                    if flag == 1:
                        call(('cmd','/c','start','',os.path.join(self.PathOrigin)))
                        wx.MessageBox("Result has been saved in {b}.".format(b=pvFile+'.pv'))
                    r.close()
                    os.remove('output')

            else:
                event.Skip()
        else:
            wx.MessageBox("Please open an existing case first!")

    # tính toán kháng bù
    def Shunt_Reactor_Cal_Fcn(self,event):
        dirName = os.path.dirname(self.PathOrigin)
        busNum = []
        for i in range(len(self.matrixBus[self.indexFile][:,0])):
            busNum.append(str(self.matrixBus[self.indexFile][i,0])+'-'+self.matrixBus[self.indexFile][i,1])
        # tạo dialog để lấy thông tin về đường dây cần tính bù, số đoạn chia, dung lượng kháng bù, bước thay đổi
        dialog = Line_Tab_Shunt_Reactor(self.parent)
        dialog.fromBus.SetItems(map(str,busNum))
        dialog.Middle.SetItems(map(str,busNum))
        dialog.toBus.SetItems(map(str,busNum))
        dialog.ShowModal()


        if dialog.flag == 1:
            qOffset = float(dialog.textCtrl_QOffset.GetValue())
            step = float(dialog.textCtrl_Step.GetValue())
            n = int(100/(step))
            result = dialog.Next(event)
            
            [fromBus,middle,id1,toBus,id2,segments,tabLineType] = result
            ierr,voltage = psspy.busdat(int(fromBus),'BASE')
            # chỉ có from bus và to bus, chia 8 đoạn
            if tabLineType == 2:
                ierr, rval = psspy.brncur(fromBus,toBus,id2)
                if ierr != 1 and ierr != 2 and ierr != 3 :
                    segmentsBus = []
                    count =0
                    for i in range(1,1000):
                        if not str(i) in busNum:
                            segmentsBus.append(i)
                        if len(segmentsBus)==segments+1:
                            break

                    createLineTabFile(dirName,fromBus,toBus,id2,voltage,segmentsBus)
                    pyPath = os.path.join(dirName,'lineTab.py')
                    execfile(pyPath)
                    # tóm tắt thông tin vào đầu file kết quả
                    f = open(dirName+'\\voltage.txt','w')
                    f.writelines('Parameters:\n')
                    f.writelines('- From Bus: {}\n'.format(dialog.fromBus.GetValue()))
                    f.writelines('- Middle Bus: {}\n'.format(dialog.Middle.GetValue()))
                    f.writelines('- ID: {}\n'.format(dialog.textCtrl_ID1.GetValue()))
                    f.writelines('- To Bus: {}\n'.format(dialog.toBus.GetValue()))
                    f.writelines('- ID: {}\n'.format(dialog.textCtrl_ID2.GetValue()))
                    f.writelines('- Segment numbers: {}\n'.format(dialog.textCtrl_Number.GetValue()))
                    f.writelines('- Q line: {}\n'.format(dialog.textCtrl_QLine.GetValue()))
                    f.writelines('- Q offset: {}\n'.format(dialog.textCtrl_QOffset.GetValue()))
                    f.writelines('- Step(%): {}\n'.format(dialog.textCtrl_Step.GetValue()))
                    f.writelines('\n')
                    f.writelines('# Voltage Origin\n')
                    f.writelines('\n')
                    f.writelines('BUS'.ljust(5,' ')+'VOLTAGE(PU)'.ljust(20,' ')+'VOLTAGE(KV)'.ljust(20,' ')+'\n')
                    for bus in segmentsBus:
                        ierr,voltage = psspy.busdat(int(bus),'KV')
                        ierr,voltagePu = psspy.busdat(int(bus),'PU')
                        f.writelines(str(bus).ljust(5,' ')+str(voltagePu).ljust(20,' ')+str(voltage).ljust(20,' ')+'\n')
                    f.close()
                    # open circuit in FromBus side
                    buCanFromBus = []
                    buLechFromBus1 = []
                    buLechToBus1 = []
                    buCanToBus = []
                    buLechFromBus2 = []
                    buLechToBus2 = []

                    psspy.shunt_data(segmentsBus[0],r"""1""",1,[0.0,0.0])
                    psspy.shunt_data(segmentsBus[len(segmentsBus)-1],r"""1""",1,[0.0,0.0])
                    for i in range(n+1):
                        QbuCan = -i*qOffset/(2*n) # Bù cân 2 đầu đường dây

                        psspy.branch_chng(fromBus,segmentsBus[0],r"""1""",INTGAR1 = 0) # ho mach phia from bus
                        psspy.branch_chng(segmentsBus[len(segmentsBus)-1],toBus,r"""1""",INTGAR1 = 1)

                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 = QbuCan)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 = QbuCan)
                        # Power flow calculation
                        self.PowerFlow(event)
                        vol = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            vol.append(voltage)
                        buCanFromBus.append(vol)

                        # Bù lệch phía From bus
                        QbuLech = -i*qOffset/(n)
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 = QbuLech)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =0)

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech.append(voltage)
                        buLechFromBus1.append(volBuLech)
                        # Bù lệch phía To bus
                        QbuLech = -i*qOffset/(n)
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =0)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 =QbuLech)

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech2 = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech2.append(voltage)
                        buLechToBus1.append(volBuLech2)

                        # Hở mạch phía toBus
                        psspy.branch_chng(segmentsBus[len(segmentsBus)-1],toBus,r"""1""",INTGAR1 = 0)
                        psspy.branch_chng(fromBus,segmentsBus[0],r"""1""",INTGAR1 = 1)

                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 =QbuCan)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 =QbuCan)
                        # Power flow calculation
                        self.PowerFlow(event)

                        volBuCan = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuCan.append(voltage)
                        buCanToBus.append(volBuCan)

                         # Bù lệch phía From bus
                        
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 = QbuLech)  # chinh lai gia tri khang phia FromBus
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =0) # tat khang phia ToBus

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech.append(voltage)
                        buLechFromBus2.append(volBuLech)
                        # Bù lệch phía To bus
                        QbuLech = -i*qOffset/(n)
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 = 0) # tat khang phia FromBus
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 = QbuLech) # chinh lai gia tri khang phia ToBus

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech2 = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech2.append(voltage)
                        buLechToBus2.append(volBuLech2)
                    # xuat ket qua ra file voltage.txt
                    label = 'BUS'.ljust(10,' ')
                    for i in range(n+1):
                        label = label + '{}%'.format(i*step).ljust(10,' ')

                    outName = dirName+'\\voltage.txt'
                    f = open(dirName+'\\voltage.txt','a')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the From Bus ({}) side\n'.format(fromBus))
                    f.writelines('\n')
                    f.writelines(label+'\n')

                    # rewrite file

                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buCanFromBus[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the From Bus ({a}) side, Q compensation on Bus {a}.\n'.format(a=fromBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechFromBus1[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the From Bus ({a}) side,  Q compensation on Bus {b}.\n'.format(a=fromBus,b = toBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechToBus1[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    #  To bus
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the To Bus ({}) side\n'.format(toBus))
                    f.writelines('\n')
                    f.writelines(label+'\n')
                    
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buCanToBus[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the To Bus ({a}) side,  Q compensation on Bus {b}.\n'.format(a = toBus,b = fromBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechFromBus2[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the To Bus ({a}) side,  Q compensation on Bus {a}.\n'.format(a=toBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechToBus2[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.close()
                    wx.MessageBox('Result has been saved in {}'.format(outName))
            elif tabLineType == 3: # nếu có đủ frombus, middle bus và tobus, chia 16 đoạn
                ierr1, rval1 = psspy.brncur(fromBus,middle,id1)
                ierr2, rval2 = psspy.brncur(fromBus,toBus,id2)

                if  ierr1 != 1 and ierr2 != 1 and ierr1 != 2 and ierr2 != 2 and ierr1 != 3 and ierr2 != 3 :
                    segmentsBus = []
                    count =0
                    for i in range(1,1000):
                        if not str(i) in busNum:
                            segmentsBus.append(i)
                        if count < segments:
                            count+=1
                        else:
                            break
                    segmentsBus[8] = middle

                    createLineTabFile3Bus(dirName,fromBus,middle,id1,toBus,id2,voltage,segmentsBus)
                    pyPath = os.path.join(dirName,'lineTab.py')
                    execfile(pyPath)

                    f = open(dirName+'\\voltage.txt','w')
                    f.writelines('# Voltage Origin\n')
                    f.writelines('\n')
                    f.writelines('BUS'.ljust(5,' ')+'VOLTAGE(PU)'.ljust(20,' ')+'VOLTAGE(KV)'.ljust(20,' ')+'\n')
                    for bus in segmentsBus:
                        ierr,voltage = psspy.busdat(int(bus),'KV')
                        ierr,voltagePu = psspy.busdat(int(bus),'PU')
                        f.writelines(str(bus).ljust(5,' ')+str(voltagePu).ljust(20,' ')+str(voltage).ljust(20,' ')+'\n')
                    f.close()
                    # open circuit in FromBus side
                    buCanFromBus = []
                    buLechFromBus1 = []
                    buLechToBus1 = []
                    buCanToBus = []
                    buLechFromBus2 = []
                    buLechToBus2 = []

                    psspy.shunt_data(segmentsBus[0],r"""1""",1,[0.0,0.0])
                    psspy.shunt_data(segmentsBus[len(segmentsBus)-1],r"""1""",1,[0.0,0.0])

                    for i in range(n+1):
                        QbuCan = -i*qOffset/(2*n) # Bù đều 2 đầu đường dây
                        # open circuit in FromBus side
                        psspy.branch_chng(fromBus,segmentsBus[0],r"""1""",INTGAR1 = 0)
                        psspy.branch_chng(segmentsBus[len(segmentsBus)-1],toBus,r"""1""",INTGAR1 = 1)
                        
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 = QbuCan)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 = QbuCan)
                        # Power flow calculation
                        self.PowerFlow(event)

                        vol = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            vol.append(voltage)
                        buCanFromBus.append(vol)
                        
                        QbuLech = -i*qOffset/(n)
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 = QbuLech)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =0)

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech.append(voltage)
                        buLechFromBus1.append(volBuLech)
                        # bu lech To bus
                        QbuLech = -i*qOffset/(n)
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =0)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 =QbuLech)

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech2 = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech2.append(voltage)
                        buLechToBus1.append(volBuLech2)
                         # open circuit in toBus side
                        psspy.branch_chng(segmentsBus[len(segmentsBus)-1],toBus,r"""1""",INTGAR1 = 0)
                        psspy.branch_chng(fromBus,segmentsBus[0],r"""1""",INTGAR1 = 1)

                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 =QbuCan)
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 =QbuCan)
                        # Power flow calculation
                        self.PowerFlow(event)

                        volBuCan = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuCan.append(voltage)
                        buCanToBus.append(volBuCan)

                         # bu lech From bus
                        
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 =1,REALAR2 = QbuLech)  # chinh lai gia tri khang phia FromBus
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =0) # tat khang phia ToBus

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech.append(voltage)
                        buLechFromBus2.append(volBuLech)
                        # bu lech To bus
                        QbuLech = -i*qOffset/(n)
                        psspy.shunt_chng(segmentsBus[0],r"""1""",INTGAR1 = 0) # tat khang phia FromBus
                        psspy.shunt_chng(segmentsBus[len(segmentsBus)-1],r"""1""",INTGAR1 =1,REALAR2 = QbuLech) # chinh lai gia tri khang phia ToBus

                        # Power flow calculation
                        self.PowerFlow(event)
                        volBuLech2 = []
                        for bus in segmentsBus:
                            ierr,voltage = psspy.busdat(int(bus),'KV')
                            ierr,voltagePu = psspy.busdat(int(bus),'PU')
                            volBuLech2.append(voltage)
                        buLechToBus2.append(volBuLech2)
                    # mo file ghi ket qua
                    label = 'BUS'.ljust(10,' ')
                    for i in range(n+1):
                        label = label + '{}%'.format(i*step).ljust(10,' ')
                    
                    # Ghi kết quả ra file voltage.txt

                    outName = dirName+'\\voltage.txt'
                    f = open(dirName+'\\voltage.txt','a')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the From Bus ({}) side\n'.format(fromBus))
                    f.writelines('\n')
                    f.writelines(label+'\n')
                    # rewrite file

                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buCanFromBus[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the From Bus ({a}) side, Q compensation on Bus {a}.\n'.format(a=fromBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechFromBus1[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the From Bus ({a}) side,  Q compensation on Bus {b}.\n'.format(a=fromBus,b = toBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechToBus1[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    # To bus
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the To Bus ({}) side\n'.format(toBus))
                    f.writelines('\n')
                    f.writelines(label+'\n')
                    
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buCanToBus[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the To Bus ({a}) side,  Q compensation on Bus {b}.\n'.format(a = toBus,b = fromBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechFromBus2[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.writelines('\n')
                    f.writelines('# Open Circuit on the To Bus ({a}) side,  Q compensation on Bus {a}.\n'.format(a=toBus))
                    for i,bus in enumerate(segmentsBus):
                        s = ''
                        for j in range(n+1):
                            s = s + '{:.4f}'.format((buLechToBus2[j][i])).ljust(10,' ')
                        f.writelines(str(bus).ljust(10,' ')+s+'\n')
                    f.close()
                    wx.MessageBox('Result has been saved in {}'.format(outName))

        else:
            event.Skip()

    # tính kháng bù từ file python có sẵn, chỉ thực hiện chia đoạn đường dây, việc lắp kháng và đo điện áp do người dùng tự thực hiện
    def Shunt_Reactor_Cal_From_File_Fcn(self,event):
        PATH = self.Path
        if PATH != '':
            dirName = os.path.dirname(self.PathOrigin)
            pyFile = openFile(self,'Choose the created python file', "Python file (*.py)|*.py|All files|*")
            dirname = os.path.dirname(pyFile)
            path = os.path.join(dirname,'shunt_reactor.py')
            f = open(path,'w')
            f.write("import pssepath\n")
            f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
            f.write("sys.path.append(PSSE_LOCATION)\n")
            f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
            f.write("pssepath.add_pssepath(33)\n")
            f.write("import psspy \n")
            r = open(pyFile,'r')

            for line in r:
                if not ('import' in line or  'PSSE_LOCATION' in line or 'add_pssepath(33)' in line):
                    f.write(line)
                if "flat_2" in line:
                    break 

            f.write('psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n')
            f.write('psspy.fdns()\n')
            f.write('psspy.fnsl()\n')
            f.close()
            execfile(path)
            os.remove(path)
            psspy.save(self.PathOrigin)
            call(('cmd','/c','start','',os.path.join(self.PathOrigin)))
                
    def PowerFlow(self,event):
        # Power flow calculation
        psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
        psspy.fdns()
        psspy.fnsl()
                        
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])\n")
            f.writelines("psspy.fdns()\n")
            f.writelines("psspy.fnsl()\n")
            f.close()

    def _n1_choose_file(self, title, wildcard):
        dialog = wx.FileDialog(self.parent, title, wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        try:
            if dialog.ShowModal() == wx.ID_OK:
                return dialog.GetPath()
            return ''
        finally:
            dialog.Destroy()

    def _n1_unique_output_path(self, sav_path, network_label):
        directory = os.path.dirname(sav_path)
        original_name = os.path.splitext(os.path.basename(sav_path))[0]
        suffix = safe_filename(network_label)
        candidate = os.path.join(directory, '%s - %s.sav' % (original_name, suffix))
        number = 2
        while os.path.exists(candidate):
            candidate = os.path.join(directory, '%s - %s (%s).sav' %
                                     (original_name, suffix, number))
            number += 1
        return candidate

    def _n1_show_summary(self, saved_count, not_converged, failed, log_path):
        lines = ['Saved: %s file(s)' % saved_count,
                 'Not converged but saved: %s case(s)' % len(not_converged)]
        if not_converged:
            lines.extend(['  - %s' % item for item in not_converged])
        lines.append('Failed or unresolved: %s case(s)' % len(failed))
        if failed:
            lines.extend(['  - %s' % item for item in failed])
        lines.append('Details: %s' % log_path)

        dialog = wx.Dialog(self.parent, wx.ID_ANY, 'Create N-1 SAV Files',
                           size=(650, 420))
        panel = wx.Panel(dialog)
        text = wx.TextCtrl(panel, wx.ID_ANY, '\n'.join(lines),
                           style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        ok_button = wx.Button(panel, wx.ID_OK, 'OK')
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(ok_button, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        panel.SetSizer(sizer)
        dialog.ShowModal()
        dialog.Destroy()

    def Create_N1_SAV_Files(self, event):
        sav_path = self._n1_choose_file(
            'Choose original SAV file', 'PSS/E SAV files (*.sav)|*.sav|All files|*.*')
        if not sav_path:
            return
        acc_path = self._n1_choose_file(
            'Choose ACC contingency results file', 'PSS/E ACC files (*.acc)|*.acc|All files|*.*')
        if not acc_path:
            return

        summary = pssarrays.accc_summary(acc_path)
        if getattr(summary, 'ierr', 0):
            wx.MessageBox('Unable to read ACC file:\n%s' % acc_path,
                          'Create N-1 SAV Files', wx.OK | wx.ICON_ERROR)
            return

        labels = []
        for label in getattr(summary, 'colabel', []):
            text = as_text(label)
            if text and text.upper() != 'BASE CASE' and text not in labels:
                labels.append(text)
        if not labels:
            wx.MessageBox('No contingency cases were found in the ACC file.',
                          'Create N-1 SAV Files', wx.OK | wx.ICON_INFORMATION)
            return

        init_ierr = psspy.psseinit(50000)
        if init_ierr:
            wx.MessageBox('Unable to initialize PSS/E for the N-1 calculation (ierr=%s).' % init_ierr,
                          'Create N-1 SAV Files', wx.OK | wx.ICON_ERROR)
            return

        case_ierr = psspy.case(sav_path)
        if case_ierr:
            wx.MessageBox('Unable to open original SAV file (PSS/E ierr=%s):\n%s' %
                          (case_ierr, sav_path),
                          'Create N-1 SAV Files', wx.OK | wx.ICON_ERROR)
            return

        inventory = three_winding_inventory(psspy)
        cases = []
        for label in labels:
            try:
                solution = pssarrays.accc_solution(acc_path, label, 'contingency', 0.5, 5.0)
                description = as_text(getattr(solution, 'codesc', ''))
                element = resolve_contingency(psspy, label, description, inventory)
            except Exception as error:
                description = ''
                element = {'state': 'unresolved',
                           'reason': 'Could not read ACC contingency: %s' % as_text(error)}
            if element.get('state') == 'ready':
                display = '%s | %s' % (label, element['display_name'])
            else:
                display = '%s | UNRESOLVED: %s' % (label, element.get('reason', 'unknown reason'))
            cases.append({'label': label, 'description': description,
                          'element': element, 'display': display})

        selector = wx.MultiChoiceDialog(self.parent,
                                        'Select ACC contingencies. Each selection switches off one element.',
                                        'Create N-1 SAV Files',
                                        [case['display'] for case in cases])
        try:
            if selector.ShowModal() != wx.ID_OK:
                return
            selected_indexes = selector.GetSelections()
        finally:
            selector.Destroy()
        if not selected_indexes:
            return

        saved_count = 0
        not_converged = []
        failed = []
        log_path = os.path.join(os.path.dirname(sav_path), 'log.txt')
        log_lines = ['Create N-1 SAV Files', 'Original SAV: %s' % sav_path,
                     'ACC file: %s' % acc_path]
        try:
            for index in selected_indexes:
                case = cases[index]
                element = case['element']
                if element.get('state') != 'ready':
                    message = '%s | %s' % (case['label'], element.get('reason', 'Unresolved case'))
                    failed.append(message)
                    log_lines.append('FAILED OR UNRESOLVED: %s' % message)
                    continue

                if psspy.case(sav_path):
                    message = '%s | Could not reopen original SAV.' % case['label']
                    failed.append(message)
                    log_lines.append('FAILED: %s' % message)
                    continue
                ierr = apply_outage(psspy, element)
                if ierr:
                    message = '%s | Could not open %s (ierr=%s).' % (
                        case['label'], element['display_name'], ierr)
                    failed.append(message)
                    log_lines.append('FAILED: %s' % message)
                    continue

                self.PowerFlow(event)
                solved_ierr = psspy.solved()
                output_path = self._n1_unique_output_path(sav_path, case['label'])
                save_ierr = psspy.save(output_path)
                if save_ierr:
                    message = '%s | Could not save %s (ierr=%s).' % (
                        case['label'], output_path, save_ierr)
                    failed.append(message)
                    log_lines.append('FAILED: %s' % message)
                    continue

                saved_count += 1
                if solved_ierr:
                    message = '%s | %s | %s' % (case['label'], element['display_name'], output_path)
                    not_converged.append(message)
                    log_lines.append('NOT CONVERGED BUT SAVED: %s' % message)
                else:
                    log_lines.append('SAVED: %s | %s | %s' %
                                     (case['label'], element['display_name'], output_path))
        finally:
            psspy.case(sav_path)

        log_file = codecs.open(log_path, 'a', 'utf-8')
        try:
            log_file.write('\n'.join(log_lines) + '\n\n')
        finally:
            log_file.close()
        self._n1_show_summary(saved_count, not_converged, failed, log_path)

    # tính giới hạn truyền tải liên miền, tương tự tính ổn định tĩnh cho 4 trường hợp và tổng hợp 4
    # trường hợp: giới hạn truyền tải trung - bắc, bắc - trung, trung - nam, nam - trung
    def InterRegionLimit(self,event):
        # tạo file sub, mon, con
        createSubMonConForStaticStability()
        dfxFile = self.PathOrigin[0:-4]+'.dfx'
        pvFile = self.PathOrigin[0:-4]+'-pv'
        SOURCE = r"""NGUON-BAC""" # nguon bac, luoi trung nam/ nguon trung nam, luoi bac
        SINK = r"""LUOI-TRUNGNAM"""
        SINKDEFAULT = r"""NGUON-BACTRUNG"""
        self.PowerFlow(event)
        psspy.dfax([1,1],'savnw_Sub.sub','savnw_Mon.mon','savnw_Con.con',dfxFile)
        psspy.pv_engine_6([0,0,0,1,1,0,0,1,0,0,1,1,4,0,0,0,1,0,0,0,0,0,1,1,0],[ 0.5, 100.0, 100.0, 10000., 0.8, 100.0,0.0,0.0],[SOURCE,SINK,SINKDEFAULT],dfxFile,"","","",pvFile,"")

        rlst            = pssarrays.pv_summary(pvFile)
        lbl             = rlst.colabel
        ierr = pssarrays.pv_solution_report(pvFile,lbl,'report_PV.txt')

        f = open('report_PV.txt','r')
        lines = f.readlines()
        resultLine = 0
        result = []
        val = 0
        for i,line in enumerate(lines):
            if 'INTERFACE BAC->TRUNG2' in line:
                line = line.split()
                val = line[len(line)-1]
                break
        result.append(val)
        f.close()

        # Nguon trung nam , luoi bac
        SOURCE = r"""NGUON-TRUNGNAM""" # nguon bac, luoi trung nam/ nguon trung nam, luoi bac
        SINK = r"""LUOI-BAC"""
        SINKDEFAULT = r"""NGUON-BACTRUNG"""
        self.PowerFlow(event)
        psspy.dfax([1,1],'savnw_Sub.sub','savnw_Mon.mon','savnw_Con.con',dfxFile)
        psspy.pv_engine_6([0,0,0,1,1,0,0,1,0,0,1,1,4,0,0,0,1,0,0,0,0,0,1,1,0],[ 0.5, 100.0, 100.0, 10000., 0.8, 100.0,0.0,0.0],[SOURCE,SINK,SINKDEFAULT],dfxFile,"","","",pvFile,"")
        ierr = pssarrays.pv_solution_report(pvFile,lbl,'report_PV.txt')

        f = open('report_PV.txt','r')
        lines = f.readlines()
        val = 0
        for i,line in enumerate(lines):
            if 'INTERFACE BAC->TRUNG2' in line:
                line = line.split()
                val = line[len(line)-1]
                break
        result.append(val)
        f.close()

        SOURCE = r"""NGUON-BACTRUNG""" # nguon trung-luoi bac, nguon bac-luoi trung
        SINK = r"""LUOI-NAM"""
        SINKDEFAULT = r"""NGUON-BACTRUNG"""
        self.PowerFlow(event)
        psspy.dfax([1,1],'savnw_Sub.sub','savnw_Mon.mon','savnw_Con.con',dfxFile)
        psspy.pv_engine_6([0,0,0,1,1,0,0,1,0,0,1,1,4,0,0,0,1,0,0,0,0,0,1,1,0],[ 0.5, 100.0, 100.0, 10000., 0.8, 100.0,0.0,0.0],[SOURCE,SINK,SINKDEFAULT],dfxFile,"","","",pvFile,"")
        ierr = pssarrays.pv_solution_report(pvFile,lbl,'report_PV.txt')

        f = open('report_PV.txt','r')
        lines = f.readlines()
        val = 0
        for i,line in enumerate(lines):
            if 'INTERFACE TRUNG->NAM2' in line:
                line = line.split()
                val = line[len(line)-1]
                break
        result.append(val)
        f.close()

        SOURCE = r"""NGUON-NAM""" # nguon trung-luoi bac, nguon bac-luoi trung
        SINK = r"""LUOI-BACTRUNG"""
        SINKDEFAULT = r"""NGUON-BACTRUNG"""
        self.PowerFlow(event)
        psspy.dfax([1,1],'savnw_Sub.sub','savnw_Mon.mon','savnw_Con.con',dfxFile)
        psspy.pv_engine_6([0,0,0,1,1,0,0,1,0,0,1,1,4,0,0,0,1,0,0,0,0,0,1,1,0],[ 0.5, 100.0, 100.0, 10000., 0.8, 100.0,0.0,0.0],[SOURCE,SINK,SINKDEFAULT],dfxFile,"","","",pvFile,"")
        ierr = pssarrays.pv_solution_report(pvFile,lbl,'report_PV.txt')

        f = open('report_PV.txt','r')
        lines = f.readlines()
        val = 0
        for i,line in enumerate(lines):
            if 'INTERFACE TRUNG->NAM2' in line:
                line = line.split()
                val = line[len(line)-1]
                break
        result.append(val)
        f.close()
        wx.MessageBox('Gioi han truyen tai lien mien:\n + Nguon Bac - luoi Trung Nam: {a} \n + Nguon Trung Nam - luoi Bac: {b}\n + Nguon Bac Trung - luoi Nam: {c}\n + Nguon Nam - luoi Bac Trung: {d}\n'.format(a=result[0],b=result[1],c=result[2],d=result[3]))
        # loại bỏ các file trung gian
        os.remove('report_PV.txt')
        os.remove('savnw_Sub.sub')
        os.remove('savnw_Mon.mon')
        os.remove('savnw_Con.con')

                





    


