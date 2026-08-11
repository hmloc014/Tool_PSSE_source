Option Explicit
Dim Excel  As Excel.Application
    Dim ExcelSheet As Object
    Dim ExcelWorkbook As Object

Public Sub ToExcel()
    
    Dim eB(1 To 2000) As ZcadText
    Dim cB(1 To 2000) As Integer
    Dim eT(1 To 2000) As ZcadText
    Dim cT(1 To 2000) As Integer
    Dim obj As ZcadObject
    Dim nB As Integer, nT As Integer
    Dim xDataType As Variant
    Dim xData As Variant
    Dim i As Integer, j As Integer


    

    Dim str() As String
    Dim ibus As Long, jbus As Long
    Dim iname As String, jname As String
    Dim idx As Integer, jdx As Integer
    Dim Header As Boolean
    Dim txt As ZcadText

    Dim sNumber As String
    Dim sPQ As String
    Dim sRate As String

    
    '   Liet ke cac nhanh va MBA can xuat ket qua
    nB = 0
    nT = 0
    For Each obj In ThisDrawing.ModelSpace
        If (TypeName(obj) = appPBrn) _
        Or (TypeName(obj) = appBrn) _
        Or (TypeName(obj) = appMBrn) Then
            obj.GetXData appExcel, xDataType, xData
            If VarType(xDataType) <> vbEmpty Then
                nB = nB + 1
                cB(nB) = CLng(xData(1))
                Set eB(nB) = obj
                eB(nB).TextString = cB(nB)
            End If
        End If
        If (TypeName(obj) = appTrans) Then
            obj.GetXData appExcel, xDataType, xData
            If VarType(xDataType) <> vbEmpty Then
                nT = nT + 1
                Set eT(nT) = obj
                cT(nT) = CLng(xData(1))
                eT(nT).TextString = cT(nT)
            End If
        End If
    Next
    
    ' read psse data
    Call ReadP2CFile
    On Error Resume Next
    Dim cont As Integer
    cont = Excel.Workbooks.Count
    If cont > 0 Then
        Excel.Visible = True
        For i = 1 To 50
            For j = 1 To 5
                ExcelSheet.Cells(i, j).Value = ""
            Next
        Next
    Else
        Set Excel = New Excel.Application
        Set ExcelWorkbook = Excel.Workbooks.Open("c:\LoadFlow.xls")
        Set ExcelSheet = Excel.ActiveSheet
        Excel.Visible = True
    End If
    
    For i = 1 To nB
        Select Case TypeName(eB(i))
            Case appPBrn
                sNumber = StrPbrn(eB(i), "number")
                sPQ = StrPbrn(eB(i), "pq")
                sRate = StrPbrn(eB(i), "rate")
            Case appBrn
                sNumber = StrBrn(eB(i), "number")
                sPQ = StrBrn(eB(i), "pq")
                sRate = StrBrn(eB(i), "rate")
            Case appMBrn
                sNumber = StrMBrn(eB(i), "number")
                sPQ = StrMBrn(eB(i), "pq")
                sRate = StrMBrn(eB(i), "rate")
        End Select
                
        str = VBA.Split(sNumber, ".")
        ibus = CLng(str(0)): jbus = CLng(str(1))
        idx = BusIndex(ibus): jdx = BusIndex(jbus)
        iname = BusAr(idx).Name: jname = BusAr(jdx).Name
        ExcelSheet.Cells(cB(i), 1).Value = iname
        ExcelSheet.Cells(cB(i), 2).Value = jname
        ExcelSheet.Cells(cB(i), 3).Value = sPQ
        
        sRate = VBA.Left(sRate, VBA.Len(sRate) - 3)
        str = VBA.Split(sRate, "/")
        ExcelSheet.Cells(cB(i), 4).Value = str(0)
        If UBound(str) >= 1 Then
            ExcelSheet.Cells(cB(i), 5).Value = str(1)
        End If
         
    Next
    
    For i = 1 To nT
        ibus = CLng(StrTrans(eT(i), "number"))
        idx = BusIndex(ibus)
        iname = BusAr(idx).Name
        ExcelSheet.Cells(cT(i), 1).Value = iname
        ExcelSheet.Cells(cT(i), 3).Value = StrTrans(eT(i), "pq")
        sRate = StrTrans(eT(i), "rate")
        sRate = VBA.Left(sRate, VBA.Len(sRate) - 3)
        str = VBA.Split(sRate, "/")
        ExcelSheet.Cells(cT(i), 4).Value = str(0)
        If UBound(str) >= 1 Then
            ExcelSheet.Cells(cT(i), 5).Value = str(1)
        End If
    Next
    ExcelSheet.Cells(1, 6).Value = ThisDrawing.Name
    

