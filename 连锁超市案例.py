import pandas as pd
import numpy as np
order=pd.read_csv(r'E:\DataAnalyst\数据分析表\order-14.3.csv',sep=',',encoding='gbk',engine='python')
# print(order)

# 综合案例一：连锁超市的数据分析
# 1、哪些类别的商品比较畅销？
# 提示：将订单表中的数据进行按照ID分组，然后对分组后的销量求和，就会得到每一类在一段时间内的销量。
# 2、哪些商品比较畅销？
# 提示：利用透视表，来计算哪些商品比较畅销，取前十名的商品；
#
# 3、求不同门店的销售额占比
# 提示：订单中没有销售额字段，所有需要新增一个销售额字段。增加字段后按照门店编号进行分组，然后计算占比。
#
# 4、哪段时间段是超市的客流高峰期？
# 提示：需要知道每个时间段对应的客流量，但是订单表中既有日期又有时间，我们需要从中提出小时数，这里利用订单ID去重计数代表客流量。

#数据处理
# 获取数据之前先要观察数据，去掉无用的、不符合逻辑的数据
mask=order['销量']<0
index=order.index[mask]
# print(index)
order.drop(labels=index,axis=0,inplace=True)
# print(order.shape)

#1题
# print(order[['类别ID', '销量']].groupby(by='类别ID').sum().reset_index().sort_values(by="销量", ascending=False))
#reset_index重置行索引 分组健作为索引
#sort_values（by='',ascending=False）
# print(order[['类别ID', '销量']].groupby(by='类别ID').sum().reset_index())

#2题
# print(pd.pivot_table(order, index='商品ID',values='销量', aggfunc=np.sum).reset_index().sort_values(by="销量", ascending=False))

##3题
order['sale']=order['单价']*order['销量']
order_grounp1=order[['门店编号','sale']].groupby(by='门店编号')
datas=order_grounp1.sum()
print(datas)
# get_data=np.array(datas)
# print(get_data)
import matplotlib.pyplot as plt
plt.figure(figsize=(6,6))##figsize为方形
plt.rcParams['font.sans-serif']='SimHei' #将默认字体修改为仿宋
plt.rcParams['axes.unicode_minus']=False
#绘制饼图
plt.title("销售额占比")
# labels=['CDLG','CDNL','CDXL'] #饼图中的标签
explode=[0.01,0.01,0.01] #设定各项距离圆形的距离
plt.pie(datas['sale'],explode,labels=datas.index,autopct='%1.1f%%',colors=['r','b','g'])
#autopct:接受特定的string，置顶数值的显示方式
plt.show()

##4题
#方法一
order['成交时间']=pd.to_datetime(order['成交时间'])
order['小时']=[i.hour for i in order['成交时间']]
# print(order[['小时', '订单ID']].groupby(by='订单ID')['小时'].first().value_counts())

#方法二
order_group=order[['订单ID', '小时']].groupby(by='小时').describe().reset_index()
# print(order_group)
data1=order_group.values[:,(0,2)]
index=np.argsort(data1[:,1],axis=0)[:-6:-1]
# print(data1[:, 0][index])

#方法三
order['成交时间'] = pd.to_datetime(order['成交时间'])
order['hours'] = [i.hour for i in order['成交时间']]
data = order[['hours', '订单ID']].drop_duplicates(keep='first') #hour和订单号同时相同时同时去重
time_order = data['hours'].value_counts()
# print(time_order)

#方法四
order['成交时间'] = pd.to_datetime(order['成交时间'])
order['hour'] = [i.hour for i in order['成交时间']]
ok = order['订单ID'].drop_duplicates(keep='first').index
forth = order.loc[ok,['hour','订单ID']].groupby(by='hour').count().sort_values(by='订单ID',ascending=False)
# print(forth)