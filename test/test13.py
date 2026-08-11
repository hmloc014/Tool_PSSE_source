import numpy as np
step = 10
n = int(100/step) 
print(n)

buCanFromBus = []
buLechFromBus1 = {}
buLechToBus1 = {}
buCanToBus = {}
buLechFromBus2 = {}
buLechToBus2 = {}

busList = [1,2,3,4,5,6,7,8,9]

for i in range(n+1):
    val = []
    val2 = []
    val3 = []
    val4 = []
    val5 = []
    val6 = []
    for bus in busList:
        val.append(bus*i)
        val2.append(bus*2*i)
        val3.append(bus*3*i)
        val4.append(bus*4*i)
        val5.append(bus*5*i)
        val6.append(bus*6*i)
    buCanFromBus.append(val) 
    buLechFromBus1['{}'.format(i*step)] = val2
    buLechToBus1['{}'.format(i*step)] = val3
    buCanToBus['{}'.format(i*step)] = val4
    buLechFromBus2['{}'.format(i*step)] = val5
    buLechToBus2['{}'.format(i*step)] = val6
# print('BUS'.ljust(5,' ')+'0%'.ljust(10,' ')+'10%'.ljust(10,' ')+'20%'.ljust(10,' ')+'30%'.ljust(10,' ')+'40%'.ljust(10,' ')+'50%'.ljust(10,' ')+'60%'.ljust(10,' ') +'\n')
# a = []
# for i in range(len(busList)):
# for item in buCanFromBus.items():
#     a.append(item[1])
# a = np.array(buCanFromBus)
# print(buCanFromBus)
# print(len(buCanFromBus[0]))
# b = a.transpose()
# print(a)
label = 'BUS'.ljust(5,' ')
for i in range(n+1):
    label = label + '{}%'.format(i*step).ljust(10,' ')
print(label)

for i in range(len(busList)):
    
    s = ''
    for j in range(n+1):
        s = s + str(buCanFromBus[j][i]).ljust(10,' ')
    print(str(busList[i]).ljust(5,' ')+s)

# print(buCanFromBus)
# print(buLechFromBus1)
# print(buLechToBus1)
# print(buCanToBus)
# print(buLechFromBus2)
# print(buLechToBus2)
genAreaName =[[]]
genArea = [[1,2,3,5,8,9,12]]
areaName = [['a','b','c','d','e','f','g','h','i','j']]
areaNumber = [[1,2,3,4,5,6,7,8,9,10]]
for i in range(7): # genArea
    for j in range(10):
        if (int(genArea[0][i])==int(areaNumber[0][j])):
            genAreaName[0].append(areaName[0][j])
    if not int(genArea[0][i]) in areaNumber[0]:
        genAreaName[0].append(' ')

print(genAreaName)