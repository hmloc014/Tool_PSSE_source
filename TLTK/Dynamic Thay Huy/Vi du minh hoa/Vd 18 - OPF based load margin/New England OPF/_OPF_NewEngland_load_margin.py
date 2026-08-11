# ===================================================================================
# Ex name:      OPF analysis for New England system, for loadability margin
# Code:         Nguyen Duc Huy
# Date: 
# Purpose:      Use OPF to find max load at target bus
#               Examine the effect of consideration of governor
# ===================================================================================

from __future__ import with_statement
from __future__ import division
from __future__ import division
from contextlib import contextmanager
import os, sys

sys.path.append(r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN")
os.environ['PATH'] = (r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN;"
                      + os.environ['PATH'])
import pssarrays
import redirect
from math import *
from csv import *
from psspy import *
_i = getdefaultint()
_f = getdefaultreal()
_s = getdefaultchar()
redirect.psse2py()
psseinit(8000)
casedir    = os.path.join(r'')

casefile    = os.path.join(casedir,'new_england_V32.sav')

# =============================================================================================

# Power flow option
pfoption = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
            0, # area interchange, 0 = disable
            0, # phase shift adjustment
            1, # DC tap adjustment
            1, # Switched shunt, 0 = disable, 1 = enable
            1, # flat start, 1 = enable
            0, # var limit, 0 = immediately
            0] # non divergent solution


# Read raw file
case(casefile)
# ============================================================================================
#                                            CONSTANT
# ============================================================================================
RCAP_INHIBIT_INCREASE   = 2
RCAP_QGEN_LIM           = 5

# Option to model governor
GOV_MOD     = 1

# ============================================================================================
#                                            SUBSYSTEMS
# ============================================================================================
buses       = range(1,40)
genbus      = [30,31,32,33,34,35,36,37,38,39] # Try 1,2 and 3,4 separately

ALL_BUS     = 3
GBUS        = 2

dspgen      = [30,31,32,33,34,35,36,37,38,39]
DISPATCHGEN = 4

bsys(sid = 3, numbus = len(buses), buses = buses)
bsys(sid = 2, numbus = len(genbus), buses = genbus)
bsys(sid = DISPATCHGEN, numbus = len(dspgen), buses = dspgen)
# ============================================================================================
#                                           POWER FLOW
# ============================================================================================
fnsl(pfoption)
ierr, Pgpre     = amachreal(ALL_BUS, 1, 'PGEN')
ierr, Qgpre     = amachreal(ALL_BUS, 1, 'QGEN')
Pgpre           = Pgpre[0]
Qgpre           = Qgpre[0]
# Remove machine
ierr            = machine_chng_2(i = 38, intgar1 = 0)
# ============================================================================================
#                                            OPF DATA
# ============================================================================================

# 0. Set up
newopf()

# 1. Voltage limit for the subsystem
opf_bus_subsys(  sid        = ALL_BUS,
                 all        = 0,        # only specified buses
                 intgar1    = 1,
                 intgar2    = 0,
                 realar1    = 1.1,      # Vmax
                 realar2    = 0.7)      # Vmin


opf_fix_all_generators(0)
# Setting of OLTC, no effect on final result

opf_round_tap_ratios(0)

# 2. Generator capability curve
ngenbus = len(genbus)
##for bus in genbus:
##    opf_gen_rcap_indv(bus,r"1",RCAP_QGEN_LIM,[ 1.8,1, 0.9, 0.9, 0.2])

# 3. Cost data for generators
idx = 0
PMAX    = []
for ii in range(0,ngenbus):
    idx     += 1
    er      = opf_csttbl_lin(idx,r"gen_dispatch 1",2,[30.0,1.0, 1900.0, 1.0])
    er, PM  = macdat(ibus = genbus[ii], id = r'1', string = 'PMAX')
    PMAX.append(PM)
    ert     = opf_apdsp_tbl(tbl = idx,intgar = [2,1,idx],realar = [PM,50,1])
    erg     = opf_gendsp_indv(genbus[ii],r"""1""",idx,1)
    print erg


# 4. Data for load
TargetBUS   = 29
idx         += 1
er1         = opf_csttbl_lin(idx,r"LOAD",2,[0.0,0.0, 4000.0, 4000])
er2         = opf_adjload_tbl(idx,[1,2,0],[1,9.5,.01, 1.0, 1.0, 1.0, 100])
er3         = opf_load_indv(TargetBUS,r"1",idx)


# 6. Add linear dependency. Here we simulate an approximate governor response
pm          = []
for ii in range(0,ngenbus):
    pm.append(1/PMAX[ii])

if GOV_MOD:    
    pd          = []
    BASEMVA     = sysmva()
    for ii in range(0,ngenbus - 1):
        lblname = 'gov' + str(ii + 1)
        Pdiff   = (Pgpre[ii]* pm[ii] - Pgpre[ngenbus - 1]* pm[ngenbus - 1])/BASEMVA
        pd.append(Pdiff)
        erl3    = opf_lnceqn_main(iqid = ii+1, labl = lblname, realar = [1.01 * Pdiff, 0.99 * Pdiff])
        erl1    = opf_lnceqn_pgen(iqid = ii+1, itbl = ii + 1, coeff = pm[ii])
        erl2    = opf_lnceqn_pgen(iqid = ii+1, itbl = ngenbus, coeff = -pm[ngenbus-1])


# ============================================================================================
#                                      OBJECTIVE FUNCTION
# ============================================================================================
vk = opf_use_generator_vsched(0) # Does not seem to take effect
minimize_reactive_reserve(0)
minimize_fuel_cost(1)
minimize_load_adjustments(1)
ierr = minimize_p_losses(0)
ierr = clamp_nonoptimized_gens(0) # Set to 0 to allows all generators to help
set_opf_report_subsystem(ALL_BUS,0)
# ============================================================================================
#                                           RUN OPF
# ============================================================================================
ierr = add_details_to_opf_log(1)
produce_opf_log_file(1, r'opf_output.txt')
nopf(GBUS,0) # Must run with GBUS ? DISPATCHGEN
 

# ============================================================================================
#                                       EXPORTING RESULTS
# ============================================================================================

ierr, Vm    = abusreal  (ALL_BUS, 1, 'PU')
ierr, Pg    = amachreal (ALL_BUS, 1, 'PGEN')
ierr, Qg    = amachreal (ALL_BUS, 1, 'QGEN')
ierr, Pl    = aloadcplx (ALL_BUS, 1, 'MVAACT')
ierr,lbus   = aloadint  (ALL_BUS, 1, 'NUMBER')

Vm          = Vm[0]
Pg          = Pg[0]
Qg          = Qg[0]
Pl          = Pl[0]
lbus        = lbus[0]


rwop(3,1,[1,1,1,1],0,r'opfdat.rop')

for lb in range(0,len(lbus)):
    ierr = load_chng_4(i = lbus[lb], id = r'1', realar1 = Pl[lb].real,realar2 = Pl[lb].imag)

rawd_2(sid = 3, all = 1, out = 0, ofile = 'opfres.raw')
# Note: Machine voltage set point are not correctly saved

close_powerflow()
