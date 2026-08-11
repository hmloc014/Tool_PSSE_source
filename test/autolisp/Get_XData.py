Option Explicit
Public Sub Show_Info()
'On Error GoTo ext
    Dim obj As ZcadObject
    Dim sset  As ZcadSelectionSet
    Set sset = ThisDrawing.SelectionSets.Add("S8")
    sset.SelectOnScreen
    If sset.Count > 0 Then
        Set obj = sset.Item(0)
        Dim xDataType As Variant
        Dim xData As Variant
        obj.GetXData appInfo, xDataType, xData
        If VarType(xDataType) <> vbEmpty Then
            MsgBox xData(1)
        End If
    End If
    
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If

End Sub
Public Function StrMacBus(obj As ZcadText, viewtype As String) As String
Debug.Print "________________strMacbus in GetXData"
Dim INum As Long, JNum As Long
Dim i As Integer, n As Integer, idx As Integer
Dim ikv As Double, jkv As Double
Dim MacBus(40) As Long
Dim CKT(40) As String
Dim MacName(40) As String
Dim str As String
Dim sumP As Double, sumQ As Double

Dim xDataType As Variant
Dim xData As Variant

    '   kiem tra xem nut co ton tai hay khong
    idx = 0
    obj.GetXData appMacBus, xDataType, xData
    If VarType(xDataType) <> vbEmpty Then
        INum = CLng(xData(1))
        idx = BusIndex(INum)
    End If
    
    '   Neu nut co trong pss/e
    If idx > 0 Then
        '   Tim nut co chua may phat
        ikv = BusAr(idx).KV / BusAr(idx).PU
        n = 0
        sumP = 0
        sumQ = 0
        For i = 1 To nBranch
            If INum = BrnAr(i).frombus Then
                JNum = BrnAr(i).tobus
                idx = BusIndex(JNum)
                jkv = BusAr(idx).KV / BusAr(idx).PU
                If Abs(ikv - jkv) > 1 Then
                    n = n + 1
                    MacBus(n) = JNum
                    CKT(n) = BrnAr(i).CKT
                    MacName(n) = BusAr(idx).Name
                    sumP = sumP - BrnAr(i).P
                    sumQ = sumQ - BrnAr(i).Q
                End If
            End If
            
            If INum = BrnAr(i).tobus Then
                JNum = BrnAr(i).frombus
                idx = BusIndex(JNum)
                jkv = BusAr(idx).KV / BusAr(idx).PU
                If Abs(ikv - jkv) > 1 Then
                    n = n + 1
                    MacBus(n) = JNum
                    CKT(n) = BrnAr(i).CKT
                    MacName(n) = BusAr(idx).Name
                    sumP = sumP + BrnAr(i).P
                    sumQ = sumQ + BrnAr(i).Q
                End If
            End If
            
        Next
        
        '   Hien thi thong so
        If n > 0 Then
            
            Select Case VBA.UCase(viewtype)
            
                '   so hieu nut cao ap
                Case "BUSNUMBER"
                    StrMacBus = INum
                    
                '   so hieu nut may phat
                Case "MACNUMBER"
                    str = CStr(MacBus(1))
                    For i = 2 To n
                        str = str + "." + CStr(MacBus(i))
                    Next
                    StrMacBus = str
                    
                '   ten nut may phat
                Case "MACNAME"
                    str = MacName(1)
                    For i = 2 To n
                        str = str + "\" + MacName(i)
                    Next
                    StrMacBus = str
                    
                '   tong dong cong suat phat chay qua may bien ap
                Case "PQTRANS"
                    StrMacBus = ToComplex(sumP, sumQ)
                    
                '   tong cong suat phat
                Case "PQGEN"
                    sumP = 0
                    sumQ = 0
                    For i = 1 To n
                        idx = GenIndex(MacBus(i), "1")
                        If idx > 0 Then
                            sumP = sumP + GenAr(idx).PG
                            sumQ = sumQ + GenAr(idx).QG
                        End If
                    Next
                    StrMacBus = ToComplex(sumP, sumQ)
                    
                Case "RATE"
                    For i = 1 To n
                        idx = GenIndex(MacBus(i), "1")
                        If idx > 0 Then
                            str = str + "\" + CStr(Round(GenAr(idx).PG / GenAr(idx).Pmax * 100, 1))
                        Else
                            str = str + "\Err!"
                        End If
                    Next
                    str = VBA.Right(str, VBA.Len(str) - 1)
                    StrMacBus = str + "%"
                Case "PARAMS"
                    
                    For i = 1 To n
                        idx = GenIndex(MacBus(i), "1")
                        If idx > 0 Then
                            str = str + "\" + CStr(Round(GenAr(idx).Pmax, 1))
                        Else
                            str = str + "\Err!"
                        End If
                    Next
                    
                    str = VBA.Right(str, VBA.Len(str) - 1)
                    StrMacBus = str + "MW"
            End Select
        Else
            StrMacBus = "NotMac!"
        End If
    Else
        StrMacBus = "Error!"
    End If
    

    
