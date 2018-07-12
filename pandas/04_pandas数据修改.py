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

#只修改一个数据
data2.iat[0,0] = 100
print(data2)

#修改一列
data2.A = 200
print(data2)

data2.A = range(6)  #这里列表长度需要匹配,如果不匹配,会报错
print(data2)


