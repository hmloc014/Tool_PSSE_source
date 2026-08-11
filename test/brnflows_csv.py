#[brnflows_csv.py]  04/08/2009    Export BRANCH FLOWS to COMMA SEPARATED FILE (CSV)
# ====================================================================================================
'''
This is an example file showing how to use "subsystem data retrieval APIs
from Python to save branch flows to Comma Separated File.
    Input : Solved PSS(R)E saved case file name
    Output: CSV file name to save
    When 'savfile' is provided, FNSL with default options is used to solve the case.
    When 'savfile' is not provided, it uses solved Case from PSS(R)E memory.
    When 'csvfile' is provided, branch flows is saved in ASCII text file 'csvfile'.
    When 'csvfile' is not provided, it produces report in PSS(R)E report window.

The subsystem data retrieval APIs return values as List of Lists. For example:
When "abusint" API is called with "istrings" as defined below:
    istrings = ['number','type','area','zone','owner','dummy']
    ierr, idata = psspy.abusint(sid, flag_bus, istrings)
The returned list will have format:
    idata=[[list of 'number'],[list of 'type'],[],[],[],[list of 'dummy']]

This example is written such that, such returned lists are converted into dictionary with
keys as strings specified in "istrings". This makes it easier to refer and use these lists.
    ibuses = array2dict(istrings, idata)
    
So ibuses['number'] gives the bus numbers returned by "abusint".

---------------------------------------------------------------------------------
How to use this file?

(1) Inside PSS(R)E
Run this file as "Automation File" within PSS(R)E.

(2) Outside PSS(R)E (with any Python Shell)
Create a Python script as below to:
    - Update Python's import search path (sys.path)
    - Update Window's search path os.environ['PATH'] and 
    - Provide required inputs

import sys, os
sys.path.insert(0,r"C:\Program Files\PTI\PSSExx\PSSBIN") # xx --> substitute xx with Version Number here.
os.environ['PATH'] = r"C:\Program Files\PTI\PSSExx\PSSBIN" + ";" + os.environ['PATH']
import redirect
redirect.psse2py()  # this redirects PSS(R)E progress, report output to Python Shell/Console
import psspy, brnflows_csv
psspy.psseinit(buses)
psspy.case(savfile)
psspy.fnsl()        # solve the case if required
brnflows_csv.brnflowscsv(savfile,csvfile)

'''
# ----------------------------------------------------------------------------------------------------
import os
PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy

# ----------------------------------------------------------------------------------------------------
def array2dict(dict_keys, dict_values):
    '''Convert array to dictionary of arrays.
    Returns dictionary as {dict_keys:dict_values}
    '''
    tmpdict = {}
    for i in range(len(dict_keys)):
        tmpdict[dict_keys[i].lower()] = dict_values[i]
    return tmpdict

# ----------------------------------------------------------------------------------------------------
def busindexes(busnum, busnumlist):
    '''Find indexes of a bus in list of buses.
    Returns list with indexes of 'busnum' in 'busnumlist'.
    '''
    busidxes = []
    startidx = 0
    buscounts = busnumlist.count(busnum)
    if buscounts:
        for i in range(buscounts):
            tmpidx = busnumlist.index(busnum,startidx)
            busidxes.append(tmpidx)
            startidx = tmpidx+1
    return busidxes

# ----------------------------------------------------------------------------------------------------
def splitstring_commaspace(tmpstr):
    '''Split string first at comma and then by space. Example:
    Input  tmpstr = a1       a2,  ,a4 a5 ,,,a8,a9
    Output strlst = ['a1', 'a2', ' ', 'a4', 'a5', ' ', ' ', 'a8', 'a9']
    '''
    strlst = []
    commalst = tmpstr.split(',')
    for each in commalst:
        eachlst = each.split()
        if eachlst:
            strlst.extend(eachlst)
        else:
            strlst.extend(' ')

    return strlst

