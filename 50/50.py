import requests
import json
import csv
from bs4 import BeautifulSoup
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
head = ['评论人昵称','星级','等级','时间','有用数','评语']
rows = []
d = {'力荐':5,'推荐':4,'还行':3,'较差':2,'很差':1}
for i in range(6):
    response = requests.get('https://movie.douban.com/subject/24753810/comments?start=' + str(i) + '&limit=100&status=P&sort=new_score',headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    for j in soup.find_all(class_ = 'comment-item'):
        try:
            v1 = j.find(name='a')['title']
            v5 = j.find(class_='vote-count').text
            v3 = j.find(class_='rating')['title']
            v2 = d[v3]
            v6 = j.find(class_='comment-content').text
            v4 = j.find(class_='comment-time')['title']
            rows.append([v1,v2,v3,v4,v5,v6])
        except:
            pass
with open('战狼.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in rows:
        try:
            f_csv.writerow(i)
        except:
            pass