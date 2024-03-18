import pandas as pd
from sklearn import metrics
from collections import Counter
import matplotlib.pyplot as plt
df = pd.read_csv("spamham.csv", encoding='latin')#因为是英文文本，编码统一为latin防止乱码
df = df.dropna(how='any')
plt.bar(['ham','spam'],[i[1] for i in [[i,j] for i,j in Counter(df['type'].values.tolist()).items()]])
plt.show()
#基于词频的文本向量
from sklearn.feature_extraction.text import CountVectorizer
vectorizer1 = CountVectorizer(binary=True)
X1 = vectorizer1.fit_transform(df.Text.astype('U'))
print(X1)
y = df.type
from sklearn.model_selection import train_test_split
#将文件数据82开 分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.20, random_state=100)
print ("训练数据中的样本个数: ", X_train.shape[0], "测试数据中的样本个数: ", X_test.shape[0])
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier as DT
# 使用决策树进行分类
dt = DT()
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
print("召回率: ", accuracy_score(y_test, y_pred))
print("查准率: ", metrics.precision_score(y_test, y_pred, average="macro"))
print("F1: ", metrics.f1_score(y_test, y_pred, average="macro"))
