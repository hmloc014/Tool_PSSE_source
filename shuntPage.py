# -*- coding: utf-8 -*- 
from Tool_V2 import MyFrame1
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
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadMachineTab,loadShuntTab,loadLoadTab,loadSourceLoadInfo
from math import *
from decimal import *
from dialogAddShunt import Add_New_Shunt_Dialog
from ui_performance import batched_grid_update, clear_grid, profiled

cellValue = 0
cellVal = 0
row = 0
col = 0
busNum = 0
busName = ''
busArea = 0
busZone = 0
busID = ''
shuntStatus = 0
pgen = 0.0
qgen = 0.0
pmax = 0.0
qmax = 0.0
busNumUpper = 0
busNameUpper= ''
busAreaUpper=0
busZoneUpper=0
busIDUpper =''
shuntStatusUpper = 0
pgenUpper = 0.0
qgenUpper = 0.0
pmaxUpper = 0.0
qmaxUpper = 0.0

TWOPLACE = Decimal(10)**-2
    
class CustomGridShunt(MyFrame1):
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
        self.matrixSource = []
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridShunt = wx.grid.Grid
    
    # chức năng thực hiện tại ô được chọn của bảng shunt
    def on_selected_cell_grid_shunt( self, event ):
        global row,col,cellValue,cellVal,busNum,busName,busArea,busZone,busID,shuntStatus,pgen,qgen,pmax,qmax
        global busNumUpper,busNameUpper,busAreaUpper,busZoneUpper,busIDUpper,shuntStatusUpper,pgenUpper,qgenUpper,pmaxUpper,qmaxUpper
        row = event.GetRow()
        col = event.GetCol()
        colLabel = self.myGridShunt.GetColLabelValue(col)
        cellValue = self.myGridShunt.GetCellValue(row,col)

        if row>0:
            cellVal = self.myGridShunt.GetCellValue(row-1,col)
            busNumUpper =int(self.myGridShunt.GetCellValue(row-1,1))
            busNameUpper = self.myGridShunt.GetCellValue(row-1,2)
            busAreaUpper = int(self.myGridShunt.GetCellValue(row-1,3))
            busZoneUpper = int(self.myGridShunt.GetCellValue(row-1,5))
            busIDUpper = str(self.myGridShunt.GetCellValue(row-1,7))
            shuntStatusUpper = int(self.myGridShunt.GetCellValue(row-1,8))
            pgenUpper = float(self.myGridShunt.GetCellValue(row-1,9))
            qgenUpper = float(self.myGridShunt.GetCellValue(row-1,10))

        busNum = int(self.myGridShunt.GetCellValue(row,1))
        busName = self.myGridShunt.GetCellValue(row,2)
        busArea = int(self.myGridShunt.GetCellValue(row,3))
        busZone = int(self.myGridShunt.GetCellValue(row,5))
        busID = str(self.myGridShunt.GetCellValue(row,7))
        shuntStatus = int(self.myGridShunt.GetCellValue(row,8))
        pgen = float(self.myGridShunt.GetCellValue(row,9))
        qgen = float(self.myGridShunt.GetCellValue(row,10))

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng shunt
    def on_cell_change_grid_shunt( self, event ):
        
        col1 = col
        if self.uk == 13:
            row1 = row-1
        else:
            row1 = row

        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if i == 0:
                    self.on_cell_change_grid_shunt_fcn(event,row1,col1,0 )
                else:
                    self.on_cell_change_grid_shunt_fcn(event,row1,col1,1 )
                psspy.save(path)
        else:
            self.on_cell_change_grid_shunt_fcn(event,row1,col1,0 )
            psspy.save(self.Path)
        self.UpdateShuntPage(event)

    def on_cell_change_grid_shunt_fcn( self, event,row,col,flag ):
        row1 = row
        col1 = col
        if self.uk == 13:
            cellVal = self.myGridShunt.GetCellValue(row1,col1)
            if col1 == 7: # change ID
                psspy.mbidshunt(busNumUpper,busIDUpper,str(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.mbidshunt({a},'{b}','{c}')\n".format(a=busNumUpper,b=busIDUpper,c=str(cellVal)))
                    f.close()

            if col1 == 8: # change status
                psspy.shunt_chng(busNumUpper,busIDUpper,int(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.shunt_chng({a},'{b}',{c})\n".format(a=busNumUpper,b=busIDUpper,c=int(cellVal)))
                    f.close()

            if col1 == 11: # change GB nom
                psspy.shunt_chng(busNumUpper,busIDUpper, REALAR2 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.shunt_chng({a},'{b}',REALAR2 = {c})\n".format(a=busNumUpper,b=busIDUpper,c=float(cellVal)))
                    f.close()

        else:
            cellNewVal = self.myGridShunt.GetCellValue(row1,col1)

            if col1 == 7: # change ID
                psspy.mbidshunt(busNum,busID,str(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.mbidshunt({a},'{b}','{c}')\n".format(a=busNum,b=busID,c=str(cellNewVal)))
                    f.close()

            if col1 == 8: # change status
                psspy.shunt_chng(busNum,busID,int(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.shunt_chng({a},'{b}',{c})\n".format(a=busNum,b=busID,c=int(cellNewVal)))
                    f.close()

            if col1 == 11: # change GB nom
                psspy.shunt_chng(busNum,busID, REALAR2 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.shunt_chng({a},'{b}',REALAR2 = {c})\n".format(a=busNum,b=busID,c=float(cellNewVal)))
                    f.close()

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng shunt
    def on_cell_right_click_grid_shunt( self, event ):
        menus = [(wx.NewId(), "Add New Shunt", self.addNew),
                 (wx.NewId(), "Turn On/Off Shunt", self.turnOnOff),
                 (wx.NewId(), "Delete Shunt", self.deleteShunt)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.gridShunt.PopupMenu(popup_menu, self.gridShunt.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return

    def addNew(self, event):
        self.Add_New_Shunt(event)

    def turnOnOff(self,event):
        self.Turn_On_Off(event)

    def deleteShunt(self,event):
        self.Delete(event)

    # Thêm mới kháng, tụ
    def Add_New_Shunt(self,event):
        dialogAddNewShunt = Add_New_Shunt_Dialog(self.parent)
        busNumList = []

        for i in range(len(self.matrixBus[0])):
            busNumList.append(self.matrixBus[0][i,0]+'-'+self.matrixBus[0][i,1])
        
        dialogAddNewShunt.fromBusNum.SetItems(busNumList)
        dialogAddNewShunt.flagSynch = self.parent.flagSynch
        dialogAddNewShunt.Path = self.Path 
        dialogAddNewShunt.macroFile = self.parent.macroFile
        dialogAddNewShunt.PathFile = self.PathFile
        dialogAddNewShunt.ShowModal()

        if not dialogAddNewShunt.onClose(event):
            event.Skip()

        self.UpdateShuntPage(event)

    # Bật/tắt kháng/tụ
    def Turn_On_Off( self, event ):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if int(shuntStatus) == 1:
                    psspy.shunt_chng(busNum,busID,0)
                else:
                    psspy.shunt_chng(busNum,busID,1)
                psspy.save(path)
        else:
            if int(shuntStatus) == 1:
                psspy.shunt_chng(busNum,busID,0)
            else:
                psspy.shunt_chng(busNum,busID,1)
            psspy.save(self.Path)
        self.UpdateShuntPage(event)

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            if int(shuntStatus) == 1:
                f.writelines("psspy.shunt_chng({a},'{b}',0)\n".format(a=busNum,b=busID))
            else:
                f.writelines("psspy.shunt_chng({a},'{b}',1)\n".format(a=busNum,b=busID))
            f.close()

    # Xóa kháng/tụ
    def Delete(self, event):
        wx.MessageBox("Delete machine number {a}, id: {b}".format(a=busNum,b=busID))
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.purgshunt(busNum,busID)
                psspy.save(path)
        else:
            psspy.purgshunt(busNum,busID)
            psspy.save(self.Path)
        self.UpdateShuntPage(event)

        if self.parent.macroFile != '' and flag == 0:
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.purgshunt({a},{b})\n".format(a=busNum,b=busID))
            f.close()

    # cập nhật trang shunt
    @profiled('refresh.shunt')
    @batched_grid_update('myGridShunt', 'parent.gridFile',
                         'parent.gridSearch', 'parent.gridShunt',
                         'parent.m_grid6')
    def UpdateShuntPage(self,event):
        if self.parent.flagUpdate == 0 and self.parent.flagPaste == 0:
            self.parent.Mark_Pending_Refresh('shunt')
        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateShunt(event, i, path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                # t3 = time.time()
                self.onUpdateShunt(event,self.indexFile,self.Path)
            self.parent.onUpdateFcn(event)
        elif self.parent.flagPaste == 0:
            clear_grid(self.gridShunt)
            self.matrixShunt[self.indexFile] = loadShuntTab(self.Path)
            for row1 in range(len(self.matrixShunt[self.indexFile])):
                for column1 in range(len(self.matrixShunt[self.indexFile][0])):
                    self.myGridShunt.SetCellValue(row1,column1,str(self.matrixShunt[self.indexFile][row1][column1]))
            self.parent.onUpdateFcn(event)

    def onUpdateShunt(self,event, indexfile, path):
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
                    self.parent.gridFile.SetCellValue(row,column,str(fileInfoTranspose[row][column]))
            clear_grid(self.parent.gridShunt)
            self.matrixBus[self.indexFile] = loadBusTab(self.Path)
            for row1 in range(len(self.matrixBus[self.indexFile])):
                for column1 in range(len(self.matrixBus[self.indexFile][0])):
                    self.parent.gridSearch.SetCellValue(row1,column1,str(self.matrixBus[self.indexFile][row1][column1]))
            self.matrixShunt[self.indexFile] = loadShuntTab(self.Path)
            for row1 in range(len(self.matrixShunt[self.indexFile])):
                for column1 in range(len(self.matrixShunt[self.indexFile][0])):
                    self.parent.gridShunt.SetCellValue(row1,column1,str(self.matrixShunt[self.indexFile][row1][column1]))
            self.matrixSource[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixSource[self.indexFile])):
                for column1 in range(len(self.matrixSource[self.indexFile][0])):
                    self.parent.m_grid6.SetCellValue(row1,column1,str(self.matrixSource[self.indexFile][row1][column1]))
                coff = self.parent.m_grid6.GetCellValue(row1,13)
                self.parent.m_grid6.SetCellValue(row1,26,str(float(coff)/100))
            
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

    # Lọc kháng/tụ theo nội dung nhập vào ở ô Number
    @profiled('search.shunt_number')
    @batched_grid_update('myGridShunt')
    def shuntNumberEnter_Fcn(self, event):
        shuntNum = self.parent.shuntNumber.GetValue()
        result = []
        if shuntNum != '':
            for i in range(len(self.matrixShunt[self.indexFile])):
                if (str(shuntNum) in str(self.matrixShunt[self.indexFile][i][1])):
                    result.append(self.matrixShunt[self.indexFile][i][:])

            if len(result)!=0:
                clear_grid(self.myGridShunt)

                for i in range(len(result)):
                    for j in range(len(result[0])):
                        self.myGridShunt.SetCellValue(i,j,str(result[i][j]))
