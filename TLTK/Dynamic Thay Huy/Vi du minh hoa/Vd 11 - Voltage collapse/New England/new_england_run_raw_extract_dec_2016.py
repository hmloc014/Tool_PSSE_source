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


casedir     = os.path.join('')
rawfile     = os.path.join(casedir,'new_england_V32.RAW')

dyrfile     = os.path.join(casedir,'new_england_V32.dyr')

outfile     = os.path.join(casedir,'ne_2.out')
prgfile     = os.path.join(casedir,'ne_.txt')


# case 38
LBUS        = 29
T_trip      = 62
# case 32
##LBUS        = 12
##T_trip      = 100
# case 35
##LBUS        = 41
##T_trip      = 100

def get_nchan():
    N = 1000
    ierr, rval = psspy.chnval(N)
    while ierr == 2:
        N   -= 1
        ierr, rval = psspy.chnval(N)
      
    return N


MACID       = 38
SHEDLOAD    = 0

redirect.psse2py()
pfoption = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
            0, # area interchange, 0 = disable
            0, # phase shift adjustment
            1, # DC tap adjustment
            1, # Switched shunt, 0 = disable, 1 = enable
            1, # flat start, 1 = enable
            0, # var limit, 0 = immediately
            0] # non divergent solution

PI      = 30
PZ      = 25
QI      = 30
QZ      = 30

genbus  = [30,31,32,33,34,35,36,37,38,39]


psspy.read(0,rawfile)
# Progress output file
ierr            = psspy.progress_output(2, prgfile, [1, 0])

#
psspy.bsys(sid = 4,numbus = 2, buses = [28,29])

# AREA 55
er, nload       = psspy.aloadcount(sid = 4, flag = 1)
er, (lbus,)     = psspy.aloadint(sid = 4, flag = 1, string = ['NUMBER'])

# power flow
ier             = psspy.fnsl(pfoption)
print 'Power flow sol = ',ier
ier             = psspy.cong(0)
ierr, rlods     = psspy.conl(0, 1, 1, [0,0], [PI, PZ, QI, QZ])
ierr, rlods     = psspy.conl(0, 1, 2, [0,0], [PI, PZ, QI, QZ])
ierr, rlods     = psspy.conl(0, 1, 3, [0,0], [PI, PZ, QI, QZ])

er,(mvalod,ilod,ylod) = psspy.aloadcplx(sid = 4, flag = 1, string = ['MVAACT','ILACT','YLACT'])

ier             = psspy.dynamicsmode(1)
ier             = psspy.dyre_new([1,1,1,1],dyrfile,'','','')

ier             = psspy.dynamics_solution_param_2(realar3 = 0.005)
ier             = psspy.set_osscan(status = 1, trip = 0)

# Skip adding channels if this is not first time run
if 'ALREADY_RUN' in globals():
	print 'Not first time run, channel added'
else:
    # Speed channel
    ier             = psspy.chsb(0, 1, [1, -1, -1, 1, 7, 1])
    # EFD
    ier             = psspy.chsb(0, 1, [11, -1, -1, 1, 5, 1])
    # OEL
    ier             = psspy.chsb(0, 1, [21, -1, -1, 1, 24, 1])
    # Reactive output
    ier             = psspy.chsb(0, 1, [31, -1, -1, 1, 2, 1])
    # Voltage 
    ier             = psspy.chsb(0, 1, [41, -1, -1, 1, 13, 0])
    # System total
    ier             = psspy.chsb(0, 1, [-1, -1, -1, 7, 0, 0])

# R and X, all branches
##ier             = psspy.chsb(0, 1, [123, -1, -1, 1, 18, 0])

###################### READ DATA FROM FILE.CSV#######################
# Data Structure in line
# From(0) - To(1) - Id(2) - R(3) - X(4) - theta(5) - Z - R1(7) - X1(8) - theta1(9)
#                                   - R2(10) - X2(11) - theta2(12) - Z2
ALREADY_RUN = 1
SZD_1 = open('SetZoneData.csv')
SZD_2 = SZD_1.readlines()
SZD = []
for x in range (0, len(SZD_2)):
    SZD_3 = [float(s) for s in SZD_2[x].split(',')]
    SZD.append(SZD_3)

