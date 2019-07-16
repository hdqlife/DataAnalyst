import pandas as pd
import numpy as np

#pandas的数据类型只有DataFrame、Series
#(1）读取各种文件数据
#（2）掌握dataframe的常用属性和操作
#（3）掌握基础时间数据处理方法
#（4）掌握分组聚合的原理和方法
#（5）掌握透视表和交叉表的制作

##==============如何创建dataframe==================

##班级、姓名、年龄、

# data=pd.DataFrame(columns=['name', 'class', 'age'],
#                   data=[['nx', '0403', 20], ['ft', '0218', 19], ['lx', '1224', 21]])   #二维 列表套列表
# print(data)
#
# data2=pd.DataFrame({'小写':["a","b","c"],'大写':["A","B","C"]},index=['aa','bb','cc'])
# print(data2)

#Series只有长度概念，无shape,一维
# data3=pd.Series(index=[0,1,2,3],data=["a","b","c","d"])
# print(data3)
# print(data3.ndim) #一维


#==================1.读文件=================
#读取Excel表： .xlsx/  .xls   #包含表头和行索引
detail=pd.read_excel(r'E:\DataAnalyst\数据分析表\meal_order_detail.xlsx',sheet_name=2)
# print(detail)
# print(type(detail))

#读取文本文件：.txt /.csv(默认是‘，’分隔符文件)

order=pd.read_table(r'E:\DataAnalyst\数据分析表\meal_order_info.csv',sep=',',encoding='gbk',engine='python')
# print(order)
# print(type(order))

##读取csv：
order2=pd.read_csv(r'E:\DataAnalyst\数据分析表\meal_order_info.csv',sep=',',encoding='gbk',engine='python')

# print(order2)
# print(type(order2))



##二、掌握dataframe的常用操作
#（1）查看数据大小、维度信息

#values:元素/index：行索引；/columns列索引 /dtypes元素类型
#size/ndim/shape
# print('行索引：\n',order2.index)
# print('列索引：\n',order2.columns)
# print('列索引：\n',type(order2.columns))
# print('查看所有元素：\n',order2.values) #返回数组类型
# print('查看所有元素：\n',type(order2.values))
# print('查看元素类型：\n',order2.dtypes)
# print('查看所有元素个数：\n',order2.size)
# print('查看维度：\n',order2.ndim)
# print('查看结构：\n',order2.shape)
# print('表转置：\n',order2.T) #行列转换

#（2）操作dataframe表

#简单切片
# print(order2.columns)
# print(order2['phone'])
# print(type(order2['phone'])) #<class 'pandas.core.series.Series'>
# print(order2['phone'].ndim) #1维
# print(order2[['phone','name']])
# print(type(order2[['phone','name']])) #<class 'pandas.core.frame.DataFrame'>
# print(order2[['phone','name']].ndim) #2维
# print(order2[['phone','name']].values) #数组类型
# print('获取phone的前2行：\n',order2['phone'][:2])
# print('获取整张表的前五行：\n',order2[:][:5])
# print('获取整张表的前五行：\n',order2[:5])

#head/tail
# print(order2.head(6)) #获取前几行，默认为前五行
# print(order2.tail(7)) #获取后几行，默认为后五行

#利用loc/iloc方法取值

#dataframe.loc[行的索引名称,列的索引名称]   数据类型为dataframe
#dataframe.iloc[行的索引位置,列的索引位置]

# print(order2.loc[:, 'phone'])
# print(order2.loc[:,[ 'phone','name']])
# print(order2.loc[3:4,[ 'phone','name']]) #3,4都包括，前闭后闭的方法
# print(order2.iloc[3:5,[-2,-1]]) #前闭后开的切片

#条件切片：#dataframe.loc[行的索引条件,列的索引名称]
# print(order2.dtypes)
# print(order2.loc[order2['info_id'] == 417, ['info_id''phone', 'name']])
# print(order2.loc[order2['info_id'] >417, ['info_id','phone', 'name']])  #条件其实就是bool取值
# print(detail.loc[detail['dishes_name'] =="凉拌菠菜", ['order_id','dishes_name']])  #其实就是bool取值
#
# mask1=detail["dishes_name"]=='凉拌菠菜'
# mask2=detail["dishes_name"]=='凉拌萝卜丝'
# mask=mask1 | mask2  #对应元素  | (或) &(与)运算 不能使用or
# print(detail.loc[mask, ['dishes_name', 'order_id']])

