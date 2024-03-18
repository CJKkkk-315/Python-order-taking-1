 # encoding=UTF-8
import random
from selenium import webdriver
from lxml import etree
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import csv

IP=['115.209.172.101','27.158.124.16','110.87.250.205','27.158.127.40','124.112.171.232'] # 此处我省略了，单引号应该是可以使用的代理IP地址，大家最好用爬虫爬取某些高质量代理网站的代理ip或者购买（很便宜）,然后用txt导入
# https://h.wandouip.com/?page=3#sec3       #https 代理IP
options = webdriver.ChromeOptions()  # 进入浏览器设置   
options.add_argument('lang=zh_CN.UTF-8')# 设置中文 
options.add_argument(  # 更换头部
        'user-agent="Chrome/10 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"')   
options.add_argument("headless")
def update_cookie(browser,dd):
    cookies = browser.get_cookies()
    # print(cookies)
    for ck1 in cookies:
        ck1['secure'] = bool(1)
        ck1['httpOnly'] = bool(1)
        # ck1['expiry']=2671373098+dd
    browser.delete_all_cookies()
    ll=len(cookies)
    for i in range(2,-1,-1):
        browser.add_cookie(cookies[i])
    return browser

def change_wind(wd,title):
    all_handles=wd.window_handles
    for handle in all_handles:
        wd.switch_to.window(handle)
        # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
        if  title in wd.page_source:
            # 如果是，那么这时候WebDriver对象就是对应该窗口，正好，跳出循环，
            wd.switch_to.window(handle)
            break
    return wd
def get_browser(url,IPN):
    # options.add_argument('-proxy-server=https://'+IP[IPN])
    browser = webdriver.Chrome(executable_path='C:\PYTHON接单\高校爬虫\chromedriver.exe',chrome_options=options)
    browser.maximize_window()
    browser.get(url)
    # browser=update_cookie(browser)
    # browser.get(url)

    return browser

def get_10_jobs_in_one_page(wd,st):
    jb=wd.find_element_by_css_selector('div[class="j_joblist"]')
    jb_list=jb.find_elements_by_css_selector('div[class="e"]')
    print(len(jb_list))
    i=st
    for x in range(st,st+10):
        a=jb_list[x].find_element_by_css_selector('a[href]')
        wd=update_cookie(wd,300) 
        # time.sleep(2)
        try:
            a.click() 
            wd=change_wind(wd,'职位信息')
            time.sleep(1)
            v1 = wd.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1').text
            v2 = wd.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]').text
            v3 = wd.find_element_by_class_name('inbox').text
            v4 = wd.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[3]/div').text
            f_csv.writerow([v1,v2,v3,v4])
            wd.close()
            wd=change_wind(wd,'前往')
            print(i)
        except:
            print('failed one job')
  
       
        i=i+1
    return wd,i


url='https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
st=0 
i=0
f = open('数据.csv','w',newline='')
f_csv = csv.writer(f)

while i<5:
    wd=get_browser(url,i)
    time.sleep(1)
    wd,st=get_10_jobs_in_one_page(wd,st)
    wd.close()
    i=i+1
 