Option Explicit
Sub Set_Info()
On Error GoTo ext
    Dim obj As ZcadObject
    Dim str As String
    Dim sset  As ZcadSelectionSet
    Set sset = ThisDrawing.SelectionSets.Add("SS8")
    sset.SelectOnScreen
    If sset.Count > 0 Then
        Set obj = sset.Item(0)
        str = ThisDrawing.Utility.GetString(1, "Enter Text: " + vbCr)
        Dim xType2(0 To 1) As Integer
        Dim xData2(0 To 1) As Variant
        xType2(0) = 1001: xData2(0) = appInfo
        xType2(1) = 1000: xData2(1) = str
        obj.SetXData xType2, xData2
    End If
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
        
End Sub

Public Sub Set_xData_To_Excel()
    On Error GoTo ext
    
    Dim Ecount As Integer
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant

    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
        
    Set sset = ThisDrawing.SelectionSets.Add("SS8118")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    
    If sset.Count > 0 Then
        Ecount = ThisDrawing.Utility.GetInteger("Nhap so thu tu")
        Set obj = sset(0)
        xtypeLBL(0) = 1001: xdataLBL(0) = appExcel
        xtypeLBL(1) = 1040: xdataLBL(1) = Ecount
        obj.SetXData xtypeLBL, xdataLBL
        obj.TextString = Ecount
    End If
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
End Sub


Sub Set_xData_To_Bus()
On Error GoTo ext
    Debug.Print "________________Set_xData_To_Bus in SetXData"
    Dim number As Double
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi As Long
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 1) As Integer
    Dim xData2(0 To 1) As Variant
    
    Set sset = ThisDrawing.SelectionSets.Add("SS8")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    
    For Each obj In sset
        xdi = 0
        On Error Resume Next
        number = CLng(obj.TextString)
        xdi = BusIndex(CLng(number))
        
        If xdi > 0 Then
        
            xtypeLBL(0) = 1001: xdataLBL(0) = appType
            xtypeLBL(1) = 1000: xdataLBL(1) = appBus
            obj.SetXData xtypeLBL, xdataLBL
            
            xType2(0) = 1001: xData2(0) = appBus
            xType2(1) = 1040: xData2(1) = number
            obj.SetXData xType2, xData2
            
            obj.TextString = StrBus(obj, "number")
            
        Else
            On Error Resume Next
            number = ThisDrawing.Utility.GetReal("Enter Bus Number" + vbCrLf)
            xdi = BusIndex(CLng(number))
            If xdi > 0 Then
                xtypeLBL(0) = 1001: xdataLBL(0) = appType
                xtypeLBL(1) = 1000: xdataLBL(1) = appBus
                obj.SetXData xtypeLBL, xdataLBL
                
                xType2(0) = 1001: xData2(0) = appBus
                xType2(1) = 1040: xData2(1) = number
                obj.SetXData xType2, xData2
                
                obj.TextString = StrBus(obj, "number")
            Else
                ThisDrawing.Utility.Prompt "Invalid number!" + vbCrLf
            End If
            
        End If
    Next
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub

