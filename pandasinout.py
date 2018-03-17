import pandas as pd #加载模块

#读取csv
data = pd.read_csv('student.csv')

#打印出data
print(data)

data.to_excel('student2.xls')