# coding:utf-8
import requests
import json
import csv
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
d = []
data = []
for i in range(64):
    d = d + json.loads(requests.get("http://www.游新疆.com/api/res/api/scenic/getApiScenicList?siteCode=site688790&crowd=&level=&region=&keyword=&areaSiteSwitch=&sortType=&lng=119.30309&lat=26.00308&currPage=" + str(i) + "&pageSize=10",headers=headers).text)['datas']
    print(i)
for i in d:
    data.append([i['id'],i['nane'],i['level'],i['video'],','.join(i['theme'])])
for i in data:
    i.append(','.join(json.loads(requests.get("https://www.xn--efvu3ql9f.com/api/res/api/scenic/getApiScenicInfo?siteCode=site688790&id=" + str(i[0]),headers=headers).text)['data']['crowd']))
    print(i)
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        try:
            f_csv.writerow(i[1::])
        except:
            pass