End Function

Public Function StrBus(obj As ZcadText, viewtype As String) As String
Dim number As Long
Dim idx As Long
Dim xDataType As Variant
Dim xData As Variant
Debug.Print "________________strbus in GetXData"
    idx = 0
    obj.GetXData appBus, xDataType, xData
    If VarType(xDataType) <> vbEmpty Then
        number = CLng(xData(1))
        idx = BusIndex(number)
    End If
    
    If idx > 0 Then
        Select Case VBA.UCase(viewtype)
            Case "NUMBER"
                StrBus = CStr(number)
            Case "NAME"
                StrBus = Left(BusAr(idx).Name, NameLen)
            Case "KV"
                StrBus = VBA.Format(BusAr(idx).KV, "###0.0")
            Case "PU"
                StrBus = VBA.Format(BusAr(idx).PU, "###0.00")
        End Select
    Else
        StrBus = "BusErr"
    End If
    
End Function

Public Function StrLoad(obj As ZcadText, viewtype As String) As String
Dim number As Long
Dim idx As Long
Dim idxbus As Long
Dim xDataType As Variant
Dim xData As Variant

Debug.Print "________________strLoad in GetXData"
idx = 0
obj.GetXData appLod, xDataType, xData
If VarType(xDataType) <> vbEmpty Then
    number = CLng(xData(1))
    idx = LoadIndex(number, 1)
End If
    

idxbus = BusIndex(number)
If idx > 0 Then
    Select Case VBA.UCase(viewtype)
        Case "NUMBER"
            StrLoad = CStr(number)
        Case "NAME"
            StrLoad = Left(BusAr(idxbus).Name, NameLen)
        Case "PQ"
            StrLoad = ToComplex(LodAr(idx).PL, LodAr(idx).QL)
    End Select
Else
    StrLoad = "LoadErr"
End If
End Function


Public Function StrMac(obj As ZcadText, viewtype As String) As String
Dim n As Long
Dim i As Long
Dim idx As Long
Dim xDataType As Variant
Dim xData As Variant
Dim number() As Long
Dim str As String
Dim sumP As Double, sumQ As Double
Dim P As Double, Q As Double, s As Double, pf As Double

Debug.Print "________________strMac in GetXData"
obj.GetXData appMac, xDataType, xData
If VarType(xDataType) <> vbEmpty Then
    n = CLng(xData(1))
    ReDim number(n)
End If
str = ""