# import numpy as np
# arr1=detail['dishes_name'].values
# mask1=arr1=="凉拌菠菜"
# mask2=arr1=="凉拌萝卜丝"
# arr=np.vstack((mask1,mask2))
# # print(arr)
# mask=np.any(arr,axis=0)
# # print(mask)
# print(detail.loc[mask, ['order_id', 'dishes_name']])


# 获取所有users中籍贯为广东，且年龄大于18岁的所有同学的姓名，以及班级；
users=pd.read_excel(r'E:\DataAnalyst\数据分析表\users.xlsx')



####方法一：
# user=pd.read_excel(r'E:\DataAnalyst\数据分析表\users.xlsx')
# # print(user)
# area=user.loc[:,'poo'].values
# # print(area)  #<class 'numpy.ndarray'>
# j=[]
# for i in area:
#     # print(i)
#     i=str(i)
#     j.append(i[:2])
# z=np.array(j)
# # print(z)
# mask1= z == "广东"
# mask2=user['age'] >= 18
# mask=mask1 & mask2#且
# print(user.loc[mask, ['ACCOUNT', 'ORGANIZE_NAME', 'poo', 'age']])

###方法二
# users = pd.read_excel(r'E:\DataAnalyst\数据分析表\users.xlsx')
# # print(users)
# # print(users.columns)
# mask1 = users['poo']
# mask1_list = []
# for i in mask1:
#     contont = str(i)[:2]
#     if contont=='广东':
#         mask1_list.append(True)
#     else:
#         mask1_list.append(False)
# # print(mask1_list)
# mask2 = users['age'] > 18
# # print(mask2)
# mask = mask1_list & mask2  # 第一种
# # print(mask)
# # mask = np.all(mask, axis=0)
# print(users.loc[mask, ['ACCOUNT', 'ORGANIZE_ID', 'ORGANIZE_NAME', 'poo', 'age']])

####方法三(简单)
# user = pd.read_excel(r'E:\DataAnalyst\数据分析表\users.xlsx')
# marker=[]
# for i in range(user['poo'].size):
#     if '广东' in str(user['poo'][i]) and user['age'][i]>18:
#         marker.append(True)
#     else:
#         marker.append(False)
# print(user.loc[marker, ['ACCOUNT','poo','age']])


####方法四
# import numpy
# detail2 = pd.read_excel(r'E:\DataAnalyst\数据分析表\users.xlsx',sheet_time=1)
# arr1 = detail2['poo'].values
# mask =  numpy.array([True if '广东' in str(i) else False for i in arr1 ])
# arr2 = detail2['age'].values
# mask1 = numpy.array([True if i>18 else False for i in arr2 ])
# mask2 = mask & mask1
# some = detail2.loc[mask2,['ACCOUNT','ORGANIZE_ID','ORGANIZE_NAME','poo','age']]
# print(some)


###############五方法
# import numpy
# students=pd.read_excel(r'E:\DataAnalyst\数据分析表\users.xlsx')
# mask1=students['age']>=18
# # print(mask1)
# pool_list=[str(i)[:2] for i in students['poo'].values]
# arr1=numpy.array([pool_list])
# mask2=arr1=='广东'
# # print(mask2)
# arr=numpy.vstack((mask1,mask2))
# mask=numpy.all(arr,axis=0)
# # print(mask)
# print(students.loc[mask,['ORGANIZE_ID','ORGANIZE_NAME','ACCOUNT','age']])

############六方法（推荐使用）
# use=pd.read_excel(r'E:\DataAnalyst\数据分析表\users.xlsx')
# mask1=use['poo'].str.contains('广东')
# mask2=use['age']>18
# mask=mask1 & mask2
# x=use.loc[mask,['ACCOUNT','ORGANIZE_ID','ORGANIZE_NAME','poo','age']]
# print(x)


#3.更改数据
# users['age']=18
# print(users['age'])

# users.loc[users['age']<25,'age']=0
# print(users.loc[users['age']<25,'age'])

#4.增添数据
# print(detail.columns)
#
# detail['payment']=detail['counts']*detail['amounts']
# detail['payway']='微信支付'
# print(detail)

