Option Explicit
Public Type GVrecord
    gvname As String
    heso As Single
End Type
Public Type HPINFO
    MaHP As String
    TenHP As String
    TC As Integer
    LT As Single
    BT As Single
    TN As Single
    HESODOAN As Single 'He so doi voi mon do an
    HESODOAN_Summer As Single 'He so doi voi mon do an
End Type
Public Const HesoGD_Summer = 3
Public Const HesoGD_DA_Summer = 1#
Public Const HesoGD_DATN_Summer = 2.5
Public Const HK1_NAME = 20191
Public Const HK2_NAME = 20192
Public Const HK3_NAME = 20193
Sub RUNALL_SEQUENCE() ' Long waiting time
Sheets("Sheet1").Range("C30").Value = Str(Time())
Sheets("Sheet1").Range("C31").Value = Str(Time())
Exit Sub
End Sub
Sub PrintWBToPDF(wb As Workbook, fileName As String, _
    Optional vQuality = xlQualityStandard, _
    Optional vIncDocProperties = True, _
    Optional vIgnorePrintAreas = False, _
    Optional vOpenAferPublish = False)
    wb.Sheets(1).PageSetup.Orientation = xlLandscape
    
    wb.Sheets(1).ExportAsFixedFormat _
        Type:=xlTypePDF, _
        fileName:=fileName, _
        Quality:=vQuality, _
        IncludeDocProperties:=vIncDocProperties, _
        IgnorePrintAreas:=vIgnorePrintAreas, _
        OpenAfterPublish:=vOpenAferPublish
End Sub
Function GetFileFromPath(ByVal strPath As String) As String
    If Right$(strPath, 1) <> "\" And Len(strPath) > 0 Then
        GetFileFromPath = GetFileFromPath(Left$(strPath, Len(strPath) - 1)) + Right$(strPath, 1)
    End If
End Function
Private Sub MAKE_FONT_SIZE(Fsize As Single)
    Cells.Select
    With Selection.Font
        .size = Fsize
        .Strikethrough = False
        .Superscript = False
        .Subscript = False
        .OutlineFont = False
        .Shadow = False
        .Underline = xlUnderlineStyleNone
        .TintAndShade = 0
    End With
End Sub


Private Function ROW_LOOKUP(SHEETNAME As String, Lookup_val As Long) As Long
Dim ii As Long
ii = 2
Do While Sheets(SHEETNAME).Range("A" & ii) <> Lookup_val And ii < 1000
    ii = ii + 1
Loop
If ii = 1000 Then
    ROW_LOOKUP = 0
Else
    ROW_LOOKUP = ii
End If
End Function

