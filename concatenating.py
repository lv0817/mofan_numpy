import pandas as pd 
import numpy as np 

# concatenating
#dataframe的合并
'''
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*3,columns=['a','b','c','d'])
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)
'''
# join ['inner','outer']
df5 = pd.DataFrame(np.ones((3,4))*1,index=[1,2,3],columns=['a','b','c','d'])
df6 = pd.DataFrame(np.ones((3,4))*2,index=[2,3,4],columns=['b','c','d','e'])
df7 = pd.DataFrame(np.ones((3,4))*3,index=[3,4,5],columns=['a','b','f','e'])
res = pd.concat([df5,df6,df7],axis=0,join='outer')
print(res )
'''
inner 找相同的部分，outer填充空的部分
join_axes=[df1.index]可以指定用哪一个的dataframe，这个frame所对应的index，才会显现，别的不匹配的index回丢掉
'''