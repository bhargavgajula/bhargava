def check(m):
    a="aketopn"
    l=set(a)
    l=list(a)
    for i in range(len(l)):
        k=0
        n=l[i].lower()
        n=set(n)
        n=list(n)
        for j in range(0,len(n)):
            if n[j] in l:
                k+=1
        if k==len(l):
            print(l[i])
m=['Arun','Varun','Ant','Peak','Peacock','kent','Pot','Zebra','Nato','Toe','Knife','Poke','Venus','Poet']


