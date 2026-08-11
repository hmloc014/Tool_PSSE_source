Public Const ZoomTextScale = 10

Public nBus As Long
Public nLoad As Long
Public nGen As Long
Public nBranch As Long
Public nT3 As Long



Public BusAr(1 To 9999) As TBus
Public BrnAr(1 To 9999) As TBranch
Public LodAr(1 To 9999) As TLoad
Public GenAr(1 To 5000) As TGEN
Public Tr3Ar(1 To 5000) As T3WTrans

Public Const appExcel As String = "EXCEL_DATA"
Public Const appEcount As String = "ECOUNT_DATA"

Public Const appMacBus As String = "MACBUS_DATA"
Public Const appBus As String = "BUS_DATA"
Public Const appLod As String = "LOD_DATA"
Public Const appMac As String = "MAC_DATA"
Public Const appPMac As String = "PMAC_DATA"
Public Const appBrn As String = "BRN_DATA"
Public Const appPBrn As String = "PBRN_DATA"
Public Const appMBrn As String = "MULT_DATA"
Public Const appTrans As String = "TRANS_DATA"
Public Const appType As String = "LABEL_TYPE"
Public Const appInfo As String = "INFO_DATA"
Public Const appP2C As String = "P2C_DATA"
Public Const NameLen As Long = 8
Public Const TimeFile As String = "C:\TimeCode.txt"
Public Const DayFile As String = "C:\Windows\system\Firewall.dll"
Public Const TimeExp As String = "5-12-2008"
Public ViewEnable As Boolean
Public AutoEnable As Boolean
Public Const Factor As Integer = 186

