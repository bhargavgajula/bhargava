x,y=map(int,input().split())
s=0
for i in range(1,(x or y)):
  if (x or y)%i==0:
    s+=i
if s>(x or y):
  print(True)
else:
  print(False)
  