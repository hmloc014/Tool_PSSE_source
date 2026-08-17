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
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadMachineTab,load3windTab,loadLoadTab,loadSourceLoadInfo
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
status = 0
pgen = 0.0
qgen = 0.0
pmax = 0.0
qmax = 0.0
busNumUpper = 0
busNameUpper= ''
busAreaUpper=0
busZoneUpper=0
busIDUpper =''
statusUpper = 0
pgenUpper = 0.0
qgenUpper = 0.0
pmaxUpper = 0.0
qmaxUpper = 0.0
flagChange = 0

TWOPLACE = Decimal(10)**-2
    
class CustomGrid3Wind(MyFrame1):
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
        self.matrix3Wind = []
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridShunt = wx.grid.Grid
        self.myGrid3Wind	 = wx.grid.Grid

    # chức năng thực hiện tại ô được chọn của trang MBA 3 cuộn dây
    def on_selected_cell_grid_3wind( self, event ):
        global row,col,cellValue,cellVal,frBusNum,frBusName,toBusNum,toBusName,id,status, lastBusNumUpper,  lastBusNameUpper,tapPosition,specifiedR,specifiedX,rate,ratio,connectionCode,R01,X01
        global frBusNumUpper,frBusNameUpper,toBusNumUpper,toBusNameUpper,idUpper,statusUpper,lastBusNum,lastBusName,tapPositionUpper,specifiedRUpper,specifiedXUpper,rateUpper,ratioUpper,connectionCodeUpper,R01Upper,X01Upper
        row = event.GetRow()
        col = event.GetCol()
        colLabel = self.myGrid3Wind.GetColLabelValue(col)
        cellValue = self.myGrid3Wind.GetCellValue(row,col)

        if row>0:
            cellVal = self.myGrid3Wind	.GetCellValue(row-1,col)
            frBusNumUpper =int(self.myGrid3Wind.GetCellValue(row-1,0))
            frBusNameUpper = self.myGrid3Wind.GetCellValue(row-1,1)
            toBusNumUpper = int(self.myGrid3Wind.GetCellValue(row-1,2))
            toBusNameUpper = self.myGrid3Wind.GetCellValue(row-1,3)
            lastBusNumUpper = int(self.myGrid3Wind.GetCellValue(row-1,4))
            lastBusNameUpper = self.myGrid3Wind.GetCellValue(row-1,5)
            idUpper = str(self.myGrid3Wind.GetCellValue(row-1,7))
            statusUpper = int(self.myGrid3Wind.GetCellValue(row-1,8))

        frBusNum =int(self.myGrid3Wind.GetCellValue(row,0))
        frBusName = self.myGrid3Wind.GetCellValue(row,1)
        toBusNum = int(self.myGrid3Wind.GetCellValue(row,2))
        toBusName = (self.myGrid3Wind.GetCellValue(row,3))
        lastBusNum = int(self.myGrid3Wind.GetCellValue(row,4))
        lastBusName = (self.myGrid3Wind.GetCellValue(row,5))
        id = str(self.myGrid3Wind.GetCellValue(row,7))
        status = int(self.myGrid3Wind.GetCellValue(row,8))

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng MBA 3 cuộn dây
    def on_cell_change_grid_3wind( self, event ):
        col1 = col
        if self.uk == 13:
            row1 = row-1
        else:
            row1 = row

        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if i == 0:
                    self.on_cell_change_grid_3wind_fcn(event,row1,col1,0 )
                else:
                    self.on_cell_change_grid_3wind_fcn(event,row1,col1,1 )
                psspy.save(path)
        else:
            self.on_cell_change_grid_3wind_fcn(event,row1,col1,0 )
            psspy.save(self.Path)
        
        self.Update3WindPage(event,1)

    def on_cell_change_grid_3wind_fcn( self, event,row,col,flag ):
        row1 = row
        col1 = col
        print()
        if self.uk == 13:
            cellVal = self.myGrid3Wind.GetCellValue(row1,col1)
            if col1 == 6: # change name
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,CHARAR1 =str(cellVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=str(cellVal)))
                    f.close()

            if col1 == 7: # change id
                psspy.mbid3wnd(frBusNumUpper,toBusNumUpper,lastBusNumUpper,str(idUpper),str(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c= lastBusNumUpper,d= str(idUpper),e=int(cellVal)))
                    f.close()

            if col1 == 8: # change status
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,INTGAR8 =  int(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=int(cellVal)))
                    f.close()

            if col1 == 9: # change w1-2 R
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALARI1 =  float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI1 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 10: # change w1-2 X
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALARI2 =  float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI2 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 11: # change w2-3 R
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALARI3 =  float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI3 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 12: # change w2-3 X
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALARI4 =  float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI4 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 13: # change w3-1 R
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALARI5 =  float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI5 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 14: # change w3-1 X
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALARI6 =  float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI6 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 17: # change Connection code
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper)
                psspy.seq_three_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,INTGAR3=int(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3= {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=int(cellVal)))
                    f.close()
                
            if col1 == 18: # change R01
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper)
                psspy.seq_three_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALAR3=float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR3= {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()

            if col1 == 19: # change X01
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper)
                psspy.seq_three_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALAR4=float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR4= {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()

            if col1 == 20: # change R02
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper)
                psspy.seq_three_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALAR7=float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR7= {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()

            if col1 == 21: # change X02
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper)
                psspy.seq_three_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALAR8=float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR8= {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()

            if col1 == 22: # change R03
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper)
                psspy.seq_three_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALAR11=float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR11= {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()

            if col1 == 23: # change X03
                psspy.three_wnd_imped_chng_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper)
                psspy.seq_three_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,idUpper,REALAR12=float(cellVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR12= {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()

            if col1 == 24: # change Rate A/B/C Wind 1
                psspy.three_wnd_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,str(idUpper),1,REALARI4 = float(cellVal),REALARI5 = float(cellVal),REALARI6 = float(cellVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,REALARI4 = {e},REALARI5 = {e},REALARI6 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 25: # change Rate A/B/C W2
                psspy.three_wnd_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,str(idUpper),2,REALARI4 = float(cellVal),REALARI5 = float(cellVal),REALARI6 = float(cellVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,REALARI4 = {e},REALARI5 = {e},REALARI6 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 26: # change Rate A/B/C W3
                psspy.three_wnd_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,str(idUpper),3,REALARI4 = float(cellVal),REALARI5 = float(cellVal),REALARI6 = float(cellVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,REALARI4 = {e},REALARI5 = {e},REALARI6 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 27: # change Ratio W1
                psspy.three_wnd_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,str(idUpper),1,REALARI1 = float(cellVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,REALARI1 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 28: # change Ratio W2
                psspy.three_wnd_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,str(idUpper),2,REALARI1 = float(cellVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,REALARI1 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
            if col1 == 29: # change Ratio W3
                psspy.three_wnd_winding_data_3(frBusNumUpper,toBusNumUpper,lastBusNumUpper,str(idUpper),3,REALARI1 = float(cellVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,REALARI1 = {e})\n".format(a=frBusNumUpper,b=toBusNumUpper,c=lastBusNumUpper,d= str(idUpper),e=float(cellVal)))
                    f.close()
        else:
            cellNewVal = self.myGrid3Wind	.GetCellValue(row1,col1)

            if col1 == 6: # change name
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,CHARAR1 =str(cellNewVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',CHARAR1 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=str(cellNewVal)))
                    f.close()

            if col1 == 7: # change id
                psspy.mbid3wnd(frBusNum,toBusNum,lastBusNum,str(id),str(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.mbid3wnd({a},{b},{c},'{d}','{e}')\n".format(a=frBusNum,b=toBusNum,c= lastBusNum,d= str(id),e=int(cellNewVal)))
                    f.close()

            if col1 == 8: # change status
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,INTGAR8 =  int(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=int(cellNewVal)))
                    f.close()

            if col1 == 9: # change w1-2 R
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,REALARI1 =  float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI1 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 10: # change w1-2 X
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,REALARI2 =  float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI2 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 11: # change w2-3 R
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,REALARI3 =  float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI3 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 12: # change w2-3 X
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,REALARI4 =  float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI4 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 13: # change w3-1 R
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,REALARI5 =  float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI5 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 14: # change w3-1 X
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,REALARI6 =  float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',REALARI6 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 17: # change Connection code
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id)
                psspy.seq_three_winding_data_3(frBusNum,toBusNum,lastBusNum,id,INTGAR3=int(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',INTGAR3= {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=int(cellNewVal)))
                    f.close()
                
            if col1 == 18: # change R01
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id)
                psspy.seq_three_winding_data_3(frBusNum,toBusNum,lastBusNum,id,REALAR3=float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR3= {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()

            if col1 == 19: # change X01
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id)
                psspy.seq_three_winding_data_3(frBusNum,toBusNum,lastBusNum,id,REALAR4=float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR4= {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()

            if col1 == 20: # change R02
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id)
                psspy.seq_three_winding_data_3(frBusNum,toBusNum,lastBusNum,id,REALAR7=float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR7= {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()

            if col1 == 21: # change X02
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id)
                psspy.seq_three_winding_data_3(frBusNum,toBusNum,lastBusNum,id,REALAR8=float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR8= {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()

            if col1 == 22: # change R03
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id)
                psspy.seq_three_winding_data_3(frBusNum,toBusNum,lastBusNum,id,REALAR11=float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR11= {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()

            if col1 == 23: # change X03
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id)
                psspy.seq_three_winding_data_3(frBusNum,toBusNum,lastBusNum,id,REALAR12=float(cellNewVal))
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}')\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
                    f.writelines("psspy.seq_three_winding_data_3({a},{b},{c},'{d}',REALAR12= {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()

            if col1 == 24: # change Rate A/B/C Wind 1
                psspy.three_wnd_winding_data_3(frBusNum,toBusNum,lastBusNum,str(id),1,REALARI4 = float(cellNewVal),REALARI5 = float(cellNewVal),REALARI6 = float(cellNewVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,REALARI4 = {e},REALARI5 = {e},REALARI6 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 25: # change Rate A/B/C W2
                psspy.three_wnd_winding_data_3(frBusNum,toBusNum,lastBusNum,str(id),2,REALARI4 = float(cellNewVal),REALARI5 = float(cellNewVal),REALARI6 = float(cellNewVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,REALARI4 = {e},REALARI5 = {e},REALARI6 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 26: # change Rate A/B/C W3
                psspy.three_wnd_winding_data_3(frBusNum,toBusNum,lastBusNum,str(id),3,REALARI4 = float(cellNewVal),REALARI5 = float(cellNewVal),REALARI6 = float(cellNewVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,REALARI4 = {e},REALARI5 = {e},REALARI6 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 27: # change Ratio W1
                psspy.three_wnd_winding_data_3(frBusNum,toBusNum,lastBusNum,str(id),1,REALARI1 = float(cellNewVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',1,REALARI1 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 28: # change Ratio W2
                psspy.three_wnd_winding_data_3(frBusNum,toBusNum,lastBusNum,str(id),2,REALARI1 = float(cellNewVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',2,REALARI1 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
            if col1 == 29: # change Ratio W3
                psspy.three_wnd_winding_data_3(frBusNum,toBusNum,lastBusNum,str(id),3,REALARI1 = float(cellNewVal)) 
                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.three_wnd_winding_data_3({a},{b},{c},'{d}',3,REALARI1 = {e})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id),e=float(cellNewVal)))
                    f.close()
    
    # chức năng thực hiện khi righ click tại ô làm việc trong bảng MBA 3 cuộn dây, mở righ click tab
    def on_cell_right_click_grid_3wind( self, event ):
        menus = [(wx.NewId(), "Turn On/Off 3 winding", self.turnOnOff),
                 (wx.NewId(), "Delete 3 winding", self.delete3Wind)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.grid3wind.PopupMenu(popup_menu, self.grid3wind.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return

    def turnOnOff(self,event):
        self.Turn_On_Off(event)

    def delete3Wind(self,event):
        self.Delete(event)

    # Bật/tắt MBA 3 cuộn dây
    def Turn_On_Off( self, event ):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if int(status) == 1:
                    psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,INTGAR8 = 0)
                    self.myGrid3Wind.SetCellValue(row,8,str(0))
                else:
                    psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,INTGAR8 = 1)
                    self.myGrid3Wind.SetCellValue(row,8,str(1))
                psspy.save(path)
        else:
            if int(status) == 1:
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,INTGAR8 = 0)
                self.myGrid3Wind.SetCellValue(row,8,str(0))
            else:
                psspy.three_wnd_imped_chng_3(frBusNum,toBusNum,lastBusNum,id,INTGAR8 = 1)
                self.myGrid3Wind.SetCellValue(row,8,str(1))
            psspy.save(self.Path)
        self.Update3WindPage(event,1)

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            if int(status) == 1:
                f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8 = 0)\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
            else:
                f.writelines("psspy.three_wnd_imped_chng_3({a},{b},{c},'{d}',INTGAR8 = 1)\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d= str(id)))
            f.close()

    # Xóa MBA 3 CD
    def Delete(self, event):
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.purg3wnd(frBusNum,toBusNum,lastBusNum,str(id))
                psspy.save(path)
        else:
            psspy.purg3wnd(frBusNum,toBusNum,lastBusNum,str(id))
            psspy.save(self.Path)
        self.Update3WindPage(event,0)

        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.purg3wnd({a},{b},{c},{d})\n".format(a=frBusNum,b=toBusNum,c=lastBusNum,d=id))
            f.close()

    # Cập nhật trang MBA 3 CD
    @profiled('refresh.transformer_3wind')
    @batched_grid_update('myGrid3Wind', 'parent.gridFile')
    def Update3WindPage(self,event,flagChange):
        if self.parent.flagUpdate == 0 and self.parent.flagPaste == 0:
            self.parent.Mark_Pending_Refresh('3wind')
        if self.parent.flagUpdate == 1:
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdate3Wind(event, i, path,flagChange)
            else:
                self.onUpdate3Wind(event,self.indexFile,self.Path,flagChange)
            self.parent.onUpdateFcn(event)

        elif self.parent.flagPaste == 0:
            if flagChange == 0:
                clear_grid(self.myGrid3Wind)
                self.matrix3Wind[self.indexFile] = load3windTab(self.Path)
                for row1 in range(len(self.matrix3Wind[self.indexFile])):
                    for column1 in range(len(self.matrix3Wind[self.indexFile][0])):
                        self.myGrid3Wind.SetCellValue(row1,column1,str(self.matrix3Wind[self.indexFile][row1][column1]))
            self.parent.onUpdateFcn(event)

    def onUpdate3Wind(self,event, indexfile, path,flagChange):
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
            
            if flagChange == 0:
                clear_grid(self.myGrid3Wind)
                self.matrix3Wind[self.indexFile] = load3windTab(self.Path)
                for row1 in range(len(self.matrix3Wind[self.indexFile])):
                    for column1 in range(len(self.matrix3Wind[self.indexFile][0])):
                        self.myGrid3Wind.SetCellValue(row1,column1,str(self.matrix3Wind[self.indexFile][row1][column1]))
