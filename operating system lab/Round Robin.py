import pandas as pd
n=int(input("Enter no of processes"))
processes=[]
prio = {'priority': [],'bt': [],'ct': [],'tat': [],'wt':[]}
class Process:
    def _init_(self,priority,burst_time):
        self.burst_time = burst_time
        self.priority = priority
def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority)
    schedule= []
    current_time = 0
    for process in processes:
        prio['priority'].append(process.priority)
        prio['bt'].append(process.burst_time)
        current_time += process.burst_time
        tat=current_time
        wt=tat-process.burst_time
        schedule.append(current_time)
        prio['tat'].append(tat)
        prio['wt'].append(wt)
    return schedule
for i in  range (n):
    values=input("Enter Priority and burst time:").split()
    values = list(map(int,values[0:]))
    processes.append(Process((values[0]),(values[1])))
s=priority_scheduling(processes)
for i in range(n):
    prio['ct'].append(s[i])
df=pd.DataFrame(prio)
print(df)