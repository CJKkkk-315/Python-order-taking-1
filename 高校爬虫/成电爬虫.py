import scrapy
import requests
import csv
import json
scrapy.version_info
head = ['招聘主题','发布日期','浏览次数']
f1 = open('CHENGDIAN_1.csv','w',newline='')
f_csv = csv.writer(f1)
f_csv.writerow(head)
url = 'https://yjsjob.uestc.edu.cn/coread/listeminfo.action'
for i in range(105):
    payload = {'page': i}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    for i in data['list']:
        v1 = i['title']
        v2 = i['date'].replace('年','-').replace('月','-').replace('日','')
        v3 = i['viewcount']
        try:
            f_csv.writerow([v1, v2, v3])
        except:
            pass