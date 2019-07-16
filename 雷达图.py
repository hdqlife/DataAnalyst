import numpy as np
import matplotlib.pyplot as plt

#两维以上使用雷达图
plt.figure()
plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False

dataLength=5 #把整个圆切成5份
angles=np.linspace(0,2*np.pi,dataLength,endpoint=False)
labels=['生存','输出','团战','KDA','发育',]
data=[2,3.5,4,4.5,5]
#闭合
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
plt.polar(angles,data,color='r',marker='o')
plt.xticks(angles,labels)
plt.title('王振荣耀战绩')
plt.show()








