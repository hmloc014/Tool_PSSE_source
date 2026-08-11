Option Compare Database

Dim Check(3)
Dim CheckLabel(3)
Dim CheckValue(3)

Dim VoltageLevel(3)
Dim VoltageLevelArr(3)

Dim GiaiDoan(6)
Dim GiaiDoanArr(6)

Dim CapDiaLy(4)
Dim CapDiaLyArr(4)

Dim SQL As String

Dim countNum As Integer


Private Sub Form_Open(Cancel As Integer)

    Check(0) = "Cap_Dien_Ap"
    Check(1) = "Cap_Dia_Ly"
    Check(2) = "Giai_Doan_VH"
    CheckLabel(0) = Me.Label32.Caption
    CheckLabel(1) = Me.Label21.Caption
    CheckLabel(2) = Me.Label42.Caption

    CheckValue(0) = Me.Check311.Value
    CheckValue(1) = Me.Check200.Value
    CheckValue(2) = Me.Check411.Value

    VoltageLevel(0) = "500"
    VoltageLevel(1) = "220"
    VoltageLevel(2) = "110"

    VoltageLevelArr(0) = Me.Option255.Value
    VoltageLevelArr(1) = Me.Option277.Value
    VoltageLevelArr(2) = Me.Option299.Value

    GiaiDoan(0) = Me.Label366.Caption
    GiaiDoan(1) = Me.Label388.Caption
    GiaiDoan(2) = Me.Label400.Caption
    GiaiDoan(3) = Me.Label444.Caption
    GiaiDoan(4) = Me.Label466.Caption
    GiaiDoan(5) = Me.Label488.Caption

    GiaiDoanArr(0) = Me.Option355.Value
    GiaiDoanArr(1) = Me.Option377.Value
    GiaiDoanArr(2) = Me.Option399.Value
    GiaiDoanArr(3) = Me.Option433.Value
    GiaiDoanArr(4) = Me.Option455.Value
    GiaiDoanArr(5) = Me.Option477.Value

    CapDiaLy(0) = "Ten_Tinh"
    CapDiaLy(1) = "Tieu_Vung"
    CapDiaLy(2) = "Vung"
    CapDiaLy(3) = "Mien"

    CapDiaLyArr(0) = Me.Option133.Value
    CapDiaLyArr(1) = Me.Option166.Value
    CapDiaLyArr(2) = Me.Option188.Value
    CapDiaLyArr(3) = Me.Option233.Value

End Sub


Function IsInArray(val As Integer, arr As Variant)
    Dim i, j As Integer
    IsInArray = False
    For i = 0 To (UBound(arr) - 1):
        If arr(i) = val Or arr(i) = "''" Then
            IsInArray = True
        End If
    Next i
End Function


Private Sub Check311_Click()
    CheckValue(0) = Me.Check311.Value
    Me.Child169.SourceObject = "Quy_Mo_DZ_Theo_Cap_Dien_Ap"
    If Me.Check311.Value = -1 Then
        Me.Option255.Enabled = True '500
        Me.Option277.Enabled = True '220
        Me.Option299.Enabled = True '110
        Me.Option499.Enabled = True 'all
    End If
    If Me.Check311.Value = 0 Then
        Me.Option255.Enabled = False '500
        Me.Option277.Enabled = False '220
        Me.Option299.Enabled = False '110
        Me.Option499.Enabled = False 'all
    End If
  
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Voltage Level"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by branch voltage"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option255_Click()

    VoltageLevelArr(0) = Option25.Value
    Dim z As Variant
    If Option25.Value = -1 Then
        z = IsInArray(0, VoltageLevelArr)
        If z = False Then
          Me.Option499.Value = -1
        End If
    Else
        Me.Option499.Value = 0
    End If
    
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Voltage Level"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by branch voltage"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option277_Click()
    Dim z As Variant
    VoltageLevelArr(1) = Option277.Value
    If Option277.Value = -1 Then
        z = IsInArray(0, VoltageLevelArr)
        If z = False Then
          Me.Option499.Value = -1
        End If
    Else
        Me.Option499.Value = 0
    End If
    
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Voltage Level"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by branch voltage"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option299_Click()
    Dim z As Variant
    VoltageLevelArr(2) = Option299.Value
    If Option299.Value = -1 Then
        z = IsInArray(0, VoltageLevelArr)
        If z = False Then
          Me.Option499.Value = -1
        End If
    Else
        Me.Option499.Value = 0
    End If
    
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Voltage Level"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by branch voltage"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option499_Click()
    If Me.Option499.Value = -1 Then
        Me.Option255.Value = -1
        Me.Option277.Value = -1
        Me.Option299.Value = -1
        VoltageLevelArr(0) = -1
        VoltageLevelArr(1) = -1
        VoltageLevelArr(2) = -1

    ElseIf Me.Option499.Value = 0 Then
        Me.Option255.Value = 0 '500
        Me.Option277.Value = 0 '220
        Me.Option299.Value = 0 '110
        VoltageLevelArr(0) = 0
        VoltageLevelArr(1) = 0
        VoltageLevelArr(2) = 0
    End If
 
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Voltage Level"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Voltage"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub


