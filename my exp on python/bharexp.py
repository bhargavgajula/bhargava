s=input("Enter any word:")
l=len(s)//2 #Bhargava
l1=[]
cnt=0
if l%2==0:
    l*=3
    for i in range(1,l+1):
        if l%i!=0:
            cnt+=1
            if cnt==2:
                l1.append(i)

    print(max(l1))
elif l%2!=0:
    l*=2
    for i in range(1,l+1):
        if l%i!=0:
             cnt+=1
             if cnt==2:
                l1.append(i)
    print(max(l1))