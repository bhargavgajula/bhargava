import numpy as np
row1,col1=list(map(int,input('Enter row and col').split()))
A=np.array(list(map(int,input('Enter matrix A').split())))
A.shape=(int(row1),int(col1))
print(A)
row2,col2=list(map(int,input('Enter row and col').split()))
B=np.array(list(map(int,input('Enter matrix B').split())))
B.shape=(int(row2),int(col2))
print(B)
if(row1==row2 and col1==col2):
    print("Addition=",np.add(A,B))
    print("Element by element multiplication",np.multiply(A,B))
else:
    print("Matrices addition and scalar multiplication are not possible")
if(col1==row2):
    print("Multiplication=",np.dot(A,B))
else:
    print("Multiplication is not possible")
