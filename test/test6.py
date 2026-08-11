
x = [1,2,3,4,5,6]
code =[[]]
for i in range(len(x)):
    if (x[i]<=2):
        print("x<=2")
        code[0].append("x<=2")
    elif x[i]<=1:
        print('x<=1')
        code[0].append("x<=1")
    elif x[i]<=3:
        print("x<3")
        code[0].append("x<=3")
    else:
        print('x<4,5,6')
        code[0].append("else")
print(code)