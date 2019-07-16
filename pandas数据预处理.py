##创建透视表与交叉表

import pandas as pd
import numpy as np
detail=pd.read_excel(r'E:\DataAnalyst\数据分析表\meal_order_detail.xlsx',sheet_name=1)
# print(detail)
# 透视表：pivot_table==> groupby:

'''
aggfunc:聚合函数：np.sum/np.mean/np.std
index:行分组键
colunms:列分组键
values:想要求统计的元素
fill_value:填充值 将表中的nan值修改为任何一个想要的值
margins：汇总开关
'''
##1行分组
# print(pd.pivot_table(detail[['order_id', 'counts', 'amounts']], index='order_id',aggfunc=np.sum))

##2.多个行分组键
# detail_pivot=pd.pivot_table(detail[['order_id', 'counts', 'amounts','dishes_name']], index=['order_id','dishes_name'],aggfunc=np.sum)
# print(detail_pivot)
# print(detail_pivot.index)

#3.列分组键
# print(pd.pivot_table(detail[['order_id', 'counts', 'amounts','dishes_name']],
#                      index='order_id',
#                      columns='dishes_name',
#                      aggfunc=np.sum))
data=pd.DataFrame({'name':['张三','乔大爷','老王','李四'],
              'age':[12,16,26,50],
              'job':['student','student','doc','doc'],
              'provi':['shandong','shanxi','taiwan','taiwan']})
# print(data)
#多个行分组键
# print(pd.pivot_table(data[['job', 'age','provi']], index=['job','provi']))

#行分组键与列分组键同时使用
# print(pd.pivot_table(data[['job', 'age', 'provi']], columns='provi', index='job'))
# print(pd.pivot_table(data[['job', 'age', 'provi']], columns='provi', index='job',values='age'))
# print(pd.pivot_table(data[['job', 'age', 'provi']], columns='provi', index='job',values='age',fill_value=0))
#
# #添加汇总开关与aggfunc统一
# print(pd.pivot_table(data[['job', 'age', 'provi']],
#                      columns='provi', index='job',values='age',fill_value=0,margins=True))


##交叉表：
# print(pd.crosstab(index=data['job'], columns=data['provi'], values=data['age'],aggfunc=np.sum))


##2.合并数据

#堆叠（横向堆叠，纵向堆叠）
# df1 = pd.DataFrame({'name': ['张三', '乔大爷', '老王','李四'],
#               'age': [12, 16, 26, 50],
#               'job':['student', 'student', 'doc', 'doc'],
#               'provi': ['shandong', 'shanxi', 'taiwan', 'taiwan']},index=range(4))
#
# df2 = pd.DataFrame({'name': ['张三','赵五'],
#               'age': [ 12, 40],
#               'id': ['0', '1']}, index= [0, 4])
# print(df1)
# print(df2)

#横向堆叠外连接
# print(pd.concat([df1, df2], axis=1, join='outer'))

#横向堆叠内连接
# print(pd.concat([df1, df2], axis=1, join='inner'))

#纵向堆叠外连接
# print(pd.concat([df1, df2], axis=0, join='outer'))
#纵向堆叠内连接
# print(pd.concat([df1, df2], axis=0, join='inner'))

#主键连接 merge

# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K3'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                          'A': ['A0', 'A1', 'A2', 'A3'],
#                         'B': ['B0', 'B1', 'B2', 'B3']})
#
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                          'C': ['C0', 'C1', 'C2', 'C3'],
#                          'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# how=(left,right,inner,outer)
# merge_data=pd.merge(left,right,how='inner',on='key1')
# print(merge_data)
# omerge_data=pd.merge(left,right,how='outer',on='key1')
# print(omerge_data)
#left拼接方式
# merge_datal=pd.merge(left,right,how='left',on='key1')
# print(merge_datal)
# # #right拼接方式
# merge_datar=pd.merge(left,right,how='right',on='key1')
# print(merge_datar)

# #通过多个主键拼接
# rmerge_data=pd.merge(left,right,how='right',on=['key1','key2'])
# print(rmerge_data)
# imerge_data=pd.merge(left,right,how='inner',on=['key1','key2'])
# print(imerge_data)
# lrimerge_data=pd.merge(left,right,how='inner',left_on='key1',right_on='key2')
# print(lrimerge_data)
# lrimerge_data1=pd.merge(left,right,how='left',left_on='key2',right_on='key1')
# print(lrimerge_data1)