####==5.删除数据
##删除某一列：inplace：表示是否对原表进行修改
# detail.drop(labels='payway',axis=1,inplace=True) #横向
# print(detail.columns)

# detail.drop(labels=range(10),axis=0,inplace=True) #纵向
# print(detail.index)


######################统计分析函数============

#补充

#1.通过numpy中的函数做统计：

#np.median #中位数     np.ptp :极差
# print(np.median(detail['amounts']))

#2.pandas方法
#min/max/mean/ptp极差/median中位数/std/var/
#mode 众数 /count非空值数目/value_counts: 频率统计
# print(detail['amounts'].min())
# print(detail['amounts'].mode())
# print(detail['amounts'].size)
# print(detail['amounts'].count())
# print(detail['dishes_name'].value_counts()) #默认排序 从高到低
#
# ###
#1.查看那个菜卖的最好？
#（包含白饭，所有是白饭的数据，删掉）
#方法一：
# mask=detail['dishes_name'].str.contains('白饭')
# # print(mask)
# index=detail.loc[mask,'order_id'].index
# # print(index)
# detail.drop(labels=index,axis=0,inplace=True)
# print(detail['dishes_name'].mode())
# print(detail['dishes_name'].value_counts().index[0])

#方法二
# mask1=detail['dishes_name'] =='白饭/大碗'
# mask2=detail['dishes_name']=='白饭/小碗'
# mask3=mask | mask2
# mask4=detail.loc[mask3]['dishes_name']
# mask=mask4.index
# detail.drop(labels=mask)
# print(detail['dishes_name'].value_counts().index[0])


###=====================describe================
#
# print(detail[['counts', 'amounts']].describe())
# print(detail[['counts', 'dishes_name']].describe())

#返回统计函数
#             counts      amounts
# count  3611.000000  3611.000000 ##非空数目
# mean      1.104403    44.748823  #均值
# std       0.600471    35.698775
# min       1.000000     1.000000  ##以下是五个4分位数
# 25%       1.000000    22.500000
# 50%       1.000000    35.000000
# 75%       1.000000    56.000000
# max      10.000000   178.000000


##针对类别型数据
# print(detail.dtypes)
#使用astype方法将目标数据类型转化为类别型
detail['counts']=detail['counts'].astype('category')
# print(detail['counts'].describe())
# print(detail[['counts','dishes_name']].describe())

# count     3611     #非空值
# unique       9     #类别数目   去重之后的个数
# top          1    #出现次数最多的类别 （众数）
# freq      3430    #出现最多的类别出现的的次数（频数=》value_counts）
# Name: counts, dtype: int64

##1.剔除整张表中全为nan的列：
##2.删除整张表中取值相同的列
# print(detail.shape)
# detail.dropna(axis=1, how='any')
# print(detail.shape)

#方法一：
# for i in detail.columns:
#     detail[i]=detail[i].astype('category')
#     # print(detail[i].describe())
#     # print(detail[i].describe()[1])
#     if detail[i].describe()[1]==1 or detail[i].describe()[1]==0:
#         detail.drop(labels=i, axis=1, inplace=True)
# print(detail)


#方法二：
#获取所有的列索引，但是需要拿到列索引取值的时候
#首先得将columns类型转换为数组：
# column=np.array(detail.columns)
# #2将所得的列转换为category类型
# detail[column]=detail[column].astype('category')
# #3.利用describe的第二种用法，求所有列的unique值
# unique1=detail.describe().loc['unique',:]
# #4.获取满足条件的列名
# mask1=unique1==0#全为空列
# mask2=unique1==1#全列相同
# mask=mask1 | mask2 ##满足条件的bool数组
# labels=unique1.index[mask] #获取所有满足条件的列名
# print(labels)
# #5.删除所有满足条件的列名：
# detail.drop(labels=labels,axis=1,inplace=True)
# print(detail.shape)


#==================三掌握基础时间数据处理方法=======================
# print(order.columns)
# print(order.dtypes)

##时间转换为标准时间类型

order['lock_time']=pd.to_datetime(order['lock_time'])
# print(order['lock_time'].dtypes)
# print(order['lock_time'])
##2.提取时间：用到列表推导式
#常用属性值

