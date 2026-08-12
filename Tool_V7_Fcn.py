# -*- coding: utf-8 -*-
import glob, os, sys
import time
# reload(sys)
# sys.setdefaultencoding('utf-8')
import pssepath
from Tool_V7 import MyFrame1
import wx
import wx.xrc
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
from subprocess import call
from Export_To_Cad import acad
# from Export_To_Cad_NVA import acadMVA
# from Export_To_Cad_Load_Percent import acadLoadPercent
from LoadTab import load2windTab, loadBusTab, loadMachineTab,searchByChoice,loadBusNumberEnter,delFileInfo,loadFileInfo,loadAreaInfo,loadZoneInfo,loadLoadTab,loadShuntTab,loadSourceLoadInfo
from LoadTab import load3windTab, select_zone_from_area, select_bus_from_zone, select_bus_from_matrixBus,select_source_from_zone,select_load_from_zone,select_shunt_from_zone
from LoadTab import select_bus_from_area, select_source_from_area,select_load_from_area,select_shunt_from_area,select_2Wind_from_area,select_3Wind_from_area,select_2Wind_from_zone,select_3Wind_from_zone
from DialogBox import getInput, openFile, openMultipleFile, openFolder, saveFile
from record import PsseCommandRecorder, RecorderError, prompt_automation_path
from Create_Sub_Mon_Con_Files import createSubFile, createMonFile, createConFile
from gridSearch import CustomGridSearch
from ConnectDataBase import ConnectDatabase
from sourcePage import CustomGridSource
from loadPage import CustomGridLoad
from shuntPage import CustomGridShunt
from gridZone import CustomGridZone
from gridArea import CustomGridArea
from dynamicPage import CustomGridDyn
from twoWindPage import CustomGrid2Wind
from threeWindPage import CustomGrid3Wind

from copy_paste import CopyPaste
import wx.grid as gridlib
import numpy as np
import pssarrays
# import run
# from NoteBook import TestNB
from ChangeBusTab import change,addNew
from decimal import *
from redirectOuput import silence
import contextlib
from Calculation import Calculation
from ui_performance import (batched_grid_update, clear_grid, debounced_search,
                            profiled)
# import multiprocessing as mt
# wiki.ozanh.com/doku.php?id=python:misc:wxpython_postevent_threading
# from dialogEx import Mywin

PATH = ''
PATHFILE = []
PATH_ORIGIN = ''
dyrNewFile = ''
PATHFILE_ORIGIN = []
indexFile = 0
busCode = [[]]
busZoneName = [[]]
busAreaName = [[]]
busOwnerName = [[]]
matrixGen = []
matrixLoad = []
matrixShunt = []
matrixBranch = []
matrix2WindBr = []
matrix3WindBr = []
matrix2Wind = []
matrix3Wind = []
matrixBus = []
matrixArea = []
matrixZone = []
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
ukNumSearch = 0
ukNumLoad = 0
ukNumSource = 0
ukNumBus = 0
ukNum2Wind = 0
ukNum3Wind = 0
ukNumShunt = 0
busNumber = 0
previousBusNumber = 0
count = 0
selectedZoneRow = 0
selectedZoneNum = 0
TWOPLACE = Decimal(10)**-2

