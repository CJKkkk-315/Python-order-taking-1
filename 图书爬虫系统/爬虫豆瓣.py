import requests
from bs4 import BeautifulSoup
import pymysql
import json
import csv
from selenium import webdriver
head = ['序号','书名','作者','出版年份','链接']
rows = []
for page in range(0,150,15):
    driver = webdriver.Opera()
    driver.get('https://book.douban.com/subject_search?search_text=python&cat=1001&start=' + str(page))
    num = 0
    #获取豆瓣图书列表
    for i in driver.find_elements_by_class_name('eJWSlY'):
        try:
            v1 = i.find_element_by_class_name('detail').find_element_by_class_name('title').text
            try:
                #爬取每个图书的作者及时间日期
                    v2 = str(i.find_element_by_class_name('detail').find_element_by_class_name('abstract').text).split('/')[0]
                    v4 = str(i.find_element_by_class_name('detail').find_element_by_class_name('title-text').get_attribute('href'))
                    for i in str(i.find_element_by_class_name('detail').find_element_by_class_name('abstract').text).split('/'):
                        if '-' in i:
                            v3 = i
                            break
            except:
                    v2 = '暂无作者'
                    v3 = '2021-1'
            v0 = num
            num += 1
            rows.append([v0,v1,v2,v3,v4])
        except:
            pass
    driver.quit()
#写入csv
with open('豆瓣.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in rows:
        try:
            f_csv.writerow(i)
        except:
            pass