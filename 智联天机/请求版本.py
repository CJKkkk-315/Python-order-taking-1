import requests
import json
import csv
import os
import datetime
from dateutil.parser import parse
import _thread
import sys
now = datetime.datetime.now()
with open('cookie.txt','r') as f:
    cookies = f.read().split('#####')
# cookies = 'INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamMxTVNJc0ltVjRjQ0k2TVRZME56UTRNVEV6T1gwLnlVZmdydzlmTjJhNWJKRjBJUFgyOFZmSkkydHhSRnRBbU50TGpkMFRWeHBwbTVIcUFrZVdiRnJRYmU4cVpxT28ycGVwSmo1UnFQQnR4RTFfc3ZseEN3; ZPSSO_USER_EMPID=13362751; ZPSSO_USER_NAME=lygsp.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp.daili%22%2C%22empId%22%3A%2213362751%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221002%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamMyTVNJc0ltVjRjQ0k2TVRZME56UTRNVEUxT0gwLko4UW1pb3FSakpzcHVNbEltTXlaYlhiZVZxa05wN2pOV2FWbno1SFFPOWRtNHBTaDlpMVFiVEFtQjQ5ZUl2S1k2VHBRVk5Zb05DcnRjcklXRG5jZzZB; ZPSSO_USER_EMPID=13362761; ZPSSO_USER_NAME=lygsp01.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp01.daili%22%2C%22empId%22%3A%2213362761%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamMzTVNJc0ltVjRjQ0k2TVRZME56UTRNVEU0T0gwLlN4T19JZm93cmc0TWViYkphT01aajFWLVR3VUVXM0YxN0lkZEZQVndmcGFnUnJPVzBBazQ3T3lCbEVMeGRieUVGQ2p2ZXN1RVd2VTAza1RwUGpGNVRR; ZPSSO_USER_EMPID=13362771; ZPSSO_USER_NAME=lygsp02.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp02.daili%22%2C%22empId%22%3A%2213362771%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamM0TVNJc0ltVjRjQ0k2TVRZME56UTRNVEl5TkgwLlk1QzhpMVlhX0kxOVN0WDN4Q2x3VlNsM2FQOEdaQUdIQjJmZktGVjdxS1YyOXpTUDhXcEJkeUdiNlB1dnB5QUx3U2xwNFFtbzUtZ0FrczA1SF9JUC1B; ZPSSO_USER_EMPID=13362781; ZPSSO_USER_NAME=lygsp03.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp03.daili%22%2C%22empId%22%3A%2213362781%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJNamM1TVNJc0ltVjRjQ0k2TVRZME56UTRNVEkzTkgwLldGeHpYM25sbGwwbkw4WkNoRE44M1l0WGpFN0ItWm0zOEwzUHdpbS1yRzBQNHN0dG9BLW5TWE84NE94cWd0M1E5d09pS244RjY0WTlpN0RXWlNfVkpn; ZPSSO_USER_EMPID=13362791; ZPSSO_USER_NAME=lygsp04.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp04.daili%22%2C%22empId%22%3A%2213362791%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGMzTVNJc0ltVjRjQ0k2TVRZME56UTRNVE14TjMwLkotUDFndGpseFZXakNva0puUVZINFhtUGJ4MnFlWlhMY0dYeU9ZMWZYSG1JOF8yODB0THBIZGpoZHEzU1BpOE14bEUydnhMSkFoQTVtN2JHZkd4YzBB; ZPSSO_USER_EMPID=13364771; ZPSSO_USER_NAME=lygsp05.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp05.daili%22%2C%22empId%22%3A%2213364771%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGM0TVNJc0ltVjRjQ0k2TVRZME56UTRNVE01TlgwLmJNUGk5ZWVJaWNqQnFZOU9lMDROeTJ0WkFheHlGOU96azRQbmlRY1lKX1NNTURDd3ZMYTlVOWcyTldqbUpaVzBaa2hEVnJzdlZSRmplcURjVXV3ZUNR; ZPSSO_USER_EMPID=13364781; ZPSSO_USER_NAME=lygsp06.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp06.daili%22%2C%22empId%22%3A%2213364781%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGM1TVNJc0ltVjRjQ0k2TVRZME56UTRNVFF4TjMwLmlBVGh4bElIbnVmbkFyenJ1MGxKMGRSbzF1QUoybHFYUFZVRW81TkRKdThiYW9FMVN2WjJmM3BzV19HWm12aXZkaTBjOHZabzhCdFFybXhRNG5vVFNB; ZPSSO_USER_EMPID=13364791; ZPSSO_USER_NAME=lygsp07.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp07.daili%22%2C%22empId%22%3A%2213364791%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGd3TVNJc0ltVjRjQ0k2TVRZME56UTRNVFUwTVgwLkNmMGR1WlRPUjFCb04weHFERVZhUGFqVk9IOURzSnE1YW5YTWxwZEt0UVlqd3d4UURtOElTLU1RMHhuSUl5eFZiUTBrU3ZYemhnbU5SNGltSHFGRzJB; ZPSSO_USER_EMPID=13364801; ZPSSO_USER_NAME=lygsp08.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp08.daili%22%2C%22empId%22%3A%2213364801%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D#####INNER_AUTHENTICATION=QmVhcmVyIGV5SmhiR2NpT2lKSVV6VXhNaUo5LmV5SnpkV0lpT2lJeE16TTJORGd4TVNJc0ltVjRjQ0k2TVRZME56UTRNVFU1Tm4wLldvSkZURXhnWUNzZmYwUVBXYk8xTzZ5andZRzF5cGtVMUcwZ1pzRlRYZHR6SDd4ZzVIaFVLSVplMS1mTExhVkMxa0pBaFczOU14T2N6am9VckdpMmhn; ZPSSO_USER_EMPID=13364811; ZPSSO_USER_NAME=lygsp09.daili; ZPSSO_USER_INFO=%7B%22empName%22%3A%22lygsp09.daili%22%2C%22empId%22%3A%2213364811%22%2C%22branchCompanyMngDeptId%22%3A%2255311%22%2C%22mngDeptId%22%3A%2288801%22%2C%22deptId%22%3A%22121331%22%2C%22empRole%22%3A%221001%22%2C%22salesLevel%22%3A%221026%22%2C%22branchCompanyMngDeptName%22%3A%22%E5%8D%97%E6%96%B9%E5%91%BC%E5%8F%AB%E4%B8%AD%E5%BF%83%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22isLeader%22%3Afalse%7D'.split('#####')
# Cookie
data = []
ext='.csv'
files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1]==ext]
file = files[0]
with open(file,encoding="gbk")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
print(data)
companys = [[] for i in range(10)]
users = ['lygsp.daili','lygsp01.daili','lygsp02.daili','lygsp03.daili','lygsp04.daili','lygsp05.daili','lygsp06.daili','lygsp07.daili','lygsp08.daili','lygsp09.daili']
full = {'lygsp.daili':0,'lygsp01.daili':0,'lygsp02.daili':0,'lygsp03.daili':0,'lygsp04.daili':0,'lygsp05.daili':0,'lygsp06.daili':0,'lygsp07.daili':0,'lygsp08.daili':0,'lygsp09.daili':0}
q = len(data)//10
for i in range(len(data)):
    companys[i%10].append(data[i])
