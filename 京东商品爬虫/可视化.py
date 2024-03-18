import csv
import matplotlib.pyplot as plt
import jieba
plt.rcParams['font.sans-serif'] = ['SimHei']
import wordcloud
from collections import Counter
data = [i.replace('\n', '').split(',') for i in open('数据.csv').readlines()]
content = ''
for i in data:
    content += i[3]
seg_list_exact = jieba.cut(content, cut_all=False, HMM=True)
with open('stopwords.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
object_list = []
for word in seg_list_exact:
    if word not in stopwords:
        object_list.append(word)
n = len(object_list)
object_list = Counter(object_list)
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    max_words = 500,
    max_font_size = 120
)
wc.generate_from_frequencies(object_list)
plt.figure('词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
good = 0
mid = 0
bad = 0
for i in data:
    if i[-1] == '1':
        bad += 1
    elif i[-1] == '3':
        mid += 1
    else:
        good += 1
a = mid + good + bad
plt.pie(labels = [f'差评({round(bad/a*100,2)}%)',f'中评({round(mid/a*100,2)}%)',f'好评({round(good/a*100,2)}%)'],x=[bad,mid,good])
plt.title('顾客对手机的评价')
plt.show()