import csv
d = []
with open('用户数据.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        d.append(row)
data1 = []
for i in d:
    s = i[5]
    if s and s != '其他' and s != '不限' and s != '省/直辖市':
        if i not in data1:
            data1.append(i)
print(len(data1))
for i in data1:
    if i[-1] == '0':
        i[-1] = '未认证'
    else:
        i[-1] = '已认证'
data1 = data1[:5086]
with open('用户数据(清洗后)(5000).csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in data1:
        try:
            f_csv.writerow(i)
        except:
            pass