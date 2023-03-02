a=list(map(int,input().split()))
b=list(set(a))
for i in b:
    if a.count(i)!=1:
        print(f"{i}-{a.count(i)}")
    