names={}
n=int(input())
for i in range(n):
    names[i+1]=input("enter names")
name=list(names.values())
pos = int(input())
name.sort(key = lambda x : x[pos])
print(name)