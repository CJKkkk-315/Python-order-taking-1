# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
s = '中华田园犬、哈士奇、京巴、藏獒、松狮、金毛、德国牧羊犬、雪纳瑞、大麦町犬、博美犬、吉娃娃、苏格兰牧羊犬、萨摩耶、可卡、拉布拉多犬、比熊、贵宾犬、马尔济斯、比利时猎犬、泰迪熊犬、边境牧羊犬、阿拉斯加、猎狐梗'
title1 = s.split('、')
s = '暹罗猫布偶猫苏格兰折耳猫英国短毛猫波斯猫俄罗斯蓝猫美国短毛猫异国短毛猫挪威森林猫孟买猫缅因猫埃及猫伯曼猫斯芬克斯猫缅甸猫阿比西尼亚猫新加坡猫索马里猫土耳其梵猫美国短尾猫中国狸花猫西伯利亚森林猫日本短尾猫巴厘猫土耳其安哥拉猫褴褛猫东奇尼猫马恩岛猫柯尼斯卷毛猫奥西猫沙特尔猫德文卷毛猫呵叻猫美国刚毛猫重点色短毛猫哈瓦那棕猫波米拉猫塞尔凯克卷毛猫拉邦猫美国卷毛猫东方猫欧洲缅甸猫'
title2 = s.split('猫')
title2 = [i + '猫' for i in title2 if i]
print(title2)
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
data = []
for t in title1:
    print(t)
    content = []
    url = 'https://baike.baidu.com/item/' + t
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text)
    if soup.find(class_='lemmaWgt-subLemmaListTitle'):
        href = soup.find(class_='para').find(name = 'a').get('href')
        response = requests.get('https://baike.baidu.com' + href, headers=headers)
        soup = BeautifulSoup(response.text)
        for i in soup.find_all(class_='para'):
            content.append(i.text.replace('\n',''))
        try:
            img = 'https://baike.baidu.com' + soup.find(class_='summary-pic').find(name='a').get('href')
        except:
            pass
    else:
        for i in soup.find_all(class_='para'):
            content.append(i.text.replace('\n',''))
        try:
            img = 'https://baike.baidu.com' + soup.find(class_='summary-pic').find(name='a').get('href')
        except:
            pass
    data.append(['宠物狗',t,'\n'.join(content),img])
for t in title2:
    print(t)
    content = []
    url = 'https://baike.baidu.com/item/' + t
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text)
    if soup.find(class_='lemmaWgt-subLemmaListTitle'):
        href = soup.find(class_='para').find(name = 'a').get('href')
        response = requests.get('https://baike.baidu.com' + href, headers=headers)
        soup = BeautifulSoup(response.text)
        for i in soup.find_all(class_='para'):
            content.append(i.text.replace('\n',''))
        try:
            img = 'https://baike.baidu.com' + soup.find(class_='summary-pic').find(name='a').get('href')
        except:
            pass
    else:
        for i in soup.find_all(class_='para'):
            content.append(i.text.replace('\n',''))
        try:
            img = 'https://baike.baidu.com' + soup.find(class_='summary-pic').find(name='a').get('href')
        except:
            pass
    data.append(['宠物猫',t,'\n'.join(content),img])
with open('res.csv','w',newline='',encoding='utf-8') as f:
    f_csv = csv.writer(f)
    for i in data:
        if i[1]:
            f_csv.writerow(i)
