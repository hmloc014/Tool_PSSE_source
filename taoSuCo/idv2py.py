from __future__ import with_statement
from __future__ import division
from contextlib import contextmanager
import os, sys
import pssepath
import psspy
import shutil
PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
from psspy import *
import redirect
from math import *
from csv import *
from dyntools import *
_i = getdefaultint()
_f = getdefaultreal()
_s = getdefaultchar()
psseinit(50000)
def get_nchan():
    N = 1000
    ierr, rval = psspy.chnval(N)
    while ierr == 2:
        N   -= 1
        ierr, rval = psspy.chnval(N)
    return N
psspy.dynamicsmode(1)
psspy.fnsl()
psspy.fnsl()
psspy.fnsl()
psspy.ordr(0)
psspy.fnsl()
psspy.conl(0,1,1,STATUS1=0)
psspy.conl(1,1,2,LOADIN1 = 100.0,LOADIN2 = 0.0,LOADIN3 = 0.0,LOADIN4=100.0)
psspy.conl(1,1,3)
psspy.cong(0)
psspy.ordr(0)
psspy.fact()
psspy.tysl(0)
psspy.save(r'D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\sme.sav')
psspy.fact()
psspy.dynamicsmode(0)
psspy.dyre_new([1,1,1,1],r'D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\2030.dyr',r'D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\CC1',r'D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\CT1',r'D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\CMP1' )
psspy.set_relang(1,0,'')
psspy.machine_array_channel([-1,1,917022],r"""1""",r"""ANGLE_LAICHAU_H2 """)
psspy.machine_array_channel([-1,1,917023],r"""1""",r"""ANGLE_LAICHAU_H3 """)
psspy.machine_array_channel([-1,1,917024],r"""1""",r"""ANGLE_LAICHAU_H4 """)
psspy.machine_array_channel([-1,1,917025],r"""1""",r"""ANGLE_LAICHAU_H4 """)
psspy.machine_array_channel([-1,1,917031],r"""1""",r"""ANGLE_HUOIQUANG_H""")
psspy.machine_array_channel([-1,7,917021],r"""1""",r"""SPEED_LAICHAU_H1 """)
psspy.machine_array_channel([-1,7,917022],r"""1""",r"""SPEED_LAICHAU_H2 """)
psspy.machine_array_channel([-1,7,917023],r"""1""",r"""SPEED_LAICHAU_H3 """)
psspy.machine_array_channel([-1,7,917024],r"""1""",r"""SPEED_LAICHAU_H4 """)
psspy.machine_array_channel([-1,7,917025],r"""1""",r"""SPEED_LAICHAU_H4 """)
psspy.machine_array_channel([-1,11,917023],r"""1""",r"""VREF_LAICHAU_H3 """)
psspy.machine_array_channel([-1,11,917024],r"""1""",r"""VREF_LAICHAU_H4 """)
psspy.machine_array_channel([-1,11,917025],r"""1""",r"""VREF_LAICHAU_H4 """)
psspy.machine_array_channel([-1,11,917031],r"""1""",r"""VREF_HUOIQUANG_H""")
psspy.strt(0,r"""D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\gop.out""")
psspy.report_output(4,"",[0,0])
psspy.close_report()
