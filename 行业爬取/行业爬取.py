import requests
from bs4 import BeautifulSoup
import datetime
import time
# d1 = time.strftime("%Y-%m-%d", time.localtime())
# d1 = datetime.datetime.strptime(d1, '%Y-%m-%d')
d2 = datetime.datetime.strptime('2022-01-19', '%Y-%m-%d')
# print(d2)
urls = ["http://info.shippingchina.com/bluenews/index/list/type/海运新闻.html","http://info.shippingchina.com/bluenews/index/list/type/港口新闻.html","http://info.shippingchina.com/bluenews/index/list/type/物流新闻.html","http://info.shippingchina.com/bluenews/index/list/type/经贸新闻.html","http://info.shippingchina.com/bluenews/index/list/type/时政新闻.html"]
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
payload = {}
for url in urls:
    response = requests.get(url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text,'lxml')
    for i,j in zip(soup.find(name='dl').find_all(name='dt'),soup.find(name='dl').find_all(name='dd')):
        if datetime.datetime.strptime(i.find(name='span').text, '%Y-%m-%d') == d2:
            print(i.find(name='a').text)
            print(j.text)

