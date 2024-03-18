import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
X = pd.read_excel('X.xlsx')
X.drop(columns=['date','债券代码','债券简称_x'],inplace=True)
labelname = ['bond_rate','main_rate','industry','govern_invest','enterprise nature','province','bond_type','guarantee']
for i in labelname:
    class_mapping = {label: idx for idx, label in enumerate(set(X[i]))}
    X[i] = X[i].map(class_mapping)+1
negname = ['listed','ROA','CPI','PPI','GDP']
for i in negname:
    x_bias = X[i].min() - 1
    X[i] = X[i] - x_bias
Y = pd.read_excel('Y.xlsx')
Y.drop(columns=['债券代码','债券简称'],inplace=True)
y_bias = Y['credit_spread'].min()-1
Y = Y['credit_spread'] - y_bias
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
model = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=160, silent=True, objective='reg:gamma')
model.fit(X_train, y_train)
a = model.feature_importances_
plt.rcParams['font.sans-serif']=['SimHei']
print(a)
b = X.columns.values.tolist()
plt.plot(a,b)
plt.show()
plot_importance(model)
plt.show()