import numpy as np
#1.Attributes of arrays
np.random.seed(0)#设置随机种子数组的属性
x1 = np.random.randint(10,size = 6)#一维数组
x2 = np.random.randint(10,size = (3,4))#3*4的二维数组
x3 = np.random.randint(10,size = (3,4,5))#3*4*5的三维数组
#可以用scientific mode 可视化查看数组
print("x3 ndim: ", x3.ndim)#维数
print("x3 shape:", x3.shape)#（层数，行数，列数）
print("x3 size: ", x3.size)#元素数
print("dtype:", x3.dtype)#data type
print("itemsize:", x3.itemsize, "bytes")#元素大小，32未编译器上int为4字节
print("nbytes:", x3.nbytes, "bytes")#多维数组的总大小

#2.下标访问
x1[-1]
x1[-2]#允许从尾部开始数
x2[0, -2]#一个中括号，用逗号分隔

x1[0] = 3.14159#自动转换
x1==3

#3.切片
x = np.arange(10)
x[start:stop:step]#与python列表一样的切片
x[5::-2]#负的步长，倒序取值
x2[:2, :3]  # 多维数组切片，two rows, three columns,注意左闭右开
print(x2[:, 0])#单取一列
print(x2[0, :])  # 单取一行，相当于x2[0]

x2_sub = x2[1:2,0:]#numpy子数组是地址的直接复制,修改子数组元素会导致原数组元素改变

