import pssepath
PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
psspy.bsys(1,0,[0.0,0.0],0,[],6,[16010, 17010, 17012, 19010, 19011, 19030],0,[],0,[])
psspy.ascc(1,0,[1,0,0,0,1,2,0,1,0,0],"","")
