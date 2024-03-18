from selenium import webdriver
import datetime
from time import sleep
from random import randint
m = randint(700,900)
start = datetime.datetime.now()
end = datetime.datetime.now()+datetime.timedelta(days=1)
start = start.strftime("%Y%m%d")
end = end.strftime("%Y%m%d")
time = datetime.datetime.now().strftime("%Y年%m月%d日%H点%M分")
name = time + "--58数据.csv"
print(end)
print(start)
# chrome_options.add_argument("headless")
url = 'https://lyg.58.com/job/?postdate=' + start + '_' + end + '&PGTID=0d302408-0080-1969-7e8b-4aaaa47c9d04&ClickID=3'
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://passport.58.com/login/')
sleep(60)
driver.get(url)
rows = []
# page = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/span[2]/i').text
# print(page)
while True:
    if len(rows) > m:
        break
    try:
        for i in driver.find_element_by_id('list_con').find_elements_by_tag_name('li'):
            b = i.find_element_by_class_name('comp_name').find_element_by_tag_name('a').get_attribute('title')
            # print(i.find_element_by_class_name('comp_name').find_element_by_tag_name('a').get_attribute('title'))
            try:
                a = i.find_element_by_class_name('comp_name').find_element_by_tag_name('i').text
            except:
                a = ''
            if [b,a] not in rows:
                rows.append([b,a])
        try:
            driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/a[2]').click()
        except:
            break
    except:
        break
with open(name,"w") as f:
    for i in rows:
        f.write(i[0] + ',' + i[1] + '\n')