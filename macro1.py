import pssepath
PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
