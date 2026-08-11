Option Explicit

Type TBus
    number As Long
    Name As String
    KV As Double
    PU As Double
    ANG As Double
End Type

Type TLoad
    number As Long
    ID As String
    PL As Double
    QL As Double
End Type

Type TBranch
    frombus As Long
    tobus As Long
    CKT As String
    P As Double
    Q As Double
    PCTRTA As Double ' PERCENT CURRENT OF RATE A
    TypeName As String
    TypeData  As Double
End Type

Type TGEN
    number As Long
    ID As Long
    PG As Double
    QG As Double
    Pmax As Double
End Type

Type T3WTrans
    ibus As Long
    jbus As Long
    KBus As Long
    ICKT As String
    P1 As Double
    Q1 As Double
    P2 As Double
    Q2 As Double
    P3 As Double
    Q3 As Double
    I_PCTRTA As Double
    J_PCTRTA As Double
    K_PCTRTA As Double
    TransName As String
End Type


    


