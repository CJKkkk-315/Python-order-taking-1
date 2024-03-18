import json
from selenium import webdriver
import time
rows = []
driver = webdriver.Opera()
driver.get('https://search.jd.com/Search?keyword=python&enc=utf-8&pvid=067ff5c5c5e9429582750fd794a3ccf0')
for i in range(4,30):
    try:
        v1 = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[' + str(i) + ']').find_element_by_class_name('p-name').find_element_by_tag_name('em').text
        v2 = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[' + str(i) + ']').find_element_by_class_name('p-bi-name').find_element_by_tag_name('a').get_attribute('title')
        v3 = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[' + str(i) + ']').find_element_by_class_name('p-bi-store').find_element_by_tag_name('a').get_attribute('title')
        v4 = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[' + str(i) + ']').find_element_by_class_name('p-bookdetails').find_elements_by_tag_name('span')[2].text
        v5 = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[' + str(i) + ']').find_element_by_class_name('p-price').find_element_by_tag_name('i').text
        v6 = time.time()
        rows.append([v1, v2, v3, v4, v5, v6])
    except:
        pass
driver.quit()
res = []
for i in rows[:20]:
    res.append(json.dumps({'书名':i[0],'作者':i[1],'出版社':i[2],'出版时间':i[3],'价格':i[4],'时间':i[5]},ensure_ascii=False))
with open('191650216_何一苇_原始数据3.json', 'w',encoding='utf-8') as json_file:
    for i in res:
        print(i + '\n')
        json_file.write(i + '\n')
