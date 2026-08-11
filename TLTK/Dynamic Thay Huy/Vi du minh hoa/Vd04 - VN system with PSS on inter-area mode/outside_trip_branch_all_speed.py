# ===================================================================================
# Ex name:    Vn power system with oscillations
# Code:       Nguyen Duc Huy
# Date: 
# Purpose:    Observe the system dominant modes, analysis using DSI Toolbox
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
import redirect
from math import *
from csv import *

from dyntools import *
_i = getdefaultint()
_f = getdefaultreal()
_s = getdefaultchar()
redirect.psse2py()
psseinit(50000)
casedir     = os.path.join(r'')
casefile    = os.path.join(casedir,'gio_down.sav')

##dyrfile     = os.path.join(casedir,'VN_nowind_1.dyr') 
dyrfile    = os.path.join(casedir,'VN_nowind_1_noPSS.dyr')



prgfile     = os.path.join(casedir,'VN_branch_trip.txt')
outfile     = os.path.join(casedir,'VN_wind_2.out')
pfoption    = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
                0, # area interchange, 0 = disable
                0, # phase shift adjustment
                1, # DC tap adjustment
                1, # Switched shunt, 0 = disable, 1 = enable
                0, # flat start, 1 = enable
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


MACID         	= [936021,928011,919011,923011,938011,978082,971011]
PG_MAX          = [330,330,340,340,300,500,300,300]
PGEN            = [280.85,290.84,247.6,284.4,287.9,399,249.4,249.4]
##PMIN
LOADID          = [285149,285050,285107,285109,285111,285114,285138,
                   28543,285146,285147,285149,734058,734059,125019,125053,126001,128832]
windbus         = [2,3,4,5,6,7,9,10,12,13,14,15,16,18,19,20,21,48,50,54]

case(casefile)
obs_sys         = [983042,  # OMON
                   978022,  # PHU MY
                   938011,  # VUNG ANG
                   919013,  # SON LA
                   923012   # HOA BINH
                   ]
windbus         = [2,3,4,5,6,7,9,10,12,13,14,15,16,18,19,20,21,48,50,54]
# New subsystem. Speeds from these gens will be observed
bsys(sid = 4, numbus = len(obs_sys),buses = obs_sys)
bsys(sid = 5,numbus = len(windbus),buses = windbus)

##chan_Pgen
ierr, (machid,)     = amachchar(sid=-1, flag=1, string="ID")
ierr, (machbus,)    = amachint(-1,1,'NUMBER')
ierr,(pg,)          = amachreal(-1,1,'PGEN')

##chan_Pload
ierr, (loadbusid,)  = aloadchar(sid=-1, flag=1, string="ID")#id_bus
ierr, (loadbus,)    = aloadint(sid=-1, flag=1, string="NUMBER")#vitri_bus
ierr, (sloadbus,)   = aloadreal(sid=-1, flag=1, string="TOTALACT")#MVA-loadbus

##
ierr, (area,)       = aareaint(sid=-1, flag=1, string="NUMBER")
ierr, (ploadarea,)  = aareareal(sid=-1, flag=1, string="PLOAD")
ierr, (pgarea,)     = aareareal(sid=-1, flag=1, string="PGEN")

##change_Pload
ierr, (loadbusid,)  = aloadchar(sid=-1, flag=1, string="ID")#id_bus
ierr, (loadbus,)    = aloadint(sid=-1, flag=1, string="NUMBER")#vitri_bus

##
ierr, (ploadarea1,) = aareareal(sid=-1, flag=1, string="PLOAD")
ierr, (pgarea1,)    = aareareal(sid=-1, flag=1, string="PGEN")
ierr,(pg1,)         = amachreal(-1,1,'PGEN')
##change progress output file
ierr                = progress_output(2, prgfile, [1, 0])
#power flow
ier                 = fnsl(pfoption)
ier                 = cong(0)
# Load model
PI      = 100
PZ      = 0
QI      = 0
QZ      = 100
ierr, rlods         = conl(0, 1, 1, [0,0], [PI, PZ, QI, QZ])
ierr, rlods         = conl(0, 1, 2, [0,0], [PI, PZ, QI, QZ])
ierr, rlods         = conl(0, 1, 3, [0,0], [PI, PZ, QI, QZ])
ier                 = dynamicsmode(1)
ier                 = dyre_new([1,1,1,1],dyrfile,'','','')
#timestep
ier                 = dynamics_solution_param_2([_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f, 0.0025,_f,_f,_f,_f,_f])
#channel
ier                 = chsb(4, 0, [1, -1, -1, 1, 7, 1])  # Speed

ier                 = strt(1,outfile)

ier                 = run(0,1,5000, 10, 1)

## trip branch

BRANID = 271001  #271001 # HAMTHUAN 936021 #NGHISON
        
# Disturbance
ier             = dist_branch_trip(60097,77013,'1')
ier             = run(0, 30, 5000, 10, 1)

nchan           = get_nchan()
nchan           += 1
chnobj          = CHNF(outfile)

chnobj.txtout(channels = range(1,nchan),txtfile = r'branch_trip.txt')

stop_2()
##