ext:

End Sub
Public Sub ViewMacBus()
'On Error GoTo ext
'If Not ViewEnable Then GoTo ext

    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim i As Long
    
    AutoEnable = False
    
    Call ReadP2CFile
    
    i = ThisDrawing.Utility.GetInteger( _
        "Enter code: 1=BusNumber; 2=MacNumber; 3=MacName; 4=PQTrans; 5=PQGen; 6=Pgen/Pmax; 7=params " + vbCrLf)
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            If TypeName(obj) = appMacBus Then
                Select Case i
                    Case 1
                        obj.TextString = StrMacBus(obj, "busnumber")
                    Case 2
                        obj.TextString = StrMacBus(obj, "macnumber")
                    Case 3
                        obj.TextString = StrMacBus(obj, "macname")
                    Case 4
                        obj.TextString = StrMacBus(obj, "pqtrans")
                    Case 5
                        obj.TextString = StrMacBus(obj, "pqgen")
                    Case 6
                        obj.TextString = StrMacBus(obj, "Rate")
                    Case 7
                        obj.TextString = StrMacBus(obj, "params")
                    Case Else
                End Select
            End If
        End If
    Next
    
ext:
    AutoEnable = True
End Sub

Public Sub ViewBus()
'On Error GoTo ext
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim i As Long
    'If Not ViewEnable Then GoTo ext
    AutoEnable = False
    Call ReadP2CFile
    i = ThisDrawing.Utility.GetInteger("Enter code: 1=Number; 2=Name; 3=KV; 4=PU" + vbCrLf)
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            If TypeName(obj) = appBus Then
                Select Case i
                    Case 1
                        obj.TextString = StrBus(obj, "number")
                    Case 2
                        obj.TextString = StrBus(obj, "name")
                    Case 3
                        obj.TextString = StrBus(obj, "kv")
                    Case 4
                        obj.TextString = StrBus(obj, "pu")
                End Select
            End If
        End If
    Next
    
ext:
    AutoEnable = True
End Sub
Public Sub ViewLoad()
'On Error GoTo ext
AutoEnable = False
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim i As Long
    
    Call ReadP2CFile
    i = ThisDrawing.Utility.GetInteger("Enter code: 1=Number; 2=Name; 3=PQ" + vbCrLf)
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            If TypeName(obj) = appLod Then
                Select Case i
                    Case 1
                        obj.TextString = StrLoad(obj, "number")
                    Case 2
                        obj.TextString = StrLoad(obj, "name")
                    Case 3
                        obj.TextString = StrLoad(obj, "pq")
                End Select
            End If
        End If
    Next
AutoEnable = True
End Sub


Public Sub ViewMac()
'On Error GoTo ext
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim i As Long
    AutoEnable = False
    Call ReadP2CFile
    i = ThisDrawing.Utility.GetInteger("Enter code: 1=Number; 2=Name; 3=PQ; 4=Rate; 5=PF; 6=Params" + vbCrLf)
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            If TypeName(obj) = appMac Then
                Select Case i
                    Case 1
                        obj.TextString = StrMac(obj, "number")
                    Case 2
                        obj.TextString = StrMac(obj, "name")
                    Case 3
                        obj.TextString = StrMac(obj, "pq")
                    Case 4
                        obj.TextString = StrMac(obj, "rate")
                    Case 5
                        obj.TextString = StrMac(obj, "pf")
                    Case 6
                        obj.TextString = StrMac(obj, "params")
                End Select
                
            End If
        End If
    Next
