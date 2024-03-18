import requests
import wordcloud
import jieba
import re
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import numpy
from PIL import Image
import csv
import sqlite3
import tkinter as tk
#  https://www.chinanews.com.cn

url = 'https://www.chinanews.com.cn'
n = 1
#创建一个模拟浏览器的代理头，防止被反爬
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
#通过request请求网页，获取html
response = requests.get(url,headers=headers)
response.encoding = 'UTF-8'
#通过BeautifulSoup处理html，方便我们进行关键信息的提取
soup = BeautifulSoup(response.text,'lxml')
link = str(soup.find(class_='nav_navcon').find(name='a')['href'])
url = 'https://www.chinanews.com.cn/' + link
response = requests.get(url,headers=headers)
response.encoding = 'UTF-8'
href = []
#创建一个正则匹配模式，方便后面进行数据的清理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
#对新闻目录进行爬取，获得每个新闻的链接
for i in BeautifulSoup(response.text,'lxml').find(class_='content_list').find_all(name='li'):
    try:
        href.append(['https://www.chinanews.com.cn' + i.find(class_='dd_bt').find(name='a')['href']])
    except:
        pass
# print(href)
content = []
#对爬取到的所有新闻链接进行内容的爬取，爬满10条为止
for i in href:
    if len(content) == 10:
        break
    response = requests.get(i[0], headers=headers)
    response.encoding = 'UTF-8'
    #新闻页面共有2种html形式，若其中一种获取失败则换另一种进行获取
    try:
        try:
            soup = BeautifulSoup(response.text,'lxml')
            s = soup.find(class_='left_zw').text.replace('\u3000','')
            s = re.sub(pattern,'',s)
            content.append(s)
        except:
            soup = BeautifulSoup(response.text, 'lxml')
            s = soup.find(class_='content_desc').text.replace('\u3000', '')
            s = re.sub(pattern, '', s)
            content.append(s)
    except:
        pass
#将爬取到的新闻内容对应上前面爬取的新闻链接
for i in range(len(content)):
    href[i].append(content[i])
#只取前面10条方便我们进行分析
href = href[:10]
object_list = []
for i in href:
    #对每一条新闻内容，进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(i[1], cut_all=False, HMM=True)
    with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    #打开停用词文件，将分词成果去掉所有的停用词
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
#打开我们预先选择好的词云背景图
mask = numpy.array(Image.open(str(n) + '.png'))
plt.axis('off')
plt.imshow(mask)
#设置词云的一些参数，字体，背景，词语数量以及词语大小等
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask = mask,
    max_words = 60,
    max_font_size = 100
)
#利用Counter对词频进行统计
res = Counter(object_list)
rows = []
for i,j in res.items():
    rows.append([i,j])
#设置词云参数，生成词云图像
print(object_list)
wc.generate_from_frequencies(Counter(object_list))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
head = ['词语','频率']
#对词频进行排序，方便我们后续有序的写入文件中
rows.sort(key=lambda x:x[1],reverse=True)
x = []
y = []
for i in rows[:20]:
    x.append(i[0])
    y.append(i[1])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.bar(x,y)
plt.show()
print(rows)
#写入csv文件
with open('词频分析.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in rows:
        try:
            f_csv.writerow(i)
        except:
            pass

