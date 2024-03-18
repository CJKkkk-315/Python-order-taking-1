import json
import time
from selenium import webdriver
rows = []
driver = webdriver.Opera()
driver.get('http://search.dangdang.com/?key=python&act=input&page_index=1')
for i in driver.find_element_by_id('component_59').find_elements_by_tag_name('li'):
    v1 = i.find_element_by_tag_name('a').get_attribute('title')
    v2 = i.find_element_by_class_name('search_book_author').find_elements_by_tag_name('span')[0].find_element_by_tag_name('a').get_attribute('title')
    v4 = i.find_element_by_class_name('search_book_author').find_elements_by_tag_name('span')[-2].text[1:]
    v3 = i.find_element_by_class_name('search_book_author').find_elements_by_tag_name('span')[-1].find_element_by_tag_name('a').text
    v5 = i.find_element_by_class_name('search_now_price').text
    v6 = time.time()
    rows.append([v1,v2,v3,v4,v5,v6])
driver.quit()
res = []
for i in rows[:20]:
    res.append(json.dumps({'书名':i[0],'作者':i[1],'出版社':i[2],'出版时间':i[3],'价格':i[4],'时间':i[5]},ensure_ascii=False))
with open('191650216_何一苇_原始数据2.json', 'w',encoding='utf-8') as json_file:
    for i in res:
        print(i + '\n')
        json_file.write(i + '\n')
