import numpy as np   

# dt = np.dtype('<S16')

# a = np.array([str('20010'),str('VINHYEN5 '), str('500.0'), str('20'), str(''), str('15'), str(''), 
#                 str('1'), str(''), str('1'),str('0.986015856266'), str('-4.60054969788'),
#                 str('1.10000002384'), str('0.899999976158'),str('1.10000002384'), str('0.899999976158')],dtype=dt)


# matrix = np.array([['16010', 'LAOCAI5     ', '500.0', u'20', u'', u'15', u'', u'1', u'', u'1',
#         u'0.986015856266', u'-4.60054969788', u'1.10000002384', '0.899999976158','1.10000002384', '0.899999976158'],
#        ['17010', 'LAICHAU5    ', '500.0', u'20', u'', u'15', u'', u'1', u'', u'1',
#         u'0.986015856266', u'-4.60054969788', u'1.10000002384', '0.899999976158','1.10000002384', '0.899999976158']],dtype=dt)
# print("***********  matrix before append is   ******************:,len: {b},{c}".format(b=len(matrix),c=len(matrix[0])))
# print("a: {a}, len(a): {b},dtype a: {c} ".format(a=a,b = len(a),c=a.dtype))
# print("matrix is:, type: {b}".format(b=matrix.dtype))
# matrix = np.append(matrix,a)
# matrix.resize(3,16)
# print("^^^^^^^^^^^^^^^^^^^^^^^^^  matrix after append is   ^^^^^^^^^^^^^^^^^^^^^^^:{a} ,len: {b},{c}".format(a=matrix,b=len(matrix),c=len(matrix[0])))
# fileInfo = [[[u'2021-HCM.sav', u'2021-m-max-6.sav', u'2021-m-max-6-70.sav']], [[-825.2012939453125, -1623.736328125, -1639.436767578125]], [[250.69317626953125, 838.2892456054688, 845.7734375]], [[0.024914266952973507, 0.85673238852157, 0.3783821683217601]], [[1712.0952795371413, 2461.7838904485106, 2444.426896966994]]]
# fileInfo1 = [fileInfo[0][0],fileInfo[1][0],fileInfo[2][0],fileInfo[3][0],fileInfo[4][0]]
# fileInfoArray = np.array(fileInfo1)
# fileInfoTranspose = fileInfoArray.transpose()
# print("--------fileInfo",len(fileInfo))
# print("--------fileInfoTrans",len(fileInfoTranspose))
# print("--------fileInfoTrans",len(fileInfoTranspose[0]))
# print("--------fileInfoArray",fileInfoArray)
# print("--------fileInfoTranspose",fileInfoTranspose)
# lista = [1,2,3,4,5]
# suma = 0
# for i in range(len(lista)):
#         suma = suma+(lista[i])
# print(suma)
# from decimal import *
# TWOPLACE = Decimal(10)**-2
# index = 1
# listb = [[1,2,3,4,5]]
# for i in range(3):
#         listb[0][index] = str(Decimal(12.01556).quantize(TWOPLACE))
# print(listb)
# import commands
# print commands.getstatusoutput('echo "test" | wc')
# import sys
# import os

# print ('line 1 to stdout  ')
# sys.stdout.write('line 2 to stdout  ') ; 
# sys.stdout.flush()
# os.write(1, b'line 3 to stdout  ')

# a = [[1,2,3,5],[4,5,6,8],[7,8,9,10]]
# print("--------- array a:",a)
# b = [[6,2,7,8],[1,2,6,3],[17,18,19,410]]
# print("--------- array b before assign value by a:",b)
# b = a
# print("--------- array b after assign value by a:",b)

# name = ['', 'LAICHAU5    ', 'TDLAICHAU5  ', 'DGCAMAU1    ',
#  'LONGMY_WP   ', 'MONSOON_W   ']
# print("name 1:",len(name))
# print("name 1:",len(name[0]))
# print('is lao in name:',('LAO') in name)
# for i in range(len(name)):
#         if 'LAO' in name[i]:
#                 print("true")
#         else:
#                 print('false')
# # print(result)
# if not '' in name:
#         print('ho la')
# else:
#         print('hello')
# print("'' in name:",'' in name)

# c = [[1,2,3,5],[4,5,6,8],[7,8,9,10]]
# c = (np.array(c).transpose())

# print("---------len array a:",len(a))
# d =  [[6,2,7,8],[1,2,6,3],[17,18,19,410]]
# d = (np.array(d).transpose())

# print(c.tolist()+d.tolist())
# e = np.append([d[0]],c)
# print(e)

arr1 = [1,2,3,4,5]
arr2 = [11,12,13,14,15]
arr2[2]=0
print(arr2)
arr3 = ['A','B','C']
ls = [arr1,arr2,arr3]
m = []
for i in range(len(ls)):
        for j in range(len(ls[i])):
                a = str(ls[i][j])
                m.append(a)
print(m)
print(ls)