If n > 0 Then
    Select Case VBA.UCase(viewtype)
    
        Case "NUMBER"
            For i = 0 To n - 1
                number(i) = CLng(xData(i + 2))
                str = str + CStr(number(i)) + "."
            Next
            str = Left(str, Len(str) - 1)
            
        Case "NAME"
            For i = 0 To n - 1
                number(i) = CLng(xData(i + 2))
                idx = BusIndex(number(i))
                If idx > 0 Then
                    str = str + Left(BusAr(idx).Name, NameLen) + "/"
                Else
                    str = str + CStr(number(i)) + "."
                End If
            Next
            str = Left(str, Len(str) - 1)
        Case "PQ"
            sumP = 0
            sumQ = 0
            For i = 0 To n - 1
                number(i) = CLng(xData(i + 2))
                
                'idx = GenIndex(Number(i), "1")
                idx = Trans2Index(number(i))
                If Abs(idx) > 0 Then
                    If idx > 0 Then
                        sumP = sumP + BrnAr(idx).P
                        sumQ = sumQ + BrnAr(idx).Q
                    Else
                        sumP = sumP - BrnAr(Abs(idx)).P
                        sumQ = sumQ - BrnAr(Abs(idx)).Q
                    End If
                Else
                    str = "MacErr"
                    Exit For
                End If
            Next
            If str <> "MacErr" Then
                str = ToComplex(sumP, sumQ)
            End If
        
        Case "RATE"
            For i = 0 To n - 1
                number(i) = CLng(xData(i + 2))
                idx = GenIndex(number(i), "1")
                If idx > 0 Then
                    If (GenAr(idx).Pmax <> 0) Then
                        str = str + CStr(Abs(100 * Round(GenAr(idx).PG / GenAr(idx).Pmax, 1))) + "/"
                    Else
                        str = str + "NaN/"
                    End If
                Else
                    str = "MacErr"
                    Exit For
                End If
            Next
            If str <> "MacErr" Then
                str = Left(str, Len(str) - 1)
                str = str + "[%]"
            End If
            
        Case "PF"
            For i = 0 To n - 1
                number(i) = CLng(xData(i + 2))
                idx = GenIndex(number(i), "1")
                If idx > 0 Then
                    P = GenAr(idx).PG
                    Q = GenAr(idx).QG
                    s = (P ^ 2 + Q ^ 2)
                    
                    If (s <> 0) Then
                        pf = P / Sqr(s)
                        str = str + VBA.Format(pf, "###0.00") + "/"
                    Else
                        str = str + "NaN" + "/"
                    End If
                Else
                    str = "MacErr"
                    Exit For
                End If
            Next
            If str <> "MacErr" Then
                str = Left(str, Len(str) - 1)
                str = str + "[pf]"
            End If
            
        Case "PARAMS"
            For i = 0 To n - 1
                number(i) = CLng(xData(i + 2))
                idx = GenIndex(number(i), "1")
                If idx > 0 Then
                    str = str + CStr(GenAr(idx).Pmax) + "/"
                Else
                    str = str + CStr(number(i)) + "/"
                End If
            Next
            str = Left(str, Len(str) - 1) + "[MW]"
            
    End Select
Else
    str = "MacErr"
End If
    StrMac = str
End Function


Public Function StrBrn(obj As ZcadText, viewtype As String) As String
Dim frombus As Long, tobus As Long, CKT As String
Dim idx As Long, k As Long
Dim xDataType As Variant
Dim xData As Variant
Debug.Print "________________strBrn in GetXData"
    idx = 0
    obj.GetXData appBrn, xDataType, xData
    If VarType(xDataType) <> vbEmpty Then
        frombus = CLng(xData(1))
        tobus = CLng(xData(2))
        CKT = CStr(xData(3))
        idx = BranchIndex(frombus, tobus, CKT)
    End If
    
    k = Abs(idx)
    If k > 0 Then
        Select Case VBA.UCase(viewtype)
            Case "NUMBER"
                StrBrn = CStr(frombus) + "." + CStr(tobus) + "." + CKT
            Case "PQ"
                If idx > 0 Then
                    StrBrn = ToComplex(BrnAr(k).P, BrnAr(k).Q)
                Else
                    StrBrn = ToComplex(-BrnAr(k).P, -BrnAr(k).Q)
                End If
            Case "RATE"
                StrBrn = VBA.Format(BrnAr(k).PCTRTA, "###0.0") + "%"
            Case "PARAMS"
                StrBrn = BrnAr(k).TypeName + "-" + CStr(BrnAr(k).TypeData)
            
        End Select
    Else
        StrBrn = "BrnErr"
    End If
    
