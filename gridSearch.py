# -*- coding: utf-8 -*-
from Tool_V7 import MyFrame1
import time
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
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadMachineTab,loadShuntTab,load2windTab,load3windTab,loadLoadTab,loadSourceLoadInfo
from math import *
from decimal import *
from dialogAddBus import Add_New_Bus

cellValue = 0
cellVal = 0
row = 0
col = 0
busNum = 0
busName = ''
busArea = 0
busZone = 0
busBaseKV = 0.0
busVM = 0.0
busVA = 0.0
owener = 0
code = 0
TWOPLACE = Decimal(10)**-2
    
class CustomGridSearch(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.Path = ''
        self.PathFile = [[]]
        self.parent = parent
        self.fileInfoTranspose = []
        self.matrixBus = []
        self.matrixArea = []
        self.matrixZone = []
        self.matrixSource = []
        self.matrixLoad = []
        self.matrixShunt = []
        self.matrix2Wind = []
        self.matrix3Wind = []
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridSource = wx.grid.Grid
        self.myGridLoad = wx.grid.Grid
        self.myGridShunt = wx.grid.Grid
        self.myGrid2Wind = wx.grid.Grid
        self.myGrid3Wind = wx.grid.Grid
        self.indexFile = 0
        self.uk = 0
        self.flagSynch  = 0

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng thông tin bus
    def on_cell_change_grid_search( self, event ):

        if (row == len(self.matrixBus[0]) and str(self.myGridBus.GetCellValue(row,0)) in self.matrixBus[self.indexFile][:,0]):
            wx.MessageBox("This number is existing in onGridCellChange3!")
        elif (self.uk == 13):
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    if i==0:
                        change(self.myGridBus,self.matrixBus[self.indexFile],row-1,col,cellVal,self.parent.macroFile,0)
                    else:
                        change(self.myGridBus,self.matrixBus[self.indexFile],row-1,col,cellVal,self.parent.macroFile,1)
                    psspy.save(path)
            else:
                change(self.myGridBus,self.matrixBus[self.indexFile],row-1,col,cellVal,self.parent.macroFile,0)
                psspy.save(self.Path)
        else:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    if i == 0:
                        change(self.myGridBus,self.matrixBus[self.indexFile],row,col,cellValue,self.parent.macroFile,0)
                    else:
                        change(self.myGridBus,self.matrixBus[self.indexFile],row,col,cellValue,self.parent.macroFile,1)
                    psspy.save(path)
            else:
                change(self.myGridBus,self.matrixBus[self.indexFile],row,col,cellValue,self.parent.macroFile,0)
                psspy.save(self.Path)
        # update
        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateBus(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateBus(event,self.indexFile,self.Path)
                # self.parent.UpdatedData(event,self.indexFile,self.Path)
            # self.parent.onUpdateFcn(event)
        elif self.parent.flagPaste == 0:
            dt=np.dtype("<S16")
            a = np.array([],dt)
            self.matrixBus[self.indexFile] = loadBusTab(self.Path)
            for row1 in range(len(self.matrixBus[self.indexFile])):
                for column1 in range(len(self.matrixBus[self.indexFile][0])):
                    self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))
            self.parent.onUpdateFcn(event)

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng thông tin bus
    def on_cell_right_click_grid_search( self, event ):
        menus = [(wx.NewId(), "Add New Bus", self.addNew),
                 (wx.NewId(), "Turn On/Off Bus", self.turnOnOff),
                #  (wx.NewId(), "Split Bus", self.splitBus),
                 (wx.NewId(), "Delete Bus", self.deleteBus)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.gridSearch.PopupMenu(popup_menu, self.gridSearch.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return
    
    # chức năng thực hiện tại ô được chọn của bảng thông tin bus
    def on_selected_cell_grid_search( self, event ):
        global row,col,cellValue,cellVal,busNum,busName,busArea,busZone,busBaseKV,busVM,busVA,owner,code
        row = event.GetRow()
        col = event.GetCol()
        colLabel = self.myGridBus.GetColLabelValue(col)
        cellValue = self.myGridBus.GetCellValue(row,col)
        if row>0:
            cellVal = self.myGridBus.GetCellValue(row-1,col)
        busNum = int(self.myGridBus.GetCellValue(row,0))
        busName = self.myGridBus.GetCellValue(row,1)
        busArea = int(self.myGridBus.GetCellValue(row,3))
        busZone = int(self.myGridBus.GetCellValue(row,5))
        owner = int(self.myGridBus.GetCellValue(row,7))
        code = int(self.myGridBus.GetCellValue(row,8))
        busBaseKV = float(self.myGridBus.GetCellValue(row,2))
        busVM = float(self.myGridBus.GetCellValue(row,9)) # Voltage magnitude
        busVA = float(self.myGridBus.GetCellValue(row,10)) # Voltage angle
    
    def on_key_down_grid_search( self, event ):
        event.Skip()

    # Thêm bus mới
    def Add_New_Bus(self,event):
        addBusDialog = Add_New_Bus(self.parent)
        busNumList = []
        voltageList = []
        areaList = []
        zoneList = []
        ownerList = []
        codeList = []
        for i in range(len(self.matrixBus[self.indexFile])):
            busNumList.append(str(self.matrixBus[self.indexFile][i,0])+'-'+str(self.matrixBus[self.indexFile][i,1]))
            voltage = self.matrixBus[self.indexFile][i,2]
            owner = self.matrixBus[self.indexFile][i,7]
            code = self.matrixBus[self.indexFile][i,8]
            if not voltage in voltageList: 
                voltageList.append(self.matrixBus[self.indexFile][i,2])
            if not owner in ownerList:
                ownerList.append(self.matrixBus[self.indexFile][i,7])
            if not code in codeList:
                codeList.append(self.matrixBus[self.indexFile][i,8])

        for i in range(len(self.matrixArea[self.indexFile])):
            areaList.append(str(self.matrixArea[self.indexFile][i,0]))
        for i in range(len(self.matrixZone[self.indexFile])):
            zoneList.append(str(self.matrixZone[self.indexFile][i,0]))


        addBusDialog.fromBusNum.SetItems(busNumList)
        addBusDialog.comboBoxVoltageLevel.SetItems(voltageList)
        addBusDialog.comboBoxArea.SetItems(areaList)
        addBusDialog.comboBoxZone.SetItems(zoneList)
        addBusDialog.flagSynch = self.parent.flagSynch
        addBusDialog.macroFile = self.parent.macroFile
        addBusDialog.Path = self.Path 
        addBusDialog.PathFile = self.PathFile
        addBusDialog.ShowModal()

        if not addBusDialog.onClose(event) :
            event.Skip()
        elif self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateBus(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateBus(event,self.indexFile,self.Path)
        else:
            # print('-------------con day la cap nhat sau nhe!!!')
            dt=np.dtype("<S16")
            a = np.array([],dt)
            self.matrixBus[self.indexFile] = loadBusTab(self.Path)
            for row1 in range(len(self.matrixBus[self.indexFile])):
                for column1 in range(len(self.matrixBus[self.indexFile][0])):
                    self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))

            self.parent.onUpdateFcn(event)

    # Cập nhật bảng bus
    def onUpdateBus(self,event,indexfile,path):
        self.indexFile = indexfile
        self.Path = path
        for row1 in range(self.myGridBus.GetNumberRows()):
            for column1 in range(self.myGridBus.GetNumberCols()): 
                self.myGridBus.SetCellValue(row1,column1,"")
        self.matrixBus[self.indexFile] = loadBusTab(self.Path)
        for row1 in range(len(self.matrixBus[self.indexFile])):
            for column1 in range(len(self.matrixBus[self.indexFile][0])):
                self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))
        self.parent.onUpdateFcn(event)

    def UpdatedData(self,event,indexfile,path): # only for reload page
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
            for row1 in range(self.myGridArea.GetNumberRows()):
                for column1 in range(self.myGridArea.GetNumberCols()):
                    self.myGridArea.SetCellValue(row1,column1,"")
            for row1 in range(self.myGridZone.GetNumberRows()):
                for column1 in range(self.myGridZone.GetNumberCols()):
                    self.myGridZone.SetCellValue(row1,column1,"")
            for row1 in range(self.myGridBus.GetNumberRows()):
                for column1 in range(self.myGridBus.GetNumberCols()): 
                    self.myGridBus.SetCellValue(row1,column1,"")
            for row1 in range(self.myGridSource.GetNumberRows()):
                for column1 in range(27): 
                    self.myGridSource.SetCellValue(row1,column1,"")
            for row1 in range(self.gridLoad.GetNumberRows()):
                for column1 in range(12):
                    self.gridLoad.SetCellValue(row1,column1,"")
            for row1 in range(self.gridShunt.GetNumberRows()):
                for column1 in range(self.gridShunt.GetNumberCols()):
                    self.gridShunt.SetCellValue(row1,column1,"")
            for row1 in range(self.myGrid2Wind.GetNumberRows()):
                for column1 in range(self.myGrid2Wind.GetNumberCols()):
                    self.myGrid2Wind.SetCellValue(row1,column1,"")
            for row1 in range(self.myGrid3Wind.GetNumberRows()):
                for column1 in range(self.myGrid3Wind.GetNumberCols()):
                    self.myGrid3Wind.SetCellValue(row1,column1,"")

            self.matrixArea[self.indexFile] = loadAreaInfo(self.Path)
            for row1 in range(len(self.matrixArea[self.indexFile])):
                for column1 in range(len(self.matrixArea[self.indexFile][0])):
                    self.myGridArea.SetCellValue(row1,column1,str(self.matrixArea[self.indexFile][row1][column1]))

            self.matrixZone[self.indexFile] = loadZoneInfo(self.Path)
            for row2 in range(len(self.matrixZone[self.indexFile])):
                for column2 in range(len(self.matrixZone[self.indexFile][0])):
                    self.myGridZone.SetCellValue(row2,column2,str(self.matrixZone[self.indexFile][row2][column2])) 

            self.matrixBus[self.indexFile] = loadBusTab(self.Path)
            for row1 in range(len(self.matrixBus[self.indexFile])):
                for column1 in range(len(self.matrixBus[self.indexFile][0])):
                    self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))

            self.matrixSource[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixSource[self.indexFile])):
                for column1 in range(len(self.matrixSource[self.indexFile][0])):
                    self.myGridSource.SetCellValue(row1,column1,str(self.matrixSource[self.indexFile][row1][column1]))
                coff = self.myGridSource.GetCellValue(row1,13)
                self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))

            self.matrixLoad[self.indexFile] = loadLoadTab(self.Path)
            for row1 in range(len(self.matrixLoad[self.indexFile])):
                for column1 in range(len(self.matrixLoad[self.indexFile][0])):
                    self.myGridLoad.SetCellValue(row1,column1,str(self.matrixLoad[self.indexFile][row1][column1]))

            self.matrixShunt[self.indexFile] = loadShuntTab(self.Path)
            for row1 in range(len(self.matrixShunt[self.indexFile])):
                for column1 in range(len(self.matrixShunt[self.indexFile][0])):
                    self.myGridShunt.SetCellValue(row1,column1,str(self.matrixShunt[self.indexFile][row1][column1]))

            self.matrix2Wind[self.indexFile] = load2windTab(self.Path)
            for row1 in range(len(self.matrix2Wind[self.indexFile])):
                for column1 in range(len(self.matrix2Wind[self.indexFile][0])):
                    self.myGrid2Wind.SetCellValue(row1,column1,str(self.matrix2Wind[self.indexFile][row1][column1]))

            self.matrix3Wind[self.indexFile] = load3windTab(self.Path)
            for row1 in range(len(self.matrix3Wind[self.indexFile])):
                for column1 in range(len(self.matrix3Wind[self.indexFile][0])):
                    self.myGrid3Wind.SetCellValue(row1,column1,str(self.matrix3Wind[self.indexFile][row1][column1]))
                
            sourceLoad = loadSourceLoadInfo(self.Path)
            [totalPgen,totalLoad, totalPgenNorth,totalLoadNorth,totalPgenCentral,totalLoadCentral,totalPgenSouth,totalLoadSouth,ratio] = sourceLoad
            for i in range(len(ratio)):
                self.parent.m_grid6.SetCellValue(i,29, str((Decimal(ratio[i]).quantize(TWOPLACE))))

            self.parent.totalSource.SetValue(str(Decimal(totalPgen).quantize(TWOPLACE)))
            self.parent.totalLoad.SetValue(str(Decimal(totalLoad).quantize(TWOPLACE)))
            self.parent.sourceNorth.SetValue(str(Decimal(totalPgenNorth).quantize(TWOPLACE)))
            self.parent.loadNorth.SetValue(str(Decimal(totalLoadNorth).quantize(TWOPLACE)))
            self.parent.sourceCentral.SetValue(str(Decimal(totalPgenCentral).quantize(TWOPLACE)))
            self.parent.loadCentral.SetValue(str(Decimal(totalLoadCentral).quantize(TWOPLACE)))
            self.parent.sourceSouth.SetValue(str(Decimal(totalPgenSouth).quantize(TWOPLACE)))
            self.parent.loadSouth.SetValue(str(Decimal(totalLoadSouth).quantize(TWOPLACE)))

    def addNew(self, e):
        self.parent.Add_New_Bus(e)

    # Bật/tắt bus
    def Turn_On_Off( self, event ):
        busCode = self.myGridBus.GetCellValue(row,8)
        if int(busCode) == 4:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.recn(busNum)
                    psspy.save(path)
            else:
                psspy.recn(busNum)
                psspy.save(self.Path)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.recn({})\n""".format(busNum))
                f.close()
        else:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.dscn(busNum)
                    psspy.save(path)
            else:
                psspy.dscn(busNum)
                psspy.save(self.Path)

            if self.parent.macroFile != '':
                f = open(self.parent.macroFile,'a')
                f.writelines("""psspy.dscn({})\n""".format(busNum))
                f.close()

        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    # self.onUpdateBus(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
                    self.matrixBus[i] = loadBusTab(path)
                    for row1 in range(len(self.matrixBus[i])):
                        for column1 in range(len(self.matrixBus[i][0])):
                            self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[i][row1][column1]))
            else:
                # self.onUpdateBus(event,self.indexFile,self.Path)
                # self.parent.UpdatedData(event,self.indexFile,self.Path)
                self.matrixBus[self.indexFile] = loadBusTab(self.Path)
                for row1 in range(len(self.matrixBus[self.indexFile])):
                    for column1 in range(len(self.matrixBus[self.indexFile][0])):
                        self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))
        else:
            dt=np.dtype("<S16")
            a = np.array([],dt)
            self.matrixBus[self.indexFile] = loadBusTab(self.Path)

            for row1 in range(len(self.matrixBus[self.indexFile])):
                for column1 in range(len(self.matrixBus[self.indexFile][0])):
                    self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))
            self.parent.onUpdateFcn(event)

    def turnOnOff(self,event):
        self.parent.Turn_On_Off(event)
        
    def splitBus(self,event):
        print("This is splitBus")
    
    def tapLine(self,event):
        print("This is tapLine")

    # Xóa bus
    def Delete_Bus_Fcn( self, event ):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.bsysinit(1)
                psspy.bsyso(1,  int(busNum))
                psspy.extr(1,0,[0,0])
                psspy.save(path)
        else:
            psspy.bsysinit(1)
            psspy.bsyso(1,  int(busNum))
            psspy.extr(1,0,[0,0])
            psspy.save(self.Path)
        
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.write("psspy.bsysinit(1)\n")
            f.write("psspy.bsyso(1,  {})\n".format(int(busNum)))
            f.write("psspy.extr(1,0,[0,0])\n")
            f.close()

        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateBus(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateBus(event,self.indexFile,self.Path)
                # self.parent.UpdatedData(event,self.indexFile,self.Path)
        else:
            dt=np.dtype("<S16")
            a = np.array([],dt)
            self.matrixBus[self.indexFile] = loadBusTab(self.Path)
            for row1 in range(len(self.matrixBus[self.indexFile])):
                for column1 in range(len(self.matrixBus[self.indexFile][0])):
                    self.myGridBus.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))
            self.parent.onUpdateFcn(event)

    def deleteBus(self,event):
        self.parent.Delete_Bus_Fcn(event)
