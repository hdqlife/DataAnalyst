import numpy as np
import matplotlib.pyplot as plt
a=np.arange(-np.pi,np.pi,2 * np.pi / 1000)
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
plt.title("sin-cos")
plt.xlabel('刻度')
plt.ylabel('数值')
plt.plot(a,np.sin(a), linewidth=2, linestyle="-", color="red")
plt.plot(a,np.cos(a), linewidth=2, linestyle="-", color="blue")
plt.legend(['sin图','cos图'])
plt.show()

plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
plt.title("圆")
plt.xlabel('刻度')
plt.ylabel('数值')
theta = np.arange(0, 2 * np.pi, 2 * np.pi / 1000)
x1 = np.cos(theta)
y1 = np.sin(theta)
plt.plot(x1, y1,color='pink')
plt.show()
