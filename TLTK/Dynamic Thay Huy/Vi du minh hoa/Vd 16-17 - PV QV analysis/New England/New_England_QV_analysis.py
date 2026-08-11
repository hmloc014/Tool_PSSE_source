# ===================================================================================
# Ex name:      QV curve analysis for New England system
# Code:         Nguyen Duc Huy
# Date: 
# Purpose:      Use PSS/E QV analysis engine to determine loadability limits with 
#               generation and branch contingencies.
#               Play with different dispatch mode (0 to 4) to see the effect
# ===================================================================================
import sys, os, csv

sys.path.append(r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN")
os.environ['PATH'] = (r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN;"
                      + os.environ['PATH'])
import pssarrays
from psspy import *
import numpy
from excelpy import *

import redirect

redirect.psse2py()
psseinit()
OLD_STDOUT = sys.stdout
def silence(file_object = None):
    """
    Discard stdout (i.e. write to null device) or
    optionally write to given file-like object.
    """
    if file_object is None:
        file_object = open(os.devnull, 'w')

    try:
        sys.stdout = file_object
    except:
        sys.stdout = OLD_STDOUT
    return

def unsilence():
    """
    Reset stdout to the terminal like normal
    """
    sys.stdout = OLD_STDOUT
    return

CORRECTIVE_ACTION = True

casefile    = r"new_england_V32.sav"

case(casefile)
# =============================================================================================

# Power flow option
pfoption = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
            0, # area interchange, 0 = disable
            0, # phase shift adjustment
            1, # DC tap adjustment
            1, # Switched shunt, 0 = disable, 1 = enable
            0, # flat start, 1 = enable
            0, # var limit, 0 = immediately
            0] # non divergent solution

fnsl(pfoption)

# ============================================================================================
#                                          BUILD DFAX
# ============================================================================================
dfxfile         = r'NewEngland.dfx'
SUBFILE         = 'SUBFILE.sub'
MONFILE         = 'MONFILE.mon'
CONFILE         = 'CONFILE.con'
pvfile          = r'pvres.pv'


# ============================================================================================
#                                           OPTION
# ============================================================================================
MACHINE_IN_OTHER_ISLAND = []
VMAX                = 1.1
VMIN                = 0.8
QVBUS               = 29
CHECK_VOLTAGE       = True
CHECK_FLOWS         = True
DISPATCH_MODE       = 4 # 0 = disable, 1 - reserve, 2 -Pmax, 3 - inertia, 4 - governor

# 1. CENTRE BUS
CENTRE_BUS          = 0
CENTRE_BUSNUM       = [29]
ierr                = bsys(sid = CENTRE_BUS, numbus = len(CENTRE_BUSNUM), buses = CENTRE_BUSNUM)
ierr, (centre_bus,) = abusint(sid = CENTRE_BUS, flag = 1, string = r"NUMBER")

# 2. BRANCH
BRANCH              = 1
ierr                = bsys(sid = BRANCH, usekv = 1, basekv = [200.,500.])
ierr,(cbus,)        = abusint(sid = BRANCH, flag = 1, string = r"NUMBER")
# 3. MACHINE
ierr,(mbus,)        = agenbusint(sid = -1, flag = 1, string = r"NUMBER")
# 4. ALL MACHINE
ierr,(sbus,)        = agenbusint(sid = -1, flag = 1, string = r"NUMBER")
# ============================================================================================
#                                          SUBSYSTEM DEF
# ============================================================================================
CENTRE          = r'LOADBUS'
BRNCON          = r'CONTINGENCY_BRANCH'
MACCON          = r'CONTINGENCY_MACHINE'
SYS_ALL         = r'ALL'
# ============================================================================================
#                                          SUBSYSTEM FILE
# ============================================================================================
# 1. CENTRE
fo          = open(SUBFILE, 'w')  # Open 
wstr        = "SUBSYSTEM '" + CENTRE + "' \n"
fo.write(wstr)
for bid in centre_bus:
    wstr = '   BUS ' + str(bid) + ' \n'
    fo.write(wstr)
fo.write('END \n')
# 2. CONTINGENCY BRANCH
wstr        = "SUBSYSTEM '" + BRNCON + "' \n"
fo.write(wstr)
for bid in cbus:
    wstr = '   BUS ' + str(bid) + ' \n'
    fo.write(wstr)
fo.write('END \n')
# 3. CONTINGENCY MACHINE
wstr        = "SUBSYSTEM '" + MACCON + "' \n"
fo.write(wstr)
for mac in mbus:
    if mac not in MACHINE_IN_OTHER_ISLAND:
        wstr = '   BUS ' + str(mac) + ' \n'
        fo.write(wstr)
fo.write('END \n')
# 4. ALL MACHINE
wstr        = "SUBSYSTEM '" + SYS_ALL + "' \n"
fo.write(wstr)
for bid in sbus:
    if bid not in MACHINE_IN_OTHER_ISLAND:
        wstr = '   BUS ' + str(bid) + ' \n'
        fo.write(wstr)
