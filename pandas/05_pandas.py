import numpy as np
import pandas as pd

# 创建一个日期序列
data1 = pd.date_range('20180310', periods=6)
print(data1)

''''
数据选择的文件中的方法,基本上都能完成对数据的修改
'''

# 创建一个dateframe
# 日期是行的标签,abcd是列的标签
data2 = pd.DataFrame(np.random.rand(6, 4), index=data1, columns=list("ABCD"))
print(data2)

# 添加一列,以NaN补全
a1 = data2.reindex(index=data1[0:4], columns=list(data2.columns) + ['E'])
print(a1)

# 赋值
data2.loc[data1[1:3], "E"] = 2
print(data2)

# 丢弃空数据
data3 = data2.dropna()
print(data3)

# 替换空数据
data4 = data2.fillna(value=5)
print(data4)

# 判断数据集中是否有空数据,空数据的地方时true
data5 = pd.isnull(data2)
print(data5)

# 判断数据集中是否有空数据,空数据的地方时true,筛选是否有true
data6 = pd.isnull(data2).any().any()
print(data6)

# 空数据是不参与计算的
# 比如,取每一列的平均值
data7 = data2.mean()
print(data7)

# 按照行取平均值
data8 = data2.mean(axis=1)
print(data8)

# 累加
data9 = pd.DataFrame(np.random.rand(6, 4), index=data1, columns=list("ABCD"))
print(data9)

data10 = data9.apply(np.cumsum)
print(data10)

# 创建一个随机序列
data11 = pd.Series(np.random.randint(10, 20, size=20)) #size 表示这个创建的新序列总共20个数
print(data11)

# 查看这个序列中随机数出现的次数
data12 = data11.value_counts()
print(data12)
# 新创建序列中产生次数最多的随机数,可并列最多
data13 = data11.mode()
print(data13)




