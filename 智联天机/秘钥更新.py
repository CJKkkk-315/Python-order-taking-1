from selenium import webdriver
from time import sleep
import csv
import os
users = ['lygsp.daili','lygsp01.daili','lygsp02.daili','lygsp03.daili','lygsp04.daili','lygsp05.daili','lygsp06.daili','lygsp07.daili','lygsp08.daili','lygsp09.daili']
passwords = ['tTXHx7KUag','Ul7Q2scThC','dHL9rm3RmC','dig9-xiBc3','@dJ1q2dNn6','xeNOUCKecO','DFen6rXWqJ','g8uOxhyrY5','4EiQjQglSu','ns1N5WLm3Z']
res = []
for f1 in range(10):
        url = 'https://cmp.zhaopin.com/#/'
        driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe')
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="sel_account"]').click()
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(users[f1])
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwords[f1])
        driver.find_element_by_xpath('//*[@id="login"]').click()
        sleep(6)
        c = []
        c.append('INNER_AUTHENTICATION=' + driver.get_cookie('INNER_AUTHENTICATION')['value'])
        c.append('ZPSSO_USER_EMPID=' + driver.get_cookie('ZPSSO_USER_EMPID')['value'])
        c.append('ZPSSO_USER_NAME=' + driver.get_cookie('ZPSSO_USER_NAME')['value'])
        c.append('ZPSSO_USER_INFO=' + driver.get_cookie('ZPSSO_USER_INFO')['value'])
        res.append('; '.join(c))
with open('cookie.txt','w') as f:
        f.write('#####'.join(res))
