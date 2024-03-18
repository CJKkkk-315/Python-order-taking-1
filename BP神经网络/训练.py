# coding=UTF-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import xlrd

## 设置字符集，防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False

data = xlrd.open_workbook('train.xls')
table = data.sheets()[0]
data = []
for i in range(2,table.nrows):
    aw = []
    for j in range(table.ncols):
        aw.append(table.cell_value(i, j))
    data.append(aw)
xaxis = [str(int(i[0])) for i in data]
x = [i[1:10] for i in data]
y = [i[-1] for i in data]
x = pd.DataFrame(x)
y = pd.DataFrame(y)
data = xlrd.open_workbook('forecast.xls')
table = data.sheets()[0]
data = []
for i in range(1,table.nrows):
    aw = []
    for j in range(table.ncols):
        aw.append(table.cell_value(i, j))
    data.append(aw)
xaxist = [str(int(i[0])) for i in data]
xt = [i[1:10] for i in data]
yt = [i[-1] for i in data]
xt = pd.DataFrame(xt)
yt = pd.DataFrame(yt)

# 归一化
x_scaler = MinMaxScaler(feature_range=(-1, 1))
y_scaler = MinMaxScaler(feature_range=(-1, 1))

x = x_scaler.fit_transform(x)
y = y_scaler.fit_transform(y)
xt = x_scaler.fit_transform(xt)

# 为了后面和w进行矩阵的乘法操作
sample_in = x.T
sample_out = y.T
test_in = xt.T
# 超参
max_epochs = 60000 # 最大迭代次数
learn_rate = 0.035 #    学习率
mse_final = 6.5e-4 # 最终误差
sample_number = x.shape[0]
input_number = 9 # 输入个数
output_number = 1   # 输出个数
hidden_unit_number = 8 # 隐藏层

# 创建网格参数
# 8*3矩阵
w1 = np.random.rand(hidden_unit_number, input_number) - 0.1
# 8*1矩阵
b1 = np.random.rand(hidden_unit_number, 1) - 0.1
# 2*8矩阵
w2 = np.random.rand(output_number, hidden_unit_number) - 0.1
# 1*8矩阵
b2 = np.random.rand(output_number, 1) - 0.1


# sigmoid函数
def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))


mse_history = []
for i in range(max_epochs):
    # FP过程
    # 隐藏层输出,transpose是让列相同才能矩阵相加，第二次transpose变回原形状
    hidden_out = sigmoid(np.dot(w1, sample_in).transpose() + b1.transpose()).transpose()
    # 输出层的输出（为了简化写法，输出层不进行sogmoid激活）
    network_out = (np.dot(w2, hidden_out).transpose() + b2.transpose()).transpose()

    # 误差判断
    err = sample_out - network_out
    mse = np.average(np.square(err))
    mse_history.append(mse)
    if mse < mse_final:
        break

    # BP过程
    delta2 = -err
    delta1 = np.dot(w2.transpose(), delta2) * hidden_out * (1 - hidden_out)
    dw2 = np.dot(delta2, hidden_out.transpose())
    db2 = np.dot(delta2, np.ones((sample_number, 1)))
    dw1 = np.dot(delta1, sample_in.transpose())
    db1 = np.dot(delta1, np.ones((sample_number, 1)))
    w2 -= learn_rate * dw2
    b2 -= learn_rate * db2
    w1 -= learn_rate * dw1
    b1 -= learn_rate * db1

## 设置字符集，防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False
aw = max(mse_history)
# mse_history10 = [i/aw for i in mse_history]
# 误差曲线图
mse_history10 = np.log10(mse_history)
min_mse = min(mse_history10)

plt.plot(mse_history10)
plt.plot([0, len(mse_history10)], [min_mse, min_mse])
ax = plt.gca() # 移动坐标轴
ax.set_yticks([-2,-1,0,1,2,min_mse])
ax.set_xlabel('迭代次数')
ax.set_ylabel('误差')
ax.set_title('误差曲线')
plt.show()


# 隐藏层输出
hidden_out = sigmoid((np.dot(w1, sample_in).transpose() + b1.transpose())).transpose()
test_out = sigmoid((np.dot(w1, test_in).transpose() + b1.transpose())).transpose()
# 输出层输出
network_out = (np.dot(w2, hidden_out).transpose() + b2.transpose()).transpose()
test_out = (np.dot(w2, test_out).transpose() + b2.transpose()).transpose()
# 反转获取实际值
network_out = y_scaler.inverse_transform(network_out.T)
sample_out = y_scaler.inverse_transform(y)
test_out = y_scaler.inverse_transform(test_out.T)
print(test_out)

# fig是图像对象，axes坐标轴对象
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12,10))
# k代表颜色，marker标记
line1 = axes.plot(xaxis,network_out[:,0], 'k', marker='o',label = '预测值')
line2 = axes.plot(xaxis,sample_out[:,0], 'r', markeredgecolor='b', marker='*', markersize=9,label = '真实值')
# 图例
axes.legend()
axes.set_title('BP神经网络')

plt.show()
