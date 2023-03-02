l=[]
n=int(input("enter size:"))
for i in range(n):
    x=input("enter elements")
    l.append(x)
for ele in l:
    y=l.count(ele)
    print(y)