Sub Set_xData_To_Load()
On Error GoTo ext
    Debug.Print "________________Set_xData_To_Load in SetXData"
    Dim number As Double
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi As Long
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 1) As Integer
    Dim xData2(0 To 1) As Variant
    
    AutoEnable = False
    Set sset = ThisDrawing.SelectionSets.Add("SS11")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    
    For Each obj In sset
        xdi = 0
        number = CLng(obj.TextString)
        xdi = LoadIndex(number, 1)
        If xdi > 0 Then
            xtypeLBL(0) = 1001: xdataLBL(0) = appType
            xtypeLBL(1) = 1000: xdataLBL(1) = appLod
            obj.SetXData xtypeLBL, xdataLBL
            xType2(0) = 1001: xData2(0) = appLod
            xType2(1) = 1040: xData2(1) = number
            obj.SetXData xType2, xData2
            obj.TextString = StrLoad(obj, "pq")
        Else
            ThisDrawing.Utility.Prompt "Load " + obj.TextString + " not in System." + vbCrLf
        End If
    Next
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    AutoEnable = True
End Sub
Sub Set_xData_To_MacBus()
'On Error GoTo ext

    Debug.Print "________________Set_xData_To_MacBus in SetXData"
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2() As Integer
    Dim xData2() As Variant
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi As Long
    Dim INum As Long
        
    Set sset = ThisDrawing.SelectionSets.Add("SS1")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    
    For Each obj In sset
       ' On Error Resume Next
        INum = CLng(obj.TextString)
        
        xtypeLBL(0) = 1001: xdataLBL(0) = appType
        xtypeLBL(1) = 1000: xdataLBL(1) = appMacBus
        obj.SetXData xtypeLBL, xdataLBL
        
        ReDim xType2(1)
        ReDim xData2(1)
        
        xType2(0) = 1001: xData2(0) = appMacBus
        xType2(1) = 1040: xData2(1) = INum
        obj.SetXData xType2, xData2
        
        obj.TextString = StrMacBus(obj, "pqtrans")
    Next
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub
Sub Set_xData_To_Mac()
Debug.Print "________________Set_xData_To_Mac in SetXData"
On Error GoTo ext
    Dim n As Long
    Dim str As Variant
    Dim i As Long
        
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2() As Integer
    Dim xData2() As Variant
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi As Long
        
    Set sset = ThisDrawing.SelectionSets.Add("SS11")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    
    For Each obj In sset
        str = VBA.Split(obj.TextString, ".")
        n = UBound(str)
        For i = 0 To n
            xdi = 0
            xdi = GenIndex(CLng(str(i)), "1")
            If xdi <= 0 Then
                ThisDrawing.Utility.Prompt "Warning:" + vbCrLf + "Bus: " + str(i) + " Not in system"
            End If
        Next
        
        xtypeLBL(0) = 1001: xdataLBL(0) = appType
        xtypeLBL(1) = 1000: xdataLBL(1) = appMac
        obj.SetXData xtypeLBL, xdataLBL
        
        ReDim xType2(n + 2)
        ReDim xData2(n + 2)
        
        xType2(0) = 1001: xData2(0) = appMac
        xType2(1) = 1070: xData2(1) = n + 1
        
        For i = 0 To n
            xType2(i + 2) = 1000: xData2(i + 2) = str(i)
        Next
        obj.SetXData xType2, xData2
        obj.TextString = StrMac(obj, "pq")
        
    Next
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub



Sub Set_xData_To_Branch()
Debug.Print "________________Set_xData_To_Branch in SetXData"
On Error GoTo ext
AutoEnable = False
    Dim frombus As Long
    Dim tobus As Long
    Dim CKT As String
    Dim str As Variant
    
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 3) As Integer
    Dim xData2(0 To 3) As Variant

    
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi As Long

    
    Set sset = ThisDrawing.SelectionSets.Add("SS18")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    
    For Each obj In sset
        str = VBA.Split(obj.TextString, ".")
        frombus = CLng(str(0))
        tobus = CLng(str(1))
        CKT = str(2)
        xdi = 0
        xdi = BranchIndex(frombus, tobus, CKT)
        If xdi <> 0 Then
            xtypeLBL(0) = 1001: xdataLBL(0) = appType
            xtypeLBL(1) = 1000: xdataLBL(1) = appBrn
            obj.SetXData xtypeLBL, xdataLBL
            
            xType2(0) = 1001: xData2(0) = appBrn
            xType2(1) = 1040: xData2(1) = frombus
            xType2(2) = 1040: xData2(2) = tobus
            xType2(3) = 1040: xData2(3) = CKT
            obj.SetXData xType2, xData2
            obj.TextString = StrBrn(obj, "pq")
        Else
            ThisDrawing.Utility.Prompt "Branch " + obj.TextString + " not in System. Please Try Again." + vbCrLf
        End If
        
    Next
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
AutoEnable = True
End Sub

