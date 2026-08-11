from __future__ import with_statement
from __future__ import division
from contextlib import contextmanager
import os, sys
import pssepath
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
# File:"D:\Phong RD\1. Project\1.Du An Khac\17.On Dinh HTD xam nhap NLTT\39bus-16082021\SuCo.py", generated on MON, AUG 16 2021  10:22, release 33.04.00
psspy.strt(0,r"""D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\gop.out""")
psspy.run(0, 0.5,0,1,0)
psspy.dist_branch_fault(19010,17010,r"""1""",1, 220.0,[0.0,-0.2E+10])
psspy.change_channel_out_file(r"""D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\gop.out""")
psspy.run(0, 0.7,0,1,0)
psspy.dist_clear_fault(1)
psspy.dist_branch_trip(19010,17010,r"""1""")
psspy.change_channel_out_file(r"""D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\gop.out""")
psspy.run(0, 10.0,0,1,0)
nchan = get_nchan()
nchan += 1
chnobj = CHNF(r"""D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\gop.out""")
chnobj.txtout(channels = range(1,nchan),txtfile = r"""D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\SuCo1.txt""")
shutil.copy(r'D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\gop.out',r'D:\Hang\3. Programs\SourceCode\Tool-PSSE-2\taoSuCo\SuCo1.out')
