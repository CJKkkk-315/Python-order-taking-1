import csv
import pandas as pd
df1 = pd.read_csv('BEIYOU_1.csv',encoding='gbk')
df2 = pd.read_csv('XIDIAN_1.csv',encoding='gbk')
df3 = pd.read_csv('CHENGDIAN_1.csv',encoding='gbk')
df4 = pd.read_csv('分类.csv',encoding='gbk')
with pd.ExcelWriter('总和.xlsx') as writer:
    str1 = ['北邮','西电','成电','分类']
    df1[['招聘主题','发布日期','浏览次数','招聘数量']].to_excel(writer, sheet_name='北邮')
    df2[['招聘主题','发布日期','浏览次数']].to_excel(writer, sheet_name='西电')
    df3[['招聘主题','发布日期','浏览次数']].to_excel(writer, sheet_name='成电')
    df4[['招聘主题','雇主类型']].to_excel(writer, sheet_name='分类')
    writer.save()
dic = {
    '大学':'研究学院',
    '学院':'研究学院',
    '研究所':'研究学院',
    '移动':'电信运营商',
    '电信':'电信运营商',
    '联通':'电信运营商',
    '京东':'互联网',
    '网易':'互联网',
    '小米':'互联网',
    '快手':'互联网',
    '阿里':'互联网',
    '字节':'互联网',
    '拼多多':'互联网',
    '科技':'信息科技',
    '信息':'信息科技',
    '车':'车辆工程',
    '证券':'金融',
    '金融':'金融',
    '经济':'金融',
    '国家':'国企',
    '文化':'文化',
    '教育':'教培',
    '培训':'教培',
    '广告':'媒体',
    '媒体':'媒体',
    '航':'航天',
    '海洋':'海事',
    '海军':'海事',
    '教师':'教培'
}
data = []
with open('BEIYOU_1.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append([row[1],'北邮',row[3]])
with open('XIDIAN_1.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append([row[1],'西电',row[3]])
with open('CHENGDIAN_1.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append([row[1],'成电',row[3]])
res = []
data = data[1:]
for i in data:
    for j in dic.keys():
        if j in i[0]:
            i.append(dic[j])
            break
    if len(i) == 3:
        i.append('其他')
head = ['序号','招聘主题','雇主类型','学校','浏览次数']
with open('分类.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in range(len(data)):
        f_csv.writerow([i,data[i][0],data[i][3],data[i][1],data[i][2]])