# companys = [i[:10] for i in companys]
f1 = 0
res = []
shengyu = []
flagaa = 0
def function(f1):
    global flagaa
    global shengyu
    print([len(i) for i in companys])
    cookie = cookies[f1]
    username = users[f1]
    headers1 = {'Cookie': cookie}
    headers2 = {'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': cookie}
    print('当前用户为：' + username)
    # print(cookie)
    for i in range(len(companys[f1])):
        if len(companys[f1][i][0]) < 5:
            continue
        companyname = companys[f1][i][0].replace('（', '(').replace('）', ')')
        payload = {'custName': companyname,
                   'isModify': 'false'}
        response = requests.post(
            "https://customeraudit.zhaopin.com/customeraudit/service/inputCustomer/duplicateCheck",
            headers=headers1, data=payload)
        jsondata = json.loads(response.text)
        if len(jsondata) > 0:
            jsondata = jsondata[0]
        else:
            continue
        name = jsondata['custName']
        if name == companyname:
            ten = ''
            custid = jsondata['custId']
            ad = jsondata['custAddress']
            try:
                if '连云港' in ad or ad[:3] == '连云港' or ad[:3] == '连云区' or ad[:3] == '海州区' or ad[:3] == '连云区' or ad[
                                                                                                              :3] == '赣榆区' or ad[
                                                                                                                              :3] == '灌南县' or ad[
                                                                                                                                              :3] == '东海县' or ad[
                                                                                                                                                              :3] == '灌云县' or ad[
                                                                                                                                                                              :6] == '江苏省连云港' or ad[
                                                                                                                                                                                                 :5] == '江苏连云港':
                    flag = ''
                else:
                    flag = '非连云港地区'
            except:
                flag = '非连云港地区'
            if jsondata['lastContactTime'] and (now - parse(jsondata['lastContactTime'])).days < 10:
                print('不足10天')
                ten = '不足十天'
            if jsondata['canClaim'] and not ten:
                payload = json.dumps({"custId": custid})
                a = json.loads(requests.post('https://cmp-rule.zhaopin.com/api-new/cust/receive', headers=headers2,
                                             data=payload).text)
                if a['code'] == 400:
                    print(['领取', a])
                    print(companys[f1][i])
                    full[username] = 1
                    shengyu = companys[f1][i:] + shengyu
                    break
                if a['code'] == 200 and a['message'] != '客户认领成功':
                    print(a)
                    with open('秘钥过期.txt', 'w'):
                        pass
                    sys.exit()
                jsondata['empName'] = username
                print(['领取', a])
            companys[f1][i].append(jsondata['empName'])
            companys[f1][i].append(jsondata['lastContactTime'])
            companys[f1][i].append(flag)
            companys[f1][i].append(ten)
            res.append(companys[f1][i])
        else:
            companys[f1][i].append('无')
            res.append(companys[f1][i])
        print(companys[f1][i])
    flagaa += 1
