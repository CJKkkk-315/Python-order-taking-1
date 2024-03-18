from sklearn.ensemble import RandomForestRegressor as RF
import pandas as pd
from sklearn.metrics import accuracy_score
data = pd.read_csv('res.csv')
x = data.drop(columns=['popularity'])
y = data['popularity']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
model = RF()
model.fit(X_train, y_train)
rf = accuracy_score(X_test, y_test)
print("随机森林准确率: ", rf)
importances = forest.feature_importances_
print(importances)