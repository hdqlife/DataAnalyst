import numpy as np
import matplotlib.pyplot as plt

data=np.load(r'E:\DataAnalyst\数据分析表\国民经济核算季度数据.npz',allow_pickle=True)
# print(list(data))
columns=data['columns']
values=data['values']
# print(values)

plt.figure(figsize=(6,6))##figsize为方形
plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False

#绘制饼图
labels=['第一产业','第二产业','第三产业'] #饼图中的标签
explode=[0.01,0.01,0.01] #设定各项距离圆形的距离
plt.pie(values[-1,3:6],explode,labels=labels,autopct='%1.1f%%',colors=['r','b','y'])
#autopct:接受特定的string，置顶数值的显示方式
plt.show()




