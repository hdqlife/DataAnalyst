import numpy as np
import matplotlib.pyplot as plt

# data=np.load(r'E:\DataAnalyst\国民经济核算季度数据.npz',allow_pickle=True)
# # print(list(data))
# columns=data['columns']
# values=data['values']
# # print(values)
#
# plt.figure(figsize=(10,8))##figsize为方形
plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False
#
# y=values[-1,6:]
# print(y.size)
# # x=np.arange(1,17,2)
# x=np.linspace(1,17,9) #[起始，终值，个数] a9=a1+(n-1)d
#
# #柱状图
# plt.bar(x,y,color=['r','g','c','y','k','m','b','pink','peru'],width=1.2)
#
# labels=columns[6:]
# list_lables=[]
# for i in labels:
#     a=i.split('增加值')[0]
#     list_lables.append(a)
# # print(list_lables)
# plt.xticks(x,list_lables,rotation=45)
# plt.show()

#e二直方图
salary = [2500, 3300, 2700, 5600, 6700, 5400, 3100, 3500, 7600, 7800,8700, 9800, 10400]

group = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]##分组区间

plt.hist(salary,group) #group为分组区间
plt.show()

#正态分布
x=np.random.randn(10000)
# print(x)
plt.hist(x,20)
# plt.title('正态分布随机数')
# plt.show()


#均匀分布
x=np.random.rand(10000)
plt.hist(x,20) #一共分了20组
plt.title('均匀分布随机数')
plt.show()









