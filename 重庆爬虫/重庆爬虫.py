import requests
from bs4 import BeautifulSoup
import csv
import selenium
import scrapy
data = []
response = requests.get('https://zsbxt.cqnu.edu.cn/index_lnlqcj.php?province1=21&kl1=02&kslx1=01&pc1=&major_id=104&at=single_major')
response.encoding = 'gbk'
soup = BeautifulSoup(response.text,'lxml')
# print(soup)
t = ['序号,年份,省份,科类,考试类型,专业,录取批次,省控线,录取最低分,最低分位次,录取最高分,平均分,最低分差分差,平均分分差,录取人数,备注']
t = t[0].split(',')
data.append(t)
for i in soup.find_all(class_='trbg'):
    t = []
    for j in i.find_all(name='td'):
        t.append(j.text.replace('\r','').replace('\n','').replace('\t','').replace(' ',''))
    if len(t) > 1:
        data.append(t)
with open('本科.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        f_csv.writerow(i)