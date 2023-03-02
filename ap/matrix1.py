import numpy as np
row1,col1=list(map(int,input('enter row and col').split()))
A=np.array(list(map(int,input('enter matrix A:').split())))
A.shape=(int(row1),int(col1))
print(A)
row2,col2=list(map(int,imput("enter row and col").split()))
B=np.array(list(map(int,input("enetr matrix B:").split())))
B.shape=(int(row2),int(col2))
print(B)
if row1==row2 and col1==col2:
    print("adition:",np.add(A,B))
    print("multiplication by each element:",np.multiply(A,B))
elif col1==row2:
    print("only multiplication possible")
    print("multiplication :",n.dot(A,B))
else:
    print("multiplication and addition not pssible")