ext:
AutoEnable = True
End Sub

Public Sub ViewBranch()
'On Error GoTo ext
    ''If Not ViewEnable Then GoTo ext
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim i As Long
    'If Not ViewEnable Then GoTo ext
    AutoEnable = False
    Call ReadP2CFile
    i = ThisDrawing.Utility.GetInteger("Enter code: 1=Number; 2=PQ; 3=Rate; 4=Params" + vbCrLf)
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            If TypeName(obj) = appPBrn Then
                Select Case i
                    Case 1
                        obj.TextString = StrPbrn(obj, "number")
                    Case 2
                        obj.TextString = StrPbrn(obj, "pq")
                    Case 3
                        obj.TextString = StrPbrn(obj, "rate")
                    Case 4
                        obj.TextString = StrPbrn(obj, "params")
                End Select
            Else
                If TypeName(obj) = appBrn Then
                Select Case i
                    Case 1
                        obj.TextString = StrBrn(obj, "number")
                    Case 2
                        obj.TextString = StrBrn(obj, "pq")
                    Case 3
                        obj.TextString = StrBrn(obj, "rate")
                    Case 4
                        obj.TextString = StrBrn(obj, "params")
                End Select
                End If
            End If
        End If
    Next
ext:
AutoEnable = True
End Sub

Public Sub ViewTrans()
'On Error GoTo ext
    'If Not ViewEnable Then GoTo ext
    
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim i As Long
    AutoEnable = False
    Call ReadP2CFile
    i = ThisDrawing.Utility.GetInteger("Enter code: 1=Number; 2=PQ; 3=Rate; 4=Params" + vbCrLf)
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            If TypeName(obj) = appTrans Then
                Select Case i
                    Case 1
                        obj.TextString = StrTrans(obj, "number")
                    Case 2
                        obj.TextString = StrTrans(obj, "pq")
                    Case 3
                        obj.TextString = StrTrans(obj, "rate")
                    Case 4
                        obj.TextString = StrTrans(obj, "params")
                End Select
                
            End If
        End If
    Next
ext:
    AutoEnable = True
End Sub
Public Sub KeyGen()
    Dim Val As Integer
    Open DayFile For Input As 1
    Input #1, Val
    Close #1
    printx CStr(DayValue - 5)
    printx DayValue
    printx CStr(DayValue + 5)
    
    If Val = DayValue Then
        ViewEnable = True
    End If
    
End Sub
Public Sub ViewAll()
'On Error GoTo ext
    ''If Not ViewEnable Then GoTo ext
    AutoEnable = False
    Dim i As Integer
    Call ReadP2CFile
    On Error Resume Next
    i = ThisDrawing.Utility.GetInteger _
        ("Enter code: 1=Number; 2=PQ; 3=Rate; 4=Params" + vbCrLf)
    Select Case i
        Case 1
            Call ViewNumber
        Case 2
            Call ViewPQ
        Case 3
            Call ViewRate
        Case 4
            Call ViewParams
    End Select
ext:
    AutoEnable = True
End Sub
Public Sub ViewNumber()
'On Error GoTo ext
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim lbl As String
    Call ReadP2CFile
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            lbl = TypeName(obj)
            Select Case lbl
                Case appBus
                    obj.TextString = StrBus(obj, "number")
                Case appLod
                    obj.TextString = StrLoad(obj, "number")
                Case appMac
                    obj.TextString = StrMac(obj, "number")
                Case appMacBus
                    obj.TextString = StrMacBus(obj, "busnumber")
                Case appBrn
                    obj.TextString = StrBrn(obj, "number")
                Case appMBrn
                    obj.TextString = StrMBrn(obj, "number")
                Case appPBrn
                    obj.TextString = StrPbrn(obj, "number")
                Case appTrans
                    obj.TextString = StrTrans(obj, "number")
                    
            End Select
        End If
    Next
