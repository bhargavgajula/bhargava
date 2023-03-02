import pandas as pd
n=int(input("enter no of processes:"))
f={'at':[], 'bt':[], 'ct':[], 'tat':[], 'wt':[]}
for i in range(n):
    at=int(input("enter arrival time:"))
    bt=int(input("enter burst  time:"))
    f["at"].append(at)
    f["bt"].append(bt)
    ct = at + bt
    tat = bt - at
    wt = tat - bt

    f["tat"].append(tat)
    f["wt"].append(wt)
    f["ct"].append(ct)
df=pd.DataFrame(f)
print(df)
