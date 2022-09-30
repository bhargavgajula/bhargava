l=[]
n=int(input("size:"))
print("enter numbers:")
for i in range(n):
    ele=int(input())
    l.append(ele)
print("list before sorting:")
print(l)
print("list after sorting:")
for i in range(1,len(l)):
    j=i-1
    new=l[i]
    while l[j]>new and j>=0:
        l[j+1]=l[j]
        j-=1
        l[j+1]=new
print(l)                    


