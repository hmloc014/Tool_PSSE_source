# ===================================================================================
# Ex name:    Vn power system with N - 1 branch contingency
# Code:       Nguyen Duc Huy
# Date: 
# Purpose:    Observe the voltage collapse phenomena
# ===================================================================================
from __future__ import with_statement
from __future__ import division
from __future__ import division
from contextlib import contextmanager
import os, sys

sys.path.append(r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN")
os.environ['PATH'] = (r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN;"
                      + os.environ['PATH'])
import psspy
import random
from dyntools import *
import redirect
from math import *
from csv import *

_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()

redirect.psse2py()
psspy.psseinit(8000)
casedir    = os.getcwd()

##=========================================================
# Get the number of channel already in the channel list
def get_nchan():
    N = 1000
    ierr, rval = psspy.chnval(N)
    while ierr == 2:
        N   -= 1
        ierr, rval = psspy.chnval(N)
    print N
    
    return N
##=========================================================

##dyrfile     = os.path.join(casedir,'dyr_full_ptc1_noRL.dyr')
##dyrfile     = os.path.join(casedir,'dyr_full_ptc1.dyr')
dyrfile     = os.path.join(casedir,'dyr_full_ptc1_uvls.dyr')
outfile     = os.path.join(casedir,'kk.out')
prgfile     = os.path.join(casedir,'VN_test_py_.txt')

##file_name_  = os.path.join(casedir,'d16_RL_xxxvn_snap_at')

file_name_      = 'd16_RL_xxxvn_snap_at'
freq_file       = 'freq_'
freq_channel    = [43,80,150]
#C:\PSSE
#                        ADD PATH

import datetime
tstart      = datetime.datetime.now().time()
DELTA_T     = 0.005

#redirect.psse2py()
pfoption = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
            0, # area interchange, 0 = disable
            0, # phase shift adjustment
            1, # DC tap adjustment
            1, # Switched shunt, 0 = disable, 1 = enable
            1, # flat start, 1 = enable
            0, # var limit, 0 = immediately
            0] # non divergent solution


##print "open file error: ", ierr
psspy.case('vn2011_220.sav')

psspy.bsys(sid = 3,usekv = 1, basekv = [499, 501])

psspy.bsys(sid = 4,numarea = 1, areas = [55])


# Progress output file
ierr            = psspy.progress_output(2, prgfile, [1, 0])
# power flow
ier             = psspy.fnsl(pfoption)
ier             = psspy.cong(0)
# Load model
PZ = 40
PI = 5
QZ = 45
QI = 5
t2 = 1
### Branch trip
##ibus            = 70205
##jbus            = 70215
##id              = '1'
#
ierr, rlods     = psspy.conl(0, 1, 1, [0,0], [PI, PZ, QI, QZ])
ierr, rlods     = psspy.conl(0, 1, 2, [0,0], [PI, PZ, QI, QZ])
ierr, rlods     = psspy.conl(0, 1, 3, [0,0], [PI, PZ, QI, QZ])
ier             = psspy.fact()
ier             = psspy.dynamicsmode(1)
ier             = psspy.dyre_new([1,1,1,1],dyrfile,'','','')
# Set time step
ier             = psspy.dynamics_solution_params([_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,DELTA_T,_f,_f],'',)
ier             = psspy.chsb(0, 1, [1, -1, -1, 1, 7, 1])
ier             = psspy.chsb(3, 0, [-1, -1, -1, 1, 13, 0])
ier             = psspy.chsb(0, 1, [-1, -1, -1, 7, 0, 0])

Nchan           = get_nchan()
ierr, machs     = psspy.amachcount(-1, 4) # Get the number of machine speed channel if all channels are included
##print 'Current channel number is: ', N
##ier             = psspy.chsb(0, 1, [machs + 1, -1, -1, 1, 13, 1])
ier             = psspy.strt(1,outfile)
# Run to 1sec
ier             = psspy.run(0, t2, 5000, 10, 1)

file_name       = file_name_ + str(t2) + '.raw'
er              = psspy.powerflowmode()
ierr            = psspy.writerawversion('33', 0, file_name)
print 'Error when writing', ierr
ierr            = psspy.dynamicsmode(0)
print 'Returning error = ', ierr

ierr1           = psspy.dist_branch_trip(77105, 77155, '1')
ierr2           = psspy.dist_branch_trip(70205, 70215, '1')
ierr3           = psspy.dist_branch_trip(70215, 77155, '1')
print 'Branch trip error = ', ierr1, ierr2,ierr3

for iii in range(0,200):
    t2              = t2 + 1
    ier             = psspy.run(option = 0, tpause =  t2,nplt = 10)
##    file_name       = file_name_ + str(t2) + '.raw'
##    er              = psspy.powerflowmode()
##    ierr            = psspy.writerawversion('33', 0, file_name)
##    print 'Error when writing at time = ',t2,' s', ierr
##    print   file_name
##    ierr            = psspy.dynamicsmode(0)
##    if t2 == 140:
##        iers        = psspy.load_chng_4(i = 79112, id = r'1', realar = [0,0,0,0,0,0])
##        print 'Load shed: ',iers


tend            = datetime.datetime.now().time()

psspy.powerflowmode()
psspy.close_powerflow()
psspy.stop_2()
