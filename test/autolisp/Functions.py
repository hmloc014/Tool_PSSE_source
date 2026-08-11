Option Explicit
Public Sub XemNguon()
'   Nhap so hieu nut
'   Tra ve tat ca cac nut nguon (MBA 2CD) noi voi nut do duoi dang PMac
Dim INum As Long
Dim idx As Integer

INum = 0
On Error Resume Next
INum = CLng(ThisDrawing.Utility.GetString(0, "So hieu nut Cao Ap:" + vbCrLf))
idx = BusIndex(INum)

If idx > 0 Then
    Dim i As Integer
    Dim str As String
    Dim ikv As Double, jkv As Double
    Dim JNum As Long
    ikv = BusAr(BusIndex(INum)).KV / BusAr(BusIndex(INum)).PU
    MsgBox ikv
    str = ""
    For i = 1 To nBranch
        If INum = BrnAr(i).frombus Then
            JNum = BrnAr(i).tobus
            jkv = BusAr(BusIndex(JNum)).KV / BusAr(BusIndex(JNum)).PU
            MsgBox jkv
            If ikv <> jkv Then
                str = str + CStr(JNum) + "."
            End If
        End If
        If INum = BrnAr(i).tobus Then
            JNum = BrnAr(i).frombus
            jkv = BusAr(BusIndex(JNum)).KV / BusAr(BusIndex(JNum)).PU
            MsgBox jkv
            If ikv <> jkv Then
                str = str + CStr(JNum) + "."
            End If
        End If
    Next
    If str <> "" Then
        'ThisDrawing.Utility.Prompt "Cac nut nguon: " + str + vbCrLf
        MsgBox ("Cac nut nguon: " + str + vbCrLf)
    Else
        'ThisDrawing.Utility.Prompt "Khong co nut nguon: " + vbCrLf
        MsgBox ("Khong co nut nguon: " + vbCrLf)
    End If
End If
End Sub



Public Sub copytext()
'   Chon cac text gan ket qua loadflow
'   Xuat ket qua ra de paste sang word
'
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
    
    Set sset = ThisDrawing.SelectionSets.Add("SS8")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    Dim TranStr As String
    Dim BrnStr As String
    Dim PBrnStr As String
    Dim MBrnStr As String
    BrnStr = ""
    PBrnStr = ""
    MBrnStr = ""
    TranStr = ""
    
    For Each obj In sset
            Dim lbl As String
            lbl = TypeName(obj)
            Select Case lbl
                Case appBrn
                    BrnStr = BrnStr + StrBrn(obj, "number") _
                           + " " + StrBrn(obj, "pq") _
                           + " " + StrBrn(obj, "rate") + vbCrLf
                Case appMBrn
                    MBrnStr = MBrnStr + StrMBrn(obj, "number") _
                           + " " + StrMBrn(obj, "pq") _
                           + " " + StrMBrn(obj, "rate") + vbCrLf
                Case appPBrn
                    PBrnStr = PBrnStr + StrPbrn(obj, "number") _
                           + " " + StrPbrn(obj, "pq") _
                           + " " + StrPbrn(obj, "rate") + vbCrLf
                Case appTrans
                    TranStr = TranStr + StrTrans(obj, "number") + _
                           " " + StrTrans(obj, "pq") _
                           + " " + StrTrans(obj, "rate") + vbCrLf
            End Select
    Next
    frmLFText.TextBox1.Text = BrnStr + MBrnStr + PBrnStr + TranStr
    frmLFText.Show
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub

Public Sub printx(str As String)
    ThisDrawing.Utility.Prompt str
End Sub



Function TypeName(obj As ZcadObject) As String

    Dim xDataType As Variant
    Dim xData As Variant
        TypeName = ""
        obj.GetXData appType, xDataType, xData
        If VarType(xDataType) <> vbEmpty Then
                TypeName = xData(1)
                Debug.Print "This is TypeName:", TypeName
        End If
End Function


Public Function InputFile() As String
Debug.Print "This is Inputfile:", InputFile
    ' return file name .P2C
    Dim s1 As String
    s1 = ThisDrawing.Path + "\" + ThisDrawing.Name
    s1 = VBA.Left(s1, Len(s1) - 4) + ".P2C"
    InputFile = s1
End Function

Public Sub ReadP2CFile()
Dim i As Long
Dim j As Long
Dim k As Long
Dim datacode As String

Open InputFile For Input As #1
Debug.Print "This is ReadP2CFile" + InputFile
nBus = 0
nBranch = 0
nLoad = 0
nGen = 0
nT3 = 0

