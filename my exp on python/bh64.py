l=[-1,-2,-3,4,5,4]
m=[6,7,8,9,3,8]
k=[]
s1=0
s2=0
for i in range(1,len(l)+1):
    x=l[-i]*(10**(i-1))
    s1=s1+x
print(s1)
for j in range(1,len(m)+1):
    y=m[-j]*(10**(j-1))
    s2=s2+y
print(s2)
s3=s1+s2
c=list(str(s3))
p=[]
for h in c:
    z=int(h)
    p.append(z)
print(p)