ext:
End Sub
Public Sub ViewPQ()
'On Error GoTo ext
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim lbl As String
    Call ReadP2CFile
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            lbl = TypeName(obj)
            Select Case lbl
                Case appBus
                    obj.TextString = StrBus(obj, "KV")
                Case appLod
                    obj.TextString = StrLoad(obj, "PQ")
                Case appMac
                    obj.TextString = StrMac(obj, "PQ")
                Case appBrn
                    obj.TextString = StrBrn(obj, "pq")
                Case appMBrn
                    obj.TextString = StrMBrn(obj, "pq")
                Case appPBrn
                    obj.TextString = StrPbrn(obj, "pq")
                Case appTrans
                    obj.TextString = StrTrans(obj, "pq")
                Case appMacBus
                    obj.TextString = StrMacBus(obj, "pqtrans")
            End Select
        End If
    Next
ext:
End Sub
Public Sub ViewRate()
'On Error GoTo ext
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim lbl As String
    Call ReadP2CFile
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            lbl = TypeName(obj)
            Select Case lbl
                Case appBus
                    obj.TextString = StrBus(obj, "pu")
                Case appLod
                    obj.TextString = StrLoad(obj, "PQ")
                Case appMac
                    obj.TextString = StrMac(obj, "rate")
                Case appBrn
                    obj.TextString = StrBrn(obj, "rate")
                Case appMBrn
                    obj.TextString = StrMBrn(obj, "rate")
                Case appPBrn
                    obj.TextString = StrPbrn(obj, "rate")
                Case appTrans
                    obj.TextString = StrTrans(obj, "rate")
                Case appMacBus
                    obj.TextString = StrMacBus(obj, "rate")
            End Select
        End If
    Next
ext:
End Sub

Public Sub ViewParams()
'On Error GoTo ext
    Dim obj As ZcadText
    Dim ent As ZcadObject
    Dim lbl As String
    Call ReadP2CFile
    For Each ent In ThisDrawing.ModelSpace
        If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
            Set obj = ent
            lbl = TypeName(obj)
            Select Case lbl
                Case appBus
                    obj.TextString = StrBus(obj, "number")
                Case appLod
                    obj.TextString = StrLoad(obj, "number")
                Case appMac
                    obj.TextString = StrMac(obj, "params")
                Case appBrn
                    obj.TextString = StrBrn(obj, "params")
                Case appMBrn
                    obj.TextString = StrMBrn(obj, "params")
                Case appPBrn
                    obj.TextString = StrPbrn(obj, "params")
                Case appTrans
                    obj.TextString = StrTrans(obj, "params")
                Case appMacBus
                    obj.TextString = StrMacBus(obj, "params")
            End Select
        End If
    Next
ext:
End Sub
Private Function DayValue() As Long
    Dim str As Variant
    str = VBA.Split(VBA.Date, "/")
    DayValue = Factor * CLng(str(1))
End Function

Public Sub TocadToolbar()

