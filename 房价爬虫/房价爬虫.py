from selenium import webdriver
import csv
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
name = []
with open('楼盘名.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        name.append(row[0])
name = name[1:]
url = 'https://fangjia.fang.com/hf/?e=http://fangjia.fang.com/pinggu/ajax/searchtransfer.aspx?strcity=%25u5408%25u80A5&refer=sy_seach'
res = []
name = name[2613:]
for i in name:
    try:
        driver = webdriver.Chrome(executable_path='C:\PYTHON接单\高校爬虫\chromedriver.exe',chrome_options=chrome_options)
        driver.get(url)
        driver.find_element_by_id('searchpingu').send_keys(i)
        driver.find_element_by_id('pcchafangjia_B01_01_03').click()
        try:
            price = driver.find_element_by_id('price_hq').text
            res.append([i,price])
        except:
            for j in driver.find_elements_by_class_name('bkyellow'):
                res.append([j.find_elements_by_tag_name('a')[1].text,j.find_element_by_class_name('price').text])
        # print(res)
        print(i)
        driver.quit()
    except:
        break
with open('房价.csv','a+',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)