fo.write('END \n')
fo.write('END \n')

fo.close()
# ============================================================================================
#                                       MONITOR FILE
# ============================================================================================
fo          = open(MONFILE, 'w')  # Open and append
if CHECK_FLOWS:
    wstr        = "MONITOR BRANCHES IN SUBSYSTEM '" + SYS_ALL + "' \n"
    fo.write(wstr)
if CHECK_VOLTAGE:
    wstr        = "MONITOR VOLTAGE RANGE SUBSYSTEM '" + CENTRE + "' " + str(VMIN) + " \n"
    fo.write(wstr)
fo.write('END \n')
fo.close()
# ============================================================================================
#                                      CONTINGENCY FILE
# ============================================================================================
fo          = open(CONFILE, 'w')  # Open and append

##wstr        = "SINGLE BRANCH IN SUBSYSTEM '" + BRNCON + "' \n"
##fo.write(wstr)
wstr        = "SINGLE MACHINE IN SUBSYSTEM '" + MACCON + "' \n"
fo.write(wstr)
fo.write('END \n')
fo.close()
# ============================================================================================
#                                  DISTRIBUTION FACTOR FILE
# ============================================================================================
option = [1,0]
ierr = dfax(options = option,subfile = SUBFILE,monfile = MONFILE, confile = CONFILE, dfxfile = dfxfile)
unsilence()
print '\nBUILD DFAX error code = ' + str(ierr) + '\n'
silence()
# ============================================================================================
#                                       PV ANALYSIS
# ============================================================================================

# QV option, for use with PV_ENGINE_6
qv_options      = [0,       # 1. Tap adjustment
                   0,       # 2. Area interchange adjustment
                   0,       # 3. Phase shift 
                   1,       # 4. DC tap
                   1,       # 5. Switched shunt
                   0,       # 6. Motor treatment flag, = 0
                   0,       # 7. Divergent solution flag, 1 = enable
                   0,       # 8. Solution method, 0 = fdns, 1 = fnsl 
                   0,       # 9. VAR limit for the VHI power flow solution, 0 = immediately
                   0,       # 10. VAR limit increment solution, 0 = immediately
                   QVBUS,   # 11. Study bus number
                   DISPATCH_MODE,       # 12. Dispatch mode for power unbalances resulting from the application of contingencies
                   0]       # 13. ZIP Archive file 
# ====================================================================================
#                   PERFORM QV ANALYSIS
# ====================================================================================
silence()
MWTOL           = 2
VSTEP           = 0.01
qv_values       = [MWTOL,
                   VMAX,
                   VMIN,
                   VSTEP]
# Subsystem name
SNAME           = r'ALL'
Load_throwover  = r''
QVFILE          = r'qv_file.qv'

ierr            = qv_engine_4(qv_options,
                              qv_values,
                              r'ALL',
                              dfxfile,
                              r'',      # load throw
                              r'new_england_V32.gov',      # inertia and gov
                              r'qv_file.qv',
                              r'')
print '\nQV_ENGINE_4 error code = ' + str(ierr) + '\n'
if os.path.exists('RESULTQV.xlsx'):
    os.remove('RESULTQV.xlsx')
unsilence()

qvsum       = pssarrays.qv_summary(QVFILE)

if qvsum.ierr == 0:
    print 'QV analysis of bus ',qvsum.qvbus,' finished successfully'
    print 'Number of cases analyzed: ', qvsum.qvsize.ncase
    print 'Number of monitored bus voltages: ', qvsum.qvsize.nmvbus
    print 'Number of monitored generator buses: ', qvsum.qvsize.nmgnbus


lbl         = qvsum.colabel

NSCENARIO   = qvsum.qvsize.ncase

try:
    os.remove('QV_RESULT.xlsx')
except:
    print 'There is no old result file...'

xl = workbook()
xl.worksheet_rename(newSheet = r'Sheet1')
xl.worksheet_add_after(newSheet = r'Cont',oldSheet = r'Sheet1',overwritesheet = False)
xl.set_active_sheet(r'Sheet1')
for k in range(NSCENARIO):
    qvres = pssarrays.qv_solution(QVFILE,lbl[k])
    NCASE = len(qvres.vsetpoint)
    for i in range(NCASE):
        if qvres.cnvflag[i] == True:
            xl.set_cell((2*k+1,i+1),qvres.vsetpoint[NCASE-1-i])
            xl.set_cell((2*k+2,i+1),qvres.mgenmvar[NCASE-1-i][0])
        else:
            xl.set_cell((2*k+1,i+1),qvres.vsetpoint[NCASE-1-i])
            xl.set_cell((2*k+2,i+1),-100.0)

xl.set_active_sheet(r'Cont')
for kk in range(NSCENARIO):
    xl.set_cell((kk+1,1),lbl[kk])
xl.show()
xl.save('QV_RESULT.xlsx')
##xl.close()

os.remove(SUBFILE)
os.remove(CONFILE)
os.remove(MONFILE)
os.remove(QVFILE)
os.remove(dfxfile)


##stop_2()

