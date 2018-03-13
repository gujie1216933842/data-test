# numpy最大的作用是创建数组
import numpy

a = numpy.array([0, 0, 0])
print(a)

b = numpy.array([[1, 4, 3], [1, 7, 5]])  # 注:array()数组内的每个元素内部个数要相等
print(b)

c = b[1][1]
print(c)

# 排序
b.sort()
print(b)

# 最大值和最小值  数组比python原生列表的运算效率要高很多(和c语言同级)
b_max = b.max()
b_min = b.min()
print(b_max)
print(b_min)

# 切片操作
# 指取数组中的一段元素   数组[起始下标:最终下标+1]  如果省略不写,表示一直到开头或结尾
b_qiepian = b[0:1]
print(b_qiepian)

# 导入pandas模块
import pandas as pda

'''
pandas中两种类型数据
Series:   表格中的一行或是一列  对应的是一维数组
DataFrame:数据框(类似表格)  对应的是二维数组
'''
d = pda.Series([2, 9, 4])
print(d)  # index索引也会打印出来
# 要指定缩影
d_index = pda.Series([2, 9, 4], index=[3, 4, 4])
print(d_index)

# 数据框类型数据创建
e = pda.DataFrame([[1, 3, 4], [3, 2, 5], [6, 4, 8]])
print(e)

# 指定数据框的列名
e_column = pda.DataFrame([[1, 3, 4], [3, 2, 5], [6, 4, 8]], columns=["one", "two", "three"])
print(e_column)

# 以字典形式创建数据框 , 字典中的key 值数据框中的列名
e_dict = pda.DataFrame({
    "one": 4,
    "two": [2, 5, 3],
    "three": [5, 7, 5]
})
print(e_dict)


#调用数据框的头部数据(默认显示的是前五行)
e_head = e_dict.head(2)
print(e_head)

#取数据框的尾部数据
e_tail = e_dict.tail(1)
print(e_tail)

#统计数据框的行数
# count:元素格式   mean:平均数   std:标准差  min/max:这一列中的最小/大值   25% : 对应的代表每一列的分位数(前,中,后)
e_desc = e_dict.describe()
print(e_desc)


#转置  (把行变成列,列变成行)
e_t = e_dict.T
print(e_t)
