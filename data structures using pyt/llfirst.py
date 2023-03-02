#convert to octal from int
print(0o23456)
a=input("enter octal num:")
l=len(a)
res=0
k=1
for i in a:
    res=res+ int(i)*8**(l-k)
    k+=1
print(res)