# ----------------------------------------------------------------------------------------------------
def brnflowscsv(savfile,csvfile):
    '''Generates power flow result report.
    When 'savfile' is provided, FNSL with default options is used to solve the case.
    When 'savfile' is not provided, it uses solved Case from PSS(R)E memory.
    When 'csvfile' is provided, report is saved in ASCII text file 'csvfile'.
    When 'csvfile' is not provided, it produces report in PSS(R)E report window.
    '''

    # Set Save and CSV files according to input file names
    if savfile:
        ierr = psspy.case(savfile)
        if ierr != 0: return
        fpath, fext = os.path.splitext(savfile)
        if not fext: savfile = fpath + '.sav'
    else:   # saved case file not provided, check if working case is in memory
        ierr, nbuses = psspy.abuscount(-1,2)
        if ierr != 0:
            print '\n No working case in memory.'
            print ' Either provide a Saved case file name or open Saved case in PSS(R)E.'
            return
        savfile, snapfile = psspy.sfiles()

    if csvfile:  # open CSV file to write
        csvfile_h = open(csvfile,'w')
        report    = csvfile_h.write
    else:        # send results to PSS(R)E report window
        psspy.beginreport()
        report = psspy.report

    # ================================================================================================
    # PART 1: Get the required results data
    # ================================================================================================

    # Select what to report
    if psspy.bsysisdef(0):
        sid = 0
    else:   # Select subsytem with all buses
        sid = -1    

    flag_brflow  = 1    # in-service
    owner_brflow = 1    # use bus ownership, ignored if sid is -ve
    ties_brflow  = 5    # ignored if sid is -ve

    # ------------------------------------------------------------------------------------------------
    # Branch Flow Data
    # Branch Flow Data - Integer
    istrings = ['fromnumber','tonumber','status','nmeternumber','owners','own1','own2','own3','own4']
    ierr, idata = psspy.aflowint(sid, owner_brflow, ties_brflow, flag_brflow, istrings)
    if ierr != 0: return
    iflow = array2dict(istrings, idata)
    # Branch Flow Data - Real
    rstrings = ['amps','pucur','pctrate','pctratea','pctrateb','pctratec','pctmvarate', 
                'pctmvaratea','pctmvarateb',#'pctmvaratec','fract1','fract2','fract3', 
                'fract4','rate','ratea','rateb','ratec', 
                'p','q','mva','ploss','qloss', 
                'o_p','o_q','o_mva','o_ploss','o_qloss'
                ]
    ierr, rdata = psspy.aflowreal(sid, owner_brflow, ties_brflow, flag_brflow, rstrings)
    if ierr != 0: return
    rflow = array2dict(rstrings, rdata)
    # Branch Flow Data - Complex
    xstrings = ['pq','pqloss','o_pq','o_pqloss']
    ierr, xdata = psspy.aflowcplx(sid, owner_brflow, ties_brflow, flag_brflow, xstrings)
    if ierr != 0: return
    xflow = array2dict(xstrings, xdata)
    # Branch Flow Data - Character
    cstrings = ['id','fromname','fromexname','toname','toexname','nmetername','nmeterexname']
    ierr, cdata = psspy.aflowchar(sid, owner_brflow, ties_brflow, flag_brflow, cstrings)
    if ierr != 0: return
    cflow = array2dict(cstrings, cdata)

    # ================================================================================================
    # PART 2: Write acquired results to Report file
    # ================================================================================================

    report("Branch flows from Saved case: %s\n" %savfile)
    
    clnttls = "%6s,%18s,%6s,%18s,%3s,%3s,%9s,%9s,%9s,%6s,%8s,%8s\n" %('FRMBUS',
             'FROMBUSEXNAME','TOBUS','TOBUSEXNAME','CKT','STS','MW','MVAR','MVA','%I','MWLOSS','MVARLOSS')
    report(clnttls)
    for i in range(len(iflow['fromnumber'])):
        fromnum    = iflow['fromnumber'][i]
        fromexname = cflow['fromexname'][i]
        tonum      = iflow['tonumber'][i]
        toexname   = cflow['toexname'][i]
        ckt        = cflow['id'][i]
        status     = iflow['status'][i]
        p          = rflow['p'][i]
        q          = rflow['q'][i]
        mva        = rflow['mva'][i]
        ploss      = rflow['ploss'][i]
        qloss      = rflow['qloss'][i]       
        pcti       = rflow['pctrate'][i]
        report("%(fromnum)6d,%(fromexname)18s,%(tonum)6d,%(toexname)18s,%(ckt)3s,%(status)3d,\
%(p)9.2F,%(q)9.2F,%(mva)9.2F,%(pcti)6.2F,%(ploss)8.2F,%(qloss)8.2F\n" %vars())
    # ------------------------------------------------------------------------------------------------
    if csvfile:
        csvfile_h.close()
        print '\n Done .... Power Flow Results Report saved to file %s' % csvfile
    else:
        print '\n Done .... Power Flow Results Report created in Report window.'

# ====================================================================================================
# ====================================================================================================
# if __name__ == '__main__':
def branchflow():
    savfile = None; csvfile = None

    psspy.prompt("PROVIDE SAVED CASE and CSV FILE NAMES:\n\
        - TYPE file names (type comma to use default name) or\n\
        - ENTER to use all default files\n")
    psspy.prompt("    DEFAULTS:\n\
        - Files: PSS(R)E case from memory and PSS(R)E report window\n\
        - Extensions: 'sav' and 'csv'\n")
    psspy.prompt("    TYPE file names separated either by comma or space.")
    
    ierr, fnamestr = psspy.userin()

    if fnamestr:
        fnamelst = splitstring_commaspace(fnamestr)
        try:
            savfile = fnamelst[0]
            csvfile = fnamelst[1]
        except:
            pass
        if savfile == ' ': savfile = None
        if csvfile == ' ': csvfile = None
        if csvfile:    
            fpath, fext = os.path.splitext(csvfile)
            if not fext: csvfile = fpath + '.csv'

    brnflowscsv(savfile,csvfile)
    
# ====================================================================================================
