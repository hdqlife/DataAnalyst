import numpy as np
import matplotlib.pyplot as plt
data1=np.load(r'E:\DataAnalyst\job\populations.npz')#需要打开二进制文件的位置
# print(data1)

data=data1['data']
feature_names=data1['feature_names']
print(data)
print(feature_names)
#----------------------------------------------------------------------------------
# #1.
p1=plt.figure(figsize=(30,20))
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
plt.title("1996-2015年男女，城乡和总人口所对应的散点图与折线图")
#总人口折线
p1.add_subplot(3,2,1)
x=data[:20:,0]
y=data[:20:,1]
plt.plot(x,y,marker="*")
plt.xlabel("年份")
plt.ylabel("人口数(万人)")
# plt.xticks(x,data[0:20:,0],rotation=45)
plt.legend(['总人口'])
for x,y in zip(x,y):
    plt.text(x,y,y,ha="center",va="bottom",fontsize=8)
#总人口的散点
p1.add_subplot(3,2,2)
x=data[:20:,0]
y=data[:20:,1]
plt.scatter(x,y,color='r')
plt.xlabel("年份")
plt.ylabel("人口数(万人)")
plt.xticks(x,data[0:20:,0],rotation=45)
plt.legend(['总人口'])
#男女折线
p1.add_subplot(3,2,3)
x1=data[:20:,0]
y1=data[:20:,2]
x2=data[:20:,0]
y2=data[:20:,3]
plt.plot(x1,y1,marker="p")
plt.plot(x2,y2,marker="h")
plt.xlabel("年份")
plt.ylabel("人口数(万人)")
plt.xticks(x,data[0:20:,0],rotation=45)
plt.legend(['男性人口','女性人口'])
for x1,y1 in zip(x1,y1):
    plt.text(x1,y1,y1,ha="center",va="bottom",fontsize=8)
for x2,y2 in zip(x2,y2):
    plt.text(x2,y2,y2,ha="center",va="bottom",fontsize=8)
#男女散点
p1.add_subplot(3,2,4)
x1=data[:20:,0]
y1=data[:20:,2]
x2=data[:20:,0]
y2=data[:20:,3]
plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.xlabel("年份")
plt.ylabel("人口数(万人)")
plt.xticks(x,data[0:20:,0],rotation=45)
plt.legend(['男性人口','女性人口'])#'城市人口','乡村人口'
#城乡折线
p1.add_subplot(3,2,5)
x3=data[:20:,0]
y3=data[:20:,4]
x4=data[:20:,0]
y4=data[:20:,5]
plt.plot(x3,y3,marker="s")
plt.plot(x4,y4,marker="o")
plt.xlabel("年份")
plt.ylabel("人口数(万人)")
plt.xticks(x,data[0:20:,0],rotation=45)
plt.legend(['城市人口','乡村人口'])
for x3,y3 in zip(x3,y3):
    plt.text(x3,y3,y3,ha="center",va="bottom",fontsize=8)
for x4,y4 in zip(x4,y4):
    plt.text(x4,y4,y4,ha="center",va="bottom",fontsize=8)
#城乡散点
p1.add_subplot(3,2,6)
x3=data[:20:,0]
y3=data[:20:,4]
x4=data[:20:,0]
y4=data[:20:,5]
plt.scatter(x3,y3)
plt.scatter(x4,y4)
plt.xlabel("年份")
plt.ylabel("人口数(万人)")
plt.xticks(x,data[0:20:,0],rotation=45)
plt.legend(['城市人口','乡村人口'])
plt.savefig("一.png")
plt.show()
# 分析，男生比女生多，男女比例失调，长大后会娶不到老婆啊！！！！！
# 乡村人口会逐年递减，城市人口会逐年递增，乡村人口与城市人口的占比会严重失衡

