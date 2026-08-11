Option Explicit

Sub testbus()
'On Error GoTo Ext
    Call ReadP2CFile
    Call Set_xData_To_Bus
    
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS3")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    MsgBox StrBus(sset.Item(0), "number") + vbCrLf + _
    StrBus(sset.Item(0), "name") + vbCrLf + _
    StrBus(sset.Item(0), "kv") + vbCrLf + _
    StrBus(sset.Item(0), "pu") + vbCrLf
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
End Sub
Sub testload()
'On Error GoTo Ext
    Call ReadP2CFile
    Call Set_xData_To_Load
    
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS3")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    MsgBox StrBus(sset.Item(0), "number") + vbCrLf + _
    StrLoad(sset.Item(0), "name") + vbCrLf + _
    StrLoad(sset.Item(0), "pq") + vbCrLf
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
End Sub
Sub testmac()
'On Error GoTo Ext
    Call ReadP2CFile
    Call Set_xData_To_Mac
    
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS3")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    MsgBox StrMac(sset.Item(0), "number") + vbCrLf + _
    StrMac(sset.Item(0), "name") + vbCrLf + _
    StrMac(sset.Item(0), "rate") + vbCrLf + _
    StrMac(sset.Item(0), "pf") + vbCrLf + _
    StrMac(sset.Item(0), "pq") + vbCrLf
            
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
End Sub

Sub testbrn()
'On Error GoTo Ext
    Call ReadP2CFile
    Call Set_xData_To_Branch
    
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS3")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    MsgBox StrBrn(sset.Item(0), "number") + vbCrLf + _
    StrBrn(sset.Item(0), "pq") + vbCrLf + _
    StrBrn(sset.Item(0), "params") + vbCrLf + _
    StrBrn(sset.Item(0), "rate") + vbCrLf
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
End Sub

Sub testpbrn()
'On Error GoTo Ext

    'Call Set_xData_To_PBranch
    
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS3")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    MsgBox StrPbrn(sset.Item(0), "number") + vbCrLf + _
    StrPbrn(sset.Item(0), "pq") + vbCrLf + _
    StrPbrn(sset.Item(0), "params") + vbCrLf + _
    StrPbrn(sset.Item(0), "rate") + vbCrLf
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
End Sub

Sub testtrans()
'On Error GoTo Ext
    Call ReadP2CFile
    
    
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("S0")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    MsgBox StrTrans(sset.Item(0), "number") + vbCrLf + _
    StrTrans(sset.Item(0), "pq") + vbCrLf + _
    StrTrans(sset.Item(0), "rate") + vbCrLf + _
    StrTrans(sset.Item(0), "params") + vbCrLf

    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
End Sub

Sub testdata()
    Dim i As Integer
    Dim found As String
    found = "OK"
    
    For i = 1 To nBus - 1
        If BusAr(i).number > BusAr(i + 1).number Then
            ThisDrawing.Utility.Prompt (CStr(BusAr(i).number) + "----")
            found = "Error"
        End If
    Next
    
    For i = 1 To nBus - 1
        If BusAr(i).number > BusAr(i + 1).number Then
            ThisDrawing.Utility.Prompt (CStr(BusAr(i).number) + "----")
            found = "Error"
        End If
    Next
    MsgBox found
End Sub
Sub test1()
'On Error GoTo Ext

    
    Dim obj As ZcadMText
    Dim txt As ZcadText
    Dim str As Variant
    Dim dat As String
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("S2")
    FilType(0) = 0
    FilData(0) = "MText"
    sset.SelectOnScreen FilType, FilData
    Set obj = sset.Item(0)
    If Not sset Is Nothing Then
        sset.Delete
    End If
    MsgBox obj.TextString
    str = VBA.Split(obj.TextString, ";")
    dat = VBA.Left(str(1), Len(str(1)) - 1)
    Set txt = ThisDrawing.ModelSpace.AddText(dat, obj.InsertionPoint, obj.Height)
    
    txt.Alignment = acAlignmentMiddleCenter
    txt.Rotation = obj.Rotation
    
    

    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If

End Sub

