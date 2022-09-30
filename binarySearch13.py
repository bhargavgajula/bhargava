def BinarySearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
l=[]
low=0
n=int(input("size:"))
for i in range(n):
    e=int(input("enter any number:"))
    l.append(e)
key=int(input("enter desired element:"))
result=BinarySearch(l,low,n-1,key)
if result==-1:
    print("element not found")
else:
    print("element found at:",result)
    


