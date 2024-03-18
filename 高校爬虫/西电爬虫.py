import requests
from bs4 import BeautifulSoup
import csv
head = ['招聘主题','发布日期','浏览次数']
f1 = open('XIDIAN_1.csv','w',newline='')
f_csv = csv.writer(f1)
f_csv.writerow(head)
for i in range(731652,734449):
    try:
        response = requests.get('https://job.xidian.edu.cn/campus/view/id/' + str(i))
        soup = BeautifulSoup(response.text,'lxml')
        v1 = soup.find(class_='title-message').find(name='h5').text
        v2 = soup.find(class_='share').find_all(name='li')[0].text.split(' ')[0].replace('发布时间：','')
        v3 = soup.find(class_='share').find_all(name='li')[1].text.replace('浏览次数：','')
        f_csv.writerow([v1,v2,v3])
    except:
        pass