#重叠合并
dict1 = {'ID':[1,2,3,4,5,6,7,8,9],'System':['W10','w10',np.nan,'w10',np.nan,np.nan,'w7','w7','w8']}
dict2 = {'ID':[1,2,3,4,5,6,7,8,9],'System':[np.nan,np.nan,'w7','w7','w7','w7','w8',np.nan,np.nan]}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
# print(df1)
# print(df2)

# 主表如果有值，保留原值  df2.combine_first(df1) df2主表   df1副表
# print('合并后的数据为：\n',df2.combine_first(df1))
# print('合并后的数据为：\n',df1.combine_first(df2))


#==================清洗数据=================================================

#（1）检测处理重复值
#（2）检测处理缺失值
#（3）检测处理异常值


#1.处理重复值
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K3'],
                     'key2': [4, 3,2, 1],
                         'A': [1, 1, 2, 2],
                        'B': [1, 1, 2, 3]})

left_drop=left['key2'].drop_duplicates(keep='last')
# print(left_drop)
# #keep:frist保留第一个值,last保留最后一个值,False：只要有重复都删掉
# #1.处理重复值：不同属性，只是名字有差异，但是内容大致一致
# #相似度  -1<=相似度<=1  spearman法，kendall法
# corrdet=left[['A','B']].corr(method='kendall')
# print(corrdet)

# corrdet1=left[['A','B','key2']].corr(method='spearman')
# print(corrdet1)

# 作业 删除相似度为1 或者-1的某一列

#2.检测与处理缺失值
left = pd.DataFrame({'key1': ['k2', 'K0', 'K1', np.nan],
                     'key2': [4, 3,2,1],
                         'A': [np.nan, np.nan, np.nan, np.nan],
                        'B': [1, 1, 2, 3]})
# print(left)
#isnull/notnull
# print(left.isnull().sum())
# print(left.notnull().sum())

#(1)删除法：
# print(left.dropna(axis=1,how='any'))
# print(left.dropna(axis=0,how='any'))
# print(left.dropna(axis=1,how='all'))
#
# #(2)替换法
# print(left.fillna('-1')) #众数、中位数、均值

#(3)插值法
#线性插值
# x=np.array([1,2,3,4,5,8,9,10])
# y=np.array([3,5,7,9,11,17,19,10])
# y1 = np.array([2,8,18,32,50,128,162,200])
#
# from scipy.interpolate import interp1d
# linear=interp1d(x,y,kind='linear') #y=kx+b
# linear1=interp1d(x,y1,kind='linear')
#
# print(linear([3,6]))
#
# #拉格朗日插值
# from scipy.interpolate import lagrange
# # # larger_value=lagrange(x,y)
# larger_value=lagrange(x,y1)
#
# print(larger_value([6,7]))

# import matplotlib.pyplot as plt
# x=np.arange(1,10,1)
# y1=linear(x)
# p1=plt.figure()
# # p1.add_subplot(2,1,1)
# plt.plot(x,linear(x),marker="*",markersize=14)
# # p1.add_subplot(2,1,2)
# plt.plot(x,larger_value(x),marker="o",markersize=14)
# plt.legend('linear','larger_value')
# plt.show()

##检测与处理异常值
#(1)根据经验值判断：速度、加速度 、温度
x=np.array([1,200000,3,4,5,8,9,10])

#（2）3σ原则
#μ均值 、σ标准差
#当μ-σ<x<μ+σ(0.68)
#当μ-2σ<x<μ+2σ(0.954)
#当μ-3σ<x<μ+3σ(0.997)

# ser=detail['amounts']
# mask1=ser.mean()-3*ser.std()>ser
# mask2=ser.mean()+3*ser.std()<ser
# mask=mask1 | mask2  ##异常值对应的bool值
# print(ser[mask])

##标准化数据：
#将不同的属性值化成相同的标准

#（离差标准化，标准差标准化、小数定标标准化）

#1离差标准化
#x1=(x-min)/(max-min)
##x1范围：0<x1<=1
#问题：(1)min=max,(2)min/max异常值

#2标准差标准化
#(x-μ)/σ
##输出：均值为0， 标准差为1

#3.小数定标标准化
# x1=x/10^k
ser=detail['amounts']
# print(ser / 10 ** np.ceil((np.log10(ser.abs().max()))))

##转换数据
#(1)哑变量处理
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K3'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
# print(pd.get_dummies(left1['A']))

#(2)离散化连续型数据：
# print(pd.cut(detail['amounts'], 5))







