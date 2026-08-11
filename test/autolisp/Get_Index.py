Option Explicit
Public Function BusIndex(ByVal number As Long) As Long
    Dim i As Long
    BusIndex = 0
If nBus > 0 Then
    i = 0
    Do
        i = i + 1
        If number = BusAr(i).number Then BusIndex = i
    Loop Until (i >= nBus) Or (BusIndex > 0)
End If
End Function




' Tim nhanh song song
Public Function PBranchIndex(ByVal frombus As Long, ByVal tobus As Long) As Variant
Dim i As Long
Dim nMatch As Long
Dim idx() As Long
ReDim idx(10)

nMatch = 0
If nBranch > 0 Then
    i = 0
    Do
        i = i + 1
        If (frombus = BrnAr(i).frombus) And (tobus = BrnAr(i).tobus) Then
            nMatch = nMatch + 1
            idx(nMatch) = i
        End If
        If (tobus = BrnAr(i).frombus) And (frombus = BrnAr(i).tobus) Then
            nMatch = nMatch + 1
            idx(nMatch) = -i
        End If
    Loop Until (i >= nBranch)
End If

If nMatch >= 0 Then
     ReDim Preserve idx(nMatch)
     idx(0) = nMatch
Else
    ReDim idx(0)
    idx(0) = 0
End If

PBranchIndex = idx
End Function

Public Function T3WIndex(ByVal ibus As Long, ByVal jbus As Long, ByVal KBus As Long, _
                             ByVal ICKT As String) As Long
    
    Dim i As Long
    T3WIndex = 0
If nT3 > 0 Then
    i = 0
    Do
        i = i + 1
        If (((Tr3Ar(i).ibus = ibus) And (Tr3Ar(i).jbus = jbus) And (Tr3Ar(i).KBus = KBus)) _
            Or ((Tr3Ar(i).ibus = ibus) And (Tr3Ar(i).jbus = KBus) And (Tr3Ar(i).KBus = jbus)) _
            Or ((Tr3Ar(i).ibus = jbus) And (Tr3Ar(i).jbus = ibus) And (Tr3Ar(i).KBus = KBus)) _
            Or ((Tr3Ar(i).ibus = jbus) And (Tr3Ar(i).jbus = KBus) And (Tr3Ar(i).KBus = ibus)) _
            Or ((Tr3Ar(i).ibus = KBus) And (Tr3Ar(i).jbus = ibus) And (Tr3Ar(i).KBus = jbus)) _
            Or ((Tr3Ar(i).ibus = KBus) And (Tr3Ar(i).jbus = jbus) And (Tr3Ar(i).KBus = ibus))) _
            And (VBA.UCase(Tr3Ar(i).ICKT) = VBA.UCase(ICKT)) Then
            T3WIndex = i
        End If
    Loop Until (i >= nT3) Or (T3WIndex > 0)
End If

End Function

Public Function T3WIndex1(ByVal number As Long) As Long
    Dim i As Long
    T3WIndex1 = 0
If nT3 > 0 Then
    i = 0
    Do
        i = i + 1
        If (Tr3Ar(i).ibus = number) Or (Tr3Ar(i).jbus = number) _
            Or (Tr3Ar(i).KBus = number) Then
            T3WIndex1 = i
        End If
    Loop Until (i >= nT3) Or (T3WIndex1 > 0)
End If
End Function

Public Function LoadIndex(ByVal number As Long, ByVal LoadID As Long) As Long
    Dim i As Long
    LoadIndex = 0
If nLoad > 0 Then
    i = 0
    Do
        i = i + 1
        If (number = LodAr(i).number) And (LoadID = LodAr(i).ID) Then
            LoadIndex = i
        End If
    Loop Until (i >= nLoad) Or (LoadIndex > 0)
End If
End Function
Public Function GenIndex(ByVal number As Long, ByVal GenID As String) As Long
    Dim i As Long
    GenIndex = 0
    i = 0
    Do
        i = i + 1
        If (number = GenAr(i).number) And (VBA.UCase(GenID) = VBA.UCase(GenAr(i).ID)) Then
            GenIndex = i
        End If
    Loop Until (i >= nGen) Or (GenIndex > 0)
End Function
' Tim vi tri cua nhanh fromBus, ToBus, CKT trong mang BrnAr
Public Function BranchIndex(ByVal frombus As Long, ByVal tobus As Long, ByVal CKT As String) As Long
    Dim i As Long
    BranchIndex = 0
If nBranch > 0 Then
    i = 0
    Do
        i = i + 1
        If (frombus = BrnAr(i).frombus) And (tobus = BrnAr(i).tobus) _
            And (VBA.UCase(CKT) = VBA.UCase(BrnAr(i).CKT)) Then
            BranchIndex = i
        End If
        If (tobus = BrnAr(i).frombus) And (frombus = BrnAr(i).tobus) _
            And (VBA.UCase(CKT) = VBA.UCase(BrnAr(i).CKT)) Then
            BranchIndex = -i
        End If
        
    Loop Until (i >= nBranch) Or (BranchIndex <> 0)
End If
End Function



Public Function Trans2Index(ByVal number As Long) As Long
    Dim i As Long
    Trans2Index = 0
    i = 0
    Do
        i = i + 1
        If (number = BrnAr(i).frombus) Then
            Trans2Index = i
        End If
        If (number = BrnAr(i).tobus) Then
            Trans2Index = -i
        End If
         
    Loop Until (i >= nBranch) Or (Abs(Trans2Index) > 0)
End Function
