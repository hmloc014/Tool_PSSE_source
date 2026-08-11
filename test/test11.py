# from DialogBox import getInput, openFile, openFolder, saveFile
import numpy as np

idv2 = r"D:\Hang\3. Programs\temp\dynamic\dyn_22.idv"
# print(idv2)
f = open(idv2, 'r')
lines = f.readlines()
angleArr = []
angleNameArr = []
# print('line10',lines[10])
e = ''
for line in lines:
    if 'ANGLE_' in line:
        # print('This is busnum for angle of source observe!')
        items = line.split(',')
        angleArr.append(items[0])
        angleNameArr.append(items[2])

for i in range(5,8):
    e = e+'\n'+lines[i]
    print('line ',i,lines[i])

print('----------------{}'.format(e))

# print(angleNameArr)
for i in range(len(angleNameArr)):
    a = angleNameArr[i][:-1]
    # print(a)

a = [1,2,3,4,5,6,7]
b = 4
c = min(a,key=lambda x:abs(x-b))
indexc = a.index(c)
print(c,indexc)


dyrFile = r"D:\Hang\4. hang.nt3\6. Tai lieu\Tinh Khang bu\Ngan mach phan bo\2030-PA1-K-MAX-11-pv-chitiet.txt"
dyrFileNew = r"D:\Hang\3. Programs\temp\dynamic\2030_new.dyr"
f = open(dyrFile,'r')
lines = f.readlines()
dyrArr = []
newarr = []
index = []
onePhase = []
angle = []
name = []
voltage = []
threePhase = []
right = []
rightBus = []
for line,val in enumerate(lines):
    params = val.split()
    if 'AT BUS' in val:
        newarr.append(params[2])
        name.append(params[3])
        voltage.append(params[4])

    if 'AMP/OHM' in val:
        right.append(params[11])
        rightBus.append(params[0])

    if 'TOTAL  FAULT  CURRENT' in val:
        
        onePhase.append(params[6])
        threePhase.append(params[4])


# print(leftBus)
# print(left)
# print(rightBus)
# print(right)
resume = ('BUS'.ljust(15,' ')+'BUS NAME '.ljust(30,' ')+'THREE PHASE'.ljust(15,' ')+'ONE PHASE'+'\n')
s1 = s2 = s3 = s4 = s5 = ''

for i in range(len(newarr)):
    # s = str(onePhase[i])
    if i == 0:
        s1 = s1+str(newarr[i]).ljust(9,' ')
        s2 = s2+str(rightBus[2*i+1]).ljust(9,' ')
        s3 = s3+str(right[2*i+1]).ljust(9,' ')
        s4 = s4+str(rightBus[2*i]).ljust(9,' ')
        s5 = s5+str(right[2*i]).ljust(9,' ')
    else:
        s1 = s1+str(newarr[i]).ljust(9,' ')
        s2 = s2+str(rightBus[2*i]).ljust(9,' ')
        s3 = s3+str(right[2*i]).ljust(9,' ')
        s4 = s4+str(rightBus[2*i+1]).ljust(9,' ')
        s5 = s5+str(right[2*i+1]).ljust(9,' ')
    # print(str(newarr[i]).ljust(15,' ')+str(name[i]).ljust(14,' ')+str(voltage[i]).ljust(17,' ')+str(threePhase[i]).ljust(7,' ')+str(onePhase[i]).rjust(15,' ') +'\n')
    # s=str(newarr[i]).ljust(15,' ')+str(name[i]).ljust(14,' ')+str(voltage[i]).ljust(25-n,' ')+str(threePhase[i])+str(onePhase[i]+'\n').rjust(15,' ') 
    # print(str(newarr[i]).ljust(5,' ')+' :'.ljust(5,' ')+ str(rightBus[2*i]).ljust(15,' ')+str(right[2*i]).ljust(15,' ')+ str(rightBus[2*i+1]).ljust(15,' ')+str(right[2*i+1]))
    # print(str(rightBus[2*i]).ljust(15,' ')+str(right[2*i]))
    # print(str(rightBus[2*i+1]).ljust(15,' ')+str(right[2*i+1]))

#     resume = resume+s
print('#'*160+'\n')
print('#' +' '*70+'RESUME'+' '*70+'\n')
print('#'*160+'\n')
print('BUS:     '+s1+'\n'+'FR BUS:  '+s2+'\n'+'I(AMPS): '+s3+'\n'+'TO BUS:  '+s4+'\n'+'I(AMPS): '+s5+'\n')# print('-'*160)

busNum = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
a = []
for i in range(1,100):
    if not str(i) in busNum and len(a)<10:
        a.append(i)
print(a)

ls = ['NaN']*10
ls[2] = 1
ls[4] =9
print(ls)
a = np.array([[1,2,3,4,5,6,7],['a','b','c','d','e','f','g'],[10,11,12,12,32,43,54]])
print(a)
print(a[0])
print(a[1])
print('abc    '.strip())
#     # for i in range(len(params)):
#         dyrArr.append(params)
#         index.append(params[0])
# print(dyrArr[10])
# indexArr = sorted(range(len(index)), key=lambda k: index[k])
# n = open(dyrFileNew,'w')
# for i in range(len(indexArr)):
#     line = dyrArr[indexArr[i]]
#     newarr.append(dyrArr[indexArr[i]][:])
#     for j in range(len(line)):
#         # newarr.append(line[j]+)
#         n.writelines(line[j]+' ')
#     n.writelines('\n')
# n.close()
# f.close()
# avrArr = [str(1),"'{}'".format("acd")]
# avrArr.append("bcd")
# print(avrArr)
# genArr = [11,21,243,54,665,32,32]
# f = open(dyrFileNew,'a')
# for i1 in range(len(avrArr)):
#     f.writelines(str(avrArr[i1])+'	')
# f.writelines('\n')
# for i2 in range(len(genArr)):
#     f.writelines(str(genArr[i2])+'	')
# f.writelines('\n')
# f.close()

# a = [10,11,12,'busID','busID']
# for i,val in enumerate(a):
#     if val == 'busID':
#         a[i]= '123456'

# print(a)
# modelTypes = ['GENROU','GENSAL','ESST1A','ESST4B','EXAC4','TGOV1','HYGOV','GAST','PSS2A','PVGU1','PVEU1','PANELU1','IRRADU1','GEWTGCU1','GEWTECU1','GEWT2MU1','GEWTPTU1','GEWTARU1','GEWTGDU1']
        
# print(modelTypes[:2])
# print(modelTypes[2:5])
# print(modelTypes[5:8])
# print(modelTypes[8])
# print(modelTypes[9:13])
# print(modelTypes[13:])

# modelType = 'IRRADU1'

# choice = []
# if modelType in modelTypes[:2]:
#     choice = modelTypes[:2]
# elif modelType in modelTypes[2:5]:
#     choice = modelTypes[2:5]
# elif modelType in modelTypes[5:7]:
#     choice = modelTypes[5:8]
# elif modelType == modelTypes[8]:
#     choice = modelTypes[8:9]
# elif modelType in modelTypes[9:]:
#     choice = ["'{}'".format(modelType)]
            
# a = ['','','','']
# if all(x is '' for x in a):
#     print( 'list is empty')
