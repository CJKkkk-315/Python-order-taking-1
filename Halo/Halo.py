import csv
import snownlp
import numpy as np
import jieba
from collections import Counter
import matplotlib.pyplot as plt
data = []
#从csv文件中读入电影评论数据
with open('你好，李焕英.csv',encoding='utf-8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row[5])
#将列名行截取掉
data = data[1:]
s = []
#数据清洗，去除无用符号
for i in range(len(data)):
    data[i].replace(' ','').replace('\n','')
#对每项字符串计算情感得分
for i in data:
    s.append(snownlp.SnowNLP(i).sentiments)
m = max(s)
#对每个评分进行最高为5的归一化处理
for i in range(len(s)):
    s[i] = s[i]/m * 5
# print(s)
dic = {0:'不喜欢',1:'不怎么喜欢',2:'一般',3:'比较喜欢',4:'非常喜欢'}
_dic = {'不喜欢':0,'不怎么喜欢':1,'一般':2,'比较喜欢':3,'非常喜欢':4}
x = ['不喜欢','不怎么喜欢','一般','比较喜欢','非常喜欢']
for i in range(len(s)):
    try:
        s[i] = dic[int(s[i])]
    except:
        pass
# print(s)
s = Counter(s)
_s = [0 for i in range(5)]
for i,j in s.items():
    try:
        _s[_dic[i]] += j
    except:
        pass
print(_s)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.pie(x=_s,labels=x)
plt.show()