# year1=[i.year for i in order['lock_time']]
# month1=[i.month for i in order['lock_time']] #月份
# day1=[i.day for i in order['lock_time']]
# hour1=[i.hour for i in order['lock_time']]
# minute1=[i.minute for i in order['lock_time']]
# second1=[i.second for i in order['lock_time']]
# week1=[i.week for i in order['lock_time']]
# quarter1=[i.quarter for i in order['lock_time']]
# weekday_name1=[i.weekday_name for i in order['lock_time']]
# print(year1,month1,day1,hour1,minute1,second1,week1,quarter1,weekday_name1)

##3.时间的加减运算
# print(order['lock_time'])
# #weeks周（其中最大为周加减），days, hours, minutes ,seconds
# print(order['lock_time'] + pd.Timedelta(days=1))
# print(order['lock_time'] - pd.to_datetime('2016-1-1'))

##====================掌握分组聚合的原理和方法=========================
# print(order2['lock_time'])
# print(type(order2['lock_time'])) #<class 'pandas.core.series.Series'> 一层
# print(type(order2[['lock_time']])) #<class 'pandas.core.frame.DataFrame'> 两层

# print(detail.columns)
##1.统计不同的订单号，各点多少个菜：
#(1)分组
detail_grounp=detail[['order_id','counts','amounts']].groupby(by='order_id')
# print(detail_grounp) #<pandas.core.groupby.DataFrameGroupBy object at 0x00000000061B1DD8>


#（2）聚合：
# print(detail_grounp.sum())
# print(detail_grounp.size()) ##每组的大小

#2.聚合函数==》agg:
# print(detail[['counts', 'amounts']].agg([np.sum, np.mean]))
# print(detail_grounp.agg([np.sum, np.mean]))
#          counts           amounts
#             sum      mean     sum       mean
# order_id
# 163          10  2.000000     182  36.400000
# 167          13  1.444444     344  38.222222
# 168           9  1.800000     423  84.600000
# 176           7  1.000000     365  52.142857

#(2)agg第二种用法，针对不同字段，求不同的统计函数
# print(detail.agg({'counts': np.sum, 'amounts': [np.mean, np.sum]}))

##transform聚合方法
print(detail[['counts', 'amounts']].transform(lambda x:x * 4).head())

#任务1：detail第一张表中 利用place_order_time， 求每日的营业额：
# detail['place_order_time']=pd.to_datetime(detail['place_order_time'])
# detail['day']=[i.day for i in detail['place_order_time']]
# detail['payment']=detail['counts']*detail['amounts']
# print(detail[['day','payment']].groupby(by='day').sum())

#任务2：求单日菜品的总销量数目
# mask=detail['dishes_name'].str.contains('白饭')
# index1=detail[mask].index
# detail.drop(labels=index1,axis=0,inplace=True)
# print(detail[['counts','day']].groupby('day').sum())

#任务3：求单日最受欢迎的菜品名称

#方法一
# meal_data1=pd.read_excel('E:\DataAnalyst\数据分析表\meal_order_detail.xlsx',sheet_name=0)
# meal_data1['day']=[i.day for i in meal_data1['place_order_time']]
# mask1=meal_data1['dishes_name'].str.contains('饭')
# x=meal_data1.loc[mask1,'dishes_name'].index
# meal_data1.drop(labels=x,axis=0,inplace=True)
# for d in meal_data1['day'].unique():
#     mask=meal_data1['day']==d
#     data=meal_data1.loc[mask, ['dishes_name', 'counts']]
#     gp=data[['dishes_name', 'counts']].groupby(by='dishes_name')['counts'].sum().sort_values(ascending=False)
#     print(f'{d}日卖得最多的菜是{gp.index[0]}')


#方法二
# detail['day']=[i.day for i in detail['place_order_time']]
# mask1=detail['dishes_name'].str.contains('饭')
# x=detail.loc[mask1,'dishes_name'].index
# detail.drop(labels=x,axis=0,inplace=True)
# day_time = detail['day'].unique()
# day_group2 = detail[['day', 'dishes_name', 'counts']].groupby(by='day')
# for i, j in zip(day_group2, day_time):
#     dishes_group = i[1][['dishes_name', 'counts']].groupby(by='dishes_name')
#     data = dishes_group.sum()
#     index = data.loc[data['counts']==data['counts'].max(), ['counts']].index
#     print(f'第{j}天最受欢迎的菜品：')
#     for k in index:
#         print(k)




#（3）删除全为空或者是所有元素相同的列






