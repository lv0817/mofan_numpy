import numpy as np 
import pandas as pd 

datas = pd.date_range('20130101',periods=6)
df1 = pd.DataFrame(np.arange(24).reshape(6,4),index=datas,columns=['a','b','c','d'])


print(df1)
print(df1['a'],'\n',df1.a)
print(df1[0:3],df1['20130101':'20130103'])
#select by label
print(df1.loc['20130102'])