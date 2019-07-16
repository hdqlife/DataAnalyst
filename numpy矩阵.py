import numpy as np


#-----------------------------1 矩阵创建与矩阵运算
##矩阵是ndarray的子类,矩阵继承了numpy数组对象的二维数组
#创建矩阵的方法
# matr1=np.mat('1 2 3;4 5 6')
# print(matr1)
# print(type(matr1))
matr2=np.matrix([[1,2,3],[4,5,6]])
# print(matr2)

#bmat拼接是，必须保证所拼接的数组行数相等
# arr1=np.eye(2)
# arr2=3*arr1
# print(np.bmat('arr1 arr2;arr2 arr1')) #行必须相等，列可以不一样


#矩阵运算
#矩阵加减法
# arr3=np.mat('1 2 3;2 3 4')
# arr4=np.mat('2 -2 3;3 3 5')
# print(arr3-arr4)
# print(arr3+arr4)

#矩阵乘法 a*b==>a的列数等于b的行数：a.shap[1]==b.shap[0]

# arr5=np.mat('1 2;1 1;0 0')
# print(arr4*arr5)

#对应元素相乘的方法：shape必须相等
# print(np.multiply(arr3, arr4))

#矩阵的转置：
# print(arr3)
# print(arr3.T)

#求逆
matr1=np.mat('1 0 0;0 2 0;0 0 3')
# print(matr1.I)

#共轭转置(实数的共轭转置就是本身)
# print(matr1.H)


#数组
#———————————————2 ufunc函数--------
#四则运算、比较运算、逻辑运算：
# x=np.array([1,2,3])
# y=np.array([-1,3,3])
# print(x-y)
# print(x+y)
# print(x*y)
# print(x/y)
# print(x**y)


#比较运算
x=np.array([1,2,3])
y=np.array([-1,3,3])
# print(x<y)
mask=x<y
# print(x[mask])

# print(x>y)
# print(x==y)
# print(x!=y)
# print(x>=y)
# print(x<=y)


#逻辑运算：逻辑与 、或
#np.all;np.any
# print(np.all(x == y))
# print(np.any(x == y))

#广播运算：仅限一个二维数组加一个一维数组(一行或者一列)
arr1=np.array([[1,2,3],[3,4,5],[3,4,5]])
# arr3=np.array([1,2,3])#(3,)
# arr2=np.array([[1],[2],[3]])#(3,)
# print(arr1)
# print(arr2)
# print(arr1+arr3)#一维里面的个数和二维列数一致
# print(arr1+arr2)#一维里面的个数和二维列数一致

##------ numpy文件读取：文本文件、二进制---------
#保存为二进制文件
#保存单一数组：save 返回.npy文件
arr=np.arange(100).reshape(10,10)
np.save('save_arr',arr)

# data=np.load('save_arr.npy') #读文件的时候一定要加后缀名称 .npy
# print(data)

#多个数组保存：savez 返回npz文件，存放多个.npy文件
arr2=np.arange(60).reshape(6,10)
np.savez('savez_arr',arr,arr2)
# data=np.load('savez_arr.npz')
# print(list(data))
# print(data['arr_0'])
# print(data['arr_1'])


#---文本文件的读取------------
# 文本文件的存储与读取：[.txt, .csv]
# #fmt：表示保存为整数
# #delimiter=',' 指定分隔符
np.savetxt('arr.txt',arr,fmt="%d",delimiter=',')
data=np.loadtxt('arr.txt',delimiter=',')
# print(data)

##六#统计分析
#1 排序 [sort/sorted]
arr3=np.random.randint(1,10,size=10)
# print(arr3)
arr3.sort()
# print(arr3)

arr4=np.random.randint(1,10,size=(3,6))
print(arr4)
# arr4.sort(axis=1)#横向排序
# print(arr4)
arr4.sort(axis=0)#纵向排序
print(arr4)

##argsort函数排序
arr5=np.random.randint(1,10,size=10)
# print(arr5)
# print(arr5.argsort())

#取arr5中最小的前5个值
index=arr5.argsort()[:5]
# print(arr5[index])

##去重
names=np.array(['小明','小花','小白','小明','小兰','小白','小白'])
# print(np.unique(names))

##重复：【对谁重复，重复多少次】
arr6=np.arange(5)
arr7=np.arange(12).reshape((3,4))

# print(np.tile(arr6, 4))
# print(np.tile(arr7, 2))

#对元素进行重复repeat
# print(arr7.repeat(2, axis=0))#按列进行重复
# print(arr7.repeat(2, axis=1))#按行进行重复

# #常用的统计函数
# #6 2 3 4 2 1 3
# #1求和sum
# print(arr7)
# print(np.sum(arr7))
# print(arr7.sum(axis=0))#纵向
# print(arr7.sum(axis=1))#横向

# #2求均值mean
# print(np.mean(arr7))
# print(arr7.mean(axis=0))
# print(arr7.mean(axis=1))
#
# # #3方差var
# print(np.var(arr7))
# print(arr7.var(axis=0))
# print(arr7.var(axis=1))
# #
# #4标准差std =sqrt(var)
# print(np.std(arr7))
# print(arr7.std(axis=0))
# print(arr7.std(axis=1))
#
# #5最小值min
# print(np.min(arr7))
# print(arr7.min(axis=0))
# print(arr7.min(axis=1))
#
# #6最大值max
# print(np.max(arr7))
# print(arr7)
# print(arr7.max(axis=0))
# print(arr7.max(axis=1))

#7最小索引argmin
# print(np.argmin(arr7))
# print(arr7.argmin(axis=0))
# print(arr7.argmin(axis=1))
# #
# #8最大值索引argmax
# print(arr7)
# print(np.argmax(arr7))
# print(arr7.argmax(axis=0))
# print(arr7.argmax(axis=1))

#9累计和 cumsum=[6 8 11 15 17 18 21]
# print(np.cumsum(arr7))
# print(arr7.cumsum(axis=0))
# print(arr7.cumsum(axis=1))
#10累计积
# print(np.cumprod(arr7))
# print(arr7.cumprod(axis=0))
# print(arr7.cumprod(axis=1))


# np.median #中位数     np.ptp :极差





















