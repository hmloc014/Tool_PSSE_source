Option Explicit
Public Sub Convert_xData()
    Debug.Print "________________Convert_xData"
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim lbl As String
    Call ReadP2CFile
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            Select Case TypeName(obj)
                Case appLod
                    'Call cnvLoad(obj)
                Case appMac
                    'Call cnvMac2(obj)
                Case appPMac
                    'Call cnvMac(obj)
                Case appBrn
                    obj.TextString = StrBrn(obj, "number")
                    Call cnvBrn2(obj)
                Case appPBrn
                    Call cnvPBrn(obj)
                    obj.TextString = StrPbrn(obj, "number")
                    Call cnvPBrn2(obj)
                    
                Case "PTRANS_DATA"
                    Call cnvTrans(obj)
                Case appTrans
                    Call cnvTrans2(obj)
            End Select
        End If
    Next
End Sub
Private Sub cnvBrn2(obj As ZcadText)
Debug.Print "________________cnvBrn2"
    Dim copyObj As ZcadText
    Dim str As Variant
    Set copyObj = ThisDrawing.ModelSpace.AddText(obj.TextString, obj.InsertionPoint, obj.Height)
    copyObj.Alignment = obj.Alignment
    copyObj.InsertionPoint = obj.InsertionPoint
    copyObj.Rotation = obj.Rotation
    copyObj.Layer = obj.Layer
    On Error Resume Next
    copyObj.TextAlignmentPoint = obj.TextAlignmentPoint
              
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 3) As Integer
    Dim xData2(0 To 3) As Variant
    
    xtypeLBL(0) = 1001: xdataLBL(0) = appType
    xtypeLBL(1) = 1000: xdataLBL(1) = appPBrn
    copyObj.SetXData xtypeLBL, xdataLBL
    str = VBA.Split(obj.TextString, ".")
    
    xType2(0) = 1001: xData2(0) = appPBrn
    xType2(1) = 1040: xData2(1) = CDbl(str(0))
    xType2(2) = 1040: xData2(2) = CDbl(str(1))
    xType2(3) = 1040: xData2(3) = str(2)
    copyObj.SetXData xType2, xData2
    obj.Delete
End Sub
Private Sub cnvPBrn2(obj As ZcadText)
Debug.Print "________________cnvPBrn2"
    Dim copyObj As ZcadText
    Dim str As Variant
    Set copyObj = ThisDrawing.ModelSpace.AddText(obj.TextString, obj.InsertionPoint, obj.Height)
    copyObj.Alignment = obj.Alignment
    copyObj.InsertionPoint = obj.InsertionPoint
    copyObj.Rotation = obj.Rotation
    copyObj.Layer = obj.Layer
    On Error Resume Next
    copyObj.TextAlignmentPoint = obj.TextAlignmentPoint
                
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 2) As Integer
    Dim xData2(0 To 2) As Variant
    
    xtypeLBL(0) = 1001: xdataLBL(0) = appType
    xtypeLBL(1) = 1000: xdataLBL(1) = appPBrn
    copyObj.SetXData xtypeLBL, xdataLBL
    str = VBA.Split(obj.TextString, ".")
    
    xType2(0) = 1001: xData2(0) = appPBrn
    xType2(1) = 1040: xData2(1) = CDbl(str(0))
    xType2(2) = 1040: xData2(2) = CDbl(str(1))
    copyObj.SetXData xType2, xData2
    obj.Delete
End Sub
Private Sub cnvPBrn(obj As ZcadText)
Debug.Print "________________cnvPBrn"
    Dim xDataType As Variant
    Dim xData As Variant
    Dim ibus As Long
    Dim jbus As Long
    Dim xType2(0 To 2) As Integer
    Dim xData2(0 To 2) As Variant

    obj.GetXData appPBrn, xDataType, xData
    ibus = CLng(xData(2))
    jbus = CLng(xData(3))
    
    xType2(0) = 1001: xData2(0) = appPBrn
    xType2(1) = 1040: xData2(1) = ibus
    xType2(2) = 1040: xData2(2) = jbus
    obj.SetXData xType2, xData2
