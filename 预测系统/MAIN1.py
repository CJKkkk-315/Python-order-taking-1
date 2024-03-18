import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
import seaborn as sns
data_all = pd.read_excel(r'工作簿3-预测数据.xlsx')
# In[] 分析数据，根据标签查看数据分布是否均衡
    
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

# In[] 缺失值填补  
#查看训练集中的特征缺失情况  
missing=train_X.isnull().sum().reset_index().rename(columns={0:'missNum'})
# 计算缺失比例
missing['missRate']=missing['missNum']/train_X.shape[0]
# 按照缺失率排序显示
miss_analy=missing[missing.missRate>0].sort_values(by='missRate',ascending=False)# miss_analy 存储的是每个变量缺失情况的数据框

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


# In[] #填补后查看测试集中的特征缺失情况  
missing=test_X.isnull().sum().reset_index().rename(columns={0:'missNum'})
# 计算缺失比例
missing['missRate']=missing['missNum']/test_X.shape[0]
# 按照缺失率排序显示
miss_analy=missing[missing.missRate>0].sort_values(by='missRate',ascending=False)# miss_analy 存储的是每个变量缺失情况的数据框


# In[] SMOTE过采样，全称是Synthetic Minority Oversampling Technique，即合成少数类过采样技术
from imblearn.over_sampling import SMOTE
X_resampled_smote, y_resampled_smote = SMOTE().fit_resample(train_X, train_Y)


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

# In[] 对单因素分析后的数据进行XGBOOST特征重要性评分
import xgboost as xgb
import matplotlib.pyplot as plt; plt.style.use('seaborn')
import shap
# 训练xgboost分类评分模型
model = xgb.XGBClassifier(max_depth=4, learning_rate=0.05, n_estimators=150)
model.fit(train_X,train_Y)


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

#图中每一行代表一个特征，横坐标为SHAP值。一个点代表一个样本，颜色越红说明特征本身数值越大，颜色越蓝说明特征本身数值越小，可以看出LSTAT越大，房价越小，和房价成反比关系

# In[] 也可以把一个特征对目标变量影响程度的绝对值的均值作为这个特征的重要性，如下：

# In[] 部分依赖图Partial Dependence Plot
#就是shap值和原值的散点图，可以看出趋势，是单调还是U型，等等，取出 mean shap_values值最大的四个特征分析
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

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


pd.set_option('display.max_columns', None)
model_xgb = xgb.XGBClassifier(learning_rate=0.1, n_estimators=i, max_depth=8, silent=False)
print(train_X_baoliu.columns)
print(test_X_baoliu[0:5])
model_xgb.fit(train_X_baoliu,train_Y)
model_xgb.get_booster().save_model('0001.model')
y_predict = model_xgb.predict(test_X_baoliu[0:5])
print(y_predict)
xlf_new = xgb.Booster() #init model
xlf_new.load_model("0001.model") # load data
data_test = xgb.DMatrix(test_X_baoliu[0:5])
pred_new = xlf_new.predict(data_test)
print(pred_new)



