import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
'''
# plot data
plt.figure(num=1)
#Series线性数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()#对数据累加求和
data.plot()
#plt.plot(x,y....)因为data就是一组数据，所以直接plot就可以
plt.show()
'''
plt.figure(num=2)
# dataframe
data2 = pd.DataFrame(np.random.randn(1000,4),
                        index=np.arange(1000),
                        columns=list('ABCD'))

data2 = data2.cumsum()
data2.plot()
print(data2.head(3))
plt.show()
