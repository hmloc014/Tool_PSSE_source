# -*- coding: utf-8 -*- 
import wx


def getInput(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result

# dialog mở file
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

# dialog mở nhiều file cùng lúc
def openMultipleFile(parent= None, message='', wildcard =''): 
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE
    dialog = wx.FileDialog(parent,
                            message = message,
                            wildcard = wildcard,
                            style =  style)
    if dialog.ShowModal() == wx.ID_OK:
        paths = dialog.GetPaths()
    #     filePath = paths[0]  
    # else:
    #     paths = None
    dialog.Destroy()
    return paths

# Dialog lưu file
def saveFile(parent= None, message='', wildcard ='', dDir = '',dFile='' ): 
    style = wx.SAVE | wx.OVERWRITE_PROMPT
    dialog = wx.FileDialog(parent, 
                message = message,
                defaultDir = dDir,
                defaultFile = dFile,
                wildcard = wildcard,
                style = style)
    if dialog.ShowModal() == wx.ID_OK:
        outPaths = dialog.GetPaths()
        outFilePath = outPaths[0]
        outputPath = outFilePath
    else:
        outPaths = None
    dialog.Destroy()
    return outputPath

# Dialog mở thư mục
def openFolder(parent= None, message=''): 
    dlg = wx.DirDialog(parent, message=message)

    if dlg.ShowModal() == wx.ID_OK:
        dirname = dlg.GetPath()
    dlg.Destroy()

    return dirname