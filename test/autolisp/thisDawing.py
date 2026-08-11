
Private CurHandle As String

Private Sub ZcadDocument_BeginDoubleClick(ByVal PickPoint As Variant)
Dim P(2) As Double

    P(0) = PickPoint(0)
    P(1) = PickPoint(1)
    P(2) = PickPoint(2)
   
End Sub

Private Sub ZcadDocument_ObjectModified(ByVal Object As Object)
    If AutoEnable = False Then GoTo ext
    
    If VBA.UCase(Object.ObjectName) = "ACDBTEXT" Then
        CurHandle = Object.Handle
    Else
        CurHandle = ""
    End If
ext:
End Sub
Private Sub ZcadDocument_Activate()
    AutoEnable = True
End Sub
Private Sub ZcadDocument_EndCommand(ByVal CommandName As String)
    Dim CurrentObject As ZcadText
    If CommandName <> "DDEDIT" Then GoTo ext
    If AutoEnable = False Then GoTo ext
    
    On Error Resume Next
    Set CurrentObject = ThisDrawing.HandleToObject(CurHandle)
    If AutoEnable And (Not CurrentObject Is Nothing) Then
        Set_xData_To_Object CurrentObject
    End If
    CurHandle = ""
ext:
    ThisDrawing.Utility.Prompt CommandName
End Sub
Private Sub Set_xData_To_Object(ByVal Object As ZcadObject)
    Dim obj As ZcadText
    Dim n As Integer
    Dim number As Double
    Dim frombus As Long
    Dim tobus As Long
    Dim ckt1 As String, ckt2 As String, CKT As String
    Dim idx As Integer
    Dim str As Variant
    Dim xType1(0 To 1) As Integer
    Dim xData1(0 To 1) As Variant
    Dim xType2(0 To 2) As Integer
    Dim xData2(0 To 2) As Variant
    Dim xType3(0 To 3) As Integer
    Dim xData3(0 To 3) As Variant
    Dim xType4(0 To 4) As Integer
    Dim xData4(0 To 4) As Variant
    Dim xTypen() As Integer
    Dim xDatan() As Variant
    
AutoEnable = False
'If Not ViewEnable Then GoTo ext
On Error GoTo ext
If VBA.UCase(Object.ObjectName) = "ACDBTEXT" Then
    Set obj = Object
    '------------------------
    Select Case TypeName(obj)
    Case appBus
        On Error Resume Next
        number = CDbl(obj.TextString)
        idx = BusIndex(CLng(number))
        If BusIndex(number) > 0 Then
            xType1(0) = 1001: xData1(0) = appBus
            xType1(1) = 1040: xData1(1) = number
            obj.SetXData xType1, xData1
            obj.TextString = StrBus(obj, "name")
            printx "Bus name: " + BusAr(idx).Name
        Else
            printx "Invalid Number !"
        End If
    '------------------------
    Case appLod
        On Error Resume Next
        number = CDbl(obj.TextString)
        idx = LoadIndex(CLng(number), 1)
        If BusIndex(number) <> 0 Then
            xType1(0) = 1001: xData1(0) = appLod
            xType1(1) = 1040: xData1(1) = number
            obj.SetXData xType1, xData1
            obj.TextString = StrLoad(obj, "pq")
            printx "Load at Bus: " + BusAr(idx).Name
        Else
            printx "Invalid Number !"
        End If
    '------------------------
    Case appTrans
        On Error Resume Next
        number = CDbl(obj.TextString)
        idx = BusIndex(CLng(number))
        If BusIndex(number) <> 0 Then
            xType1(0) = 1001: xData1(0) = appTrans
            xType1(1) = 1040: xData1(1) = number
            obj.SetXData xType1, xData1
            obj.TextString = StrTrans(obj, "params")
            printx "Transformer at bus: " + BusAr(idx).Name + vbCrLf
        Else
            printx "Invalid Number !" + vbCrLf
        End If
    '------------------------
    Case appMBrn
        On Error Resume Next
        str = VBA.Split(obj.TextString, ".")
        frombus = CLng(str(0))
        tobus = CLng(str(1))
        ckt1 = str(2): ckt2 = str(3)
        xdi1 = 0: xdi2 = 0
        xdi1 = BranchIndex(frombus, tobus, ckt1)
        xdi2 = BranchIndex(frombus, tobus, ckt2)
        If (xdi1 <> 0) And (xdi2 <> 0) Then
            xType4(0) = 1001: xData4(0) = appMBrn
            xType4(1) = 1040: xData4(1) = frombus
            xType4(2) = 1040: xData4(2) = tobus
            xType4(3) = 1040: xData4(3) = ckt1
            xType4(4) = 1040: xData4(4) = ckt2
            obj.SetXData xType4, xData4
            obj.TextString = StrMBrn(obj, "params")
        Else
            printx "Invalid Number !" + vbCrLf
        End If
    '------------------------
    Case appBrn
        On Error Resume Next
        str = VBA.Split(obj.TextString, ".")
        frombus = CLng(str(0))
        tobus = CLng(str(1))
        CKT = str(2)
        xdi = 0
        xdi = BranchIndex(frombus, tobus, CKT)
        If xdi <> 0 Then
            xType3(0) = 1001: xData3(0) = appBrn
            xType3(1) = 1040: xData3(1) = frombus
            xType3(2) = 1040: xData3(2) = tobus
            xType3(3) = 1040: xData3(3) = CKT
            obj.SetXData xType3, xData3
            obj.TextString = StrBrn(obj, "params")
        Else
            printx "Invalid Number !" + vbCrLf
        End If
    '------------------------
        
    Case appPBrn
        Dim ipdx As Variant
        'On Error Resume Next
        str = VBA.Split(obj.TextString, ".")
        frombus = CLng(str(0))
        tobus = CLng(str(1))
        
        ipdx = PBranchIndex(frombus, tobus)
        If ipdx(0) > 0 Then
            xType2(0) = 1001: xData2(0) = appPBrn
            xType2(1) = 1040: xData2(1) = frombus
            xType2(2) = 1040: xData2(2) = tobus
            obj.SetXData xType2, xData2
            obj.TextString = StrPbrn(obj, "params")
        Else
            printx "Invalid Number !" + vbCrLf
        End If
    '------------------------
    Case appMac
        On Error GoTo ext
        str = VBA.Split(obj.TextString, ".")
        n = UBound(str)
        For i = 0 To n
            xdi = 0
            xdi = GenIndex(CLng(str(i)), "1")
            If xdi <= 0 Then
                ThisDrawing.Utility.Prompt "Warning:" + vbCrLf + "Bus: " + str(i) + " Not in system"
            End If
        Next
        ReDim xTypen(n + 2)
        ReDim xDatan(n + 2)
        xTypen(0) = 1001: xDatan(0) = appMac
        xTypen(1) = 1070: xDatan(1) = n + 1
        For i = 0 To n
            xTypen(i + 2) = 1000: xDatan(i + 2) = str(i)
        Next
        obj.SetXData xTypen, xDatan
        obj.TextString = StrMac(obj, "pq")
        
    Case appMacBus
        On Error Resume Next
        number = CDbl(obj.TextString)
        idx = BusIndex(CLng(number))
        If idx > 0 Then
            xType1(0) = 1001: xData1(0) = appMacBus
            xType1(1) = 1040: xData1(1) = number
            obj.SetXData xType1, xData1
            obj.TextString = StrMacBus(obj, "macnumber")
            printx "Bus name: " + BusAr(idx).Name
        Else
            printx "Invalid Number !"
        End If
    End Select
    
End If
ext:
AutoEnable = True
End Sub
