import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy
from PIL import Image
import wordcloud
title = []
# 循环爬取三年
for year in range(2019,2022):
    a = []
    # 将年份拼接到url上，形成不同年份的url
    url = "https://dblp.uni-trier.de/db/conf/cvpr/cvpr" + str(year) + ".html"
    # 加入headers，防止反爬
    headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
    payload = {}
    # 利用requests请求网页，获取网页html源代码
    response = requests.get(url, headers=headers, data=payload)
    # BeautifulSoup处理html字符串，使其具有结构化
    soup = BeautifulSoup(response.text,'lxml')
    # 遍历论文项，找出含有关键词的论文题目，加入title列表中
    for i in soup.find_all(class_='entry inproceedings'):
        t = i.find(class_='title').text
        if 'Classification' in t or 'classification' in t or 'CLASSIFICATION' in t:
            a.append(t)
            title.append(t)
# 将论文题目写入csv
    with open('论文题目' + str(year) + '.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        for i in a:
            f_csv.writerow([i])
    print(str(year) + '年出现的论文数量为：' + str(len(a)))
object_list = []
# 遍历论文题目，使用nltk进行分词，同时去除停用词，结果加入列表object_list中
for i in title:
    for j in i.replace('.','').split(' '):
        with open('stoplist.txt', 'r', encoding='UTF-8') as meaninglessFile:
            stopwords = set(meaninglessFile.read().split('\n'))
        stopwords.add(' ')
        #打开停用词文件，将分词成果去掉所有的停用词
        if j not in stopwords:
            object_list.append(j)
# 利用Counter函数统计不同对象出现的次数，实现词频统计
# print(Counter(object_list))
# 设置词云背景图
mask = numpy.array(Image.open('2.png'))
plt.axis('off')
plt.imshow(mask)
# 设置词云的一些参数，字体，背景，词语数量以及词语大小等
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask = mask,
    max_words = 60,
    max_font_size = 140
)
# 利用Counter对词频进行统计
res = Counter(object_list)
rows = []
# 根据频率排序
for i,j in res.items():
    rows.append([i,j])
rows.sort(key=lambda x:x[1],reverse=True)
# 写入txt文档
with open('词频统计.txt','w') as f:
    for i in rows:
        try:
            f.writelines(i[0] + '  ' +str(i[1]) + '\n')
        except:
            pass
# 设置词云参数，生成词云图像
wc.generate_from_frequencies(Counter(object_list))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