Private Sub Check411_Click()
    CheckValue(2) = Me.Check411.Value

    GiaiDoanArr(0) = Me.Option355.Value
    GiaiDoanArr(1) = Me.Option377.Value
    GiaiDoanArr(2) = Me.Option399.Value
    GiaiDoanArr(3) = Me.Option433.Value
    GiaiDoanArr(4) = Me.Option455.Value
    GiaiDoanArr(5) = Me.Option477.Value

    If Me.Check411.Value = -1 Then
        Me.Child1699.SourceObject = "Quy_Mo_DZ_Theo_GD"
        Me.Option355.Enabled = True 'hien huu
        Me.Option377.Enabled = True '21-25
        Me.Option399.Enabled = True '26-30
        Me.Option433.Enabled = True '31-35
        Me.Option455.Enabled = True '36-40
        Me.Option477.Enabled = True '41-45
        Me.Option533.Enabled = True 'all
    End If
    If Me.Check411.Value = 0 Then
        Me.Option355.Enabled = False 'hien huu
        Me.Option377.Enabled = False '21-25
        Me.Option399.Enabled = False '26-30
        Me.Option433.Enabled = False '31-35
        Me.Option455.Enabled = False '36-40
        Me.Option477.Enabled = False '41-45
        Me.Option533.Enabled = False 'all
    End If

    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Operation period"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Operation period"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option355_Click()
    GiaiDoanArr(0) = Me.Option355.Value
    Dim z As Variant
    If Option355.Value = -1 Then
        z = IsInArray(0, GiaiDoanArr)
        If z = False Then
          Me.Option533.Value = -1
        End If
    Else
        Me.Option533.Value = 0
    End If
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Operation period"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Operation period"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option377_Click()
    GiaiDoanArr(1) = Me.Option377.Value
    Dim z As Variant
    If Option377.Value = -1 Then
        z = IsInArray(0, GiaiDoanArr)
        If z = False Then
          Me.Option533.Value = -1
        End If
    Else
        Me.Option533.Value = 0
    End If

    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Operation period"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Operation period"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option399_Click()
    GiaiDoanArr(2) = Me.Option399.Value
    Dim z As Variant
    If Option399.Value = -1 Then
        z = IsInArray(0, GiaiDoanArr)
        If z = False Then
          Me.Option533.Value = -1
        End If
    Else
        Me.Option533.Value = 0
    End If
    
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Operation period"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Operation period"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option433_Click()
    GiaiDoanArr(3) = Me.Option433.Value
    Dim z As Variant
    If Option433.Value = -1 Then
        z = IsInArray(0, GiaiDoanArr)
        If z = False Then
          Me.Option533.Value = -1
        End If
    Else
        Me.Option533.Value = 0
    End If
    
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Operation period"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Operation period"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If

End Sub

