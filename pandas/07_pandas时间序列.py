import numpy as np
import pandas as pd

# 创建一个dataframe对象,以字典的形式创建
data = pd.DataFrame({"A": ['one', 'one', 'two', 'three'] * 3,
                     "B": ["A", 'B', 'C'] * 4,
                     "C": ['foo', 'foo', 'bar', 'bar', 'bar', 'bar'] * 2,
                     "D": np.random.randn(12),
                     "E": np.random.randn(12)})  # randn函数返回一个或一组样本，具有标准正态分布

print(data)

'''
pandas提供了非常强大的时间序列处理函数
'''
# 创建一个时间序列,一共有600个
rng = pd.date_range("2018-07-01", periods=600, freq='s')
print(rng)

# 创建一个series数据,与时间序列相对应
#创建0到500范围内,个数为时间序列长度的的数据集,索引以时间序列为索引
data1 = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(data1)
#结果类似于股票的实时交易数据

#结果数据采样(求和的方式)
data2 = data1.resample('2Min').sum()
print(data2)
#结果数据采样(求平均值得方式)
data3 = data1.resample('2Min').mean()
print(data3)


#创建一个新的时间序列
rng1 = pd.date_range("2000Q1","2018Q2",freq="Q")
print(rng1)


#时间戳计算
a1 = pd.Timestamp("20180902")-pd.Timestamp("20160907")
print(a1)  #结果显示725天


#创建一个数据框,字典形式创建
data4 = pd.DataFrame({"id":[1,2,3,4,5,6],"raw_grade":['a','b','c','d','e','f',]})
print(data4)