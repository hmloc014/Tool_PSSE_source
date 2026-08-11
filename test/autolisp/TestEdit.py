Sub copytext()
    Dim sset As ZcadSelectionSet
    Dim FilType(0) As Integer
    Dim FilData(0) As Variant
    FilType(0) = 0
    FilData(0) = "Text"
    Set sset = ThisDrawing.SelectionSets.Add("copytext1")
    sset.SelectOnScreen FilType, FilData
    If sset.Count = 0 Then
        GoTo ext
    End If
    
    Dim obj As ZcadText
    Open "c:\cadflow.txt" For Output As 1
    
    For Each obj In sset
            Write #1, obj.TextString
    Next
    Close #1
ext:
    If Not sset Is Nothing Then
        sset.Delete
    End If
    
End Sub
