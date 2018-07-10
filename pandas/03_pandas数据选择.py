import numpy as np
import pandas as pd

# 创建一个日期序列
data1 = pd.date_range('20180310', periods=6)
print(data1)

# 创建一个dateframe
# 日期是行的标签,abcd是列的标签
data2 = pd.DataFrame(np.random.rand(6, 4), index=data1, columns=list("ABCD"))
print(data2)

# 数据选择(以列方式一)
a1 = data2.A
print(a1)

# 数据选择(以列方式二)
a2 = data2['A']
print(a2)

# 数据选择行
a3 = data2.loc['2018-03-10':'2018-03-13']  # 通过data2[2:4] 这种方式也可行,单数效率偏低
print(a3)

# 只选择b列和c列区间内的数据
a4 = data2.loc[:, ["B", "C"]]
print(a4)
# 只选择b列和c列区间内的数据,行标签范围 "2018-03-12","2018-03-15"
a5 = data2.loc["2018-03-12":"2018-03-15", ["B", "C"]]
print(a5)

# 访问到特定的值,和坐标类似
a6 = data2.loc["2018-03-12", "B"]
print(a6)

# 与上以条作用一样,都是访问特定的值,但是访问效率要比上一条要高
# 注意:这里使用的参数不能输格式化日期字符串,需要是原生时间戳
a7 = data2.at[pd.Timestamp("2018-03-12"), 'B']
print(a7)

# iloc函数
# 选择第一列
a8 = data2.iloc[1]
print(a8)
# 选择几行
a9 = data2.iloc[1:3]
print(a9)

# 选择几行几列
a10 = data2.iloc[1:3, 1:2]
print(a10)

#访问特定的元素
a11 = data2.iloc[1,3]
print(a11)

#访问特定的元素,作用与上一条类似,但是效率更高
a12 = data2.iat[1,3]
print(a12)
