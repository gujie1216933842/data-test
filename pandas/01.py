import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(arr1.shape)

print(arr1.dtype)
print("*****************************")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print("*****************************")

arr3 = np.arange(10)
print(arr3)

arr4 = np.arange(5, 10)  # [5 6 7 8 9]
print(arr4)

print("*****************************")
arr5 = arr3.reshape(2, 5)
print(arr5)  # 注意这里reshape里的数据是引用,而不是拷贝,即如果对arr5数组做元素修改,那么arr3数组的值也会跟着变化
print("*****************************")

arr6 = np.zeros((2, 3))  # 注:zeros参数是元组
print(arr6)

print("*****************************")

arr7 = np.ones((2, 3, 4))
print(arr7)
print("*****************************")
# 穿件一个对角数组
arr8 = np.eye(4)
print(arr8)
print("*****************************")

# 把数组转化成我们需要的维度数组

arr9 = np.arange(16).reshape(4, 4)
print(arr9)
# 二维数组索引
print(arr9[1:3])

print(arr9[1:3, 3:4])  # 行是1:3,列是3:4
print(arr9[:, 3:4])  # 行不做筛选,列是3:4
print(arr9[[1,3],[3,3]])  #二维数组的另一种方式切片
print(arr9 > 5)
print(arr9[arr9>5])  #选true的一维数组

print("*****************************")
arr10 = np.arange(100, step=10)
# 切片
print(arr10[1:4])
print(arr10[:4])