for i in range(10):
    _thread.start_new_thread(function, (i,))
while 1:
   if flagaa == 10:
       break
companys = [[] for i in range(10)]
flagaa = 0
flagbb = 0
print(11111111)
for i in range(len(shengyu)):
    companys[i%10].append(shengyu[i])
for i in range(10):
    if full[users[i]] == 1:
        companys[i+1] = companys[i] + companys[i+1]
        continue
    flagbb += 1
    _thread.start_new_thread(function, (i,))
while 1:
   if flagaa == flagbb:
       break
dd = ['南方呼叫中心销售部','南呼待审核库','南呼江苏待开发库','南呼江苏体验库','南呼无价值客户库']
for i in res:
    if (i[-1] != '不足十天' or i[-1] != '无') and i[2] in dd:
        for username,cookie in zip(users,cookies):
            if full[username] == 1:
                continue
            headers1 = {'Cookie': cookie}
            headers2 = {'Content-Type': 'application/json;charset=UTF-8',
                        'Cookie': cookie}
            payload = {'custName': i[0],
                       'isModify': 'false'}
            response = requests.post(
                "https://customeraudit.zhaopin.com/customeraudit/service/inputCustomer/duplicateCheck",
                headers=headers1, data=payload)
            jsondata = json.loads(response.text)[0]
            custid = jsondata['custId']
            if jsondata['canClaim']:
                if jsondata['lastContactTime'] and (now - parse(jsondata['lastContactTime'])).days < 10:
                    break
                else:
                    payload = json.dumps({"custId": custid})
                    a = json.loads(requests.post('https://cmp-rule.zhaopin.com/api-new/cust/receive', headers=headers2, data=payload).text)
                    if a['code'] == 400:
                        print(['领取',a])
                        print(i)
                        full[username] = 1
                        continue
                    if a['code'] == 200:
                        i[2] = username
                        print(['领取',a])
                        print(i)
                        break
                    print(['领取',a])
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)