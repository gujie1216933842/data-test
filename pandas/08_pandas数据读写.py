import pandas as pd
import numpy as np

# 创建一个100行4列的数据
#randn(100, 4)  表示100行4列
data = pd.DataFrame(np.random.randn(100, 4), columns=list("ABCD"))
print(data)
#把生成的dataframe数据框数据保存在本地磁盘
#data.to_csv('data.csv')

#读取本地磁盘中的数据,pandas可以支持很多种数据

data1 = pd.read_csv('data.csv',index_col=0)
print(data1)


