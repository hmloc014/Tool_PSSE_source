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
from dialogAddGen import Add_New_Gen
from dynamicPage import CustomGridDyn
from ui_performance import batched_grid_update, clear_grid, profiled
import pyodbc

cellValue = 0
cellVal = 0
row = 0
col = 0
busNum = 0
busName = ''
busArea = 0
busZone = 0
busID = 0
machineStatus = 0
pgen = 0.0
qgen = 0.0
pmax = 0.0
qmax = 0.0
busNumUpper = 0
busNameUpper= ''
busAreaUpper=0
busZoneUpper=0
busIDUpper =0
machineStatusUpper = 0
pgenUpper = 0.0
qgenUpper = 0.0
pmaxUpper = 0.0
qmaxUpper = 0.0

TWOPLACE = Decimal(10)**-2
    
class CustomGridSource(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.Path = ''
        self.indexFile = 0
        self.uk = 0
        self.PathFile = []
        self.parent = parent
        self.fileInfoTranspose = []
        self.matrixBus = []
        self.matrixArea = []
        self.matrixZone = []
        self.matrixGen = []
        self.areaList = []
        self.zoneList = []
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridSource = wx.grid.Grid
        self.gridDyn = wx.grid.Grid
        self.DyrNewFile = ''
        self.flagNum = 0
        self.flagName = 0
        self.ukNum = 0
        self.ukName = 0

    # chức năng thực hiện tại ô được chọn của bảng source
    def on_selected_cell_grid_source( self, event ):
        global row,col,cellValue,cellVal,busNum,busName,busArea,busZone,busID,machineStatus,pgen,qgen,pmax,qmax,indexDyr
        global busNumberUpper,busNameUpper,busAreaUpper,busZoneUpper,busIDUpper,machineStatusUpper,pgenUpper,qgenUpper,pmaxUpper,qmaxUpper
        row = event.GetRow()
        col = event.GetCol()
        colLabel = self.myGridSource.GetColLabelValue(col)
        cellValue = self.myGridSource.GetCellValue(row,col)

        if row>0:
            cellVal = self.myGridSource.GetCellValue(row-1,col)
            busNumberUpper =(self.myGridSource.GetCellValue(row-1,0))
            busNameUpper = self.myGridSource.GetCellValue(row-1,1)
            busAreaUpper = int(self.myGridSource.GetCellValue(row-1,2))
            busZoneUpper = int(self.myGridSource.GetCellValue(row-1,4))
            busIDUpper = str(self.myGridSource.GetCellValue(row-1,6))
            machineStatusUpper = int(self.myGridSource.GetCellValue(row-1,7))
            pgenUpper = float(self.myGridSource.GetCellValue(row-1,11))
            qgenUpper = float(self.myGridSource.GetCellValue(row-1,14))
            pmaxUpper = float(self.myGridSource.GetCellValue(row-1,13))
            qmaxUpper = float(self.myGridSource.GetCellValue(row-1,15))

        busNum = int(self.myGridSource.GetCellValue(row,0))
        busName = self.myGridSource.GetCellValue(row,1)
        busArea = int(self.myGridSource.GetCellValue(row,2))
        busZone = int(self.myGridSource.GetCellValue(row,4))
        busID = str(self.myGridSource.GetCellValue(row,6))
        machineStatus = int(self.myGridSource.GetCellValue(row,7))
        pgen = float(self.myGridSource.GetCellValue(row,11))
        qgen = float(self.myGridSource.GetCellValue(row,14))
        pmax = float(self.myGridSource.GetCellValue(row,13))
        qmax = float(self.myGridSource.GetCellValue(row,15))

        # if Xsource dyr not blank, get index of its source in dyr table
        if self.myGridSource.GetCellValue(row,25)!='': 
            indexDyr = self.parent.indexInDyr[row]
        if row == 0 and col == 31:
            self.applyChangeSource(event)

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng source
    def on_cell_change_grid_source( self, event ):
        col1 = col

        if self.uk == 13:
            row1 = row-1
        else:
            row1 = row
        collBypass = [0,1,2,3,4,5,9,13,16,17,18,19,20,21,22,23,27,28,29,30]
        if col1 in collBypass:
            event.Skip()
        else:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    if i == 0: # file đầu tiên không ghi vào macro
                        self.on_cell_change_grid_source_fcn(event,row1,col1,0)
                    else:
                        self.on_cell_change_grid_source_fcn(event,row1,col1,1)
                    psspy.save(path)
            else:
                self.on_cell_change_grid_source_fcn(event,row1,col1,0)
                psspy.save(self.Path)
            self.onUpdateGridSource(event)
    

    def on_cell_change_grid_source_fcn( self, event,row,col,flag ):
        row1 = row 
        col1 = col
        busNumUpper = int(busNumberUpper)
        
        if self.uk == 13:
            cellVal = self.myGridSource.GetCellValue(row1,col1)
            if col1 == 10: # change V_sched
                psspy.machine_chng_2(busNumUpper,busIDUpper)
                psspy.plant_chng(busNumUpper,REALAR1 = float(cellVal)) 

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}')\n".format(a=busNumUpper,b=busIDUpper))
                    f.writelines("psspy.plant_chng({a},REALAR1 = {b})\n".format(a=busNumUpper,b=float(cellVal)))
                    f.close() 

            if col1 == 6: # change ID
                psspy.machine_chng_2(busNumUpper,busIDUpper)
                psspy.mbidmac(busNumUpper,busIDUpper,str(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}')\n".format(a=busNumUpper,b=busIDUpper))
                    f.writelines("psspy.mbidmac({a},'{b}','{c}')\n".format(a=busNumUpper,b=busIDUpper,c=str(cellVal)))
                    f.close() 

            if col1 == 7: # change status
                psspy.machine_chng_2(busNumUpper,busIDUpper,INTGAR1 = int(cellVal),INTGAR6 = 0,REALAR17 = 1.0)

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', INTGAR1 = {c},INTGAR6 = 0,REALAR17 = 1.0)\n".format(a=busNumUpper,b=busIDUpper,c=int(cellVal)))
                    f.close() 

            if col1 == 8: # change BaseKV
                psspy.bus_chng_3(busNumUpper,REALAR1 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.bus_chng_3({a},REALAR1 = {b})\n".format(a=busNumUpper,b=float(cellVal)))
                    f.close() 

            if col1 == 11: # change Pgen
                psspy.machine_chng_2(busNumUpper,busIDUpper, REALAR1 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR1 = {c})\n".format(a=busNumUpper,b=busIDUpper,c=float(cellVal)))
                    f.close() 

            if col1 == 12: # change Pmax
                psspy.machine_chng_2(busNumUpper,busIDUpper, REALAR5 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR5 = {c})\n".format(a=busNumUpper,b=busIDUpper,c=float(cellVal)))
                    f.close() 

            if col1 == 14: # change Qgen
                psspy.machine_chng_2(busNumUpper,busIDUpper, REALAR2 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR2 = {c})\n".format(a=busNumUpper,b=busIDUpper,c=float(cellVal)))
                    f.close() 

            if col1 == 15: # change Qmax
                psspy.machine_chng_2(busNumUpper,busIDUpper, REALAR3 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR3 = {c})\n".format(a=busNumUpper,b=busIDUpper,c=float(cellVal)))
                    f.close() 

            if col1 == 24 : # change x Source ==> change MBase, all data according to database
                # try:
                [XTransient,XSyn] = self.getDataFromDatabase(int(busAreaUpper),pmaxUpper,cellVal)
                XSub = XNeg = XZero = cellVal
                if len(XTransient)!=0 or len(XSyn) !=0:
                    psspy.machine_chng_2(busNumUpper,busIDUpper,REALAR9 = float(cellVal),REALAR7 = float(sqrt(pmaxUpper*pmaxUpper+qmaxUpper*qmaxUpper))) # Xsource,MBase
                    psspy.seq_machine_data_3(busNumUpper,busIDUpper,REALAR2 = float(XSub),REALAR4 = float(XNeg),REALAR6 = float(XZero),REALAR7 = float(XTransient[0]),REALAR8 = float(XSyn[0]))
                    
                    if self.parent.macroFile != '' and flag == 0:
                        f = open(self.parent.macroFile,'a')
                        f.writelines("psspy.machine_chng_2({a},'{b}',REALAR9 = {c},REALAR7 = {d})\n".format(a=busNumUpper,b=busIDUpper,c=float(cellVal),d=float(sqrt(pmaxUpper*pmaxUpper+qmaxUpper*qmaxUpper))))
                        f.writelines("psspy.seq_machine_data_3({a},'{b}',REALAR2 = {c},REALAR4 = {d},REALAR6 = {e},REALAR7 = {f},REALAR8 = {g})\n".format(a=busNumUpper,b=busIDUpper,c=float(XSub),d=float(XNeg),e=float(XZero),f=float(XTransient[0]),g=float(XSyn[0])))
                        f.close()  
                else:
                    psspy.machine_chng_2(busNumUpper,busIDUpper,REALAR9 = float(cellVal),REALAR7 = float(sqrt(pmaxUpper*pmaxUpper+qmaxUpper*qmaxUpper))) # Xsource,MBase
                    psspy.seq_machine_data_3(busNumUpper,busIDUpper,REALAR2 = float(XSub),REALAR4 = float(XNeg),REALAR6 = float(XZero))

                    if self.parent.macroFile != '' and flag == 0:
                        f = open(self.parent.macroFile,'a')
                        f.writelines("psspy.machine_chng_2({a},'{b}',REALAR9 = {c},REALAR7 = {d}))\n".format(a=busNumUpper,b=busIDUpper,c=float(cellVal),d=float(sqrt(pmaxUpper*pmaxUpper+qmaxUpper*qmaxUpper))))
                        f.writelines("psspy.seq_machine_data_3({a},'{b}',REALAR2 = {c},REALAR4 = {d},REALAR6 = {e})\n".format(a=busNumUpper,b=busIDUpper,c=float(XSub),d=float(XNeg),e=float(XZero)))
                        f.close() 

                if self.myGridSource.GetCellValue(row1,25)!='':
                    indexDyr = self.parent.indexInDyr[row1]
                    self.myGridSource.SetCellValue(row1,25,cellVal)
                    if self.gridDyn.GetCellValue(indexDyr,1) == "'GENROU'":
                        self.gridDyn.SetCellValue(indexDyr,13,str(cellVal))
                    elif self.gridDyn.GetCellValue(indexDyr,1) == "'GENSAL'":
                        self.gridDyn.SetCellValue(indexDyr,11,str(cellVal))

            if col1 == 25 : # change Xsource Dyr

                indexDyr = self.parent.indexInDyr[row1]
                if self.gridDyn.GetCellValue(indexDyr,1) == "'GENROU'":
                    self.gridDyn.SetCellValue(indexDyr,13,str(cellVal))
                elif self.gridDyn.GetCellValue(indexDyr,1) == "'GENSAL'":
                    self.gridDyn.SetCellValue(indexDyr,11,str(cellVal))

            if col1 == 26 : # change ratio pgen/pmax
                newRatio = float(self.myGridSource.GetCellValue(row1,26))
                pmax = float(self.myGridSource.GetCellValue(row1,12))
                psspy.machine_chng_2(busNumUpper,busIDUpper, REALAR1 = newRatio*pmax)

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}',REALAR1 = {c})\n".format(a=busNumUpper,b=busIDUpper,c=newRatio*pmax))
                    f.close()

        else:
            cellNewVal = self.myGridSource.GetCellValue(row1,col1)
            if col1 == 10: # change V_sched
                psspy.machine_chng_2(busNum,busID)
                psspy.plant_chng(busNum,REALAR1 = float(cellNewVal)) 

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}')\n".format(a=busNum,b=busID))
                    f.writelines("psspy.plant_chng({a},REALAR1 = {b}) \n".format(a=busNum,b=float(cellNewVal)))
                    f.close() 

            if col1 == 6: # change ID
                psspy.machine_chng_2(busNum,busID)
                psspy.mbidmac(busNum,busID,str(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}')\n".format(a=busNum,b=busID))
                    f.writelines("psspy.mbidmac({a},'{b}','{c}')\n".format(a=busNum,b=busID,c=str(cellNewVal)))
                    f.close()

            if col1 == 7: # change status
                psspy.machine_chng_2(busNum,busID,INTGAR1 = int(cellNewVal),INTGAR6 = 0,REALAR17 = 1.0)
                
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}',INTGAR1 = {c},INTGAR6 = 0,REALAR17 = 1.0)\n".format(a=busNum,b=busID,c=int(cellNewVal)))
                    f.close()

            if col1 == 8: # change BaseKV
                psspy.bus_chng_3(busNum,REALAR1 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.bus_chng_3({a},REALAR1 = {b})\n".format(a=busNum,b=float(cellNewVal)))
                    f.close()

            if col1 == 11: # change P
                psspy.machine_chng_2(busNum,busID, REALAR1 = float(cellNewVal))
                
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR1 = {c})\n".format(a=busNum,b=busID,c=float(cellNewVal)))
                    f.close()

            if col1 == 12: # change Pmax
                psspy.machine_chng_2(busNum,busID, REALAR5 = float(cellNewVal))
                
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR5 = {c})\n".format(a=busNum,b=busID,c=float(cellNewVal)))
                    f.close()

            if col1 == 14: # change Q
                psspy.machine_chng_2(busNum,busID, REALAR2 = float(cellNewVal))
                
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR2 = {c})\n".format(a=busNum,b=busID,c=float(cellNewVal)))
                    f.close()

            if col1 == 15: # change Qmax
                psspy.machine_chng_2(busNum,busID, REALAR3 = float(cellNewVal))
                
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}', REALAR3 = {c})\n".format(a=busNum,b=busID,c=float(cellNewVal)))
                    f.close()

            if col1 ==25  : # change xSource in dyr file
                indexDyr = self.parent.indexInDyr[row1]
                if self.gridDyn.GetCellValue(indexDyr,1) == "'GENROU'":
                    self.gridDyn.SetCellValue(indexDyr,13,str(cellNewVal))
                elif self.gridDyn.GetCellValue(indexDyr,1) == "'GENSAL'":
                    self.gridDyn.SetCellValue(indexDyr,11,str(cellNewVal))

            if col1 == 24 : # change xSource according to database, (change X source, X zero, X negative, X Subtransient, X transient)
                pmax = float(self.myGridSource.GetCellValue(row1,12))
                [XTransient,XSyn] = self.getDataFromDatabase(busArea,pmax,cellNewVal)
                XSub = XNeg = XZero = cellNewVal
                if len(XTransient)!=0 or len(XSyn) !=0:
                    psspy.machine_chng_2(busNum,busID,REALAR9 = float(cellNewVal),REALAR7 = float(sqrt(pmax*pmax+qmax*qmax))) # Xsource,MBase
                    psspy.seq_machine_data_3(busNum,busID,REALAR2 = float(XSub),REALAR4 = float(XNeg),REALAR6 = float(XZero),REALAR7 = float(XTransient[0]),REALAR8 = float(XSyn[0]))
                                
                    if self.parent.macroFile != '' and flag == 0:
                        f = open(self.parent.macroFile,'a')
                        f.writelines("psspy.machine_chng_2({a},'{b}',REALAR9 = {c},REALAR7 = {d}))\n".format(a=busNum,b=busID,c=float(cellNewVal),d=float(sqrt(pmax*pmax+qmax*qmax))))
                        f.writelines("psspy.seq_machine_data_3({a},'{b}',REALAR2 = {c},REALAR4 = {d},REALAR6 = {e},REALAR7 = {f},REALAR8 = {g})\n".format(a=busNum,b=busID,c=float(XSub),d=float(XNeg),e=float(XZero),f=float(XTransient[0]),g=float(XSyn[0])))
                        f.close()

                else:
                    psspy.machine_chng_2(busNum,busID,REALAR9 = float(cellNewVal),REALAR7 = float(sqrt(pmax*pmax+qmax*qmax))) # Xsource,MBase
                    psspy.seq_machine_data_3(busNum,busID,REALAR2 = float(XSub),REALAR4 = float(XNeg),REALAR6 = float(XZero))
                    
                    if self.parent.macroFile != '' and flag == 0:
                        f = open(self.parent.macroFile,'a')
                        f.writelines("psspy.machine_chng_2({a},'{b}',REALAR9 = {c},REALAR7 = {d}))\n".format(a=busNum,b=busID,c=float(cellNewVal),d=float(sqrt(pmax*pmax+qmax*qmax))))
                        f.writelines("psspy.seq_machine_data_3({a},'{b}',REALAR2 = {c},REALAR4 = {d},REALAR6 = {e})\n".format(a=busNum,b=busID,c=float(XSub),d=float(XNeg),e=float(XZero)))
                        f.close()
                
                if self.myGridSource.GetCellValue(row1,25)!='':
                    self.myGridSource.SetCellValue(row1,25,cellNewVal)
                    indexDyr = self.parent.indexInDyr[row1]
                    if self.gridDyn.GetCellValue(indexDyr,1) == "'GENROU'":
                        self.gridDyn.SetCellValue(indexDyr,13,str(cellNewVal))
                    elif self.gridDyn.GetCellValue(indexDyr,1) == "'GENSAL'":
                        self.gridDyn.SetCellValue(indexDyr,11,str(cellNewVal))

            if col1 == 26 : # change ratio pgen/pmax
                newRatio = float(self.myGridSource.GetCellValue(row1,26))
                pmax = float(self.myGridSource.GetCellValue(row1,12))
                psspy.machine_chng_2(busNum,busID, REALAR1 = newRatio*pmax)

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.machine_chng_2({a},'{b}',REALAR1 = {c})\n".format(a=busNum,b=busID,c=newRatio*pmax))
                    f.close()

    # Cập nhật thông tin bảng source
    def onUpdateGridSource(self,event):
        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateSourceTurnOO(event,i,path)
                    self.parent.onUpdateFcn(event)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateSourceTurnOO(event,self.indexFile,self.Path)
                self.parent.onUpdateFcn(event)

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng source
    def on_cell_right_click_grid_source( self, event ):
        menus = [(wx.NewId(), "Add New Gen", self.addNew),
                 (wx.NewId(), "Turn On/Off Gen", self.turnOnOff),
                 (wx.NewId(), "Delete Gen", self.deleteMachine)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.m_grid6.PopupMenu(popup_menu, self.m_grid6.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return
    
    # Lọc nguồn theo nội dung nhập vào ở ô Number
    @profiled('search.gen_number')
    @batched_grid_update('myGridSource')
    def genNumberEnter_Fcn(self,event):
        genNum = self.parent.genNumber.GetValue()
        GenName = ''
        PgenPercent = 0
        Vschedule = 0
        CosPhi = 0
        PAMBA = [[]]
        MAX = MIN = [[]]
        result = []
        if genNum != '':
            for i in range(len(self.matrixGen[self.indexFile])):
                if (str(genNum) in str(self.matrixGen[self.indexFile][i][0])):
                    result.append(self.matrixGen[self.indexFile][i][:])

            if len(result)!=0:
                clear_grid(self.myGridSource, 27)

                for i in range(len(result)):
                    for j in range(len(result[0])):
                        self.myGridSource.SetCellValue(i,j,str(result[i][j]))
                    coff = self.myGridSource.GetCellValue(i,13)
                    self.myGridSource.SetCellValue(i,26,str(float(coff)/100))

    # Lọc nguồn theo nội dung nhập vào ở ô Name    
    @profiled('search.gen_name')
    @batched_grid_update('myGridSource')
    def genNameEnter_Fcn(self,event):
        GenName = self.parent.genName.GetValue()
        genNum = ''
        PgenPercent = 0
        Vschedule = 0
        CosPhi = 0
        PAMBA = [[]]
        MAX = MIN = [[]]
        result = []
        if GenName != '':

            for i in range(len(self.matrixGen[self.indexFile])):
                if (((GenName).encode('utf-8')).upper() in str(self.matrixGen[self.indexFile][i][1])):
                    result.append(self.matrixGen[self.indexFile][i][:])

            if len(result)!=0:
                clear_grid(self.myGridSource, 27)

                for i in range(len(result)):
                    for j in range(len(result[0])):
                        self.myGridSource.SetCellValue(i,j,str(result[i][j]))
                    coff = self.myGridSource.GetCellValue(i,13)
                    self.myGridSource.SetCellValue(i,26,str(float(coff)/100))

    def addNew(self, event):
        self.Add_New_Gen(event)

    def turnOnOff(self,event):
        self.Turn_On_Off(event)

    def deleteMachine(self,event):
        self.Delete(event)

    # Kết nối vs database, chọn các giá trị Pmax có thể có từ bảng Dynamic_gen
    def SelectPMAX(self):
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT DYNAMIC_GEN.[SCALE] FROM DYNAMIC_GEN;""")
        pmaxArr = []

        for row in cursor.fetchall():
            if not float(row[0]) in pmaxArr:
                pmaxArr.append(float(row[0]))
            else:
                next
        return pmaxArr

    # Thêm mới nguồn
    def Add_New_Gen(self,event):

        addMachineDialog = Add_New_Gen(self.parent)
        busNumList = []
        voltageList = []
        pmaxList = self.SelectPMAX()

        for i in range(len(self.matrixGen[self.indexFile][:,0])):
            busNumList.append(str(self.matrixGen[self.indexFile][i,0])+'-'+str(self.matrixGen[self.indexFile][i,1]))
        for i in range(len(self.matrixBus[self.indexFile][:,0])):
            voltage = self.matrixBus[self.indexFile][i,2]
            if not float(voltage) in voltageList: 
                voltageList.append(float(voltage))
        voltageList.sort()

        # Tạo dialog thêm mới nguồn
        addMachineDialog.fromBusNum.SetItems(busNumList)
        addMachineDialog.comboBoxVoltageLevel.SetItems(map(str,voltageList))
        addMachineDialog.comboBoxArea.SetItems(map(str,self.areaList))
        addMachineDialog.comboBoxZone.SetItems(map(str,self.zoneList))
        addMachineDialog.pmaxList = pmaxList
        addMachineDialog.comboBoxPmax.SetItems(map(str,pmaxList))
        addMachineDialog.myGridSource = self.myGridSource
        addMachineDialog.matrixGen = self.matrixGen
        addMachineDialog.parent = self.parent
        addMachineDialog.Path = self.Path
        addMachineDialog.PathFile = self.PathFile
        addMachineDialog.macroFile = self.parent.macroFile
        addMachineDialog.flagSynch = self.parent.flagSynch
        addMachineDialog.DyrNewFile = self.DyrNewFile
        addMachineDialog.gridDyn = self.gridDyn

        addMachineDialog.ShowModal()

        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateSourceAdd(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateSourceAdd(event,self.indexFile,self.Path)
                # self.parent.UpdatedData(event,self.indexFile,self.Path)

        else:
            clear_grid(self.myGridSource, 27)
            self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixGen[self.indexFile])):
                for column1 in range(len(self.matrixGen[self.indexFile][0])):
                    self.myGridSource.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
                coff = self.myGridSource.GetCellValue(row1,13)
                self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))
            self.parent.onUpdateFcn(event)

    # Bật/Tắt nguồn
    def Turn_On_Off( self, event ):
        if int(machineStatus) == 1:
            if self.parent.flagSynch == 1:

                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.machine_chng_2(busNum,busID, INTGAR1 = 0,INTGAR6 = 0, REALAR17 = 1.0)
                    psspy.save(path)
            else:
                psspy.machine_chng_2(busNum,busID, INTGAR1 = 0,INTGAR6 = 0, REALAR17 = 1.0)
                psspy.save(self.Path)
        else:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    psspy.case(path)
                    psspy.machine_chng_2(busNum,busID, INTGAR1 = 1,INTGAR6 = 0, REALAR17 = 1.0)
                    psspy.save(path)
            else:
                psspy.machine_chng_2(busNum,busID, INTGAR1 = 1,INTGAR6 = 0, REALAR17 = 1.0)
                psspy.save(self.Path)

        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateSourceTurnOO(event,i,path)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateSourceTurnOO(event,self.indexFile,self.Path)

        else:
            clear_grid(self.myGridSource, 27)
            self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixGen[self.indexFile])):
                for column1 in range(len(self.matrixGen[self.indexFile][0])):
                    self.myGridSource.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
                coff = self.myGridSource.GetCellValue(row1,13)
                self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))
            self.parent.onUpdateFcn(event)

        if self.parent.macroFile != '':
            if int(machineStatus) == 1:
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.machine_chng_2({a},'{b}', INTGAR1 = 0,INTGAR6 = 0,REALAR17 = 1.0)\n".format(a=busNum,b= busID))
                f.close()
            else:
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.machine_chng_2({a},'{b}', INTGAR1 = 1,INTGAR6 = 0,REALAR17 = 1.0)\n".format(a=busNum,b= busID))
                f.close()

    # Xóa nguồn
    def Delete(self, event):
        wx.MessageBox("Delete machine number {a}, id: {b}".format(a=busNum,b=busID))
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.purgmac(busNum,busID)
                psspy.bsysinit(1)
                psspy.bsyso(1,busNum)
                psspy.extr(1,0,[0,0])
                psspy.save(path)
        else:
            psspy.purgmac(busNum,busID)
            psspy.bsysinit(1)
            psspy.bsyso(1,busNum)
            psspy.extr(1,0,[0,0])
            psspy.save(self.Path)
        
        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateSourceDelete(event,i,path)
                    self.parent.onUpdateFcn(event)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateSourceDelete(event,self.indexFile,self.Path)
                self.parent.onUpdateFcn(event)
                # self.parent.UpdatedData(event,self.indexFile,self.Path)
        else:
            clear_grid(self.myGridSource, 27)
            self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixGen[self.indexFile])):
                for column1 in range(len(self.matrixGen[self.indexFile][0])):
                    self.myGridSource.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
                coff = self.myGridSource.GetCellValue(row1,13)
                self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))
            self.parent.onUpdateFcn(event)

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.purgmac({a},'{b}')\n".format(a=busNum,b= busID))
            f.writelines("psspy.bsysinit(1)\n")
            f.writelines("psspy.bsyso(1,{a})\n".format(a=busNum))
            f.writelines("psspy.extr(1,0,[0,0])\n")
            f.close()

    # lựa chọn giá trị XSource tương ứng với loại nguồn và quy mô
    def SelectXSourcePMAX(self,area = 0,scale = 0.0):
        TD = [16,26,36,43,53,63]
        ND = [17,18,19,42,27,28,29,52,37,38,39,62] # sinh khoi, LNG, ND
        WD = [41,51,61]
        SL = [40,50,60,70,80,90,100,110,120]
        # 16(TD),17(NT),18(NK),19(HN),40(PV),41(W),42(SK),43(TDTN) mien bac
        # 26(TD),27(NT),28(NK),29(HN),50(PV),51(W),52(SK),53(TDTN) mien trung
        # 36(TD),37(NT),38(NK),39(HN),60(PV),61(W),62(SK),63(TDTN) mien nam
        # 70,80,90,100,110,120 (DMT)
        # 1 so nguon phia bac dat trong area luoi bac 110 va luoi bac 220 (10,11,12) se k xet
        planType = ""
        if area in TD:
            planType = "TD"
        elif area in ND:
            planType = 'ND'
        elif area in WD: 
            planType = 'TYPE3'
        else:
            planType = 'TYPE4'

        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT DYNAMIC_GEN.[X''d] FROM DYNAMIC_GEN WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (abs((DYNAMIC_GEN.[SCALE])-{b})<=1));""".format(a=planType,b =scale))

        XSourceArr = []

        for row in cursor.fetchall():
            XSourceArr.append(str(row[0]))
        return XSourceArr
    
    # Lấy thông tin Xd, X'd từ csdl
    def getDataFromDatabase(self,area=0,scale = 0.0,XSource=0.0):
        TD = [16,26,36,43,53,63]
        ND = [17,18,19,42,27,28,29,52,37,38,39,62] # sinh khoi, LNG, ND
        WD = [41,51,61]
        SL = [40,50,60,70,80,90,100,110,120]

        planType = ""
        if area in TD:
            planType = "TD"
        elif area in ND:
            planType = 'ND'
        elif area in WD: 
            planType = 'TYPE3'
        else:
            planType = 'TYPE4'

        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};'
                            r'DBQ=Database.mdb;')
        cursor = conn.cursor()
        cursor.execute("""SELECT DYNAMIC_GEN.[X'd],DYNAMIC_GEN.[Xd] FROM DYNAMIC_GEN WHERE (((DYNAMIC_GEN.[PLAN_TYPE])='{a}') AND (abs((DYNAMIC_GEN.[SCALE])-{b})<=1) AND ( DYNAMIC_GEN.[X''d]={c}));""".format(a=planType,b =scale,c = XSource))

        XTransientArr = []
        XSynchronousArr = []

        for row in cursor.fetchall():
            XTransientArr.append(str(row[0]))
            XSynchronousArr.append(str(row[1]))
        return [XTransientArr,XSynchronousArr]
    
    def applyChangeSource(self,event):
        sourceType = ["NGUON_BAC_TD","NGUON_BAC_NT","NGUONBAC_PV","NGUON_BAC_W","BTRUNBO_1931","NGUON_TRG_TD","NGUON_TRG_NT","NGUON_TRG_NK","NGUON_TRG_HN","NGUONTRG_PV","NGUONTRG_W","NGUONTRG_SK","TNGUYEN_1931","NGUON_NAM_TD","NGUON_NAM_NT","NGUON_NAM_NK","NGUON_NAM_HN","NGUONNAM_PV","NGUONNAM_W","NGUONNAM_SK","NGUONNAM_LNG","TANAMBO_1931","NITHUAN_1931","DMT_1632","DMT_NOI_1870"]
        newRatio = []
        for i in range(len(sourceType)):
            if self.myGridSource.GetCellValue(i,30) != '':
                newRatio.append(self.myGridSource.GetCellValue(i,30))
            else:
                newRatio.append(self.myGridSource.GetCellValue(i,29))
        
        areaNum = [16,17,40,41,70,26,27,28,29,50,51,52,80,36,37,38,39,60,61,62,63,90,100,110,120]
        dictionany = {'Type':newRatio,'Area':areaNum}
        num = []
        lineNum = []
        for i in range(len(self.matrixGen[self.indexFile])):
            # print('--------genArea:',self.matrixGen[self.indexFile][i][2])
            # print('--------genNum:',self.matrixGen[self.indexFile][i][0])
            genArea =  self.matrixGen[self.indexFile][i][2] #self.myGridSource.GetCellValue(i,2)
            # print(genArea)
            genNum = int(self.matrixGen[self.indexFile][i][0])
            psspy.bsys(1,0,[ 1.0, 500.0],0,[],1,[genNum],0,[],0,[])
            ierr, busTypeCode = psspy.abusint(1,2,'TYPE')

            if int(genArea) in areaNum and busTypeCode[0][0]!=3:
                indexNum = areaNum.index(int(genArea))
                pmax = float(self.matrixGen[self.indexFile][i][12])
                busNum = int(self.matrixGen[self.indexFile][i][0])
                busID = str(self.matrixGen[self.indexFile][i][6])
                psspy.machine_chng_2(busNum,busID, REALAR1 = (float(newRatio[indexNum])*pmax))

            else:
                num.append('{a}-{b}'.format(a=genNum,b=busTypeCode[0][0]))
                lineNum.append(i+1)
                next

        psspy.save(self.Path)
        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdateSourceTurnOO(event,i,path)
                    self.parent.onUpdateFcn(event)
                    # self.parent.UpdatedData(event,i,path)
            else:
                self.onUpdateSourceTurnOO(event,self.indexFile,self.Path)
                self.parent.onUpdateFcn(event)
                # self.parent.UpdatedData(event,self.indexFile,self.Path)
        else:
            clear_grid(self.myGridSource, 27)
            self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixGen[self.indexFile])):
                for column1 in range(len(self.matrixGen[self.indexFile][0])):
                    self.myGridSource.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
                coff = self.myGridSource.GetCellValue(row1,13)
                self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))
    
    #for add/delete, have to delete all source page and update new data
    # turn on/off/delete need calculate power flow, for add new don't need

    # cập nhật bảng source  khi thực hiện chức năng DELETE (tính lại TLCS, xóa đi, cập nhật lại)
    @profiled('refresh.source_delete')
    @batched_grid_update('parent.gridFile', 'parent.gridArea',
                         'parent.gridZone', 'parent.m_grid6')
    def onUpdateSourceDelete(self, event, indexfile, path):
           
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

            clear_grid(self.parent.m_grid6, 27)
            
            self.matrixArea[self.indexFile] = loadAreaInfo(self.Path)
            for row1 in range(len(self.matrixArea[self.indexFile])):
                for column1 in range(len(self.matrixArea[self.indexFile][0])):
                    self.parent.gridArea.SetCellValue(row1,column1,str(self.matrixArea[self.indexFile][row1][column1]))

            self.matrixZone[self.indexFile] = loadZoneInfo(self.Path)
            for row2 in range(len(self.matrixZone[self.indexFile])):
                for column2 in range(len(self.matrixZone[self.indexFile][0])):
                    self.parent.gridZone.SetCellValue(row2,column2,str(self.matrixZone[self.indexFile][row2][column2])) 
            
            self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixGen[self.indexFile])):
                for column1 in range(len(self.matrixGen[self.indexFile][0])):
                    self.parent.m_grid6.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
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

    # cập nhật bảng source  khi thực hiện chức năng TURN ON/OFF (không cần xóa đi cập nhật lại)
    @profiled('refresh.source_status')
    @batched_grid_update('parent.gridFile', 'parent.gridArea',
                         'parent.gridZone', 'parent.m_grid6')
    def onUpdateSourceTurnOO(self, event, indexfile, path):
          
        self.indexFile = indexfile
        self.Path = path
        if self.parent.flagUpdate == 1 or self.parent.flagReload == 1:
            self.parent.Power_Flow_Selected_Cal_Fcn_ALL(event,path)
            fileInfo = loadFileInfo(self.Path)
            fileInfo1 = [fileInfo[0][0],fileInfo[1][0],fileInfo[2][0],fileInfo[3][0],fileInfo[4][0],fileInfo[5][0]]
            fileInfoArray = np.array(fileInfo1)
            fileInfoTranspose = fileInfoArray.transpose()

            # for row1 in range(self.parent.m_grid6.GetNumberRows()):
            #     for column1 in range(27): 
            #         self.parent.m_grid6.SetCellValue(row1,column1,"")
            for row in range(len(fileInfoTranspose)):
                for column in range(len(fileInfoTranspose[0])):
                    self.parent.gridFile.SetCellValue(row,column,str(fileInfoTranspose[row][column]))

            self.matrixArea[self.indexFile] = loadAreaInfo(self.Path)
            for row1 in range(len(self.matrixArea[self.indexFile])):
                for column1 in range(len(self.matrixArea[self.indexFile][0])):
                    self.parent.gridArea.SetCellValue(row1,column1,str(self.matrixArea[self.indexFile][row1][column1]))

            self.matrixZone[self.indexFile] = loadZoneInfo(self.Path)
            for row2 in range(len(self.matrixZone[self.indexFile])):
                for column2 in range(len(self.matrixZone[self.indexFile][0])):
                    self.parent.gridZone.SetCellValue(row2,column2,str(self.matrixZone[self.indexFile][row2][column2])) 
            
            self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixGen[self.indexFile])):
                for column1 in range(len(self.matrixGen[self.indexFile][0])):
                    self.parent.m_grid6.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
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

    # cập nhật bảng source  khi thực hiện chức năng ADD NEW (không tính lại TLCS)
    @profiled('refresh.source_add')
    @batched_grid_update('parent.gridFile', 'parent.gridArea',
                         'parent.gridZone', 'parent.m_grid6')
    def onUpdateSourceAdd(self, event, indexfile, path):
        self.indexFile = indexfile
        self.Path = path
        fileInfo = loadFileInfo(self.Path)
        fileInfo1 = [fileInfo[0][0],fileInfo[1][0],fileInfo[2][0],fileInfo[3][0],fileInfo[4][0],fileInfo[5][0]]
        fileInfoArray = np.array(fileInfo1)
        fileInfoTranspose = fileInfoArray.transpose()

        if self.parent.flagUpdate == 1 or self.parent.flagReload == 1:

            clear_grid(self.parent.m_grid6, 27)
            
            for row in range(len(fileInfoTranspose)):
                for column in range(len(fileInfoTranspose[0])):
                    self.parent.gridFile.SetCellValue(row,column,str(fileInfoTranspose[row][column]))

            self.matrixArea[self.indexFile] = loadAreaInfo(self.Path)
            for row1 in range(len(self.matrixArea[self.indexFile])):
                for column1 in range(len(self.matrixArea[self.indexFile][0])):
                    self.parent.gridArea.SetCellValue(row1,column1,str(self.matrixArea[self.indexFile][row1][column1]))

            self.matrixZone[self.indexFile] = loadZoneInfo(self.Path)
            for row2 in range(len(self.matrixZone[self.indexFile])):
                for column2 in range(len(self.matrixZone[self.indexFile][0])):
                    self.parent.gridZone.SetCellValue(row2,column2,str(self.matrixZone[self.indexFile][row2][column2])) 
            
            self.matrixGen[self.indexFile] = loadMachineTab(self.Path)
            for row1 in range(len(self.matrixGen[self.indexFile])):
                for column1 in range(len(self.matrixGen[self.indexFile][0])):
                    self.parent.m_grid6.SetCellValue(row1,column1,str(self.matrixGen[self.indexFile][row1][column1]))
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