Private Sub Option455_Click()
    GiaiDoanArr(4) = Me.Option455.Value
    Dim z As Variant
    If Option455.Value = -1 Then
        z = IsInArray(0, GiaiDoanArr)
        If z = False Then
          Me.Option533.Value = -1
        End If
    Else
        Me.Option533.Value = 0
    End If
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Operation period"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Operation period"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option477_Click()
    GiaiDoanArr(5) = Me.Option477.Value
    Dim z As Variant
    If Option477.Value = -1 Then
        z = IsInArray(0, GiaiDoanArr)
        If z = False Then
          Me.Option533.Value = -1
        End If
    Else
        Me.Option533.Value = 0
    End If
    
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Operation period"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Operation period"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option533_Click()
    If Me.Option533.Value = -1 Then
        Me.Option355.Value = -1
        Me.Option377.Value = -1
        Me.Option399.Value = -1
        Me.Option433.Value = -1
        Me.Option455.Value = -1
        Me.Option477.Value = -1
        Me.Option533.Value = -1
        
        GiaiDoanArr(0) = -1
        GiaiDoanArr(1) = -1
        GiaiDoanArr(2) = -1
        GiaiDoanArr(3) = -1
        GiaiDoanArr(4) = -1
        GiaiDoanArr(5) = -1
    End If
    If Me.Option533.Value = 0 Then
        Me.Option355.Value = 0
        Me.Option377.Value = 0
        Me.Option399.Value = 0
        Me.Option433.Value = 0
        Me.Option455.Value = 0
        Me.Option477.Value = 0
        Me.Option533.Value = 0
        
        GiaiDoanArr(0) = 0
        GiaiDoanArr(1) = 0
        GiaiDoanArr(2) = 0
        GiaiDoanArr(3) = 0
        GiaiDoanArr(4) = 0
        GiaiDoanArr(5) = 0
    End If
    
    Run_Branch
    
    If SQL <> "" Then
        Me.Label0.Caption = "Voltage Level"
        Me.Label0.Caption = "Operation period"
    Me.Chart12.RowSource = SQL
    Me.Chart12.ChartTitle = "Scale by Operation period"
    Me.Chart12.HasLegend = False
    Me.RecordSource = SQL
    End If
End Sub


Private Sub Check200_Click()
    CheckValue(1) = Me.Check20.Value
    If Me.Check200.Value = -1 Then
        Me.Child1699.SourceObject = "Quy_Mo_DZ_Theo_Tinh"
        Me.Option133.Enabled = True 'tinh
        Me.Option166.Enabled = True 'tieu vung
        Me.Option188.Enabled = True 'vung
        Me.Option233.Enabled = True 'mien
    End If
    If Me.Check200.Value = 0 Then
        Me.Option133.Enabled = False 'tinh
        Me.Option166.Enabled = False 'tieu vung
        Me.Option188.Enabled = False 'vung
        Me.Option233.Enabled = False 'mien
    End If

    CapDiaLyArr(0) = Me.Option133.Value
    CapDiaLyArr(1) = Me.Option166.Value
    CapDiaLyArr(2) = Me.Option188.Value
    CapDiaLyArr(3) = Me.Option233.Value

    Run_Branch
    If SQL <> "" Then
        Me.Label0.Caption = "Province"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Province"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub


Private Sub Option133_Click()
    CapDiaLyArr(0) = Me.Option133.Value
    If Me.Option133.Value = -1 Then
        Me.Option166.Value = 0
        Me.Option188.Value = 0
        Me.Option233.Value = 0
        CapDiaLyArr(1) = Me.Option166.Value
        CapDiaLyArr(2) = Me.Option188.Value
        CapDiaLyArr(3) = Me.Option233.Value
    End If

    Run_Branch
    If SQL <> "" Then
        Me.Label0.Caption = "Province"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Province"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option166_Click()
    CapDiaLyArr(1) = Me.Option166.Value
    If Me.Option166.Value = -1 Then
        Me.Option133.Value = 0
        Me.Option188.Value = 0
        Me.Option233.Value = 0
        CapDiaLyArr(0) = Me.Option133.Value
        CapDiaLyArr(2) = Me.Option188.Value
        CapDiaLyArr(3) = Me.Option233.Value
    End If
    
    Run_Branch
    If SQL <> "" Then
        Me.Label0.Caption = "Province"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Province"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option188_Click()
    CapDiaLyArr(2) = Me.Option188.Value
    If Me.Option188.Value = -1 Then
        Me.Option133.Value = 0
        Me.Option166.Value = 0
        Me.Option233.Value = 0
        CapDiaLyArr(0) = Me.Option133.Value
        CapDiaLyArr(1) = Me.Option166.Value
        CapDiaLyArr(3) = Me.Option233.Value
    End If
    
    Run_Branch
    If SQL <> "" Then
        Me.Label0.Caption = "Province"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Province"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub

