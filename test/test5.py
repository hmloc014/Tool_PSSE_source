import numpy as np 

arr = np.array([[[1, 2, 3,4],[4, 5, 6,7],[7, 8, 9,10]],[[11 ,22], [23, 24], [34, 23]] ]) #,
print("-------------arr",arr)
print("-------------len(arr[0])",len(arr[0]))
print("-------------arr[1]",arr[1])
print("-------------len arr[1]",len(arr[1]))
print("-------------len arr[1][0]",len(arr[1][0]))
print("------------- arr[0][0]",arr[1][0][:])
print("------------- arr[0][1]",arr[1][1][:])
# print("------------- arr[0][2]",arr[1][2][:])
# arr1 = np.array([arr[0][0][:],arr[0][1][:],arr[0][2][:]])
arr1=[]
for i in range(len(arr[1])):
    for j in range(len(arr[1][0])):
        arr1 =np.append(arr1,str(arr[1][i][j]))
print("-------------arr1",arr1)
arr1.resize(3,2)
print("-------------arr1",arr1)
print("-------------len arr1[0]",len(arr1))
print("-------------len arr1[0][0]",len(arr1[0]))
arr1 = arr1.transpose()
print("-------------len arr1[0]",len(arr1))
print("-------------len arr1[0][0]",len(arr[0]))