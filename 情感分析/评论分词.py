import csv
import jieba
import jieba.posseg
import numpy as np
from pandas import DataFrame
import pandas as pd
data = []
with open('评论数据（清理后）.csv',encoding='gbk')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
for i in data:
    # 进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(i[6], cut_all=False, HMM=True)
    with open('stoplist.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    # 打开停用词文件，将分词成果去掉所有的停用词
    i[6] = []
    for word in seg_list_exact:
        if word not in stopwords:
            i[6].append(word)
#对评论的分词进行词性分析
for i in data:
    seg_list_exact = jieba.posseg.cut(''.join(i[6]))
    i[6] = []
    for word in seg_list_exact:
        i[6].append(list(word)[0] + ',' + list(word)[1])
dic = {'评论id':[],'词语':[],'词语id':[]}
#构造评论id，词语，词语位置id
for i in data:
    for j in range(len(i[6])):
        dic['评论id'].append(i[1])
        dic['词语'].append(i[6][j])
        dic['词语id'].append(j)
df = DataFrame(dic)
print(df)
#合并评论id，评论中词的id，词，词性
h = []
for i,j,k in zip(list(df['评论id']),list(df['词语']),list(df['词语id'])):
    h.append([i,k,j.split(',')[0],j.split(',')[1]])
print(h)
#提取含有名词类的评论
ndata = []
for i in data:
    for j in i[-1]:
        if j.split(',')[1] == 'n':
            ndata.append(i[1])
            break
print(ndata)
