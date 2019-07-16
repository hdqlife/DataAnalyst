import numpy as np
import matplotlib.pyplot as plt

#创建画布
p1=plt.figure(figsize=(8,6))

#添加子图
# p1.add_subplot(2,1,1)  #两行一列第一个图
x=np.arange(10)
# y=-x+2
# plt.plot(x,y)
# p1.add_subplot(2,3,5) #两行三列第五个图（行，列，第几个图）
y1=x**2-2*x
# plt.plot(x,y1)
# plt.show()
#
# ##散点图
p1.add_subplot(2,1,2)
y2=x**2-2*x
plt.scatter(x,y1,marker="d",color='yellow')
plt.show()

#==============================国民经济核算================================
data=np.load(r'E:\DataAnalyst\数据分析表\国民经济核算季度数据.npz',allow_pickle=True)

plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False

# print(list(data))
columns=data['columns']
values=data['values']
print(values)

##绘制2000年到2017年第一季度国民生产总值散点图
#字符串不能直接画图
x=values[::4,0]
y=values[::4,2]
plt.figure(figsize=(10,8))
plt.scatter(x,y,marker="d")

x=values[1::4,0]
y=values[1::4,2]
plt.scatter(x,y,marker="d")

x=values[2::4,0]
y=values[2::4,2]
plt.scatter(x,y,marker="d")

x=values[3::4,0]
y=values[3::4,2]
plt.scatter(x,y,marker="d")

plt.title('2000年到2017年各季度国民生产总值散点图')
plt.legend(['第一季度','第二季度','第三季度','第四季度'])
plt.xlabel('季度')
plt.ylabel('生产总值')

# plt.xticks(values[0::4,0],values[0::4,1],rotation='45')
plt.xticks(values[0::4,0],np.arange(2000,2018,1),rotation='45') #把刻度替换为我们需要显示的值


plt.show()



