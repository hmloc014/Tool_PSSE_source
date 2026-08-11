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
_i = getdefaultint()
_f = getdefaultreal()
_s = getdefaultchar()
redirect.psse2py()
psseinit(8000)
casedir    = os.path.join(r'')
rawfile    = os.path.join(casedir,'new_england.raw')

pfoption = [0, # tap adjustment, 0 = disable, 1 = step, 2 = direct
            0, # area interchange, 0 = disable
            0, # phase shift adjustment
            1, # DC tap adjustment
            1, # Switched shunt, 0 = disable, 1 = enable
            1, # flat start, 1 = enable
            0, # var limit, 0 = immediately
            0] # non divergent solution

# ====================================================================================================
#                                           MAIN PROGRAM
# ====================================================================================================

# CONSTANTS FOR RCAP
RCAP_INHIBIT_INCREASE   = 2
RCAP_QGEN_LIM           = 5
RCAP_FIXED_EFD          = 4
#

# Read raw file
read(0,rawfile)

# 1. Define a subsystem
buses = range(1,40)

# Generator buses that participate to help increase Q reserve
genbus      = [30,31,32,33,34,35,36,37,38,39]

# Targeted generator that is shed
target_gen  = [38]

# Optioin to model governor
GOV_MOD     = 1

bus2        = genbus
ALL_BUS     = 3

bsys(sid = ALL_BUS, numbus = len(buses), buses = buses)
bsys(sid = 2,       numbus = len(bus2), buses = bus2)


# ========================================================================
#                          POWER FLOW
# ========================================================================
ier = fnsl(pfoption)
ierr, Pgpre = amachreal(3, 1, 'PGEN')
Pgpre       = Pgpre[0]
# Get load bus
ierr,lbus   = aloadint(3, 1, 'NUMBER')
lbus        = lbus[0]
print lbus

# ========================================================================
#                          OPF PARAMETERS
# ========================================================================
# Set up data for OPF
newopf()
# 1. Voltage limit for the subsystem
opf_bus_subsys(      sid = 3,
                     all = 0, # only specified buses
                     intgar1 = 1,
                     intgar2 = 0,
                     realar1 = 1.1,
                     realar2 = 0.9)
opf_fix_all_generators(0)
# 2. Data for fuel prices for generators. All generators have same price.
ngenbus = len(genbus)
idx = 0
PMAX    = []
for ii in range(0,ngenbus):
    idx     += 1
    er      = opf_csttbl_lin(idx,r"gen_dispatch 1",2,[30.0,00.0, 2900.0, 1.1])
    er, PM  = macdat(ibus = genbus[ii], id = r'1', string = 'PMAX')
    PMAX.append(PM)
    er      = opf_apdsp_tbl(tbl = idx,intgar = [2,1,idx],realar = [PM,50,1])
    erg     = opf_gendsp_indv(genbus[ii],r"""1""",idx,1)
    

# 3.Adding reactive capability curve data for generator.
for bus in genbus: 
    opf_gen_rcap_indv(bus,r"1",RCAP_QGEN_LIM,[1.8,1, 0.9, 0.9, 0.2])

# 4. Data for load. Load can only reduce, not increase
bsys(sid = 4, numbus = len(lbus), buses = lbus)
ierr, Pl    = aloadcplx(4, 1, 'MVAACT')
Plinit      = Pl[0]
kk          = 0
for TargetBUS in lbus:
    idx     += 1
    er2     = opf_adjload_tbl(idx,[2,_i,0],[1,1,0.1, 1.0, 1.0, 1.0, 100])
    er3     = opf_load_indv(TargetBUS,r"1",idx)
    kk      += 1

# 5. Disable one machine, which is the targeted generator
ierr = machine_data_2(target_gen[0], r'1', intgar1 = 0)

# 6. Objective - the objective chosen here is minimize the reactive reserve and (with minimal) load adjustment.
opf_use_generator_vsched(1) # Does not seem to take effect
minimize_reactive_reserve(1)
reactive_resv_cost_coeff(-0.4)
minimize_fuel_cost(1)
minimize_p_losses(0)
minimize_load_adjustments(1)
ierr = clamp_nonoptimized_gens(1) # Set to 0 to allows all generators to help

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

# ========================================================================
#                                SOLVE OPF
# ========================================================================
produce_opf_log_file(1, r'opf_output.txt')
set_opf_report_subsystem(3,0)
ierr = add_details_to_opf_log(1)
nopf(3,0)

ierr, Vm    = abusreal(3, 1, 'PU')
ierr, Pg    = amachreal(3, 1, 'PGEN')
ierr, Qg    = amachreal(3, 1, 'QGEN')

ierr, Pl    = aloadcplx(4, 1, 'MVAACT')


Vm          = Vm[0]
Pg          = Pg[0]
Qg          = Qg[0]
Pl          = Pl[0]

Vg  = []
for b in bus2:
    Vg.append(Vm[b-1])
rwop(3,1,[1,1,1,1],0,r'opfdat.rop')

for lb in range(0,len(lbus)):
    ierr = load_chng_4(i = lbus[lb], id = r'1', realar1 = Pl[lb].real,realar2 = Pl[lb].imag)
rawd_2(sid = ALL_BUS, all = 1, out = 0, ofile = 'opfres.raw')
#stop_2()