# 2.直方图
##=========================================================================================2.1城乡所占总人数比例
# p1=plt.figure(figsize=(30,25))
# plt.rcParams['font.sans-serif']='SimHei'
# plt.rcParams['axes.unicode_minus']=False
# p1.add_subplot(2,1,1)
# plt.title("1996-2015城乡人口占总人数百分比与人口数直方图").set_size(20)#set_size(20)修改标题字的大小
# y=data[-3:-23:-1,4]
# x=range(0,80,4)
#
# y1=data[-3:-23:-1,5]
# x1=range(1,81,4)
#
# y2=data[-3:-23:-1,1]
# x2=range(0,80,4)
#
# y3=data[-3:-23:-1,1]
# x3=range(0,80,4)
#
# y4=data[-3:-23:-1,1]
# x4=range(0,80,4)
#
# plt.bar(x,y,width=1)
# plt.bar(x1,y1,width=1)
# plt.plot(x2,y2,marker=">",markersize=10,color="y")
# plt.xlabel("年份")
# plt.ylabel("人口数(万人)")
# plt.legend(["总人数","城市人口",'乡村人口'])
# plt.xticks(x,data[-3:-23:-1,0],rotation=90)
# for x,y,x2,y2 in zip(x,y,x2,y2):
#     a=y / y2 * 100;
#     a*=10;
#     a=int(a)
#     a=float(a)
#     a=a/10
#     plt.text(x,y,str(a)+"%",ha="center",va="bottom",fontsize=10,color='y')
# for x1,y1,x3,y3 in zip(x1,y1,x3,y3):
#     a = y1 / y3 * 100;
#     a *= 10;
#     a = int(a)
#     a = float(a)
#     a = a / 10
#     plt.text(x1,y1,str(a)+"%",ha="center",va="bottom",fontsize=10,color='y')
# for x4,y4 in zip(x4,y4):
#     plt.text(x4,y4,y4,ha="center",va="bottom",fontsize=10)
#
# #城乡人口数
# p1.add_subplot(2,1,2)
# y=data[-3:-23:-1,4]
# x=range(0,80,4)
#
# y1=data[-3:-23:-1,5]
# x1=range(1,81,4)
#
# y2=data[-3:-23:-1,4]
# x2=range(0,80,4)
#
# y3=data[-3:-23:-1,5]
# x3=range(1,81,4)
#
# plt.bar(x,y,width=1)
# plt.bar(x1,y1,width=1)
# plt.plot(x2,y2,marker=">",markersize=10,color="y")
# plt.plot(x3,y3,marker="<",markersize=10,color="r")
# plt.xlabel("年份")
# plt.ylabel("人口数(万人)")
# plt.legend(["城市",'乡村',"城市人口",'乡村人口'])
# plt.xticks(x,data[-3:-23:-1,0],rotation=90)
# for x2,y2 in zip(x2,y2):
#     plt.text(x2,y2,y2,ha="center",va="bottom",fontsize=10)
# for x3, y3 in zip(x3, y3):
#     plt.text(x3, y3, y3, ha="center", va="bottom", fontsize=10)
# plt.savefig("城乡直.png")
# plt.show()


