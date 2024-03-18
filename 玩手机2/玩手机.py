import csv
import matplotlib.pyplot as plt
data = []
phone = []
#打开csv文件，读取所有行数据
with open('玩手机.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            v1 = row[0]
            v2 = row[2]
            v3 = row[3]
            v3.replace(' ','')
            line = [v1,v2,v3]
            data.append(line)
        except:
            pass
#切片头行属性行
data = data[1:]
print(data)
#从数据中筛选出玩手机的数据，添加进新列表中
for i in data:
    if i[1] == '玩手机':
        phone.append(i)

#玩手机时间
date = []
#对应日期
time = []
res = []
#遍历数组，将日期与时间分别存入数组
for i in phone:
    d = i[0]
    #对日期数据进行清洗简化，防止X轴坐标过长
    i[0] = i[0].replace('2021/','')
    i[0] = i[0].replace('/2021', '')
    i[0] = i[0].replace('/', '')
    #筛选日期，只保留12月份以后的数据
    if int(i[0]) > 1200:
        res.append(i)
print(res)
for i in res:
    date.append(i[0])
    # 将时长数据转化为int
    t = i[2]
    t = int(t)
    time.append(t)
print(date)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title('玩手机时间')
plt.bar(
    date,
    time,
    width=0.5,
    )
#调整X轴字体大小
plt.tick_params(labelsize=6)
plt.show()