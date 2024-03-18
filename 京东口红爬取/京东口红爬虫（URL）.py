
import csv
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
for p in range(0,100,2):
    print(p)
    url = 'https://search.jd.com/Search?keyword=口红&wq=口红&pvid=a45d1c13816f4e4b99bf0767450b9baa&page=' + str(p) + '&psort=4&click=0'
    rows = []
    driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe',options=chrome_options)
    driver.get(url)
    # print(len(driver.find_element_by_id('J_goodsList').find_element_by_tag_name('ul').find_elements_by_tag_name('li')))
    for i in range(1,31):
        try:
            res = []
            res.append(driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li['+ str(i) + ']/div/div[2]/strong/i').text)
            res.append(driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li['+ str(i) + ']/div/div[3]/a/em').text.replace('\n',''))
            res.append(driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li['+ str(i) + ']/div/div[5]/span/a').text)
            res.append(driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li['+ str(i) + ']/div/div[3]/a').get_attribute('href'))
            rows.append(res)
        except:
            print(i)
            pass
    driver.quit()
    # #写入csv
    with open('URL.csv','a+',newline='') as f:
        f_csv = csv.writer(f)
        for i in rows:
            f_csv.writerow(i)