Do While Not EOF(1)
    Input #1, datacode
    Select Case datacode
    Case "A100"
        nBus = nBus + 1
        Input #1, BusAr(nBus).number
        Input #1, BusAr(nBus).Name
        Input #1, BusAr(nBus).KV
        Input #1, BusAr(nBus).PU
        Input #1, BusAr(nBus).ANG
        If nBus <= 20 Then
            Debug.Print "nbus and number is:", BusAr(nBus).Name
        End If
        'MsgBox CStr(BusAr(nBus).number) + "/" + CStr(BusAr(nBus).BusPU)
    Case "A200"
        nLoad = nLoad + 1
        Input #1, LodAr(nLoad).number
        Input #1, LodAr(nLoad).ID
        Input #1, LodAr(nLoad).PL
        Input #1, LodAr(nLoad).QL
        If nLoad <= 10 Then
            Debug.Print "Load Number is:", LodAr(nLoad).number
        End If
    Case "A300"
        nGen = nGen + 1
        Input #1, GenAr(nGen).number
        Input #1, GenAr(nGen).ID
        Input #1, GenAr(nGen).PG
        Input #1, GenAr(nGen).QG
        Input #1, GenAr(nGen).Pmax
        If nGen <= 10 Then
            Debug.Print "Gen Number is:", GenAr(nGen).number
        End If
    Case "A400"
        nBranch = nBranch + 1
        Input #1, BrnAr(nBranch).frombus
        Input #1, BrnAr(nBranch).tobus
        Input #1, BrnAr(nBranch).CKT
        Input #1, BrnAr(nBranch).P
        Input #1, BrnAr(nBranch).Q
        Input #1, BrnAr(nBranch).PCTRTA
        Input #1, BrnAr(nBranch).TypeName
        Input #1, BrnAr(nBranch).TypeData
        If nBranch <= 10 Then
            Debug.Print "Branch Number is:", BrnAr(nBranch).frombus, "-", BrnAr(nBranch).tobus, "-", BrnAr(nBranch).CKT
        End If
    Case "A500"
        nT3 = nT3 + 1
        Input #1, Tr3Ar(nT3).ibus
        Input #1, Tr3Ar(nT3).jbus
        Input #1, Tr3Ar(nT3).KBus
        Input #1, Tr3Ar(nT3).ICKT
        Input #1, Tr3Ar(nT3).P1
        Input #1, Tr3Ar(nT3).Q1
        Input #1, Tr3Ar(nT3).P2
        Input #1, Tr3Ar(nT3).Q2
        Input #1, Tr3Ar(nT3).P3
        Input #1, Tr3Ar(nT3).Q3
        Input #1, Tr3Ar(nT3).I_PCTRTA
        Input #1, Tr3Ar(nT3).J_PCTRTA
        Input #1, Tr3Ar(nT3).K_PCTRTA
        Input #1, Tr3Ar(nT3).TransName
        If nT3 <= 10 Then
            Debug.Print "Tr3Ar Number is:", Tr3Ar(nT3).ibus, "-", Tr3Ar(nT3).jbus, "-", Tr3Ar(nT3).KBus
        End If
    End Select
Loop

Close #1
End Sub



Public Function BUSNAME(ByVal number As Long) As String
    Dim ID As Long
    BUSNAME = ""
If nBus > 0 Then
    ID = BusIndex(number)
    If ID > 0 Then
        BUSNAME = BusAr(ID).Name
    End If
End If
End Function


Public Function ToComplex(ByVal P As Double, ByVal Q As Double) As String
    Dim s As String
    s = VBA.Format(P, "###0.0")
    If Q >= 0 Then
        s = s + "+j" + VBA.Format(Q, "###0.0")
    Else
        s = s + "-j" + VBA.Format(Abs(Q), "###0.0")
    End If
    ToComplex = s
End Function




' thu tuc zoomwindow text co handle ObjHandle voi ban kinh = ZScale * Text'sHeight
Public Sub ZoomText(ByVal ObjHandle As String, ByVal Zscale)
On Error GoTo ext
    Dim TextObj As ZcadText
    Dim point1(0 To 2) As Double
    Dim point2(0 To 2) As Double
    Dim insP As Variant
    Dim TextHeight As Long
    If ObjHandle <> "" Then
        Set TextObj = ThisDrawing.HandleToObject(ObjHandle)
            TextObj.Highlight (True)
            insP = TextObj.InsertionPoint
            TextHeight = TextObj.Height
            point1(0) = insP(0) - TextHeight * Zscale: point1(1) = insP(1) - TextHeight * Zscale: point1(2) = 0
            point2(0) = insP(0) + TextHeight * Zscale: point2(1) = insP(1) + TextHeight * Zscale: point2(2) = 0
            ZoomWindow point1, point2
            TextObj.Highlight (False)
    End If
