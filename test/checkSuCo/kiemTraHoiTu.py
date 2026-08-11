
import glob, os, sys
import pssepath
import wx
import wx.xrc
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
from subprocess import call
from redirectOuput import silence


def openFile(parent= None, message='', wildcard =''): 
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE
    dialog = wx.FileDialog(parent,
                            message = message,
                            wildcard = wildcard,
                            style =  style)
    if dialog.ShowModal() == wx.ID_OK:
        paths = dialog.GetPaths()
        filePath = paths[0]  
    else:
        paths = None
    dialog.Destroy()
    return filePath

def openFolder(parent= None, message=''): 
    dlg = wx.DirDialog(parent, message=message)

    if dlg.ShowModal() == wx.ID_OK:
        dirname = dlg.GetPath()
    dlg.Destroy()

    return dirname

def Run_Multi_Macro_Fcn( self, event ):
        
        savFile = openFile(self,'Please select .sav file', '*.sav')
        dirNamePy = openFolder(self,"Choose the folder contain all py files." )
        os.chdir(dirNamePy)
        pyfileNames = glob.glob('*.py')

        for pyFile in pyfileNames:
            print(pyyFile )
            psspy.psseinit(2000)
            psspy.case(savFile)
            outFile = '{}.txt'.format(pyFile)
            with open(outFile, 'w') as f, silence(f):
                execfile(pyFile)
            r = open(outFile,'r')
            lines = r.readlines()
            finalLine =len(lines)
            print(finalLine)

            if "not" in lines[finalLine-1]:
                print(lines[finalLine-1])
                print('----------Su co {} Khong hoi tu'.format(pyFile))
            else: 
                print('Su co {} hoi tu'.format(pyFile))

            r.close()
            f.close()
            os.remove(pyFile[:-4]+'.out')

