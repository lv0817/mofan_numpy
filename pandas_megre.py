import pandas as pd 
import numpy as np 

#merging two df by key/keys(maybe used in database)
#simple example 
'''
left  = pd.DataFrame({'key':['k0','k1','k2','k3'],
                        'A':['a0','a1','a2','a3'],
                        'B':['b0','b1','b2','b3']})
right = pd.DataFrame({'key':['k0','k1','k2','k3'],
                        'C':['c0','c1','c2','c3'],
                        'D':['d0','d1','d2','d3']})
print(left)
print(right)    
res = pd.merge(left,right,how='outer',on='key')#on代表以哪一个coloumns为基准 
print(res)    
'''
# 两个key的情况       
left  = pd.DataFrame({'key':['k0','k1','k2','k3'],
                        'A':['a0','a1','a2','a3'],
                        'B':['b0','b1','b2','b3'],
                        'key2':['k3','k1','k0','k2']})
right = pd.DataFrame({'key':['k0','k1','k2','k3'],
                        'C':['c0','c1','c2','c3'],
                        'D':['d0','d1','d2','d3'],
                        'key2':['k1','k1','k0','k1']})
print(left)
print(right)    
res = pd.merge(left,right,how='outer',on=['key','key2'],indicator=True)
#on代表以哪一个coloumns为基准 ,
# ndicator表示会吧数据如何组织的显示出来，both，还是只有左边有，只有右边有，这样子
print(res)    
