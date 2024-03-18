import requests
from bs4 import BeautifulSoup
import csv

rows = []
headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27',
                'Cookie':'bid=d89BtRgqN4g; douban-fav-remind=1; __utmc=30149280; __gpi=00000000-0000-0000-0000-000000000000; ll="118201"; __utmv=30149280.22071; _ga=GA1.1.491822689.1623747306; _ga_RXNMP372GL=GS1.1.1633688561.1.0.1633688563.0; __gads=ID=0c28cbccd780629c-22b2684f51cc002c:T=1623747305:RT=1633689082:S=ALNI_MYB9yVNkv8-ZUHueuIvDzAtYZKXyQ; gr_user_id=376fb970-3719-46d1-981c-a28050ebb796; viewed="30293801_33450010_26381341"; dbcl2="220718836:CK/Wv5YVbKQ"; ck=seZG; ct=y; push_noty_num=0; ap_v=0,6.0; _pk_ref.100001.2939=%5B%22%22%2C%22%22%2C1644659318%2C%22https%3A%2F%2Fnetflix.mom%2Findex.php%2Fvod%2Fdetail%2Fid%2F8341.html%22%5D; _pk_ses.100001.2939=*; __utmt=1; push_doumail_num=0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=b830e886-052f-4488-8318-d59184751f09; gr_cs1_b830e886-052f-4488-8318-d59184751f09=user_id%3A1; __utma=30149280.491822689.1623747306.1644659319.1644660240.72; __utmz=30149280.1644660240.72.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt_douban=1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_b830e886-052f-4488-8318-d59184751f09=true; _pk_id.100001.2939=e94ddcf843f41cdb.1644633510.3.1644660481.1644647220.; __utmb=30149280.18.10.1644660240'
}
payload = {}
for i in range(900,901):
        url = 'https://netflix.mom/index.php/vod/detail/id/' + str(i) + '.html'
        response = requests.get(url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text,'lxml')
        a = soup.find(class_='data video-info-items').find(name='a')['href']
        b = soup.find_all(class_='video-info-item')[2].text
        c = soup.find(class_='page-title').text
        response = requests.get(a, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'lxml')
        print(soup)
        d = soup.find(class_='sc-bZQynM jKwOab sc-bxivhb jDZFxE')
        rows.append([a,b,c])
        print(d)
    # except:
    #     print('https://netflix.mom/index.php/vod/detail/id/' + str(i) + '.html')
# with open('数据.csv','w',newline='') as f:
#     f_csv = csv.writer(f)
#     for i in rows:
#         f_csv.writerow(i)