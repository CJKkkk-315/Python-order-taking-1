import csv
from collections import Counter
import matplotlib.pyplot as plt
import wordcloud
import jieba
import numpy
from PIL import Image
y = []
res = []
with open('豆瓣.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        #通过字符串分隔，找到每本书的发表年份
        y.append(row[3].split('-')[0].replace(' ',''))
for i in Counter(y[1:]).items():
    try:
        if int(i[0]) >= 2015:
            res.append(list(i))
    except:
        pass
year = []
num = []
#对年份进行排序，并分类
print(res)
for i in sorted(res,key=lambda x:x[0]):
    year.append(i[0])
    num.append(i[1])
#画出图片
plt.plot(year,num)
plt.show()
data = []
with open('豆瓣.csv',encoding='gbk')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
object_list = []
for i in data:
    #对每一条新闻内容，进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(i[1], cut_all=False, HMM=True)
    #打开停用词文件，将分词成果去掉所有的停用词
    for word in seg_list_exact:
        object_list.append(word)
#打开我们预先选择好的词云背景图
mask = numpy.array(Image.open('1.png'))
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