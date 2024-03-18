import json
from selenium import webdriver
import time
rows = []
for page in range(0,30,15):
    driver = webdriver.Opera()
    driver.get('https://book.douban.com/subject_search?search_text=python&cat=1001&start=' + str(page))
    for i in driver.find_elements_by_class_name('eJWSlY'):
        try:
            v1 = i.find_element_by_class_name('detail').find_element_by_class_name('title').text
            v2 = str(i.find_element_by_class_name('detail').find_element_by_class_name('abstract').text).split('/')[0]
            v3 = str(i.find_element_by_class_name('detail').find_element_by_class_name('abstract').text).split('/')[-3]
            v4 = str(i.find_element_by_class_name('detail').find_element_by_class_name('abstract').text).split('/')[-2]
            v5 = str(i.find_element_by_class_name('detail').find_element_by_class_name('abstract').text).split('/')[-1]
            v6 = time.time()
            rows.append([v1,v2,v3,v4,v5,v6])
        except:
            pass
    driver.quit()
res = []
for i in rows[:20]:
    res.append(json.dumps({'书名':i[0],'作者':i[1],'出版社':i[2],'出版时间':i[3],'价格':i[4],'时间':i[5]},ensure_ascii=False))
with open('191650216_何一苇_原始数据1.json', 'w',encoding='utf-8') as json_file:
    for i in res:
        print(i + '\n')
        json_file.write(i + '\n')
