import pandas as pd 
import numpy as np 

# append 默认网下面加数据，index是数据索引，colounm是数据属性
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

res = df1.append([df2,df3],ignore_index=True)
#print(res)

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res2 = res.append(s1,ignore_index=True)

print(res2)