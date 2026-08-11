import pssepath
PSSE_LOCATION = r'C:\Program Files\PTI\PSSE33\PSSBIN'
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION
pssepath.add_pssepath(33)
import psspy 
psspy.bus_chng_3(21012,[1,15,21,1],[500.0,1.05,-0.32,1.1,0.9,1.1,0.9],'abc')
psspy.flat_2([0,0,0,0,0,0,0,0],[0.0,0.0])
psspy.fdns()
psspy.fnsl()
psspy.fnsl()
psspy.bus_chng_3(29010,[1,15,29,1],[500.0,1.02,-0.45,1.1,0.9,1.1,0.9],'PHONOI5     ')
psspy.bus_chng_3(29010,[4,15,29,1],[500.0,1.02,-0.45,1.1,0.9,1.1,0.9],'PHONOI5     ')
psspy.bus_number(34020,34011)
