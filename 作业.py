import numpy as np
import matplotlib.pyplot as plt

p1=plt.figure(figsize=(10,10))
plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False


datas=np.load(r'E:\DataAnalyst\数据分析表\populations.npz',allow_pickle=True)
print(list(datas))

data=datas['data']
feature_names=datas['feature_names']
# print(data)



p1.add_subplot(2,2,1)
labels=['城镇人口','乡村人口']
explode=[0.01,0.01]
plt.pie(data[0,4:6],explode=explode,labels=labels,autopct='%1.1f%%',colors=['r','b'])
plt.title("城乡人口变化图")


p1.add_subplot(2,2,2)
labels=['男','女']
explode=[0.01,0.01]
plt.pie(data[1,3:5],explode=explode,labels=labels,autopct='%1.1f%%',colors=['r','b'])
plt.title("男女人口变化图")


p1.add_subplot(3,2,3)
x=np.linspace(0,20,20)
y=data[-3::-1,1]
plt.plot(x,y,marker="*",)
plt.title('总人口变化图')
plt.xlabel('年份')
plt.ylabel('人口')
plt.xticks(x,data[-3::-1,0],rotation=45)
plt.show()



















