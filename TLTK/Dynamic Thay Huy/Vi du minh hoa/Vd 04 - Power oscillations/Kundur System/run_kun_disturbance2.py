# ===================================================================================
# Ex name:    Kundur test system with excitation disturbance
# Code:       Nguyen Duc Huy
# Date: 
# Purpose:    Observe the electromechanical oscillation with small signal disturbance
# Note:       Change MACID and see how local modes change
# ===================================================================================
from __future__ import with_statement
from __future__ import division
from __future__ import division
from contextlib import contextmanager
import os, sys

sys.path.append(r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN")
os.environ['PATH'] = (r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN;"
                      + os.environ['PATH'])
from psspy import *
import random
from dyntools import *
import redirect
from math import *
from csv import *
_i = getdefaultint()
_f = getdefaultreal()
_s = getdefaultchar()
redirect.psse2py()
psseinit(8000)
casedir    = os.path.join(r'')



rawfile    = os.path.join(casedir,'kundur_case.raw')
dyrfile    = os.path.join(casedir,'kundur.dyr')

prgfile    = os.path.join(casedir,'kundur.txt')
outfile    = os.path.join(casedir,'kundur.out')
pfoption = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
            0, # area interchange, 0 = disable
            0, # phase shift adjustment
            1, # DC tap adjustment
            1, # Switched shunt, 0 = disable, 1 = enable
            1, # flat start, 1 = enable
            0, # var limit, 0 = immediately
            0] # non divergent solution
def get_nchan():
    N = 1000
    ierr, rval = chnval(N)
    while ierr == 2:
        N   -= 1
        ierr, rval = chnval(N)
      
    return N

# ====================================================================================================
#                                           MAIN PROGRAM
# ====================================================================================================

    
MACID           = [1]
LOADID          = [7,9]

##f.close() 

Tdis            = 1
Toffset         = 0
Tfinal          = 30
ierr            = progress_output(2, prgfile, [1, 0])
read(0,rawfile)
ier             = fnsl(pfoption)
# Voltage at target machine
erf             = bsys(sid = 2,numbus = len(MACID),buses = MACID)
ir,vol          = abusreal(sid = 2,string = 'PU')
vol             = vol[0]

ier             = cong(0)
# Load model
PZ = 100
PI = 0
QZ = 0
QI = 100
DELTA_T         = 0.002

# ====================================================================================================
#                                     INITIALIZE 
# ====================================================================================================
dynamics_solution_params([_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,DELTA_T,_f,_f],'',)
ierr, rlods     = conl(0, 1, 1, [0,0], [PI, PZ, QI, QZ])
ierr, rlods     = conl(0, 1, 2, [0,0], [PI, PZ, QI, QZ])
ierr, rlods     = conl(0, 1, 3, [0,0], [PI, PZ, QI, QZ])
ier             = dynamicsmode(1)
ier             = dyre_new([1,1,1,1],dyrfile,'','','')

ier             = chsb(0, 1, [1, -1, -1, 1, 7, 1])  # Speed
ier             = chsb(0,1,[-1,-1,-1,1,2,0])        # Pmech
ier             = chsb(0,1,[-1,-1,-1,1,13,0])       # Voltage
ier             = chsb(2,0,[-1,-1,-1,1,11,0])       # Vref
ier             = strt(1,outfile)
ier             = run(0, Tdis, 5000, 10, 1)


# Change Vref
print vol


for ii in range(0,len(MACID)):
    vol_new         = vol[ii] + 0.02      
    ierr            = change_vref(ibus = MACID[ii], id = r'1', newval = vol_new)
    Tdis            += Toffset
    ier             = run(0, Tdis, 5000, 10, 1)

##ier             = run(0, Tdis + (Tfinal-Tdis)/2, 5000, 10, 1)
##
##for ii in range(0,len(MACID)):
##    vol_new         = vol[ii] - 0.02      
##    ierr            = change_vref(ibus = MACID[ii], id = r'1', newval = vol_new)
##    Tdis            += Toffset

    
ier             = run(0, Tfinal, 5000, 10, 1)

# ====================================================================================================
#                                      EXPORT DATA
# ====================================================================================================
nchan           = get_nchan()
nchan           += 1
chnobj          = CHNF(outfile)
chnobj.txtout(channels = range(1,nchan),txtfile = r'kun_out.txt')
close_powerflow()
stop_2()