End Function

Public Function StrMBrn(obj As ZcadText, viewtype As String) As String
Dim frombus As Long, tobus As Long, ckt1 As String, ckt2 As String
Dim idx1 As Long, idx2 As Long, k1 As Long, k2 As Long
Dim xDataType As Variant
Dim xData As Variant
Dim sumP As Double, sumQ As Double
Dim s1 As String, s2 As String
Debug.Print "________________strMBrn in GetXData"
    idx1 = 0: idx2 = 0
    obj.GetXData appMBrn, xDataType, xData
    If VarType(xDataType) <> vbEmpty Then
        frombus = CLng(xData(1))
        tobus = CLng(xData(2))
        ckt1 = CStr(xData(3))
        ckt2 = CStr(xData(4))
        idx1 = BranchIndex(frombus, tobus, ckt1)
        idx2 = BranchIndex(frombus, tobus, ckt2)
    End If
    k1 = Abs(idx1)
    k2 = Abs(idx2)
    If (k1 > 0) And (k2 > 0) Then
        Select Case VBA.UCase(viewtype)
            Case "NUMBER"
                StrMBrn = CStr(frombus) + "." + CStr(tobus) + "." + ckt1 + "." + ckt2
            Case "PQ"
                    sumP = (idx1 / k1) * BrnAr(k1).P + (idx2 / k2) * BrnAr(k2).P
                    sumQ = (idx1 / k1) * BrnAr(k1).Q + (idx2 / k2) * BrnAr(k2).Q
                    StrMBrn = ToComplex(sumP, sumQ)
            Case "RATE"
                StrMBrn = VBA.Format(BrnAr(k1).PCTRTA, "###0.0") + "/" + _
                          VBA.Format(BrnAr(k2).PCTRTA, "###0.0") + "%"
            Case "PARAMS"
                s1 = BrnAr(k1).TypeName + "-" + CStr(BrnAr(k1).TypeData)
                s2 = BrnAr(k2).TypeName + "-" + CStr(BrnAr(k2).TypeData)
                If s1 = s2 Then
                    StrMBrn = "2x(" + s1 + ")"
                Else
                    StrMBrn = s1 + "/" + s2
                End If
        End Select
    Else
        StrMBrn = "BrnErr"
    End If
End Function

Public Function StrPbrn(obj As ZcadText, viewtype As String) As String
'On Error GoTo ext
Debug.Print "________________strPbrn in GetXData"
    Dim xDataType As Variant
    Dim xData As Variant
    

    Dim frombus As Long, tobus As Long
    obj.GetXData appPBrn, xDataType, xData
    If VarType(xDataType) <> vbEmpty Then
        frombus = CLng(xData(1))
        tobus = CLng(xData(2))
    End If
        
    Select Case VBA.UCase(viewtype)
        Case "NUMBER"
            StrPbrn = CStr(frombus) + "." + CStr(tobus)
        Case "PQ"
            StrPbrn = PBrnPQ(frombus, tobus)
        Case "RATE"
            StrPbrn = PBrnRate(frombus, tobus)
        Case "PARAMS"
            StrPbrn = PBrnParams(frombus, tobus)
    End Select
   
ext:
   
