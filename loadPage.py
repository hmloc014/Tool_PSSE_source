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
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadMachineTab,loadShuntTab,loadLoadTab,loadSourceLoadInfo
from math import *
from decimal import *
from dialogAddLoad import Add_New_Load_Dialog
from ui_performance import batched_grid_update, clear_grid, profiled
from LoadTab import select_load_from_zone

cellValue = 0
cellVal = 0
row = 0
col = 0
busNum = 0
busID = 0
loadStatus = 0
busNumUpper = 0
busIDUpper = 0
PloadUpper = 0.0
QloadUpper = 0.0
TWOPLACE = Decimal(10)**-2
    
class CustomGridLoad(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.Path = ''
        self.PathFile = []
        self.parent = parent
        self.fileInfoTranspose = []
        self.matrixBus = []
        self.matrixArea = []
        self.matrixZone = []
        self.matrixLoad = []
        self.matrixSource = []
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridLoad = wx.grid.Grid
        self.zoneNum = 0
        self.indexFile = 0
        self.uk = 0
    
    # chức năng thực hiện tại ô được chọn của bảng phụ tải
    def on_selected_cell_grid_load( self, event ):
        global row,col,cellValue,cellVal,busNum,busNumUpper
        global busID,busIDUpper,loadStatus,Pload,PloadUpper,Qload,QloadUpper
        row = event.GetRow()
        col = event.GetCol()
        colLabel = self.myGridLoad.GetColLabelValue(col)
        cellValue = self.myGridLoad.GetCellValue(row,col)
        if row>0:
            cellVal = self.myGridLoad.GetCellValue(row-1,col)
            busNumUpper = self.myGridLoad.GetCellValue(row-1,0)
            busIDUpper = self.myGridLoad.GetCellValue(row-1,6)
            PloadUpper = self.myGridLoad.GetCellValue(row-1,8)
            QloadUpper = self.myGridLoad.GetCellValue(row-1,9)
        busNum = self.myGridLoad.GetCellValue(row,0)
        busID = self.myGridLoad.GetCellValue(row,6)
        loadStatus = self.myGridLoad.GetCellValue(row,7)
        Pload = self.myGridLoad.GetCellValue(row,8)
        Qload = self.myGridLoad.GetCellValue(row,9)

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng phụ tải
    def on_cell_right_click_grid_load( self, event ):
        menus = [(wx.NewId(), "Add New Load", self.addNew),
                 (wx.NewId(), "Turn On/Off Load", self.turnOnOff),
                 (wx.NewId(), "Delete Load", self.deleteLoad)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.gridLoad.PopupMenu(popup_menu, self.gridLoad.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return

    def addNew(self, event):
        self.Add_New_Load(event)

    def turnOnOff(self,event):
        self.Turn_On_Off(event)

    def deleteLoad(self,event):
        self.Delete(event)

    # Thêm mới tải
    def Add_New_Load(self,event):
        dialogAddNewLoad = Add_New_Load_Dialog(self.parent)
        busNumList = []

        for i in range(len(self.matrixBus[0])):
            busNumList.append(str(self.matrixBus[0][i,0])+'-'+str(self.matrixBus[0][i,1]))
        
        dialogAddNewLoad.fromBusNum.SetItems(busNumList)
        dialogAddNewLoad.flagSynch = self.parent.flagSynch
        dialogAddNewLoad.Path = self.Path
        dialogAddNewLoad.PathFile = self.PathFile
        dialogAddNewLoad.macroFile = self.parent.macroFile
        dialogAddNewLoad.ShowModal()

        if not dialogAddNewLoad.onClose(event):
            event.Skip()
        else:
            self.UpdatedLoadPage(event)

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng phụ tải
    def on_cell_change_grid_load( self, event ):
        col1 = col
        if self.uk == 13:
            row1 = row-1
        else:
            row1 = row

        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if i == 0:
                    self.on_cell_change_grid_load_fcn( event,row1,col1,0 )
                else:
                    self.on_cell_change_grid_load_fcn( event,row1,col1,1 )
                psspy.save(path)
        else:
            self.on_cell_change_grid_load_fcn( event,row1,col1,0 )
            psspy.save(self.Path)
        
        self.UpdatedLoadPage(event)

    def on_cell_change_grid_load_fcn( self, event,row,col,flag ):
        row1 = row 
        col1 = col 
        if self.uk == 13:
            cellVal = self.myGridLoad.GetCellValue(row1,col1)
            if col1 == 2: # change area
                psspy.load_chng_4(int(busNumUpper),str(busIDUpper),INTGAR2 = int(cellVal),REALAR1 = float(PloadUpper),REALAR2 = float(QloadUpper))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}',INTGAR2 = {c},REALAR1 = {d},REALAR2 = {e})\n".format(a=int(busNumUpper),b=str(busIDUpper),c=int(cellVal),d=float(PloadUpper),e=float(QloadUpper)))
                    f.close()

            if col1 == 4: # change zone
                psspy.load_chng_4(int(busNumUpper),str(busIDUpper),INTGAR3 = int(cellVal),REALAR1 = float(PloadUpper),REALAR2 = float(QloadUpper))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}',INTGAR3 = {c},REALAR1 = {d},REALAR2 = {e})\n".format(a=int(busNumUpper),b=str(busIDUpper),c=int(cellVal),d=float(PloadUpper),e=float(QloadUpper)))
                    f.close()

            if col1 == 6: # change ID
                psspy.load_chng_4(int(busNumUpper),str(busIDUpper))
                psspy.mbidload(int(busNumUpper),str(busIDUpper),str(cellVal))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}')\n".format(a=int(busNumUpper),b=str(busIDUpper)))
                    f.writelines("psspy.mbidload({a},'{b}','{c}')\n".format(a=int(busNumUpper),b=str(busIDUpper),c=str(cellVal)))
                    f.close()

            if col1 == 7: # change status
                psspy.load_chng_4(int(busNumUpper),str(busIDUpper), INTGAR1 = int(cellVal),INTGAR5 = 1)
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}',INTGAR1 = {c},INTGAR5 = 1)\n".format(a=int(busNumUpper),b=str(busIDUpper),c=int(cellVal)))
                    f.close()

            if col1 == 8: # change P
                psspy.load_chng_4(int(busNumUpper),str(busIDUpper), REALAR1 = float(cellVal))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}',REALAR1 = {c})\n".format(a=int(busNumUpper),b=str(busIDUpper),c=float(cellVal)))
                    f.close()

            if col1 == 9: # change Q
                psspy.load_chng_4(int(busNumUpper),str(busIDUpper), REALAR2 = float(cellVal))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}',REALAR2 = {c})\n".format(a=int(busNumUpper),b=str(busIDUpper),c=float(cellVal)))
                    f.close()
        else:
            cellNewVal = self.myGridLoad.GetCellValue(row1,col1)
            if col == 2: # change area
                psspy.load_chng_4(int(busNum),str(busID),INTGAR2 = int(cellNewVal),REALAR1 = float(Pload),REALAR2 = float(Qload))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}', INTGAR2 = {c},REALAR1 = {d},REALAR2 = {e})\n".format(a=int(busNum),b=str(busID),c=int(cellNewVal),d=float(Pload),e=float(Qload)))
                    f.close()

            if col == 4: # change zone
                psspy.load_chng_4(int(busNum),str(busID),INTGAR3 = int(cellNewVal),REALAR1 = float(Pload),REALAR2 = float(Qload))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}', INTGAR3 = {c},REALAR1 = {d},REALAR2 = {e})\n".format(a=int(busNum),b=str(busID),c=int(cellNewVal),d=float(Pload),e=float(Qload)))
                    f.close()

            if col == 6: # change ID
                psspy.load_chng_4(int(busNum),str(busID))
                psspy.mbidload(int(busNum),str(busID),str(cellNewVal))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}')\n".format(a=int(busNum),b=str(busID)))
                    f.writelines("psspy.mbidload({a},'{b}','{c}')\n".format(a=int(busNum),b=str(busID),c=str(cellNewVal)))
                    f.close()

            if col == 7: # change status
                psspy.load_chng_4(int(busNum),str(busID), INTGAR1 = int(cellNewVal),INTGAR5 = 1) 
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}', INTGAR1 = {c},INTGAR5 = 1)\n".format(a=int(busNum),b=str(busID),c=float(cellNewVal)))
                    f.close()
              
            if col == 8: # change P
                psspy.load_chng_4(int(busNum),str(busID), REALAR1 = float(cellNewVal))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}', REALAR1 = {c})\n".format(a=int(busNum),b=str(busID),c=float(cellNewVal)))
                    f.close()

            if col == 9: # change Q
                psspy.load_chng_4(int(busNum),str(busID), REALAR2 = float(cellNewVal))
                
                if self.parent.macroFile != '' and flag == 0	:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.load_chng_4({a},'{b}', REALAR2 = {c})\n".format(a=int(busNum),b=str(busID),c=float(cellNewVal)))
                    f.close()

    # Bật, tắt tải
    def Turn_On_Off( self, event ):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if int(loadStatus) == 1:
                    psspy.load_chng_4(int(busNum),str(busID), INTGAR1 = 0,
                                                    INTGAR5 = 1)
                else:
                    psspy.load_chng_4(int(busNum),str(busID), INTGAR1 = 1,
                                                    INTGAR5 = 1)
                psspy.save(path)
        else:
            if int(loadStatus) == 1:
                psspy.load_chng_4(int(busNum),str(busID), INTGAR1 = 0,
                                                INTGAR5 = 1)
            else:
                psspy.load_chng_4(int(busNum),str(busID), INTGAR1 = 1,
                                                INTGAR5 = 1)
            psspy.save(self.Path)

        self.UpdatedLoadPage(event)
        
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            if int(loadStatus) == 1: 
                f.writelines("psspy.load_chng_4({a},'{b}', INTGAR1 = 0,INTGAR5 = 1)\n".format(a=int(busNum),b=str(busID)))
            else:
                f.writelines("psspy.load_chng_4({a},'{b}', INTGAR1 = 1,INTGAR5 = 1)\n".format(a=int(busNum),b=str(busID)))
            f.close()

    # Xóa phụ tải
    def Delete(self, event):
        wx.MessageBox("Delete load {a} in bus {b}".format(a=str(busID),b=int(busNum)))
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.purgload(int(busNum),str(busID))
                psspy.save(path)
        else:
            psspy.purgload(int(busNum),str(busID))
            psspy.save(self.Path)
        self.UpdatedLoadPage(event)  

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.purgload({a},'{b}')\n".format(a=int(busNum),b=str(busID)))
            f.close()

    # cập nhật trang thông tin tải
    @profiled('refresh.load')
    @batched_grid_update('myGridLoad', 'parent.gridFile',
                         'parent.gridArea', 'parent.gridZone',
                         'parent.gridLoad', 'parent.m_grid6')
    def UpdatedLoadPage(self, event):
        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateLoad(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                # t3 = time.time()
                self.onUpdateLoad(event,self.indexFile,self.Path)
            self.parent.onUpdateFcn(event)
                
        elif self.parent.flagPaste == 0:
            clear_grid(self.gridLoad)
            self.matrixLoad[self.indexFile] = loadLoadTab(self.Path)
            for row1 in range(len(self.matrixLoad[self.indexFile])):
                for column1 in range(len(self.matrixLoad[self.indexFile][0])):
                    self.myGridLoad.SetCellValue(row1,column1,str(self.matrixLoad[self.indexFile][row1][column1]))
            self.parent.onUpdateFcn(event)

    def onUpdateLoad(self, event, indexfile, path):
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
            clear_grid(self.parent.gridLoad, 12)
            self.matrixArea[self.indexFile] = loadAreaInfo(self.Path)
            for row1 in range(len(self.matrixArea[self.indexFile])):
                for column1 in range(len(self.matrixArea[self.indexFile][0])):
                    self.parent.gridArea.SetCellValue(row1,column1,str(self.matrixArea[self.indexFile][row1][column1]))

            self.matrixZone[self.indexFile] = loadZoneInfo(self.Path)
            for row2 in range(len(self.matrixZone[self.indexFile])):
                for column2 in range(len(self.matrixZone[self.indexFile][0])):
                    self.parent.gridZone.SetCellValue(row2,column2,str(self.matrixZone[self.indexFile][row2][column2])) 
            
            self.matrixLoad[self.indexFile] = loadLoadTab(self.Path)
            for row1 in range(len(self.matrixLoad[self.indexFile])):
                for column1 in range(len(self.matrixLoad[self.indexFile][0])):
                    self.parent.gridLoad.SetCellValue(row1,column1,str(self.matrixLoad[self.indexFile][row1][column1]))
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

    # Scale phụ tải của tỉnh được chọn
    def scaleZoneLoad(self,event,row,mygridLoad = wx.grid.Grid):
        inputVal = self.parent.m_textCtrl17.GetValue()
        qLoad = self.parent.Q_Value.GetValue()
        pZone = self.parent.P_value.GetValue()
        zoneNum = self.zoneNum
        if self.parent.flagChangePPercent ==1 and inputVal != '':
            newPLoad = (100-float(inputVal))*float(pZone)/100
        elif self.parent.flagChangeDeltaP == 1 and inputVal != '':
            newPLoad = float(pZone) + float(inputVal)
        elif self.parent.flagChangeNewPVal == 1 and inputVal != '':
            newPLoad = float(inputVal)
        if int(newPLoad) != 0:
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,[int(zoneNum)])
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,[int(zoneNum)])
            ierr, shuntGBNomCplx = psspy.afxshuntcplx(0,4,"SHUNTNOM")
            totalReactor = 0
            totalCapacitor = 0

            for i in range(len(shuntGBNomCplx[0])):
                if shuntGBNomCplx[0][i].imag >0:
                    totalCapacitor = totalCapacitor + shuntGBNomCplx[0][i].imag
                else:
                    totalReactor = totalReactor + shuntGBNomCplx[0][i].imag
            psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
            psspy.scal_2(0,1,2,[0,1,0,1,0],[float(newPLoad),float(pZone),0.0,float(totalReactor),float(totalCapacitor),-.0, float(qLoad)])


        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateLoad(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateLoad(event,self.indexFile,self.Path)
                # self.parent.UpdatedData(event,self.indexFile,self.Path)

            [PLoad,QLoad,CosPhi,selectedMatrixLoad] = select_load_from_zone(row,zoneNum,self.matrixLoad,self.myGridZone)
            for row1 in range(self.myGridLoad.GetNumberRows()):
                for column1 in range(self.myGridLoad.GetNumberCols()):
                    self.myGridLoad.SetCellValue(row1,column1,"")
            for row1 in range(len(selectedMatrixLoad)):
                for column1 in range(len(selectedMatrixLoad[0])):
                    self.myGridLoad.SetCellValue(row1,column1,str(selectedMatrixLoad[row1][column1]))
        else:
            for row1 in range(self.myGridLoad.GetNumberRows()):
                for column1 in range(self.myGridLoad.GetNumberCols()):
                    self.myGridLoad.SetCellValue(row1,column1,"")
            for row1 in range(self.myGridArea.GetNumberRows()):
                for column1 in range(self.myGridArea.GetNumberCols()):
                    self.myGridArea.SetCellValue(row1,column1,"")
            for row1 in range(self.myGridZone.GetNumberRows()):
                for column1 in range(self.myGridZone.GetNumberCols()):
                    self.myGridZone.SetCellValue(row1,column1,"")

            self.matrixArea[self.indexFile] = loadAreaInfo(self.Path)
            for row1 in range(len(self.matrixArea[self.indexFile])):
                for column1 in range(len(self.matrixArea[self.indexFile][0])):
                    self.myGridArea.SetCellValue(row1,column1,str(self.matrixArea[self.indexFile][row1][column1]))

            self.matrixZone[self.indexFile] = loadZoneInfo(self.Path)
            for row2 in range(len(self.matrixZone[self.indexFile])):
                for column2 in range(len(self.matrixZone[self.indexFile][0])):
                    self.myGridZone.SetCellValue(row2,column2,str(self.matrixZone[self.indexFile][row2][column2])) 
            
            [PLoad,QLoad,CosPhi,selectedMatrixLoad] = select_load_from_zone(row,zoneNum,self.matrixLoad,self.myGridZone)
            for row1 in range(len(selectedMatrixLoad)):
                for column1 in range(len(selectedMatrixLoad[0])):
                    self.myGridLoad.SetCellValue(row1,column1,str(selectedMatrixLoad[row1][column1]))


        self.parent.P_value.SetValue(str(PLoad))
        self.parent.Q_Value.SetValue(str(QLoad))
        self.parent.Cos_Phi_Value.SetValue(str(CosPhi))

    # lọc phụ tải theo thông tin nhập vào từ ô Bus Num
    @profiled('search.load_number')
    @batched_grid_update('myGridLoad')
    def loadNumberEnter_Fcn(self,event):
        loadNum = self.parent.loadNumber.GetValue()
        result = []
        if loadNum != '':
            for i in range(len(self.matrixLoad[self.indexFile])):
                if (str(loadNum) in str(self.matrixLoad[self.indexFile][i][0])):
                    result.append(self.matrixLoad[self.indexFile][i][:])

            if len(result)!=0:
                clear_grid(self.myGridLoad)

                for i in range(len(result)):
                    for j in range(len(result[0])):
                        self.myGridLoad.SetCellValue(i,j,str(result[i][j]))
