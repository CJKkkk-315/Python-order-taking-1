import csv
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import wordcloud
import numpy
from PIL import Image
#合并正负面词语
with open("正面情感词语（中文）.txt", "r",encoding='utf-8') as f:  # 打开文件
    data = f.readlines()  # 读取文件
cdata = []
for i in range(len(data)):
    if data[i].replace('\n','').replace(' ',''):
        cdata.append(data[i].replace('\n','').replace(' ',''))
with open("正面评价词语（中文）.txt", "r",encoding='utf-8') as f:  # 打开文件
    data = f.readlines()  # 读取文件
for i in range(len(data)):
    if data[i].replace('\n','').replace(' ','') and data[i].replace('\n','').replace(' ','') not in cdata:
        cdata.append(data[i].replace('\n','').replace(' ',''))
pos = []
pos = cdata[::]
with open("负面情感词语（中文）.txt", "r",encoding='utf-8') as f:  # 打开文件
    data = f.readlines()  # 读取文件
cdata = []
for i in range(len(data)):
    if data[i].replace('\n','').replace(' ',''):
        cdata.append(data[i].replace('\n','').replace(' ',''))
with open("负面评价词语（中文）.txt", "r",encoding='utf-8') as f:  # 打开文件
    data = f.readlines()  # 读取文件
for i in range(len(data)):
    if data[i].replace('\n','').replace(' ','') and data[i].replace('\n','').replace(' ','') not in cdata:
        cdata.append(data[i].replace('\n','').replace(' ',''))
neg = []
neg = cdata[::]
data = []
#读入评论数据
with open('评论数据（清理后）.csv',encoding='gbk')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
sentiment = []
no = []
#载入否定词
with open('否定词.csv',encoding='utf-8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        no.append(row[0])
no = no[1:]
posword = []
negword = []
#对评论进行分词
for i in data:
    o = []
    o1 = []
    score = 0
    seg_list_exact = jieba.cut(i[6], cut_all=False, HMM=True)
    with open('stoplist.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    for word in seg_list_exact:
        if word not in stopwords:
            o.append(word)
    #将分词结果与正负面词语进行对比，同时进行否定修正
    for j in o:
        s = 1
        if j in pos:
            for n in no:
                if n in j:
                    s = -1
                    break
            score += s
            posword.append(j)
        elif j in neg:
            for n in no:
                if n in j:
                    s = -1
                    break
            score += -s
            negword.append(j)
        o1.append(j)
    sentiment.append([score])
# print(sentiment)
cdata = []
for i,j in zip(data,sentiment):
    if j[0] > 0:
        i.append('pos')
        cdata.append(i)
    elif j[0] < 0:
        i.append('neg')
        cdata.append(i)
# print(cdata)
head = ['用户昵称','商品id','评分','商品尺寸','商品颜色','评论时间','评论内容','评论类型']
with open('评论数据（分析后）.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in cdata:
        try:
            f_csv.writerow(i)
        except:
            pass
#打开我们预先选择好的词云背景图
    mask = numpy.array(Image.open('1.png'))
    #设置词云的一些参数，字体，背景，词语数量以及词语大小等
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        mask = mask,
        max_words = 60,
        max_font_size = 100
    )
    #设置词云参数，生成词云图像
    wc.generate_from_frequencies(Counter(posword))
    wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
    plt.figure('正面词云')
    plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0)
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    mask = numpy.array(Image.open('1.png'))
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        mask = mask,
        max_words = 60,
        max_font_size = 100
    )
    wc.generate_from_frequencies(Counter(negword))
    wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
    plt.figure('负面词云')
    plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0)
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()
# print(posword)
# print(negword)
# print(data)

