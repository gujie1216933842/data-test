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
Series:   表格中的一行或是一列
DataFrame:数据框(类似表格)
'''
d = pda.Series([2, 9, 4])
print(d)  # index索引也会打印出来
# 要指定缩影
d_index = pda.Series([2, 9, 4],index=[3,4,4] )
print(d_index)