End Function
Private Function PBrnPQ(frombus As Long, tobus As Long) As String
Debug.Print "________________strPBrnPQ in GetXData"
    Dim i As Long, n As Long, k As Long
    Dim sumP As Double
    Dim sumQ As Double
    Dim idx As Variant
    idx = PBranchIndex(frombus, tobus)
    n = idx(0)
    sumP = 0: sumQ = 0
    If n > 0 Then
        For i = 1 To n
        
            If idx(i) > 0 Then
                sumP = sumP + BrnAr(idx(i)).P: sumQ = sumQ + BrnAr(idx(i)).Q
            Else
                k = Abs(idx(i))
                sumP = sumP - BrnAr(k).P: sumQ = sumQ - BrnAr(k).Q
            End If
        Next
        PBrnPQ = ToComplex(sumP, sumQ)
    Else
        PBrnPQ = "PBrnErr"
    End If
End Function
Private Function PBrnRate(frombus As Long, tobus As Long) As String
Debug.Print "________________PbrnRate in GetXData"
    Dim i As Long, n As Long, k As Long
    Dim str As String
    Dim idx As Variant
    idx = PBranchIndex(frombus, tobus)
    n = idx(0)
    str = ""
    If n > 0 Then
        For i = 1 To n
            k = Abs(idx(i))
            str = str + VBA.Format(BrnAr(k).PCTRTA, "###0.0") + "/"
        Next
        PBrnRate = Left(str, Len(str) - 1) + "[%]"
    Else
        PBrnRate = "PBrnErr"
    End If
End Function
Private Function PBrnParams(frombus As Long, tobus As Long) As String
Debug.Print "________________PbrnParams in GetXData"
    Dim i As Long, n As Long, k As Long
    Dim str As String
    Dim idx As Variant
    idx = PBranchIndex(frombus, tobus)
    n = idx(0)
    str = ""
    If n > 0 Then
        For i = 1 To n
            k = Abs(idx(i))
            If BrnAr(k).PCTRTA > 0 Then
                str = str + BrnAr(k).TypeName + "-" + CStr(BrnAr(k).TypeData) + "/"
            End If
        Next
        On Error GoTo err
        str = Left(str, Len(str) - 1)
        PBrnParams = reName(str)
    Else
err:
        PBrnParams = "PBrnErr"
    End If
End Function



Public Function StrTrans(obj As ZcadText, viewtype As String) As String
    Debug.Print "________________strTrans in GetXData"
    Dim number As Long
    Dim xDataType As Variant
    Dim xData As Variant
    Dim idx As Long
    
    obj.GetXData appTrans, xDataType, xData
    If VarType(xDataType) <> vbEmpty Then
        number = CLng(xData(1))
        idx = BusIndex(number)
    End If
    
    If idx > 0 Then
        Select Case VBA.UCase(viewtype)
            Case "NUMBER"
                StrTrans = CStr(number)
            Case "PQ"
                StrTrans = TransPQ(number)
            Case "RATE"
                StrTrans = TransRate(number)
            Case "PARAMS"
                StrTrans = TransParams(number)
        End Select
    Else
        StrTrans = "TransErr"
    End If
    
End Function
Private Function TransPQ(ByVal number As Long) As String
    Dim n As Long, i As Long
    Dim idi As Long, idj As Long, idk As Long
    Dim sumP As Double, sumQ As Double
    
    sumP = 0
    sumQ = 0
    n = 0
    For i = 1 To nT3
        If (Tr3Ar(i).ibus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idi).KV > BusAr(idj).KV) And (BusAr(idi).KV > BusAr(idk).KV) Then
                sumP = sumP + Tr3Ar(i).P1
                sumQ = sumQ + Tr3Ar(i).Q1
            End If
            n = n + 1
        End If
        
        If (Tr3Ar(i).jbus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idj).KV > BusAr(idi).KV) And (BusAr(idj).KV > BusAr(idk).KV) Then
                sumP = sumP + Tr3Ar(i).P2
                sumQ = sumQ + Tr3Ar(i).Q2
            End If
            n = n + 1
        End If
        
        If (Tr3Ar(i).KBus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idk).KV > BusAr(idi).KV) And (BusAr(idk).KV > BusAr(idj).KV) Then
                sumP = sumP + Tr3Ar(i).P3
                sumQ = sumQ + Tr3Ar(i).Q3
            End If
            n = n + 1
        End If
    Next
    If n > 0 Then
        TransPQ = ToComplex(sumP, sumQ)
    Else
        TransPQ = "TransErr"
    End If
    
