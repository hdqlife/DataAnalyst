# #numpy是数据科学计算的基础模块，可用来存储和处理大型矩阵
# # （1）numpy创建多维数组、通用函数的方法；
# # （2）数组的索引与变换；
# #（3）numpy矩阵的创建、通用函数的方法；
# #（4）numpy读写文件；
#
#
# #+++++++++++1.numpy数组的创建与属性方法
#
import numpy as np
#
# #创建一维数组
#
arr1=np.array([1,2,3,4])
# print(arr1)
# print(type(arr1)) #<class 'numpy.ndarray'>
#
# #创建二维数组
arr2=np.array([[1,0,1,1],[2,1,1,1],[0,2,1,1]])
# print(arr2)

#
# #数组结构
# print("数组结构",arr2.shape) #数组结构 (3, 4)
#
#
# #数组元素类型
# print("数组元素类型",arr2.dtype) #数组元素类型 int32
#
# #数组元素个数
# print("数组元素个数",arr1.size)
# print("数组元素个数",arr2.size) #数组元素个数 6
#
# #数组的维度
# print("数组维度",arr1.ndim) #数组维度 1
# print("数组维度",arr2.ndim) #数组维度 2
#
# #重设数组的结构
arr2.shape=2,6 #2*6=size
# print("重设结构后的数组arr2\n",arr2)
#++++++++++++++++++++++++++++++++++++++++++++++++++
# #利用numpy函数创建数组：
# #1.arange[起始，终值[不包括]，步长]
# print(np.arange(10))
# print(np.arange(0,1,0.1))
# print(np.arange(0,10))
# 2等差数列[起始，结束(包括)，多少个数]
# print(np.linspace(0,9,10)) #等差数列公式，an=a1+(n-1)*d;d=(an-a1)/(n-1)

# 3等比数列：
# print(np.logspace(0, 2, 20)) #以10为底，在10^0-10^2之间  第一个起始值10^0  第二个终值10^2（包括）  第三个数取20个数
#
# 4创建全零数组 参数 为元组
# print(np.zeros((2, 3)))
#
# 5全一数组 参数为元组
# print(np.ones((4, 3)))

#6单位矩阵(方正)
# print(np.eye(3))

#7对角矩阵
# print(np.diag([1, 2, 3]))

##==================================
#生成随机数random
#1生成随机数组
# print(np.random.random(10))

#2生成服从均匀分布的函数
# print(np.random.rand(2, 5))#传结构

#3.正态分布
# print(np.random.randn(10, 5)) #传结构

#4随机整数2<=x<10
# print(np.random.randint(2, 10, size=(3, 5)))

#5索引访问数组
#一维数组索引
arr=np.arange(10)
# print(arr)
# print(arr[:5])
# print(arr[5:])
# print(arr[::2])
# print(arr[::-1])

#二维数组索引：
arr2=np.array([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11]])
print(arr2)
#第一种方法：切片：逗号前面行，后面列 arr2[行切片，列切片]
# print(arr2[:2, 0])
# print(arr2[:2,2:4])
# print(arr2[1:3, 1:4:2])
# print(arr2[0:3:2, 1:4:2])

#第二种方法：arr2[(行),(列)] 逗号后面是元组
# print(arr2[(0, 2), (1, 4)])
print(arr2[(0,1, 2), (1,2,3)])

#第三种:布尔值切片，条件取值
mask=np.array([1,0,1],dtype=np.bool)
mask2=np.array([0,0,1,0,0],dtype=np.bool)

#mask为1：true(取值) 为0：false（不取这一行或一列的值）
#不要用bool值同时去取行和列
# print(arr2[mask,2])#mask表示行取值，一定和数组的行个数一致
# print(arr2[1,mask2])#mask表示列取值，一定和数组的列个数一致


##变换数组形态
#（1）重设数组形态
arr3=np.arange(12)
# print(arr3)
arr4=arr3.reshape((3, 4))
# print(arr4)
##（2）展平数组
# print(arr4.ravel())#横向展平[ 0  1  2  3  4  5  6  7  8  9 10 11]
# print(arr4.ravel("F"))#纵向展平[ 0  4  8  1  5  9  2  6 10  3  7 11]

#(3)flatten
# print(arr4.flatten())#默认为“C”表示横向展平[ 0  1  2  3  4  5  6  7  8  9 10 11]
# print(arr4.flatten("F"))#纵向展平[ 0  4  8  1  5  9  2  6 10  3  7 11]

#（4）组合方式
arr5=np.array([[1,2],[3,4],[5,6]])
arr6=np.array([[11,12],[13,14],[15,16]])
# print(np.hstack((arr5, arr6)))#横向组合
# print(np.vstack((arr5, arr6)))#纵向组合

# arr6=np.vstack((arr5, arr6))
# #5数组分割
# print(np.hsplit(arr6, 2)) #横向分割
# print(np.vsplit(arr6, 3))#纵向分割
# #axis=1表示横向，axis=0表示纵向
# print(np.split(arr6, 2, axis=1))