#==================================================================================================2.2男女人口占比
# p1=plt.figure(figsize=(30,25))
# plt.rcParams['font.sans-serif']='SimHei'
# plt.rcParams['axes.unicode_minus']=False
# plt.title("1996-2015男女人口占总人数百分比与人口数直方图").set_size(20)
# p1.add_subplot(2,1,1)
# #总人数
# y=data[-3:-23:-1,1]
# x=range(20)
# #男性人数
# y1=data[-3:-23:-1,2]
# x1=range(20)
#
# y3=data[-3:-23:-1,2]
# x3=range(20)
#
# #总人数
# y2=data[-3:-23:-1,1]
# x2=range(20)
#
# #总人数
# y4=data[-3:-23:-1,1]
# x4=range(20)
# plt.bar(x,y,width=0.3)
# plt.plot(x,y,marker=">",color="r",markersize=10)
# plt.bar(x1,y1,width=0.3)
# plt.xlabel("年份")
# plt.ylabel("人口数（万人）")
# plt.xticks(x,data[-3:-23:-1,0])
# plt.legend(["总人数",'女性占比',"男性占比"])
# for x,y in zip(x,y):
#     plt.text(x,y,y,ha="center",va="bottom",fontsize=10)
# #男性百分比
# for x1,y1,x2,y2 in zip(x1,y1,x2,y2):
#     a = y1 / y2 * 100;
#     a *= 10;
#     a = int(a)
#     a = float(a)
#     a = a / 10
#     plt.text(x1,y1,str(a)+"%",ha="center",va="top",fontsize=10)#va里的值只能是'top', 'bottom', 'center', 'baseline'
# #女性百分比
# for x3,y3,x4,y4 in zip(x3,y3,x4,y4):
#     a = y3 / y4 * 100;
#     a *= 10;
#     a = int(a)
#     a = float(a)
#     a = a / 10
#     b=100-a
#     plt.text(x3,y3,str(b)+"%",ha="center",va="bottom",fontsize=10,color='yellow')
# #男女人口数
# p1.add_subplot(2,1,2)
# y=data[-3:-23:-1,2]
# x=range(0,80,4)
#
# y1=data[-3:-23:-1,3]
# x1=range(1,81,4)
#
# plt.bar(x,y,width=1)
# plt.bar(x1,y1,width=1)
# plt.plot(x,y,marker="<",markersize=10,color="r")
# plt.plot(x1,y1,marker=">",markersize=10,color="y")
#
# plt.xlabel("年份")
# plt.ylabel("人口数(万人)")
# plt.legend(["男性",'女性',"男性人口",'女性人口'])
# plt.xticks(x,data[-3:-23:-1,0],rotation=90)
# for x,y in zip(x,y):
#     plt.text(x,y,y,ha="center",va="bottom",fontsize=8,color="b")
# for x1, y1 in zip(x1, y1):
#     plt.text(x1, y1, y1, ha="center", va="bottom", fontsize=8,color="r")
# plt.savefig("男女直方.png")
# plt.show()




# #---------------------------------------------------------------------------------------------------- 饼图
# #男女1996-2015年的人口占比
# plt.rcParams['font.sans-serif']='SimHei'
# plt.rcParams['axes.unicode_minus']=False
# p1=plt.figure(figsize=(30,40))
# plt.title("1996-2015男女占总人数的占比情况").set_size(20)
# num=1
# count=0
# year=2015
# for i in data[-3:-23:-1]:
#     p1.add_subplot(4, 5, num)
#     lable = ["男性人口"+str(year)+"年", '女性人口'+str(year)+"年"]
#     plt.pie(data[count,2:4],explode=[0,0],autopct='%1.1f%%',labels=lable)
#     num+=1
#     count+=1
#     year-=1
# plt.savefig("男女.png")
# plt.show()



##城乡1996-2015年的人口占比
# plt.rcParams['font.sans-serif']='SimHei'
# plt.rcParams['axes.unicode_minus']=False
# p1=plt.figure(figsize=(20,25))
# plt.title("1996-2015城乡占总人数的占比情况").set_size(20)
# num=1
# count=0
# year=2015
# for i in data[-3:-23:-1]:
#     p1.add_subplot(4,5,num)
#     lable=["城市人口"+str(year)+"年",'农村人口'+str(year)+"年"]
#     plt.pie(data[count,4:6],explode=[0,0],autopct='%1.1f%%',labels=lable)
#     num+=1
#     count+=1
#     year-=1
# plt.savefig("城乡.png")
plt.show()

# plt.savefig(r"C:\Users\AsuraDong\Desktop\test.png")#这个样可以设置保存的路径
# 控制x轴和y轴的范围
# plt.xlim(0,4)
# plt.ylim(0,4)


#分析：人口结构是男多女少，2010年之前乡村人口多余城市人口，之后就少于城市人口，城市人口逐年增加，农村人口逐年减少
#：人口增长速度较快，人口每年都在增加，