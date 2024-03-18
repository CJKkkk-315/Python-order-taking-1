from sklearn.linear_model import LinearRegression as LR
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.ensemble import RandomForestRegressor as RF
from sklearn.metrics import accuracy_score
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import csv
import time
import warnings
warnings.filterwarnings("ignore")
x = []
y = []
# 打开训练集csv文件
with open('heart_train.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        # 将文件的第一列以逗号分隔，作为列表，存储为x
        x.append(row[1].split(','))
        # 将文件的第二列，也就是心跳类型存储为y
        y.append(row[2])
# 将xy去掉第一行的列名信息
x =  x[1:]
y =  y[1:]
# 将xy转换为数据框的格式，便于下面进行训练，同时新建一个yplot列表，用于下面的特征画图
x = pd.DataFrame(x)
yplot = y[::]
y = pd.DataFrame(y)
x_test = []
y_true = []
# 打开测试集，做与上述训练集相同的操作
with open('heart_test.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        x_test.append(row[1].split(','))
        y_true.append(row[2])
x_test =  x_test[1:]
y_true =  y_true[1:]
# 对测试集利用map函数将每一个心跳类型化为int型，方便后面进行比对
y_true = list(map(int,y_true))
# 同样，将数据转换为数据框的格式
x_test = pd.DataFrame(x_test)
y_true = pd.DataFrame(y_true)
# 决策树模型
start = time.time()
model = DT()
model.fit(x, y)
y_test = model.predict(x_test)
y_test = list(map(int,y_test))
y_test = pd.DataFrame(y_test)
dt = accuracy_score(y_test, y_true)
print("决策树分类准确率: ", dt)
end = time.time()
dtt = end - start
print("决策树分类用时为：")
print(dtt)
# 随机森林模型
start = time.time()
model = RF()
model.fit(x, y)
y_test = model.predict(x_test)
y_test = list(map(int,y_test))
y_test = pd.DataFrame(y_test)
rf = accuracy_score(y_test, y_true)
print("随机森林准确率: ", rf)
end = time.time()
print("随机森林用时为：")
rft = end - start
print(rft)
# 多元线性回归模型
start = time.time()
model = LR()
model.fit(x, y)
y_test = model.predict(x_test)
y_test = list(map(int,y_test))
y_test = pd.DataFrame(y_test)
lr = accuracy_score(y_test, y_true)
print("多元线性回归准确率: ", lr)
end = time.time()
lrt = end - start
print("多元线性回归用时为：")
print(lrt)
# 画出三种算法的准确率对比
num = [dt,rf,lr]
name = ['决策树准确率','随机森林准确率','线性回归准确率']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('算法性能对比')
plt.bar(name,num)
plt.show()
# 三种算法的时间对比
num = [dtt,rft,lrt]
name = ['决策树耗时','随机森林耗时','线性回归耗时']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('算法耗时对比')
plt.bar(name,num)
plt.show()
# 对训练集中数据的心跳类型特征做一个统计绘图
res = []
for i,j in Counter(yplot).items():
    res.append([i,j])
res.sort(key=lambda x:x[0])
num = []
name = ['类型0特征数量','类型1特征数量','类型2特征数量','类型3特征数量']
for i in res:
    num.append(i[1])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('心跳类型特征对比')
plt.bar(name,num)
plt.show()