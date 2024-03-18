from selenium import webdriver
from time import sleep
import csv
import os
users = ['lygsp.daili','lygsp01.daili','lygsp02.daili','lygsp03.daili','lygsp04.daili','lygsp05.daili','lygsp06.daili','lygsp07.daili','lygsp08.daili','lygsp09.daili']
passwords = ['tTXHx7KUag','Ul7Q2scThC','dHL9rm3RmC','dig9-xiBc3','@dJ1q2dNn6','xeNOUCKecO','DFen6rXWqJ','g8uOxhyrY5','4EiQjQglSu','ns1N5WLm3Z']
data = []
res = []
ext='.csv'
files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1]==ext]
file = files[0]
with open(file,encoding="gbk")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
companys = [[] for i in range(10)]
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
full = {'lygsp.daili':0,'lygsp01.daili':0,'lygsp02.daili':0,'lygsp03.daili':0,'lygsp04.daili':0,'lygsp05.daili':0,'lygsp06.daili':0,'lygsp07.daili':0,'lygsp08.daili':0,'lygsp09.daili':0}
q = len(data)//10
for i in range(len(data)):
    companys[i%10].append(data[i])
f1 = 0
b1 = 0
while f1 < 10:
    try:
        print(users[f1])
        if full[users[f1]] == 1:
            if sum(full.values()) == 10:
                break
            f1 += 1
            continue
        url = 'https://cmp.zhaopin.com/#/'
        driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe',chrome_options=chrome_options)
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="sel_account"]').click()
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(users[f1])
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwords[f1])
        driver.find_element_by_xpath('//*[@id="login"]').click()
        allHandles1 = driver.window_handles
        js = 'window.open("https://cmp.zhaopin.com/#/myCustomerNew")'
        driver.execute_script(js)
        allHandles2 = driver.window_handles
        newhandle = [handle for handle in allHandles2 if handle not in allHandles1]
        driver.switch_to.window(newhandle[0])
        sleep(10)
        num = int(driver.find_element_by_xpath('//*[@id="my-customer2"]/div[4]/div[1]/div[1]/span[2]/span[1]').text.split(' (')[1].replace(')', ''))
        print(num)
        driver.close()
        allHandles1 = driver.window_handles
        driver.switch_to.window(allHandles1[0])
        js = 'window.open("https://cmp.zhaopin.com/#/customerEntering");'
        driver.execute_script(js)
        allHandles2 = driver.window_handles
        newhandle = [handle for handle in allHandles2 if handle not in allHandles1]
        driver.switch_to.window(newhandle[0])
        sleep(6)
        js0 = "document.getElementsByClassName('el-cascader__label')[0].click()"
        js1 = "document.getElementsByClassName('el-cascader-menu')[1].getElementsByTagName('li')[9].click()"
        js2 = "document.getElementsByClassName('el-cascader-menu')[2].getElementsByTagName('li')[7].click()"
        while True:
            try:
                driver.execute_script(js0)
                driver.execute_script(js1)
                driver.execute_script(js2)
                break
            except:
                pass
        print([len(i) for i in companys])
        for i in range(len(companys[f1])):
            if num <= 0:
                full[users[f1]] = 1
                if f1 == 9:
                    f1 = -1
                companys[f1+1] += companys[f1][i:]
                break
            try:
                companyname = companys[f1][i][0].replace('（','(').replace('）',')')
                if len(companyname) < 5:
                    res.append(companys[f1][i][::])
                    continue
                driver.find_element_by_xpath('//*[@id="custName"]/div/div/input').clear()
                driver.find_element_by_xpath('//*[@id="custName"]/div/div/input').send_keys(companyname)
                driver.find_element_by_xpath('//*[@id="custName"]/div/button').click()
                sleep(3)
                target = driver.find_element_by_xpath('//*[@id="entering"]/div/div[5]/div[2]/div[3]/table/tbody').find_element_by_tag_name('tr').find_element_by_tag_name('span').text
                if target == companyname:
                    ad = driver.find_element_by_xpath('//*[@id="address"]/div/div/input').get_attribute('value')
                    try:
                        if '连云港' in ad or ad[:3] == '连云港' or ad[:3] == '连云区' or ad[:3] == '海州区' or ad[:3] == '连云区' or ad[:3] == '赣榆区' or ad[
                                                                                                       :3] == '灌南县' or ad[
                                                                                                                       :3] == '东海县' or ad[
                                                                                                                                       :3] == '灌云县' or ad[
                                                                                                                                                       :6] == '江苏省连云港' or ad[
                                                                                                                                                                          :5] == '江苏连云港':
                            flag = ''
                        else:
                            flag = '非连云港地区'
                    except:
                        flag = '非连云港地区'
                    sell = driver.find_element_by_xpath('//*[@id="entering"]/div/div[5]/div[2]/div[3]/table/tbody').find_elements_by_tag_name('td')[3].text
                    lasttime = driver.find_element_by_xpath('//*[@id="entering"]/div/div[5]/div[2]/div[3]/table/tbody').find_elements_by_tag_name('td')[6].text
                    try:
                        js = "document.getElementsByTagName('table')[5].getElementsByTagName('td')[10].getElementsByTagName('div')[2].click()"
                        driver.execute_script(js)
                        num -= 1
                        sleep(5)
                    except:
                        pass
                else:
                    driver.find_element_by_xpath('//*[@id="entering"]/div/div[4]/button').click()
                    num -= 1
                    sleep(2)
                    sell = '无'
                    lasttime = ''
                    flag = ''
                companys[f1][i].append(users[f1])
                companys[f1][i].append(sell)
                companys[f1][i].append(lasttime)
                companys[f1][i].append(flag)
                # print(i)
            except:
                print('bbb')
                sell = '无'
                lasttime = ''
                flag = ''
                sleep(3)
                companys[f1][i].append(users[f1])
                companys[f1][i].append(sell)
                companys[f1][i].append(lasttime)
                companys[f1][i].append(flag)
                print(companys[f1][i][::])
            res.append(companys[f1][i][::])
        driver.quit()
        f1 += 1
        print(full)
    except:
        print('意外')
        with open('res.csv', 'w', newline='') as f:
            f_csv = csv.writer(f)
            for i in res:
                try:
                    f_csv.writerow(i)
                except:
                    print(i)
index = {'lygsp.daili':0,'lygsp01.daili':1,'lygsp02.daili':2,'lygsp03.daili':3,'lygsp04.daili':4,'lygsp05.daili':5,'lygsp06.daili':6,'lygsp07.daili':7,'lygsp08.daili':8,'lygsp09.daili':9}
for i in res:
    try:
        i[3] = index[i[3]]
    except:
        pass
with open('结果.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        try:
            f_csv.writerow(i)
        except:
            print(i)