Sub Thu_thap_thong_tin_Hocky1() '
' Chon thu muc, sau do copy toan bo thong tin cac file excel trong thu muc vao mot sheet destination
Dim fldr As Object, folder As String, fileName As String, outputFolder As String, wb As Workbook, app As Excel.Application
Dim ftype As String, flen As Integer, ii As Integer
Dim wb1 As Workbook, wb2 As Workbook
Dim SHEET As Worksheet
Dim pasteStart As Range
'Dim app As Excel.Application
    '----Select folder----
    Set fldr = Application.FileDialog(msoFileDialogFolderPicker)
    With fldr
        .Title = "Select folder with Excel files to export to PDF"
        .AllowMultiSelect = False
        If .Show <> -1 Then GoTo EndSub
        folder = .SelectedItems(1)
    End With
    '----Output directory---
    Sheets("Hocky_1").Select
    Cells.Select
    Selection.ClearContents
    Selection.ClearFormats
    Set wb1 = ActiveWorkbook
    Set pasteStart = [Hocky_1!A1]
    On Error GoTo 0
    
    fileName = Dir(folder & "\")
    ii = 2
    Do Until fileName = vbNullString
        flen = Len(fileName)
        ftype = Mid(fileName, flen, 1)
        If ftype <> "m" Then
            Sheets("Sheet1").Range("A" & ii).Value = fileName
            
            Set wb2 = Workbooks.Open(folder & "\" & fileName)
            
            For Each SHEET In wb2.Sheets
                    With SHEET.UsedRange
                        .Copy pasteStart
                        Set pasteStart = pasteStart.Offset(.Rows.Count)
                    End With
            Next SHEET
            ii = ii + 1
            wb2.Close
        End If
        fileName = Dir()
    Loop
EndSub:
    'MsgBox "Finished!"
End Sub

Sub Thu_thap_thong_tin_Hocky2() '
' Chon thu muc, sau do copy toan bo thong tin cac file excel trong thu muc vao mot sheet destination
Dim fldr As Object, folder As String, fileName As String, outputFolder As String, wb As Workbook, app As Excel.Application
Dim ftype As String, flen As Integer, ii As Integer
Dim wb1 As Workbook, wb2 As Workbook
Dim SHEET As Worksheet
Dim pasteStart As Range
'Dim app As Excel.Application
    '----Select folder----
    Set fldr = Application.FileDialog(msoFileDialogFolderPicker)
    With fldr
        .Title = "Select folder with Excel files to export to PDF"
        .AllowMultiSelect = False
        If .Show <> -1 Then GoTo EndSub
        folder = .SelectedItems(1)
    End With
    '----Output directory---
    Sheets("Hocky_2").Select
    Cells.Select
    Selection.ClearContents
    Selection.ClearFormats
    Set wb1 = ActiveWorkbook
    Set pasteStart = [Hocky_2!A1]
    On Error GoTo 0
    
    fileName = Dir(folder & "\")
    ii = 2
    Do Until fileName = vbNullString
        flen = Len(fileName)
        ftype = Mid(fileName, flen, 1)
        If ftype <> "m" Then
            Sheets("Sheet1").Range("A" & ii).Value = fileName
            
            Set wb2 = Workbooks.Open(folder & "\" & fileName)
            
            For Each SHEET In wb2.Sheets
                    With SHEET.UsedRange
                        .Copy pasteStart
                        Set pasteStart = pasteStart.Offset(.Rows.Count)
                    End With
            Next SHEET
            ii = ii + 1
            wb2.Close
        End If
        fileName = Dir()
    Loop
EndSub:
    'MsgBox "Finished!"
End Sub

Sub Thu_thap_thong_tin_Hocky3() '
' Chon thu muc, sau do copy toan bo thong tin cac file excel trong thu muc vao mot sheet destination
Dim fldr As Object, folder As String, fileName As String, outputFolder As String, wb As Workbook, app As Excel.Application
Dim ftype As String, flen As Integer, ii As Integer
Dim wb1 As Workbook, wb2 As Workbook
Dim SHEET As Worksheet
Dim pasteStart As Range
'Dim app As Excel.Application
    '----Select folder----
    Set fldr = Application.FileDialog(msoFileDialogFolderPicker)
    With fldr
        .Title = "Select folder with Excel files to export to PDF"
        .AllowMultiSelect = False
        If .Show <> -1 Then GoTo EndSub
        folder = .SelectedItems(1)
    End With
    '----Output directory---
    Sheets("Hocky_3").Select
    Cells.Select
    Selection.ClearContents
    Selection.ClearFormats
    Set wb1 = ActiveWorkbook
    Set pasteStart = [Hocky_3!A1]
    On Error GoTo 0
    
    fileName = Dir(folder & "\")
    ii = 2
    Do Until fileName = vbNullString
        flen = Len(fileName)
        ftype = Mid(fileName, flen, 1)
        If ftype <> "m" Then
            Sheets("Sheet1").Range("A" & ii).Value = fileName
            
            Set wb2 = Workbooks.Open(folder & "\" & fileName)
            
            For Each SHEET In wb2.Sheets
                    With SHEET.UsedRange
                        .Copy pasteStart
                        Set pasteStart = pasteStart.Offset(.Rows.Count)
                    End With
            Next SHEET
            ii = ii + 1
            wb2.Close
        End If
        fileName = Dir()
    Loop
EndSub:
    'MsgBox "Finished!"
End Sub


Sub Tong_hop_thong_tin_HD_Hocky_1a_OBSOLETE()
Dim ii As Long, mssv As Long, tenGV As String, tenSV As String, kk As Long, SISO As Long
Dim celval As Long, MALOP As Long, MaHP As String, TenHP As String, ttval As Long
Dim CL20182 As Range
Dim rowid As Long
Dim TARGET As String, CLASS_LIST As String, SV_STAY_TILL_SEMESTER_END As Boolean
Dim idx As Long, start_row As Long
TARGET = "DA_Hocky_1"
CLASS_LIST = "DS_ky1"

Sheets(TARGET).Range("A2:H5000").ClearContents
Sheets(TARGET).Range("A2:H5000").ClearFormats

'Set CL20182 = Sheets("Class_HK1").Range("A2:Q681")
ii = 2
Sheets("Hocky_1").Select

For kk = 1 To 5000
    celval = Val(Range("F" & kk).Text) 'Ma sinh vien
    ttval = Val(Range("A" & kk).Text) ' Ma lop
    tenSV = Range("G" & kk).Text
    tenGV = Range("I" & kk).Text
    If (ttval > 100000 And ttval < 700000) Then ' Ten ma lop
        'MaHP = Application.WorksheeTetFunction.VLookup(celval, CL20182, 2)
        MALOP = ttval
        rowid = ROW_LOOKUP("Class_HK1", MALOP)
    End If
    If IsNumeric(ttval) And celval > 10000000 And Len(Str(celval) = 8) And (rowid <> 0) Then
        Sheets(TARGET).Range("B" & ii).Value = MALOP
        Sheets(TARGET).Range("A" & ii).Value = tenGV
        Sheets(TARGET).Range("F" & ii).Value = tenSV
        Sheets(TARGET).Range("E" & ii).Value = celval
        Sheets(TARGET).Range("C" & ii).Value = Sheets("Class_HK1").Range("C" & rowid).Value 'ma HP
        Sheets(TARGET).Range("D" & ii).Value = Sheets("Class_HK1").Range("D" & rowid).Value '  Ten mon
        Sheets(TARGET).Range("G" & ii).Value = Sheets("Class_HK1").Range("N" & rowid).Value
        Sheets(TARGET).Range("H" & ii).Value = Sheets("Class_HK1").Range("F" & rowid).Value
        SISO = Sheets("Class_HK1").Range("H" & rowid).Value
        'Check if student actually stays until end of semester, cross check with class list
        SV_STAY_TILL_SEMESTER_END = True
        idx = 2
        'Tra ma lop
        Do While Sheets(CLASS_LIST).Range("B" & idx).Value <> MALOP And idx < 50000
            idx = idx + 1
        Loop
        If idx >= 50000 Then 'Khong thay lop
            SV_STAY_TILL_SEMESTER_END = False
        Else
            start_row = idx
            Do While Sheets(CLASS_LIST).Range("G" & idx).Value <> celval And Sheets(CLASS_LIST).Range("B" & idx).Value = MALOP 'Khong kiem tra theo si so vi khong tin cay
                idx = idx + 1
            Loop
            If Sheets(CLASS_LIST).Range("B" & idx).Value <> MALOP Then ' idx >= start_row + SISO Then
                SV_STAY_TILL_SEMESTER_END = False
            End If
        End If
        If Not (SV_STAY_TILL_SEMESTER_END) Then
            Sheets(TARGET).Range("H" & ii).Value = Sheets(TARGET).Range("H" & ii).Value + "_DROP"
        End If
        ii = ii + 1
    End If
Next
End Sub

Sub Tong_hop_thong_tin_HD_Hocky_2()
Dim ii As Long, mssv As Long, tenGV As String, tenSV As String, kk As Long, SISO As Long
Dim celval As Long, MALOP As Long, MaHP As String, TenHP As String, ttval As Long
Dim CL20182 As Range, cell As Range
Dim rowid As Long
Dim LAST_DAT_ROW As Integer
Dim TARGET As String, CLASS_LIST As String, SV_STAY_TILL_SEMESTER_END As Boolean
Dim CLSHEET As String
Dim idx As Long, start_row As Long

Sheets("Sheet1").Range("C30").Value = "Start at " + Str(Time())

TARGET = "DA_Hocky_2"
CLASS_LIST = "DS_ky2"
LAST_DAT_ROW = 2000
CLSHEET = "Class_HK2"
Sheets(TARGET).Range("A2:H5000").ClearContents
Sheets(TARGET).Range("A2:H5000").ClearFormats

'Set CL20182 = Sheets("Class_HK1").Range("A2:Q681")
ii = 2
Sheets("Hocky_2").Select

For kk = 1 To LAST_DAT_ROW
    celval = Val(Range("F" & kk).Text) 'Ma sinh vien
    ttval = Val(Range("A" & kk).Text) ' Ma lop
    tenSV = Range("G" & kk).Text
    tenGV = Range("I" & kk).Text
    If (ttval > 100000 And ttval < 700000) Then ' Ten ma lop
        'MaHP = Application.WorksheeTetFunction.VLookup(celval, CL20182, 2)
        MALOP = ttval
        rowid = ROW_LOOKUP(CLSHEET, MALOP)
    End If
    If IsNumeric(ttval) And celval > 10000000 And Len(Str(celval) = 8) And (rowid <> 0) Then
        Sheets(TARGET).Range("B" & ii).Value = MALOP
        Sheets(TARGET).Range("A" & ii).Value = tenGV
        Sheets(TARGET).Range("F" & ii).Value = tenSV
        Sheets(TARGET).Range("E" & ii).Value = celval
        Sheets(TARGET).Range("C" & ii).Value = Sheets(CLSHEET).Range("C" & rowid).Value 'ma HP
        Sheets(TARGET).Range("D" & ii).Value = Sheets(CLSHEET).Range("D" & rowid).Value '  Ten mon
        Sheets(TARGET).Range("G" & ii).Value = Sheets(CLSHEET).Range("N" & rowid).Value
        Sheets(TARGET).Range("H" & ii).Value = Sheets(CLSHEET).Range("F" & rowid).Value
        SISO = Sheets(CLSHEET).Range("H" & rowid).Value
        'Check if student actually stays until end of semester, cross check with class list
        SV_STAY_TILL_SEMESTER_END = True
        
        'Tra ma lop
        
        With Sheets(CLASS_LIST).Range("B:B")
        Set cell = .Find(What:=(MALOP), LookAt:=xlWhole, MatchCase:=False)
        End With
        If cell Is Nothing Then
            
            SV_STAY_TILL_SEMESTER_END = False
        Else
            idx = cell.Row
            Do While Sheets(CLASS_LIST).Range("G" & idx).Value <> celval And Sheets(CLASS_LIST).Range("B" & idx).Value = MALOP 'Khong kiem tra theo si so vi khong tin cay
                idx = idx + 1
            Loop
            If Sheets(CLASS_LIST).Range("B" & idx).Value <> MALOP Then ' idx >= start_row + SISO Then
                SV_STAY_TILL_SEMESTER_END = False
            End If
        End If
        If Not (SV_STAY_TILL_SEMESTER_END) Then
            Sheets(TARGET).Range("H" & ii).Value = Sheets(TARGET).Range("H" & ii).Value + "_DROP"
        End If
        ii = ii + 1
    End If
Next
Sheets("Sheet1").Range("C31").Value = "Finished at " + Str(Time())
End Sub
Sub Tong_hop_thong_tin_HD_Hocky_1()
Dim ii As Long, mssv As Long, tenGV As String, tenSV As String, kk As Long, SISO As Long
Dim celval As Long, MALOP As Long, MaHP As String, TenHP As String, ttval As Long
Dim CL20182 As Range, cell As Range
Dim rowid As Long
Dim LAST_DAT_ROW As Integer
Dim TARGET As String, CLASS_LIST As String, SV_STAY_TILL_SEMESTER_END As Boolean
Dim CLSHEET As String
Dim idx As Long, start_row As Long
TARGET = "DA_Hocky_1"
CLASS_LIST = "DS_ky1"
LAST_DAT_ROW = 2000
CLSHEET = "Class_HK1"
Sheets(TARGET).Range("A2:H5000").ClearContents
Sheets(TARGET).Range("A2:H5000").ClearFormats

'Set CL20182 = Sheets("Class_HK1").Range("A2:Q681")
ii = 2
Sheets("Hocky_1").Select

For kk = 1 To LAST_DAT_ROW
    celval = Val(Range("F" & kk).Text) 'Ma sinh vien
    ttval = Val(Range("A" & kk).Text) ' Ma lop
    tenSV = Range("G" & kk).Text
    tenGV = Range("I" & kk).Text
    If (ttval > 100000 And ttval < 700000) Then ' Ten ma lop
        'MaHP = Application.WorksheeTetFunction.VLookup(celval, CL20182, 2)
        MALOP = ttval
        rowid = ROW_LOOKUP(CLSHEET, MALOP)
    End If
    If IsNumeric(ttval) And celval > 10000000 And Len(Str(celval) = 8) And (rowid <> 0) Then
        Sheets(TARGET).Range("B" & ii).Value = MALOP
        Sheets(TARGET).Range("A" & ii).Value = tenGV
        Sheets(TARGET).Range("F" & ii).Value = tenSV
        Sheets(TARGET).Range("E" & ii).Value = celval
        Sheets(TARGET).Range("C" & ii).Value = Sheets(CLSHEET).Range("C" & rowid).Value 'ma HP
        Sheets(TARGET).Range("D" & ii).Value = Sheets(CLSHEET).Range("D" & rowid).Value '  Ten mon
        Sheets(TARGET).Range("G" & ii).Value = Sheets(CLSHEET).Range("N" & rowid).Value
        Sheets(TARGET).Range("H" & ii).Value = Sheets(CLSHEET).Range("F" & rowid).Value
        SISO = Sheets(CLSHEET).Range("H" & rowid).Value
        'Check if student actually stays until end of semester, cross check with class list
        SV_STAY_TILL_SEMESTER_END = True
        
        'Tra ma lop
        
        With Sheets(CLASS_LIST).Range("B:B")
        Set cell = .Find(What:=(MALOP), LookAt:=xlWhole, MatchCase:=False)
        End With
        If cell Is Nothing Then
            
            SV_STAY_TILL_SEMESTER_END = False
        Else
            idx = cell.Row
            Do While Sheets(CLASS_LIST).Range("G" & idx).Value <> celval And Sheets(CLASS_LIST).Range("B" & idx).Value = MALOP 'Khong kiem tra theo si so vi khong tin cay
                idx = idx + 1
            Loop
            If Sheets(CLASS_LIST).Range("B" & idx).Value <> MALOP Then ' idx >= start_row + SISO Then
                SV_STAY_TILL_SEMESTER_END = False
            End If
        End If
        If Not (SV_STAY_TILL_SEMESTER_END) Then
            Sheets(TARGET).Range("H" & ii).Value = Sheets(TARGET).Range("H" & ii).Value + "_DROP"
        End If
        ii = ii + 1
    End If
Next
End Sub
Sub Tong_hop_GD()
Dim ii As Integer, rowid As Integer, s As Variant, idx As Integer, class_type As String, kk As Integer, foundCB As Boolean
Dim tenGV_raw As String, tenGV As String, heso As Single, SUM_heso As Single
Dim substrings() As String, noGV As Integer, gvrec(1 To 100) As GVrecord, DATA_SHEET As String, TARGET As String
Dim MALOP As Long, HPNAME As String, PRGTYPE As String, HPCODE As String, mssv As Long
Dim HKNAME As Long, hpinf As HPINFO, siso_SV As Integer, TENLOP As String, SEMESTER As String
Dim SVNAME As String, tg1 As String, tg2 As String, TEN_KHONG_DAU As String
Dim TCCODE As String
'Luan an TS
Dim TenNCS As String, GVHD1 As String, GVHD2 As String
Dim NCS_daBV As Boolean, NCS_year As String

Sheets("Sheet1").Range("C30").Value = "Start at " + Str(Time())

TARGET = "Tong_hop_GD"
Sheets(TARGET).Range("A2:R10000").ClearContents
'Sheets(TARGET).Range("A2:R10000").ClearFormats
rowid = 2
Application.Calculation = xlManual
DATA_SHEET = "Phancong_ky1"
TARGET = "Tong_hop_GD"
HKNAME = HK1_NAME
ii = 2
'======= LT UNDERGRAD =============================================
BEGIN_LT: 'GD ly thuyet va thi  nghiem, Dai hoc
Do While Sheets(DATA_SHEET).Range("A" & ii).Text <> ""
    
    tenGV_raw = Sheets(DATA_SHEET).Range("O" & ii).Text
    class_type = Sheets(DATA_SHEET).Range("K" & ii).Text
    MALOP = Val(Sheets(DATA_SHEET).Range("C" & ii).Text)
    HPCODE = Sheets(DATA_SHEET).Range("D" & ii).Text
    HPNAME = Sheets(DATA_SHEET).Range("E" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("G" & ii).Text
    'If class_type = "TN" Then 'Kiem tra cheo neu lop TN gan voimon cua CTTT hoac KSTN
    '            tg1 = cross_check_mon_TN(HPCODE)
    '            Select Case tg1
    '                Case "KSTN"
    '                    PRGTYPE = tg1
    '                Case "KSCLC"
    '                    PRGTYPE = tg1
    '                Case "CTTT"
    '                    PRGTYPE = tg1
    '            End Select
    'End If
    siso_SV = Sheets(DATA_SHEET).Range("I" & ii).Text
    TENLOP = Sheets(DATA_SHEET).Range("F" & ii).Text
    'If Trim(tenGV_raw) <> "" And IS_LT(class_type) Then
    If IS_LT(class_type) Then
        hpinf = GET_HP_INFO(HPCODE)
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        If noGV = 0 Then 'mon hoc chua duoc phan cong
            noGV = 1
            gvrec(1).heso = 1
            gvrec(1).gvname = "CHUA PHAN CONG"
            SUM_heso = 1
        End If
        
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso ' / SUM_heso
            'Dien thong tin mon LT tuong ung
            
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            Sheets(TARGET).Range("C" & rowid) = MALOP
            
            Sheets(TARGET).Range("D" & rowid) = HPCODE
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = class_type
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = siso_SV
            Sheets(TARGET).Range("M" & rowid) = HesoLop(siso_SV)
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT(PRGTYPE)
            
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT(PRGTYPE)
            Sheets(TARGET).Range("H" & rowid) = TENLOP
            If siso_SV > 0 Then
                If class_type = "TN" Then
                    Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=RC[-10]*(RC[-1]+RC[-3])*RC[-4]"
                Else 'LT + BT
                    If siso_SV >= 5# Then ' Really a LT class
                        Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=(RC[-10]+RC[-9])*(RC[-3]+RC[-2])*RC[-4]"
                    Else 'Lop Project, tinh nhu do an
                        Sheets(TARGET).Range("N" & rowid) = Heso_DA_CTDT(PRGTYPE)
                        Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=RC[-10]*RC[-5]*RC[-4]*RC[-2]"
                    End If
                End If
            Else ' Khong co sinh vien
                Sheets(TARGET).Range("P" & rowid).Value = 0
            End If
            
            With hpinf
                'Sheets(TARGET).Range("D" & rowid) = .MAHP  'Su dung so lieu QLDT
                If class_type = "TN" Then
                    Sheets(TARGET).Range("F" & rowid) = .TN
                    Sheets(TARGET).Range("G" & rowid) = 0#
                Else
                    Sheets(TARGET).Range("F" & rowid) = .LT
                    Sheets(TARGET).Range("G" & rowid) = .BT
                End If
                Sheets(TARGET).Range("E" & rowid) = .TenHP
                If StrComp(.TenHP, HPNAME) <> 0 Then
                    'MsgBox HPNAME + "NEED TO BE VERIFIED FOR CONSISTENCY"
                End If
                
            End With
            rowid = rowid + 1
        Next
    End If
    ii = ii + 1
Loop
If HKNAME = HK2_NAME Then
    GoTo VANBANG2
End If
'GD ly thuyet va thi  nghiem, Dai hoc, ly 20182
DATA_SHEET = "Phancong_ky2"
TARGET = "Tong_hop_GD"
HKNAME = HK2_NAME
ii = 2
GoTo BEGIN_LT
'======= VB2 UNDERGRAD =============================================
VANBANG2:
DATA_SHEET = "VB2"

TARGET = "Tong_hop_GD"
ii = 3
Do While Sheets(DATA_SHEET).Range("A" & ii).Text <> ""
    
    tenGV_raw = Sheets(DATA_SHEET).Range("H" & ii).Text
    class_type = Sheets(DATA_SHEET).Range("C" & ii).Text
    MALOP = 0 'Val(Sheets(DATA_SHEET).Range("C" & ii).Text)
    HPCODE = "" 'Sheets(DATA_SHEET).Range("D" & ii).Text
    HPNAME = Sheets(DATA_SHEET).Range("E" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("B" & ii).Text
    siso_SV = Val(Sheets(DATA_SHEET).Range("F" & ii).Text)
    TENLOP = Sheets(DATA_SHEET).Range("A" & ii).Text
    TCCODE = Sheets(DATA_SHEET).Range("G" & ii).Text
    HKNAME = Sheets(DATA_SHEET).Range("D" & ii).Value
    If IS_LT(class_type) Then
        hpinf = GET_HP_VB2_INFO(TCCODE)
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        If noGV = 0 Then 'mon hoc chua duoc phan cong
            noGV = 1
            gvrec(1).heso = 1
            gvrec(1).gvname = "CHUA PHAN CONG"
            SUM_heso = 1
        End If
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso / SUM_heso
            'Dien thong tin mon LT tuong ung
            
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            Sheets(TARGET).Range("C" & rowid) = MALOP
            
            Sheets(TARGET).Range("D" & rowid) = HPCODE
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = class_type
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = siso_SV
            Sheets(TARGET).Range("M" & rowid) = HesoLop(siso_SV)
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT(PRGTYPE)
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT(PRGTYPE)
            Sheets(TARGET).Range("H" & rowid) = TENLOP
            If siso_SV > 0 Then
                If class_type = "TN" Then
                    Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=RC[-10]*(RC[-1]+RC[-3])*RC[-4]"
                Else 'LT + BT
                    Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=(RC[-10]+RC[-9])*(RC[-3]+RC[-2])*RC[-4]"
                
                End If
            Else ' Khong co sinh vien
                Sheets(TARGET).Range("P" & rowid).Value = 0
            End If
            
            With hpinf
                'Sheets(TARGET).Range("D" & rowid) = .MAHP  'Su dung so lieu QLDT
                If class_type = "TN" Then
                    Sheets(TARGET).Range("F" & rowid) = .TN
                    Sheets(TARGET).Range("G" & rowid) = 0#
                Else
                    Sheets(TARGET).Range("F" & rowid) = .LT
                    Sheets(TARGET).Range("G" & rowid) = .BT
                End If
                Sheets(TARGET).Range("E" & rowid) = HPNAME
                'If StrComp(.TenHP, HPNAME) <> 0 Then
                '    'MsgBox HPNAME + "NEED TO BE VERIFIED FOR CONSISTENCY"
                'End If
                
            End With
            rowid = rowid + 1
        Next
    End If
    ii = ii + 1
Loop
' ==================== DA, DATN VB2 ================================
DATA_SHEET = "DA_VB2"
TARGET = "Tong_hop_GD"
ii = 2
Do While Sheets(DATA_SHEET).Range("A" & ii).Text <> "" 'Do theo ten giao vien
    tenGV_raw = Sheets(DATA_SHEET).Range("A" & ii).Text
    class_type = Sheets(DATA_SHEET).Range("D" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("C" & ii).Text
    HKNAME = Sheets(DATA_SHEET).Range("H" & ii).Text
    With hpinf
        .TC = Sheets(DATA_SHEET).Range("G" & ii).Value
        .TenHP = Sheets(DATA_SHEET).Range("E" & ii).Text
        .HESODOAN = 1
    End With
    SVNAME = Sheets(DATA_SHEET).Range("F" & ii).Text
    'Dien thong tin mon DA tuong ung
    If IS_DA(class_type) Then
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        If noGV = 1 Then
            SUM_heso = 1
        End If
        If Trim(tenGV_raw) = "" Then
            noGV = 1
            gvrec(1).gvname = "CHUA PHAN CONG"
            gvrec(1).heso = 1
            SUM_heso = 1
        End If
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso / SUM_heso
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            'Sheets(TARGET).Range("C" & rowid) = MALOP
            'Sheets(TARGET).Range("D" & rowid) = HPCODE
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = class_type
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = 1
            Sheets(TARGET).Range("M" & rowid) = 0
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT(PRGTYPE)
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT(PRGTYPE)
            Sheets(TARGET).Range("H" & rowid) = SVNAME
            If class_type = "DA" Or class_type = "DATN" Then
                With hpinf
                    Select Case class_type
                        Case "DATN"
                            Sheets(TARGET).Range("P" & rowid).Value = .HESODOAN * gvrec(idx).heso
                            If HKNAME = HK3_NAME Then
                                Sheets(TARGET).Range("R" & rowid).FormulaR1C1 = "=RC[-2] * " & Str(HesoGD_DATN_Summer)
                            End If
                        Case "DA"
                            Sheets(TARGET).Range("P" & rowid).Value = Heso_DA_CTDT(PRGTYPE) * .TC * gvrec(idx).heso
                            If HKNAME = HK3_NAME Then
                                Sheets(TARGET).Range("R" & rowid).FormulaR1C1 = "=RC[-2] * " & Str(HesoGD_DA_Summer)
                            End If
                    End Select
                    
                    Sheets(TARGET).Range("E" & rowid) = .TenHP
                    Sheets(TARGET).Range("F" & rowid).Value = .TC
                    Sheets(TARGET).Range("G" & rowid).Value = 0
                End With
                rowid = rowid + 1
            End If
        Next
        'Tinh GD
    End If
    ii = ii + 1
Loop
' ==================================================================
DOANMON_DOANTN:
DATA_SHEET = "DA_Hocky_1"
TARGET = "Tong_hop_GD"
HKNAME = HK1_NAME
ii = 2
'======= DA UNDERGRAD =============================================
BEGIN_DA:
Do While Sheets(DATA_SHEET).Range("B" & ii).Text <> "" 'Do theo ma lop
    tenGV_raw = Sheets(DATA_SHEET).Range("A" & ii).Text
    class_type = Sheets(DATA_SHEET).Range("H" & ii).Text
    MALOP = Val(Sheets(DATA_SHEET).Range("B" & ii).Text)
    HPCODE = Sheets(DATA_SHEET).Range("C" & ii).Text
    HPNAME = Sheets(DATA_SHEET).Range("D" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("G" & ii).Text
    SVNAME = Sheets(DATA_SHEET).Range("F" & ii).Text
    mssv = Sheets(DATA_SHEET).Range("E" & ii).Value
    hpinf = GET_HP_INFO(HPCODE)
    
    'Dien thong tin mon DA tuong ung
    If IS_DA(class_type) Then
        hpinf = GET_HP_INFO(HPCODE)
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        If noGV = 1 Then
            SUM_heso = 1
        End If
        If Trim(tenGV_raw) = "" Then
            noGV = 1
            gvrec(1).gvname = "CHUA PHAN CONG"
            gvrec(1).heso = 1
            SUM_heso = 1
        End If
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso / SUM_heso
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            Sheets(TARGET).Range("C" & rowid) = MALOP
            Sheets(TARGET).Range("D" & rowid) = HPCODE
            PRGTYPE = Find_student_prog(mssv)
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = bo_dau_tieng_viet2(class_type)
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = 1
            Sheets(TARGET).Range("M" & rowid) = 0
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT(PRGTYPE)
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT(PRGTYPE)
            Sheets(TARGET).Range("H" & rowid) = SVNAME & "/" & Trim(Str(mssv))
            class_type = bo_dau_tieng_viet2(class_type)
            If class_type = "DA" Or class_type = "DATN" Then
                With hpinf
                    Select Case class_type
                        Case "DATN"
                            Sheets(TARGET).Range("P" & rowid).Value = .HESODOAN * gvrec(idx).heso
                        Case "DA"
                            Sheets(TARGET).Range("P" & rowid).Value = Heso_DA_CTDT(PRGTYPE) * .TC * gvrec(idx).heso
                    End Select
                    Sheets(TARGET).Range("E" & rowid) = .TenHP
                    Sheets(TARGET).Range("F" & rowid).Value = .TC
                    Sheets(TARGET).Range("G" & rowid).Value = 0
                End With
                rowid = rowid + 1
            End If
        Next
        'Tinh GD
        
        
    End If
    ii = ii + 1
Loop
If HKNAME = HK2_NAME Then
    GoTo BEGIN_NHAPMON
End If

DATA_SHEET = "DA_Hocky_2"
TARGET = "Tong_hop_GD"
HKNAME = HK2_NAME
ii = 2
GoTo BEGIN_DA

BEGIN_NHAPMON:
DATA_SHEET = "Nhapmon_ky1"
TARGET = "Tong_hop_GD"
'======= NHAPMON UNDERGRAD =============================================
TT_NHAPMON:
ii = 2
Do While Sheets(DATA_SHEET).Range("A" & ii).Text <> ""
    SVNAME = Sheets(DATA_SHEET).Range("B" & ii).Value
    tenGV = Sheets(DATA_SHEET).Range("E" & ii).Value
    MALOP = Val(Sheets(DATA_SHEET).Range("C" & ii).Text)
    If tenGV <> "" Then
        Sheets(TARGET).Range("A" & rowid).Value = Trim(tenGV)
        'Ten mon nhap mon
        Sheets(TARGET).Range("E" & rowid).Value = Sheets(DATA_SHEET).Range("D" & ii).Value
        'Ma lop
        Sheets(TARGET).Range("C" & rowid).Value = MALOP
        'Ten sinh vien
        Sheets(TARGET).Range("H" & rowid).Value = SVNAME
        'GD
        Sheets(TARGET).Range("P" & rowid).Value = Sheets(DATA_SHEET).Range("F" & ii).Value
        rowid = rowid + 1
    End If
    
    ii = ii + 1
Loop
If DATA_SHEET = "Nhapmon_ky1" Then
    DATA_SHEET = "Nhapmon_ky2"
    GoTo TT_NHAPMON
End If
'======= LT GRAD =============================================
BEGIN_SDH:
DATA_SHEET = "GD_Caohoc"
TARGET = "Tong_hop_GD"

ii = 2
Do While Sheets(DATA_SHEET).Range("B" & ii).Text <> ""
    tenGV_raw = Sheets(DATA_SHEET).Range("M" & ii).Text
    class_type = Sheets(DATA_SHEET).Range("I" & ii).Text
    MALOP = Val(Sheets(DATA_SHEET).Range("A" & ii).Text)
    HPCODE = Sheets(DATA_SHEET).Range("B" & ii).Text
    HPNAME = Sheets(DATA_SHEET).Range("C" & ii).Text
    SEMESTER = Sheets(DATA_SHEET).Range("F" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("E" & ii).Text
    PRGTYPE = UCase(PRGTYPE)
    If IsNumeric(Sheets(DATA_SHEET).Range("G" & ii).Text) Then
        siso_SV = Sheets(DATA_SHEET).Range("G" & ii).Text
    Else
        siso_SV = 0
    End If
    If IS_LT(class_type) Then
        hpinf = GET_HP_INFO(HPCODE)
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        If Trim(tenGV_raw) = "" Then
            noGV = 1
            gvrec(1).gvname = "CHUA PHAN CONG"
            gvrec(1).heso = 1
            SUM_heso = 1
        End If
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso / SUM_heso
            'Dien thong tin mon LT tuong ung
            
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            Sheets(TARGET).Range("C" & rowid) = MALOP
            Sheets(TARGET).Range("D" & rowid) = HPCODE
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = class_type
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = siso_SV
            Sheets(TARGET).Range("M" & rowid) = HesoLop(siso_SV)
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT(PRGTYPE)
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT(PRGTYPE)
            Sheets(TARGET).Range("B" & rowid) = SEMESTER
            If siso_SV > 0 Then
                If class_type = "TN" Then
                    Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=RC[-10]*(RC[-1]+RC[-3])*RC[-4]"
                Else 'LT + BT
                    If siso_SV >= 5 Then
                        Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=(RC[-10]+RC[-9])*(RC[-3]+RC[-2])*RC[-4]"
                    Else ' Lop nho hon 10 sinh vien, tinh nhu do an
                        Sheets(TARGET).Range("N" & rowid) = Heso_DA_CTDT(PRGTYPE)
                        Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=(RC[-10]+RC[-9])*(RC[-5])*RC[-2]"
                    End If
                
                End If
            Else ' Khong co sinh vien
                Sheets(TARGET).Range("P" & rowid).Value = 0
            End If
            
            With hpinf
                'Sheets(TARGET).Range("D" & rowid) = .MAHP  'Su dung so lieu QLDT
                If class_type = "TN" Then
                    Sheets(TARGET).Range("F" & rowid) = .TN
                    Sheets(TARGET).Range("G" & rowid) = 0#
                Else
                    Sheets(TARGET).Range("F" & rowid) = .LT
                    Sheets(TARGET).Range("G" & rowid) = .BT
                End If
                Sheets(TARGET).Range("E" & rowid) = .TenHP
                If StrComp(.TenHP, HPNAME) <> 0 Then
                    'MsgBox HPNAME + "NEED TO BE VERIFIED FOR CONSISTENCY"
                End If
                
            End With
            
            rowid = rowid + 1
        Next
    End If
    ii = ii + 1
Loop

BEGIN_LVCH:
DATA_SHEET = "LV_caohoc"
TARGET = "Tong_hop_GD"
'HKNAME = 20192020
ii = 2  '
Do While Sheets(DATA_SHEET).Range("A" & ii).Text <> ""
    tenGV_raw = Sheets(DATA_SHEET).Range("G" & ii).Text
    class_type = "DATN"
    MALOP = Val(Sheets(DATA_SHEET).Range("B" & ii).Text)
    HPCODE = "" 'Sheets(DATA_SHEET).Range("B" & ii).Text
    HPNAME = Sheets(DATA_SHEET).Range("J" & ii).Text
    HKNAME = Sheets(DATA_SHEET).Range("A" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("F" & ii).Text 'Ky thuat hoac khoa hoc
    PRGTYPE = UCase(PRGTYPE)
    siso_SV = 1 'Sheets(DATA_SHEET).Range("C" & ii).Text
    SVNAME = Sheets(DATA_SHEET).Range("C" & ii).Text
    If Trim(tenGV_raw) <> "" Then
        hpinf = GET_HP_INFO(HPCODE)
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso / SUM_heso
            'Dien thong tin mon LT tuong ung
            
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("H" & rowid) = SVNAME
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            Sheets(TARGET).Range("C" & rowid) = MALOP
            Sheets(TARGET).Range("D" & rowid) = HPCODE
            Sheets(TARGET).Range("E" & rowid) = HPNAME
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = class_type
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = siso_SV
            Sheets(TARGET).Range("M" & rowid) = HesoLop(siso_SV)
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT(PRGTYPE)
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT(PRGTYPE)
            If class_type = "DATN" Then
                Select Case PRGTYPE
                    Case "THSKT"
                        Sheets(TARGET).Range("P" & rowid).Value = 1.2 * gvrec(idx).heso
                    Case "THSKH"
                        Sheets(TARGET).Range("P" & rowid).Value = 1.5 * gvrec(idx).heso
                End Select
            End If
            rowid = rowid + 1
        Next
    End If
    ii = ii + 1
Loop


BEGIN_LATS:
DATA_SHEET = "NCS"
TARGET = "Tong_hop_GD"
ii = 3
Do While Sheets(DATA_SHEET).Range("B" & ii).Text <> "" ' Cot ten NCS
    TenNCS = Sheets(DATA_SHEET).Range("B" & ii).Value
    GVHD1 = Trim(Sheets(DATA_SHEET).Range("L" & ii).Value)
    GVHD2 = Trim(Sheets(DATA_SHEET).Range("M" & ii).Value)
    NCS_year = Sheets(DATA_SHEET).Range("F" & ii).Value
    NCS_daBV = Trim(Sheets(DATA_SHEET).Range("E" & ii).Value) <> ""
    If Not (NCS_daBV) Then
        If Trim(GVHD2) = "" Then 'Chi mot gv hd
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD1
            Sheets(TARGET).Range("P" & rowid).Value = 2#
            Sheets(TARGET).Range("B" & rowid).Value = HK1_NAME
            rowid = rowid + 1
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD1
            Sheets(TARGET).Range("P" & rowid).Value = 2#
            Sheets(TARGET).Range("B" & rowid).Value = HK2_NAME
            rowid = rowid + 1
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD1
            Sheets(TARGET).Range("P" & rowid).Value = 2#
            Sheets(TARGET).Range("R" & rowid).Value = 2# ' GD thuc tinh cho he
            Sheets(TARGET).Range("B" & rowid).Value = HK3_NAME
            rowid = rowid + 1
        Else
            'GV1
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD1
            Sheets(TARGET).Range("P" & rowid).Value = 1.2
            Sheets(TARGET).Range("B" & rowid).Value = HK1_NAME
            rowid = rowid + 1
            'GV1
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD1
            Sheets(TARGET).Range("P" & rowid).Value = 1.2
            Sheets(TARGET).Range("B" & rowid).Value = HK2_NAME
            rowid = rowid + 1
            'GV1
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD1
            Sheets(TARGET).Range("P" & rowid).Value = 1.2
            Sheets(TARGET).Range("R" & rowid).Value = 1.2 ' GD thuc tinh cho he
            Sheets(TARGET).Range("B" & rowid).Value = HK3_NAME
            rowid = rowid + 1
            'GV2
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD2
            Sheets(TARGET).Range("P" & rowid).Value = 0.8
            Sheets(TARGET).Range("B" & rowid).Value = HK1_NAME
            rowid = rowid + 1
            'GV2
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD2
            Sheets(TARGET).Range("P" & rowid).Value = 0.8
            Sheets(TARGET).Range("B" & rowid).Value = HK2_NAME
            rowid = rowid + 1
            'GV2
            Sheets(TARGET).Range("H" & rowid) = TenNCS
            Sheets(TARGET).Range("I" & rowid) = "LATS"
            Sheets(TARGET).Range("A" & rowid).Value = GVHD2
            Sheets(TARGET).Range("P" & rowid).Value = 0.8
            Sheets(TARGET).Range("R" & rowid).Value = 0.8 ' GD thuc tinh cho he
            Sheets(TARGET).Range("B" & rowid).Value = HK3_NAME
            rowid = rowid + 1
        End If
        
    End If
    ii = ii + 1
Loop
'Hoc phan Tien si
HPTS:
DATA_SHEET = "HPTS"
TARGET = "Tong_hop_GD"
ii = 2
Do While Sheets(DATA_SHEET).Range("B" & ii).Text <> "" ' Cot ten NCS
    HPCODE = Sheets(DATA_SHEET).Range("B" & ii).Value
    HPNAME = Sheets(DATA_SHEET).Range("C" & ii).Value
    tenGV_raw = Sheets(DATA_SHEET).Range("L" & ii).Value
    siso_SV = Sheets(DATA_SHEET).Range("G" & ii).Value
    HKNAME = Sheets(DATA_SHEET).Range("F" & ii).Value
    hpinf = GET_HP_INFO(HPCODE)
    noGV = 0
    substrings = Split(tenGV_raw, "-")
    For Each s In substrings
        noGV = noGV + 1
    Next
    ' tinh toan so luong giao vien va he so
    SUM_heso = 0
    For idx = 1 To noGV
        gvrec(idx) = get_GVNAME(substrings(idx - 1))
        SUM_heso = SUM_heso + gvrec(idx).heso
    Next
    If Trim(tenGV_raw) = "" Then
        'noGV = 1
        'gvrec(1).gvname = "CHUA PHAN CONG"
        'gvrec(1).heso = 1
        SUM_heso = 1
    End If
    For idx = 1 To noGV
        Sheets(TARGET).Range("A" & rowid) = gvrec(idx).gvname
        Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
        Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT(PRGTYPE)
        Sheets(TARGET).Range("I" & rowid) = "HPTS"
        Sheets(TARGET).Range("D" & rowid) = HPCODE
        Sheets(TARGET).Range("B" & rowid) = HKNAME 'Hoc ky, de ky 2 (chung)
        With hpinf
            Sheets(TARGET).Range("E" & rowid) = .TenHP
            Sheets(TARGET).Range("P" & rowid).Value = .TC * gvrec(idx).heso * siso_SV * 0.3
        End With
                            
        rowid = rowid + 1
    Next idx
    ii = ii + 1
Loop
'Chuyen de nghien cuu sinh
CD_NCS:
DATA_SHEET = "CD_NCS"
TARGET = "Tong_hop_GD"
ii = 2
Do While Sheets(DATA_SHEET).Range("B" & ii).Text <> "" ' Cot ten NCS
    TenNCS = Sheets(DATA_SHEET).Range("B" & ii).Value
    HKNAME = Sheets(DATA_SHEET).Range("F" & ii).Value
    tenGV_raw = Trim(Sheets(DATA_SHEET).Range("D" & ii).Value)
    noGV = 0
    substrings = Split(tenGV_raw, "-")
    For Each s In substrings
        noGV = noGV + 1
    Next
    ' tinh toan so luong giao vien va he so
    SUM_heso = 0
    For idx = 1 To noGV
        gvrec(idx) = get_GVNAME(substrings(idx - 1))
        SUM_heso = SUM_heso + gvrec(idx).heso
    Next
    
    'GVHD2 = Trim(Sheets(DATA_SHEET).Range("M" & ii).Value)
    'TenGV
    For idx = 1 To noGV
        gvrec(idx).heso = gvrec(idx).heso / SUM_heso
        Sheets(TARGET).Range("A" & rowid).Value = Trim(gvrec(idx).gvname)
        Sheets(TARGET).Range("B" & rowid).Value = HKNAME
        Sheets(TARGET).Range("I" & rowid).Value = "CDNCS"
        Sheets(TARGET).Range("H" & rowid).Value = TenNCS
        'Ten chuyen de
        Sheets(TARGET).Range("E" & rowid).Value = Sheets(DATA_SHEET).Range("E" & ii).Value
        Sheets(TARGET).Range("H" & rowid).Value = TenNCS
        Sheets(TARGET).Range("P" & rowid).Value = 1# * gvrec(idx).heso
    rowid = rowid + 1
    Next idx
    ii = ii + 1
    'rowid = rowid + 1
Loop
rowid = rowid - 1
Sheets("Internal").Range("B8").Value = rowid
' Correct names
For ii = 2 To rowid
    TEN_KHONG_DAU = bo_dau_tieng_viet2(Sheets("Tong_hop_GD").Range("A" & ii))
    'First, try by original data
    Sheets(TARGET).Range("Q" & ii).FormulaR1C1 = "=VLOOKUP(RC[-16],CSDLCB,3,FALSE)"
    'If #N/A, try using no-accent data
    If Sheets(TARGET).Range("Q" & ii).Text = "#N/A" Then
        kk = 2
        foundCB = False
        Do While Not (foundCB) And kk < 300
            If Sheets("CSDL_CB").Range("B" & kk).Value = TEN_KHONG_DAU Then
                foundCB = True
            Else
                kk = kk + 1
            End If
        Loop
        If foundCB Then
            Sheets(TARGET).Range("A" & ii).Value = Sheets("CSDL_CB").Range("A" & kk).Value
        End If
    End If
Next


With Sheets(TARGET).Range("A2:Q" & rowid)
        .Borders(xlEdgeLeft).LineStyle = xlContinuous
        .Borders(xlEdgeTop).LineStyle = xlContinuous
        .Borders(xlEdgeBottom).LineStyle = xlContinuous
        .Borders(xlEdgeRight).LineStyle = xlContinuous
        .Borders(xlInsideVertical).LineStyle = xlContinuous
        .Borders(xlInsideHorizontal).LineStyle = xlContinuous
    End With
Sheets("Internal").Range("B1").Value = rowid
Application.Calculation = xlAutomatic

Sheets("Sheet1").Range("C31").Value = "Finish at " + Str(Time())
End Sub
Private Function get_GVNAME(ten As String) As GVrecord
Dim tg As String, kk As Integer
tg = Trim(ten)
If tg = "" Then
    get_GVNAME.gvname = ten
    get_GVNAME.heso = 1
    Exit Function
End If
If Mid(tg, Len(tg), 1) = ")" Then
    kk = Len(tg)
    Do While Mid(tg, kk, 1) <> "("
        kk = kk - 1
    Loop
    get_GVNAME.gvname = Mid(tg, 1, kk - 1)
    get_GVNAME.heso = Val(Mid(tg, kk + 1, Len(tg) - kk))
Else
    get_GVNAME.gvname = ten
    get_GVNAME.heso = 1
End If
End Function
Private Function IS_LT(cltype As String) As Boolean
If cltype = "LT" Or cltype = "TN" Or cltype = "LT+BT" Or cltype = "LT+BT+TN" Or cltype = "LT+BT+TH" Then
    IS_LT = True
Else
    IS_LT = False ' Mon do an, khong duyet
End If
End Function
Private Function IS_DA(cltype_org As String) As Boolean
Dim cltype As String
cltype = bo_dau_tieng_viet2(cltype_org)
If cltype = "DA" Or cltype = "DATN" Then
    IS_DA = True
Else
    IS_DA = False ' Mon do an, khong duyet
End If
End Function
Private Function Find_student_prog(mssv As Long) As String ' Return student type as string KSCQ, CLC, CTTT
Dim cell As Range, rowid As Integer, tg As Integer
With Sheets("SVKD").Range("A:A")
    Set cell = .Find(What:=(mssv), LookAt:=xlWhole, MatchCase:=False)
    If Not cell Is Nothing Then
        rowid = cell.Row
        tg = Sheets("SVKD").Range("F" & rowid).Value
    Else
        tg = 0
    End If
End With
Select Case tg
    Case 781, 690, 890, 1103, 1215
        Find_student_prog = "KSTN"
    Case 1242, 1325, 844, 1065, 1211
        Find_student_prog = "KSCLC"
    Case 781, 1289, 1206, 1345, 1363, 1073, 696, 896, 1112
        Find_student_prog = "CTTT"
    Case Else
        Find_student_prog = "KSCQ"
End Select
End Function
Private Function Find_student_class(mssv As Long) As String ' Return student type as string KSCQ, CLC, CTTT
Dim cell As Range, rowid As Integer
With Sheets("SVKD").Range("A:A")
    Set cell = .Find(What:=(mssv), LookAt:=xlWhole, MatchCase:=False)
    If Not cell Is Nothing Then
        rowid = cell.Row
        Find_student_class = Sheets("SVKD").Range("P" & rowid).Value
    Else
        Find_student_class = ""
        Exit Function
    End If
End With

End Function
Private Function Find_student_ProgID(mssv As Long) As String ' Return student type as string KSCQ, CLC, CTTT
Dim cell As Range, rowid As Integer
With Sheets("SVKD").Range("A:A")
    Set cell = .Find(What:=(mssv), LookAt:=xlWhole, MatchCase:=False)
    If Not cell Is Nothing Then
        rowid = cell.Row
        Find_student_ProgID = Sheets("SVKD").Range("F" & rowid).Value
    Else
        Find_student_ProgID = ""
        Exit Function
    End If
End With

End Function
Private Function GET_HP_INFO(HPCODE As String) As HPINFO
Dim ii As Long
Dim ca1 As String, ca2 As String, ca3 As String, ca4 As String, kk As Integer
Dim found_sub As Boolean, tg1 As String, tg2() As String
Dim list As ListObject
Dim config As Worksheet
Dim cell As Range
Dim TCCODE As String
Dim tgres As HPINFO
found_sub = False
Set config = Sheets("MONKD")
Set list = config.ListObjects("EE_SUBJ")

'search in any cell of the data range of excel table
Set cell = list.DataBodyRange.Find(HPCODE)

If HPCODE = "EE3482" Then
    ii = ii + 0
End If
If cell Is Nothing Then
    'when information is not found
    tgres.TenHP = "SUBJ NOT FOUND"
Else
    'when information is found
    ii = cell.Row
    TCCODE = Sheets("MONKD").Range("E" & ii).Value
    tgres.HESODOAN = Sheets("MONKD").Range("H" & ii).Value ' Quy che hien nay, he so do an khong phu thuoc dai tra hay elitech
    tgres.HESODOAN_Summer = Val(Sheets("MONKD").Range("I" & ii).Text) '
    With tgres
        .MaHP = HPCODE
        .TenHP = Sheets("MONKD").Range("C" & ii).Value
        .TC = Sheets("MONKD").Range("D" & ii).Value
        '.LT = Val(Mid(TCCODE, 3, 1))
       ' .BT = Val(Mid(TCCODE, 5, 1))
       ' .TN = Val(Mid(TCCODE, 7, 1))
       kk = 1
       Do While Mid(TCCODE, kk, 1) <> "("
        kk = kk + 1
       Loop
        tg1 = Mid(TCCODE, kk + 1, Len(TCCODE) - kk) 'Does not work with HP more then 10 credits
        tg2 = Split(tg1, "-")
        .LT = Val(tg2(0))
        .BT = Val(tg2(1))
        .TN = Val(tg2(2))
    End With
    found_sub = True
End If
GET_HP_INFO = tgres
End Function
Private Function GET_HP_VB2_INFO(TCCODE As String) As HPINFO
Dim ii As Long
Dim ca1 As String, ca2 As String, ca3 As String, ca4 As String, kk As Integer
Dim found_sub As Boolean, tg1 As String, tg2() As String
Dim cell As Range

Dim tgres As HPINFO


With tgres
    .MaHP = ""
    .TenHP = ""
    
    kk = 1
    Do While Mid(TCCODE, kk, 1) <> "("
        kk = kk + 1
    Loop
    .TC = Val(Mid(TCCODE, 1, kk - 1))
    tg1 = Mid(TCCODE, kk + 1, Len(TCCODE) - kk) 'Does not work with HP more then 10 credits
    tg2 = Split(tg1, "-")
    .LT = Val(tg2(0))
    .BT = Val(tg2(1))
    .TN = Val(tg2(2))
End With


GET_HP_VB2_INFO = tgres
End Function
Private Function HesoLop(SISO As Integer) As Single
If SISO <= 60 Then
    HesoLop = 0
Else
    If SISO <= 120 Then
        HesoLop = 0.2
    Else
        If SISO < 180 Then
            HesoLop = 0.4
        Else
            If SISO <= 240 Then
                HesoLop = 0.6
            Else
                If SISO <= 300 Then
                    HesoLop = 0.8
                Else
                    HesoLop = 1
                End If
            End If
        End If
    End If
End If
End Function
Private Function Heso_LT_CTDT(PRGTYPE_org As String) As Single
Dim PRGTYPE As String
PRGTYPE = bo_dau_tieng_viet2(PRGTYPE_org)

    Select Case PRGTYPE
        Case "KSCQ", "CNCN", "Dai hoc dai tra"
            Heso_LT_CTDT = 1.5
        Case "KSCLC", "KSTN", "HEDSPI"
            Heso_LT_CTDT = 1.8
        Case "CTTT"
            Heso_LT_CTDT = 2
        Case "VB2", "SIE"
            Heso_LT_CTDT = 2
        Case "THSKT", "THSKH"
            Heso_LT_CTDT = 2
    End Select
End Function
Private Function Heso_DA_CTDT(PRGTYPE_org As String) As Single
Dim PRGTYPE As String
PRGTYPE = bo_dau_tieng_viet2(PRGTYPE_org)
    Select Case PRGTYPE
        Case "KSCQ", "CNCN", "Dai hoc dai tra"
            Heso_DA_CTDT = 0.12
        Case "KSCLC", "KSTN"
            Heso_DA_CTDT = 0.18
        Case "CTTT", "SIE"
            Heso_DA_CTDT = 0.2
        Case "VB2"
            Heso_DA_CTDT = 0.12
        Case "THSKT", "THSKH"
            Heso_DA_CTDT = 0.2
    End Select
End Function
Private Function Heso_TN_CTDT(PRGTYPE As String) As Single
    Select Case PRGTYPE
        Case "KSCQ", "CNCN"
            Heso_TN_CTDT = 1#
        Case "KSCLC", "KSTN"
            Heso_TN_CTDT = 1.5
        Case "CTTT", "SIE"
            Heso_TN_CTDT = 1.5
        Case "VB2"
            Heso_TN_CTDT = 1.5
    End Select
End Function

Private Function Heso_LT_CTDT_Summer(PRGTYPE_org As String) As Single
Dim PRGTYPE As String
PRGTYPE = bo_dau_tieng_viet2(PRGTYPE_org)

    Select Case PRGTYPE
        Case "KSCQ", "CNCN", "Dai hoc dai tra"
            Heso_LT_CTDT_Summer = 2.5
        Case "KSCLC", "KSTN", "HEDSPI"
            Heso_LT_CTDT_Summer = 1.8
        Case "CTTT", "SIE"
            Heso_LT_CTDT_Summer = 2
        Case "VB2", "SIE"
            Heso_LT_CTDT_Summer = 2
        Case "THSKT", "THSKH"
            Heso_LT_CTDT_Summer = 2
    End Select
End Function
Private Function Heso_TN_CTDT_Summer(PRGTYPE As String) As Single
    Select Case PRGTYPE
        Case "KSCQ", "CNCN"
            Heso_TN_CTDT_Summer = 1.5
        Case "KSCLC", "KSTN"
            Heso_TN_CTDT_Summer = 1.5
        Case "CTTT", "SIE"
            Heso_TN_CTDT_Summer = 1.5
        Case "VB2"
            Heso_TN_CTDT_Summer = 1.5
    End Select
End Function
Private Function Heso_DA_CTDT_Summer(PRGTYPE_org As String) As Single
Dim PRGTYPE As String
PRGTYPE = bo_dau_tieng_viet2(PRGTYPE_org)
    Select Case PRGTYPE
        Case "KSCQ", "CNCN", "Dai hoc dai tra"
            Heso_DA_CTDT_Summer = 0.3
        Case "KSCLC", "KSTN"
            Heso_DA_CTDT_Summer = 0.3 '.18, sua theo de nghi cua DKTK, bang voi chinh quy
        Case "CTTT"
            Heso_DA_CTDT_Summer = 0.3 '.2, sua theo de nghi cua DKTK, bang voi chinh quy
        Case "VB2"
            Heso_DA_CTDT_Summer = 0.12
        Case "THSKT", "THSKH"
            Heso_DA_CTDT_Summer = 0.2
    End Select
End Function

Sub Thu_thap_thong_tin_LVCH() '
' Chon thu muc, sau do copy toan bo thong tin cac file excel trong thu muc vao mot sheet destination
Dim fldr As Object, folder As String, fileName As String, outputFolder As String, wb As Workbook, app As Excel.Application
Dim ftype As String, flen As Integer, ii As Integer
Dim wb1 As Workbook, wb2 As Workbook
Dim SHEET As Worksheet
Dim pasteStart As Range
'Dim app As Excel.Application
    '----Select folder----

    '----Output directory---
    Sheets("LV_caohoc").Select
    Cells.Select
    Selection.ClearContents
    Set wb1 = ActiveWorkbook
    Set pasteStart = [LV_caohoc!A1]
    On Error GoTo 0
    
    fileName = "D:\HP1\Documents\OneDrive - Hanoi University of Science and Technology\DTCQ\SDH_2018_2019\LVTHS_2018_2019.xlsx"

    
            
            Set wb2 = Workbooks.Open(fileName)
            
            For Each SHEET In wb2.Sheets
                If SHEET.Name <> "Sheet1" Then 'Sheet Sheet1 chua thong tin khong can thiet
                    With SHEET.UsedRange
                        .Copy pasteStart
                        Set pasteStart = pasteStart.Offset(.Rows.Count)
                    End With
                End If
            Next SHEET

            wb2.Close
    
    
    
EndSub:
    'MsgBox "Finished!"
End Sub

Sub Thu_thap_thong_tin_GDCH() '
' Chon thu muc, sau do copy toan bo thong tin cac file excel trong thu muc vao mot sheet destination
Dim fldr As Object, folder As String, fileName As String, outputFolder As String, wb As Workbook, app As Excel.Application
Dim ftype As String, flen As Integer, ii As Integer
Dim wb1 As Workbook, wb2 As Workbook
Dim SHEET As Worksheet
Dim pasteStart As Range
'Dim app As Excel.Application
    '----Select folder----

    '----Output directory---
    Sheets("GD_Caohoc").Select
    Cells.Select
    Selection.ClearContents
    Set wb1 = ActiveWorkbook
    Set pasteStart = [GD_Caohoc!A1]
    On Error GoTo 0
    
    fileName = "D:\HP1\Documents\OneDrive - Hanoi University of Science and Technology\DTCQ\SDH_2018_2019\Giang_day_SDH_2018_2019.xlsx"

    
            
            Set wb2 = Workbooks.Open(fileName)
            
            For Each SHEET In wb2.Sheets
                If SHEET.Name = "MON_CH" Then 'Chi lay thong tin tu sheet 1
                    With SHEET.UsedRange
                        .Copy pasteStart
                        Set pasteStart = pasteStart.Offset(.Rows.Count)
                    End With
                End If
            Next SHEET

            wb2.Close
    
    
    
EndSub:
    'MsgBox "Finished!"
End Sub
Sub SORT_BY_DEPARTMENT()
Dim kk As Integer, rowid As Integer
Dim num_of_record As Integer, numTK As Integer, fname As String, DVNAME(1 To 6000) As String
Dim tg As Variant, sname As String, THINHGIANG As Boolean, last_row As Long
Dim savepath As String, savepath_all As String
Dim newWB As Workbook, newS As Worksheet
Sheets("Tong_hop_GD").Select

last_row = Sheets("Internal").Range("B1").Value
'savepath = Sheets("Internal").Range("B2").Value
'savepath_all = Sheets("Internal").Range("B3").Value
'MsgBox ActiveWorkbook.Path

savepath = ActiveWorkbook.Path & "\Public\"
savepath_all = ActiveWorkbook.Path & "\Tong hop GD2019-2020\"

For kk = 2 To last_row
    DVNAME(kk - 1) = (Range("Q" & kk).Text)
Next
tg = RemoveDupesColl(DVNAME)
kk = 1
Do While tg(kk) <> ""
    kk = kk + 1
Loop
numTK = kk - 1
For kk = 1 To numTK
    Call Extract_record(last_row, tg(kk))
    If tg(kk) = "#N/A" Then
        tg(kk) = "CHUA_RO_CAN_XEM_LAI"
    End If
    sname = savepath + tg(kk) + ".xlsx"
    Call Paste_to_new(sname, last_row, "R")
Next
ActiveSheet.Range("$A$1:$R$" & last_row).AutoFilter Field:=17
sname = savepath_all + "GD_SOURCE.xlsx"
Call Paste_to_new(sname, last_row, "R")

'Thong tin tong hop khac
fname = savepath_all + "Tong hop 2019-2020.xlsx"
ActiveWorkbook.Sheets("Giaoket").Cells.Copy
Set newWB = Workbooks.Add
With newWB
    Set newS = newWB.Sheets("Sheet1")
    newS.Range("A1").PasteSpecial Paste:=xlPasteAll
    'Set newS = newWB.Sheets.Add
    
    'Workbooks("GD2019_2020.xlsm").Sheets("Giao_ket").Activate
    'ActiveChart.ChartArea.Select
    'Application.CutCopyMode = False
    'ActiveChart.ChartArea.Copy
     
    'newWB.Activate
    'ActiveSheet.Paste
    
    'ActiveSheet.ChartObjects("Chart 1").Activate
    'ActiveChart.Location Where:=xlLocationAsNewSheet, Name:="Giao_ket"
    Application.DisplayAlerts = False
    .SaveAs fileName:=fname, FileFormat:=xlOpenXMLWorkbook
    .Close
    Application.DisplayAlerts = True
End With


End Sub
Function RemoveDupesColl(MyArray As Variant) As Variant
'DESCRIPTION: Removes duplicates from your array using the collection method.
'NOTES: (1) This function returns unique elements in your array, but
' it converts your array elements to strings.
'SOURCE: https://wellsr.com
'-----------------------------------------------------------------------
    Dim i As Long
    Dim arrColl As New Collection
    Dim arrDummy() As Variant
    Dim arrDummy1() As Variant
    Dim item As Variant
    ReDim arrDummy1(LBound(MyArray) To UBound(MyArray))

    For i = LBound(MyArray) To UBound(MyArray) 'convert to string
        arrDummy1(i) = CStr(MyArray(i))
    Next i
    On Error Resume Next
    For Each item In arrDummy1
       arrColl.Add item, item
    Next item
    Err.Clear
    ReDim arrDummy(LBound(MyArray) To arrColl.Count + LBound(MyArray) - 1)
    i = LBound(MyArray)
    For Each item In arrColl
       arrDummy(i) = item
       i = i + 1
    Next item
    RemoveDupesColl = arrDummy
End Function
Function getDimension(var As Variant) As Long
    On Error GoTo Err
    Dim i As Long
    Dim tmp As Long
    i = 0
    Do While True
        i = i + 1
        tmp = UBound(var, i)
    Loop
Err:
    getDimension = i - 1
End Function

Private Sub Extract_record(last_row, tkname)
    ActiveSheet.Range("$A$6:$WWD$" & last_row).AutoFilter Field:=17, Criteria1:=tkname
End Sub

Private Sub Paste_to_new(fname As String, last_row As Long, last_col As String)
Dim newWB As Workbook, currentWB As Workbook
Dim newS As Worksheet, currentS As Worksheet
Dim range_str As String
range_str = "A1:" + Trim((last_col)) + Trim(Str(last_row))
'Copy the data you need
Set currentWB = ThisWorkbook
Set currentS = currentWB.Sheets("Tong_hop_GD")
currentS.Range(range_str).Select
Selection.Copy

'Export sheet for Departments
Set newWB = Workbooks.Add
    With newWB
        Set newS = newWB.Sheets("Sheet1")
        newS.Range("A1").PasteSpecial Paste:=xlPasteValues
        newS.Range("A1").PasteSpecial Paste:=xlPasteFormats
        'nn
        'newS.Range("A1").PasteSpecial Paste:=xlPasteFormulas
        If last_col = "P" Then 'GD
            newS.Range("A1").PasteSpecial Paste:=xlPasteFormulas
        End If
        newS.Cells.Select
        Format_AUTO_COLs
        
        Cells.Select
        'Cells.EntireColumn.AutoFit
        Cells.EntireRow.AutoFit
        'Columns("A:E").EntireColumn.AutoFit
        'Columns("H").EntireColumn.AutoFit
        Application.DisplayAlerts = False
        On Error Resume Next
        .SaveAs fileName:=fname, FileFormat:=xlOpenXMLWorkbook
        Application.DisplayAlerts = True
        .Close
    End With

End Sub
Sub Check_Dupplicate_DA()
Dim kk As Long
Dim TARGETSHEET As String
Dim last_mssv As Long, last_class_code As Long, last_drop As String
Dim mssv As Long, class_code As Long, drop As String

TARGETSHEET = "DA_20181"
BEGIN_SWEEP:
kk = 2
Do While Sheets(TARGETSHEET).Range("E" & kk).Value <> 0
    kk = kk + 1
Loop
Sheets(TARGETSHEET).Range("I2:I" & kk).Clear
Call Sort_DA_BY_MSSV(TARGETSHEET, kk - 1)
kk = 2
Do While Sheets(TARGETSHEET).Range("E" & kk).Value <> 0
    mssv = Sheets(TARGETSHEET).Range("E" & kk).Value
    class_code = Sheets(TARGETSHEET).Range("B" & kk).Value
    drop = Sheets(TARGETSHEET).Range("H" & kk).Value
    If mssv = last_mssv And last_class_code = class_code And StrComp(drop, last_drop) = 0 Then
        Sheets(TARGETSHEET).Range("I" & kk - 1).Value = 1
        Sheets(TARGETSHEET).Range("I" & kk).Value = Sheets(TARGETSHEET).Range("I" & kk - 1).Value + 1
    End If
    last_drop = drop
    last_mssv = mssv
    last_class_code = class_code
    kk = kk + 1
Loop
If TARGETSHEET = "DA_20181" Then
    TARGETSHEET = "DA_20182"
    GoTo BEGIN_SWEEP
End If
End Sub
Sub Correct_prgType_DA()
'sub nay dung de chinh sua chuong trinh dao tao cua cac entries mon Do an. Mot so sinh vien he CTTT, KSTN dang ky ma cac mon do an vao lop thuong,
'vi vay khi tinh khoi luong chuong trinh tinh khong xac dinh dung he so
Dim ii As Long, DATASHEET As String, mssv As Long, kk As Long
Dim list As ListObject, cell As Range, config As Worksheet
Dim LOP_SV As String, PRGTYPE As String
Set config = Sheets("SVDATA")
Set list = config.ListObjects("CSDLSV")

DATASHEET = "DA_20181"
BEGIN_SWEEP:
ii = 2
Do While Sheets(DATASHEET).Range("E" & ii).Text <> ""
    mssv = Val(Sheets(DATASHEET).Range("E" & ii).Text)
    Set cell = list.DataBodyRange.Find(mssv)
    If cell Is Nothing Then
    Else
        kk = cell.Row
        LOP_SV = Sheets("SVDATA").Range("D" & kk).Value
        PRGTYPE = check_prg_from_class_name(LOP_SV)
    Select Case PRGTYPE 'correct if prgtype change
            Case "KSTN"
                Sheets(DATASHEET).Range("G" & ii).Value = "KSTN"
            Case "CTTT"
                Sheets(DATASHEET).Range("G" & ii).Value = "CTTT"
            Case "KSCLC"
                Sheets(DATASHEET).Range("G" & ii).Value = "KSCLC"
        End Select
    End If
    ii = ii + 1
Loop
If DATASHEET = "DA_20182" Then
Else
    DATASHEET = "DA_20182"
    GoTo BEGIN_SWEEP
End If
End Sub

Private Function check_prg_from_class_name(lopsv As String) As String
check_prg_from_class_name = "KSCQ" 'by default
If InStr(1, lopsv, "KSTN") Then
    check_prg_from_class_name = "KSTN"
End If
If InStr(1, lopsv, "CTTT") Or InStr(1, lopsv, "TT.") Then
    check_prg_from_class_name = "CTTT"
End If
If InStr(1, lopsv, "KSCLC") Then
    check_prg_from_class_name = "KSCLC"
End If
End Function
Private Function cross_check_mon_TN(MaHP As String) As String
'Sub nay xac dinh mon thuoc ct hoc nao, neu thuoc ctt ,kstn, ksclc thi can hieu chinh GD
Dim DATASHEET As String, ctname As String, ii As Integer
DATASHEET = "MONHOC_CT"
ii = 2
Do While Sheets(DATASHEET).Range("A" & ii).Text <> ""
    If StrComp(Sheets(DATASHEET).Range("A" & ii).Text, MaHP) = 0 Then
        ctname = Sheets(DATASHEET).Range("C" & ii).Text
        cross_check_mon_TN = check_prg_from_class_name(ctname)
        Exit Function
    End If
    ii = ii + 1
Loop
cross_check_mon_TN = ""
End Function
Sub Tinh_GD_Nhapmon()
Dim ii As Long, kk As Long, mssv As Long
Dim TARGETSHEET As String
Dim list As ListObject, cell As Range, config As Worksheet
Dim LOP_SV As String, PRGTYPE As String
Set config = Sheets("SVDATA")
Set list = config.ListObjects("CSDLSV")

TARGETSHEET = "Nhapmon_ky1"
BEGIN_NHAPMON:
ii = 2
Do While Sheets(TARGETSHEET).Range("A" & ii).Text <> ""
    mssv = Val(Sheets(TARGETSHEET).Range("A" & ii).Text)
    Set cell = list.DataBodyRange.Find(mssv)
    If cell Is Nothing Then 'We assume KSCQ
        Sheets(TARGETSHEET).Range("F" & ii).Value = 0.025
    Else
        kk = cell.Row
        LOP_SV = Sheets("SVDATA").Range("D" & kk).Value
        PRGTYPE = check_prg_from_class_name(LOP_SV)
        Select Case PRGTYPE
            Case "KSTN", "KSCLC", "CTTT"
                Sheets(TARGETSHEET).Range("F" & ii).Value = 0.035
            Case Else
                Sheets(TARGETSHEET).Range("F" & ii).Value = 0.025
        End Select
    End If
    ii = ii + 1
Loop
If TARGETSHEET = "Nhapmon_ky1" Then
    TARGETSHEET = "Nhapmon_ky2"
    GoTo BEGIN_NHAPMON
End If
End Sub
Private Sub Sort_DA_BY_MSSV(TARGETSHEET As String, nrow As Long)
'
' Macro1 Macro
'
Dim rg1 As String, rg2 As String, rg3 As String
'
rg1 = "E2:E" + Trim(Str(nrow))
rg2 = "B2:B" + Trim(Str(nrow))
rg3 = "H2:H" + Trim(Str(nrow))
    ActiveWorkbook.Worksheets(TARGETSHEET).Sort.SortFields.Clear
    ActiveWorkbook.Worksheets(TARGETSHEET).Sort.SortFields.Add Key:=Range( _
        rg1), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    ActiveWorkbook.Worksheets(TARGETSHEET).Sort.SortFields.Add Key:=Range( _
        rg2), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    ActiveWorkbook.Worksheets(TARGETSHEET).Sort.SortFields.Add Key:=Range( _
        rg3), SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:= _
        xlSortNormal
    With ActiveWorkbook.Worksheets(TARGETSHEET).Sort
        .SetRange Range("A1:I" & nrow)
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
End Sub
Private Function bo_dau_tieng_viet2(Text As String) As String
  Dim AsciiDict(1 To 10000) As String
  
  AsciiDict(97) = "a"
  AsciiDict(192) = "A"
  AsciiDict(193) = "A"
  AsciiDict(194) = "A"
  AsciiDict(195) = "A"
  AsciiDict(196) = "A"
  AsciiDict(197) = "A"
  AsciiDict(199) = "C"
  AsciiDict(200) = "E"
  AsciiDict(201) = "E"
  AsciiDict(202) = "E"
  AsciiDict(203) = "E"
  AsciiDict(204) = "I"
  AsciiDict(205) = "I"
  AsciiDict(206) = "I"
  AsciiDict(207) = "I"
  AsciiDict(208) = "D"
  AsciiDict(209) = "N"
  AsciiDict(210) = "O"
  AsciiDict(211) = "O"
  AsciiDict(212) = "O"
  AsciiDict(213) = "O"
  AsciiDict(214) = "O"
  AsciiDict(217) = "U"
  AsciiDict(218) = "U"
  AsciiDict(219) = "U"
  AsciiDict(220) = "U"
  AsciiDict(221) = "Y"
  AsciiDict(224) = "a"
  AsciiDict(225) = "a"
  AsciiDict(226) = "a"
  AsciiDict(227) = "a"
  AsciiDict(228) = "a"
  AsciiDict(229) = "a"
  AsciiDict(231) = "c"
  AsciiDict(232) = "e"
  AsciiDict(233) = "e"
  AsciiDict(234) = "e"
  AsciiDict(235) = "e"
  AsciiDict(236) = "i"
  AsciiDict(237) = "i"
  AsciiDict(238) = "i"
  AsciiDict(239) = "i"
  AsciiDict(240) = "d"
  AsciiDict(241) = "n"
  AsciiDict(242) = "o"
  AsciiDict(243) = "o"
  AsciiDict(244) = "o"
  AsciiDict(245) = "o"
  AsciiDict(246) = "o"
  AsciiDict(249) = "u"
  AsciiDict(250) = "u"
  AsciiDict(251) = "u"
  AsciiDict(252) = "u"
  AsciiDict(253) = "y"
  AsciiDict(255) = "y"
  AsciiDict(352) = "S"
  AsciiDict(353) = "s"
  AsciiDict(376) = "Y"
  AsciiDict(381) = "Z"
  AsciiDict(382) = "z"
  AsciiDict(258) = "A"
  AsciiDict(259) = "a"
  AsciiDict(272) = "D"
  AsciiDict(273) = "d"
  AsciiDict(296) = "I"
  AsciiDict(297) = "i"
  AsciiDict(360) = "U"
  AsciiDict(361) = "u"
  AsciiDict(416) = "O"
  AsciiDict(417) = "o"
  AsciiDict(431) = "U"
  AsciiDict(432) = "u"
  AsciiDict(7840) = "A"
  AsciiDict(7841) = "a"
  AsciiDict(7842) = "A"
  AsciiDict(7843) = "a"
  AsciiDict(7844) = "A"
  AsciiDict(7845) = "a"
  AsciiDict(7846) = "A"
  AsciiDict(7847) = "a"
  AsciiDict(7848) = "A"
  AsciiDict(7849) = "a"
  AsciiDict(7850) = "A"
  AsciiDict(7851) = "a"
  AsciiDict(7852) = "A"
  AsciiDict(7853) = "a"
  AsciiDict(7854) = "A"
  AsciiDict(7855) = "a"
  AsciiDict(7856) = "A"
  AsciiDict(7857) = "a"
  AsciiDict(7858) = "A"
  AsciiDict(7859) = "a"
  AsciiDict(7860) = "A"
  AsciiDict(7861) = "a"
  AsciiDict(7862) = "A"
  AsciiDict(7863) = "a"
  AsciiDict(7864) = "E"
  AsciiDict(7865) = "e"
  AsciiDict(7866) = "E"
  AsciiDict(7867) = "e"
  AsciiDict(7868) = "E"
  AsciiDict(7869) = "e"
  AsciiDict(7870) = "E"
  AsciiDict(7871) = "e"
  AsciiDict(7872) = "E"
  AsciiDict(7873) = "e"
  AsciiDict(7874) = "E"
  AsciiDict(7875) = "e"
  AsciiDict(7876) = "E"
  AsciiDict(7877) = "e"
  AsciiDict(7878) = "E"
  AsciiDict(7879) = "e"
  AsciiDict(7880) = "I"
  AsciiDict(7881) = "i"
  AsciiDict(7882) = "I"
  AsciiDict(7883) = "i"
  AsciiDict(7884) = "O"
  AsciiDict(7885) = "o"
  AsciiDict(7886) = "O"
  AsciiDict(7887) = "o"
  AsciiDict(7888) = "O"
  AsciiDict(7889) = "o"
  AsciiDict(7890) = "O"
  AsciiDict(7891) = "o"
  AsciiDict(7892) = "O"
  AsciiDict(7893) = "o"
  AsciiDict(7894) = "O"
  AsciiDict(7895) = "o"
  AsciiDict(7896) = "O"
  AsciiDict(7897) = "o"
  AsciiDict(7898) = "O"
  AsciiDict(7899) = "o"
  AsciiDict(7900) = "O"
  AsciiDict(7901) = "o"
  AsciiDict(7902) = "O"
  AsciiDict(7903) = "o"
  AsciiDict(7904) = "O"
  AsciiDict(7905) = "o"
  AsciiDict(7906) = "O"
  AsciiDict(7907) = "o"
  AsciiDict(7908) = "U"
  AsciiDict(7909) = "u"
  AsciiDict(7910) = "U"
  AsciiDict(7911) = "u"
  AsciiDict(7912) = "U"
  AsciiDict(7913) = "u"
  AsciiDict(7914) = "U"
  AsciiDict(7915) = "u"
  AsciiDict(7916) = "U"
  AsciiDict(7917) = "u"
  AsciiDict(7918) = "U"
  AsciiDict(7919) = "u"
  AsciiDict(7920) = "U"
  AsciiDict(7921) = "u"
  AsciiDict(7922) = "Y"
  AsciiDict(7923) = "y"
  AsciiDict(7924) = "Y"
  AsciiDict(7925) = "y"
  AsciiDict(7926) = "Y"
  AsciiDict(7927) = "y"
  AsciiDict(7928) = "Y"
  AsciiDict(7929) = "y"
  AsciiDict(8363) = "d"
  Text = Trim(Text)
  If Text = "" Then Exit Function
  Dim Char As String, _
    NormalizedText As String, _
    UnicodeCharCode As Long, _
    i As Long
  'Remove accent marks (diacritics) from text
  For i = 1 To Len(Text)
    Char = Mid(Text, i, 1)
    UnicodeCharCode = AscW(Char)
    
    If (UnicodeCharCode < 0) Then
      'See http://support.microsoft.com/kb/272138
      UnicodeCharCode = 65536 + UnicodeCharCode
    End If
    If UnicodeCharCode <= 122 Then
        NormalizedText = NormalizedText & Char
    Else
        NormalizedText = NormalizedText & AsciiDict(UnicodeCharCode) 'Char
    End If
  Next
  bo_dau_tieng_viet2 = NormalizedText
End Function
Private Function bo_dau_tieng_viet(Text As String) As String
  Dim AsciiDict As Object
  Set AsciiDict = CreateObject("scripting.dictionary")
  AsciiDict(97) = "a"
  AsciiDict(192) = "A"
  AsciiDict(193) = "A"
  AsciiDict(194) = "A"
  AsciiDict(195) = "A"
  AsciiDict(196) = "A"
  AsciiDict(197) = "A"
  AsciiDict(199) = "C"
  AsciiDict(200) = "E"
  AsciiDict(201) = "E"
  AsciiDict(202) = "E"
  AsciiDict(203) = "E"
  AsciiDict(204) = "I"
  AsciiDict(205) = "I"
  AsciiDict(206) = "I"
  AsciiDict(207) = "I"
  AsciiDict(208) = "D"
  AsciiDict(209) = "N"
  AsciiDict(210) = "O"
  AsciiDict(211) = "O"
  AsciiDict(212) = "O"
  AsciiDict(213) = "O"
  AsciiDict(214) = "O"
  AsciiDict(217) = "U"
  AsciiDict(218) = "U"
  AsciiDict(219) = "U"
  AsciiDict(220) = "U"
  AsciiDict(221) = "Y"
  AsciiDict(224) = "a"
  AsciiDict(225) = "a"
  AsciiDict(226) = "a"
  AsciiDict(227) = "a"
  AsciiDict(228) = "a"
  AsciiDict(229) = "a"
  AsciiDict(231) = "c"
  AsciiDict(232) = "e"
  AsciiDict(233) = "e"
  AsciiDict(234) = "e"
  AsciiDict(235) = "e"
  AsciiDict(236) = "i"
  AsciiDict(237) = "i"
  AsciiDict(238) = "i"
  AsciiDict(239) = "i"
  AsciiDict(240) = "d"
  AsciiDict(241) = "n"
  AsciiDict(242) = "o"
  AsciiDict(243) = "o"
  AsciiDict(244) = "o"
  AsciiDict(245) = "o"
  AsciiDict(246) = "o"
  AsciiDict(249) = "u"
  AsciiDict(250) = "u"
  AsciiDict(251) = "u"
  AsciiDict(252) = "u"
  AsciiDict(253) = "y"
  AsciiDict(255) = "y"
  AsciiDict(352) = "S"
  AsciiDict(353) = "s"
  AsciiDict(376) = "Y"
  AsciiDict(381) = "Z"
  AsciiDict(382) = "z"
  AsciiDict(258) = "A"
  AsciiDict(259) = "a"
  AsciiDict(272) = "D"
  AsciiDict(273) = "d"
  AsciiDict(296) = "I"
  AsciiDict(297) = "i"
  AsciiDict(360) = "U"
  AsciiDict(361) = "u"
  AsciiDict(416) = "O"
  AsciiDict(417) = "o"
  AsciiDict(431) = "U"
  AsciiDict(432) = "u"
  AsciiDict(7840) = "A"
  AsciiDict(7841) = "a"
  AsciiDict(7842) = "A"
  AsciiDict(7843) = "a"
  AsciiDict(7844) = "A"
  AsciiDict(7845) = "a"
  AsciiDict(7846) = "A"
  AsciiDict(7847) = "a"
  AsciiDict(7848) = "A"
  AsciiDict(7849) = "a"
  AsciiDict(7850) = "A"
  AsciiDict(7851) = "a"
  AsciiDict(7852) = "A"
  AsciiDict(7853) = "a"
  AsciiDict(7854) = "A"
  AsciiDict(7855) = "a"
  AsciiDict(7856) = "A"
  AsciiDict(7857) = "a"
  AsciiDict(7858) = "A"
  AsciiDict(7859) = "a"
  AsciiDict(7860) = "A"
  AsciiDict(7861) = "a"
  AsciiDict(7862) = "A"
  AsciiDict(7863) = "a"
  AsciiDict(7864) = "E"
  AsciiDict(7865) = "e"
  AsciiDict(7866) = "E"
  AsciiDict(7867) = "e"
  AsciiDict(7868) = "E"
  AsciiDict(7869) = "e"
  AsciiDict(7870) = "E"
  AsciiDict(7871) = "e"
  AsciiDict(7872) = "E"
  AsciiDict(7873) = "e"
  AsciiDict(7874) = "E"
  AsciiDict(7875) = "e"
  AsciiDict(7876) = "E"
  AsciiDict(7877) = "e"
  AsciiDict(7878) = "E"
  AsciiDict(7879) = "e"
  AsciiDict(7880) = "I"
  AsciiDict(7881) = "i"
  AsciiDict(7882) = "I"
  AsciiDict(7883) = "i"
  AsciiDict(7884) = "O"
  AsciiDict(7885) = "o"
  AsciiDict(7886) = "O"
  AsciiDict(7887) = "o"
  AsciiDict(7888) = "O"
  AsciiDict(7889) = "o"
  AsciiDict(7890) = "O"
  AsciiDict(7891) = "o"
  AsciiDict(7892) = "O"
  AsciiDict(7893) = "o"
  AsciiDict(7894) = "O"
  AsciiDict(7895) = "o"
  AsciiDict(7896) = "O"
  AsciiDict(7897) = "o"
  AsciiDict(7898) = "O"
  AsciiDict(7899) = "o"
  AsciiDict(7900) = "O"
  AsciiDict(7901) = "o"
  AsciiDict(7902) = "O"
  AsciiDict(7903) = "o"
  AsciiDict(7904) = "O"
  AsciiDict(7905) = "o"
  AsciiDict(7906) = "O"
  AsciiDict(7907) = "o"
  AsciiDict(7908) = "U"
  AsciiDict(7909) = "u"
  AsciiDict(7910) = "U"
  AsciiDict(7911) = "u"
  AsciiDict(7912) = "U"
  AsciiDict(7913) = "u"
  AsciiDict(7914) = "U"
  AsciiDict(7915) = "u"
  AsciiDict(7916) = "U"
  AsciiDict(7917) = "u"
  AsciiDict(7918) = "U"
  AsciiDict(7919) = "u"
  AsciiDict(7920) = "U"
  AsciiDict(7921) = "u"
  AsciiDict(7922) = "Y"
  AsciiDict(7923) = "y"
  AsciiDict(7924) = "Y"
  AsciiDict(7925) = "y"
  AsciiDict(7926) = "Y"
  AsciiDict(7927) = "y"
  AsciiDict(7928) = "Y"
  AsciiDict(7929) = "y"
  AsciiDict(8363) = "d"
  Text = Trim(Text)
  If Text = "" Then Exit Function
  Dim Char As String, _
    NormalizedText As String, _
    UnicodeCharCode As Long, _
    i As Long
  'Remove accent marks (diacritics) from text
  For i = 1 To Len(Text)
    Char = Mid(Text, i, 1)
    UnicodeCharCode = AscW(Char)
    
    If (UnicodeCharCode < 0) Then
      'See http://support.microsoft.com/kb/272138
      UnicodeCharCode = 65536 + UnicodeCharCode
    End If
    If AsciiDict.Exists(UnicodeCharCode) Then
      NormalizedText = NormalizedText & AsciiDict.item(UnicodeCharCode)
    Else
      NormalizedText = NormalizedText & ChrW(UnicodeCharCode) 'Char
    End If
  Next
  bo_dau_tieng_viet = NormalizedText
End Function


Private Sub Format_AUTO_COLs()
'
' Macro2 Macro
'

'
    Columns("A:A").EntireColumn.AutoFit
    Columns("B:B").ColumnWidth = 7.86
    Columns("C:C").ColumnWidth = 7.71
    Columns("D:D").ColumnWidth = 8.14
    Columns("F:F").ColumnWidth = 4.57
    Columns("G:G").ColumnWidth = 4.29
    Columns("H:H").EntireColumn.AutoFit
    Columns("I:I").ColumnWidth = 6.86
    Columns("J:J").ColumnWidth = 7.14
    Columns("K:K").ColumnWidth = 5
    Columns("L:L").ColumnWidth = 5.57
    Columns("M:M").ColumnWidth = 5.86
    Columns("N:N").ColumnWidth = 4.29
    Columns("O:O").ColumnWidth = 6
    Columns("E:E").ColumnWidth = 27
    Columns("P:P").ColumnWidth = 4
    Columns("Q:Q").ColumnWidth = 27
    Rows("1:1").EntireRow.AutoFit
End Sub
Sub Tinh_Hoc_Phi()
Dim ii As Integer, classtype As String, mssv As Long, MaHP As String
Dim student_prog As String, hpinf As HPINFO, hocphi As Single
ii = 2
Do While Sheets("DS_ky1").Range("G" & ii).Value <> ""
    mssv = Val(Sheets("DS_ky1").Range("G" & ii).Text)
    classtype = Sheets("DS_ky1").Range("E" & ii).Value
    MaHP = Sheets("DS_ky1").Range("C" & ii).Value
    student_prog = Find_student_prog(mssv)
    If classtype <> "TN" Then
        hpinf = GET_HP_INFO(MaHP)
        With hpinf
            If bo_dau_tieng_viet2(classtype) = "DA" Then
            Select Case student_prog
                Case "KSCQ"
                    hocphi = (.BT + .LT + 1.5 * .TN) * 400000#
                Case "KSTN"
                    hocphi = (.BT + .LT + 1.5 * .TN) * 440000#
                Case "CTTT"
                    hocphi = (.BT + .LT + 1.5 * .TN) * 540000#
            End Select
            End If
        End With
        Sheets("DS_ky1").Range("O" & ii).Value = hocphi
    End If
    ii = ii + 1
Loop
End Sub
Sub SORT_CURRENT_CELL()
    Dim sort_status As Integer, cell_content As String, sort_col As Integer, cur_col As Integer, last_row As Integer
    sort_status = Sheets("Internal").Range("B6").Value
    cur_col = ActiveCell.Column
    sort_col = Sheets("Internal").Range("B7").Value
    last_row = Sheets("Internal").Range("B1").Value
    cell_content = ActiveCell.Value
    If sort_status = 0 Then ' Not being sorted
        sort_status = 1
        Sheets("Internal").Range("B6").Value = sort_status
        Sheets("Internal").Range("B7").Value = ActiveCell.Column
        ActiveSheet.Range("A2:Q" & last_row).AutoFilter Field:=cur_col, Criteria1:=cell_content
    Else
        ActiveSheet.Range("A2:Q" & last_row).AutoFilter Field:=sort_col
        sort_status = 0
        Sheets("Internal").Range("B6").Value = sort_status
    End If
    
End Sub
Sub ListSheets() 'List all sheets in wb
 
Dim ws As Worksheet
Dim x As Integer
 
x = 1
 
Sheets("Sheet1").Range("G:G").Clear
 
For Each ws In Worksheets
     Sheets("Sheet1").Cells(x, 7) = ws.Name
     x = x + 1
Next ws
 
End Sub

Sub Tong_hop_GD_He()
Dim ii As Integer, rowid As Integer, s As Variant, idx As Integer, class_type As String, kk As Integer, foundCB As Boolean
Dim tenGV_raw As String, tenGV As String, heso As Single, SUM_heso As Single
Dim substrings() As String, noGV As Integer, gvrec(1 To 100) As GVrecord, DATA_SHEET As String, TARGET As String
Dim MALOP As Long, HPNAME As String, PRGTYPE As String, HPCODE As String, mssv As Long
Dim HKNAME As Long, hpinf As HPINFO, siso_SV As Integer, TENLOP As String, SEMESTER As String
Dim SVNAME As String, tg1 As String, tg2 As String, TEN_KHONG_DAU As String
Dim TCCODE As String
'Luan an TS
Dim TenNCS As String, GVHD1 As String, GVHD2 As String
Dim NCS_daBV As Boolean, NCS_year As String

Sheets("Sheet1").Range("C30").Value = "Start at " + Str(Time())

TARGET = "Tong_hop_GD"
rowid = Sheets("Internal").Range("B8").Value
Application.Calculation = xlManual
DATA_SHEET = "Phancong_ky3"
TARGET = "Tong_hop_GD"
HKNAME = HK3_NAME
ii = 2
'======= LT UNDERGRAD =============================================
BEGIN_LT: 'GD ly thuyet va thi  nghiem, Dai hoc
Do While Sheets(DATA_SHEET).Range("A" & ii).Text <> ""
    
    tenGV_raw = Sheets(DATA_SHEET).Range("O" & ii).Text
    class_type = Sheets(DATA_SHEET).Range("K" & ii).Text
    MALOP = Val(Sheets(DATA_SHEET).Range("C" & ii).Text)
    HPCODE = Sheets(DATA_SHEET).Range("D" & ii).Text
    HPNAME = Sheets(DATA_SHEET).Range("E" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("G" & ii).Text
    siso_SV = Val(Sheets(DATA_SHEET).Range("I" & ii).Text)
    TENLOP = Sheets(DATA_SHEET).Range("F" & ii).Text
    'If Trim(tenGV_raw) <> "" And IS_LT(class_type) Then
    If IS_LT(class_type) Then
        hpinf = GET_HP_INFO(HPCODE)
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        If noGV = 0 Then 'mon hoc chua duoc phan cong
            noGV = 1
            gvrec(1).heso = 1
            gvrec(1).gvname = "CHUA PHAN CONG"
            SUM_heso = 1
        End If
        
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso ' / SUM_heso
            'Dien thong tin mon LT tuong ung
            
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            Sheets(TARGET).Range("C" & rowid) = MALOP
            
            Sheets(TARGET).Range("D" & rowid) = HPCODE
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = class_type
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = siso_SV
            Sheets(TARGET).Range("M" & rowid) = HesoLop(siso_SV)
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT_Summer(PRGTYPE)
            
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT_Summer(PRGTYPE)
            Sheets(TARGET).Range("H" & rowid) = TENLOP
            If siso_SV > 0 Then
                If class_type = "TN" Then
                    Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=RC[-10]*(RC[-1]+RC[-3])*RC[-4]"
                Else 'LT + BT
                    If siso_SV >= 5# Then ' Really a LT class
                        Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=(RC[-10]+RC[-9])*(RC[-3]+RC[-2])*RC[-4]"
                    Else 'Lop Project, tinh nhu do an
                        Sheets(TARGET).Range("N" & rowid) = Heso_DA_CTDT_Summer(PRGTYPE)
                        Sheets(TARGET).Range("P" & rowid).FormulaR1C1 = "=RC[-10]*RC[-5]*RC[-4]*RC[-2]"
                    End If
                End If
                Sheets(TARGET).Range("R" & rowid).FormulaR1C1 = "=RC[-2] * " & Str(HesoGD_Summer)
                
            Else ' Khong co sinh vien
                Sheets(TARGET).Range("P" & rowid).Value = 0
            End If
            
            With hpinf
                'Sheets(TARGET).Range("D" & rowid) = .MAHP  'Su dung so lieu QLDT
                If class_type = "TN" Then
                    Sheets(TARGET).Range("F" & rowid) = .TN
                    Sheets(TARGET).Range("G" & rowid) = 0#
                Else
                    Sheets(TARGET).Range("F" & rowid) = .LT
                    Sheets(TARGET).Range("G" & rowid) = .BT
                End If
                Sheets(TARGET).Range("E" & rowid) = .TenHP
                If StrComp(.TenHP, HPNAME) <> 0 Then
                    'MsgBox HPNAME + "NEED TO BE VERIFIED FOR CONSISTENCY"
                End If
                
            End With
            rowid = rowid + 1
        Next
    End If
    ii = ii + 1
Loop

'GD ly thuyet va thi  nghiem, Dai hoc, ly 20182
'DATA_SHEET = "Phancong_ky3"



' ==================================================================
DOANMON_DOANTN:
DATA_SHEET = "DA_Hocky_3"
TARGET = "Tong_hop_GD"
ii = 2
'======= DA UNDERGRAD =============================================
BEGIN_DA:
Do While Sheets(DATA_SHEET).Range("B" & ii).Text <> "" 'Do theo ma lop
    tenGV_raw = Sheets(DATA_SHEET).Range("A" & ii).Text
    class_type = Sheets(DATA_SHEET).Range("H" & ii).Text
    MALOP = Val(Sheets(DATA_SHEET).Range("B" & ii).Text)
    HPCODE = Sheets(DATA_SHEET).Range("C" & ii).Text
    HPNAME = Sheets(DATA_SHEET).Range("D" & ii).Text
    PRGTYPE = Sheets(DATA_SHEET).Range("G" & ii).Text
    SVNAME = Sheets(DATA_SHEET).Range("F" & ii).Text
    mssv = Sheets(DATA_SHEET).Range("E" & ii).Value
    hpinf = GET_HP_INFO(HPCODE)
    
    'Dien thong tin mon DA tuong ung
    If IS_DA(class_type) Then
        hpinf = GET_HP_INFO(HPCODE)
        noGV = 0
        substrings = Split(tenGV_raw, "-")
        For Each s In substrings
            noGV = noGV + 1
        Next
        ' tinh toan so luong giao vien va he so
        SUM_heso = 0
        For idx = 1 To noGV
            gvrec(idx) = get_GVNAME(substrings(idx - 1))
            SUM_heso = SUM_heso + gvrec(idx).heso
        Next
        If noGV = 1 Then
            SUM_heso = 1
        End If
        If Trim(tenGV_raw) = "" Then
            noGV = 1
            gvrec(1).gvname = "CHUA PHAN CONG"
            gvrec(1).heso = 1
            SUM_heso = 1
        End If
        For idx = 1 To noGV
            gvrec(idx).heso = gvrec(idx).heso / SUM_heso
            Sheets(TARGET).Range("A" & rowid) = Trim(gvrec(idx).gvname)
            Sheets(TARGET).Range("B" & rowid) = HKNAME
            Sheets(TARGET).Range("C" & rowid) = MALOP
            Sheets(TARGET).Range("D" & rowid) = HPCODE
            PRGTYPE = Find_student_prog(mssv)
            Sheets(TARGET).Range("I" & rowid) = PRGTYPE
            Sheets(TARGET).Range("J" & rowid) = bo_dau_tieng_viet2(class_type)
            Sheets(TARGET).Range("L" & rowid) = gvrec(idx).heso
            Sheets(TARGET).Range("K" & rowid) = 1
            Sheets(TARGET).Range("M" & rowid) = 0
            Sheets(TARGET).Range("N" & rowid) = Heso_LT_CTDT_Summer(PRGTYPE)
            Sheets(TARGET).Range("O" & rowid) = Heso_TN_CTDT_Summer(PRGTYPE)
            Sheets(TARGET).Range("H" & rowid) = SVNAME & "/" & Trim(Str(mssv))
            class_type = bo_dau_tieng_viet2(class_type)
            If class_type = "DA" Or class_type = "DATN" Then
                With hpinf
                    Select Case class_type
                        Case "DATN"
                            Sheets(TARGET).Range("P" & rowid).Value = .HESODOAN * gvrec(idx).heso
                            Sheets(TARGET).Range("R" & rowid).FormulaR1C1 = "=RC[-2] * " & Str(HesoGD_DATN_Summer)
                        Case "DA"
                            Sheets(TARGET).Range("P" & rowid).Value = Heso_DA_CTDT_Summer(PRGTYPE) * .TC * gvrec(idx).heso
                            Sheets(TARGET).Range("R" & rowid).FormulaR1C1 = "=RC[-2] * " & Str(HesoGD_DA_Summer)
                    End Select
                    
                                        
                    Sheets(TARGET).Range("E" & rowid) = .TenHP
                    Sheets(TARGET).Range("F" & rowid).Value = .TC
                    Sheets(TARGET).Range("G" & rowid).Value = 0
                End With
                rowid = rowid + 1
            End If
        Next
        'Tinh GD
        
        
    End If
    ii = ii + 1
Loop

' Correct names
For ii = 2 To rowid
    TEN_KHONG_DAU = bo_dau_tieng_viet2(Sheets("Tong_hop_GD").Range("A" & ii))
    'First, try by original data
    Sheets(TARGET).Range("Q" & ii).FormulaR1C1 = "=VLOOKUP(RC[-16],CSDLCB,3,FALSE)"
    'If #N/A, try using no-accent data
    If Sheets(TARGET).Range("Q" & ii).Text = "#N/A" Then
        kk = 2
        foundCB = False
        Do While Not (foundCB) And kk < 300
            If Sheets("CSDL_CB").Range("B" & kk).Value = TEN_KHONG_DAU Then
                foundCB = True
            Else
                kk = kk + 1
            End If
        Loop
        If foundCB Then
            Sheets(TARGET).Range("A" & ii).Value = Sheets("CSDL_CB").Range("A" & kk).Value
        End If
    End If
Next


With Sheets(TARGET).Range("A2:Q" & rowid)
        .Borders(xlEdgeLeft).LineStyle = xlContinuous
        .Borders(xlEdgeTop).LineStyle = xlContinuous
        .Borders(xlEdgeBottom).LineStyle = xlContinuous
        .Borders(xlEdgeRight).LineStyle = xlContinuous
        .Borders(xlInsideVertical).LineStyle = xlContinuous
        .Borders(xlInsideHorizontal).LineStyle = xlContinuous
    End With
Sheets("Internal").Range("B1").Value = rowid
Application.Calculation = xlAutomatic

Sheets("Sheet1").Range("C31").Value = "Finish at " + Str(Time())
End Sub

Sub Tong_hop_thong_tin_HD_Hocky_3()
Dim ii As Long, mssv As Long, tenGV As String, tenSV As String, kk As Long, SISO As Long
Dim celval As Long, MALOP As Long, MaHP As String, TenHP As String, ttval As Long
Dim CL20182 As Range, cell As Range
Dim rowid As Long
Dim LAST_DAT_ROW As Integer
Dim TARGET As String, CLASS_LIST As String, SV_STAY_TILL_SEMESTER_END As Boolean
Dim CLSHEET As String
Dim idx As Long, start_row As Long

Sheets("Sheet1").Range("C30").Value = "Start at " + Str(Time())

TARGET = "DA_Hocky_3"
CLASS_LIST = "DS_ky3"
LAST_DAT_ROW = 2000
CLSHEET = "Class_HK3"
Sheets(TARGET).Range("A2:H5000").ClearContents
Sheets(TARGET).Range("A2:H5000").ClearFormats

'Set CL20182 = Sheets("Class_HK1").Range("A2:Q681")
ii = 2
Sheets("Hocky_3").Select

For kk = 1 To LAST_DAT_ROW
    celval = Val(Range("F" & kk).Text) 'Ma sinh vien
    ttval = Val(Range("A" & kk).Text) ' Ma lop
    tenSV = Range("G" & kk).Text
    tenGV = Range("I" & kk).Text
    If (ttval > 100000 And ttval < 700000) Then ' Ten ma lop
        'MaHP = Application.WorksheeTetFunction.VLookup(celval, CL20182, 2)
        MALOP = ttval
        rowid = ROW_LOOKUP(CLSHEET, MALOP)
    End If
    If IsNumeric(ttval) And celval > 10000000 And Len(Str(celval) = 8) And (rowid <> 0) Then
        Sheets(TARGET).Range("B" & ii).Value = MALOP
        Sheets(TARGET).Range("A" & ii).Value = tenGV
        Sheets(TARGET).Range("F" & ii).Value = tenSV
        Sheets(TARGET).Range("E" & ii).Value = celval
        Sheets(TARGET).Range("C" & ii).Value = Sheets(CLSHEET).Range("C" & rowid).Value 'ma HP
        Sheets(TARGET).Range("D" & ii).Value = Sheets(CLSHEET).Range("D" & rowid).Value '  Ten mon
        Sheets(TARGET).Range("G" & ii).Value = Sheets(CLSHEET).Range("N" & rowid).Value
        Sheets(TARGET).Range("H" & ii).Value = Sheets(CLSHEET).Range("F" & rowid).Value
        SISO = Val(Sheets(CLSHEET).Range("H" & rowid).Text)
        'Check if student actually stays until end of semester, cross check with class list
        SV_STAY_TILL_SEMESTER_END = True
        
        'Tra ma lop
        
        With Sheets(CLASS_LIST).Range("B:B")
        Set cell = .Find(What:=(MALOP), LookAt:=xlWhole, MatchCase:=False)
        End With
        If cell Is Nothing Then
            
            SV_STAY_TILL_SEMESTER_END = False
        Else
            idx = cell.Row
            Do While Sheets(CLASS_LIST).Range("G" & idx).Value <> celval And Sheets(CLASS_LIST).Range("B" & idx).Value = MALOP 'Khong kiem tra theo si so vi khong tin cay
                idx = idx + 1
            Loop
            If Sheets(CLASS_LIST).Range("B" & idx).Value <> MALOP Then ' idx >= start_row + SISO Then
                SV_STAY_TILL_SEMESTER_END = False
            End If
        End If
        If Not (SV_STAY_TILL_SEMESTER_END) Then
            Sheets(TARGET).Range("H" & ii).Value = Sheets(TARGET).Range("H" & ii).Value + "_DROP"
        End If
        ii = ii + 1
    End If
Next
Sheets("Sheet1").Range("C31").Value = "Finished at " + Str(Time())
End Sub
