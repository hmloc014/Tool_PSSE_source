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
from LoadTab import loadBusTab,loadAreaInfo,loadFileInfo,loadZoneInfo,loadMachineTab,load2windTab,loadLoadTab,loadSourceLoadInfo
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

TWOPLACE = Decimal(10)**-2
    
class CustomGrid2Wind(MyFrame1):
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
        self.matrix2Wind = []
        self.myGridBus = wx.grid.Grid
        self.myGridArea = wx.grid.Grid
        self.myGridZone = wx.grid.Grid
        self.myGridFile = wx.grid.Grid
        self.myGridShunt = wx.grid.Grid
        self.myGrid2Wind = wx.grid.Grid

    # chức năng thực hiện tại ô được chọn của trang MBA 2 cuộn dây
    def on_selected_cell_grid_2wind( self, event ):
        global row,col,cellValue,cellVal,frBusNum,frBusName,toBusNum,toBusName,id,status,tapPosition,specifiedR,specifiedX,rate,ratio,connectionCode,R01,X01
        global frBusNumUpper,frBusNameUpper,toBusNumUpper,toBusNameUpper,idUpper,statusUpper,tapPositionUpper,specifiedRUpper,specifiedXUpper,rateUpper,ratioUpper,connectionCodeUpper,R01Upper,X01Upper
        row = event.GetRow()
        col = event.GetCol()
        colLabel = self.myGrid2Wind.GetColLabelValue(col)
        cellValue = self.myGrid2Wind.GetCellValue(row,col)

        if row>0:
            cellVal = self.myGrid2Wind.GetCellValue(row-1,col)
            frBusNumUpper =int(self.myGrid2Wind.GetCellValue(row-1,0))
            frBusNameUpper = self.myGrid2Wind.GetCellValue(row-1,1)
            toBusNumUpper = int(self.myGrid2Wind.GetCellValue(row-1,2))
            toBusNameUpper = self.myGrid2Wind.GetCellValue(row-1,3)
            idUpper = str(self.myGrid2Wind.GetCellValue(row-1,4))
            statusUpper = int(self.myGrid2Wind.GetCellValue(row-1,5))
            tapPositionUpper = int(self.myGrid2Wind.GetCellValue(row-1,6))
            specifiedRUpper = float(self.myGrid2Wind.GetCellValue(row-1,7))
            specifiedXUpper = float(self.myGrid2Wind.GetCellValue(row-1,8))
            rateUpper = float(self.myGrid2Wind.GetCellValue(row-1,9))
            ratioUpper = float(self.myGrid2Wind.GetCellValue(row-1,10))
            connectionCodeUpper = int(self.myGrid2Wind.GetCellValue(row-1,14))
            R01Upper = float(self.myGrid2Wind.GetCellValue(row-1,15))
            X01Upper = float(self.myGrid2Wind.GetCellValue(row-1,16))

        frBusNum =int(self.myGrid2Wind.GetCellValue(row,0))
        frBusName = self.myGrid2Wind.GetCellValue(row,1)
        toBusNum = int(self.myGrid2Wind.GetCellValue(row,2))
        toBusName = (self.myGrid2Wind.GetCellValue(row,3))
        id = str(self.myGrid2Wind.GetCellValue(row,4))
        status = int(self.myGrid2Wind.GetCellValue(row,5))
        tapPosition = int(self.myGrid2Wind.GetCellValue(row,6))
        specifiedR = float(self.myGrid2Wind.GetCellValue(row,7))
        specifiedX = float(self.myGrid2Wind.GetCellValue(row,8))
        rate = float(self.myGrid2Wind.GetCellValue(row,9))
        ratio = float(self.myGrid2Wind.GetCellValue(row,10))
        connectionCode = int(self.myGrid2Wind.GetCellValue(row,14))
        R01 = float(self.myGrid2Wind.GetCellValue(row,15))
        X01 = float(self.myGrid2Wind.GetCellValue(row,16))

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng MBA 2 cuộn dây
    def on_cell_change_grid_2wind( self, event ):
        col1 = col
        if self.uk == 13:
            row1 = row-1
        else:
            row1 = row

        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if i == 0:
                    self.on_cell_change_grid_2wind_fcn(event,row1,col1,0 )
                else:
                    self.on_cell_change_grid_2wind_fcn(event,row1,col1,1 )
                psspy.save(path)
        else:
            self.on_cell_change_grid_2wind_fcn(event,row1,col1,0 )
            psspy.save(self.Path)
        self.Update2WindPage(event,1)

    def on_cell_change_grid_2wind_fcn( self, event,row,col,flag ):
        row1 = row
        col1 = col
        if self.uk == 13: # nhấn Enter
            cellVal = self.myGrid2Wind.GetCellValue(row1,col1)
            if col1 == 5: # change status
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR1 = int(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR1 = {d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),d=int(cellVal)))
                    f.close()

            if col1 == 6: # change tab position
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR7 = int(cellVal),INTGAR9 = frBusNumUpper,INTGAR12 = 0)

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR7 = {d},INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),d=int(cellVal),e=frBusNumUpper))
                    f.close()

            if col1 == 7: # change specific R
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR9 = frBusNumUpper,INTGAR12 = 0,REALARI1 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI1 ={d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),e=frBusNumUpper,d=float(cellVal)))
                    f.close()
            if col1 == 8: # change specific X
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR9 = frBusNumUpper,INTGAR12 = 0,REALARI2 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI2 ={d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),e=frBusNumUpper,d=float(cellVal)))
                    f.close()
            if col1 == 9: # change Rate
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR9 = frBusNumUpper,INTGAR12 = 0,REALARI9 = float(cellVal),REALARI10 = float(cellVal),REALARI11 =float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI9 ={d},REALARI10 ={d},REALARI11 ={d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),e=frBusNumUpper,d=float(cellVal)))
                    f.close()
            if col1 == 10: # change Ratio
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR9 = frBusNumUpper,INTGAR12 = 0,REALARI4 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI4 ={d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),e=frBusNumUpper,d=float(cellVal)))
                    f.close()
            if col1 == 14: # connection code
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR9 = frBusNumUpper,INTGAR12 = 0)
                psspy.seq_two_winding_data_3(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR1 = int(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),e=frBusNumUpper))
                    f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',INTGAR1 = {d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),d=int(cellVal)))
                    f.close()
            if col1 == 15: # change R01
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR9 = frBusNumUpper,INTGAR12 = 0)
                psspy.seq_two_winding_data_3(frBusNumUpper,toBusNumUpper,str(idUpper),REALAR3 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),e=frBusNumUpper))
                    f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',REALAR3 = {d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),d=float(cellVal)))
                    f.close()
            if col1 == 16: # change X01
                psspy.two_winding_chng_4(frBusNumUpper,toBusNumUpper,str(idUpper),INTGAR9 = frBusNumUpper,INTGAR12 = 0)
                psspy.seq_two_winding_data_3(frBusNumUpper,toBusNumUpper,str(idUpper),REALAR4 = float(cellVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),e=frBusNumUpper))
                    f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',REALAR4 = {d})\n".format(a=frBusNumUpper,b=toBusNumUpper,c= str(idUpper),d=float(cellVal)))
                    f.close()

        else: # thay đổi bằng cách di chuyển sang ô khác sử dụng con trỏ chuột
            cellNewVal = self.myGrid2Wind.GetCellValue(row1,col1)

            if col1 == 5: # change status
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR1 = int(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR1 = {d})\n".format(a=frBusNum,b=toBusNum,c= str(id),d=int(cellNewVal)))
                    f.close()

            if col1 == 6: # change tab position
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR7 = int(cellNewVal),INTGAR9 = frBusNum,INTGAR12 = 0)

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR7 = {d},INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNum,b=toBusNum,c= str(id),d=int(cellNewVal),e=frBusNum))
                    f.close()

            if col1 == 7: # change specific R
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR9 = frBusNum,INTGAR12 = 0,REALARI1 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI1 ={d})\n".format(a=frBusNum,b=toBusNum,c= str(id),e=frBusNum,d=float(cellNewVal)))
                    f.close()
            if col1 == 8: # change specific X
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR9 = frBusNum,INTGAR12 = 0,REALARI2 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI2 ={d})\n".format(a=frBusNum,b=toBusNum,c= str(id),e=frBusNum,d=float(cellNewVal)))
                    f.close()
            if col1 == 9: # change Rate
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR9 = frBusNum,INTGAR12 = 0,REALARI9 = float(cellNewVal),REALARI10 = float(cellNewVal),REALARI11 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI9 ={d},REALARI10 ={d},REALARI11 ={d})\n".format(a=frBusNum,b=toBusNum,c= str(id),e=frBusNum,d=float(cellNewVal)))
                    f.close()
            if col1 == 10: # change Ratio
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR9 = frBusNum,INTGAR12 = 0,REALARI4 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0,REALARI4 ={d})\n".format(a=frBusNum,b=toBusNum,c= str(id),e=frBusNum,d=float(cellNewVal)))
                    f.close()
            if col1 == 14: # connection code
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR9 = frBusNum,INTGAR12 = 0)
                psspy.seq_two_winding_data_3(frBusNum,toBusNum,str(id),INTGAR1 = int(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNum,b=toBusNum,c= str(id),e=frBusNum))
                    f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',INTGAR1 = {d})\n".format(a=frBusNum,b=toBusNum,c= str(id),d=int(cellNewVal)))
                    f.close()
            if col1 == 15: # change R01
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR9 = frBusNum,INTGAR12 = 0)
                psspy.seq_two_winding_data_3(frBusNum,toBusNum,str(id),REALAR3 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNum,b=toBusNum,c= str(id),e=frBusNum))
                    f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',REALAR3 = {d})\n".format(a=frBusNum,b=toBusNum,c= str(id),d=float(cellNewVal)))
                    f.close()
            if col1 == 16: # change X01
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR9 = frBusNum,INTGAR12 = 0)
                psspy.seq_two_winding_data_3(frBusNum,toBusNum,str(id),REALAR4 = float(cellNewVal))

                if self.parent.macroFile != '' and flag == 0:
                    f = open(self.parent.macroFile,'a')
                    f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR9 = {e},INTGAR12 = 0)\n".format(a=frBusNum,b=toBusNum,c= str(id),e=frBusNum))
                    f.writelines("psspy.seq_two_winding_data_3({a},{b},'{c}',REALAR4 = {d})\n".format(a=frBusNum,b=toBusNum,c= str(id),d=float(cellNewVal)))
                    f.close()

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng MBA 2 cuộn dây, mở righ click tab
    def on_cell_right_click_grid_2wind( self, event ):
        menus = [(wx.NewId(), "Turn On/Off 2 winding", self.turnOnOff),
                 (wx.NewId(), "Delete 2 winding", self.delete2Wind)]
        popup_menu = wx.Menu()

        for menu in menus:
            if menu is None:
                popup_menu.AppendSeparator()
                continue
            popup_menu.Append(menu[0], menu[1])
            self.Bind(wx.EVT_MENU, menu[2], id=menu[0])
        self.grid2wind.PopupMenu(popup_menu, self.grid2wind.ScreenToClient(wx.GetMousePosition()))
        popup_menu.Destroy()
        return

    # bật/tắt MBA 2 cuộn dây
    def turnOnOff(self,event):
        self.Turn_On_Off(event)

    # xóa MBA 2 CD
    def delete2Wind(self,event):
        self.Delete(event)

    def Turn_On_Off( self, event ):
        # cập nhật đồng thời cho nhiều file
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                if int(status) == 1:
                    psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR1 = 0)
                    self.myGrid2Wind.SetCellValue(row,5,str(0))
                else:
                    psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR1 = 1)
                    self.myGrid2Wind.SetCellValue(row,5,str(1))
                psspy.save(path)
        else: # chỉ cập nhật cho file hiện tại
            if int(status) == 1:
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR1 = 0)
                self.myGrid2Wind.SetCellValue(row,5,str(0))
            else:
                psspy.two_winding_chng_4(frBusNum,toBusNum,str(id),INTGAR1 = 1)
                self.myGrid2Wind.SetCellValue(row,5,str(1))
            psspy.save(self.Path)
        self.Update2WindPage(event,1)

        # nếu có enable chức năng record macro thì sẽ ghi thao tác này vào file macro
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            if int(status) == 1:
                f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR1 = 0)\n".format(a=frBusNum,b=toBusNum,c= str(id)))
            else:
                f.writelines("psspy.two_winding_chng_4({a},{b},'{c}',INTGAR1 = 1)\n".format(a=frBusNum,b=toBusNum,c= str(id)))
            f.close()

    # xóa MBA 2 CD
    def Delete(self, event):
        # cập nhật đồng thời cho nhiều file
        if self.parent.flagSynch == 1:
            for i,path in enumerate(self.PathFile):
                psspy.case(path)
                psspy.purgbrn(frBusNum,toBusNum,str(id))
                psspy.save(path)
        else: # chỉ cập nhật cho file hiện tại
            psspy.purgbrn(frBusNum,toBusNum,str(id))
            psspy.save(self.Path)
        self.Update2WindPage(event,0)

        # nếu có enable chức năng record macro thì sẽ ghi thao tác này vào file macro
        if self.parent.macroFile != '':
            f = open(self.parent.macroFile,'a')
            f.writelines("psspy.purgbrn({a},{b},{c})\n".format(a=frBusNum,b=toBusNum,c=id))
            f.close()

    # cập nhật bảng MBA 2 CD
    @profiled('refresh.transformer_2wind')
    @batched_grid_update('myGrid2Wind', 'grid2wind', 'parent.gridFile')
    def Update2WindPage(self,event,flagChange):
        # cập nhật từng bước
        if self.parent.flagUpdate == 1:
            # cập nhật đồng bộ cho các file
            if self.parent.flagSynch == 1:
                for i,path in enumerate(self.PathFile):
                    self.onUpdate2Wind(event, i, path,flagChange)
            else:
                self.onUpdate2Wind(event,self.indexFile,self.Path,flagChange)
            # tính lại TLCS và cập nhật lại toàn bộ bảng
            self.parent.onUpdateFcn(event)

        elif self.parent.flagPaste == 0: # không thực hiện chức năng copy-paste nên cập nhật ngay sau mỗi thay đổi, 
            #nếu thực hiện copy-paste thì chỉ cập nhật sau khi paste đến giá trị cuối cùng
            if flagChange == 0: # có sự thay đổi kích thước bảng MBA 2 CD, nếu =1 thì k cần xóa đi cập nhật lại
                clear_grid(self.grid2wind)
                self.matrix2Wind[self.indexFile] = load2windTab(self.Path)
                for row1 in range(len(self.matrix2Wind[self.indexFile])):
                    for column1 in range(len(self.matrix2Wind[self.indexFile][0])):
                        self.myGrid2Wind.SetCellValue(row1,column1,str(self.matrix2Wind[self.indexFile][row1][column1]))
            self.parent.onUpdateFcn(event)

    # khi cập nhật lại bảng 2 wind, cần cập nhật lại kết quả tính TLCS ở bảng file
    def onUpdate2Wind(self,event, indexfile, path,flagChange):
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
            if flagChange == 0: # =0 có nghĩa là có sự thay đổi kích thước bảng, nên cần xóa đi cập nhật lại, nếu =1
                # nghĩa là đã thay đổi trực tiếp trên bảng 2 wind rồi, không cần xóa đi cập nhật lại nữa mà chỉ cần cập nhật lại bảng file (thông tin TLCS) thôi
                # như vậy việc thay đổi thông tin/ bật, tắt MBA không ảnh hưởng đến kích thước bảng nên flagchange = 1, chỉ khi add/delete thì mới thay đổi kích thước và flagchange = 0
                clear_grid(self.parent.grid2wind)

                self.matrix2Wind[self.indexFile] = load2windTab(self.Path)
                for row1 in range(len(self.matrix2Wind[self.indexFile])):
                    for column1 in range(len(self.matrix2Wind[self.indexFile][0])):
                        self.parent.grid2wind.SetCellValue(row1,column1,str(self.matrix2Wind[self.indexFile][row1][column1]))
