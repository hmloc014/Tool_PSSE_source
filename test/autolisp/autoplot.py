Sub Example_PrinterConfigPath()
    ' This example reads and modifies the preference value that controls
    ' the location for printer configuration files.
    ' When finished, this example resets the preference value back to
    ' its original value.
    
    Dim ZcadPref As ZcadPreferencesFiles
    Dim originalValue As Variant, newValue As Variant
    
    ' Get the files preferences object
    Set ZcadPref = ThisDrawing.Application.Preferences.Files
    
    ' Read and display the original value
    originalValue = ZcadPref.PrinterConfigPath
    MsgBox "The PrinterConfigPath preference is set to: " & originalValue

    ' Modify the PrinterConfigPath preference by changing the path to "C:\"
    ZcadPref.PrinterConfigPath = "C:\"
    newValue = ZcadPref.PrinterConfigPath
    MsgBox "The PrinterConfigPath preference has been set to: " & newValue

    ' Reset the preference back to its original value
    '
    ' * Note: Comment out this last section to leave the change to
    '         this preference in effect
    ZcadPref.PrinterConfigPath = originalValue
    MsgBox "The PrinterConfigPath preference was reset back to: " & originalValue
End Sub
Public Sub AutoPlot()
    ' Verify that the active space is model space
    If ThisDrawing.ActiveSpace = acPaperSpace Then
        ThisDrawing.MSpace = True
        ThisDrawing.ActiveSpace = acModelSpace
    End If
    
    ' Chon net
    Dim ZcadPref As ZcadPreferencesOutput
    Set ZcadPref = ThisDrawing.Application.Preferences.Output
    Dim PlotTable As String
    PlotTable = "C:\Documents and Settings\tuna\Application Data\Autodesk\AutoCAD 2009\R17.2\enu\Plot Styles\"
    PlotTable = PlotTable + "Zcad.ctb"
    ZcadPref.DefaultPlotStyleTable = PlotTable
    
    ' Set the extents and scale of the plot area
    ThisDrawing.ModelSpace.Layout.PlotType = acExtents
    
    ThisDrawing.ModelSpace.Layout.StandardScale = acScaleToFit
    ThisDrawing.ModelSpace.Layout.CenterPlot = True
    'ThisDrawing.ModelSpace.Layout.ConfigName = "\\Loanrole\HP LaserJet 1160"
    ThisDrawing.ModelSpace.Layout.ConfigName = "HP LaserJet 1320 PCL 6"
    'ThisDrawing.ModelSpace.Layout.ConfigName = "\\Hopdt\HP LaserJet 1320 PCL 6"
    ThisDrawing.ModelSpace.Layout.PlotWithPlotStyles = True
    ThisDrawing.ModelSpace.Layout.PlotWithLineweights = True
    
    ' Set the number of copies to one
    ThisDrawing.Plot.NumberOfCopies = 1

    ' Initiate the plot
    ThisDrawing.Plot.PlotToDevice


End Sub

Sub Example_DefaultPlotStyleTable()
    ' This example reads and modifies the preference value that
    ' specifies the default plot style table to attach to new drawings.
    '
    ' Note: You may want to change the path of the new plot style table below.
    
    

End Sub

