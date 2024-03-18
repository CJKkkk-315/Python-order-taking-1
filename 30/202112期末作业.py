# -*- coding: utf-8 -*-
"""
2021年12月，Python在数据分析中的应用：期末作业

基本要求：

1. 提交要求：可以从头到尾执行的.py文件，因此不建议使用Jupyter。文件命名为“学号_姓名.py”，注意中间有下划线。
2. 基本要求：代码执行完成 + 输出正确结果。
3. 加分项：良好的程序结构 + 良好的注释。
4. 欢迎查询资料以及讨论，但应独立完成。


注1：打印结果的代码，所有print()代码，请勿修改。

注2：数据的读写必须使用**相对路径**。可参考讲义对应章节。

"""

# %% 范例

"""
现有一个变量a=1，一个变量b=2。
请计算c=a+b，并最终打印变量c的值
"""
a = 1
b = 2
c = a + b

print(c)

# %%

# ==============================================
# 
# 题目开始
#
# ==============================================

# %%
"""
总体目标：

本次作业的总体目标是：计算A股上市公司中，2020年度平均ROE高的5个行业（排除ST股和公司少于10家的行业）。


数据说明：

在data文件夹下，有2份数据
1. data/sample_basic_info.xlsx，为A股上市公司的基础信息，包括公司代码、简称等
2. data/sample_fin_data.xlsx，为A股上市公司近5年的部分财务数据

"""

# %% E1
print("E1")
"""
题目1：数据的读取

1. 读取sample_basic_info.xlsx，到basic_info_df
2. 读取sample_fin_data，到fin_data_df

输出1：
打印basic_info_df行数
打印fin_data_df的行数
"""
import pandas as pd
from pandas.core.frame import DataFrame
#读取数据
basic_info_df = pd.read_csv('data/sample_basic_info.csv')
fin_data_df = pd.read_csv('data/sample_fin_data.csv')
#输出行数
print(len(basic_info_df))
print(len(fin_data_df))

# %% E2
print("E2")
"""
题目2：

1. 以“证券代码”为标准，把basic_info_df的全部数据与merge到fin_data_df中，保存到变量data中
2. 在上述数据基础上，计算全样本的净资产收益率，其中“净资产收益率 = 净利润 / 净资产”，存入data[净资产收益率]中。

输出2：
1. 打印净资产收益率的最大值，保留2位小数。

"""
#将两个数据以证券代码为标准连接
data = pd.merge(basic_info_df, fin_data_df, on='证券代码')
tp = []
#逐个计算全样本的净资产收益率
for i,j in zip(data['净利润'].items(),data['净资产'].items()):
    tp.append(i[1]/j[1])
tp = DataFrame(tp)
data['净资产收益率'] = tp
print(round(max(data['净资产收益率']), 2))

# %% E3
print("E3")
"""
题目3：
1. 在上述数据基础上，排除“证券简称”中含有“ST”的企业（注意是大写ST）

输出：
1. 打印处理后的data的样本数。

"""

# <请在此处完成代码>
#drop掉所有带有ST的企业
data.drop(data[data.apply(lambda row: 'ST' in row.to_string(header=False), axis=1)].index, inplace=True)
print(len(data))

# %% E4
print("E4")
"""
题目4：

1. 提取2020年的统计数据，写入变量data_2020
2. 在data_2020基础上，按“行业名称”，计算每一个行业的上市公司数量（提示，value_counts)
3. 上述数据保存为一个2列的DataFrame，名为ind_size。第一列为“行业名称”，第二列为“公司数量”（提示:reset_index，rename）

输出4：

1.公司最多的行业名称 

"""

#将数据类型转为str
data = data.astype(str)
#提取出统计时间为2020年的数据
data_2020 = data[(data['统计截止日期'].str.contains('2020'))]
#存入新的DataFrame中
ind_size = DataFrame(data_2020['行业名称'].value_counts().reset_index())
ind_size.columns = ['行业名称','公司数量']
print(ind_size['行业名称'][0])

# %%
print("E5")
"""
题目5：

1. 计算data_2020中，每个行业的净资产收益率的均值，保存为roe_2020（提示：groupby）
2. roe_2020的第一列为“行业名称”，第二列为“净资产收益率”
3. 把ind_size，以行业名称为标准，并入roe_2020中。
4. 从roe_2020中，排除上市公司数量不足<10的行业

输出：

1. 打印行业数量

"""


#计算2020年全部数据的净资产收益率
roe_2020 = DataFrame(list(zip(data_2020['行业名称'],data_2020['净资产收益率'])))
roe_2020.columns = ['行业名称','净资产收益率']
#以行业名称为标准，将ind_size和roe_2020进行连接
roe_2020["净资产收益率"] = pd.to_numeric(roe_2020["净资产收益率"],errors='coerce')
roe_2020 = roe_2020.groupby('行业名称').mean()
roe_2020 = pd.merge(roe_2020, ind_size, on='行业名称')
#drop掉上市公司数量不足10的行业
roe_2020 = roe_2020.drop(roe_2020[roe_2020['公司数量']<10].index)
print(len(roe_2020))

# %%
print("E6")
"""
题目6：

1. 基于roe_2020，选出净资产收益率最高的5个行业，存入top5_ind中
2. 打印净资产收益率最高的行业名称，及其净资产收益率（保留2位小数）。

"""

#根据净资产收益率进行排序，提取头5个存入TOP5_ind
top5_ind = roe_2020.sort_values(by = '净资产收益率',ascending=False).head(5)
print(top5_ind.行业名称.values[0])
print(round(top5_ind.净资产收益率.values[0], 2))
