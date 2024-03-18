#-*-coding:utf-8-*-
import requests
import csv
import json
d = []
users = []
headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Cookie': 'xq_a_token=fbc7bfef1e09beda4e5ad33d503c29e5aa980eb8; xqat=fbc7bfef1e09beda4e5ad33d503c29e5aa980eb8; xq_r_token=692e7688d33c8aedebdcd521135ae3706921c61c; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY0NDk2NDAyNCwiY3RtIjoxNjQzMzMzNDc3OTk5LCJjaWQiOiJkOWQwbjRBWnVwIn0.HnbIi2ukFRTGmZvHr3ptx5pUT7iKzq9Pe-zjMFPtALaV82BSvBWcAWr2ezpfUHQ685IGyO013IfOkcuwoSzMjN7pnb4o20THZuzeK3GMYIraeF4JezV93rs1YYMMiBXydplnvJ95W18vkail8eaMl9EyRPs6qHku9DQjeHCahZw2iBAgtyDbpXYvImKSoWRkav7lvTbIHlkvXy0ZEdzmRLLfaoTeooi8lToD1Ry6hi9Dh58cCGDG9rzRLYXNJIIoskpBuj56X1DH0CzVTuD-f1wNlOpdHAtoFoTmFS0QqDqurw2HsVVv4jF4hjTU5wVwwAJpjWNiKeJKzEwKRg1_Tw; u=581643333487641; device_id=ecc630d2d95510ca58725d47348d1ed7; Hm_lvt_1db88642e346389874251b5a1eded6e3=1643333489; s=bs1b4hafcv; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1643357706'    }
with open('用户数据(清洗后)(5000).csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        users.append(row)
users = users[:31]
for user in users:
    url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?pid=-120&category=3&size=1000&uid=' + str(user[1])
    response = requests.get(url, headers=headers)
    stock = json.loads(response.text)['data']['stocks']
    s = []
    for i in stock:
        s.append(i['name'])
    n = len(s)
    user.append(n)
    user.append(','.join(s))
    print(user)
users = users
with open('用户数据(清洗后)(5000)(组合).csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in users:
        try:
            f_csv.writerow(i)
        except:
            pass