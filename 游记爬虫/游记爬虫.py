import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Opera()
driver.get('https://www.qixin.com')
js = "document.getElementsByClassName('app-user-login font-12')[0].click()"
driver.execute_script(js)
js = "document.getElementsByClassName('switch-tabs h4 clearfix')[0].getElementsByClassName('item')[1].click()"
driver.execute_script(js)
js = "document.getElementsByClassName('form-control input-lg input-flat number-input')[0].value = '18150139952'"
driver.execute_script(js)
js = "document.getElementsByClassName('form-control input-lg input-flat')[1].value = '00377863a'"
driver.execute_script(js)
js = "document.getElementsByClassName('btn btn-primary btn-block btn-lg')[0].click()"
driver.execute_script(js)
js = "document.getElementsByClassName('btn btn-primary btn-block btn-lg')[0].click()"
driver.execute_script(js)
js = "document.getElementsByClassName('btn btn-primary btn-block btn-lg')[0].click()"
driver.execute_script(js)