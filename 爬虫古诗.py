import requests
from bs4 import BeautifulSoup
import pymysql
import json
import csv
head = ['古诗名','内容','解析']
rows = []
url = "https://so.gushiwen.cn/gushi/tangshi.aspx"
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
payload = {}
response = requests.get(url, headers=headers, data=payload)
soup = BeautifulSoup(response.text,'lxml')
#爬取唐诗300首诗名，作者及链接
for i in soup.find_all(class_='typecont'):
    for j in i.find_all(name='span'):
        try:
            v1 = j.text
            v2 = j.find(name='a')['href']
            url = v2
            #进入每个链接，获取其中的诗歌内容及解析
            response = requests.get('https://so.gushiwen.cn' + url, headers=headers, data=payload)
            soup1 = BeautifulSoup(response.text, 'lxml')
            v3 = soup1.find(class_='contyishang').find(name='p').text
            v4 = soup1.find(class_='contson').text
            rows.append([v1,v4,v3])
        except:
            print(1)

#写入csv
with open('res4.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in rows:
        try:
            f_csv.writerow(i)
        except:
            pass