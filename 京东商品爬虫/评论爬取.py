headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
import csv
import requests
import json
from time import sleep
data = []
with open('url22.csv',encoding='utf8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
payload = {}
rows = []
for d in data:

    #拼接URL，获取商品评论json格式接口
    url1 = "https://club.jd.com/comment/productPageComments.action?productId=" + d[3].replace('https://item.jd.com/','').replace('.html','') +"&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
    url2 = "https://club.jd.com/comment/productPageComments.action?productId=" + d[3].replace('https://item.jd.com/','').replace('.html','') + "&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&fold=1"
    try:
        response = requests.get(url1, headers=headers, data=payload)
        #对json格式中所需要的数据进行提取，并去除多余的无关字符
        for i in json.loads(response.text)['comments']:
            content = i['content'].replace(' ','').replace('\n','').replace('\r','')
            time = i['creationTime']
            score = str(i['score'])
            rows.append([d[0],d[2],d[1],content,time,score])
        sleep(3)
        response = requests.get(url2, headers=headers, data=payload)
        for i in json.loads(response.text)['comments']:
            content = i['content'].replace(' ', '').replace('\n', '').replace('\r', '')
            time = i['creationTime']
            score = str(i['score'])
            rows.append([d[0], d[2], d[1], content, time, score])
        print(len(rows))
        sleep(3)
    except:
        print(url1)
        print(url2)
with open('数据22.csv','a+',newline='') as f:
    f_csv = csv.writer(f)
    for i in rows:
        try:
            f_csv.writerow(i)
        except:
            pass