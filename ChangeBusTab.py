# -*- coding: utf-8 -*-
import psspy
import wx
import wx.grid

# thay đổi trong bảng thông tin bus
def change(myGridBus= wx.grid,matrixBus = [[]],rowNum=0,col=0,cellValue='',macroFile='',flag=0):
    row = rowNum
    area = int(myGridBus.GetCellValue(row,3))
    zone = int(myGridBus.GetCellValue(row,5))
    baseKV = float(myGridBus.GetCellValue(row,2))
    VM = float(myGridBus.GetCellValue(row,9))
    VA = float(myGridBus.GetCellValue(row,10))
    label = myGridBus.GetColLabelValue(col)
    cellValueNew = myGridBus.GetCellValue(row,col)
    IDE = int(myGridBus.GetCellValue(row,8))
    Owner = int(myGridBus.GetCellValue(row,7))

    if label == "Bus Name":
        psspy.bus_chng_3(int(myGridBus.GetCellValue(row,0)),[],[],cellValueNew)#[1,area,zone,1],[baseKV,VM,VA,1.1,0.9,1.1,0.9],cellValueNew)
        # ghi vào file record thao tác
        if macroFile != '' and flag == 0:
            f = open(macroFile,'a')
            f.writelines("""psspy.bus_chng_3({a},[],[],'{g}')\n""".format(a=int(myGridBus.GetCellValue(row,0)),b=area,c=zone,d=baseKV,e=VM,f=VA,g=cellValueNew))
            f.close()

    elif label == 'Bus Num': 
        psspy.bus_number(int(cellValue),int(cellValueNew))
        # ghi vào file record thao tác
        if macroFile != '' and flag == 0:
            f = open(macroFile,'a')
            f.writelines("""psspy.bus_number({a},{b})\n""".format(a=int(cellValue),b=int(cellValueNew)))
            f.close()

    elif label == 'Area':
        psspy.bus_chng_3(int(myGridBus.GetCellValue(row,0)),[IDE,int(cellValueNew),zone,Owner],[baseKV,VM,VA,1.1,0.9,1.1,0.9],myGridBus.GetCellValue(row,1))
        # ghi vào file record thao tác
        if macroFile != '' and flag == 0:
            f = open(macroFile,'a')
            f.writelines("""psspy.bus_chng_3({a},[{b},{c},{d},{e}],[{f},{g},{h},1.1,0.9,1.1,0.9],'{i}')\n""".format(a=int(myGridBus.GetCellValue(row,0)),b=IDE,c=int(cellValueNew),d=zone,e=Owner,f=baseKV,g=VM,h=VA,i=myGridBus.GetCellValue(row,1)))
            f.close()

    elif label == 'Zone':
        psspy.bus_chng_3(int(myGridBus.GetCellValue(row,0)),[IDE,area,int(cellValueNew),Owner],[baseKV,VM,VA,1.1,0.9,1.1,0.9],myGridBus.GetCellValue(row,1))
        # ghi vào file record thao tác
        if macroFile != '' and flag == 0:
            f = open(macroFile,'a')
            f.writelines("""psspy.bus_chng_3({a},[{b},{c},{d},{e}],[{f},{g},{h},1.1,0.9,1.1,0.9],'{i}')\n""".format(a=int(myGridBus.GetCellValue(row,0)),b=IDE,c=area,d=int(cellValueNew),e=Owner,f=baseKV,g=VM,h=VA,i=myGridBus.GetCellValue(row,1)))
            f.close()

    elif label == 'Base KV':
        psspy.bus_chng_3(int(myGridBus.GetCellValue(row,0)),[IDE,area,zone,Owner],[float(cellValueNew),VM,VA,1.1,0.9,1.1,0.9],myGridBus.GetCellValue(row,1))
        # ghi vào file record thao tác
        if macroFile != '' and flag == 0:
            f = open(macroFile,'a')
            f.writelines("""psspy.bus_chng_3({a},[{b},{c},{d},{e}],[{f},{g},{h},1.1,0.9,1.1,0.9],'{i}')\n""".format(a=int(myGridBus.GetCellValue(row,0)),b=IDE,c=area,d=zone,e=Owner,f=float(cellValueNew),g=VM,h=VA,i=myGridBus.GetCellValue(row,1)))
            f.close()

    elif label == 'Owner':
        psspy.bus_chng_3(int(myGridBus.GetCellValue(row,0)),[IDE,area,zone,int(cellValueNew)],[baseKV,VM,VA,1.1,0.9,1.1,0.9],myGridBus.GetCellValue(row,1))
        # ghi vào file record thao tác
        if macroFile != '' and flag == 0:
            f = open(macroFile,'a')
            f.writelines("""psspy.bus_chng_3({a},[{b},{c},{d},{e}],[{f},{g},{h},1.1,0.9,1.1,0.9],'{i}')\n""".format(a=int(myGridBus.GetCellValue(row,0)),b=IDE,c=area,d=zone,e=int(cellValueNew),f=baseKV,g=VM,h=VA,i=myGridBus.GetCellValue(row,1)))
            f.close()

    elif label == 'Code':
        psspy.bus_chng_3(int(myGridBus.GetCellValue(row,0)),[int(cellValueNew),area,zone,Owner],[baseKV,VM,VA,1.1,0.9,1.1,0.9],myGridBus.GetCellValue(row,1))
        # ghi vào file record thao tác
        if macroFile != '' and flag == 0:
            f = open(macroFile,'a')
            f.writelines("""psspy.bus_chng_3({a},[{b},{c},{d},{e}],[{f},{g},{h},1.1,0.9,1.1,0.9],'{i}')\n""".format(a=int(myGridBus.GetCellValue(row,0)),b=int(cellValueNew),c=area,d=zone,e=Owner,f=baseKV,g=VM,h=VA,i=myGridBus.GetCellValue(row,1)))
            f.close()
# thêm mới bus
def addNew(myGridBus= wx.grid,row=0):
    busNum = int(myGridBus.GetCellValue(row,0))
    name = myGridBus.GetCellValue(row,1)
    area = int(myGridBus.GetCellValue(row,3))
    zone = int(myGridBus.GetCellValue(row,5))
    baseKV = float(myGridBus.GetCellValue(row,2))
    VM = float(myGridBus.GetCellValue(row,9))
    VA = float(myGridBus.GetCellValue(row,10))

    if (busNum or name or area or zone or baseKV or VM or VA) == '':
        wx.MessageBox("Please fill in all required fields!")
    else:
        psspy.bus_data_3(busNum,[1,area,zone,1],[ baseKV, VM,VA,1.1,0.9,1.1,0.9],name)
