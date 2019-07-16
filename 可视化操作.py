##matplotlib

import numpy as np
import matplotlib.pyplot as plt

##1创建一个空白画布
plt.figure()


#修改参数
plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False #解决保存图像“-”显示为方块的问题

#2.绘制什么图？
x=np.arange(10)
y=2*x+1
# print(y)

#3.折线图:plot x,y的size必须一致
plt.plot(x,y,color='r',linewidth=3,marker='*',markersize='20',linestyle=':',markerFaceColor='hotpink',
         markeredgeColor='hotpink' ) #设置样式
#markFaceColor:mfc   markeredgeColor:mec
#o是圆形
#-.   :

plt.plot(x,x**2,color='cyan',linewidth=3,markersize='20',linestyle='-.')
plt.legend(['y=2*x+1','y=x^2']) ##图例位置不能互换

#4添加
plt.title('折线图') #标题
plt.xlabel('x轴')  #x名称
plt.ylabel('y轴') #y名称

plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.yticks([]) #根据函数给出y范围

#保存
plt.savefig('line.png')

#4.显示图片
plt.show()













