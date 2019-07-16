import numpy as np
import matplotlib.pyplot as plt




plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False

plt.figure(figsize=(8,8))
x=np.arange(0,2*np.pi,0.1)
plt.plot(x,np.sin(x),color='aqua',linestyle=':')
plt.plot(x,np.cos(x),color='yellow')
plt.legend(['y=sin(x)','y=cos(x)'])
plt.title('三角函数图像')
plt.xlabel('x的取值范围')
plt.xlabel('y的取值范围')
plt.show()


plt.figure(figsize=(8,8))
a=np.arange(0,2*np.pi+0.1,0.1)
plt.plot(np.cos(a),np.sin(a))
plt.legend(['y=pi(a)'])
plt.title('圆的图像')
plt.xlabel('x的取值范围')
plt.xlabel('y的取值范围')

plt.show()

