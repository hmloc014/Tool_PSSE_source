dyrFile = r"D:\Hang\3. Programs\temp\dynamic\dyn_22new.idv"
f = open(dyrFile,'r')
lines = f.readlines()

flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = flag7 = flag8 = flag9 = 0
flag10 = flag11 = flag12 = flag13 = flag14 = flag15 = flag16 = flag17 = flag18 =0
flag19 = flag20 = flag21 = flag22 = flag23 = flag24 = flag25 = flag26 = flag27 = 0
flag28 = flag29 = flag30 = flag31 = flag32 = flag33 = flag34 = flag35 = flag36 = flag37 =0

arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []
arr9 = []
arr10 = []
arr11 = []
arr12 = []
arr13 = []

arr14 = []
arr15 = []
arr16 = []
arr17 = []
arr18 = []
arr19 = []
arr20 = []
arr21 = []

arr22 = []
arr23 = []
arr24 = []
arr25 = []
arr26 = []
arr27 = []
arr28 = []
arr29 = []

arr30 = []
arr31 = []
arr32 = []
arr33 = []
arr34 = []
arr35 = []
arr36 = []
arr37 = []

for i,line in enumerate(lines):

    if line == '1\n':
        flag1 = 1
    if flag1 ==1 and len(line.split(','))>1:
        arr1.append(line.split(',')[0])

    if line == '2\n' :
        flag2 = 1
    if flag2 ==1 and len(line.split(','))>1 :
        arr2.append(line.split(',')[0])

    if line == '3\n':
        flag3 = 1
    if flag3 ==1 and len(line.split(','))>1  :
        arr3.append(line.split(',')[0])

    if line == '4\n':
        flag4 = 1
    if flag4 ==1 and len(line.split(','))>1:
        arr4.append(line.split(',')[0])

    if line == '5\n':
        flag5 = 1
    if flag5 ==1 and len(line.split(','))>1  :
        arr5.append(line.split(',')[0])

    if line == '6\n':
        flag6 = 1
    if flag6 ==1 and len(line.split(','))>1 :
        arr6.append(line.split(',')[0])

    if line == '7\n' and lines[i-1]!= 'dlst\n':
        flag7 = 1
    if flag7 ==1 and len(line.split(','))>1 :
        arr7.append(line.split(',')[0])

    if line == '8\n':
        flag8 = 1
    if flag8 ==1 and len(line.split(','))>1 :
        arr8.append(line.split(',')[0])

    if line == '9\n':
        flag9 = 1
    if flag9 ==1 and len(line.split(','))>1 :
        arr9.append(line.split(',')[0])

    if line == '10\n':
        flag10 = 1
    if flag10 ==1 and len(line.split(','))>1 :
        arr10.append(line.split(',')[0])

    if line == '11\n':
        flag11 = 1
    if flag11 ==1 and len(line.split(','))>1 :
        arr11.append(line.split(',')[0])

    if line == '12\n':
        flag12 = 1
    if flag12 ==1 and len(line.split(','))>1 :
        arr12.append(line.split(',')[0])

    if line == '13\n':
        flag13 = 1
    if flag13 ==1 and len(line.split(','))>1 :
        arr13.append(line.split(',')[0])

    if line == '14\n':
        flag14 = 1
    if flag14 ==1 and len(line.split(','))>1 :
        arr14.append(line.split(',')[0])

    if line == '15\n':
        flag15 = 1
    if flag15 ==1 and len(line.split(','))>1 :
        arr15.append(line.split(',')[0])

    if line == '16\n':
        flag16 = 1
    if flag16 ==1 and len(line.split(','))>1 :
        arr16.append(line.split(',')[0])

    if line == '17\n':
        flag17 = 1
    if flag17 ==1 and len(line.split(','))>1 :
        arr17.append(line.split(',')[0])

    if line == '18\n':
        flag18 = 1
    if flag18 ==1 and len(line.split(','))>1 :
        arr18.append(line.split(',')[0])

    if line == '19\n':
        flag19 = 1
    if flag19 ==1 and len(line.split(','))>1 :
        arr19.append(line.split(',')[0])

    if line == '20\n':
        flag20 = 1
    if flag20 ==1 and len(line.split(','))>1 :
        arr20.append(line.split(',')[0])

    if line == '21\n':
        flag21 = 1
    if flag21 ==1 and len(line.split(','))>1 :
        arr21.append(line.split(',')[0])

    if line == '22\n':
        flag22 = 1
    if flag22 ==1 and len(line.split(','))>1 :
        arr22.append(line.split(',')[0])

    if line == '23\n':
        flag23 = 1
    if flag23 ==1 and len(line.split(','))>1  :
        arr23.append(line.split(',')[0])

    if line == '24\n':
        flag24 = 1
    if flag24 ==1 and len(line.split(','))>1 :
        arr24.append(line.split(',')[0])

    if line == '25\n':
        flag25 = 1
    if flag25 ==1 and len(line.split(','))>1 :
        arr25.append(line.split(',')[0])

    if line == '26\n':
        flag26 = 1
    if flag26 ==1 and len(line.split(','))>1 :
        arr26.append(line.split(',')[0])

    if line == '27\n':
        flag27 = 1
    if flag27 ==1 and len(line.split(','))>1 :
        arr27.append(line.split(',')[0])

    if line == '28\n':
        flag28 = 1
    if flag28 ==1 and len(line.split(','))>1 :
        arr28.append(line.split(',')[0])

    if line == '29\n':
        flag29 = 1
    if flag29 ==1 and len(line.split(','))>1 :
        arr29.append(line.split(',')[0])

    if line == '30\n':
        flag30 = 1
    if flag30 ==1 and len(line.split(','))>1 :
        arr30.append(line.split(',')[0])

    if line == '31\n':
        flag31 = 1
    if flag31 ==1 and len(line.split(','))>1  :
        arr31.append(line.split(',')[0])

    if line == '32\n':
        flag32 = 1
    if flag32 ==1 and len(line.split(','))>1  :
        arr32.append(line.split(',')[0])

    if line == '33\n':
        flag33 = 1
    if flag33 ==1 and len(line.split(','))>1 :
        arr33.append(line.split(',')[0])

    if line == '34\n':
        flag34 = 1
    if flag34 ==1 and len(line.split(','))>1 :
        arr34.append(line.split(',')[0])

    if line == '35\n':
        flag35 = 1
    if flag35 ==1 and len(line.split(','))>1 :
        arr35.append(line.split(',')[0])

    if line == '36\n':
        flag36 = 1
    if flag36 ==1 and len(line.split(','))>1 :
        arr36.append(line.split(',')[0])

    if line == '37\n':
        flag37 = 1
    if flag37 ==1 and len(line.split(','))>1 :
        arr37.append(line.split(',')[0])

    if line == '\n':
        flag1 = flag2 = flag3 = flag4 = flag5 = flag6 = flag7 = flag8 = flag9 = 0
        flag10 = flag11 = flag12 = flag13 = flag14 = flag15 = flag16 = flag17 = flag18 =0
        flag19 = flag20 = flag21 = flag22 = flag23 = flag24 = flag25 = flag26 = flag27 = 0
        flag28 = flag29 = flag30 = flag31 = flag32 = flag33 = flag34 = flag35 = flag36 = flag37 =0

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print(arr10)
print(arr11)
print(arr12)
print(arr13)
print(arr14)
print(arr15)
print(arr16)
print(arr17)
print(arr18)
print(arr19)
print(arr20)
print(arr21)
print(arr22)
print(arr23)
print(arr24)
print(arr25)
print(arr26)
print(arr27)
print(arr28)
print(arr29)
print(arr30)
print(arr31)
print(arr32)
print(arr33)
print(arr34)
print(arr35)
print(arr36)
print(arr37)