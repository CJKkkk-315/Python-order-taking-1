import requests

from json import JSONDecoder
from time import sleep
import os
import csv
import datetime
ext='.jpg'
ext1= '.png'
datas = []
files = [f for f in os.listdir() if os.path.isfile(f) and (os.path.splitext(f)[1]==ext or os.path.splitext(f)[1]==ext1)]
for file in files:
    sleep(1)
    data = []
    http_url = "https://api-cn.faceplusplus.com/cardpp/v1/ocridcard"

    key = "ldWEQHwqnYPbsdxhyZsCdbCBjg_HBwY3"

    secret = "uXVD1B70rgyUuLHcTZhcIlusLaIAgaJw"

    imgpath = file

    data1 = {"api_key": key, "api_secret": secret, "legality": 0}

    files = {"image_file": open(imgpath, "rb")}

    response = requests.post(http_url, data=data1, files=files)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    # print(req_dict)
    print(req_dict)
    people_message = req_dict['cards'][0]  # 不加[0]的话，返回的是列表内有一个字典，形式为[{}]，加入[0]，则是一个字典

    # print(people_message)

    data.append(people_message['name'])

    data.append(people_message['gender'])

    data.append(people_message['race'])

    data.append(people_message['birthday'])

    data.append('\t' + people_message['id_card_number'])

    data.append(people_message['address'])
    print(data)
    datas.append(data)
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in datas:
        f_csv.writerow(i)