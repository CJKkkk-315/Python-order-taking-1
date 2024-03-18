headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
import csv
import requests
import json
from time import sleep
data = []
with open('URL（去重）.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        #通过字符串分隔，找到每本书的发表年份
        data.append(row)
payload = {}

for d in data:
    print(d)
    rows = []
    #拼接URL，获取商品评论json格式接口
    for page in range(20):
        url = "https://club.jd.com/comment/productPageComments.action?productId=" + d[3].replace('https://item.jd.com/','').replace('.html','') +"&score=1&sortType=5&page="+ str(page) +"&pageSize=10&isShadowSku=0&fold=1"
        sleep(3)
        response = requests.get(url, headers=headers, data=payload)
        js = json.loads(response.text)
        all = js['productCommentSummary']['commentCountStr']
        if '万' in all:
            all = all.replace('万','').replace('+','')
            all = str(float(all)*10000)
        else:
            all = all.replace('+','')
        allpoor = js['productCommentSummary']['poorCountStr']
        #对json格式中所需要的数据进行提取，并去除多余的无关字符
        if not js['comments']:
            sleep(3)
            break
        for i in js['comments']:
            content = i['content'].replace(' ','').replace('\n','').replace('\r','')
            time = i['creationTime']
            id = i['referenceId']
            try:
                recontent = i['replies'][0]['content']
                retime = i['replies'][0]['creationTime']
            except:
                # print(url)
                recontent = '无'
                retime = '无'
            rows.append([d[1],d[0],d[2],all,allpoor,id,content,time,recontent,retime])

    with open('京东.csv','a+',newline='') as f:
        f_csv = csv.writer(f)
        for i in rows:
            try:
                f_csv.writerow(i)
            except:
                print(i)