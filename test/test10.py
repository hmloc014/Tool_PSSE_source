ID3Wind = [['1 ', '4 ', '2 ', '1 ', '2 ']]
name3Wind = [['AT1_NQ', 'ABCD', 'NHOQUAN5', 'NHOQUAN2', 'NHOQUAN2']]
ID3WindByWind = [['4 ', '1 ', '2 ', '2 ', '1 ', '4 ', '1 ', '2 ', '1 ', '2 ', '4 ', '1 ', '2 ', '2 ', '1 ']]
name3WindByWind = [['ABCD','AT1_NQ','NHOQUAN5','NHOQUAN2','NHOQUAN2','ABCD','AT1_NQ','NHOQUAN2','NHOQUAN2','NHOQUAN5','ABCD','AT1_NQ','NHOQUAN5','NHOQUAN2','NHOQUAN2']]

index1 = []
index2 = []
index3 = []
print(float(ID3Wind[0]))
n = len(ID3Wind[0])
for i in range(n):
    for j in range(n):
        if ID3WindByWind[0][i] == ID3Wind[0][j] and name3WindByWind[0][i] == name3Wind[0][j]:
            index1.append(j)
for i in range(n):
    for j in range(n):
        if ID3WindByWind[0][i+n] == ID3Wind[0][j] and name3WindByWind[0][i+n] == name3Wind[0][j]:
            print("i+n and ID3WindByWind[0][i+n]:",i+n,ID3WindByWind[0][i+n])
            print("j is:",j)
            index2.append(j+n)
for i in range(n):
    for j in range(n):
        if ID3WindByWind[0][i+2*n] == ID3Wind[0][j] and name3WindByWind[0][i+2*n] == name3Wind[0][j]:
            index3.append(j+2*n)
print("index1",index1)
print("index2",index2)
print("index3",index3)
index = index1+index2+index3
print("index",index)
name3WindByWindNew = [[]]
ID3WindByWindNew = [[]]
indexFinal = []
for i in range(len(ID3WindByWind[0])):
    
    ID3WindByWindNew[0].append(ID3WindByWind[0][index[i]])
    name3WindByWindNew[0].append(name3WindByWind[0][index[i]])
    # for j in range(len(index)):
    #     indexFinal.append(index[j]+i*n)

print("__________________ID3WindByWindNew_______________",ID3WindByWindNew)
print("__________________indexFinal_______________",indexFinal)
print("__________________name3WindByWindNew_______________",name3WindByWindNew)