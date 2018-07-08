import numpy as np

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print(arr1)

'''
array()常用4个属性
ndim  维度数量
shape 是一个表示各维度大小的元组,如上:(2,3)
dtype 一个用与说明数组元素数据类型的对象
size  元素总个数,即shape中个数相乘


'''

print("ndim:%s" % arr1.ndim)

print(arr1.shape)

arr2= np.array([1,2,3,4],dtype="|S")  #设置元素的数据类型
print(arr2)

arr3 = np.array(['nihao','hahaha','hello'],dtype="|S4")

print(arr3)


arr4 = np.array(['1','2','3'],dtype="int") #会把元素转化成整形,但是元素必须可转,否则报错,比如"aa"

print(arr4)

print("size:%s" % arr1.size)  #元素总数