##TimerArray
Tmer = [0]*len(SZD_2)
ss   = 42
Sup  = [[0]*ss]*ss
TimeDelay = 0.2
#####################################################################
for y in range (0,len(SZD)):
    chname      = str(SZD[y][0]) + '-to-' + str(SZD[y][1])
##    ierr        = psspy.branch_app_r_x_channel([-1,-1,-1,int(SZD[y][0]),int(SZD[y][1])],'1',chname)
    # Try to add relay model
    idata 		= [int(1),int(1),int(SZD[y][0]),int(SZD[y][1]),int(SZD[y][2]),0,0,0,0,0,0]
    chdata              = [r'',r'',r'',r'',r'',r'',r'',r'',r'',r'',r'']
    rdata 		= [   0,SZD[y][8],SZD[y][9],SZD[y][8]/2, 		                # zone 1
				   0.3,SZD[y][11],SZD[y][12],SZD[y][11]/2, 	                # zone 2
				   0.8,SZD[y][11]*1.2,SZD[y][12]*1.4,SZD[y][11]*1.4/2,		# Zone 3
				   170,1,3,100000,3,100000,					# breaker time
				   2,10,90,
				   2,10,90] 
    ierr 		= psspy.add_relay_model(int(SZD[y][0]),int(SZD[y][1]),  # From and to bus
                            str(int(SZD[y][2])),1,r'DISTR1',  	                # id,rs,name,
                            11, 				                # 'DISTR1' requires 11 ICON
                            idata,
                            chdata,					        # chdata
                            24,					                # ncon,
                            rdata)
#    ierch               = psspy.change_rlmod_icon(int(SZD[y][0]),int(SZD[y][1]),r'1',1,r'DISTR1',2,1)
    print 'relay add ',ierr

# Placing gen overspeed relays
instance = 0
for ii in genbus:
    instance            += 1 
    ierr 		= psspy.add_cctmsco_model(model = r'FRQTPAT',
                                                  mins = instance,
                                                  nicn = 3, idata = [ii,ii,1],
                                                  chdata = [r'',r'',r''],
                                                  ncon = 4,
                                                  rdata = [46,54,0.2,0.06])
	
ierr            = psspy.dyda(sid = 0, all = 1, status = [2,1], out = 0, ofile = r'tt2.dyr')
print           'savedata = ',ierr
ier             = psspy.strt(1,outfile)
ier             = psspy.run(0, 1, 1000, 10, 1)

for t in range(2,180):# System collapse or islands if no UVLS installed, at ~100s
    ierun           = psspy.run(0, t, 1000, 10, 1)
    print 'Time is: ', t, ierun
####    er              = psspy.powerflowmode()
##    fname           = 'new_eng_' + str(t) + '.raw'
##    ierr            = psspy.writerawversion('33', 0, fname)
##    er              = psspy.dynamicsmode()
    if t == 5:
        ierr            = psspy.dist_machine_trip(MACID,r'1')
        print 'Trip error ', ierr
    # Intelligent UVLS
    if t == 50:
        for ii in range(0,nload):
            iers        = psspy.load_chng_4(i = lbus[ii], id = r'1', realar = [mvalod[ii].real*0.5,
                                                                               mvalod[ii].imag*0.5,
                                                                               ilod[ii].real*0.5,
                                                                               ilod[ii].imag*0.5,
                                                                               ylod[ii].real*0.5,
                                                                               -ylod[ii].imag*0.5])
            



##ierr            = psspy.load_chng_4(i = 29, id = r'1', realar = [150,0,0,0,0,0])
##ier             = psspy.run(0, 100, 1000, 10, 1)


chnobj          = CHNF(outfile)
txtout          = r'NE_chn.txt'
nchan           = get_nchan()
nchan           += 1
print 'Number of channels is: ',nchan
chnobj.txtout(channels = range(1,nchan),txtfile = txtout)


er              = psspy.powerflowmode()
    
ierr            = psspy.writerawversion('33', 0, 'new_eng_final.raw')
psspy.close_powerflow()

er = psspy.stop_2()
print 'exit code = ',er

