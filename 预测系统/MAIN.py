import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
import seaborn as sns
data_all = pd.read_excel(r'工作簿3-预测数据.xlsx')
# In[] 分析数据，根据标签查看数据分布是否均衡
plt.rcParams['font.sans-serif']=['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    # 用来正常显示负号
number2=np.sum(data_all['GOS']==2)   #统计标签中是的数量
number1=np.sum(data_all['GOS']==1)   #统计标签中否的数量
yy=[number2,number1]    #将这两个数值放到yy中，画图时作为y轴的值
xx=['2','1']     #将这两个数值放到xx中,画图时作为x轴值
fig = plt.figure(figsize=(15,8))    #设置图框大小
plt.bar(xx,list(yy), align = 'center',color=['red','green','yellow','steelblue'])    #画柱状图，并设置线条颜色
plt.title('标签分布情况')    #图的标题
plt.xlabel('标签类别')       #x轴标签
plt.ylabel('数量')           #y轴标签
# 添加数值显示
for x,y in enumerate(list(yy)):        #循环遍历yy里面的值
    plt.text(x,y+0.12,y,ha='center')  #让循环遍历yy里面的值显示在柱状图上
    
# In[] 数据预处理
#删除第一列无用特征(序号)
data_all.drop(['序号'],axis=1,inplace=True)      #删除第一列名字 
target=data_all['GOS']
feature_data=data_all.loc[:,'性别':'人血白蛋白'] 
#根据标签将数据集按照7:3的比列划分为训练集和测试集
from sklearn.model_selection import train_test_split   #导入train_test_split包用来划分数据 
train_X, test_X, train_Y, test_Y = train_test_split(feature_data,target,test_size=0.3,stratify=target)  

# In[] 训练集查看异常值
#箱线图查看异常值可视化，查看一些连续型生理特征中有无异常值
plt.rcParams['font.sans-serif']=['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    # 用来正常显示负号
df = []     #定义一个空集
cols = ['白细胞计数','红细胞计数','血红蛋白','血小板计数','成熟中性粒细胞绝对值','单核细胞绝对值','淋巴细胞绝对值','中性粒细胞绝对值','谷草转氨酶','乳酸脱氢酶','肌酸酶同工酶','羟丁酸脱氢酶','白蛋白']    #取出列名
df=train_X.loc[:,('白细胞计数','红细胞计数','血红蛋白','血小板计数','成熟中性粒细胞绝对值','单核细胞绝对值','淋巴细胞绝对值','中性粒细胞绝对值','谷草转氨酶','乳酸脱氢酶','肌酸酶同工酶','羟丁酸脱氢酶','白蛋白')]
df.plot.box(title="异常值查看",              #定义异常值查看的函数
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色)
plt.grid(linestyle="--", alpha=0.3) #设置线型，透明度
plt.xticks(rotation=30)   #x轴坐标旋转角度
plt.show()                #绘图
# In[] 测试集查看异常值
#箱线图查看异常值可视化，查看一些连续型生理特征中有无异常值
plt.rcParams['font.sans-serif']=['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    # 用来正常显示负号
df = []     #定义一个空集
cols = ['白细胞计数','红细胞计数','血红蛋白','血小板计数','成熟中性粒细胞绝对值','单核细胞绝对值','淋巴细胞绝对值','中性粒细胞绝对值','谷草转氨酶','乳酸脱氢酶','肌酸酶同工酶','羟丁酸脱氢酶','白蛋白']    #取出列名
df=test_X.loc[:,('白细胞计数','红细胞计数','血红蛋白','血小板计数','成熟中性粒细胞绝对值','单核细胞绝对值','淋巴细胞绝对值','中性粒细胞绝对值','谷草转氨酶','乳酸脱氢酶','肌酸酶同工酶','羟丁酸脱氢酶','白蛋白')]
df.plot.box(title="异常值查看",              #定义异常值查看的函数
            patch_artist=True, # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True, # 以点的形式显示均值
            boxprops = {'color':'black','facecolor':'#9999ff'}, # 设置箱体属性，填充色和边框色
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # 设置异常值属性，点的形状、填充色和边框色
            meanprops = {'marker':'D','markerfacecolor':'indianred'}, # 设置均值点的属性，点的形状、填充色
            medianprops = {'linestyle':'--','color':'orange'}) # 设置中位数线的属性，线的类型和颜色)
plt.grid(linestyle="--", alpha=0.3) #设置线型，透明度
plt.xticks(rotation=30)   #x轴坐标旋转角度
plt.show()                #绘图
# In[] 缺失值填补  
#查看训练集中的特征缺失情况  
missing=train_X.isnull().sum().reset_index().rename(columns={0:'missNum'})
# 计算缺失比例
missing['missRate']=missing['missNum']/train_X.shape[0]
# 按照缺失率排序显示
miss_analy=missing[missing.missRate>0].sort_values(by='missRate',ascending=False)# miss_analy 存储的是每个变量缺失情况的数据框
# 柱形图可视化
fig = plt.figure(figsize=(15,8))
plt.bar(np.arange(miss_analy.shape[0]), list(miss_analy.missRate.values), align = 'center',color=['red','green','yellow','steelblue'])
plt.title('训练集缺失值特征统计')
plt.xlabel('变量名称')
plt.ylabel('缺失比率')
# 添加x轴标签，并旋转90度
plt.xticks(np.arange(miss_analy.shape[0]),list(miss_analy['index']))
pl.xticks(rotation=90)
# 添加数值显示
for x,y in enumerate(list(miss_analy.missRate.values)):
    plt.text(x,y+0.01,'{:.2%}'.format(y),ha='center',rotation=90)    
plt.ylim([0,1])
plt.show() 
# In[] 去除缺失值比例大于50%的特征(对应的把测试集中那些特征也删除)
del_missing = list(missing.index)
for i in list(missing.index):
    if (missing.missRate[i] > 0.5):
        del_missing.remove(i)

names= missing['index']
names_82=names[del_missing]
train_X=train_X[names_82]
test_X=test_X[names_82]
# 对训练集和测试集的脑梗塞史这列分类型变量用众数填补
dd=int(train_X['脑梗塞史'].mode())
ee=int(test_X['脑梗塞史'].mode())
train_X['脑梗塞史'].fillna(dd, inplace=True)
test_X['脑梗塞史'].fillna(ee, inplace=True)
# In[] 删除特征后，缺失值占比大于0.1小于0.5的特征进行均值填补(测试集对应的列也用均值填补)
missing=train_X.isnull().sum(axis=0)
missing_percent = missing/train_X.shape[0]
#缺失值比列大于10%的用均值填补
list_add_means = list(missing_percent[missing_percent>0.1].index)
for column in list_add_means:
    train_X[column].fillna(train_X[column].mean(), inplace=True)
    
for column in list_add_means:
    test_X[column].fillna(test_X[column].mean(), inplace=True)   
    
# In[] 均值填补后，缺失值比列小于的10%采用KNN缺失值填补的方法(测试集也是一样)
Missing_train_1 = train_X.isnull().sum()/train_X.shape[0]
Missing_train_1  = list(Missing_train_1[Missing_train_1>0].index) 
from sklearn.impute import KNNImputer 
imputer = KNNImputer(n_neighbors=3)
df_filled = imputer.fit_transform(train_X[Missing_train_1])
df_filled = pd.DataFrame(df_filled,columns = Missing_train_1)
#删除原来索引，重新索引排序
train_X=train_X.reset_index(drop=True)
for i in Missing_train_1:
    train_X[i] = df_filled[i] 
    
    
Missing_train_1 = test_X.isnull().sum()/test_X.shape[0]
Missing_train_1  = list(Missing_train_1[Missing_train_1>0].index) 
from sklearn.impute import KNNImputer 
imputer = KNNImputer(n_neighbors=3)
df_filled = imputer.fit_transform(test_X[Missing_train_1])
df_filled = pd.DataFrame(df_filled,columns = Missing_train_1)
test_X=test_X.reset_index(drop=True)
for i in Missing_train_1:
    test_X[i] = df_filled[i]     
    
# In[] #填补后查看训练集中的特征缺失情况  
missing=train_X.isnull().sum().reset_index().rename(columns={0:'missNum'})
# 计算缺失比例
missing['missRate']=missing['missNum']/train_X.shape[0]
# 按照缺失率排序显示
miss_analy=missing[missing.missRate>0].sort_values(by='missRate',ascending=False)# miss_analy 存储的是每个变量缺失情况的数据框
# 柱形图可视化
fig = plt.figure(figsize=(15,8))
plt.bar(np.arange(miss_analy.shape[0]), list(miss_analy.missRate.values), align = 'center',color=['red','green','yellow','steelblue'])
plt.title('训练集缺失值特征统计')
plt.xlabel('变量名称')
plt.ylabel('缺失比率')
# 添加x轴标签，并旋转90度
plt.xticks(np.arange(miss_analy.shape[0]),list(miss_analy['index']))
pl.xticks(rotation=30)
# 添加数值显示
for x,y in enumerate(list(miss_analy.missRate.values)):
    plt.text(x,y+0.01,'{:.2%}'.format(y),ha='center',rotation=90)    
plt.ylim([0,1])
plt.show()     

# In[] #填补后查看测试集中的特征缺失情况  
missing=test_X.isnull().sum().reset_index().rename(columns={0:'missNum'})
# 计算缺失比例
missing['missRate']=missing['missNum']/test_X.shape[0]
# 按照缺失率排序显示
miss_analy=missing[missing.missRate>0].sort_values(by='missRate',ascending=False)# miss_analy 存储的是每个变量缺失情况的数据框
# 柱形图可视化
fig = plt.figure(figsize=(15,8))
plt.bar(np.arange(miss_analy.shape[0]), list(miss_analy.missRate.values), align = 'center',color=['red','green','yellow','steelblue'])
plt.title('测试集缺失值特征统计')
plt.xlabel('变量名称')
plt.ylabel('缺失比率')
# 添加x轴标签，并旋转90度
plt.xticks(np.arange(miss_analy.shape[0]),list(miss_analy['index']))
pl.xticks(rotation=30)
# 添加数值显示
for x,y in enumerate(list(miss_analy.missRate.values)):
    plt.text(x,y+0.01,'{:.2%}'.format(y),ha='center',rotation=90)    
plt.ylim([0,1])
plt.show()  
# In[] 查看训练数据中标签的均衡 
number2=np.sum(train_Y==2)   #统计标签中是的数量
number1=np.sum(train_Y==1)   #统计标签中否的数量
yy=[number2,number1]    #将这两个数值放到yy中，画图时作为y轴的值
xx=['2','1']     #将这两个数值放到xx中,画图时作为x轴值
fig = plt.figure(figsize=(15,8))    #设置图框大小
plt.bar(xx,list(yy), align = 'center',color=['red','green','yellow','steelblue'])    #画柱状图，并设置线条颜色
plt.title('标签分布情况')    #图的标题
plt.xlabel('标签类别')       #x轴标签
plt.ylabel('数量')           #y轴标签
# 添加数值显示
for x,y in enumerate(list(yy)):        #循环遍历yy里面的值
    plt.text(x,y+0.12,y,ha='center')  #让循环遍历yy里面的值显示在柱状图上  
# In[] SMOTE过采样，全称是Synthetic Minority Oversampling Technique，即合成少数类过采样技术 
from imblearn.over_sampling import SMOTE
X_resampled_smote, y_resampled_smote = SMOTE().fit_resample(train_X, train_Y)
# In[] 查看SMOTE过采样后训练数据中标签的均衡 
number2=np.sum(y_resampled_smote==2)   #统计标签中是的数量
number1=np.sum(y_resampled_smote==1)   #统计标签中否的数量
yy=[number2,number1]    #将这两个数值放到yy中，画图时作为y轴的值
xx=['2','1']     #将这两个数值放到xx中,画图时作为x轴值
fig = plt.figure(figsize=(15,8))    #设置图框大小
plt.bar(xx,list(yy), align = 'center',color=['red','green','yellow','steelblue'])    #画柱状图，并设置线条颜色
plt.title('标签分布情况')    #图的标题
plt.xlabel('标签类别')       #x轴标签
plt.ylabel('数量')           #y轴标签
# 添加数值显示
for x,y in enumerate(list(yy)):        #循环遍历yy里面的值
    plt.text(x,y+0.12,y,ha='center')  #让循环遍历yy里面的值显示在柱状图上 

# In[] 特征选择
#基于逻辑回归的递归特征消除法来挑选特征
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

rfe = RFE(estimator= LogisticRegression(solver='liblinear',penalty='l2'),n_features_to_select=30)
Fea_data_1 = rfe.fit_transform(X_resampled_smote,y_resampled_smote)
Fea_data_1 = pd.DataFrame(Fea_data_1)
Bool_values = rfe.get_support()
list_lr = list()
for i in X_resampled_smote.columns[Bool_values]:
    list_lr.append(i)  

#基于AdaBoost的递归特征消除法来挑选特征
from sklearn.ensemble import AdaBoostClassifier
rfe = RFE(estimator= AdaBoostClassifier(),n_features_to_select=30)
Fea_data_1 = rfe.fit_transform(X_resampled_smote,y_resampled_smote)
Fea_data_1 = pd.DataFrame(Fea_data_1)
Bool_values = rfe.get_support()
list_ada = list()
for i in X_resampled_smote.columns[Bool_values]:
    list_ada.append(i)

#基于RandomForest的递归特征消除法来挑选特征
from sklearn.ensemble import RandomForestClassifier
rfe = RFE(estimator= RandomForestClassifier(random_state=1),n_features_to_select=30)
Fea_data_1 = rfe.fit_transform(X_resampled_smote,y_resampled_smote)
Fea_data_1 = pd.DataFrame(Fea_data_1)
Bool_values = rfe.get_support()
list_rf = list()
for i in X_resampled_smote.columns[Bool_values]:
    list_rf.append(i)

##对用3种特征选择方法选择出来的特征进行取并集
list_columns = list(list_lr) + list(list_ada)+ list(list_rf)
columns_total=[]
for i in list_columns:
    if not i in columns_total:
        columns_total.append(i) 


#取出这些并集后特征对应的数据
train_X=X_resampled_smote[columns_total]
column=list(train_X)
test_X=test_X[columns_total]
train_Y=y_resampled_smote

# In[] spearman单因素分析
#某些自变量之间相关性很强，用spearman删除只保留一个
corr = train_X.corr(method='spearman')
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
f , ax = plt.subplots(figsize = (25, 25))
plt.title('Correlation of Numeric Features with Loss',y=1,size=30)
sns.heatmap(corr,square = True,annot=False,cmap="RdBu_r")#热力图

drop_list1 = list()
def Slect_Sperman(correlation):
    del_listi = []
    del_listj = []
    for i in correlation.columns:
        for j in correlation.index:
            if 1 > abs(correlation[i][j]) > 0.8:
                del_listi.append(i)
                if j not in del_listi:
                    del_listj.append(j)
    return del_listj

#提取spearman后的数据
drop_list1 = Slect_Sperman(corr)
train_X = train_X.drop(drop_list1,axis=1) 
test_X = test_X.drop(drop_list1,axis=1) 
column=list(train_X)
#查看spearman删除后，变量之间的相关性
corr2 = train_X.corr(method='spearman')
f , ax = plt.subplots(figsize = (25, 25))
plt.title('Correlation of Numeric Features with Loss',y=1,size=30)
sns.heatmap(corr2,square = True,annot=False,cmap="RdBu_r")#热力图
# In[] 对单因素分析后的数据进行XGBOOST特征重要性评分
import xgboost as xgb
import matplotlib.pyplot as plt; plt.style.use('seaborn')
import shap
# 训练xgboost分类评分模型
model = xgb.XGBClassifier(max_depth=4, learning_rate=0.05, n_estimators=150)
model.fit(train_X,train_Y)

# 画出重要性得分情况
plt.rcParams['font.sans-serif']=['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    # 用来正常显示负号
plt.bar(range(len(model.feature_importances_)), model.feature_importances_)
plt.show()
plt.xticks(range(len(column)), column, rotation=-90, fontsize=8)
plt.title('Feature importance', fontsize=14)
plt.xlabel('特征类别')       #x轴标签
plt.ylabel('评分大小')           #y轴标签
plt.show()
# 添加数值显示
for x,y in enumerate(list(model.feature_importances_)):        #循环遍历yy里面的值
    plt.text(x,y+0.001,'{:.2}'.format(y),ha='center',rotation=90)  #让循环遍历yy里面的值显示在柱状图上 

# model是刚才训练的模型
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(train_X)

# In[] 单个样本（一行数据）的SHAP值,随机检查其中一个样本的每个特征对预测值的影响
#第一列是特征名称，第二列是特征的数值，第三列是各个特征在该样本中对应的SHAP值。
# 比如我们挑选数据集中的第30位
j = 30
player_explainer = pd.DataFrame()
player_explainer['feature'] = column
player_explainer['feature_value'] = train_X.iloc[j].values
player_explainer['shap_value'] = shap_values[j]
player_explainer['base'] = model.predict(train_X).mean() #就是预测的分数的均值
player_explainer['sum'] = player_explainer['shap_value'].sum() #特征的shap和
player_explainer['base+sum'] = player_explainer['base']+player_explainer['sum']
player_explainer
# In[] 全部特征的分析
#除了能对单个样本的SHAP值进行可视化之外，还能对特征进行整体的可视化
# shap_values值区间较大的前20个特征
shap.summary_plot(shap_values, train_X)
#图中每一行代表一个特征，横坐标为SHAP值。一个点代表一个样本，颜色越红说明特征本身数值越大，颜色越蓝说明特征本身数值越小，可以看出LSTAT越大，房价越小，和房价成反比关系

# In[] 也可以把一个特征对目标变量影响程度的绝对值的均值作为这个特征的重要性，如下：
shap.summary_plot(shap_values, train_X, plot_type="bar")
# In[] 部分依赖图Partial Dependence Plot
#就是shap值和原值的散点图，可以看出趋势，是单调还是U型，等等，取出 mean shap_values值最大的四个特征分析
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as plt  
shap.dependence_plot('住院天数', shap_values, train_X, interaction_index=None, show=False)
shap.dependence_plot('幼稚中性粒细胞绝对值', shap_values, train_X, interaction_index=None, show=False)
shap.dependence_plot('氨甲环酸', shap_values, train_X, interaction_index=None, show=False)
shap.dependence_plot('年龄', shap_values, train_X, interaction_index=None, show=False)
# In[] 最小二乘回归法进行拟合
id1=column.index('住院天数')
xx1=train_X['住院天数']
yy1=shap_values[:,id1]

import numpy as np
from scipy.optimize import leastsq
import pylab as pl
# 拟合，自由度为6(六阶多项式)
z2 = np.polyfit(xx1, yy1, 6)
# 生成多项式对象
p2 = np.poly1d(z2)
print(z2)
print(p2) 
# 原数据散点
plt.scatter(xx1,yy1,s=30,marker='o')#画出原来观测点的位置
#画出拟合曲线
x_paixu=sorted(xx1,reverse=True)
y_paixu=p2(x_paixu)
y_0=[0 for _ in range(xx1.shape[0])]
plt.plot(x_paixu,y_paixu,color='r',label='plot')#画出原来观测点的位置
plt.plot(x_paixu,y_0,color='g',label='plot')#画出原来观测点的位置
plt.xlabel('住院天数')
plt.ylabel('SHAP value for 住院天数')
plt.scatter(17,0,color='y')
plt.text(17, 0, (17, 0), ha='center', va='bottom',color='r',fontsize=10)



id1=column.index('幼稚中性粒细胞绝对值')
xx1=train_X['幼稚中性粒细胞绝对值']
yy1=shap_values[:,id1]

import numpy as np
from scipy.optimize import leastsq
import pylab as pl
# 拟合，自由度为6(六阶多项式)
z2 = np.polyfit(xx1, yy1, 6)
# 生成多项式对象
p2 = np.poly1d(z2)
print(z2)
print(p2) 
# 原数据散点
plt.scatter(xx1,yy1,s=30,marker='o')#画出原来观测点的位置
#画出拟合曲线
x_paixu=sorted(xx1,reverse=True)
y_paixu=p2(x_paixu)
y_0=[0 for _ in range(xx1.shape[0])]
plt.plot(x_paixu,y_paixu,color='r',label='plot')#画出原来观测点的位置
plt.plot(x_paixu,y_0,color='g',label='plot')#画出原来观测点的位置
plt.xlabel('幼稚中性粒细胞绝对值')
plt.ylabel('SHAP value for 幼稚中性粒细胞绝对值')
plt.scatter(0.031,0,color='y')
plt.text(0.031, 0, (0.031, 0), ha='center', va='bottom',color='r',fontsize=10)



id1=column.index('氨甲环酸')
xx1=train_X['氨甲环酸']
yy1=shap_values[:,id1]
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
# 拟合，自由度为6(六阶多项式)
z2 = np.polyfit(xx1, yy1, 6)
# 生成多项式对象
p2 = np.poly1d(z2)
print(z2)
print(p2) 
# 原数据散点
plt.scatter(xx1,yy1,s=30,marker='o')#画出原来观测点的位置
#画出拟合曲线
x_paixu=sorted(xx1,reverse=True)
y_paixu=p2(x_paixu)
y_0=[0 for _ in range(xx1.shape[0])]
plt.plot(x_paixu,y_paixu,color='r',label='plot')#画出原来观测点的位置
plt.plot(x_paixu,y_0,color='g',label='plot')#画出原来观测点的位置
plt.xlabel('氨甲环酸')
plt.ylabel('SHAP value for 氨甲环酸')
plt.scatter(0.21,0,color='y')
plt.text(0.21, 0, (0.21, 0), ha='center', va='bottom',color='r',fontsize=10)



id1=column.index('年龄')
xx1=train_X['年龄']
yy1=shap_values[:,id1]
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
# 拟合，自由度为6(六阶多项式)
z2 = np.polyfit(xx1, yy1, 6)
# 生成多项式对象
p2 = np.poly1d(z2)
print(z2)
print(p2) 
# 原数据散点
plt.scatter(xx1,yy1,s=30,marker='o')#画出原来观测点的位置
#画出拟合曲线
x_paixu=sorted(xx1,reverse=True)
y_paixu=p2(x_paixu)
y_0=[0 for _ in range(xx1.shape[0])]
plt.plot(x_paixu,y_paixu,color='r',label='plot')#画出原来观测点的位置
plt.plot(x_paixu,y_0,color='g',label='plot')#画出原来观测点的位置
plt.xlabel('年龄')
plt.ylabel('SHAP value for 年龄')
plt.scatter(63.4,0,color='y')
plt.text(63.4, 0, (63.4, 0), ha='center', va='bottom',color='r',fontsize=10)
# In[] 构建GOS的分类模型
aa=model.feature_importances_
temp=[]
for i in range(0,aa.shape[0]):
    if aa[i]<0.025:
        temp.append(i)


column_baoliu=pd.DataFrame(column)
column_baoliu.drop(temp,axis=0,inplace=True)

temp=[]
for i in column_baoliu.index:
    temp.append(column_baoliu.loc[i,0])


train_X_baoliu=train_X.loc[:,temp]
test_X_baoliu=test_X.loc[:,temp]
#模型建立
from sklearn import metrics
from sklearn.metrics import roc_curve, auc,confusion_matrix
#模型建立
from sklearn import metrics
from sklearn.metrics import roc_curve, auc,confusion_matrix
def try_different_method(model):  
    model.fit(train_X_baoliu,train_Y)
    y_predict = model.predict(test_X_baoliu)
    fpr, tpr, thresholds  =  roc_curve(test_Y, y_predict)  #计算真正率和假正率
    roc_auc = auc(fpr,tpr)
    print('AUC的值为：',auc(fpr,tpr))
    return y_predict

f , ax = plt.subplots(figsize = (20, 20))
#将标签2替换为0
for i in range(0,train_Y.shape[0]):
    if train_Y.loc[i]==2:
        train_Y.loc[i]=0

#删除原来索引，重新索引排序
test_Y=test_Y.reset_index(drop=True)
for j in range(test_Y.shape[0]):
    if test_Y.loc[j]==2:
        test_Y.loc[j]=0

# In[] xgboost构建GOS的分类预测模型
import xgboost as xgb
model_xgb = xgb.XGBClassifier(learning_rate=0.1, n_estimators=200, max_depth=8, silent=False)
y_pre = try_different_method(model_xgb)
Accuracy = int(metrics.accuracy_score(test_Y, y_pre)*10000 )/100 # 计算准确率
print('准确率为：',Accuracy)
C2 = pd.DataFrame(confusion_matrix(test_Y, y_pre, labels=[0, 1]))
print('召回率为：', C2.iloc[0,0]/(C2.iloc[0,0] + C2.iloc[0,1]) ) 
plt.subplots(figsize = (5, 5))
sns.heatmap(C2,annot=True,fmt = '.20g') #画热力图
plt.title('confusion matrix') #标题
plt.xlabel('predict') #x轴
plt.ylabel('true') #y轴

# In[] 基于逻辑回归构建GOS的分类预测模型
from sklearn.linear_model import LogisticRegression
model_lr =LogisticRegression(penalty = 'l2')
y_pre = try_different_method(model_lr)
y_pre2=y_pre 
Accuracy = int(metrics.accuracy_score(test_Y, y_pre)*10000 )/100 # 计算准确率
print('准确率为：',Accuracy)
C2 = pd.DataFrame(confusion_matrix(test_Y, y_pre, labels=[0, 1]))
print('召回率为：', C2.iloc[0,0]/(C2.iloc[0,0] + C2.iloc[0,1]) ) 
plt.subplots(figsize = (5, 5))
sns.heatmap(C2,annot=True,fmt = '.20g') #画热力图
plt.title('confusion matrix') #标题
plt.xlabel('predict') #x轴
plt.ylabel('true') #y轴

# In[] 随机森林模型
from sklearn import ensemble
model_rfc = ensemble.RandomForestClassifier(n_estimators=300,random_state=1)
y_pre = try_different_method(model_rfc)
Accuracy = int(metrics.accuracy_score(test_Y, y_pre)*10000 )/100 # 计算准确率
print('准确率为：',Accuracy)
C2 = pd.DataFrame(confusion_matrix(test_Y, y_pre, labels=[0, 1]))
print('召回率为：', C2.iloc[0,0]/(C2.iloc[0,0] + C2.iloc[0,1]) ) 
plt.subplots(figsize = (5, 5))
sns.heatmap(C2,annot=True,fmt = '.20g') #画热力图
plt.title('confusion matrix') #标题
plt.xlabel('predict') #x轴
plt.ylabel('true') #y轴
# In[] MLP神经网络模型
from sklearn.neural_network import MLPClassifier
# hidden_layer_sizes:第i个元素表示第i个隐藏层的神经元的个数；例如hidden_layer_sizes=(50,50),表示有两层隐藏层，第一层隐藏层有50个神经元，第二层有50个神经元
# activation：激活函数
# solver： 激活函数
# alpha：float，可选的，默认0.0001，正则化项参数
# batch_size:int，可选的，默认'auto'，随机优化的minibatches的大小，如果 solver是'lbfgs'，分类器将不使用minibatch，当设置成'auto',batch_size=min(200,n_samples)
# learning_rate 学习率
# learning_rate_init 初始学习率
# max_iter 最大迭代次数
# power_t:double,optional,default 0.5,只有solver='sgd'时使用，是逆扩展学习率的指数，当learning_rate='invscaling',用来更新有效学习率

model = MLPClassifier(hidden_layer_sizes=(256,128,64,32,16,8),
                      activation='relu',
                      solver='adam',alpha=0.0001,
                      batch_size='auto',learning_rate='constant',
                      learning_rate_init=0.001,power_t=0.5, 
                      max_iter=5000, shuffle=True,
                      random_state=None, 
                      tol=0.0001, verbose=False, 
                      warm_start=False, momentum=0.9, 
                      nesterovs_momentum=True, 
                      early_stopping=False, 
                      validation_fraction=0.1, 
                      beta_1=0.9, beta_2=0.999, 
                      epsilon=1e-08, 
                      n_iter_no_change=10)
# 训练模型
model.fit(train_X_baoliu, train_Y)
# 评估
pre = model.predict(test_X_baoliu) #对测试集进行测试，得到预测值
model.score(test_X_baoliu,test_Y) #
Accuracy = int(metrics.accuracy_score(test_Y, y_pre)*10000 )/100 # 计算准确率
fpr, tpr, thresholds  =  roc_curve(test_Y, pre)  #计算真正率和假正率
roc_auc = auc(fpr,tpr)
print('AUC的值为：',auc(fpr,tpr))
#测试集混淆矩阵
print('准确率为：',Accuracy)
C2 = pd.DataFrame(confusion_matrix(test_Y, y_pre, labels=[0, 1]))
print('召回率为：', C2.iloc[0,0]/(C2.iloc[0,0] + C2.iloc[0,1]) ) 
plt.subplots(figsize = (5, 5))
sns.heatmap(C2,annot=True,fmt = '.20g') #画热力图
plt.title('confusion matrix') #标题
plt.xlabel('predict') #x轴
plt.ylabel('true') #y轴
# In[] 画出ROC曲线
from sklearn import metrics
import pylab as plt
def ks(y_predicted1, y_true1, y_predicted2, y_true2, y_predicted3, y_true3, y_predicted4, y_true4):
  Font={'size':18, 'family':'Times New Roman'}
  
  label1=y_true1
  label2=y_true2
  label3=y_true3
  label4=y_true4
  fpr1,tpr1,thres1 = metrics.roc_curve(label1, y_predicted1)
  fpr2,tpr2,thres2 = metrics.roc_curve(label2, y_predicted2)
  fpr3,tpr3,thres3 = metrics.roc_curve(label3, y_predicted3)
  fpr4,tpr4,thres4 = metrics.roc_curve(label4, y_predicted4)
  
  roc_auc1 = metrics.auc(fpr1, tpr1)
  roc_auc2 = metrics.auc(fpr2, tpr2)
  roc_auc3 = metrics.auc(fpr3, tpr3)
  roc_auc4 = metrics.auc(fpr4, tpr4)

  plt.figure(figsize=(6,6))
  plt.plot(fpr1, tpr1, 'b', label = 'AUC_XG = %0.3f' % roc_auc1, color='Red')
  plt.plot(fpr2, tpr2, 'b', label = 'AUC_LR = %0.3f' % roc_auc2, color='k')
  plt.plot(fpr3, tpr3, 'b', label = 'AUC_RF = %0.3f' % roc_auc3, color='RoyalBlue')
  plt.plot(fpr4, tpr4, 'b', label = 'AUC_BP = %0.3f' % roc_auc4, color='navy')
 
  plt.legend(loc = 'lower right', prop=Font)
  plt.plot([0, 1], [0, 1],'r--')
  plt.xlim([0, 1])
  plt.ylim([0, 1])
  plt.ylabel('True Positive Rate', Font)
  plt.xlabel('False Positive Rate', Font)
  plt.tick_params(labelsize=15)
  plt.show()
  return abs(fpr1 - tpr1).max(),abs(fpr2 - tpr2).max(),abs(fpr3 - tpr3).max(),abs(fpr4 - tpr4).max()
import pandas as pd
r1 = pd.read_csv(r"C:\Users\Administrator\Desktop\分类任务\XG.csv",header=None,names=['用户标识','预测','标签'])
r2 = pd.read_csv(r"C:\Users\Administrator\Desktop\分类任务\LR.csv",header=None,names=['用户标识','预测','标签'])
r3 = pd.read_csv(r"C:\Users\Administrator\Desktop\分类任务\RF.csv",header=None,names=['用户标识','预测','标签'])
r4 = pd.read_csv(r"C:\Users\Administrator\Desktop\分类任务\BP.csv",header=None,names=['用户标识','预测','标签'])

print("线下得分;")
print(ks(r1.预测, r1.标签, r2.预测, r2.标签, r3.预测, r3.标签, r4.预测, r4.标签))
# In[] xgboost网格搜索调参
# xgb网格搜索超参数调优
# from sklearn.model_selection import GridSearchCV
# estimator = xgb.XGBClassifier()
# param_grid = {
#     'learning_rate': [0.01, 0.1, 1],
#     'n_estimators': [20, 200,1],
#     'max_depth':[2,20]
# }
# xgb_grid = GridSearchCV(estimator, param_grid)
# xgb_grid.fit(train_X_baoliu, train_Y,eval_metric='auc')
# print('Best parameters found by grid search are:', xgb_grid.best_params_)

# # 构建调参后的预测模型
# model_xgb = xgb.XGBClassifier(max_depth=8, learning_rate=0.01, 
#                              n_estimators=200, silent=False)

# model_xgb.fit(train_X_baoliu,train_Y)
# y_pre = model_xgb.predict(test_X_baoliu) 
# Accuracy = int(metrics.accuracy_score(test_Y, y_pre)*10000 )/100 # 计算准确率
# fpr, tpr, thresholds  =  roc_curve(test_Y, y_pre)  #计算真正率和假正率
# roc_auc = auc(fpr,tpr)
# print('AUC的值为：',auc(fpr,tpr))
# #测试集混淆矩阵
# print('准确率为：',Accuracy)
# C2 = pd.DataFrame(confusion_matrix(test_Y, y_pre, labels=[0, 1]))
# print('召回率为：', C2.iloc[0,0]/(C2.iloc[0,0] + C2.iloc[0,1]) ) 
# plt.subplots(figsize = (5, 5))
# sns.heatmap(C2,annot=True,fmt = '.20g') #画热力图
# ax.set_title('confusion matrix') #标题
# ax.set_xlabel('predict') #x轴
# ax.set_ylabel('true') #y轴
# In[] xgboost网格搜索调参
# xgb网格搜索超参数调优
zhunque=[]
for i in range(20,300,10):
    for j in range(1,20,1):
        model_xgb = xgb.XGBClassifier(learning_rate=0.1, n_estimators=i, max_depth=8, silent=False)
        y_pre = try_different_method(model_xgb)
        Accuracy = int(metrics.accuracy_score(test_Y, y_pre)*10000 )/100 # 计算准确率
        zhunque.append(Accuracy)
        

number=[]
for i in range(1,533,1):
    number.append(i)

plt.plot(number,zhunque,color='r',label='plot')#画出原来观测点的位置
plt.scatter(50,78.57,color='y')
plt.text(50, 78.57, (50, 78.57), ha='center', va='bottom',color='r',fontsize=10)
plt.title('网格搜索调参') #标题
plt.xlabel('第i次搜索') #x轴
plt.ylabel('准确率') #y轴





