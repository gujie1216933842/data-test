import numpy as np
import pandas as pd

# 创建一个日期序列
data1 = pd.date_range('20180310', periods=6)
print(data1)

# 创建一个dateframe
# 日期是行的标签,abcd是列的标签
data2 = pd.DataFrame(np.random.rand(6, 4), index=data1, columns=list("ABCD"))
print(data2)

# 行属性
a1 = data2.index
print(a1)

# 列属性
a2 = data2.columns
print(a2)

a3 = data2.values
print(a3)

# 排序
a4 = data2.sort_index(axis=1)  # 列正序

print(a4)

a5 = data2.sort_index(axis=1, ascending=False)  # 列标签倒序
print(a5)

a6 = data2.sort_index(axis=0)  # 行标签正序
print(a6)
a7 = data2.sort_index(axis=0, ascending=False)  # 行标签倒序
print(a7)

a8 = data2.sort_values(by="A")  # 通过A这一列的值进行排序,正序
print(a8)





