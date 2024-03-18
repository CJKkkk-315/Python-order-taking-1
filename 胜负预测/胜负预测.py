# 采用sklearn中的多元线性回归模型
from sklearn.linear_model import LinearRegression as LR
import pandas as pd
import csv
# 从文件中读入训练集
df = pd.read_csv('train.csv')
# 查看一下数据中是否有空值需要清理
# print(np.isnan(df).any())
# 清除所有带有空值的数据
df.dropna(inplace=True)
# Teamid对我们训练没有帮助，删除它
del df['Team_id']
# y是胜负的结果，将其单独作为一个数据框
y = df['y']
# 除了y以外的剩下的作为x，作为多元输入的变量，作为一个数据框
del df['y']
x = df
# 初始化多元线性回归模型为model
model = LR()
# x作为输入，y作为输出进行训练
model.fit(x, y)
# 打开测试集，将测试集的数据全部输入到列表tests中
tests = []
with open('test.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        tests.append(row[1:])
# 去除列名行
tests = tests[1:]
# 清洗测试集数据，若有空值，用0填充
for i in range(len(tests)):
    for j in range(len(tests[i])):
        if tests[i][j] == '':
            tests[i][j] = 0
# 由于读入以后数据均为str类型，将其全部转为float类型，方便我们输入模型
for i in range(len(tests)):
    tests[i] = list(map(float,tests[i]))
# 将测试集输入刚才训练好的模型
test_pre = model.predict(tests)
# 利用数据框搭载预测的结果
predictY = pd.DataFrame(test_pre)
# 输出到csv文件中
predictY.to_csv('D:\Results_1.csv', encoding = 'utf-8', index=False , header=False)