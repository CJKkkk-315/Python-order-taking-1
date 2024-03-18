import scrapy
import requests
import csv
from selenium import webdriver
scrapy.version_info
from bs4 import BeautifulSoup
from time import sleep
head = ['招聘主题','发布日期','浏览次数']

urls = []
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
# driver = webdriver.Chrome(executable_path='C:\PYTHON接单\高校爬虫\chromedriver.exe',chrome_options=chrome_options)
# driver.get('https://job.bupt.edu.cn/frontpage/bupt/html/recruitmentinfoList.html?type=1')
# for i in range(60):
#     for j in range(1,16):
#         url = driver.find_element_by_xpath('//*[@id="listPlace"]/div[' + str(j) +']').find_element_by_class_name('left').find_element_by_tag_name('a').get_attribute('href')
#         urls.append(url)
#     a = driver.find_element_by_class_name('fPage').find_elements_by_tag_name('li')[-1].find_element_by_tag_name('a')
#     driver.execute_script("arguments[0].click();", a)
#     sleep(1)
# driver.quit()
# print(urls)
f1 = open('BEIYOU_1.csv','w',newline='')
f_csv = csv.writer(f1)
f_csv.writerow(head)
rows = []
for i in range(0,len(urls)):
    try:
        driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)
        driver.get(urls[i])
        sleep(1)
        v1 = driver.find_element_by_xpath('//*[@id="positionPlace"]/div[2]/div[1]/div[1]').text
        f = [i for i in driver.find_element_by_class_name('midInfo').find_element_by_tag_name('div').text.split(' ') if i]
        v2 = f[-2].replace('日期：','')
        v3 = f[-1].replace('浏览次数：','')
        try:
            v4 = driver.find_element_by_xpath('//*[@id="positionPlace"]/div/div[1]/div[2]/table/tbody/tr[2]/td[3]').text
        except:
            v4 = '1'
        print([v1,v2,v3,v4])
        f_csv.writerow([v1,v2,v3,v4])
        driver.quit()
    except:
        print('error')