class CustomMyframe1(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.LOCATION = os.getcwd()
        self.Path = ''
        self.PathFile = [[]]
        self.parent = parent
        self.flagUpdate = 1
        self.flagReload = 0
        self.flagSynch = 0
        self.flagChangePPercent = 0
        self.flagChangeDeltaP = 0
        self.flagChangeNewPVal = 0
        self.flagRestriction = 0
        self.flagCreateMacro = 0
        self.flagPaste = 0
        # binh thuong flagPaste = 0, nen se cap nhat bt, 
        # con khi copy-paste, neu chon che do update later
        # thi sau khi cp den phan tu cuoi cung moi update
        self.macroFile = ''
        self.commandRecorder = PsseCommandRecorder(psspy)
        self.Count = 0
        self.indexInDyr = []
        self.priority = 0
        self.onUpdate = 0
        self.rowArea = 0
        self.colArea = 0
        self.rowZone = 0
        self.colZone = 0

        self.gridAreaLink = CustomGridArea(self)
        self.gridZoneLink = CustomGridZone(self)
        self.gridBusInfoLink = ConnectDatabase(self)

        self.gridSearchLink = CustomGridSearch(self)
        self.Calculation_Link = Calculation(self)
        self.gridSourceLink = CustomGridSource(self)
        self.gridLoadLink = CustomGridLoad(self)
        self.gridShuntLink = CustomGridShunt(self)
        self.gridDynLink = CustomGridDyn(self)
        self.grid2windLink = CustomGrid2Wind(self)
        self.grid3windLink = CustomGrid3Wind(self)
        self.copyPaste = CopyPaste(self)
        self.flagOnClose = 0
        
    def Close_PSSE( self, event ):
        wx.MessageBox("Close Window!")

    # Tắt tool, xóa các file trung gian tại ổ D
    def onClose( self, event ):
        if self.commandRecorder.is_recording:
            try:
                self.commandRecorder.stop()
            except RecorderError:
                pass
        for path in PATHFILE:
            os.remove(path)
        event.Skip()

    # Chức năng tắt file được chọn
    def Close_PSSE_Fcn( self, event ):
        self.flagOnClose = 1
        global PATH_ORIGIN,PATHFILE,PATHFILE_ORIGIN,PATH, indexFile
        wx.MessageBox("Close {}".format(PATHFILE_ORIGIN[indexFile]))
        # Loại bỏ đường dẫn của file được chọn trong mảng chứa đường dẫn của các file đang mở với index tương ứng
        PATHFILE.pop(indexFile)
        PATHFILE_ORIGIN.pop(indexFile)
        if len(PATHFILE_ORIGIN) != 0:
            PATH_ORIGIN = PATHFILE_ORIGIN[0]
            PATH = PATHFILE[0]
        else:
            PATH_ORIGIN = ''
            PATH = ''
        # Loại bỏ thông số của file được chọn trong các bảng thông số với index tương ứng
        matrixArea.pop(indexFile)
        matrixZone.pop(indexFile)
        matrixBus.pop(indexFile)
        matrixGen.pop(indexFile)
        matrixLoad.pop(indexFile)
        matrixShunt.pop(indexFile)
        matrix2Wind.pop(indexFile)
        matrix3Wind.pop(indexFile)
        
        # xóa thông tin trong grid file
        for row1 in range(myGridFile.GetNumberRows()):
                for column1 in range(myGridFile.GetNumberCols()):
                    myGridFile.SetCellValue(row1,column1,"")
        delFileInfo(indexFile)
        # nếu còn file khác trong tool, cập nhật lại thông tin trong grid file và các grid còn lại
        if len(PATHFILE) != 0:
            fileInfo = loadFileInfo(PATHFILE[0])
            fileInfo1 = [fileInfo[0][0],fileInfo[1][0],fileInfo[2][0],fileInfo[3][0],fileInfo[4][0],fileInfo[5][0]]
            fileInfoArray = np.array(fileInfo1)
            fileInfoTranspose = fileInfoArray.transpose()
            for row in range(len(fileInfoTranspose)):
                for column in range(len(fileInfoTranspose[0])):
                    myGridFile.SetCellValue(row,column,str(fileInfoTranspose[row][column]))
            self.UpdatedData(event,0,PATHFILE[0])
            indexFile = 0
            self.busNumberEnter_Fcn(event)
        else: # file được chọn để đóng là file duy nhất còn lại trong tool, khi đóng tool, tất cả các trang reset lại
            for row1 in range(myGridArea.GetNumberRows()):
                for column1 in range(myGridArea.GetNumberCols()):
                    myGridArea.SetCellValue(row1,column1,"")
            for row1 in range(myGridZone.GetNumberRows()):
                for column1 in range(myGridZone.GetNumberCols()):
                    myGridZone.SetCellValue(row1,column1,"")
            for row1 in range(myGridBus.GetNumberRows()):
                for column1 in range(myGridBus.GetNumberCols()): 
                    myGridBus.SetCellValue(row1,column1,"")
            for row1 in range(self.gridBusInfo.GetNumberRows()):
                for column1 in range(self.gridBusInfo.GetNumberCols()): 
                    self.gridBusInfo.SetCellValue(row1,column1,"")
            for row1 in range(self.m_grid6.GetNumberRows()):
                for column1 in range(27): 
                    self.m_grid6.SetCellValue(row1,column1,"")
            for row1 in range(self.gridLoad.GetNumberRows()):
                for column1 in range(12):
                    self.gridLoad.SetCellValue(row1,column1,"")
            for row1 in range(self.gridShunt.GetNumberRows()):
                for column1 in range(self.gridShunt.GetNumberCols()):
                    self.gridShunt.SetCellValue(row1,column1,"")
            for row1 in range(self.grid2wind.GetNumberRows()):
                for column1 in range(self.grid2wind.GetNumberCols()):
                    self.grid2wind.SetCellValue(row1,column1,"")
            for row1 in range(self.grid3wind.GetNumberRows()):
                for column1 in range(self.grid3wind.GetNumberCols()):
                    self.grid3wind.SetCellValue(row1,column1,"")
            content = self.terminalText
            content.Value = ''
        event.Skip()

    # chức năng mở 1 file PSSE
    def Open_PSSE( self, event ): 
        global PATHFILE_ORIGIN,PATH_ORIGIN,PATHFILE,PATH
        global matrixBus
        global myGridBus
        global matrixGen
        global matrixLoad
        # global matrixBranch
        global matrixShunt
        global matrix2Wind
        global matrix3Wind
        global matrixArea
        global myGridArea
        global matrixZone
        global myGridZone
        global myGridFile
        global myGrid2Wind
        global myGrid3Wind
        global fileInfoTranspose

        PATH_ORIGIN = openFile(self,'Please select .sav file', '*.sav')
        self.Path = PATH_ORIGIN
        # print('self.PATH_ORIGIN: ',PATH_ORIGIN)

        # Assign value to grid
        myGridBus = self.gridSearch
        myGridFile = self.gridFile
        myGridArea = self.gridArea
        myGridZone = self.gridZone
        myGrid2Wind = self.grid2wind
        myGrid3Wind = self.grid3wind

        psspy.psseinit(50000)
        psspy.case(PATH_ORIGIN)
        fileName = os.path.basename(PATH_ORIGIN)
        dirName = r"D:/"

        # first open this file
        if not PATH_ORIGIN in PATHFILE_ORIGIN: 
            PATHFILE_ORIGIN.append(PATH_ORIGIN)
            PATH = os.path.join(dirName,fileName[0:-4] + "-{}".format(len(PATHFILE_ORIGIN))+".sav") 
            PATHFILE.append(PATH)
            # print('-----Path:',PATH)
            psspy.save(PATH)
            matrixArea.append(loadAreaInfo(PATH))
            matrixZone.append(loadZoneInfo(PATH))
            matrixBus.append(loadBusTab(PATH))
            matrixGen.append(loadMachineTab(PATH))
            matrixLoad.append(loadLoadTab(PATH))
            matrixShunt.append(loadShuntTab(PATH))
            matrix2Wind.append(load2windTab(PATH))
            matrix3Wind.append(load3windTab(PATH))
        # file exist
        else: 
            fileIndex = PATHFILE_ORIGIN.index(PATH_ORIGIN)
            PATH = PATHFILE[fileIndex]
            psspy.save(PATH)
            matrixArea[fileIndex] = loadAreaInfo(PATH)
            matrixZone[fileIndex] = loadZoneInfo(PATH)
            matrixBus[fileIndex] = loadBusTab(PATH)
            matrixGen[fileIndex] = loadMachineTab(PATH)
            matrixLoad[fileIndex] = loadLoadTab(PATH)
            matrixShunt[fileIndex] = loadShuntTab(PATH)
            matrix2Wind[fileIndex] = load2windTab(PATH)
            matrix3Wind[fileIndex] = load3windTab(PATH)

        fileIndex = PATHFILE.index(PATH)
        sourceLoad = loadSourceLoadInfo(PATH)
        [totalPgen,totalLoad, totalPgenNorth,totalLoadNorth,totalPgenCentral,totalLoadCentral,totalPgenSouth,totalLoadSouth,ratio] = sourceLoad

        # Table of files
        fileInfo = loadFileInfo(PATH)
        fileInfo1 = [fileInfo[0][0],fileInfo[1][0],fileInfo[2][0],fileInfo[3][0],fileInfo[4][0],fileInfo[5][0]]
        fileInfoArray = np.array(fileInfo1)
        fileInfoTranspose = fileInfoArray.transpose()

        # Table of Zone and Area
        currentMatrixArea = matrixArea[fileIndex]
        currentMatrixZone = matrixZone[fileIndex]
        currentMatrixBus = matrixBus[fileIndex]
        currentMatrixGen = matrixGen[fileIndex]
        currentMatrixLoad = matrixLoad[fileIndex]
        currentMatrixShunt = matrixShunt[fileIndex]
        currentMatrix2Wind = matrix2Wind[fileIndex]
        currentMatrix3Wind = matrix3Wind[fileIndex]
        
        global areaList,zoneList
        areaList = currentMatrixArea[:,0]
        zoneList = currentMatrixZone[:,0]


        self.BusNumInput.SetItems(currentMatrixBus[:,0].tolist())

        if busNumber != 0:
            self.BusNumInput.SetValue(str(busNumber))
        
        # reload all grid
        if(indexFile>0):
            for row1 in range(myGridArea.GetNumberRows()):
                for column1 in range(myGridArea.GetNumberCols()):
                    myGridArea.SetCellValue(row1,column1,"")
            for row1 in range(myGridZone.GetNumberRows()):
                for column1 in range(myGridZone.GetNumberCols()):
                    myGridZone.SetCellValue(row1,column1,"")
            for row1 in range(myGridBus.GetNumberRows()):
                for column1 in range(myGridBus.GetNumberCols()):
                    myGridBus.SetCellValue(row1,column1,"")
            for row1 in range(self.m_grid6.GetNumberRows()):
                for column1 in range(27):
                    self.m_grid6.SetCellValue(row1,column1,"")
            for row1 in range(self.gridShunt.GetNumberRows()):
                for column1 in range(self.gridShunt.GetNumberCols()):
                    self.gridShunt.SetCellValue(row1,column1,"")
            for row1 in range(self.grid2wind.GetNumberRows()):
                for column1 in range(self.grid2wind.GetNumberCols()):
                    self.grid2wind.SetCellValue(row1,column1,"")
            for row1 in range(self.grid3wind.GetNumberRows()):
                for column1 in range(self.grid3wind.GetNumberCols()):
                    self.grid3wind.SetCellValue(row1,column1,"")
        for row in range(len(fileInfoTranspose)):
            for column in range(len(fileInfoTranspose[0])):
                myGridFile.SetCellValue(row,column,str(fileInfoTranspose[row][column]))

        for row1 in range(len(currentMatrixArea)):
            for column1 in range(len(currentMatrixArea[0])):
                myGridArea.SetCellValue(row1,column1,str(currentMatrixArea[row1][column1]))

        for row2 in range(len(currentMatrixZone)):
            for column2 in range(len(currentMatrixZone[0])):
                myGridZone.SetCellValue(row2,column2,str(currentMatrixZone[row2][column2])) 

        for row3 in range(len(currentMatrixBus)):
            for column3 in range(len(currentMatrixBus[0])):
                myGridBus.SetCellValue(row3,column3,str(currentMatrixBus[row3][column3]))
        toGenNumList = []
        toGenNameList = []

        for row3 in range(len(currentMatrixGen)):
            toGenNumList.append(str(currentMatrixGen[row3,0]))
            toGenNameList.append(str(currentMatrixGen[row3,1]))
            
            for column3 in range(len(currentMatrixGen[0])):
                self.m_grid6.SetCellValue(row3,column3,str(currentMatrixGen[row3][column3]))
            coff = self.m_grid6.GetCellValue(row3,13)
            self.m_grid6.SetCellValue(row3,26,str(float(coff)/100))

        toLoadNumList = []
        for row3 in range(len(currentMatrixLoad)):
            toLoadNumList.append(str(currentMatrixLoad[row3,0]))
            for column3 in range(len(currentMatrixLoad[0])):
                self.gridLoad.SetCellValue(row3,column3,str(currentMatrixLoad[row3][column3]))
        toShuntNumList = []
        for row3 in range(len(currentMatrixShunt)):
            toShuntNumList.append(str(currentMatrixShunt[row3,1]))
            for column3 in range(len(currentMatrixShunt[0])):
                self.gridShunt.SetCellValue(row3,column3,str(currentMatrixShunt[row3][column3]))

        to2WindNumList = []
        for row3 in range(len(currentMatrix2Wind)):
            to2WindNumList.append(str(currentMatrix2Wind[row3,1]))
            for column3 in range(len(currentMatrix2Wind[0])):
                self.grid2wind.SetCellValue(row3,column3,str(currentMatrix2Wind[row3][column3]))

        to3WindNumList = []
        for row3 in range(len(currentMatrix3Wind)):
            to3WindNumList.append(str(currentMatrix3Wind[row3,1]))
            for column3 in range(len(currentMatrix3Wind[0])):
                self.grid3wind.SetCellValue(row3,column3,str(currentMatrix3Wind[row3][column3]))

        self.genNumber.SetItems(toGenNumList)
        self.genName.SetItems(toGenNameList)
        self.loadNumber.SetItems(toLoadNumList)
        self.shuntNumber.SetItems(toLoadNumList)
        self.search_dyn.SetItems(toGenNumList)

        self.PathFile = PATHFILE
        self.matrixBus = matrixBus  
        # cập nhật lại số liệu nguồn tải cho toàn quốc và miền bắc, trung, nam (miền phân theo zone), làm trong 2 chữ số thập phân
        self.totalSource.SetValue(str(Decimal(totalPgen).quantize(TWOPLACE)))
        self.totalLoad.SetValue(str(Decimal(totalLoad).quantize(TWOPLACE)))
        self.sourceNorth.SetValue(str(Decimal(totalPgenNorth).quantize(TWOPLACE)))
        self.loadNorth.SetValue(str(Decimal(totalLoadNorth).quantize(TWOPLACE)))
        self.sourceCentral.SetValue(str(Decimal(totalPgenCentral).quantize(TWOPLACE)))
        self.loadCentral.SetValue(str(Decimal(totalLoadCentral).quantize(TWOPLACE)))
        self.sourceSouth.SetValue(str(Decimal(totalPgenSouth).quantize(TWOPLACE)))
        self.loadSouth.SetValue(str(Decimal(totalLoadSouth).quantize(TWOPLACE)))
        for i in range(len(ratio)):
            self.m_grid6.SetCellValue(i,29, str((Decimal(ratio[i]).quantize(TWOPLACE))))
        
    # chức năng mở nhiều file psse
    def Open_Multiple_PSSE(self,event):
        global PATHFILE_ORIGIN,PATH_ORIGIN,PATHFILE,PATH
        global matrixBus
        global myGridBus
        global matrixGen
        global matrixLoad
        # global matrixBranch
        global matrixShunt
        global matrixArea
        global myGridArea
        global matrixZone
        global myGridZone
        global myGridFile
        global myGrid2Wind
        global myGrid3Wind
        global fileInfoTranspose

        PATHS = openMultipleFile(self,'Please select input .sav file','*.sav')
        # print('-------------inputPath:',PATH_ORIGIN)
        # Assign value to grid
        myGridBus = self.gridSearch
        myGridFile = self.gridFile
        myGridArea = self.gridArea
        myGridZone = self.gridZone
        myGrid2Wind = self.grid2wind
        myGrid3Wind = self.grid3wind
        psspy.psseinit(50000)
        dirName = r"D:/"
        
        for i in range(len(PATHS)):
            self.Path = PATHS[i]
            fileName = os.path.basename(PATHS[i])
            
            # lần đầu tiên mở file này thì thông tin sẽ được thêm mới vào mảng
            if not PATHS[i] in PATHFILE_ORIGIN: 
                PATHFILE_ORIGIN.append(PATHS[i])
                PATH = os.path.join(dirName,fileName[0:-4] + "-{}".format(len(PATHFILE_ORIGIN))+".sav") 
                psspy.case(PATHS[i])
                PATHFILE.append(PATH)
                psspy.save(PATH)
                matrixArea.append(loadAreaInfo(PATH))
                matrixZone.append(loadZoneInfo(PATH))
                matrixBus.append(loadBusTab(PATH))
                matrixGen.append(loadMachineTab(PATH))
                matrixLoad.append(loadLoadTab(PATH))
                matrixShunt.append(loadShuntTab(PATH))
                matrix2Wind.append(load2windTab(PATH))
                matrix3Wind.append(load3windTab(PATH))
            # nếu mở lại file đã có trong tool thì thông số sẽ được cập nhật lại, index của file giữ k đổi
            else: 
                fileIndex = PATHFILE_ORIGIN.index(PATHS[i])
                PATH = PATHFILE[fileIndex]
                
                psspy.save(PATH)
                matrixArea[fileIndex] = loadAreaInfo(PATH)
                matrixZone[fileIndex] = loadZoneInfo(PATH)
                matrixBus[fileIndex] = loadBusTab(PATH)
                matrixGen[fileIndex] = loadMachineTab(PATH)
                matrixLoad[fileIndex] = loadLoadTab(PATH)
                matrixShunt[fileIndex] = loadShuntTab(PATH)
                matrix2Wind[fileIndex] = load2windTab(PATH)
                matrix3Wind[fileIndex] = load3windTab(PATH)

            fileIndex = PATHFILE.index(PATH)
            sourceLoad = loadSourceLoadInfo(PATH)
            [totalPgen,totalLoad, totalPgenNorth,totalLoadNorth,totalPgenCentral,totalLoadCentral,totalPgenSouth,totalLoadSouth,ratio] = sourceLoad

            # Table of files
            fileInfo = loadFileInfo(PATH)
            fileInfo1 = [fileInfo[0][0],fileInfo[1][0],fileInfo[2][0],fileInfo[3][0],fileInfo[4][0],fileInfo[5][0]]
            fileInfoArray = np.array(fileInfo1)
            fileInfoTranspose = fileInfoArray.transpose()
            if i == len(PATHS)-1:
                PATH_ORIGIN = PATHS[i]
                # Table of Zone and Area
                currentMatrixArea = matrixArea[fileIndex]
                currentMatrixZone = matrixZone[fileIndex]
                currentMatrixBus = matrixBus[fileIndex]
                currentMatrixGen = matrixGen[fileIndex]
                currentMatrixLoad = matrixLoad[fileIndex]
                currentMatrixShunt = matrixShunt[fileIndex]
                currentMatrix2Wind = matrix2Wind[fileIndex]
                currentMatrix3Wind = matrix3Wind[fileIndex]
                
                # global areaList,zoneList
                global areaList,zoneList
                areaList = currentMatrixArea[:,0]
                zoneList = currentMatrixZone[:,0]

                self.BusNumInput.SetItems(currentMatrixBus[:,0].tolist())

                if busNumber != 0:
                    self.BusNumInput.SetValue(str(busNumber))
                
                #reload all grid
                if(indexFile>0):
                    for row1 in range(myGridArea.GetNumberRows()):
                        for column1 in range(myGridArea.GetNumberCols()):
                            myGridArea.SetCellValue(row1,column1,"")
                    for row1 in range(myGridZone.GetNumberRows()):
                        for column1 in range(myGridZone.GetNumberCols()):
                            myGridZone.SetCellValue(row1,column1,"")
                    for row1 in range(myGridBus.GetNumberRows()):
                        for column1 in range(myGridBus.GetNumberCols()):
                            myGridBus.SetCellValue(row1,column1,"")
                    for row1 in range(self.m_grid6.GetNumberRows()):
                        for column1 in range(27):
                            self.m_grid6.SetCellValue(row1,column1,"")
                    for row1 in range(self.gridShunt.GetNumberRows()):
                        for column1 in range(self.gridShunt.GetNumberCols()):
                            self.gridShunt.SetCellValue(row1,column1,"")
                    for row1 in range(self.grid2wind.GetNumberRows()):
                        for column1 in range(self.grid2wind.GetNumberCols()):
                            self.grid2wind.SetCellValue(row1,column1,"")
                    for row1 in range(self.grid3wind.GetNumberRows()):
                        for column1 in range(self.grid3wind.GetNumberCols()):
                            self.grid3wind.SetCellValue(row1,column1,"")
                for row in range(len(fileInfoTranspose)):
                    for column in range(len(fileInfoTranspose[0])):
                        myGridFile.SetCellValue(row,column,str(fileInfoTranspose[row][column]))

                for row1 in range(len(currentMatrixArea)):
                    for column1 in range(len(currentMatrixArea[0])):
                        myGridArea.SetCellValue(row1,column1,str(currentMatrixArea[row1][column1]))

                for row2 in range(len(currentMatrixZone)):
                    for column2 in range(len(currentMatrixZone[0])):
                        myGridZone.SetCellValue(row2,column2,str(currentMatrixZone[row2][column2])) 

                for row3 in range(len(currentMatrixBus)):
                    for column3 in range(len(currentMatrixBus[0])):
                        myGridBus.SetCellValue(row3,column3,str(currentMatrixBus[row3][column3]))
                toGenNumList = []
                toGenNameList = []

                for row3 in range(len(currentMatrixGen)):
                    toGenNumList.append(str(currentMatrixGen[row3,0]))
                    toGenNameList.append(str(currentMatrixGen[row3,1]))
                    
                    for column3 in range(len(currentMatrixGen[0])):
                        self.m_grid6.SetCellValue(row3,column3,str(currentMatrixGen[row3][column3]))
                    coff = self.m_grid6.GetCellValue(row3,13)
                    self.m_grid6.SetCellValue(row3,26,str(float(coff)/100))

                toLoadNumList = []
                for row3 in range(len(currentMatrixLoad)):
                    toLoadNumList.append(str(currentMatrixLoad[row3,0]))
                    for column3 in range(len(currentMatrixLoad[0])):
                        self.gridLoad.SetCellValue(row3,column3,str(currentMatrixLoad[row3][column3]))
                toShuntNumList = []
                for row3 in range(len(currentMatrixShunt)):
                    toShuntNumList.append(str(currentMatrixShunt[row3,1]))
                    for column3 in range(len(currentMatrixShunt[0])):
                        self.gridShunt.SetCellValue(row3,column3,str(currentMatrixShunt[row3][column3]))

                to2WindNumList = []
                for row3 in range(len(currentMatrix2Wind)):
                    to2WindNumList.append(str(currentMatrix2Wind[row3,1]))
                    for column3 in range(len(currentMatrix2Wind[0])):
                        self.grid2wind.SetCellValue(row3,column3,str(currentMatrix2Wind[row3][column3]))

                to3WindNumList = []
                for row3 in range(len(currentMatrix3Wind)):
                    to3WindNumList.append(str(currentMatrix3Wind[row3,1]))
                    for column3 in range(len(currentMatrix3Wind[0])):
                        self.grid3wind.SetCellValue(row3,column3,str(currentMatrix3Wind[row3][column3]))

                self.genNumber.SetItems(toGenNumList)
                self.genName.SetItems(toGenNameList)
                self.loadNumber.SetItems(toLoadNumList)
                self.shuntNumber.SetItems(toLoadNumList)
                self.search_dyn.SetItems(toGenNumList)

                self.PathFile = PATHFILE
                self.matrixBus = matrixBus  

                self.totalSource.SetValue(str(Decimal(totalPgen).quantize(TWOPLACE)))
                self.totalLoad.SetValue(str(Decimal(totalLoad).quantize(TWOPLACE)))
                self.sourceNorth.SetValue(str(Decimal(totalPgenNorth).quantize(TWOPLACE)))
                self.loadNorth.SetValue(str(Decimal(totalLoadNorth).quantize(TWOPLACE)))
                self.sourceCentral.SetValue(str(Decimal(totalPgenCentral).quantize(TWOPLACE)))
                self.loadCentral.SetValue(str(Decimal(totalLoadCentral).quantize(TWOPLACE)))
                self.sourceSouth.SetValue(str(Decimal(totalPgenSouth).quantize(TWOPLACE)))
                self.loadSouth.SetValue(str(Decimal(totalLoadSouth).quantize(TWOPLACE)))
                for i in range(len(ratio)):
                    self.m_grid6.SetCellValue(i,29, str((Decimal(ratio[i]).quantize(TWOPLACE))))

        event.Skip()

    # chức năng thực hiện tại ô được chọn của bảng thông tin file
    def on_selected_cell_grid_file( self, event ):
        self.priority = ""
        global indexFile ,PATH,PATH_ORIGIN
        row = event.GetRow()
        col = event.GetCol()

        cellValue = myGridFile.GetCellValue(row,col)
        if(cellValue !=""):
            indexFile = row # - 1
            PATH = PATHFILE[indexFile]
            PATH_ORIGIN = PATHFILE_ORIGIN[indexFile]
            psspy.case(PATH) 
            selectedMatrixArea = matrixArea[indexFile]
            selectedMatrixZone = matrixZone[indexFile]
            selectedMatrixBus = matrixBus[indexFile]
            selectedMatrixSource = matrixGen[indexFile]
            selectedMatrixLoad = matrixLoad[indexFile]
            selectedMatrixShunt = matrixShunt[indexFile]
            selectedMatrix2Wind = matrix2Wind[indexFile]
            selectedMatrix3Wind = matrix3Wind[indexFile]

            #reload all grid
            if(indexFile>=0): 
                self.BusNumInput.SetItems(selectedMatrixBus[:,0].tolist())
                if busNumber != '' and busNumber != 0:
                    self.BusNumInput.SetValue(busNumber)
                for row1 in range(myGridArea.GetNumberRows()):
                    for column1 in range(myGridArea.GetNumberCols()):
                        myGridArea.SetCellValue(row1,column1,"")
                for row1 in range(myGridZone.GetNumberRows()):
                    for column1 in range(myGridZone.GetNumberCols()):
                        myGridZone.SetCellValue(row1,column1,"")
                for row1 in range(myGridBus.GetNumberRows()):
                    for column1 in range(myGridBus.GetNumberCols()):
                        myGridBus.SetCellValue(row1,column1,"")
                for row1 in range(self.m_grid6.GetNumberRows()):
                    for column1 in range(27):
                        self.m_grid6.SetCellValue(row1,column1,"")
                for row1 in range(self.gridLoad.GetNumberRows()):
                    for column1 in range(self.gridLoad.GetNumberCols()):
                        self.gridLoad.SetCellValue(row1,column1,"")
                for row1 in range(self.gridShunt.GetNumberRows()):
                    for column1 in range(self.gridShunt.GetNumberCols()):
                        self.gridShunt.SetCellValue(row1,column1,"")
                for row1 in range(self.grid2wind.GetNumberRows()):
                    for column1 in range(self.grid2wind.GetNumberCols()):
                        self.grid2wind.SetCellValue(row1,column1,"")
                for row1 in range(self.grid3wind.GetNumberRows()):
                    for column1 in range(self.grid3wind.GetNumberCols()):
                        self.grid3wind.SetCellValue(row1,column1,"")

            for row1 in range(len(selectedMatrixArea)):
                for column1 in range(len(selectedMatrixArea[0])):
                    myGridArea.SetCellValue(row1,column1,str(selectedMatrixArea[row1][column1]))

            for row1 in range(len(selectedMatrixZone)):
                for column1 in range(len(selectedMatrixZone[0])):
                    myGridZone.SetCellValue(row1,column1,str(selectedMatrixZone[row1][column1])) 
            
            for row1 in range(len(selectedMatrixBus)):
                for column1 in range(len(selectedMatrixBus[0])):
                    myGridBus.SetCellValue(row1,column1,str(selectedMatrixBus[row1][column1]))
            
            toGenNumList = []
            toGenNameList = []
            for row1 in range(len(selectedMatrixSource)):
                toGenNumList.append(str(selectedMatrixSource[row1][0]))
                toGenNameList.append(str(selectedMatrixSource[row1][1]))
                for column1 in range(len(selectedMatrixSource[0])):
                    self.m_grid6.SetCellValue(row1,column1,str(selectedMatrixSource[row1][column1]))
                coff = self.m_grid6.GetCellValue(row1,13)
                self.m_grid6.SetCellValue(row1,26,str(float(coff)/100))

            toLoadNumList = []
            for row1 in range(len(selectedMatrixLoad)):
                toLoadNumList.append(str(selectedMatrixLoad[row1][0]))
                for column1 in range(len(selectedMatrixLoad[0])):
                    self.gridLoad.SetCellValue(row1,column1,str(selectedMatrixLoad[row1][column1]))

            toShuntNumList = []
            for row1 in range(len(selectedMatrixShunt)):
                toShuntNumList.append(str(selectedMatrixShunt[row1][1]))
                for column1 in range(len(selectedMatrixShunt[0])):
                    self.gridShunt.SetCellValue(row1,column1,str(selectedMatrixShunt[row1][column1]))
            
            to2WindNumList = []
            for row1 in range(len(selectedMatrix2Wind)):
                to2WindNumList.append(str(selectedMatrix2Wind[row1][1]))
                for column1 in range(len(selectedMatrix2Wind[0])):
                    self.grid2wind.SetCellValue(row1,column1,str(selectedMatrix2Wind[row1][column1]))

            to3WindNumList = []
            for row1 in range(len(selectedMatrix3Wind)):
                to3WindNumList.append(str(selectedMatrix3Wind[row1][1]))
                for column1 in range(len(selectedMatrix3Wind[0])):
                    self.grid3wind.SetCellValue(row1,column1,str(selectedMatrix3Wind[row1][column1]))

            sourceLoad = loadSourceLoadInfo(PATH)
            [totalPgen,totalLoad, totalPgenNorth,totalLoadNorth,totalPgenCentral,totalLoadCentral,totalPgenSouth,totalLoadSouth,ratio] = sourceLoad
            for i in range(len(ratio)):
                self.m_grid6.SetCellValue(i,29, str((Decimal(ratio[i]).quantize(TWOPLACE))))

            # cập nhật lại số liệu nguồn tải cho toàn quốc và miền bắc, trung, nam (miền phân theo zone), làm trong 2 chữ số thập phân
            self.totalSource.SetValue(str(Decimal(totalPgen).quantize(TWOPLACE)))
            self.totalLoad.SetValue(str(Decimal(totalLoad).quantize(TWOPLACE)))
            self.sourceNorth.SetValue(str(Decimal(totalPgenNorth).quantize(TWOPLACE)))
            self.loadNorth.SetValue(str(Decimal(totalLoadNorth).quantize(TWOPLACE)))
            self.sourceCentral.SetValue(str(Decimal(totalPgenCentral).quantize(TWOPLACE)))
            self.loadCentral.SetValue(str(Decimal(totalLoadCentral).quantize(TWOPLACE)))
            self.sourceSouth.SetValue(str(Decimal(totalPgenSouth).quantize(TWOPLACE)))
            self.loadSouth.SetValue(str(Decimal(totalLoadSouth).quantize(TWOPLACE)))

            self.genNumber.SetItems(toGenNumList)
            self.genName.SetItems(toGenNameList)
            self.loadNumber.SetItems(toLoadNumList)
            self.shuntNumber.SetItems(toShuntNumList)
            self.busNumberEnter_Fcn(event)
        else:
            event.Skip()

    # chức năng thực hiện tại ô được chọn của bảng area
    def on_selected_cell_grid_area( self, event ):
        self.priority = "AREA"
        if self.onUpdate != 1:
            self.rowArea = event.GetRow()
            self.colArea = event.GetCol()
        cellValue = myGridArea.GetCellValue(self.rowArea,self.colArea)
        colLabel = myGridArea.GetColLabelValue(self.colArea)
        self.gridAreaLink.myGridArea  = myGridArea
        self.gridAreaLink.matrixArea = matrixArea
        self.gridAreaLink.myGridZone = myGridZone
        self.gridAreaLink.matrixZone = matrixZone
        self.gridAreaLink.myGridLoad = self.gridLoad
        self.gridAreaLink.matrixLoad = matrixLoad
        self.gridAreaLink.myGridSource = self.m_grid6
        self.gridAreaLink.matrixSource = matrixGen
        self.gridAreaLink.indexFile = indexFile
        self.gridAreaLink.Path = PATH
        self.gridAreaLink.PathFile = PATHFILE
        self.gridAreaLink.selectedZoneRow = selectedZoneRow
        self.gridAreaLink.selectedZoneNum = selectedZoneNum

        # khi chọn một ô bất kỳ trong bảng area, tất cả thông tin ở bảng bus, nguồn, tải, kháng tụ, MBA 2, 3 CD được lọc theo area tương ứng
        if (cellValue !=""):
            selectedAreaNum = myGridArea.GetCellValue(self.rowArea,0)
            selectedMatrixZone = select_zone_from_area(selectedAreaNum,matrixBus[indexFile],matrixZone[indexFile])
            selectedMatrixBus = select_bus_from_area(selectedAreaNum,matrixBus[indexFile])
            selectedMatrix2Wind = select_2Wind_from_area(selectedAreaNum,matrixBus[indexFile],matrix2Wind[indexFile])
            selectedMatrix3Wind = select_3Wind_from_area(selectedAreaNum,matrixBus[indexFile],matrix3Wind[indexFile])
            selectedMatrixSource = select_source_from_area(selectedAreaNum,matrixGen[indexFile])
            [PLoad,QLoad,CosPhi,selectedMatrixLoad] = select_load_from_area(self.rowArea,selectedAreaNum,matrixLoad[indexFile],myGridArea)
            selectedMatrixShunt = select_shunt_from_area(selectedAreaNum,matrixShunt[indexFile])

            for i in range(myGridZone.GetNumberRows()):
                for j in range(myGridZone.GetNumberCols()):
                    myGridZone.SetCellValue(i,j,'0')

            clear_grid(myGridBus)

            for i in range(self.grid2wind.GetNumberRows()):
                for j in range(self.grid2wind.GetNumberCols()):
                    self.grid2wind.SetCellValue(i,j,'')

            for i in range(self.grid3wind.GetNumberRows()):
                for j in range(self.grid3wind.GetNumberCols()):
                    self.grid3wind.SetCellValue(i,j,'')

            for i in range(self.m_grid6.GetNumberRows()):
                for j in range(25):
                    self.m_grid6.SetCellValue(i,j,'')
                
            for i in range(self.gridLoad.GetNumberRows()):
                for j in range(self.gridLoad.GetNumberCols()):
                    self.gridLoad.SetCellValue(i,j,'')

            for i in range(self.gridShunt.GetNumberRows()):
                for j in range(self.gridShunt.GetNumberCols()):
                    self.gridShunt.SetCellValue(i,j,'')

            for row1 in range(len(selectedMatrixZone)):
                for column1 in range(len(selectedMatrixZone[0])):
                    myGridZone.SetCellValue(row1,column1,str(selectedMatrixZone[row1][column1])) 

            for row1 in range(len(selectedMatrixBus)):
                for column1 in range(len(selectedMatrixBus[0])):
                    myGridBus.SetCellValue(row1,column1,str(selectedMatrixBus[row1][column1])) 

            for row1 in range(len(selectedMatrixSource)):
                for column1 in range(len(selectedMatrixSource[0])):
                    self.m_grid6.SetCellValue(row1,column1,str(selectedMatrixSource[row1][column1]))
                coff = self.m_grid6.GetCellValue(row1,13)
                self.m_grid6.SetCellValue(row1,26,str(float(coff)/100))

            for row1 in range(len(selectedMatrix2Wind)):
                for column1 in range(len(selectedMatrix2Wind[0])):
                    self.grid2wind.SetCellValue(row1,column1,str(selectedMatrix2Wind[row1][column1]))

            for row1 in range(len(selectedMatrix3Wind)):
                for column1 in range(len(selectedMatrix3Wind[0])):
                    self.grid3wind.SetCellValue(row1,column1,str(selectedMatrix3Wind[row1][column1]))

            self.P_value.SetValue(str(PLoad))
            self.Q_Value.SetValue(str(QLoad))
            self.Cos_Phi_Value.SetValue(str(CosPhi))
            for row1 in range(len(selectedMatrixLoad)):
                for column1 in range(len(selectedMatrixLoad[0])):
                    self.gridLoad.SetCellValue(row1,column1,str(selectedMatrixLoad[row1][column1]))

            for row1 in range(len(selectedMatrixShunt)):
                for column1 in range(len(selectedMatrixShunt[0])):
                    self.gridShunt.SetCellValue(row1,column1,str(selectedMatrixShunt[row1][column1]))

        else:
            event.Skip()

        self.gridAreaLink.on_selected_cell_grid_area(event)

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng area
    def on_cell_change_grid_area( self, event ):
        self.gridAreaLink.myGridArea  = myGridArea
        self.gridAreaLink.matrixArea = matrixArea
        self.gridAreaLink.myGridZone = myGridZone
        self.gridAreaLink.matrixZone = matrixZone
        self.gridAreaLink.myGridLoad = self.gridLoad
        self.gridAreaLink.matrixLoad = matrixLoad
        self.gridAreaLink.myGridSource = self.m_grid6
        self.gridAreaLink.matrixSource = matrixGen
        self.gridAreaLink.indexFile = indexFile
        self.gridAreaLink.Path = PATH
        self.gridAreaLink.PathFile = PATHFILE
        self.gridAreaLink.selectedZoneRow = selectedZoneRow
        self.gridAreaLink.selectedZoneNum = selectedZoneNum
        self.gridAreaLink.on_cell_change_grid_area(event)

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng area
    def on_cell_right_click_grid_area( self, event ):
        self.gridAreaLink.myGridArea = myGridArea
        self.gridAreaLink.matrixArea = matrixArea
        self.gridAreaLink.myGridZone = myGridZone
        self.gridAreaLink.matrixZone = matrixZone
        self.gridAreaLink.myGridLoad = self.gridLoad
        self.gridAreaLink.matrixLoad = matrixLoad
        self.gridAreaLink.indexFile = indexFile
        self.gridAreaLink.myGridSource = self.m_grid6
        self.gridAreaLink.matrixSource = matrixGen
        self.gridAreaLink.Path = PATH
        self.gridAreaLink.PathFile = PATHFILE
        self.gridAreaLink.on_cell_right_click_grid_area(event)

    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại bảng area
    def on_key_down_grid_area(self,event):
        self.gridAreaLink.myGridArea = myGridArea
        self.gridAreaLink.matrixArea = matrixArea
        self.gridAreaLink.myGridZone = myGridZone
        self.gridAreaLink.matrixZone = matrixZone
        self.gridAreaLink.indexFile = indexFile
        self.gridAreaLink.uk = event.UnicodeKey
        self.gridAreaLink.Path = PATH
        self.gridAreaLink.PathFile = PATHFILE
        self.gridAreaLink.on_key_down_grid_area(event)
        event.Skip()

    # chức năng thay đổi nguồn của area (scale area source)
    def Change_Area_Source_Fcn( self, event ):
        self.gridAreaLink.myGridArea  = myGridArea
        self.gridAreaLink.matrixArea = matrixArea
        self.gridAreaLink.myGridZone = myGridZone
        self.gridAreaLink.matrixZone = matrixZone
        self.gridAreaLink.indexFile = indexFile
        self.gridAreaLink.PathFile = PATHFILE
        self.gridAreaLink.Path = PATH
        self.gridAreaLink.Change_Area_Source_Fcn(event)

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng zone
    def on_cell_change_grid_zone( self, event ):
        self.gridZoneLink.myGridZone = myGridZone
        self.gridZoneLink.matrixZone = matrixZone
        self.gridZoneLink.myGridLoad = self.gridLoad
        self.gridZoneLink.matrixLoad = matrixLoad
        self.gridZoneLink.myGridSource = self.m_grid6
        self.gridZoneLink.matrixSource = matrixGen
        self.gridZoneLink.myGridShunt = self.gridShunt
        self.gridZoneLink.matrixShunt = matrixShunt
        self.gridZoneLink.selectedZoneRow = selectedZoneRow
        self.gridZoneLink.selectedZoneNum = selectedZoneNum
        self.gridZoneLink.PathFile = PATHFILE
        self.gridZoneLink.Path = PATH
        self.gridZoneLink.indexFile = indexFile
        self.gridZoneLink.on_cell_change_grid_zone(event)

    # chức năng thực hiện tại ô được chọn của bảng zone
    def on_selected_cell_grid_zone( self, event ):
        self.priority = 'ZONE'
        global selectedZoneNum, selectedZoneRow
        if self.onUpdate != 1:
            self.rowZone = event.GetRow()
            self.colZone = event.GetCol()

        cellValue = myGridZone.GetCellValue(self.rowZone,self.colZone)
        colLabel = myGridZone.GetColLabelValue(self.colZone)

        selectedZoneRow = self.rowZone

        # khi chọn một ô bất kỳ trong bảng zone, tất cả thông tin ở bảng bus, nguồn, tải, MBA 2, 3 CD được lọc theo zone tương ứng
        if (cellValue !=""):
            selectedZoneNum = myGridZone.GetCellValue(self.rowZone,0)
            selectedMatrixBus = select_bus_from_zone(selectedZoneNum,matrixBus[indexFile])
            selectedMatrixSource = select_source_from_zone(selectedZoneNum,matrixGen[indexFile])
            selectedMatrix2Wind = select_2Wind_from_zone(selectedZoneNum,matrixBus[indexFile],matrix2Wind[indexFile])
            selectedMatrix3Wind = select_3Wind_from_zone(selectedZoneNum,matrixBus[indexFile],matrix3Wind[indexFile])
            [PLoad,QLoad,CosPhi,selectedMatrixLoad] = select_load_from_zone(self.rowZone,selectedZoneNum,matrixLoad[indexFile],myGridZone)
            selectedMatrixShunt = select_shunt_from_zone(selectedZoneNum,matrixShunt[indexFile])

            clear_grid(myGridBus)

            for i in range(self.m_grid6.GetNumberRows()):
                for j in range(25):
                    self.m_grid6.SetCellValue(i,j,'')
                
            for i in range(self.gridLoad.GetNumberRows()):
                for j in range(self.gridLoad.GetNumberCols()):
                    self.gridLoad.SetCellValue(i,j,'')

            for i in range(self.grid2wind.GetNumberRows()):
                for j in range(self.grid2wind.GetNumberCols()):
                    self.grid2wind.SetCellValue(i,j,'')

            for i in range(self.grid3wind.GetNumberRows()):
                for j in range(self.grid3wind.GetNumberCols()):
                    self.grid3wind.SetCellValue(i,j,'')

            for i in range(self.gridShunt.GetNumberRows()):
                for j in range(self.gridShunt.GetNumberCols()):
                    self.gridShunt.SetCellValue(i,j,'')

            for row1 in range(len(selectedMatrixBus)):
                for column1 in range(len(selectedMatrixBus[0])):
                    myGridBus.SetCellValue(row1,column1,str(selectedMatrixBus[row1][column1])) 

            for row1 in range(len(selectedMatrixSource)):
                for column1 in range(len(selectedMatrixSource[0])):
                    self.m_grid6.SetCellValue(row1,column1,str(selectedMatrixSource[row1][column1]))
                coff = self.m_grid6.GetCellValue(row1,13)
                self.m_grid6.SetCellValue(row1,26,str(float(coff)/100))

            self.P_value.SetValue(str(PLoad))
            self.Q_Value.SetValue(str(QLoad))
            self.Cos_Phi_Value.SetValue(str(CosPhi))
            for row1 in range(len(selectedMatrixLoad)):
                for column1 in range(len(selectedMatrixLoad[0])):
                    self.gridLoad.SetCellValue(row1,column1,str(selectedMatrixLoad[row1][column1]))

            for row1 in range(len(selectedMatrixShunt)):
                for column1 in range(len(selectedMatrixShunt[0])):
                    self.gridShunt.SetCellValue(row1,column1,str(selectedMatrixShunt[row1][column1]))

            for row1 in range(len(selectedMatrix2Wind)):
                for column1 in range(len(selectedMatrix2Wind[0])):
                    self.grid2wind.SetCellValue(row1,column1,str(selectedMatrix2Wind[row1][column1]))

            for row1 in range(len(selectedMatrix3Wind)):
                for column1 in range(len(selectedMatrix3Wind[0])):
                    self.grid3wind.SetCellValue(row1,column1,str(selectedMatrix3Wind[row1][column1]))

            self.gridZoneLink.myGridZone = myGridZone
            self.gridZoneLink.matrixZone = matrixZone
            self.gridZoneLink.myGridLoad = self.gridLoad
            self.gridZoneLink.matrixLoad = matrixLoad
            self.gridZoneLink.myGridSource = self.m_grid6
            self.gridZoneLink.matrixSource = matrixGen
            self.gridZoneLink.myGridShunt = self.gridShunt
            self.gridZoneLink.matrixShunt = matrixShunt
            self.gridZoneLink.selectedZoneRow = selectedZoneRow
            self.gridZoneLink.selectedZoneNum = selectedZoneNum
            self.gridZoneLink.indexFile = indexFile
            self.gridZoneLink.PathFile = PATHFILE
            self.gridZoneLink.Path = PATH
            self.gridZoneLink.on_selected_cell_grid_zone(event)
            event.Skip()
        else:
            event.Skip()

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng zone
    def on_cell_right_click_grid_zone( self, event ):
        self.gridZoneLink.myGridZone = myGridZone
        self.gridZoneLink.matrixZone = matrixZone
        self.gridZoneLink.myGridArea = myGridArea
        self.gridZoneLink.matrixArea = matrixArea
        self.gridZoneLink.myGridLoad = self.gridLoad
        self.gridZoneLink.matrixLoad = matrixLoad
        self.gridZoneLink.myGridSource = self.m_grid6
        self.gridZoneLink.matrixSource = matrixGen
        self.gridZoneLink.myGridShunt = self.gridShunt
        self.gridZoneLink.matrixShunt = matrixShunt
        self.gridZoneLink.selectedZoneRow = selectedZoneRow
        self.gridZoneLink.selectedZoneNum = selectedZoneNum
        self.gridZoneLink.indexFile = indexFile
        self.gridZoneLink.PathFile = PATHFILE
        self.gridZoneLink.Path = PATH
        self.gridZoneLink.on_cell_right_click_grid_zone(event)

    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại bảng zone
    def on_key_down_grid_zone(self,event):
        self.gridZoneLink.myGridZone = myGridZone
        self.gridZoneLink.matrixZone = matrixZone
        self.gridZoneLink.myGridArea = myGridArea
        self.gridZoneLink.matrixArea = matrixArea
        self.gridZoneLink.indexFile = indexFile
        self.gridZoneLink.PathFile = PATHFILE
        self.gridZoneLink.Path = PATH
        self.gridZoneLink.uk = event.UnicodeKey
        self.gridZoneLink.on_key_down_grid_zone(event)
        event.Skip()

    # chức năng thay đổi nguồn của zone (scale zone source)
    def Change_Zone_Source_Fcn( self, event ):
        self.gridZoneLink.myGridZone = myGridZone
        self.gridZoneLink.matrixZone = matrixZone
        self.gridZoneLink.myGridArea = myGridArea
        self.gridZoneLink.matrixArea = matrixArea
        self.gridZoneLink.indexFile = indexFile
        self.gridZoneLink.PathFile = PATHFILE
        self.gridZoneLink.Path = PATH
        self.gridZoneLink.Change_Zone_Source_Fcn(event)

    # chức năng thay đổi tải của zone (scale zone load)
    def Change_Zone_Load_Fcn( self, event ):
        self.gridZoneLink.myGridZone = myGridZone
        self.gridZoneLink.matrixZone = matrixZone
        self.gridZoneLink.myGridArea = myGridArea
        self.gridZoneLink.matrixArea = matrixArea
        self.gridZoneLink.indexFile = indexFile
        self.gridZoneLink.PathFile = PATHFILE
        self.gridZoneLink.Path = PATH
        self.gridZoneLink.Change_Zone_Load_Fcn(event)

    # Chức năng hiển thị thông tin đường dây, MBA 2 CD, 3 CD nối tới bus được chọn
    @debounced_search('bus_number', 'BusNumInput', delay_ms=200)
    @profiled('search.bus_connections')
    @batched_grid_update('gridBusInfo')
    def busNumberEnter_Fcn( self, event ):
        global busNumber,previousBusNumber,matrixBranch
        busNumber = self.BusNumInput.GetValue()
        
        if busNumber in matrixBus[indexFile][:,0] :
            busInfo = select_bus_from_matrixBus(int(busNumber),matrixBus[indexFile])

            self.BusNameInput.Label = busInfo[1]
            self.CodeInput.Label = busInfo[7]
            self.UdmInput.Label = busInfo[2]
            if int(busInfo[8]) != 4:
                self.VoltageInput.Label = str(float(busInfo[9])*float(busInfo[2]))
            else:
                self.VoltageInput.Label = str(0)
            self.AreaInput.Label = busInfo[3]
            self.AreaNameInput.Label = busInfo[4]
            self.ZoneInput.Label = busInfo[5]
            self.ZoneNameInput.Label = busInfo[6]
            self.CosPInput.Label = busInfo[11]

            self.gridBusInfoLink.matrixBus = matrixBus
            self.gridBusInfoLink.myGridBus = myGridBus
            self.gridBusInfoLink.myGridZone = myGridZone
            self.gridBusInfoLink.matrixZone = matrixZone
            self.gridBusInfoLink.myGridArea = myGridArea
            self.gridBusInfoLink.matrixArea = matrixArea
            self.gridBusInfoLink.myGridFile = myGridFile
            self.gridBusInfoLink.fileInfoTranspose = fileInfoTranspose
            self.gridBusInfoLink.indexFile = indexFile
            self.gridBusInfoLink.uk = ukNumBus
            self.gridBusInfoLink.Path = PATH
            self.gridBusInfoLink.PathFile = PATHFILE
            self.gridBusInfoLink.location = self.LOCATION
            # trả về mảng chứa thông tin branch, 2 wind, 3 wind ứng với mã bus được chọn
            matrixBranch,matrix2WindBr,matrix3WindBr = self.gridBusInfoLink.loadBusNumberEnter(int(busNumber))

            global previousBusNumber

            # chọn tất cả các kiểu đường dây có thể theo cấp điện áp
            [lineType] = self.gridBusInfoLink.SelectAllLineTypeByBusVoltage(busNumber)

            celChoiceLines =wx.grid.GridCellChoiceEditor(lineType.tolist(),allowOthers=True)

            if int(busNumber)!=previousBusNumber:
                psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(busNumber)],0,[],0,[])
                ierr, busBaseKVOrigin = psspy.abusreal(0,2,'BASE')
                clear_grid(self.gridBusInfo)
                            
                for row1 in range(len(matrixBranch)):

                    celChoiceLines.IncRef()
                    self.gridBusInfo.SetCellEditor(row1,1,celChoiceLines)
                    for col1 in range(len(matrixBranch[0])):
                        self.gridBusInfo.SetCellValue(row1,col1,str(matrixBranch[row1][col1]))
                        self.gridBusInfo.SetCellTextColour(row1,col1,wx.Colour(0,0,0))
                busNumList = []
                for row in range (len(matrix3WindBr)):
                    branchRowNum = len(matrixBranch)
                    psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(matrix3WindBr[row][2])],0,[],0,[])
                    ierr, busBaseKV = psspy.abusreal(0,2,'BASE')
                    if row % 2 ==0 and float(busBaseKV[0][0])>float(busBaseKVOrigin[0][0]):
                        busNumList.append(matrix3WindBr[row][2])
                        busNumList.append(matrix3WindBr[row][2])
                    elif row % 2 ==0 and float(busBaseKV[0][0])<float(busBaseKVOrigin[0][0]):
                        busNumList.append(busNumber)
                        busNumList.append(busNumber)

                    for col in range(len(matrix3WindBr[0])):
                        self.gridBusInfo.SetCellValue(row+branchRowNum,col,str(matrix3WindBr[row][col]))
                        self.gridBusInfo.SetCellTextColour(row+branchRowNum,col,wx.Colour(0,0,0))

                celChoiceTrans =wx.grid.GridCellChoiceEditor([],allowOthers=True)
                for index,busNum in enumerate(busNumList):
                    TransType = self.gridBusInfoLink.SelectAllTransTypeByBusVoltage(busNum)[0]
                    celChoiceTrans.IncRef()
                    celChoiceTrans.Destroy()
                    celChoiceTrans = wx.grid.GridCellChoiceEditor(TransType.tolist(),allowOthers=True)
                    self.gridBusInfo.SetCellEditor(index+len(matrixBranch),1,celChoiceTrans)

                [trans2Type,R,X,Rate,R01,X01] = self.gridBusInfoLink.SelectAllTrans2WindType()
                celChoiceTrans2 =wx.grid.GridCellChoiceEditor(trans2Type.tolist(),allowOthers=True)

                for row in range (len(matrix2WindBr)):
                    CurrentRowNum = len(matrixBranch)+len(matrix3WindBr)
                    for col in range(len(matrix2WindBr[0])):
                        celChoiceTrans2.IncRef()
                        self.gridBusInfo.SetCellEditor(row+CurrentRowNum,1,celChoiceTrans2)
                        self.gridBusInfo.SetCellValue(row+CurrentRowNum,col,str(matrix2WindBr[row][col]))
                        self.gridBusInfo.SetCellTextColour(row+CurrentRowNum,col,wx.Colour(0,0,0))

                for row2 in range(len(matrixBranch)+len(matrix2WindBr)+len(matrix3WindBr)):
                    if  self.gridBusInfo.GetCellValue(row2,8) != 'N/A' and float(self.gridBusInfo.GetCellValue(row2,8))>=100:
                        self.gridBusInfo.SetCellTextColour(row2,8, wx.RED)

            previousBusNumber = busNumber

        else:
            event.Skip()

    # chức năng tìm kiếm theo bus ID, bus Name, base kV, area name, area num, zone name, zone num,  code
    @debounced_search('grid_filter', 'filter_input_text',
                      priority='FILTER_INPUT_TEXT', delay_ms=200)
    @profiled('search.grid_filter')
    @batched_grid_update('gridSearch')
    def OnTextSearch( self, event ):
        self.priority = 'FILTER_INPUT_TEXT'
        choiceValue = self.filter_selection.GetSelection()
        searchText = self.filter_input_text.GetValue()
        name  = [[]]
        areaName = [[]]
        zoneName = [[]]
        for i in range(len(matrixBus[0])):
            name[0].append(matrixBus[0][i,1])
            areaName[0].append(matrixBus[0][i,4])
            zoneName[0].append(matrixBus[0][i,6])

        if choiceValue == 0 : # tìm kiếm theo Bus ID
            result = []
            for i in range(len(matrixBus[indexFile])):
                if ((str(searchText)).upper() in (matrixBus[indexFile][i,0])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))
        
        elif choiceValue == 1: # tìm kiếm theo bus Name
            result = []   
            for i in range(len(matrixBus[indexFile])):
                if ((str(searchText)).upper() in (matrixBus[indexFile][i,1])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))

        elif choiceValue == 2 and searchText in matrixBus[indexFile][:,2]: # tìm theo cấp điện áp
            result = []
            for i in range(len(matrixBus[indexFile])):
                if (searchText in str(matrixBus[indexFile][i,2])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))

        elif choiceValue == 3 and searchText in matrixBus[indexFile][:,3]: # tìm theo Area Number
            result = []
            for i in range(len(matrixBus[indexFile])):
                if (searchText in (matrixBus[indexFile][i][3])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))

        elif choiceValue == 4: # tìm theo Area Name
            result = []   
            for i in range(len(matrixBus[indexFile])):
                if ((str(searchText)).upper() in (matrixBus[indexFile][i,4])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))

        elif choiceValue == 5 and searchText in matrixBus[indexFile][:,5]: # tìm theo Zone Number
            result = []
            for i in range(len(matrixBus[indexFile])):
                if (searchText in (matrixBus[indexFile][i][5])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))

        elif choiceValue == 6 : # tìm theo zone Name
            result = []   
            for i in range(len(matrixBus[indexFile])):
                if ((str(searchText)).upper() in (matrixBus[indexFile][i,6])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))

        elif choiceValue == 7 and searchText in matrixBus[indexFile][:,8]: #tìm theo code
            result = []
            for i in range(len(matrixBus[indexFile])):
                if (searchText in (matrixBus[indexFile][i][8])):
                    result.append(matrixBus[indexFile][i][:])

            clear_grid(myGridBus)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    myGridBus.SetCellValue(i,j,str(result[i][j]))
        else:
            event.Skip()

        
    # chức năng lưu file đang làm việc
    def Save_PSSE( self, event ):
        if PATH != '':
            psspy.save(PATHFILE_ORIGIN[PATHFILE.index(PATH)])
            wx.MessageBox("Case saved in file {}".format(PATHFILE_ORIGIN[PATHFILE.index(PATH)]))
        else:
            wx.MessageBox("Please open an existing case first!")
    
    # chức năng lưu lần lượt tất cả các file trong tool
    def Save_All_PSSE( self, event ):
        if PATHFILE != '':
            for i in range(len(PATHFILE)):
                psspy.case(PATHFILE[i])
                psspy.save(PATHFILE_ORIGIN[i])
                wx.MessageBox("Case saved in file {}".format(PATHFILE_ORIGIN[i]))
        else:
            wx.MessageBox("Please open an existing case first!")

    # chức năng lưu file thành file khác
    def Save_As_Fcn(self, event):
        if PATH != '':
            fileIndex = PATHFILE_ORIGIN.index(PATH_ORIGIN)
            dDir = os.path.dirname(PATH_ORIGIN)
            dFile = os.path.basename(PATH_ORIGIN)
        else:
            dDir = os.getcwd() 
            dFile = u""
        wildcard = "PSS/E files (*.sav)|*.sav|All files|*"
        saveAsPath = saveFile(self,"Filename",wildcard,dDir,dFile )
        psspy.save(saveAsPath)

    # option = 1, export PQ in cad
    def Export_Cad( self, event ):
        if PATH_ORIGIN != '':
            dDir = os.path.dirname(PATH_ORIGIN)
            dFile = os.path.basename(PATH_ORIGIN)
            inputPath = openFile(self,'Please select input .dxf file','*.dxf')
            outFilePath = saveFile(self, "Output file name:","PSS/E files (*.dxf)|*.dxf|All files|*",dDir,dFile[0:-4]+'.dxf' )
            inputName = os.path.basename(inputPath)
            inpDir = os.path.dirname(inputPath)
            outputName = os.path.basename(outFilePath)
            outpDir = os.path.dirname(outFilePath)
            acad(inputName[0:-4],inpDir,outputName[0:-4],outpDir,1,1)
        else:
            wx.MessageBox("Please open an existing case first!")

    # option = 2, export MVA in cad
    def Export_Cad_MVA( self, event ): 
        if PATH_ORIGIN != '':
            dDir = os.path.dirname(PATH_ORIGIN)
            dFile = os.path.basename(PATH_ORIGIN)
            inputPath = openFile(self,'Please select input .dxf file','*.dxf')
            outFilePath = saveFile(self, "Output file name:","PSS/E files (*.dxf)|*.dxf|All files|*",dDir,dFile[0:-4]+'.dxf' )
            inputName = os.path.basename(inputPath)
            inpDir = os.path.dirname(inputPath)
            outputName = os.path.basename(outFilePath)
            outpDir = os.path.dirname(outFilePath)
            acad(inputName[0:-4],inpDir,outputName[0:-4],outpDir,1,2)
        else:
            wx.MessageBox("Please open an existing case first!")

    # option = 3, export Load(%) in cad
    def Export_Cad_Load_Percent( self, event ): 
        if PATH_ORIGIN != '':
            dDir = os.path.dirname(PATH_ORIGIN)
            dFile = os.path.basename(PATH_ORIGIN)
            inputPath = openFile(self,'Please select input .dxf file','*.dxf')
            outFilePath = saveFile(self, "Output file name:","PSS/E files (*.dxf)|*.dxf|All files|*",dDir,dFile[0:-4]+'.dxf' )
            inputName = os.path.basename(inputPath)
            inpDir = os.path.dirname(inputPath)
            outputName = os.path.basename(outFilePath)
            outpDir = os.path.dirname(outFilePath)
            acad(inputName[0:-4],inpDir,outputName[0:-4],outpDir,1,3)
        else:
            wx.MessageBox("Please open an existing case first!")

    # xuất cad cho tất cả file trong thư mục
    def Export_Multi_Cad( self, event ):

        inputPath = openFile(self,'Please select input .dxf file','*.dxf')
        dirNameSav = openFolder(self,"Choose the folder contain all sav files." )
        os.chdir(dirNameSav)
        savfileNames = glob.glob('*.sav')
        for savFile in savfileNames:
            cadFileName = savFile[0:-4]+'.dxf'
            outFilePath = os.path.join(dirNameSav,cadFileName)
            inputName = os.path.basename(inputPath)
            inpDir = os.path.dirname(inputPath)
            outputName = os.path.basename(outFilePath)
            outpDir = os.path.dirname(outFilePath)
            psspy.psseinit(2000)
            path = inpDir+'\\'+outputName[0:-4]+'.sav'
            psspy.case(path)
            acad(inputName[0:-4],inpDir,outputName[0:-4],outpDir,0,1)
        wx.MessageBox("Export to multiple cad complete!")

    # thêm bus mới
    def Add_New_Bus( self, event ):
        self.m_notebook2.SetSelection(0)
        self.gridSearchLink.matrixBus = matrixBus
        self.gridSearchLink.matrixArea = matrixArea
        self.gridSearchLink.matrixZone = matrixZone
        self.gridSearchLink.matrixSource = matrixGen
        self.gridSearchLink.matrixLoad = matrixLoad
        self.gridSearchLink.matrixShunt = matrixShunt
        self.gridSearchLink.myGridArea = myGridArea
        self.gridSearchLink.myGridZone = myGridZone
        self.gridSearchLink.myGridBus = myGridBus
        self.gridSearchLink.myGridSource = self.m_grid6
        self.gridSearchLink.myGridLoad = self.gridLoad
        self.gridSearchLink.myGridShunt = self.gridShunt
        self.gridSearchLink.myGridFile = myGridFile
        self.gridSearchLink.indexFile = indexFile
        self.gridSearchLink.uk = ukNumSearch
        self.gridSearchLink.Path = PATH
        self.gridSearchLink.PathFile = PATHFILE
        self.gridSearchLink.Add_New_Bus(event)

    def Power_Flow_Cal_Fcn(self, event):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Power_Flow_Cal_Fcn(event)

    # tính TLCS cho file được chọn
    def Power_Flow_Selected_Cal_Fcn(self, event):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Power_Flow_Selected_Cal_Fcn(event,PATH)

    # tính TLCS cho tất cả các file
    def Power_Flow_Selected_Cal_Fcn_ALL(self, event, path):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Power_Flow_Selected_Cal_Fcn(event,path)

    # tính ổn định động từ file idv có sẵn
    def Dynamic_Stability_Cal_Fcn( self, event ):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.matrixGen = matrixGen
        self.Calculation_Link.Dynamic_Stability_Cal_Fcn(event)

    # tính ổn định động bằng cách tạo mới file IDV
    def Dynamic_Stability_Cal_By_Create_New_IDV_Fcn( self, event ):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.indexFile =  indexFile
        self.Calculation_Link.matrixBus = matrixBus
        self.Calculation_Link.Dynamic_Stability_Cal_By_Create_New_IDV_Fcn(event)

    # tính ổn định tĩnh bằng cho tất cả các file trong thư mục từ file sub, mon, con có sẵn, trả về file .pv tương ứng
    def Auto_Static_Stability_Cal_Fcn( self, event ):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Auto_Static_Stability_Cal_Fcn(event)
    
    # chức năng tính ổn định tĩnh cho file được chọn
    def Static_Stability_Cal_Selected_Case_Fcn( self, event ):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Static_Stability_Cal_Selected_Case_Fcn(event)

    # chức năng tính toán kháng bù
    def Shunt_Reactor_Cal_Fcn(self,event):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.indexFile =  indexFile
        self.Calculation_Link.matrixBus = matrixBus
        self.Calculation_Link.Shunt_Reactor_Cal_Fcn(event)

    # chức năng tính contingency bằng cách tao mới file sub, mon, con
    def Create_New_DFX_Fcn( self, event ):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.matrixBus = matrixBus
        self.Calculation_Link.matrixZone = matrixZone
        self.Calculation_Link.matrixArea = matrixArea
        self.Calculation_Link.indexFile = indexFile
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Create_New_DFX_Fcn(event)

    # chức năng tính contingency từ file sub, mon, con đã có
    def Choose_Available_DFX_Fcn( self, event ):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Choose_Available_DFX_Fcn(event)

    # chức năng tự động tính contingency cho tất cả các file trong thư mục
    def Auto_Contigencies_Fcn( self, event ):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Auto_Contigencies_Fcn(event)

    # chức năng tính ngắn mạch phân bố từ bus chọn
    def Distribution_Short_Circuit_Cal_Fcn(self,event):
        self.Calculation_Link.Path = self.Path
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.matrixBus = matrixBus
        self.Calculation_Link.indexFile =  indexFile
        self.Calculation_Link.Distribution_Short_Circuit_Cal_Fcn(event)

    # chức năng tính ngắn mạch phân bố từ file python có sẵn
    def Distribution_Short_Circuit_From_File_Fcn(self,event):
        self.Calculation_Link.Path = self.Path
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.matrixBus = matrixBus
        self.Calculation_Link.indexFile =  indexFile
        self.Calculation_Link.Distribution_Short_Circuit_From_File_Fcn(event)
   
    # chức năng tính ngắn mạch từ bus chọn
    def Short_Circuit_Cal_New_Fcn( self, event ):
        self.Calculation_Link.Path = self.Path
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.matrixBus = matrixBus
        self.Calculation_Link.indexFile =  indexFile
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.Short_Circuit_Cal_New_Fcn(event)

    # tính ngắn mạch từ file python có sẵn
    def Short_Circuit_Cal_From_File_Fcn( self, event ):
        self.Calculation_Link.Path = self.Path
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.Short_Circuit_Cal_From_File_Fcn(event)

    # chức năng tính ngắn mạch cho toàn bộ file trong thư mục, trả về kết quả tổng hợp trong một file txt
    def Short_Circuit_Cal_All_Cases_Fcn_Export_Word( self, event ):
        self.Calculation_Link.Path = self.Path
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Short_Circuit_Cal_All_Cases_Fcn_Export_Word(event)
   
    # chức năng tính ngắn mạch cho toàn bộ file trong thư mục, trả về kết quả cho từng file trong các file txt
    def Short_Circuit_Cal_All_Cases_Fcn_Export_Txt( self, event ):
        self.Calculation_Link.Path = self.Path
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.Short_Circuit_Cal_All_Cases_Fcn_Export_Txt(event)

    # chức năng thu nhỏ cửa sổ
    def Minimize_Fcn(self, event):
        self.Iconize()

    # Hiển thị version
    def Help_Fcn( self, event ):
        wx.MessageBox("Power system calculation support tool Version 1.0.1 date 05/12/2022.")

    # phím tắt
    def Shortcut_Fcn(self, event):
        wx.MessageBox("""Shortcut: 
                        1. Ctrl + O : Open new file.\n
                        2. Ctrl + S : Save all.\n
                        3. Ctrl + W : Close Window. \n
                        4. Ctrl + R : Reload.\n
                        5. Ctrl + G : Add Gen.\n
                        6. Ctrl + B : Add Branch.\n
                        7. Ctrl + 2 : Add 2-Winding.\n
                        8. Ctrl + 3 : Add 3-Winding.\n
                        9. Ctrl + L : Add Load.\n
                        10. Ctrl + U : Add Bus.\n""")
   
    # chức năng turn on/turn off bus
    def Turn_On_Off( self, event ):
        self.gridSearchLink.Path = PATH
        self.gridSearchLink.PathFile = PATHFILE
        self.gridSearchLink.matrixBus = matrixBus
        self.gridSearchLink.myGridBus = myGridBus
        self.gridSearchLink.myGridZone = myGridZone
        self.gridSearchLink.matrixZone = matrixZone
        self.gridSearchLink.myGridArea = myGridArea
        self.gridSearchLink.matrixArea = matrixArea
        self.gridSearchLink.fileInfoTranspose = fileInfoTranspose
        self.gridSearchLink.Turn_On_Off(event) 

    # chức năng split bus (chưa phát triển)
    def splitBus(self,event):
        CustomMyframe1.Add_New_Bus(event)

    # chức năng xóa bus
    def Delete_Bus_Fcn( self, event ):
        self.gridSearchLink.Path = PATH
        self.gridSearchLink.PathFile = PATHFILE
        self.gridSearchLink.matrixBus = matrixBus
        self.gridSearchLink.myGridBus = myGridBus
        self.gridSearchLink.indexFile = indexFile
        self.gridSearchLink.Delete_Bus_Fcn(event)

    # chức năng Reload
    def Reload_Fcn( self, event ):
        self.flagReload = 1
        if self.flagSynch == 0:
            self.UpdatedData(event,indexFile,PATH)
        else:
            for i,path in enumerate(PATHFILE):
                self.UpdatedData(event,i,path)
        self.busNumberEnter_Fcn(event)

    # chức năng cập nhật toàn bộ bảng dữ liệu
    def UpdatedData(self,event,indexfile,path):
        self.gridSearchLink.Path = path
        self.gridSearchLink.PathFile = PATHFILE
        self.gridSearchLink.indexFile = indexfile
        self.gridSearchLink.matrixBus = matrixBus
        self.gridSearchLink.myGridBus = myGridBus
        self.gridSearchLink.myGridZone = myGridZone
        self.gridSearchLink.matrixZone = matrixZone
        self.gridSearchLink.myGridArea = myGridArea
        self.gridSearchLink.matrixArea = matrixArea
        self.gridSearchLink.myGridFile = myGridFile
        self.gridSearchLink.matrixSource = matrixGen
        self.gridSearchLink.matrixLoad = matrixLoad
        self.gridSearchLink.matrixShunt = matrixShunt
        self.gridSearchLink.matrix2Wind = matrix2Wind
        self.gridSearchLink.matrix3Wind = matrix3Wind
        self.gridSearchLink.myGridSource = self.m_grid6
        self.gridSearchLink.myGridLoad = self.gridLoad
        self.gridSearchLink.myGridShunt = self.gridShunt
        self.gridSearchLink.myGrid2Wind = self.grid2wind
        self.gridSearchLink.myGrid3Wind = self.grid3wind
        self.gridSearchLink.fileInfoTranspose = fileInfoTranspose
        self.gridSearchLink.flagSynch = self.flagSynch
        self.gridSearchLink.UpdatedData(event,indexfile,path)

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng đường dây + MBA
    def on_cell_right_click_grid_search( self, event ):
        self.gridSearchLink.matrixBus = matrixBus
        self.gridSearchLink.myGridBus = myGridBus
        self.gridSearchLink.indexFile = indexFile
        self.gridSearchLink.uk = ukNumSearch
        self.gridSearchLink.Path = PATH
        self.gridSearchLink.PathFile = PATHFILE
        self.gridSearchLink.on_cell_right_click_grid_search(event)
    
    # chức năng thực hiện tại ô được chọn của bảng bus
    def on_selected_cell_grid_search( self, event ):
        self.gridSearchLink.matrixBus = matrixBus
        self.gridSearchLink.myGridBus = myGridBus
        self.gridSearchLink.indexFile = indexFile
        self.gridSearchLink.uk = ukNumSearch
        self.gridSearchLink.Path = PATH
        self.gridSearchLink.PathFile = PATHFILE
        self.gridSearchLink.on_selected_cell_grid_search(event)
    
    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại bảng thông tin bus
    def on_key_down_grid_search( self, event ):
        global ukNumSearch
        ukNumSearch = event.UnicodeKey
        self.copyPaste.myGrid = myGridBus
        self.copyPaste.OnKey(event,'Search')

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng bus
    def on_cell_change_grid_search( self, event ):
        self.gridSearchLink.matrixBus = matrixBus
        self.gridSearchLink.myGridBus = myGridBus
        self.gridSearchLink.indexFile = indexFile
        self.gridSearchLink.uk = ukNumSearch
        self.gridSearchLink.Path = PATH
        self.gridSearchLink.PathFile = PATHFILE
        self.gridSearchLink.on_cell_change_grid_search(event)

    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại bảng thông tin đường dây+MBA
    def on_key_down_grid_bus( self, event ):
        global ukNumBus
        self.gridBusInfoLink.matrixMachine = matrixGen
        self.gridBusInfoLink.indexFile = indexFile
        self.gridBusInfoLink.Path = PATH
        self.gridBusInfoLink.PathFile = PATHFILE
        ukNumBus = event.UnicodeKey
        self.gridBusInfoLink.uk = ukNumBus
        self.gridBusInfoLink.location = self.LOCATION
        self.copyPaste.myGrid = self.gridBusInfo
        self.copyPaste.OnKey(event,'busInfo')
        event.Skip()

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng đường dây+MBA
    def on_cell_right_click_grid_bus( self, event ):
        try:
            self.gridBusInfoLink.matrixMachine = matrixGen
            self.gridBusInfoLink.indexFile = indexFile
            self.gridBusInfoLink.matrixBus = matrixBus
            self.gridBusInfoLink.uk = ukNumBus
            self.gridBusInfoLink.Path = PATH
            self.gridBusInfoLink.PathFile = PATHFILE
            self.gridBusInfoLink.location = self.LOCATION
            self.gridBusInfoLink.on_cell_right_click_grid_bus(event)
            event.Skip()
        except:
            wx.MessageBox('Error in on_cell_right_click_grid_bus, please check again!')
            event.Skip()

    # chức năng thực hiện tại ô được chọn của bảng đường dây + MBA
    def on_selected_cell_grid_bus( self, event ):
        row = event.GetRow()
        col = event.GetCol()
        celVal = self.gridBusInfo.GetCellValue(row,col)
        if celVal != '':
            self.gridBusInfoLink.matrixBus = matrixBus
            self.gridBusInfoLink.myGridBus = myGridBus
            self.gridBusInfoLink.indexFile = indexFile
            self.gridBusInfoLink.Path = PATH
            self.gridBusInfoLink.PathFile = PATHFILE
            self.gridBusInfoLink.uk = ukNumBus
            self.gridBusInfoLink.location = self.LOCATION
            self.gridBusInfoLink.on_selected_cell_grid_bus(event)
        else:
            event.Skip()

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng đường dây+MBA
    def on_cell_change_grid_bus( self, event ):

        self.gridBusInfoLink.matrixBus = matrixBus
        self.gridBusInfoLink.myGridBus = myGridBus
        self.gridBusInfoLink.Path = PATH
        self.gridBusInfoLink.PathFile = PATHFILE
        self.gridBusInfoLink.indexFile = indexFile
        self.gridBusInfoLink.uk = ukNumBus
        self.gridBusInfoLink.location = self.LOCATION
        self.gridBusInfoLink.on_cell_change_grid_bus(event)
        event.Skip()

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng MBA 2 cuộn dây
    def on_cell_change_grid_2wind( self, event ):
        self.grid2windLink.matrixBus = matrixBus
        self.grid2windLink.myGridBus = myGridBus
        self.grid2windLink.Path = PATH
        self.grid2windLink.PathFile = PATHFILE
        self.grid2windLink.indexFile = indexFile
        self.grid2windLink.uk = ukNum2Wind
        self.grid2windLink.location = self.LOCATION
        self.grid2windLink.on_cell_change_grid_2wind(event)
        event.Skip()

    # chức năng thực hiện tại ô được chọn của trang MBA 2 cuộn dây
    def on_selected_cell_grid_2wind( self, event ):
        self.grid2windLink.matrixBus = matrixBus
        self.grid2windLink.myGridBus = myGridBus
        self.grid2windLink.indexFile = indexFile
        self.grid2windLink.matrix2Wind = matrix2Wind
        self.grid2windLink.Path = PATH
        self.grid2windLink.PathFile = PATHFILE
        self.grid2windLink.myGrid2Wind = self.grid2wind
        # self.grid2windLink.matrixGen = matrixGen
        self.grid2windLink.uk = ukNum2Wind
        self.grid2windLink.on_selected_cell_grid_2wind(event)
        event.Skip()

    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại bảng MBA 2 cuộn dây
    def on_key_down_grid_2wind( self, event ):
        global ukNum2Wind
        self.grid2windLink.matrix2Wind = matrix2Wind
        self.grid2windLink.myGrid2Wind = self.grid2wind
        self.grid2windLink.Path = PATH
        self.grid2windLink.PathFile = PATHFILE
        self.grid2windLink.indexFile = indexFile
        # self.copyPaste.myGrid = self.m_grid6
        # self.copyPaste.OnKey(event,'source')
        ukNum2Wind = event.UnicodeKey
        event.Skip()

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng MBA 2 cuộn dây
    def on_cell_right_click_grid_2wind( self, event ):
        self.grid2windLink.myGridArea = myGridArea
        self.grid2windLink.matrixArea = matrixArea
        self.grid2windLink.myGridZone = myGridZone
        self.grid2windLink.matrixZone = matrixZone
        self.grid2windLink.myGrid2Wind = self.grid2wind
        self.grid2windLink.matrix2Wind = matrix2Wind
        self.grid2windLink.indexFile = indexFile
        # self.grid2windLink.myGridSource = self.m_grid6
        self.grid2windLink.matrixSource = matrixGen
        self.grid2windLink.Path = PATH
        self.grid2windLink.PathFile = PATHFILE
        self.grid2windLink.on_cell_right_click_grid_2wind(event)

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng mba 3 cuộn dây
    def on_cell_change_grid_3wind( self, event ):
        self.grid3windLink.matrixBus = matrixBus
        self.grid3windLink.myGridBus = myGridBus
        self.grid3windLink.Path = PATH
        self.grid3windLink.PathFile = PATHFILE
        self.grid3windLink.indexFile = indexFile
        self.grid3windLink.uk = ukNum3Wind
        self.grid3windLink.location = self.LOCATION
        self.grid3windLink.on_cell_change_grid_3wind(event)
        event.Skip()

    # chức năng thực hiện tại ô được chọn của trang MBA 3 cuộn dây
    def on_selected_cell_grid_3wind( self, event ):
        self.grid3windLink.matrixBus = matrixBus
        self.grid3windLink.myGridBus = myGridBus
        self.grid3windLink.indexFile = indexFile
        self.grid3windLink.matrix3Wind = matrix3Wind
        self.grid3windLink.Path = PATH
        self.grid3windLink.PathFile = PATHFILE
        self.grid3windLink.myGrid3Wind = self.grid3wind
        self.grid3windLink.uk = ukNum3Wind
        self.grid3windLink.on_selected_cell_grid_3wind(event)
        event.Skip()

    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại bảng MBA 3 cuộn dây
    def on_key_down_grid_3wind( self, event ):
        global ukNum3Wind
        self.grid3windLink.matrix3Wind = matrix3Wind
        self.grid3windLink.myGrid3Wind = self.grid3wind
        self.grid3windLink.Path = PATH
        self.grid3windLink.PathFile = PATHFILE
        self.grid3windLink.indexFile = indexFile
        ukNum3Wind = event.UnicodeKey
        event.Skip()

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng MBA 3 cuộn dây
    def on_cell_right_click_grid_3wind( self, event ):
        self.grid3windLink.myGridArea = myGridArea
        self.grid3windLink.matrixArea = matrixArea
        self.grid3windLink.myGridZone = myGridZone
        self.grid3windLink.matrixZone = matrixZone
        self.grid3windLink.myGrid3Wind = self.grid3wind
        self.grid3windLink.matrix3Wind = matrix3Wind
        self.grid3windLink.indexFile = indexFile
        self.grid3windLink.matrixSource = matrixGen
        self.grid3windLink.Path = PATH
        self.grid3windLink.PathFile = PATHFILE
        self.grid3windLink.on_cell_right_click_grid_3wind(event)
    
    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại ô làm việc trong bảng nguồn
    def on_key_down_grid_source( self, event ):
        global ukNumSource
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.PathFile = PATHFILE
        self.gridSourceLink.indexFile = indexFile
        self.copyPaste.myGrid = self.m_grid6
        self.copyPaste.OnKey(event,'source')
        ukNumSource = event.UnicodeKey
        event.Skip()

    # chức năng thực hiện khi righ click tại ô làm việc trong bảng nguồn
    def on_cell_right_click_grid_source( self, event ):
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.PathFile = PATHFILE
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.areaList = areaList
        self.gridSourceLink.zoneList = zoneList
        self.gridSourceLink.matrixZone = matrixZone
        self.gridSourceLink.matrixArea = matrixArea
        self.gridSourceLink.uk = ukNumSource
        self.gridSourceLink.DyrNewFile = dyrNewFile
        self.gridSourceLink.gridDyn = self.gridDyn
        self.gridSourceLink.on_cell_right_click_grid_source(event)
        event.Skip()
    
    # chức năng thực hiện tại ô làm việc trong bảng nguồn
    def on_selected_cell_grid_source( self, event ):
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.PathFile = PATHFILE
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.uk = ukNumSource
        self.gridSourceLink.on_selected_cell_grid_source(event)
        event.Skip()

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng nguồn
    def on_cell_change_grid_source( self, event ):
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.gridDyn = self.gridDyn
        self.gridSourceLink.matrixZone = matrixZone
        self.gridSourceLink.matrixArea = matrixArea
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.PathFile = PATHFILE
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.uk = ukNumSource
        self.gridSourceLink.on_cell_change_grid_source(event)
        event.Skip()

    # Khi search một nguồn bất kỳ theo mã nguồn, sẽ xóa thông tin trong bảng source, 
    # chỉ hiển thị thông tin của nguồn tìm được
    @debounced_search('gen_number', 'genNumber',
                      priority='GENNUMBER', delay_ms=200)
    def genNumberEnter_Fcn(self,event):
        self.priority = 'GENNUMBER'
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.uk = ukNumSource
        self.gridSourceLink.genNumberEnter_Fcn(event)
        event.Skip()
    
    # Khi search một nguồn bất kỳ theo tên nguồn, sẽ xóa thông tin trong bảng source, 
    # chỉ hiển thị thông tin của nguồn tìm được
    @debounced_search('gen_name', 'genName',
                      priority='GENNAME', delay_ms=200)
    def genNameEnter_Fcn(self,event):
        self.priority = "GENNAME"
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.uk = ukNumSource
        self.gridSourceLink.genNameEnter_Fcn(event)
        event.Skip()

    # chức năng thực hiện khi thay đổi tại ô Gen Number (search gen theo mã nguồn)
    def onKeyDownGenNumber(self,event):
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.ukNum = event.UnicodeKey
        self.gridSourceLink.ukName = 0
        self.gridSourceLink.genNameEnter_Fcn(event)
        event.Skip()

    # chức năng thực hiện khi thay đổi tại ô Gen Name (search gen theo tên nguồn)
    def onKeyDownGenName(self,event):
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.ukName = event.UnicodeKey
        self.gridSourceLink.ukNum = 0
        self.gridSourceLink.genNameEnter_Fcn(event)
        event.Skip()

    # chức năng thực hiện khi nhấn phím enter tại ô làm  việc trong bảng phụ tải
    @debounced_search('load_number', 'loadNumber',
                      priority='LOADNUMBER', delay_ms=200)
    def loadNumberEnter_Fcn(self,event):
        self.priority = 'LOADNUMBER'
        self.gridLoadLink.matrixBus = matrixBus
        self.gridLoadLink.myGridBus = myGridBus
        self.gridLoadLink.indexFile = indexFile
        self.gridLoadLink.Path = PATH
        self.gridLoadLink.PathFile = PATHFILE
        self.gridLoadLink.myGridLoad = self.gridLoad
        self.gridLoadLink.matrixLoad = matrixLoad
        self.gridLoadLink.uk = ukNumLoad
        self.gridLoadLink.loadNumberEnter_Fcn(event)
        event.Skip()

    # chức năng thực hiện khi nhấn phím enter tại ô làm  việc trong bảng kháng/tụ
    @debounced_search('shunt_number', 'shuntNumber',
                      priority='SHUNTNUMBER', delay_ms=200)
    def shuntNumberEnter_Fcn(self,event):
        self.priority = 'SHUNTNUMBER'
        self.gridShuntLink.matrixBus = matrixBus
        self.gridShuntLink.myGridBus = myGridBus
        self.gridShuntLink.indexFile = indexFile
        self.gridShuntLink.Path = PATH
        self.gridShuntLink.PathFile = PATHFILE
        self.gridShuntLink.myGridShunt = self.gridShunt
        self.gridShuntLink.matrixShunt = matrixShunt
        self.gridShuntLink.uk = ukNumShunt
        self.gridShuntLink.shuntNumberEnter_Fcn(event)
        event.Skip()

    # chức năng thực hiện khi nhấn phím enter tại ô làm  việc trong bảng dynamic
    @debounced_search('dynamic_number', 'search_dyn', delay_ms=200)
    def dynNumberEnter_Fcn(self,event):
        self.gridDynLink.matrixBus = matrixBus
        self.gridDynLink.myGridBus = myGridBus
        self.gridDynLink.indexFile = indexFile
        self.gridDynLink.myGridDyn = self.gridDyn
        self.gridDynLink.matrixGen = matrixGen
        self.gridDynLink.matrixLoad = matrixLoad
        self.gridDynLink.Path = PATH
        self.gridDynLink.dynNumberEnter_Fcn(event)
    
    # chức năng thêm mới phụ tải
    def Add_New_Load(self,event):
        self.gridLoadLink.matrixBus = matrixBus
        self.gridLoadLink.myGridBus = myGridBus
        self.gridLoadLink.indexFile = indexFile
        self.gridLoadLink.myGridLoad = self.gridLoad
        self.gridLoadLink.matrixLoad = matrixLoad
        self.gridLoadLink.Path = PATH
        self.gridLoadLink.PathFile = PATHFILE
        self.gridLoadLink.uk = ukNumLoad
        self.gridLoadLink.Add_New_Load(event)
        event.Skip()

    # chức năng thêm mới phụ tải
    def load_new_fcn( self, event ):
        self.Add_New_Load(event)
    
    # chức năng kiểm soát sự thay đổi khi click chuột phải trong bảng phụ tải
    def on_cell_right_click_grid_load( self, event ):
        self.gridLoadLink.matrixBus = matrixBus
        self.gridLoadLink.myGridBus = myGridBus
        self.gridLoadLink.indexFile = indexFile
        self.gridLoadLink.Path = PATH
        self.gridLoadLink.PathFile = PATHFILE
        self.gridLoadLink.myGridLoad = self.gridLoad
        self.gridLoadLink.matrixZone = matrixZone
        self.gridLoadLink.matrixArea = matrixArea
        self.gridLoadLink.matrixLoad = matrixLoad
        self.gridLoadLink.matrixSource = matrixGen
        self.gridLoadLink.uk = ukNumLoad
        self.gridLoadLink.on_cell_right_click_grid_load(event)
        event.Skip()
    
    # chức năng thực hiện tại ô được chọn trong bảng phụ tải
    def on_selected_cell_grid_load( self, event ):
        self.gridLoadLink.matrixBus = matrixBus
        self.gridLoadLink.myGridBus = myGridBus
        self.gridLoadLink.indexFile = indexFile
        self.gridLoadLink.Path = PATH
        self.gridLoadLink.PathFile = PATHFILE
        self.gridLoadLink.myGridLoad = self.gridLoad
        self.gridLoadLink.matrixLoad = matrixLoad
        self.gridLoadLink.uk = ukNumLoad
        self.gridLoadLink.on_selected_cell_grid_load(event)
        event.Skip()

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng phụ tải
    def on_cell_change_grid_load( self, event ):
        self.gridLoadLink.matrixBus = matrixBus
        self.gridLoadLink.myGridBus = myGridBus
        self.gridLoadLink.indexFile = indexFile
        self.gridLoadLink.Path = PATH
        self.gridLoadLink.PathFile = PATHFILE
        self.gridLoadLink.myGridLoad = self.gridLoad
        self.gridLoadLink.matrixZone = matrixZone
        self.gridLoadLink.matrixArea = matrixArea
        self.gridLoadLink.matrixLoad = matrixLoad
        self.gridLoadLink.matrixSource = matrixGen
        self.gridLoadLink.uk = ukNumLoad
        self.gridLoadLink.on_cell_change_grid_load(event)
        event.Skip()

    # chức năng thực hiện khi có sự thay đổi từ bàn phím tại ô làm việc trong bảng phụ tải
    def on_key_down_grid_load( self, event ):
        self.gridLoadLink.myGridLoad = self.gridLoad
        self.gridLoadLink.matrixLoad = matrixLoad
        self.gridLoadLink.Path = PATH
        self.gridLoadLink.PathFile = PATHFILE
        self.gridLoadLink.indexFile = indexFile
        global ukNumLoad
        ukNumLoad = event.UnicodeKey
        self.gridLoadLink.uk = ukNumLoad
        self.gridLoadLink.on_key_down_grid_load(event)
        self.copyPaste.myGrid = self.gridLoad
        self.copyPaste.OnKey(event,'load')
        event.Skip()

    # chức năng scale tải của zone
    def scale_zone_load( self,event):
        self.gridLoadLink.myGridLoad = self.gridLoad
        self.gridLoadLink.matrixLoad = matrixLoad
        self.gridLoadLink.myGridZone = myGridZone
        self.gridLoadLink.matrixZone = matrixZone
        self.gridLoadLink.myGridArea = myGridArea
        self.gridLoadLink.matrixArea = matrixArea
        self.gridLoadLink.zoneNum = selectedZoneNum
        self.gridLoadLink.indexFile = indexFile
        self.gridLoadLink.Path = PATH
        self.gridLoadLink.PathFile = PATHFILE
        self.gridLoadLink.scaleZoneLoad(event,selectedZoneRow)
        event.Skip()
    
    # chức năng thay đổi thông số tải của zone được chọn theo % thay đổi
    def change_percent_p_fcn( self, event ):
        self.flagChangePPercent = 1
        self.flagChangeNewPVal = 0
        self.flagChangeDeltaP = 0
        event.Skip()
    
    # chức năng thay đổi thông số tải của zone được chọn thành số mới theo delta P 
    def change_delta_p_fcn( self, event ):
        self.flagChangePPercent = 0
        self.flagChangeNewPVal = 0
        self.flagChangeDeltaP = 1
        event.Skip()
    
    # chức năng thay đổi thông số tải của zone được chọn thành số mới
    def change_new_fcn( self, event ):
        self.flagChangePPercent = 0
        self.flagChangeNewPVal = 1
        self.flagChangeDeltaP = 0
        event.Skip()

    # Chuc nang them moi khang/tu
    def Add_New_Shunt(self,event):
        self.gridShuntLink.matrixBus = matrixBus
        self.gridShuntLink.myGridBus = myGridBus
        self.gridShuntLink.indexFile = indexFile
        self.gridShuntLink.myGridShunt = self.gridShunt
        self.gridShuntLink.matrixShunt = matrixShunt
        self.gridShuntLink.Path = PATH
        self.gridShuntLink.PathFile = PATHFILE
        self.gridShuntLink.uk = ukNumShunt
        self.gridShuntLink.Add_New_Shunt(event)

    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng kháng tụ
    def on_cell_change_grid_shunt( self, event ):
        self.gridShuntLink.matrixBus = matrixBus
        self.gridShuntLink.myGridBus = myGridBus
        self.gridShuntLink.indexFile = indexFile
        self.gridShuntLink.Path = PATH
        self.gridShuntLink.PathFile = PATHFILE
        self.gridShuntLink.myGridShunt = self.gridShunt
        self.gridShuntLink.matrixZone = matrixZone
        self.gridShuntLink.matrixSource = matrixGen
        self.gridShuntLink.matrixShunt = matrixShunt
        self.gridShuntLink.uk = ukNumShunt
        self.gridShuntLink.on_cell_change_grid_shunt(event)
    
    # chuc nang kiem soat su thay doi khi click chuot phai trong bang khang tu, tao righ click tab
    def on_cell_right_click_grid_shunt( self, event ):
        self.gridShuntLink.matrixBus = matrixBus
        self.gridShuntLink.myGridBus = myGridBus
        self.gridShuntLink.indexFile = indexFile
        self.gridShuntLink.Path = PATH
        self.gridShuntLink.PathFile = PATHFILE
        self.gridShuntLink.myGridShunt = self.gridShunt
        self.gridShuntLink.matrixZone = matrixZone
        self.gridShuntLink.matrixShunt = matrixShunt
        self.gridShuntLink.matrixSource = matrixGen
        self.gridShuntLink.uk = ukNumShunt
        self.gridShuntLink.on_cell_right_click_grid_shunt(event)
    
    # chức năng thực hiện tại ô được chọn trong bảng kháng tụ
    def on_selected_cell_grid_shunt( self, event ):
        self.gridShuntLink.matrixBus = matrixBus
        self.gridShuntLink.myGridBus = myGridBus
        self.gridShuntLink.indexFile = indexFile
        self.gridShuntLink.Path = PATH
        self.gridShuntLink.PathFile = PATHFILE
        self.gridShuntLink.myGridShunt = self.gridShunt
        self.gridShuntLink.matrixShunt = matrixShunt
        self.gridShuntLink.uk = ukNumShunt
        self.gridShuntLink.on_selected_cell_grid_shunt(event)
    
    # chức năng thực hiện khi có sự thay đổi từ bàn phím trong bảng kháng tụ
    def on_key_down_grid_shunt( self, event ):
        global ukNumShunt
        self.gridShuntLink.matrixBus = matrixBus
        self.gridShuntLink.myGridBus = myGridBus
        self.gridShuntLink.indexFile = indexFile
        self.gridShuntLink.Path = PATH
        self.gridShuntLink.PathFile = PATHFILE
        self.gridShuntLink.myGridShunt = self.gridShunt
        self.gridShuntLink.matrixShunt = matrixShunt
        ukNumShunt = event.UnicodeKey
        self.gridShuntLink.uk = ukNumShunt
        self.gridShuntLink.on_key_down_grid_shunt(event)
        self.copyPaste.myGrid = self.gridShunt
        self.copyPaste.OnKey(event,'shunt')
        event.Skip()

    # Chức năng load file Dyr vào công cụ và hiển thị
    def Load_Dyr_File(self,event):
        # GEN
        labelGENROU = ['','','',"T'do",'T"do',"T'qo",'T"qo','H','D','Xd','Xq',"X'd","X'q",'X"d','X1','S(1.0)','S(1.2)']
        labelGENSAL = ['','','',"T'do",'T"do','T"qo','H','D','Xd','Xq',"X'd",'X"d','X1','S(1.0)','S(1.2)']
        # AVR
        labelESST1A = ['','','']
        labelESST4B = ['','','','TR','KPR','KIR','VRMAX','VRMIN','TA','KPM','KIM','VMMAX','VMMIN','KG','KP','KI','VBMAX','KC','XL','THETAP']
        labelEXAC4 = ['','','',"TR","VIMAX","VIMIN","TC","TB","KA","TA","VRMAX","VRMIN","KC"]
        # GOV
        labelTGOV1 = ['','','','R','T1','VMAX','VMIN','T2','T3','Dt']
        labelHYGOV = ['','','',"R","r","Tr","Tf","Tg","VELM","GMAX","GMIN","TW","At","Dturb","qNL"]
        labelGAST = ['','','',"R","T1","T2","T3","AT","KT","VMAX","VMIN","Dturb"]
        # PSS
        labelPSS2A = ['','','','IC1','REMBUS1','IC2','REMBUS2','M','N','TW1','TW2','T6','TW3','TW4','T7','Ks2','Ks3','T8','T9','Ks1','T1','T2','T3','T4','VSTMAX','VATMIN']
        # Solar
        labelPVGU1 = ['','','','','','','','','','TlqCmd','TlpCmd','VLVPL1','VLVPL2','GLVPL','VHVRCR','CURHVRCR','Rip_LVPL','T_LVPL']
        labelPVEU = ['','','','','','','','','','Remote Bus','PFAFLG','VARFLG','PQFLG','Tw','Kpv','Kiv','Kpp','Kip','Kf','Tf','Qmx','Qmn','IPmax','Trv','dPMX','dPMN','Tpower','KQi','Vmincl','Vmaxcl','KVi','Tv','Tp','ImaxTD','IphI','IqhI','PMX']
        labelPANELU1 = ['','','','','','','','','','PDCMAX200','PDCMAX400','PDCMAX600','PDCMAX800','PDCMAX1000']
        labelIRRADU1 = ['','','','','','','','','','Inservice flag','TIME1','IRRADIANCE1','TIME2','IRRADIANCE2','TIME3','IRRADIANCE3','TIME4','IRRADIANCE4','TIME5','IRRADIANCE5','TIME6','IRRADIANCE6','TIME7','IRRADIANCE7','TIME8','IRRADIANCE8','TIME9','IRRADIANCE9','TIME10','IRRADIANCE10']
        # Wind
        labelGEWTGCU1 = ['','','','','','','','','','WTs originNum','Full ConvFlag','Prate','Xeq','Vlvpl1','Vlvpl2','Glvpl','Vhvrcr2','CURhvrcr2','Vlvacr1','VLVACR2','Rip_LVPL','T_LVPL','LVPL1stV','LVPL1stP','LVPL2ndV','LVPL2ndP','LVPL3rdV','LVPL3rdP','Impedance']
        labelGEWTECU1 = ['','','','','','','','','','Remote Bus','PFAFlg','VARFlg','APCFlg','PQFlg','Qdroof FromBus','Qdroof ToBus','Qdroof ID','Tfv','Kpv','Kiv','Rc','Xc','Tfp','Kpp','Kip','Pmax','Pmin','Qmax','Qmin','IPmax','Trv','RPmax','RPmin','Tpowwer','KQu','Vmincl','Vmaxcl','KV','XLmin',\
                        'XLmax','Tv','Tp','Fn','Tpav','FRa','FRb','FRc','FRd','PFRa','PFRb','PFRc','PFRd','PFRmax','PFRmin','Tw','Tlvpl','Vlvpl','SPDW1','SPDWmax','SPDWmin','SPDlow','WTTHRES','EBST','KDBR','PDBRmax','IMAXtd','IPHL','IQHL','Tlpqd','Kqd','Xqd','Kwi','DBwi','TLPwi','TWOwi','URLwi','DRLwi','PMXwi','PMNwi','VERmx','VERmn','Vfrz','QZPmx','QZPmn']
        labelGEWT2MU1 = ['','','','','','','','','','H','DAMP','HTfrac','FREQ','DSHAFT']
        labelGEWTPTU1 = ['','','','','','','','','','','','Tp','Kppt','Kipt','Kpc','Kic','0min','0max','d0/dtmin','d0/dtmax','Pref']
        labelGEWTARU1 = ['','','','','','','','','','','LamdaMax','LamdaMin','PITCHmax','PITCHmin','Ta','P','Raddius','GBRatio','SYNCHR']
        labelGEWTGDU1 = ['','','','','','','','','','','T1G','Tg','MAXg','T1r','T2r','Max']

        labelTypes = [labelGENROU,labelGENSAL,labelESST1A,labelESST4B,labelEXAC4,labelTGOV1,labelHYGOV,labelGAST,labelPSS2A,labelPVGU1,labelPVEU,labelPANELU1,labelIRRADU1,labelGEWTGCU1,labelGEWTECU1,labelGEWT2MU1,labelGEWTPTU1,labelGEWTARU1,labelGEWTGDU1]
        modelTypes = ["'GENROU'","'GENSAL'","'ESST1A'","'ESST4B'","'EXAC4'","'TGOV1'","'HYGOV'","'GAST'","'PSS2A'","'PVGU1'","'PVEU1'","'PANELU1'","'IRRADU1'","'GEWTGCU1'","'GEWTECU1'","'GEWT2MU1'","'GEWTPTU1'","'GEWTARU1'","'GEWTGDU1'"]
        
        global dyrNewFile,lineNumber,lineNumberUpdate

        dyrFile = openFile(self,'Choose the dyr files', "Dynamic files (*.dyr)|*.dyr|All files|*")
        dyrNewFile = dyrFile
        rows = self.gridDyn.GetNumberRows()
        cols = self.gridDyn.GetNumberCols()

        self.gridDynLink.myGridDyn = self.gridDyn

        flag = 1
        for i in range(rows):
                rowArr = []
                if i%2==1:
                    for j in range(cols):
                            val = self.gridDyn.GetCellValue(i,j)
                            rowArr.append(str(val))
                    if all(x is '' for x in rowArr) and i!=0:
                            lineNumber = (i-1)/2
                            flag = 0
                if flag == 0:
                    break
        
        for i in range(lineNumber*2):
            for j in range(cols):
                self.gridDyn.SetCellValue(i,j,'')
                color = self.gridDyn.GetCellTextColour(i,j)
                if self.flagRestriction == 1 and color == wx.Colour(255, 0, 0, 255):
                    self.gridDyn.SetCellTextColour(i,j,wx.Colour(0,0,0))

        f = open(dyrFile,'r')
        lines = f.readlines()
        lineNumberUpdate = len(lines)
    
        for i,line in enumerate(lines):
            line = line.split()
            model = ''
            if len(line)!=0:
                model = line[1]
                indexType = modelTypes.index(model)
                label = labelTypes[indexType]
                modelType = self.gridDynLink.returnType(modelTypes,model[1:-1])
                celChoice =wx.grid.GridCellChoiceEditor(modelType,allowOthers=True)
                self.gridDyn.SetCellEditor(2*i+1,1,celChoice)

                # ghi label cho thông số động
                for j in range(len(label)):
                    self.gridDyn.SetCellValue(2*i,j,str(label[j]))
                # ghi giá trị cho thông số động
                for j in range(len(line)):
                    self.gridDyn.SetCellValue(2*i+1,j,str(line[j]))

                if self.flagRestriction == 1:
                    for j in range(len(line)):
                        self.gridDynLink.set_restriction(line[1][1:-1],2*i+1)

        f.close()

    # Chức năng đặt điều kiện ràng buộc để kiểm tra giá trị trong file dyr có vi phạm giới hạn không?
    def onSetRestriction(self,event):
        val = self.SetRestriction.GetValue()
        if  val == True:
            self.flagRestriction = 1
        else:
            self.flagRestriction = 1
        event.Skip()
    
    # Chức năng lưu file Dyr
    def Save_Dyr_File(self,event):
        n = open(dyrNewFile,'w')    
        rowNums = self.gridDyn.GetNumberRows()
        colNums = self.gridDyn.GetNumberCols()
        flag = 1
        for i in range(rowNums):
            rowArr = []
            if i%2==1:
                for j in range(colNums):
                    val = self.gridDyn.GetCellValue(i,j)
                    rowArr.append(str(val))
                    n.writelines(val+'  ')
                n.writelines('\n')
                if all(x is '' for x in rowArr) and i!=0:
                    flag = 0
            if flag == 0:
                break
        n.close()
        wx.MessageBox('This dyr file was saved in: {}'.format(dyrNewFile))
    
    # chức năng thực hiện tại ô được chọn của trang dynamic
    def on_selected_cell_grid_dyn( self, event ):
        self.gridDynLink.matrixBus = matrixBus
        self.gridDynLink.myGridBus = myGridBus
        self.gridDynLink.indexFile = indexFile
        self.gridDynLink.myGridDyn = self.gridDyn
        self.gridDynLink.matrixLoad = matrixLoad
        self.gridDynLink.Path = PATH
        self.gridDynLink.on_selected_cell_grid_dyn(event)
    
    # chức năng thực hiện khi có sự chuyển đổi ô làm việc trong bảng dynamic
    def on_cell_change_grid_dyn( self, event ):
        self.gridDynLink.matrixBus = matrixBus
        self.gridDynLink.myGridBus = myGridBus
        self.gridDynLink.indexFile = indexFile
        self.gridDynLink.myGridDyn = self.gridDyn
        self.gridDynLink.matrixLoad = matrixLoad
        self.gridDynLink.myGridSource = self.m_grid6
        self.gridDynLink.matrixGen = matrixGen
        self.gridDynLink.Path = PATH
        self.gridDynLink.on_cell_change_grid_dyn(event)
    
    # chức năng thêm mới nguồn
    def Add_New_Gen( self, event ):
        if dyrNewFile == '' and self.Count == 0:
            wx.MessageBox('Please load Dynamic model!')
            self.Count = 1
        self.gridSourceLink.matrixBus = matrixBus
        self.gridSourceLink.myGridBus = myGridBus
        self.gridSourceLink.indexFile = indexFile
        self.gridSourceLink.myGridSource = self.m_grid6
        self.gridSourceLink.areaList = areaList
        self.gridSourceLink.zoneList = zoneList
        self.gridSourceLink.matrixZone = matrixZone
        self.gridSourceLink.matrixArea = matrixArea
        self.gridSourceLink.matrixZone = matrixZone
        self.gridSourceLink.matrixGen = matrixGen
        self.gridSourceLink.uk = ukNumSource
        self.gridSourceLink.Path = PATH
        self.gridSourceLink.PathFile = PATHFILE
        self.gridSourceLink.DyrNewFile = dyrNewFile
        self.gridSourceLink.gridDyn = self.gridDyn
        self.gridSourceLink.Add_New_Gen(event) 

    def add_gen_fcn( self, event ):
        self.Add_New_Gen(event)

    def onClickShuntPage( self, event ):
        event.Skip()

    # chức năng thêm mới nguồn
    def Add_Gen_Fcn( self, event ):
        self.m_notebook2.SetSelection(1)
        self.Add_New_Gen(event)

    # chức năng kiểm tra X Source trong file psse đang làm việc và cơ sở dữ liệu
    def checkDatabase_fcn( self,event):
        for row3 in range(len(matrixGen[indexFile])):
            XSourceDataBase = self.gridSourceLink.SelectXSourcePMAX(int(self.m_grid6.GetCellValue(row3,2)),float(self.m_grid6.GetCellValue(row3,12))) # select by area num and PMax
            celChoiceLines =wx.grid.GridCellChoiceEditor(XSourceDataBase,allowOthers=True)
            MBase  = float(self.m_grid6.GetCellValue(row3,12))/0.9
            if len(XSourceDataBase)!=0:
                self.m_grid6.SetCellEditor(row3,24,celChoiceLines)
                if XSourceDataBase[0]!= self.m_grid6.GetCellValue(row3,24):
                    self.m_grid6.SetCellTextColour(row3,24,wx.RED)
        event.Skip()
    
    # chức năng kiểm tra X Source trong file dữ liệu động và file psse đang làm việc
    def checkDyr_fcn(self,event):
        if dyrNewFile != '':
            self.indexInDyr = ['NaN']*len(matrixGen[indexFile])
            for row3 in range(len(matrixGen[indexFile])):
                xSource = ''
                number = self.m_grid6.GetCellValue(row3,0)
                idGenSourcePage = self.m_grid6.GetCellValue(row3,6)

                for i in range(lineNumberUpdate):
                    numberDyr = self.gridDyn.GetCellValue(2*i+1,0)
                    idGenDynPage =  self.gridDyn.GetCellValue(2*i+1,2)
                    model =  self.gridDyn.GetCellValue(2*i+1,1)

                    if str(number) == str(numberDyr) and str(model) == "'GENROU'" and str(idGenSourcePage).strip() == str(idGenDynPage).strip() :
                        xSource = self.gridDyn.GetCellValue(2*i+1,13)
                        self.indexInDyr[row3] = 2*i+1
                        break
                    elif str(number) == str(numberDyr) and str(model) == "'GENSAL'" and str(idGenSourcePage).strip() == str(idGenDynPage).strip()  :
                        xSource = self.gridDyn.GetCellValue(2*i+1,11)
                        self.indexInDyr[row3] = 2*i+1
                        break

                self.m_grid6.SetCellValue(row3,25,str(xSource))
        else:
            wx.MessageBox('Please load the dyr file first!')

        event.Skip()

    # thêm mới đường dây
    def Add_Branch_Fcn( self, event ):
        self.m_notebook2.SetSelection(0)
        self.gridBusInfoLink.matrixBus = matrixBus
        self.gridBusInfoLink.indexFile = indexFile
        self.gridBusInfoLink.Path = PATH
        self.gridBusInfoLink.PathFile = PATHFILE
        self.gridBusInfoLink.AddNewBranch(event)

    # thêm mới MBA 3 cuộn dây
    def Add_3Winding_Fcn( self, event ):
        self.m_notebook2.SetSelection(0)
        self.gridBusInfoLink.matrixBus = matrixBus
        self.gridBusInfoLink.indexFile = indexFile
        self.gridBusInfoLink.Path = PATH
        self.gridBusInfoLink.PathFile = PATHFILE
        self.gridBusInfoLink.AddNew3Wind(event)

    # thêm mới MBA 2 cuộn dây
    def Add_2Winding_Fcn( self, event ):
        self.m_notebook2.SetSelection(0)
        self.gridBusInfoLink.Path = PATH
        self.gridBusInfoLink.PathFile = PATHFILE
        self.gridBusInfoLink.matrixBus = matrixBus
        self.gridBusInfoLink.matrixMachine = matrixGen
        self.gridBusInfoLink.indexFile = indexFile
        self.gridBusInfoLink.AddNew2Wind(event)

    # thêm mới tải
    def Add_Load_Fcn( self, event ):
        self.m_notebook2.SetSelection(2)
        self.Add_New_Load(event)
        event.Skip()

    # thêm mới kháng/tụ
    def Add_Shunt_Fcn( self, event ):
        self.m_notebook2.SetSelection(3)
        self.Add_New_Shunt(event)
        event.Skip()

    # Mở file psse đang làm việc
    def View_PSSE_Fcn( self, event ):
        if PATH != "":
            # Open file with PSS/E
            call(('cmd','/c','start','',PATH_ORIGIN))
        else: wx.MessageBox("Please open an existing case first!")
    
    # Mở cơ sở dữ liệu
    def View_Database_Fcn( self, event ):
        DatabasePath = "Database.mdb"
        call(('cmd','/c','start','',DatabasePath))

    # chức năng cập nhật từng bước
    def onUpdatedStepByStep( self, event ):
        self.flagUpdate = 1
        event.Skip()
    
    # chức năng cập nhật sau
    def onUpdatedLater( self, event ):
        self.flagUpdate = 0
        event.Skip()

    # chức năng cập nhật đồng thời nhiều file
    def onUpdateSynch(self,event):
        self.flagSynch = 1
        event.Skip()

    # chức năng cập nhật riêng lẻ từng file
    def onUpdateIndividual(self,event):
        self.flagSynch = 0
        event.Skip()

    # chức năng tạo file lưu thao tác
    def onCreateMacro(self,event):
        self.flagCreateMacro = 1
        if PATH != '':
            fileIndex = PATHFILE_ORIGIN.index(PATH_ORIGIN)
            dDir = os.path.dirname(PATH_ORIGIN)
            dFile = os.path.basename(PATH_ORIGIN)
        else:
            dDir = os.getcwd() 
            dFile = u""
        wildcard = "Python files (*.py)|*.py|All files|*"
        self.macroFile = saveFile(self,"Filename",wildcard,dDir,dFile )
        f = open(self.macroFile,'w')
        f.write("import pssepath\n")
        f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
        f.write("sys.path.append(PSSE_LOCATION)\n")
        f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
        f.write("pssepath.add_pssepath(33)\n")
        f.write("import psspy \n")
        f.close()
        event.Skip()
    
    # ghi nhận việc kết thúc quá trình lưu thao tác
    def onFinishRecord(self,event):
        self.flagCreateMacro = 0
        self.macroFile = ''
        event.Skip()

    # chức năng run một file macro có sẵn
    def Run_Macro_Fcn( self, event ):
        if PATH == '':
            psspy.psseinit(2000)
        # vì khi runn macro file không phải từ tool thì cần có thư viện hỗ trỡ kết nối,
        # do đó khi run 1 file macro có sẵn cần bổ sung phần thư viện này 
        pythonFile = openFile(self,'Please select .py file', '*.py')
        dirNameSav = openFolder(self,"Choose the folder contain all sav files." )
        os.chdir(dirNameSav)
        savfileNames = glob.glob('*.sav')
        f = open('auto.py','w')
        f.write("import pssepath\n")
        f.write("PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'\n")
        f.write("sys.path.append(PSSE_LOCATION)\n")
        f.write("os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION\n")
        f.write("pssepath.add_pssepath(33)\n")
        f.write("import psspy \n")
        for savFile in savfileNames:
            f.write('psspy.case(r"""{}""") \n'.format(savFile))
            r = open(pythonFile,'r')
            for line in r:
                if not ('import' in line or  'PSSE_LOCATION' in line or 'add_pssepath(33)' in line):
                    f.write(line)
            r.close()
            f.write('psspy.save(r"""{}""") \n'.format(savFile))
        f.close()
        # thực thi file trung gian
        execfile('auto.py')
        wx.MessageBox("Calculation Finish!")
        # loại bỏ file trung gian
        os.remove('auto.py')
        
        event.Skip()
    
    # Chức năng cập nhật lại theo thứ tự ưu tiên, để giảm thiểu thời gian, mỗi lần cập nhật lại chỉ cập nhật cho bảng đang làm việc
    def onUpdateFcn(self,event):
        # self.flagOnUpdateFcn != 1
        self.onUpdate = 1
        if self.priority == "AREA":
            self.on_selected_cell_grid_area( event )
        elif self.priority == "ZONE":
            self.on_selected_cell_grid_zone( event )
        elif self.priority == "FILTER_INPUT_TEXT":
            self.OnTextSearch( event )
        elif self.priority == "GENNUMBER":
            self.genNumberEnter_Fcn( event )
        elif self.priority == "GENNAME":
            self.genNameEnter_Fcn( event )
        elif self.priority == "LOADNUMBER":
            self.loadNumberEnter_Fcn( event )
        elif self.priority == "SHUNTNUMBER":
            self.shuntNumberEnter_Fcn( event )
        elif self.priority == "":
            self.onUpdate = 0
        self.onUpdate = 0

    # chức năng tính toán truyền tải liên miền
    def InterRegionLimit(self,event):
        self.Calculation_Link.Path = PATH
        self.Calculation_Link.PathOrigin = PATH_ORIGIN
        self.Calculation_Link.PathFile = self.PathFile
        self.Calculation_Link.InterRegionLimit(event)

    # Button tính nhanh có chức năng tính contingency cho tất cả các file trong thư mục được chọn
    def Auto_Contingency( self, event ):
        self.Auto_Contigencies_Fcn(event )
        event.Skip()
    
    # Button tính nhanh có chức năng xuất cad cho tất cả các file trong thư mục được chọn
    def Export_Multiple_Cad( self, event ):
        self.Export_Multi_Cad(event )
        event.Skip()

    # Button tính nhanh có chức năng tính ngắn mạch cho tất cả các file trong thư mục được chọn và export kết quả tổng hợp
    def Short_Circuit_All_File( self, event ):
        self.Short_Circuit_Cal_All_Cases_Fcn_Export_Word( event )
        event.Skip()

    def _set_record_tool_state(self, is_recording):
        self.m_tool4.SetValue(is_recording)
        if is_recording:
            self.m_tool4.SetLabel(u"Stop Recording")
            self.m_tool4.SetToolTipString(u"Stop and save PSSE command recording")
        else:
            self.m_tool4.SetLabel(u"Record")
            self.m_tool4.SetToolTipString(u"Record PSSE commands")
        self.m_tool4.Refresh()

    # Start/stop native PSSE Python command recording from the dashboard.
    def Record_Automation( self, event ):
        if self.commandRecorder.is_recording:
            try:
                outputPath = self.commandRecorder.stop()
            except RecorderError as error:
                wx.MessageBox(str(error), u"Recording error", wx.OK | wx.ICON_ERROR, self)
            else:
                wx.MessageBox(
                    u"Automation recording saved to:\n%s" % outputPath,
                    u"Recording completed",
                    wx.OK | wx.ICON_INFORMATION,
                    self,
                )
            self._set_record_tool_state(False)
            if event is not None:
                event.Skip()
            return

        if PATH_ORIGIN == '':
            self._set_record_tool_state(False)
            wx.MessageBox(
                u"Open a PSSE .sav file before starting a recording.",
                u"No PSSE file is open",
                wx.OK | wx.ICON_WARNING,
                self,
            )
            if event is not None:
                event.Skip()
            return

        defaultDirectory = os.path.dirname(PATH_ORIGIN)
        outputPath = prompt_automation_path(self, defaultDirectory, u"auto1.py")
        if outputPath is None:
            self._set_record_tool_state(False)
            if event is not None:
                event.Skip()
            return

        try:
            self.commandRecorder.start(outputPath)
        except RecorderError as error:
            self._set_record_tool_state(False)
            wx.MessageBox(str(error), u"Recording error", wx.OK | wx.ICON_ERROR, self)
        else:
            self._set_record_tool_state(True)
            wx.MessageBox(
                u"Recording PSSE commands to:\n%s\n\nClick Record again to stop and save." % outputPath,
                u"Recording started",
                wx.OK | wx.ICON_INFORMATION,
                self,
            )

        if event is not None:
            event.Skip()

if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = CustomMyframe1(None)
    frame.SetIcon(wx.Icon("icon4.png"))
    frame.Show(True)
    app.MainLoop()