Sub Set_xData_To_MBranch()
Debug.Print "________________Set_xData_To_MBranch in SetXData"
On Error GoTo ext
    AutoEnable = False
    Dim frombus As Long
    Dim tobus As Long
    Dim ckt1 As String, ckt2 As String
    Dim str As Variant
    
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 4) As Integer
    Dim xData2(0 To 4) As Variant
       
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi1, xdi2 As Long
    
    Set sset = ThisDrawing.SelectionSets.Add("SS18")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    
    For Each obj In sset
        str = VBA.Split(obj.TextString, ".")
        frombus = CLng(str(0))
        tobus = CLng(str(1))
        ckt1 = str(2): ckt2 = str(3)
        xdi1 = 0: xdi2 = 0
        xdi1 = BranchIndex(frombus, tobus, ckt1)
        xdi2 = BranchIndex(frombus, tobus, ckt2)
        If (xdi1 <> 0) And (xdi2 <> 0) Then
            xtypeLBL(0) = 1001: xdataLBL(0) = appType
            xtypeLBL(1) = 1000: xdataLBL(1) = appMBrn
            obj.SetXData xtypeLBL, xdataLBL
            
            xType2(0) = 1001: xData2(0) = appMBrn
            xType2(1) = 1040: xData2(1) = frombus
            xType2(2) = 1040: xData2(2) = tobus
            xType2(3) = 1040: xData2(3) = ckt1
            xType2(4) = 1040: xData2(4) = ckt2
            obj.SetXData xType2, xData2
            obj.TextString = StrMBrn(obj, "pq")
        Else
            ThisDrawing.Utility.Prompt "Branch " + obj.TextString + " not in System. Please Try Again." + vbCrLf
        End If
        
    Next
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
AutoEnable = True
End Sub
Sub Set_xData_To_PBranch()
Debug.Print "________________Set_xData_To_PBranch in SetXData"
On Error GoTo ext
AutoEnable = False
    Dim frombus As Long
    Dim tobus As Long
    
    
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 2) As Integer
    Dim xData2(0 To 2) As Variant
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi As Long
    Set sset = ThisDrawing.SelectionSets.Add("SS31")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    If sset.Count = 3 Then
        frombus = CLng(sset.Item(0).TextString)
        tobus = CLng(sset.Item(1).TextString)
        Set obj = sset.Item(2)
        xtypeLBL(0) = 1001: xdataLBL(0) = appType
        xtypeLBL(1) = 1000: xdataLBL(1) = appPBrn
        obj.SetXData xtypeLBL, xdataLBL
        xType2(0) = 1001: xData2(0) = appPBrn
        xType2(1) = 1040: xData2(1) = frombus
        xType2(2) = 1040: xData2(2) = tobus
        obj.SetXData xType2, xData2
        obj.TextString = StrPbrn(obj, "number")
    End If
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    AutoEnable = True
End Sub

Sub Set_xData_To_Trans()
Debug.Print "________________Set_xData_To_Trans in SetXData"
On Error GoTo ext
    
    Dim number As Double
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim xdi As Long
    Dim xtypeLBL(0 To 1) As Integer
    Dim xdataLBL(0 To 1) As Variant
    Dim xType2(0 To 1) As Integer
    Dim xData2(0 To 1) As Variant
    AutoEnable = False
    Set sset = ThisDrawing.SelectionSets.Add("SS6")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData

    For Each obj In sset
        xdi = 0
        number = CLng(obj.TextString)
        xdi = BusIndex(CLng(number))
        If xdi > 0 Then
        
            xtypeLBL(0) = 1001: xdataLBL(0) = appType
            xtypeLBL(1) = 1000: xdataLBL(1) = appTrans
            obj.SetXData xtypeLBL, xdataLBL
            
            xType2(0) = 1001: xData2(0) = appTrans
            xType2(1) = 1040: xData2(1) = number
            obj.SetXData xType2, xData2
            
            obj.TextString = StrTrans(obj, "pq")
        Else
            ThisDrawing.Utility.Prompt "Bus " + obj.TextString + " not in System." + vbCrLf
        End If
    Next
ext:
    
    If Not sset Is Nothing Then
        sset.Delete
    End If
    AutoEnable = True
    
End Sub

