import glob, os, sys
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
from LoadTab import loadBusTab, loadMachineTab,searchByChoice,loadBusNumberEnter,loadFileInfo,loadAreaInfo,loadZoneInfo,loadLoadTab,loadShuntTab
from LoadTab import select_zone_from_area, select_bus_from_zone, select_bus_from_matrixBus,select_source_from_zone,select_load_from_zone,select_shunt_from_zone
from DialogBox import getInput, openFile, openFolder, saveFile
from Create_Sub_Mon_Con_Files import createSubFile, createMonFile, createConFile
from gridSearch import CustomGridSearch
from ConnectDataBase import ConnectDatabase
from sourcePage import CustomGridSource
from loadPage import CustomGridLoad
from shuntPage import CustomGridShunt
from gridZone import CustomGridZone
from gridArea import CustomGridArea
from dynamicPage import CustomGridDyn
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
# import multiprocessing
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
ukNumShunt = 0
busNumber = 0
previousBusNumber = 0
count = 0
selectedZoneRow = 0
selectedZoneNum = 0

class CustomMyframe1(MyFrame1):
    def __init__ (self,parent):
        MyFrame1.__init__ (self,parent)
        self.Path = ''
        self.PathFile = [[]]
        self.parent = parent
        self.flagUpdate = 1
        self.flagReload = 0
        self.flagChangePPercent = 0
        self.flagChangeDeltaP = 0
        self.flagChangeNewPVal = 0
        self.flagRestriction = 0
        self.Count = 0
        self.indexInDyr = []
        self.gridBusInfoLink = ConnectDatabase(self)

    def Close_PSSE( self, event ):
        wx.MessageBox("Close PSSE Case ?")
        self.Close()

    def onClose( self, event ):
        for path in PATHFILE:
            # wx.MessageBox("remove {}".format(path))
            os.remove(path)
        event.Skip()
  
    def Open_PSSE( self, event ): 
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
        global fileInfoTranspose

        PATH_ORIGIN = openFile(self,'Please select .sav file', '*.sav')
        self.Path = PATH_ORIGIN
        fileName = os.path.basename(PATH_ORIGIN)
        dirName = r"D:/"
        # Assign value to grid
        myGridBus = self.gridSearch
        myGridFile = self.gridFile
        myGridArea = self.gridArea
        myGridZone = self.gridZone
        psspy.psseinit(2000)
        psspy.case(PATH_ORIGIN)


        if not PATH_ORIGIN in PATHFILE_ORIGIN: # first open this file
            PATHFILE_ORIGIN.append(PATH_ORIGIN)
            PATH = os.path.join(dirName,fileName[0:-4] + "-{}".format(len(PATHFILE_ORIGIN))+".sav") 
            # print("MEDIA PATH:",PATH)
            PATHFILE.append(PATH)
            psspy.save(PATH)
            # Open file with PSS/E
            # call(('cmd','/c','start','',PATH))
            # print("----------path is:",PATH)
            matrixArea.append(loadAreaInfo(PATH))
            matrixZone.append(loadZoneInfo(PATH))
            matrixBus.append(loadBusTab(PATH))
            matrixGen.append(loadMachineTab(PATH))
            matrixLoad.append(loadLoadTab(PATH))
            matrixShunt.append(loadShuntTab(PATH))
            # matrixBranch.append(loadBranchTab(PATH))
        else: # file exist
            fileIndex = PATHFILE_ORIGIN.index(PATH_ORIGIN)
            PATH = PATHFILE[fileIndex]
            # print("MEDIA PATH of exist file:",PATH)
            psspy.save(PATH)
            matrixArea[fileIndex] = loadAreaInfo(PATH)
            matrixZone[fileIndex] = loadZoneInfo(PATH)
            matrixBus[fileIndex] = loadBusTab(PATH)
            matrixGen[fileIndex] = loadMachineTab(PATH)
            matrixLoad[fileIndex] = loadLoadTab(PATH)
            matrixShunt[fileIndex] = loadShuntTab(PATH)

        fileIndex = PATHFILE.index(PATH)

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
         
        global areaList,zoneList
        areaList = currentMatrixArea[:,0]
        zoneList = currentMatrixZone[:,0]


        self.BusNumInput.SetItems(currentMatrixBus[:,0].tolist())

        if busNumber != 0:
            self.BusNumInput.SetValue(str(busNumber))

        if(indexFile>0): #reload all grid
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
                self.m_grid6.SetCellValue(row1,25,"")
                for column1 in range(self.m_grid6.GetNumberCols()):
                    self.m_grid6.SetCellValue(row1,column1,"")
            for row1 in range(self.gridShunt.GetNumberRows()):
                for column1 in range(self.gridShunt.GetNumberCols()):
                    self.gridShunt.SetCellValue(row1,column1,"")

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

        for row3 in range(len(currentMatrixGen)):
            toGenNumList.append(str(currentMatrixGen[row3,0]))
            
            for column3 in range(len(currentMatrixGen[0])):
                self.m_grid6.SetCellValue(row3,column3,str(currentMatrixGen[row3][column3]))

        for row3 in range(len(currentMatrixLoad)):
            for column3 in range(len(currentMatrixLoad[0])):
                self.gridLoad.SetCellValue(row3,column3,str(currentMatrixLoad[row3][column3]))

        for row3 in range(len(currentMatrixShunt)):
            for column3 in range(len(currentMatrixShunt[0])):
                self.gridShunt.SetCellValue(row3,column3,str(currentMatrixShunt[row3][column3]))
        # print("currentMatrixGen[i,0] :",currentMatrixGen[:,0])
        self.genNumber.SetItems(toGenNumList)

        self.PathFile = PATHFILE
        self.matrixBus = matrixBus  


    def busNumberEnter_Fcn( self, event ):
        # print('event in busNumberEnter_Fcn is:',event)
        # print(" self.BusNumInput.GetValue() in busNumberEnter: ",self.BusNumInput.GetValue())
        # try:
        global busNumber,previousBusNumber,matrixBranch
        busNumber = self.BusNumInput.GetValue()
        
        if busNumber in matrixBus[indexFile][:,0] :
            # print('matrixBus [{a}][:,0]: {b}'.format(a=indexFile,b=matrixBus[indexFile][:,0]))
            busInfo = select_bus_from_matrixBus(int(busNumber),matrixBus)

            self.BusNameInput.Label = busInfo[1]
            self.CodeInput.Label = busInfo[7]
            self.UdmInput.Label = busInfo[2]
            self.VoltageInput.Label = str(float(busInfo[8])*float(busInfo[2]))
            self.AreaInput.Label = busInfo[3]
            self.AreaNameInput.Label = busInfo[4]
            self.ZoneInput.Label = busInfo[5]
            self.ZoneNameInput.Label = busInfo[6]
            self.CosPInput.Label = busInfo[11]
            # gridBusInfo = ConnectDatabase(self)

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

            matrixBranch,matrix2Wind,matrix3Wind = self.gridBusInfoLink.loadBusNumberEnter(int(busNumber))

            global previousBusNumber

            [lineType] = self.gridBusInfoLink.SelectAllLineTypeByBusVoltage(busNumber)

            # celChoiceLines =wx.grid.GridCellChoiceEditor(lineType.tolist(),allowOthers=True)

            if int(busNumber)!=previousBusNumber:
                psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(busNumber)],0,[],0,[])
                ierr, busBaseKVOrigin = psspy.abusreal(0,2,'BASE')
                for row in range(self.gridBusInfo.GetNumberRows()):
                    for col in range(self.gridBusInfo.GetNumberCols()):
                        self.gridBusInfo.SetCellValue(row,col,'')
                            
                for row1 in range(len(matrixBranch)):
                    # celChoiceLines.Destroy()
                    # celChoiceLines =wx.grid.GridCellChoiceEditor(lineType.tolist(),allowOthers=True)
                    # self.gridBusInfo.SetCellEditor(row1,1,celChoiceLines)

                    for col1 in range(len(matrixBranch[0])):
                        self.gridBusInfo.SetCellValue(row1,col1,str(matrixBranch[row1][col1]))
                        self.gridBusInfo.SetCellTextColour(row1,col1,wx.Colour(0,0,0))
                busNumList = []
                for row in range (len(matrix3Wind)):
                    branchRowNum = len(matrixBranch)
                    psspy.bsys(0,0,[ 1.0, 500.],0,[],1,[int(matrix3Wind[row][2])],0,[],0,[])
                    ierr, busBaseKV = psspy.abusreal(0,2,'BASE')
                    if row % 2 ==0 and float(busBaseKV[0][0])>float(busBaseKVOrigin[0][0]):
                        busNumList.append(matrix3Wind[row][2])
                        busNumList.append(matrix3Wind[row][2])
                    elif row % 2 ==0 and float(busBaseKV[0][0])<float(busBaseKVOrigin[0][0]):
                        busNumList.append(busNumber)
                        busNumList.append(busNumber)
                    # celChoiceTrans.Destroy()
                    # celChoiceTrans = wx.grid.GridCellChoiceEditor(TransType.tolist(),allowOthers=True)
                    # self.gridBusInfo.SetCellEditor(row+branchRowNum,1,celChoiceTrans)
                    for col in range(len(matrix3Wind[0])):
                        self.gridBusInfo.SetCellValue(row+branchRowNum,col,str(matrix3Wind[row][col]))
                        self.gridBusInfo.SetCellTextColour(row+branchRowNum,col,wx.Colour(0,0,0))

                for index,busNum in enumerate(busNumList):
                    [TransType] = self.gridBusInfoLink.SelectAllTransTypeByBusVoltage(busNum)
                    # celChoiceTrans =wx.grid.GridCellChoiceEditor(TransType.tolist(),allowOthers=True)
                    # celChoiceTrans.Destroy()
                    # celChoiceTrans = wx.grid.GridCellChoiceEditor(TransType.tolist(),allowOthers=True)
                    # self.gridBusInfo.SetCellEditor(index+len(matrixBranch),1,celChoiceTrans)

                [trans2Type,R,X,Rate,R01,X01] = self.gridBusInfoLink.SelectAllTrans2WindType()
                for row in range (len(matrix2Wind)):
                    CurrentRowNum = len(matrixBranch)+len(matrix3Wind)
                    for col in range(len(matrix2Wind[0])):
                        # celChoiceTrans2 =wx.grid.GridCellChoiceEditor(trans2Type.tolist(),allowOthers=True)
                        # celChoiceTrans2.Destroy()
                        # celChoiceTrans2 = wx.grid.GridCellChoiceEditor(trans2Type.tolist(),allowOthers=True)
                        # self.gridBusInfo.SetCellEditor(row+CurrentRowNum,1,celChoiceTrans2)
                        self.gridBusInfo.SetCellValue(row+CurrentRowNum,col,str(matrix2Wind[row][col]))
                        self.gridBusInfo.SetCellTextColour(row+CurrentRowNum,col,wx.Colour(0,0,0))

                for row2 in range(len(matrixBranch)+len(matrix2Wind)+len(matrix3Wind)):
                    if  self.gridBusInfo.GetCellValue(row2,8) != 'N/A' and float(self.gridBusInfo.GetCellValue(row2,8))>=100:
                        self.gridBusInfo.SetCellTextColour(row2,8, wx.RED)

            previousBusNumber = busNumber

        else:
            event.Skip()

    def on_selected_cell_grid_bus( self, event ):
        # try:
        # gridBusInfo = ConnectDatabase(self)
        self.gridBusInfoLink.on_selected_cell_grid_bus(event)
        event.Skip()

    def on_cell_change_grid_bus( self, event ):
        # gridBusInfo = ConnectDatabase(self)
        self.gridBusInfoLink.on_cell_change_grid_bus(event)
        event.Skip()


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = CustomMyframe1(None)
    frame.SetIcon(wx.Icon("icon4.png"))
    frame.Show(True)
    app.MainLoop()