ext:
End Sub

Sub Delete_Excel_xData()
On Error GoTo ext
        
    Dim number As Double
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS611")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    Set obj = sset.Item(0)
    
    For Each obj In sset
        Dim xtypeLBL(0 To 1) As Integer
        Dim xdataLBL(0 To 1) As Variant
        xtypeLBL(0) = 1001: xdataLBL(0) = appExcel
        xtypeLBL(1) = 1000: xdataLBL(1) = "0"
        obj.SetXData xtypeLBL, xdataLBL
        obj.TextString = "DelExcel"
    Next
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub

Sub Delete_xData()
On Error GoTo ext
        
    Dim number As Double
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS6")
    FilType(0) = 0
    FilData(0) = "Text"
    sset.SelectOnScreen FilType, FilData
    Set obj = sset.Item(0)
    
    For Each obj In sset
        Dim xtypeLBL(0 To 1) As Integer
        Dim xdataLBL(0 To 1) As Variant
        xtypeLBL(0) = 1001: xdataLBL(0) = appType
        xtypeLBL(1) = 1000: xdataLBL(1) = "NO LABEL"
        obj.SetXData xtypeLBL, xdataLBL
        'obj.TextString = "label"
                
    Next
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub


Public Sub InvBranchDirect()
' Dao chieu dong cong suat nhanh don va nhanh kep
    
    Dim frombus As Long, tobus As Long, CKT As String, ckt1 As String, ckt2 As String
    Dim obj As ZcadText
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Dim ent As ZcadObject
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    Dim labeltype As String
    Dim i As Long
    Dim n As Long
    
    Dim Blk As ZcadBlockReference
    
    Set sset = ThisDrawing.SelectionSets.Add("s111")
    sset.SelectOnScreen
    
 For Each ent In sset
    
    If VBA.UCase(ent.ObjectName) = "ACDBBLOCKREFERENCE" Then
        Set Blk = ent
        Blk.Rotation = Blk.Rotation + 3.14159265358979
    End If
    
    If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
        Set obj = ent
    
        ent.GetXData appType, xDataType, xData
        If VarType(xDataType) <> vbEmpty Then
                labeltype = xData(1)
        End If
        AutoEnable = False
        Select Case labeltype
        Case appBrn
            ' BRANCH DATA
            ent.GetXData appBrn, xDataType, xData
            If VarType(xDataType) <> vbEmpty Then
                frombus = CLng(xData(1))
                tobus = CLng(xData(2))
                CKT = xData(3)
                Dim xType3(0 To 3) As Integer
                Dim xData3(0 To 3) As Variant
                xType3(0) = 1001: xData3(0) = appBrn
                xType3(1) = 1040: xData3(1) = tobus
                xType3(2) = 1040: xData3(2) = frombus
                xType3(3) = 1040: xData3(3) = CKT
                obj.SetXData xType3, xData3
                obj.TextString = StrBrn(obj, "PQ")
            End If

        Case appPBrn
            ' PARALLEL BRANCH DATA
             ent.GetXData appPBrn, xDataType, xData
            If VarType(xDataType) <> vbEmpty Then
                frombus = CLng(xData(1))
                tobus = CLng(xData(2))
                Dim xType2(0 To 2) As Integer
                Dim xData2(0 To 2) As Variant
                xType2(0) = 1001: xData2(0) = appPBrn
                xType2(1) = 1040: xData2(1) = tobus
                xType2(2) = 1040: xData2(2) = frombus
                obj.SetXData xType2, xData2
                obj.TextString = StrPbrn(obj, "PQ")
            End If
        '-----------------------------------------
        Case appMBrn
        
            ' Multi BRANCH DATA
            ent.GetXData appMBrn, xDataType, xData
            If VarType(xDataType) <> vbEmpty Then
                frombus = CLng(xData(1))
                tobus = CLng(xData(2))
                ckt1 = xData(3)
                ckt2 = xData(4)
                Dim xType4(0 To 4) As Integer
                Dim xData4(0 To 4) As Variant
                xType4(0) = 1001: xData4(0) = appMBrn
                xType4(1) = 1040: xData4(1) = CDbl(tobus)
                xType4(2) = 1040: xData4(2) = CDbl(frombus)
                xType4(3) = 1040: xData4(3) = CDbl(ckt1)
                xType4(4) = 1040: xData4(4) = CDbl(ckt2)
                obj.SetXData xType4, xData4
                obj.TextString = StrMBrn(obj, "PQ")
            End If
            
        End Select
        AutoEnable = True
    End If
  Next
  
  If Not sset Is Nothing Then
    sset.Delete
  End If
