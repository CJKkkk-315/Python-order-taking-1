import wordcloud
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import numpy
from PIL import Image
f = open('数据.txt','r',encoding='utf-8')
s = f.read()
f.close()
print(s)
meaninglessFile = open('停用词库.txt', 'r', encoding='UTF-8')
stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
meaninglessFile.close()
object_list = []
seg_list_exact = jieba.cut(s, cut_all=False, HMM=True)
for word in seg_list_exact:
    if word not in stopwords:
        object_list.append(word)
print(object_list)
while '\n' in object_list:
    object_list.remove('\n')
while '\u3000' in object_list:
    object_list.remove('\u3000')
print(object_list)
wordt = Counter(object_list)
print(wordt)
mask = numpy.array(Image.open('1.png'))
plt.axis('off')
plt.imshow(mask)
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask = mask,
    max_words = 60,
    max_font_size = 100
)
print(object_list)
wc.generate_from_frequencies(Counter(object_list))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()