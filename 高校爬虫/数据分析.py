import csv
from collections import Counter
bybest = []
with open('BEIYOU_1.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            bybest.append([row[1],int(row[3])])
        except:
            pass
bybest.sort(key=lambda x:x[1],reverse=True)
print('最受北邮学生欢迎关注的招聘TOP20为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')'  for i in bybest[1:21]]))
xdbest = []
with open('XIDIAN_1.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            xdbest.append([row[1], int(row[3])])
        except:
            pass
xdbest.sort(key=lambda x:x[1],reverse=True)
print('最受西电学生欢迎关注的招聘TOP20为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')'   for i in xdbest[1:21]]))
cdbest = []
with open('CHENGDIAN_1.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            cdbest.append([row[1], int(row[3])])
        except:
            pass
cdbest.sort(key=lambda x:x[1],reverse=True)
print('最受成电学生欢迎关注的招聘TOP20为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')'   for i in cdbest[1:21]]))
bygroup = {
    '研究学院':0,
    '电信运营商':0,
    '互联网':0,
    '信息科技':0,
    '车辆工程':0,
    '金融':0,
    '国企':0,
    '文化':0,
    '教培':0,
    '媒体':0,
    '航天':0,
    '海事':0,
}
xdgroup = {
    '研究学院':0,
    '电信运营商':0,
    '互联网':0,
    '信息科技':0,
    '车辆工程':0,
    '金融':0,
    '国企':0,
    '文化':0,
    '教培':0,
    '媒体':0,
    '航天':0,
    '海事':0,
}
cdgroup = {
    '研究学院':0,
    '电信运营商':0,
    '互联网':0,
    '信息科技':0,
    '车辆工程':0,
    '金融':0,
    '国企':0,
    '文化':0,
    '教培':0,
    '媒体':0,
    '航天':0,
    '海事':0,
}
with open('分类.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if row[3] == '北邮':
            if row[2] != '其他':
                bygroup[row[2]] += int(row[-1])
        elif row[3] == '成电':
            if row[2] != '其他':
                cdgroup[row[2]] += int(row[-1])
        elif row[3] == '西电':
            if row[2] != '其他':
                xdgroup[row[2]] += int(row[-1])
print('最受北邮学生欢迎关注的雇主类型TOP10为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')' for i in sorted([[i,j] for i,j in bygroup.items()],key=lambda x:x[1],reverse=True)[:10]]))
print('最受西电学生欢迎关注的雇主类型TOP10为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')' for i in sorted([[i,j] for i,j in xdgroup.items()],key=lambda x:x[1],reverse=True)[:10]]))
print('最受成电学生欢迎关注的雇主类型TOP10为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')' for i in sorted([[i,j] for i,j in cdgroup.items()],key=lambda x:x[1],reverse=True)[:10]]))
mem = []
with open('BEIYOU_1.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            mem.append([row[1],int(row[-1])])
        except:
            pass
print('北邮招聘职位总数,招聘职位数量top10为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')'  for i in sorted(mem[1:],key=lambda x:x[1],reverse=True)[:10]]))
bygroup = {
    '研究学院':0,
    '电信运营商':0,
    '互联网':0,
    '信息科技':0,
    '车辆工程':0,
    '金融':0,
    '国企':0,
    '文化':0,
    '教培':0,
    '媒体':0,
    '航天':0,
    '海事':0,
}
with open('分类.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if row[3] == '北邮':
            if row[2] != '其他':
                for i in mem:
                    if row[1] == i[0]:
                        bygroup[row[2]] += int(i[-1])
print('北邮招聘职位个数所属雇主类型TOP10为：' + ',   '.join([i[0] + '(' + str(i[1]) + ')'  for i in sorted([[i,j] for i,j in bygroup.items()],key=lambda x:x[1],reverse=True)[:10]]))
sametime = []
with open('分类.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        sametime.append(row[1])
t = []
h = []
with open('分类.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        h.append([row[1],row[-1]])
for i in sorted([i for i,j in Counter(sametime).items() if i and i !='招聘主题'],key=lambda x:x[1],reverse=True)[:10]:
    t.append([i,0])
    for j in h:
        if j[0] == i:
            t[-1][1] += int(j[1])
t.sort(key=lambda x:x[1],reverse=True)
print('最关注ICT行业的招聘主题TOP10为：' + ',   '.join(i[0] + '(' + str(i[1]) + ')'  for i in t))