End Sub

Public Sub LIST_LOAD()
    Call ReadP2CFile
    Dim xDataType As Variant
    Dim xData As Variant
    Dim xd As Variant
    
    Dim obj As ZcadText
    Dim ent As ZcadEntity
    Dim number As Long
    Dim ID As Long
    
    Dim ibus As Long
    Dim n As Long
    Dim i As Long
    Dim idx As Long
    Dim ierr As Long
    Dim s As String
    'Dim pCKT(1 To 10) As String
    'Dim pIBus(1 To 10) As Long, pJBus(1 To 10) As Long, pKBus(1 To 10) As Long
    
    Dim labeltype As String
    ThisDrawing.Utility.Prompt vbCrLf
    For Each ent In ThisDrawing.ModelSpace
    If VBA.UCase(ent.ObjectName) = "ACDBTEXT" Then
        Set obj = ent
                ent.GetXData appType, xDataType, xData
        If VarType(xDataType) <> vbEmpty Then
                labeltype = xData(1)
        End If
    ' LOAD DATA
       If labeltype = appLod Then
            ent.GetXData appLod, xDataType, xData
            If VarType(xDataType) <> vbEmpty Then
                    s = ""
                    number = CLng(xData(1))
                    ID = CInt(xData(2))
                    idx = LoadIndex(number, ID)
                    
                    If idx > 0 Then
                        s = BusAr(BusIndex(number)).Name + "      " + CStr(number) _
                        + "      " + CStr(ID) + "        " + CStr(Round(LodAr(idx).PL)) _
                        + "      " + CStr(Round(LodAr(idx).QL)) + "       " _
                        + ToComplex(Round(LodAr(idx).PL, 1), Round(LodAr(idx).QL, 1))
                    Else
                        obj.TextString = "@Error"
                    End If
                    ThisDrawing.Utility.Prompt s + vbCrLf
            End If
        End If
    End If
    Next ent
End Sub









Public Sub Import_PSSE_Data()
    Call ReadP2CFile
    ThisDrawing.Utility.Prompt vbCrLf & "Import PSSE Results."
End Sub

Public Sub DubText()
' Lenh dung de kiem tra cac text co noi dung trung nhau
' Chu y: Chi cac Text nam trong Active Layer moi duoc kiem tra
    Dim obj As ZcadObject
    Dim TextHDL(1 To 10000) As String
    Dim iText As ZcadText, jText As ZcadText
    Dim n As Long, i As Long, j As Long
    Dim Line1 As ZcadLine
    Dim ans As Long
    
    n = 0
    For Each obj In ThisDrawing.ModelSpace
        If VBA.UCase(obj.ObjectName) = "ACDBTEXT" Then
            
            Set iText = obj
            If iText.Layer = ThisDrawing.ActiveLayer.Name Then
                n = n + 1
                TextHDL(n) = obj.Handle
            End If
        End If
    Next obj
    
    For i = 1 To n - 1
    For j = i + 1 To n
        Set iText = ThisDrawing.HandleToObject(TextHDL(i))
        Set jText = ThisDrawing.HandleToObject(TextHDL(j))
        If iText.TextString = jText.TextString Then
            ThisDrawing.Utility.Prompt "Warning Text: " + iText.TextString
            iText.Highlight True
            jText.Highlight True
            ZoomCenter iText.InsertionPoint, 50
            Set Line1 = ThisDrawing.ModelSpace.AddLine(iText.InsertionPoint, jText.InsertionPoint)
            ThisDrawing.Layers.Add ("TEMP LAYER 1")
            Line1.Layer = "TEMP LAYER 1"
           ' ans = MsgBox("Next ?", vbOKCancel)
           ' If ans <> vbOK Then
           '     GoTo ExitSub
           ' End If
            
        End If
    Next
    Next
    
ExitSub:
    
