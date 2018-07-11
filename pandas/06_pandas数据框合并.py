import numpy as np
import pandas as pd

# 创建一个数据框
data = pd.DataFrame(np.random.randn(10, 4), columns=list("ABCD"))
print(data)

# 把数据框分割成几个部分
data1 = data.iloc[:3]
print(data1)

data2 = data.iloc[3:7]
print(data2)

data3 = data.iloc[7:]
print(data3)

# 把拆分的数据合并
# concat()方法中参数是一个序列
data4 = pd.concat([data.iloc[:3], data.iloc[3:7], data.iloc[7:]])
print(data4)

# data和data4 比较是否一致
print(data == data4)

# data和data4 比较是否一致,优化
print((data == data4).all().all())

# 合并数据集的另一种方式
left = pd.DataFrame({"key": ['foo', 'foo'], 'lavl': [1, 2]})
right = pd.DataFrame({"key": ['foo', 'foo'], 'lavl': [4, 5]})

print(left)
print(right)

# 把left 和right当成sql中的两张表

data5 = pd.merge(left, right, on="key")
# 等价于 select *  from left inner join right on left.key = right.key
print(data5)
'''
   key  lavl_x  lavl_y
0  foo       1       4
1  foo       1       5
2  foo       2       4
3  foo       2       5
'''

# 数据集插入数据序列

data6 = pd.DataFrame(np.random.randn(10, 4), columns=list("ABCD"))
data7 = pd.Series(np.random.randint(1, 5, size=4), index=list("ABCD"))
print(data7)

data8 = data6.append(data7, ignore_index=True)
print(data8)

# 数据集分组累加
# 先创建一个
data8 = pd.DataFrame({"A": ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
                      "B": ['one', 'two', 'three', 'two', 'one', 'three', 'one', 'two'],
                      "C": np.random.randn(8),
                      "D": np.random.randn(8)})
print(data8)

data9 = data8.groupby("A").sum()
print(data9)

#通过多个分组
data10 = data8.groupby(["A","B"]).sum()
print(data10)
