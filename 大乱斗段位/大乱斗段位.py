import requests
import json
import csv
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import time

areavalue = ['艾欧尼亚', '比尔吉沃特', '祖安', '诺克萨斯', '德玛西亚', '班德尔城', '皮尔特沃夫', '战争学院', '弗雷尔卓德', '巨神峰', '雷瑟守备', '无畏先锋', '裁决之地',
             '黑色玫瑰', '暗影岛', '钢铁烈阳', '恕瑞玛', '水晶之恒', '教育网', '影流', '守望之海', '扭曲丛林', '征服之海', '卡拉曼达', '皮城警备', '巨龙之巢', '男爵领域',
             '均衡教派']
deadline = '2021-6-1'
mktime = time.mktime(time.strptime(deadline,'%Y-%m-%d'))*1000
def online():
    global winscore
    accountid = accountid1.get()
    cookie = cookie1.get()
    username = username1.get()
    areaId = area1.get()
    areaId = areavalue.index(areaId) + 1
    if not accountid:
        with open('user.csv') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                if username == row[0]:
                    accountid = row[1]
    # accountid = '4005072532'
    # username = '我真的A不动啊'
    # areaId = '7'
    # cookie = 'RK=E6z0VP2vah; ptcz=0129e96ccea286feae9efc16cd3ff9336da31ddc250cff8e1fd86f895cf4a479; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; pgv_pvid=5321798180; pgv_info=ssid=s4881124090; livelinkqqcomrouteLine=a20200527midgroupage; rv2=80767C289C639E2363D79C64920B350DFD45034374A0A4D6E9; property20=5B9BAC4812F757D923B1631C8095504196CF8163198A6201BE2A86160603C9B510DC2490A07A4576; tvfe_boss_uuid=a3887872d3314168; vversion_name=8.2.95; video_omgid=562c37dfaf09356e; eas_sid=T1o633j1S4x351C189a1v9d6X1; LW_uid=41V6Z3s1v4L341C241e9M4X9p3; jccqqcomrouteLine=a20210715pass; lplqqcomrouteLine=a20210719toc; lolqqcomrouteLine=a20210824reward_a20210719fight_a20210719fight_a20210903phoenix_a20210903phoenix_a20210719fight_a20210719fight; pac_uid=1_1121033787; iip=0; _qpsvr_localtk=0.5666624728297449; tokenParams=%3Fe_code%3D500142%26area%3D7; ptui_loginuin=1870941579; o_cookie=1870941579; LW_sid=M1U6K471z2f6M143d9m7i2i2P2; luin=o1121033787; lskey=000100009504fb6d9f5118571089f47583bbea14dd5ac4278a65bc4990a5087b862fc131cb2074e8a26b2de8; LOLWebSet_AreaBindInfo_1121033787=%257B%2522areaid%2522%253A%25227%2522%252C%2522areaname%2522%253A%2522%25E7%259A%25AE%25E5%25B0%2594%25E7%2589%25B9%25E6%25B2%2583%25E5%25A4%25AB%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221121033787%2522%252C%2522rolename%2522%253A%2522daafhajf%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1121033787%257C7%257C1121033787*%257C%257C%257C%257Cdaafhajf*%257C%257C%257C1641365587%257C%2522%252C%2522md5str%2522%253A%2522E8148D306D417F54965DFD853B400F52%2522%252C%2522roleareaid%2522%253A%25227%2522%252C%2522sPartition%2522%253A%25227%2522%257D; ied_qq=o1870941579; uin_cookie=o1870941579; uin=o1870941579; LOLWebSet_AreaBindInfo_1870941579=%257B%2522areaid%2522%253A%25227%2522%252C%2522areaname%2522%253A%2522%25E7%259A%25AE%25E5%25B0%2594%25E7%2589%25B9%25E6%25B2%2583%25E5%25A4%25AB%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221870941579%2522%252C%2522rolename%2522%253A%2522Apheliosss%25E4%25B8%25B6%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1870941579%257C7%257C1870941579*%257C%257C%257C%257CApheliosss%2525E4%2525B8%2525B6*%257C%257C%257C1641436222%257C%2522%252C%2522md5str%2522%253A%2522F4E84998557B70314BAA769F81AD68F0%2522%252C%2522roleareaid%2522%253A%25227%2522%252C%2522sPartition%2522%253A%25227%2522%257D; skey=@YvPUi5PaK; p_uin=o1870941579; pt4_token=0jtor5R1ypoOFy214LMmLecL-Lyh0hQJUhWWFT17zwM_; p_skey=IhL5tUG4CfgYololTJBB*UogZSY-YGZNdL9yRc2p2XU_; IED_LOG_INFO2=userUin%3D1870941579%26nickName%3D1111%26nickname%3D1111%26userLoginTime%3D1641447125%26logtype%3Dqq%26loginType%3Dqq%26uin%3D1870941579'
    headers = { 'Cookie': cookie}
    url = "https://lol.sw.game.qq.com/lol/api/?c=Battle&a=matchList&areaId=" + str(areaId) + "&accountId=" + str(accountid) +"&queueId=65,450&r1=matchList"
    response = requests.request("GET", url, headers=headers)
    s = ''.join(response.text[15:])
    data = json.loads(s)
    gameid = []
    for i in data['msg']['games']:
        gameid.append(str(i['gameId']))
    # print(gameid)
    userdata = []
    with open('user.csv') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            userdata.append(row)
    newgameid = []
    is_new = 1
    for i in userdata:
        if i[1] == accountid:
            last = str(i[2])
            for j in gameid:
                if j == last:
                    break
                newgameid.append(j)
            i[2] = gameid[0]
            is_new = 0
            break
    if is_new:
        userdata.append([username,accountid,gameid[0]])
        newgameid = gameid[::]
    # print(newgameid)
    # print(gameid)
    res = []
    for i in newgameid:
        url = 'https://lol.sw.game.qq.com/lol/api/?c=Battle&a=combatGains&areaId=' + str(areaId) + '&gameId=' + str(i) +'&r1=combatGains'
        response = requests.get(url,headers=headers)
        # print(response.text)
        data = json.loads(response.text[18:])
        # print(data)
        createtime = data['msg']['gameInfo']['gameCreationTime']
        #     continue
        data = data['msg']['participants']
        # print(data)
        for j in data:
            if j['summonerName'] == username:
                if j['stats']['win'] == 'Fail':
                    win = 0
                else:
                    win = 1
                kills = j['stats']['kills']
                deaths = j['stats']['deaths']
                assists = j['stats']['assists']
                kda = int(kills+assists)/int(deaths+1)
                res.append([i,win,kills,deaths,assists,round(kda,2),createtime])
    res = res[::-1]
    with open(str(accountid) + '.csv','a+',newline='') as f:
        f_csv = csv.writer(f)
        for i in res:
            f_csv.writerow(i)
    with open('user.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        for i in userdata:
            f_csv.writerow(i)
    winscore = count(accountid)
    add = 0
    if winscore >= 4400:
        add = winscore - 4400
        winscore = 4400
    duanweilist = ['黑铁','青铜','白银','黄金','铂金','钻石','大师','宗师','王者']
    localtime = time.localtime(time.time())
    tkinter.messagebox.askokcancel(title= '结果', message =username + '\n您当前的段位是' + duanweilist[winscore//500] + str(5 - winscore%500//100) + '\n您当前的胜点是' + str(winscore%100 + add) +
                                                         '\n当前时间' + str(localtime.tm_year) + '年' + str(
        localtime.tm_mon) + '月' + str(localtime.tm_mday) + '日' + str(localtime.tm_hour) + '时' + str(
        localtime.tm_min) + '分' + str(localtime.tm_sec) + '秒'

                                   )
def offline():
    accountid = accountid1.get()
    username = username1.get()
    if not accountid:
        with open('user.csv') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                if username == row[0]:
                    accountid = row[1]
    winscore = count(accountid)
    add = 0
    if winscore >= 4400:
        add = winscore-4400
        winscore = 4400
    duanweilist = ['黑铁', '青铜', '白银', '黄金', '铂金', '钻石', '大师', '宗师', '王者']
    localtime = time.localtime(time.time())
    tkinter.messagebox.askokcancel(title='结果', message=
    username +
    '\n您当前的段位是' +
    duanweilist[winscore // 500] +
    str(5 - winscore % 500 // 100) +
    '\n您当前的胜点是' +
    str(winscore % 100 + add)+
    '\n当前时间' + str(localtime.tm_year) + '年' + str(localtime.tm_mon) + '月' + str(localtime.tm_mday) + '日' + str(localtime.tm_hour) + '时' + str(localtime.tm_min) +  '分' + str(localtime.tm_sec) + '秒'
                                   )


def count(accountid):
    win = []
    kda = []
    ava = []
    x = 0
    with open(str(accountid) + '.csv') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if int(row[6]) > mktime:
                win.append(row[1])
                kda.append(float(row[5]))
    for i in range(min(len(kda),10)):
        ava.append(3)
    if len(kda) > 10:
        for i in range(10,len(kda)):
            ava.append(round(sum(kda[i-10:i])/10,2))
    for i,j,k in zip(win,kda,ava):
        if int(i):
            x += int(max(3,(j-k+10)))
        else:
            x += int((j-k+10)-30)
            x = max(0,x)
    return x
if __name__ == '__main__':
    window=tk.Tk()
    window.title('欢迎进入系统')
    window.geometry('600x350')
    tk.Label(window,text='请输入accountid:').place(x=50,y=70)
    tk.Label(window, text='这是xg的大乱斗排位系统\n\n根据你的历史战绩进行“合理”计算\n\n 给出你的段位\n\n你最近10场的战绩尤为重要哦\n\nTips:\n\n若第一次查询请输入accountid\n重复查询无需再输\n离线查询仅需要输入角色id').place(x=350, y=70)
    tk.Label(window,text='请选择cookie:').place(x=50,y=110)
    tk.Label(window,text='请选择大区:').place(x=50,y=150)
    tk.Label(window,text='请输入游戏id:').place(x=50,y=190)
    accountid1=tk.Entry(window)
    accountid1.place(x=160,y=70)
    cookie1=tk.Entry(window)
    cookie1.place(x=160,y=110)
    area1=tk.ttk.Combobox(values=areavalue)
    area1.place(x=160,y=150)
    username1=tk.Entry(window)
    username1.place(x=160,y=190)
    bt_login1=tk.Button(window,text='在线查询',command=online)
    bt_login1.place(x=140, y=250)
    bt_login2 = tk.Button(window, text='离线查询', command=offline)
    bt_login2.place(x=240,y=250)
    #主循环
    window.mainloop()