Private Sub Option233_Click()
    CapDiaLyArr(3) = Me.Option233.Value
    If Me.Option233.Value = -1 Then
        Me.Option133.Value = 0
        Me.Option166.Value = 0
        Me.Option188.Value = 0
        CapDiaLyArr(0) = Me.Option133.Value
        CapDiaLyArr(1) = Me.Option166.Value
        CapDiaLyArr(2) = Me.Option188.Value
    End If
    
    Run_Branch
    If SQL <> "" Then
        Me.Label0.Caption = "Province"
        Me.Chart12.RowSource = SQL
        Me.Chart12.ChartTitle = "Scale by Province"
        Me.Chart12.HasLegend = False
        Me.RecordSource = SQL
    End If
End Sub


Function Run_Branch()

    Dim i As Integer
    Dim j As Integer
    Dim Line1 As String
    Dim Line2 As String
    Dim Line3 As String
    Dim Line4 As String
    Dim countNum As Integer

    Set CheckArray = CreateObject("System.Collections.ArrayList")
    Set Op1Array = CreateObject("System.Collections.ArrayList")
    Set Op2Array = CreateObject("System.Collections.ArrayList")
    Set Op3Array = CreateObject("System.Collections.ArrayList")
    % Set Op5Array = CreateObject("System.Collections.ArrayList")
    Set CountArr = CreateObject("System.Collections.ArrayList")
  
        
    If CheckValue(0) = -1 Then
        countNum = 0
        
        For i = 0 To 2
            If VoltageLevelArr(i) = -1 Then
                Op1Array.Add VoltageLevel(i)
                countNum = countNum + 1
            End If
        Next i
        
        If countNum > 0 Then
            CheckArray.Add Check(0)
            CountArr.Add countNum
        End If
    End If
    

    If CheckValue(2) = -1 Then
        countNum = 0
        
        For i = 0 To 5
            If GiaiDoanArr(i) = -1 Then
                Op3Array.Add GiaiDoan(i)
                countNum = countNum + 1
            End If
        Next i
        
        If countNum > 0 Then
            CheckArray.Add Check(2)
            CountArr.Add countNum
        End If
    End If

    If CheckValue(1) = -1 Then
        countNum = 0
        
        For i = 0 To 3
            If CapDiaLyArr(i) = -1 Then
                Op2Array.Add CapDiaLy(i)
                countNum = countNum + 1
            End If
        Next i
        
        If countNum > 0 Then
            CheckArray.Add Check(1)
            CountArr.Add countNum
        End If
    End If

    
    Line1 = "SELECT "
    Line2 = "FROM Cap_Dia_Ly INNER JOIN Branch ON Cap_Dia_Ly.Ma_Tinh = Branch.Ma_Tinh "
    Line3 = "GROUP BY "
    Line4 = "HAVING ("

    If CheckArray.Count > 1 Then 'co 2 o check tro len'
        For i = 0 To (CheckArray.Count - 1)
            If i = 0 Then
                If CheckArray(i) = Check(0) Then
                    Line1 = Line1 + "Branch." & CheckArray(i) & " As Field1, Sum([So_Mach]*[chieu_dai]) AS Field2, "
                    Line3 = Line3 + "Branch." & CheckArray(i) & ", "
                    If CountArr(i) = 1 Then
                        Line4 = Line4 + "((Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "') "
                    Else
                        For j = 0 To CLng(CountArr(i)) - 1
                            If j = 0 Then
                                Line4 = Line4 + "((Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "' "
                            ElseIf j = CLng(CountArr(i)) - 1 Then
                                Line4 = Line4 + "Or (Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "') "
                            Else
                                Line4 = Line4 + "Or (Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "' "
                            End If
                        Next j
                    End If
                ElseIf CheckArray(i) = Check(1) Then
                    If IsInArray(-1, CapDiaLyArr) = True Then
                        Line1 = Line1 + "Cap_Dia_Ly." & Op2Array(0) & " AS Field1, Sum([So_Mach]*[chieu_dai]) AS Field2, "
                        Line3 = Line3 + "Cap_Dia_Ly." & Op2Array(0) & ", "
                    Else
                        Line1 = Line1 + "Cap_Dia_Ly.Ten_Tinh AS Field1, Sum([So_Mach]*[chieu_dai]) AS Field2, "
                        Line3 = Line3 + "Cap_Dia_Ly.Ten_Tinh, "
                        Me.Option13.Value = -1
                    End If

                ElseIf CheckArray(i) = Check(2) Then
                    Line1 = Line1 + "Branch." & CheckArray(i) & " As Field1, Sum([So_Mach]*[chieu_dai]) AS Field2, "
                    Line3 = Line3 + "Branch." & CheckArray(i) & ", "
                    If CountArr(i) = 1 Then
                        Line4 = Line4 + "((Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "') "
                    Else
                        For j = 0 To CLng(CountArr(i)) - 1
                            If j = 0 Then
                                Line4 = Line4 + "((Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "' "
                            ElseIf j = CLng(CountArr(i)) - 1 Then
                                Line4 = Line4 + "Or (Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "') "
                            Else
                                Line4 = Line4 + "Or (Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "' "
                            End If
                        Next j
                    End If
                End If
                    
            ElseIf (i > 0 And i < (CheckArray.Count - 1)) Then

                If CheckArray(i) = Check(0) Then
                    Line1 = Line1 + "Branch." & CheckArray(i) & " AS Field" & i + 2 & ", "
                    Line3 = Line3 + "Branch." & CheckArray(i) & ", "
                    If CLng(CountArr(i)) = 1 Then
                        Line4 = Line4 + "AND ((Branch." & CheckArray(i) & ") = '" & Op1Array(0) & "') "
                    Else
                        For j = 0 To CLng(CountArr(i)) - 1
                            If j = 0 Then
                                Line4 = Line4 + "AND ((Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "' "
                            ElseIf j = CLng(CountArr(i)) - 1 Then
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "') "
                            Else
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "' "
                            End If
                        Next j
                    End If
                ElseIf CheckArray(i) = Check(1) Then
                    If IsInArray(-1, CapDiaLyArr) = True Then
                        Line1 = Line1 + "Cap_Dia_Ly." & Op2Array(0) & " AS Field" & i + 2 & ", "
                        Line3 = Line3 + "Cap_Dia_Ly." & Op2Array(0) & ", "
                    Else ' M?c dinh
                        Line1 = Line1 + "Cap_Dia_Ly.Ten_Tinh AS Field" & i + 2 & ", "
                        Line3 = Line3 + "Cap_Dia_Ly.Ten_Tinh, "
                        Me.Option13.Value = -1
                    End If
                ElseIf CheckArray(i) = Check(2) Then
                    Line1 = Line1 + "Branch." & CheckArray(i) & " AS Field" & i + 2 & ", "
                    Line3 = Line3 + "Branch." & CheckArray(i) & ", "
                    If CLng(CountArr(i)) = 1 Then
                        Line4 = Line4 + "AND ((Branch." & CheckArray(i) & ") = '" & Op3Array(0) & "') "
                    Else
                        For j = 0 To CLng(CountArr(i)) - 1
                            If j = 0 Then
                                Line4 = Line4 + "AND ((Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "' "
                            ElseIf j = CLng(CountArr(i)) - 1 Then
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "') "
                            Else
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "' "
                            End If
                        Next j
                    End If
                End If
            ElseIf i = (CheckArray.Count - 1) Then
                If CheckArray(i) = Check(0) Then
                    Line1 = Line1 + "Branch." & CheckArray(i) & " AS Field" & i + 2 & " "
                    Line3 = Line3 + "Branch." & CheckArray(i) & " "
                    If CLng(CountArr(i)) = 1 Then
                        Line4 = Line4 + "AND ((Branch." & CheckArray(i) & ") = '" & Op1Array(0) & "')); "
                    Else
                        For j = 0 To CLng(CountArr(i)) - 1
                            If j = 0 Then
                                Line4 = Line4 + "AND (((Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "' "
                            ElseIf j = CLng(CountArr(i)) - 1 Then
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "')); "
                            Else
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op1Array(j) & "' "
                            End If
                        Next j
                    End If
                ElseIf CheckArray(i) = Check(1) Then
                    If IsInArray(-1, CapDiaLyArr) = True Then
                        Line1 = Line1 + "Cap_Dia_Ly." & Op2Array(0) & " AS Field" & i + 2 & " "
                        Line3 = Line3 + "Cap_Dia_Ly." & Op2Array(0) & " "
                        If i = 1 Then
                            Line4 = ";"
                        Else
                            Line4 = Line4 + ");"
                        End If
                        
                    Else ' M?c dinh
                        Line1 = Line1 + "Cap_Dia_Ly.Ten_Tinh AS Field" & i + 2 & " "
                        Line3 = Line3 + "Cap_Dia_Ly.Ten_Tinh "
                        If i = 1 Then
                            Line4 = ";"
                        Else
                            Line4 = Line4 + ");"
                        End If
                        Me.Option13.Value = -1
                    End If
                ElseIf CheckArray(i) = Check(2) Then
                    Line1 = Line1 + "Branch." & CheckArray(i) & " AS Field" & i + 2 & " "
                    Line3 = Line3 + "Branch." & CheckArray(i) & " "
                    If CLng(CountArr(i)) = 1 Then
                        Line4 = Line4 + "AND ((Branch." & CheckArray(i) & ") = '" & Op3Array(0) & "')); "
                    Else
                        For j = 0 To CLng(CountArr(i)) - 1
                            If j = 0 Then
                                Line4 = Line4 + "AND ((Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "' "
                            ElseIf j = CLng(CountArr(i)) - 1 Then
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "')); "
                            Else
                                Line4 = Line4 + "OR (Branch." & CheckArray(i) & ") = '" & Op3Array(j) & "' "
                            End If
                        Next j
                    End If
                End If
            End If
        Next i
    ElseIf CheckArray.Count > 0 Then
        If CheckArray(0) = Check(0) Then
            Line1 = Line1 + "Branch." & CheckArray(0) & " As Field1, Sum([So_Mach]*[chieu_dai]) AS Field2 "
            Line3 = Line3 + "Branch." & CheckArray(0) & " "
            If CLng(CountArr(0)) = 1 Then
                Line4 = Line4 + "((Branch." & CheckArray(0) & ") = '" & Op1Array(j) & "')); "
            Else
                For j = 0 To CLng(CountArr(0)) - 1
                    If j = 0 Then
                        Line4 = Line4 + "((Branch." & CheckArray(0) & ") = '" & Op1Array(j) & "' "
                    ElseIf j = CLng(CountArr(0)) - 1 Then
                        Line4 = Line4 + "OR (Branch." & CheckArray(0) & ") = '" & Op1Array(j) & "')); "
                    Else
                        Line4 = Line4 + "OR (Branch." & CheckArray(0) & ") = '" & Op1Array(j) & "' "
                    End If
                Next j
            End If

        ElseIf CheckArray(0) = Check(1) Then
            If CLng(CountArr(0)) = 1 Then
                Line1 = Line1 + "Cap_Dia_Ly." & Op2Array(0) & " AS Field1, Sum([So_Mach]*[chieu_dai]) AS Field2 "
                Line3 = Line3 + "Cap_Dia_Ly." & Op2Array(0) & " "
                Line4 = ";"
            Else ' M?c dinh
                Line1 = Line1 + "Cap_Dia_Ly.Ten_Tinh AS Field1, Sum([So_Mach]*[chieu_dai]) AS Field2 "
                Line3 = Line3 + "Cap_Dia_Ly.Ten_Tinh "
                Line4 = ";"
                Me.Option13.Value = -1
            End If
        ElseIf CheckArray(0) = Check(2) Then
            Line1 = Line1 + "Branch." & CheckArray(0) & " As Field1, Sum([So_Mach]*[chieu_dai]) AS Field2 "
            Line3 = Line3 + "Branch." & CheckArray(0) & " "
            If CLng(CountArr(0)) = 1 Then
                Line4 = Line4 + "((Branch." & CheckArray(0) & ") = '" & Op3Array(j) & "')) ;"
            Else
                For j = 0 To CLng(CountArr(0)) - 1
                    If j = 0 Then
                        Line4 = Line4 + "((Branch." & CheckArray(0) & ") = '" & Op3Array(j) & "' "
                    ElseIf j = CLng(CountArr(0)) - 1 Then
                        Line4 = Line4 + "OR (Branch." & CheckArray(0) & ") = '" & Op3Array(j) & "')); "
                    Else
                        Line4 = Line4 + "OR (Branch." & CheckArray(0) & ") = '" & Op3Array(j) & "' "
                    End If
                Next j
            End If

        End If
    Else ' Khong co lua chon nao
    SQL = ""
    End If

    Dim flag As Integer
    flag = 0
    If CheckArray.Count > 0 Then
        If CountArr.Count > 0 Then
            flag = 1
        End If
    End If
    
    If flag = 1 Then
        SQL = Line1 + Line2 + Line3 + Line4
    End If

    If CheckArray.Count = 2 And flag = 1 Then
        Me.Text2111.Visible = True
        Me.Label2099.Visible = True
        Me.Label09.Caption = CheckArray(0)
        Me.Label2099.Caption = CheckArray(1)
        Me.Text2233.Visible = False
        Me.Label2222.Visible = False
        Me.Text2333.Visible = False
        Me.Label2322.Visible = False
        Me.Text2433.Visible = False
        Me.Label2422.Visible = False
    ElseIf CheckArray.Count = 3 And flag = 1 Then
        Me.Text2111.Visible = True
        Me.Label2099.Visible = True
        Me.Text2233.Visible = True
        Me.Label2222.Visible = True
        Me.Text2333.Visible = False
        Me.Label2322.Visible = False
        Me.Text2433.Visible = False
        Me.Label2422.Visible = False
        Me.Label0.Caption = CheckArray(0)
        Me.Label2099.Caption = CheckArray(1)
        Me.Label2222.Caption = CheckArray(2)
    ElseIf CheckArray.Count = 4 And flag = 1 Then
        Me.Text2111.Visible = True
        Me.Label2099.Visible = True
        Me.Text2233.Visible = True
        Me.Label2222.Visible = True
        Me.Text2333.Visible = True
        Me.Label2322.Visible = True
        Me.Text2433.Visible = False
        Me.Label2422.Visible = False
        Me.Label0.Caption = CheckArray(0)
        Me.Label2099.Caption = CheckArray(1)
        Me.Label2222.Caption = CheckArray(2)
    ElseIf CheckArray.Count = 5 And flag = 1 Then
        Me.Text2111.Visible = True
        Me.Label2099.Visible = True
        Me.Text2233.Visible = True
        Me.Label2222.Visible = True
        Me.Text2333.Visible = True
        Me.Label2322.Visible = True
        Me.Text2433.Visible = True
        Me.Label2422.Visible = True
        Me.Label0.Caption = CheckArray(0)
        Me.Label2099.Caption = CheckArray(1)
        Me.Label2222.Caption = CheckArray(2)

    Else
        Me.Text2111.Visible = False
        Me.Label2099.Visible = False
        Me.Text2233.Visible = False
        Me.Label2222.Visible = False
        Me.Text2333.Visible = False
        Me.Label2322.Visible = False
        Me.Text2433.Visible = False
        Me.Label2422.Visible = False
    End If
End Function



