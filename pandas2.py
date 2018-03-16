import numpy as np 
import pandas as pd 

datas = pd.date_range('20130101',periods=6)
df1 = pd.DataFrame(np.arange(24).reshape(6,4),index=datas,columns=['a','b','c','d'])

'''
print(df1)
print(df1['a'],'\n',df1.a)
print(df1[0:3],df1['20130101':'20130103'])
#select by label
print(df1.loc['20130102'])
'''
df1.iloc[2,2]=123
df1.loc['20130102','C']=321

print(df1)
df1[df1.a>6]=0
df1['F']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20170101',periods=6))
print(df1)
 