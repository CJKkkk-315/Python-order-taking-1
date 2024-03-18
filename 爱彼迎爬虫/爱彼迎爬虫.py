import requests
from bs4 import BeautifulSoup
import csv
# 需要访问的url，其中页面只需要更改offset信息，每20为一页
url = 'https://www.airbnb.cn/s/厦门/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&screen_size=large&hide_dates_and_guests_filters=false&map_toggle=false&place_id=ChIJJ-u_5XmDFDQRVtBolgpnoCg&last_search_session_id=a50b3bde-54af-475b-b660-3c86c5df0c2c&items_offset=220&section_offset=6'
# 加入请求头，模拟浏览器访问，防止防爬
headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
# 请求页面，将返回的结果存储为response
response = requests.get(url,headers=headers)
# 利用BeautifulSoup解析返回的文本结果，使其变为结构化的数据
soup = BeautifulSoup(response.text,'lxml')
res = []
# 遍历soup中所有房源item，提取其中的信息
for i in soup.find(class_='_fhph4u').find_all(class_='_14csrlku'):
    try:
        v1 = i.find(class_='_9ofhsl')['alt']    # 标题
        v2 = i.find(class_='_9ofhsl')['src']    # 图片地址
        v3 = i.find(class_='_69pvqtq').text     # 评论数
        v4 = i.find(class_='_1d8yint7').find_all(name='span')[2].text   # 价格
        v5 = i.find(class_='_faldii7').text     # 标签
        v6 = i.find(class_='_1d5f1nt5').find_all(name='a')[3].text  # 评分
        res.append([v1,v6,v2,v3,v4,v5])
    except:
        pass
# 以追加写入的方式将数据写入csv中
with open('结果.csv','a+',newline='',encoding='utf-8') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)