End Sub
Public Sub Check_Overload()
' lenh nay kiem tra cac dong cong sat qua tai
' Chu y: Chi cac Text nam trong Active Layer moi duoc kiem tra
    Dim obj As ZcadObject
    Dim TextHDL(1 To 10000) As String
    Dim iText As ZcadText
    Dim n As Long, m As Long, i As Long, j As Long
    Dim Line1 As ZcadLine
    Dim ans As Long
    Dim s1 As String
    Dim StrAr() As String
    Dim MaxRate As Double
    Dim basePoint(0 To 2) As Double
    basePoint(0) = 0: basePoint(1) = 0: basePoint(2) = 0
    
    MaxRate = ThisDrawing.Utility.GetReal("Maximum Percent of Load: ")
    If (MaxRate < 0) Or (MaxRate > 100) Then
        MaxRate = 85
    End If
    
        
    n = 0
    For Each obj In ThisDrawing.ModelSpace
        If VBA.UCase(obj.ObjectName) = "ACDBTEXT" Then
            Set iText = obj
            If iText.Layer = ThisDrawing.ActiveLayer.Name Then
                n = n + 1
                TextHDL(n) = obj.Handle
            End If
        End If
    Next obj
    
    For i = 1 To n
        Set iText = ThisDrawing.HandleToObject(TextHDL(i))
        s1 = iText.TextString
        s1 = VBA.Left(s1, Len(s1) - 3)
        StrAr = VBA.Split(s1, "/")
        m = UBound(StrAr)
        
        For j = 0 To m
            On Error Resume Next
            If CDbl(StrAr(j)) > MaxRate Then
                ZoomCenter iText.InsertionPoint, 50
                Set Line1 = ThisDrawing.ModelSpace.AddLine(iText.InsertionPoint, basePoint)
                ThisDrawing.Layers.Add ("TEMP LAYER 1")
                Line1.Layer = "TEMP LAYER 1"
                GoTo next_text
            End If
        Next
next_text:
    Next
    
ExitSub:
End Sub

Public Sub cls()
' lenh nay xoa tat ca cac doi tuong trong layer "Temp layer 1"

    Dim obj As ZcadObject

    For Each obj In ThisDrawing.ModelSpace
        On Error Resume Next
            If VBA.UCase(obj.Layer) = "TEMP LAYER 1" Then
                obj.Delete
            End If
        
    Next obj
    

End Sub
Sub test()
    Dim sset As ZcadSelectionSet
    Set sset = ThisDrawing.SelectionSets.Add("S1")
    sset.SelectOnScreen
    Dim obj As ZcadObject
    Set obj = sset(0)
    MsgBox (obj.ObjectName)
    sset.Delete
End Sub




Public Sub Extend_Bus_Bar()
On Error GoTo ext
    
    Dim objLine As ZcadLine
    Dim ZcadObj As ZcadObject
    Dim StartPoint As Variant, EndPoint As Variant
    Dim SP(0 To 2) As Double, EP(0 To 2) As Double
    Dim Lx As Double, Ly As Double
    Dim Scal As Double
    
    Dim sset  As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    Set sset = ThisDrawing.SelectionSets.Add("SS6")
    FilType(0) = 0
    FilData(0) = "Line"
    sset.SelectOnScreen FilType, FilData
    
    Scal = 0.1
    For Each ZcadObj In sset
        Set objLine = ZcadObj
        StartPoint = objLine.StartPoint
        EndPoint = objLine.EndPoint
        SP(0) = StartPoint(0): SP(1) = StartPoint(1): SP(2) = 0
        EP(0) = EndPoint(0): EP(1) = EndPoint(1): EP(2) = 0
        Lx = Scal * Abs((EP(0) - SP(0))): Ly = Scal * Abs((EP(1) - SP(1)))
        If SP(0) < EP(0) Then
            SP(0) = SP(0) - Lx
            EP(0) = EP(0) + Lx
        Else
            SP(0) = SP(0) + Lx
            EP(0) = EP(0) - Lx
        End If
        
        If SP(1) < EP(1) Then
            SP(1) = SP(1) - Ly
            EP(1) = EP(1) + Ly
        Else
            SP(1) = SP(1) + Ly
            EP(1) = EP(1) - Ly
        End If
        
        objLine.StartPoint = SP
        objLine.EndPoint = EP
    Next
    
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub



Public Function UpCaseFirstLeter(ByVal str As String) As String
Dim s1 As String
Dim ch1 As String
Dim ch2 As String
Dim i As Long

Dim cap As Boolean
s1 = ""
cap = True

For i = 1 To VBA.Len(str) - 1

    ch1 = VBA.Mid(str, i, 1)
    ch2 = VBA.Mid(str, i + 1, 1)
    If cap = True Then ch1 = VBA.UCase(ch1)
    s1 = s1 + ch1
    If (ch1 = " ") And (ch2 <> " ") Then
        cap = True
    Else
        cap = False
    End If
    
Next
ch1 = VBA.Mid(str, VBA.Len(str), 1)
s1 = s1 + ch1
UpCaseFirstLeter = s1
End Function


