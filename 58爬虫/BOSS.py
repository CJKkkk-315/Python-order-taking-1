from selenium import webdriver
from time import sleep
chrome_options = webdriver.ChromeOptions()
url = 'https://www.zhipin.com/c101191000/?page=1&ka=page-1'
driver = webdriver.Chrome(executable_path='D:\chromedriver.exe',chrome_options=chrome_options)
driver.get(url)
while True:
        sleep(3)
        for i in driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/ul').find_elements_by_tag_name('li'):
            all_handles = driver.window_handles
            i.find_element_by_class_name('primary-box').click()
            all_handles2 = driver.window_handles
            newhandle = [handle for handle in all_handles2 if handle not in all_handles]
            driver.switch_to.window(newhandle[0])
            while True:
                try:
                    sleep(3)
                    print(driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[5]/div[1]').text)
                    break
                except:
                    sleep(3)
                    continue
            driver.close()
            driver.switch_to.window(all_handles[0])
        driver.find_element_by_class_name('page').find_element_by_class_name('next').click()