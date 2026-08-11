# ===================================================================================
# Ex name:      PV curve analysis for New England system
# Code:         Nguyen Duc Huy
# Date: 
# Purpose:      Use PSS/E PV analysis engine to determine loadability limits with 
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

VMIN                = 0.85
CHECK_VOLTAGE       = True
CHECK_FLOWS         = True
DISPATCH_MODE       = 1 # 0 = disable, 1 - reserve, 2 -Pmax, 3 - inertia, 4 - governor

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

# PV option, for use with PV_ENGINE_6
pv_option       = [0,   # 1. Tap adjustment
                   0,   # 2. Area interchange adjustment
                   0,   # 3. Phase shift 
                   1,   # 4. DC tap
                   1,   # 5. Switched shunt
                   0,   # 6. Motor treatment flag, = 0
                   1,   # 7. Divergent solution flag, 1 = enable
                   0,   # 8. Solution method, 0 = fdns, 1 = fnsl 
                   0,   # 9. VAR limit base case, 0 = immediately
                   0,   # 10. VAR limit increment solution, 0 = immediately
                   1,   # 11. Rating set, 1 = RATEA
                   1,   # 12. Study source system transfer dispatch method, 1 = positive MW machines, no cost
                   4,   # 13. Sink system transfer dispatch method, 2 = bus with positive constant MVA load
                   1,   # 14. Generation plant limits flag, 1 = honor active limit
                   0,   # 15. Load flag for transfer method, 0 = no limit
                   1,   # 16. Flag to check low voltage, 1 = enable check
                   1,   # 17. Flag to check excessive loading, 1 = enable
                   DISPATCH_MODE,   # 18. Dispatch mode for power unbalances from application of contingencies
                   0,   # 19. Zip archive, 0 = no zip
                   0,   # 20. Contingency case tap adjust
                   0,   # 21. Contingency case area interchange, 0 = disable
                   0,   # 22. Contingency case phase shift adjust
                   0,   # 23. Contingency case DC tap adjust
                   0,   # 24. Contingency case switch shunt
                   0]   # 25. Contingency case induction motor
pv_values       = [1,   # 1. Mismatch tolerance
                   10,  # 2. Transfer increment
                   1,   # 3. Transer increment tol
                   5e3, # 4. Max incremental transfer
                   0.8, # 5. Low voltage threshold
                   120, # 6. Percentage of rating
                   0,   # 7. Minimum incremental transfer
                   -1]  # 8. Power factor for load increase
# ====================================================================================
#                   PERFORM PV ANALYSIS
# ====================================================================================
silence()
ierr            = pv_engine_6(pv_option,
                              pv_values,
                              [r'ALL',          # Source system
                               r'LOADBUS',      # Sink
                               r'ALL'],         # dispatch
                              dfxfile,          #
                              r'',              # load throw
                              r'',              # EDC
                              r'new_england_V32.gov', # gov
                              r'pvres.pv',
                              r'')

if os.path.exists('RESULT.xlsx'):
    os.remove('RESULT.xlsx')
unsilence()
print '\nPV_ENGINE_6 error code = ' + str(ierr) + '\n'
rlst            = pssarrays.pv_summary(pvfile)

lbl             = rlst.colabel

NSCENARIO       = rlst.pvsize.ncase
MBUS            = centre_bus.index(29) # Bus index to draw

# Export data, Bus voltage and power transfer
xl              = workbook()
xl.worksheet_rename(newSheet = r'Sheet1')
xl.worksheet_add_after(newSheet = r'Cont',oldSheet = r'Sheet1',overwritesheet = False)
xl.set_active_sheet(r'Sheet1')
for kk in range(NSCENARIO):
    pvres           = pssarrays.pv_solution(pvfile,lbl[kk])
    NCASE           = len(pvres.mloadmw)
    start_row       = 2 * kk
    for ii in range(NCASE):
            xl.set_cell((start_row + 1,ii+1),pvres.mwtransfer[ii])
            xl.set_cell((start_row + 2,ii+1),pvres.volts[ii][MBUS])

##xl.show()
xl.set_active_sheet(r'Cont')
for kk in range(NSCENARIO):
    xl.set_cell((kk+1,1),lbl[kk])

xl.save('RESULT.xlsx')
# xl.close()

# os.remove(SUBFILE)
os.remove(CONFILE)
os.remove(MONFILE)
os.remove('pvres.pv')
os.remove(dfxfile)
##stop_2()

