import requests
import json
import csv
import _thread
c = []
res = []
with open('res.csv','r') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        if i not in c:
            c.append(i)
with open('cookie.txt','r') as f:
    cookies = f.read().split('#####')
f = open('upload.csv','w',newline='')
f_csv = csv.writer(f)
cookie = cookies[0]
headers1 = {'Cookie': cookie}
headers2 = {'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': cookie}
flag = 0
def function(c):
    global flag
    for i in c:
        payload = {'custName': i[0],
                   'isModify': 'false'}
        response = requests.post(
            "https://customeraudit.zhaopin.com/customeraudit/service/inputCustomer/duplicateCheck",
            headers=headers1, data=payload)
        jsondata = json.loads(response.text)[0]
        custid = jsondata['custId']
        # print(custid)
        response = requests.get(
            "https://cmp-apigw.zhaopin.com/api-contact-service/contact/queryFrequentContacts?friendId=" + str(custid) + "&size=3",
            headers = headers1
        )
        data = json.loads(response.text)['data']
        aw = []
        for j in data:
            if j['mobilePhone']:
                aw.append(j)
        if len(aw) < 1:
            aw.append(data[0])
            aw[0]['mobilePhone'] = '12345678912'
        data = aw[:2]
        name1 = data[0]['cnName']
        phone1 = data[0]['mobilePhone']
        name2 = ''
        phone2 = ''
        row = ['' for _ in range(19)]
        if len(data) > 1:
            name2 = data[1]['cnName']
            phone2 = data[1]['mobilePhone']
        row[0] = i[0]
        row[2] = name1
        row[3] = phone1
        row[-3] = name2
        row[-2] = phone2
        f_csv.writerow(row)
        print(row)
    flag += 1
jdata = [[] for i in range(10)]
for i in range(len(c)):
  jdata[i%10].append(c[i])
flag = 0
try:
    for i in jdata:
       _thread.start_new_thread(function, (i,))
except:
   print ("Error: 无法启动线程")
while 1:
   if flag == 10:
       break
