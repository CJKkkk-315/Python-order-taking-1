import csv
import re
import jieba.posseg
import numpy as np
import pandas as pd
data = []
rows = []
#读入CSV
with open('评论数据.csv',encoding='gbk')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if row[0] == '用户昵称':
            continue
        rows.append(row)
# print(len(rows))
#数据去重
for i in rows:
    if i not in data:
        data.append(i)
# print(len(data))
for i in data:
    #去除掉数字，英文，和所要求的关键词语
    i[6] = re.sub('[a-zA-Z]','',i[6])
    i[6] = re.sub('[\d]', '', i[6])
    i[6].replace('京东','').replace('美的','').replace('电热水器','')
#

with open('评论数据（清理后）.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        try:
            f_csv.writerow(i)
        except:
            pass

