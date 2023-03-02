import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('path')
x=data.iloc[0:10,0]
y=data.iloc[0:10,1]
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.bar(x,y,colour=Orange)
plt.subplot(2,2,3)
plt.scatter(x,y)
plt.subplot(2,2,2)
plt.pie(y,labels=x)
plt.show()