End Sub
Private Sub cnvTrans(obj As ZcadText)
Debug.Print "________________cnvTrans"
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    xtypeLBL(0) = 1001: xdataLBL(0) = appType
    xtypeLBL(1) = 1000: xdataLBL(1) = appTrans
    obj.SetXData xtypeLBL, xdataLBL

    Dim xDataType As Variant
    Dim xData As Variant
    Dim ibus As Long
    obj.GetXData "PTRANS_DATA", xDataType, xData
    ibus = CLng(xData(2))
        
    Dim xType2(0 To 1) As Integer
    Dim xData2(0 To 1) As Variant
    xType2(0) = 1001: xData2(0) = appTrans
    xType2(1) = 1040: xData2(1) = ibus
    obj.SetXData xType2, xData2
End Sub

Private Sub cnvTrans2(obj As ZcadText)
    Debug.Print "________________cnvTrans2"
    Dim copyObj As ZcadText
    Set copyObj = ThisDrawing.ModelSpace.AddText(obj.TextString, obj.InsertionPoint, obj.Height)
    copyObj.Alignment = obj.Alignment
    copyObj.InsertionPoint = obj.InsertionPoint
    copyObj.Rotation = obj.Rotation
    copyObj.Layer = obj.Layer
    On Error Resume Next
    copyObj.TextAlignmentPoint = obj.TextAlignmentPoint
           
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    
    xtypeLBL(0) = 1001: xdataLBL(0) = appType
    xtypeLBL(1) = 1000: xdataLBL(1) = appTrans
    copyObj.SetXData xtypeLBL, xdataLBL
    
    Dim xDataType As Variant
    Dim xData As Variant
    obj.GetXData appTrans, xDataType, xData
    copyObj.SetXData xDataType, xData
    
    obj.Delete
End Sub

Private Sub cnvLoad(obj As ZcadText)
Debug.Print "________________cnvLoad"
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xType2(0 To 1) As Integer
    Dim xData2(0 To 1) As Variant
    Dim number As Long
    
    obj.GetXData appLod, xDataType, xData
    If VarType(xDataType) <> vbEmpty Then
        number = CLng(xData(1))
        xType2(0) = 1001: xData2(0) = appLod
        xType2(1) = 1040: xData2(1) = number
        obj.SetXData xType2, xData2
    End If
    
End Sub


Private Sub cnvMac(obj As ZcadText)
Debug.Print "________________cnvMac"
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 1) As Integer
    Dim xData2(0 To 1) As Variant
    
    xtypeLBL(0) = 1001: xdataLBL(0) = appType
    xtypeLBL(1) = 1000: xdataLBL(1) = appMac
    obj.SetXData xtypeLBL, xdataLBL
    
    Dim xDataType As Variant
    Dim xData As Variant
    obj.GetXData appPMac, xDataType, xData
    xData(0) = appMac
    xData(1) = xData(1) + 1
    obj.SetXData xDataType, xData
    
End Sub

Private Sub cnvMac2(obj As ZcadText)
Debug.Print "________________cnvMac2"
    Dim copyObj As ZcadText

    Dim xDataType As Variant
    Dim xData As Variant
    obj.GetXData appMac, xDataType, xData
        
    Set copyObj = ThisDrawing.ModelSpace.AddText(obj.TextString, obj.InsertionPoint, obj.Height)
    copyObj.Alignment = obj.Alignment
    copyObj.InsertionPoint = obj.InsertionPoint
    copyObj.Rotation = obj.Rotation
    copyObj.Layer = obj.Layer
    'On Error Resume Next
    copyObj.TextAlignmentPoint = obj.TextAlignmentPoint
    
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 1) As Integer
    Dim xData2(0 To 1) As Variant
    
    xtypeLBL(0) = 1001: xdataLBL(0) = appType
    xtypeLBL(1) = 1000: xdataLBL(1) = appMac
    copyObj.SetXData xtypeLBL, xdataLBL

    copyObj.SetXData xDataType, xData
    obj.Delete
End Sub
