# -*- coding: utf-8 -*-
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
from ChangeBusTab import change,addNew
import numpy as np
from DialogBox import getInput
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadMachineTab,loadShuntTab,loadLoadTab,select_load_from_zone,select_source_from_zone,select_shunt_from_zone
from math import *
from decimal import *
from dialogChangeZoneSourceLoad import Scale_Zone

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
selectedZoneRow = 0
selectedZoneNum = 0
TWOPLACE = Decimal(10)**-2
    
class CustomGridZone(MyFrame1):
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
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridSource = wx.grid.Grid
        self.myGridLoad = wx.grid.Grid
        self.myGridShunt = wx.grid.Grid
        self.selectedZoneNum = 0
        self.selectedZoneRow = 0
        self.indexFile = 0
        self.uk = 0
    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng zone
    def on_cell_change_grid_zone( self, event ):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if i == 0: # file đầu không ghi thao tác vào file macro
                    self.on_cell_change_grid_zone_fcn(0)
                else:
                    self.on_cell_change_grid_zone_fcn(1)
                psspy.save(path)
            for i,path in enumerate(self.PathFile):
                self.UpdateGridZoneFcn(event,i,path)
        else:
            self.on_cell_change_grid_zone_fcn(0)
            psspy.save(self.Path)
            self.UpdateGridZoneFcn(event,self.indexFile,self.Path)

    def on_cell_change_grid_zone_fcn( self,flag):
        if col == 2 and uk ==13: # change PGen with enter
            newPGen = self.myGridZone.GetCellValue(row-1,2)
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNumUpper))
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNumUpper))
            ierr, shuntGBNomCplx = psspy.afxshuntcplx(0,4,"SHUNTNOM")
            totalReactor = 0
            totalCapacitor = 0
            for i in range(len(shuntGBNomCplx[0])):
                if shuntGBNomCplx[0][i].imag >0:
                    totalCapacitor = totalCapacitor + shuntGBNomCplx[0][i].imag
                else:
                    totalReactor = totalReactor + shuntGBNomCplx[0][i].imag

            psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
            psspy.scal_2(0,1,2,[0,1,0,1,0],[float(PloadUpper),float(newPGen),0.0,float(totalReactor),float(totalCapacitor),-.0, float(QloadUpper)])

            if self.parent.macroFile != '' and flag == 0:
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])\n")
                f.writelines("psspy.scal_2(0,1,2,[0,1,0,1,0],[{a},{b},0.0,{c},{d},-.0, {e}])\n".format(a=float(PloadUpper),b=float(newPGen),c=float(totalReactor),d=float(totalCapacitor),e=float(QloadUpper)))
                f.close()

        elif col == 2:  # change PGen with other way
            newPGen = self.myGridZone.GetCellValue(row,2)
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNum))
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNum))
            ierr, shuntGBNomCplx = psspy.afxshuntcplx(0,4,"SHUNTNOM")
            totalReactor = 0
            totalCapacitor = 0
            for i in range(len(shuntGBNomCplx[0])):
                if shuntGBNomCplx[0][i].imag >0:
                    totalCapacitor = totalCapacitor + shuntGBNomCplx[0][i].imag
                else:
                    totalReactor = totalReactor + shuntGBNomCplx[0][i].imag

            psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
            psspy.scal_2(0,1,2,[0,1,0,1,0],[float(Pload),float(newPGen),0.0,float(totalReactor),float(totalCapacitor),-.0, float(Qload)])
            
            if self.parent.macroFile != '' and flag == 0:
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])\n")
                f.writelines("psspy.scal_2(0,1,2,[0,1,0,1,0],[{a},{b},0.0,{c},{d},-.0, {e}])\n".format(a=float(Pload),b=float(newPGen),c=float(totalReactor),d=float(totalCapacitor),e=float(Qload)))
                f.close()

        elif col == 4 and uk == 13: # change PLoad with enter
            newPLoad = self.myGridZone.GetCellValue(row-1,4)
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNumUpper))
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNumUpper))
            ierr, shuntGBNomCplx = psspy.afxshuntcplx(0,4,"SHUNTNOM")
            totalReactor = 0
            totalCapacitor = 0
            for i in range(len(shuntGBNomCplx[0])):
                if shuntGBNomCplx[0][i].imag >0:
                    totalCapacitor = totalCapacitor + shuntGBNomCplx[0][i].imag
                else:
                    totalReactor = totalReactor + shuntGBNomCplx[0][i].imag

            psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
            psspy.scal_2(0,1,2,[0,1,0,1,0],[float(newPLoad),float(PgenUpper),0.0,float(totalReactor),float(totalCapacitor),-.0, float(QloadUpper)])
            
            if self.parent.macroFile != '' and flag == 0:
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])\n")
                f.writelines("psspy.scal_2(0,1,2,[0,1,0,1,0],[{a},{b},0.0,{c},{d},-.0, {e}])\n".format(a=float(newPLoad),b=float(PgenUpper),c=float(totalReactor),d=float(totalCapacitor),e=float(QloadUpper)))
                f.close()

        elif col ==4:
            newPLoad = self.myGridZone.GetCellValue(row,4)
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNum))
            psspy.bsys(0,0,[ 1.0, 500.0],0,[],0,[],0,[],1,int(zoneNum))
            ierr, shuntGBNomCplx = psspy.afxshuntcplx(0,4,"SHUNTNOM")
            totalReactor = 0
            totalCapacitor = 0
            for i in range(len(shuntGBNomCplx[0])):
                if shuntGBNomCplx[0][i].imag >0:
                    totalCapacitor = totalCapacitor + shuntGBNomCplx[0][i].imag
                else:
                    totalReactor = totalReactor + shuntGBNomCplx[0][i].imag

            psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])
            psspy.scal_2(0,1,2,[0,1,0,1,0],[float(newPLoad),float(Pgen),0.0,float(totalReactor),float(totalCapacitor),-.0, float(Qload)])

            if self.parent.macroFile != '' and flag == 0:
                f = open(self.parent.macroFile,'a')
                f.writelines("psspy.scal_2(0,0,1,[0,0,0,0,0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0])\n")
                f.writelines("psspy.scal_2(0,1,2,[0,1,0,1,0],[{a},{b},0.0,{c},{d},-.0, {e}])\n".format(a=float(newPLoad),b=float(Pgen),c=float(totalReactor),d=float(totalCapacitor),e=float(Qload)))
                f.close()
    # chức năng thực hiện khi righ click tại ô làm việc trong bảng zone
    def on_cell_right_click_grid_zone( self, event ):

        menus = [(wx.NewId(), "Change Zone Source/Load", self.changePSourceLoadFcn)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.gridZone.PopupMenu(popup_menu, self.gridZone.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return

    # chức năng thực hiện tại ô được chọn của bảng zone
    def on_selected_cell_grid_zone( self, event ):

        global row,col,cellValue,cellVal,zoneNum,zoneName,Pgen,Qgen,Pload,Qload,CosPhi,rowNum,zoneNum,zonePgen,selectedZoneNum,selectedZoneRow
        global zoneNumUpper,zoneNameUpper,PgenUpper,QgenUpper,PloadUpper,QloadUpper,CosPhiUpper
        selectedZoneNum = self.selectedZoneNum
        selectedZoneRow = self.selectedZoneRow
        if self.parent.onUpdate!=1:
            self.parent.rowZone = event.GetRow()
            self.parent.colZone = event.GetCol()
        row = self.parent.rowZone
        col = self.parent.colZone
        colLabel = self.myGridZone.GetColLabelValue(col)
        cellValue = self.myGridZone.GetCellValue(row,col)
        rowNum = self.myGridZone.GetNumberRows()
        zoneNum = self.matrixZone[self.indexFile][:,0]
        zonePgen = self.matrixZone[self.indexFile][:,2]

        if row>0:
            cellVal = self.myGridZone.GetCellValue(row-1,col)
            zoneNumUpper = int(self.myGridZone.GetCellValue(row-1,0))
            zoneNameUpper = str(self.myGridZone.GetCellValue(row-1,1))
            PgenUpper = float(self.myGridZone.GetCellValue(row-1,2))
            QgenUpper = float(self.myGridZone.GetCellValue(row-1,3))
            PloadUpper = float(self.myGridZone.GetCellValue(row-1,4))
            QloadUpper = float(self.myGridZone.GetCellValue(row-1,5))
            CosPhiUpper = float(self.myGridZone.GetCellValue(row-1,6))
        zoneNum = int(self.myGridZone.GetCellValue(row,0))
        zoneName = str(self.myGridZone.GetCellValue(row,1))
        Pgen = float(self.myGridZone.GetCellValue(row,2))
        Qgen = float(self.myGridZone.GetCellValue(row,3))
        Pload = float(self.myGridZone.GetCellValue(row,4))
        Qload = float(self.myGridZone.GetCellValue(row,5))
        CosPhi = float(self.myGridZone.GetCellValue(row,6))
    
    def on_key_down_grid_zone( self, event ):
        global uk
        rowsNum = self.myGridZone.GetNumberRows()
        uk = self.uk #uk ==13 is Enter key

    # thay đổi P source/load của bảng zone
    def changePSourceLoad(self,event):
        if self.parent.flagUpdate == 0:
            self.parent.Mark_Pending_Refresh('source')
            self.parent.Mark_Pending_Refresh('load')

        dialogChangeZoneLoad = Scale_Zone(self.parent)
        dialogChangeZoneLoad.mygridZone = self.myGridZone
        dialogChangeZoneLoad.flagSynch = self.parent.flagSynch
        dialogChangeZoneLoad.Path = self.Path
        dialogChangeZoneLoad.PathFile = self.PathFile
        dialogChangeZoneLoad.macroFile = self.parent.macroFile

        zoneList = []
        for i in range(len(self.matrixZone[self.indexFile])):
            zoneList.append(str(self.matrixZone[self.indexFile][i,0])+'-'+str(self.matrixZone[self.indexFile][i,1]))

        dialogChangeZoneLoad.lb.SetItems(zoneList)

        dialogChangeZoneLoad.ShowModal()
        if not dialogChangeZoneLoad.onClose(event):
            event.Skip()

        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                self.UpdateGridZoneFcn(event,i,path)
        else:
            self.UpdateGridZoneFcn(event,self.indexFile,self.Path)

    # cập nhật bảng zone
    def UpdateGridZoneFcn(self,event,indexFile,path):
        self.indexFile = indexFile
        self.Path = path
        if self.parent.flagUpdate == 1:
            self.parent.UpdatedData(event,indexFile,path)
            if selectedZoneNum != 0:
                # for row1 in range(self.myGridLoad.GetNumberRows()):
                #     for column1 in range(self.myGridLoad.GetNumberCols()):
                #         self.myGridLoad.SetCellValue(row1,column1,"")
            
                # for row1 in range(self.myGridSource.GetNumberRows()):
                #     for column1 in range(27):
                #         self.myGridSource.SetCellValue(row1,column1,"")
                selectedMatrixSource = select_source_from_zone(selectedZoneNum,self.matrixSource[self.indexFile])
                for row1 in range(len(selectedMatrixSource)):
                    for column1 in range(len(selectedMatrixSource[0])):
                        self.myGridSource.SetCellValue(row1,column1,str(selectedMatrixSource[row1][column1]))
                    coff = self.myGridSource.GetCellValue(row1,13)
                    self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))

                [PLoad,QLoad,CosPhi,selectedMatrixLoad] = select_load_from_zone(selectedZoneRow,selectedZoneNum,self.matrixLoad[self.indexFile],self.myGridZone)
                for row1 in range(len(selectedMatrixLoad)):
                    for column1 in range(len(selectedMatrixLoad[0])):
                        self.myGridLoad.SetCellValue(row1,column1,str(selectedMatrixLoad[row1][column1]))
                
                selectedMatrixShunt = select_shunt_from_zone(selectedZoneNum,matrixShunt[indexFile])
                for row1 in range(len(selectedMatrixShunt)):
                    for column1 in range(len(selectedMatrixShunt[0])):
                        self.myGridShunt.SetCellValue(row1,column1,str(selectedMatrixShunt[row1][column1]))

                self.parent.P_value.SetValue(str(PLoad))
                self.parent.Q_Value.SetValue(str(QLoad))
                self.parent.Cos_Phi_Value.SetValue(str(CosPhi))
        else:
            self.matrixArea[self.indexFile] = loadAreaInfo(self.Path)
            for row1 in range(len(self.matrixArea[self.indexFile])):
                for column1 in range(len(self.matrixArea[self.indexFile][0])):
                    self.myGridArea.SetCellValue(row1,column1,str(self.matrixArea[self.indexFile][row1][column1]))

            self.matrixZone[self.indexFile] = loadZoneInfo(self.Path)
            for row2 in range(len(self.matrixZone[self.indexFile])):
                for column2 in range(len(self.matrixZone[self.indexFile][0])):
                    self.myGridZone.SetCellValue(row2,column2,str(self.matrixZone[self.indexFile][row2][column2])) 
            if selectedZoneNum != 0:
                # for row1 in range(self.myGridSource.GetNumberRows()):
                #     for column1 in range(27):
                #         self.myGridSource.SetCellValue(row1,column1,"")

                # for row1 in range(self.myGridLoad.GetNumberRows()):
                #     for column1 in range(self.myGridLoad.GetNumberCols()):
                #         self.myGridLoad.SetCellValue(row1,column1,"")

                selectedMatrixSource = select_source_from_zone(selectedZoneNum,self.matrixSource[self.indexFile])
                for row1 in range(len(selectedMatrixSource)):
                    for column1 in range(len(selectedMatrixSource[0])):
                        self.myGridSource.SetCellValue(row1,column1,str(selectedMatrixSource[row1][column1]))
                    coff = self.myGridSource.GetCellValue(row1,13)
                    self.myGridSource.SetCellValue(row1,26,str(float(coff)/100))

                if selectedZoneNum != 0:
                    [PLoad,QLoad,CosPhi,selectedMatrixLoad] = select_load_from_zone(selectedZoneRow,selectedZoneNum,self.matrixLoad[self.indexFile],self.myGridZone)
                    for row1 in range(len(selectedMatrixLoad)):
                        for column1 in range(len(selectedMatrixLoad[0])):
                            self.myGridLoad.SetCellValue(row1,column1,str(selectedMatrixLoad[row1][column1]))
                
                selectedMatrixShunt = select_shunt_from_zone(selectedZoneNum,matrixShunt[indexFile])
                for row1 in range(len(selectedMatrixShunt)):
                    for column1 in range(len(selectedMatrixShunt[0])):
                        self.myGridShunt.SetCellValue(row1,column1,str(selectedMatrixShunt[row1][column1]))


    def changePSourceLoadFcn(self,event):
        self.changePSourceLoad(event)

    def Change_Zone_Source_Fcn( self, event ):
        self.changePSourceLoad(event)
