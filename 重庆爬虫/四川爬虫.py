import requests
from bs4 import BeautifulSoup
import csv
import selenium
import scrapy
for i in range(2017,2022):
    data = []
    response = requests.get('https://zs.sicnu.edu.cn/(S(ujd05ibm5531nqcxv34wp2n3))/SubPage.aspx?Id=' + str(i))
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'lxml')
    # print(soup)
    t = ['年份,省份,科类,录取最低分,录取最高分,平均分,录取人数,备注']
    t = t[0].split(',')
    data.append(t)
    for i in soup.find_all(class_='name'):
        t = []
        sw = i.find(id='number')
        for h in sw:
            t.append(h.text)
with open('四川.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        f_csv.writerow(i)