'On Error GoTo Ext
    
    Dim ToolbarName As String
    Dim ToolbarFound As Integer
    Dim currMenuGroup As ZcadMenuGroup
    Set currMenuGroup = ThisDrawing.Application.MenuGroups.Item(0)
    Dim i As Integer
    ToolbarName = "ToCadToolbar (TuNa-PECC1)"
    
    
    ' Create the new toolbar
    ToolbarFound = False
    Dim newToolbar As ZcadToolbar
    For i = 0 To currMenuGroup.Toolbars.Count - 1
        Set newToolbar = currMenuGroup.Toolbars.Item(i)
        If newToolbar.Name = ToolbarName Then
            'newToolbar.Delete
            ToolbarFound = True
        End If
    Next
    
    If Not ToolbarFound Then
        Set newToolbar = currMenuGroup.Toolbars.Add(ToolbarName)
        ' Add a button to the new toolbar
        Dim newButton As ZcadToolbarItem
        Dim CommandString As String
        Dim SmallBitmap As String
        Dim LargeBitmap As String
        
                
        ' LOAD_PSSE
        CommandString = "Import_PSSE_Data" + Chr(13)
        SmallBitmap = "IMPORT_DATA.BMP"
        LargeBitmap = "IMPORT_DATA.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "IMPORT PSS/E", "IMPORT PSS/E", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' View bus data
        CommandString = "ViewBus" + Chr(13)
        SmallBitmap = "Bus_Data.bmp"
        LargeBitmap = "Bus_Data.bmp"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "View bus", "Bus bus", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' View load data
        CommandString = "ViewLoad" + Chr(13)
        SmallBitmap = "Load_Data.bmp"
        LargeBitmap = "Load_Data.bmp"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "View load", "View load", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' View machine data
        CommandString = "ViewMac" + Chr(13)
        SmallBitmap = "Mac_Data.BMP"
        LargeBitmap = "Mac_Data.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "View generator", "View generator", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' View branch data
        CommandString = "ViewBranch" + Chr(13)
        SmallBitmap = "Branch_Data.BMP"
        LargeBitmap = "Branch_Data.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "View branch", "View branch", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' View transformer data
        CommandString = "ViewTrans" + Chr(13)
        SmallBitmap = "Trans_Data.BMP"
        LargeBitmap = "Trans_Data.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "View Transformer", "View Transformer", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' View all data
        CommandString = "ViewAll" + Chr(13)
        SmallBitmap = "All_Data.BMP"
        LargeBitmap = "All_Data.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "View All", "View All", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        

        '*****************************************************************
        Set newButton = newToolbar.AddSeparator(7)
        '*****************************************************************
        
        ' KIEM TRA CAC TEXT CO NOI DUNG TRUNG NHAU
        CommandString = "OVL" + Chr(13)
        SmallBitmap = "CHECK_OVERLOAD.BMP"
        LargeBitmap = "CHECK_OVERLOAD.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "CHECK OVERLOAD", _
                       "CHECK OVERLOAD", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' KIEM TRA QUA TAI
        CommandString = "DBT" + Chr(13)
        SmallBitmap = "DUP_TEXT.BMP"
        LargeBitmap = "DUP_TEXT.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "CHECK REPEATED TEXT", _
                       "CHECK REPEATED TEXT", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
      
        ' SET INFO DATA
        CommandString = "SET_INFO" + Chr(13)
        SmallBitmap = "INF.BMP"
        LargeBitmap = "INF.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "SET INFO TO OBJECT", _
                       "SET INFO TO OBJECT", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' SHOW INFO DATA
        CommandString = "SHOW_INFO" + Chr(13)
        SmallBitmap = "SIF.BMP"
        LargeBitmap = "SIF.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "SHOW OBJECT INFO", _
                       "SHOW OBJECT INFO", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' SetTo Excel
        CommandString = "setexcel" + Chr(13)
        SmallBitmap = "SIF.BMP"
        LargeBitmap = "SIF.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "Excel Order", _
                       "Excel Order", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
        ' To Excel
        CommandString = "toexcel" + Chr(13)
        SmallBitmap = "CREATE_EXCEL.BMP"
        LargeBitmap = "CREATE_EXCEL.BMP"
        Set newButton = newToolbar.AddToolbarButton _
                       ("", "To Excel", _
                       "To Excel", CommandString)
        newButton.SetBitmaps SmallBitmap, LargeBitmap
        
         
        ' Create Excel To Output
'        CommandString = "CreateExcel" + Chr(13)
'        SmallBitmap = "CREATE_EXCEL.BMP"
'        LargeBitmap = "CREATE_EXCEL.BMP"
'        Set newButton = newToolbar.AddToolbarButton _
'                       ("", "Tao File Excel de xuat ket qua", _
'                       "Tao File Excel de xuat ket qua", CommandString)
'        newButton.SetBitmaps SmallBitmap, LargeBitmap


    End If
    


ext:
    

End Sub

Public Sub CreateExcel()
    

    
End Sub
Private Sub test()

    
End Sub

Private Sub CloseExcel()
    ExcelWorkbook.Close
End Sub

