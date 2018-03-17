'''
同样的名字，但确有不同含义的coloumns该如何合并？
'''
import pandas as pd 

boys = pd.DataFrame({'k':['k0','k1','k2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['k0','k4','k2'],'age':[4,5,6]})

res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'])
print(res)