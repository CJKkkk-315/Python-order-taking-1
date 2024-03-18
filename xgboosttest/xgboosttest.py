import xgboost as xgb
import matplotlib.pyplot  as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import sklearn.preprocessing as sp
from sklearn.metrics import accuracy_score  # 准确率
import pandas as pd
X = pd.read_excel('X.xlsx')
X.drop(columns=['date','债券代码','债券简称_x'],inplace=True)
X.dropna(axis=0,subset = ["LEV","ROA"])
c = ['bond_rate','main_rate','industry','govern_invest','enterprise nature','province','bond_type','guarantee']
for i in c:
    class_mapping = {label: idx for idx, label in enumerate(set(X[i]))}
    X[i] = X[i].map(class_mapping)+1
# X[['bond_rate','main_rate','industry','govern_invest','enterprise nature','province','bond_type']] = X[['bond_rate','main_rate','industry','govern_invest','enterprise nature','province','bond_type']].astype(int)
# X[['bond_rate','main_rate','industry','govern_invest','enterprise nature','province','bond_type']] = X[['bond_rate','main_rate','industry','govern_invest','enterprise nature','province','bond_type']].apply(LabelEncoder().fit_transform)
print(X)
Y = pd.read_excel('Y.xlsx')
Y.drop(columns=['债券代码','债券简称'],inplace=True)
# 数据集分割
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=123457)

# 算法参数
params = {
    'booster':'gbtree',
    'objective':'reg:gamma',
    'gamma':0.1,
    'max_depth':5,
    'lambda':3,
    'subsample':0.7,
    'colsample_bytree':0.7,
    'min_child_weight':3,
    'slient':1,
    'eta':0.1,
    'seed':1000,
    'nthread':4,
}

plst = list(params.items())

# 生成数据集格式
dtrain = xgb.DMatrix(X_train, y_train)
num_rounds = 300
# xgboost模型训练
model = xgb.train(plst, dtrain, num_rounds)


# 显示重要特征
xgb.plot_importance(model)
plt.show()