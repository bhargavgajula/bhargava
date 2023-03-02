n ="02468"
e=""
o=""
for i in range(1,int(input())+1):
    if str(i)[-1] in n:e=e+str(i)+" "
    else:o=o+str(i)+" "
print(e,"is even","\n",o,"is odd")
    