End Function

Private Function TransRate(ByVal number As Long) As String
    Dim n As Long, i As Long
    Dim idi As Long, idj As Long, idk As Long
    Dim str As String
    str = ""
    For i = 1 To nT3
        If (Tr3Ar(i).ibus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idi).KV > BusAr(idj).KV) And (BusAr(idi).KV > BusAr(idk).KV) Then
                str = str + VBA.Format(Tr3Ar(i).I_PCTRTA, "###0") + "/"
            End If
            n = n + 1
        End If
        
        If (Tr3Ar(i).jbus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idj).KV > BusAr(idi).KV) And (BusAr(idj).KV > BusAr(idk).KV) Then
                str = str + VBA.Format(Tr3Ar(i).J_PCTRTA, "###0") + "/"
            End If
            n = n + 1
        End If
        
        If (Tr3Ar(i).KBus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idk).KV > BusAr(idi).KV) And (BusAr(idk).KV > BusAr(idj).KV) Then
                str = str + VBA.Format(Tr3Ar(i).K_PCTRTA, "###0") + "/"
            End If
            n = n + 1
        End If
    Next
    If (n > 0) And (Len(str) > 0) Then
        TransRate = Left(str, Len(str) - 1) + "%"
    Else
        TransRate = "TransErr"
    End If
    
End Function

Private Function TransParams(ByVal number As Long) As String
    Dim n As Long, i As Long
    Dim idi As Long, idj As Long, idk As Long
    Dim str As String
    Dim s As String
    str = ""
    For i = 1 To nT3
        If (Tr3Ar(i).ibus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idi).KV > BusAr(idj).KV) And (BusAr(idi).KV > BusAr(idk).KV) _
            And (Tr3Ar(i).I_PCTRTA > 0) Then
                str = str + Tr3Ar(i).TransName + "/"
            End If
            n = n + 1
        End If
        
        If (Tr3Ar(i).jbus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idj).KV > BusAr(idi).KV) And (BusAr(idj).KV > BusAr(idk).KV) _
            And (Tr3Ar(i).J_PCTRTA > 0) Then
                str = str + Tr3Ar(i).TransName + "/"
            End If
            n = n + 1
        End If
        
        If (Tr3Ar(i).KBus = number) Then
            idi = BusIndex(Tr3Ar(i).ibus)
            idj = BusIndex(Tr3Ar(i).jbus)
            idk = BusIndex(Tr3Ar(i).KBus)
            If (BusAr(idk).KV > BusAr(idi).KV) And (BusAr(idk).KV > BusAr(idj).KV) _
            And (Tr3Ar(i).K_PCTRTA > 0) Then
                str = str + Tr3Ar(i).TransName + "/"
            End If
            n = n + 1
        End If
    Next
        

    If (n > 0) And (Len(str) > 0) Then
        s = Left(str, Len(str) - 1)
        str = VBA.Replace(s, "-", "")
        TransParams = reName(str)
    Else
        TransParams = "TransErr"
    End If
   
    
End Function


Public Function reName(ByVal s As String) As String
    Dim str As Variant
    str = VBA.Split(s, "/")
    reName = s
    Select Case UBound(str)
        Case 1
            If (str(0) = str(1)) Then
                reName = "2x(" + str(0) + ")"
            End If
        Case 2
            If (str(0) = str(1)) And (str(0) = str(2)) Then
                reName = "3x(" + str(0) + ")"
            End If
        Case 3
            If (str(0) = str(1)) And (str(2) = str(3)) Then
                reName = "2x(" + str(0) + ")/" + "2x(" + str(2) + ")"
            End If
    End Select
    

End Function
