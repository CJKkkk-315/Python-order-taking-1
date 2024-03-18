
import csv
from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
rows = []
for i in range(1,10,2):
    url = 'https://search.jd.com/Search?keyword=电脑&wq=电脑&pvid=a45d1c13816f4e4b99bf0767450b9baa&page='+str(i)+'&click=0'
    driver.get(url)
    #每一页30个商品信息全部爬取
    for i in range(1,31):
        res = []
        # 利用xpath解析
        res.append(driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li['+ str(i) + ']/div/div[2]/strong/i').text)
        res.append(driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li['+ str(i) + ']/div/div[3]/a/em').text.replace('\n',''))
        res.append(driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li['+ str(i) + ']/div/div[3]/a').get_attribute('href'))
        # 存入res列表中
        rows.append(res)
        print(res)
driver.quit()
# #写入csv
with open('data.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in rows:
        f_csv.writerow(i)