import csv
a = []
b = []
with open('房价.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        a.append(row[0])
        b.append(row[1])
c = []
d = []
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
        d.append(b[i])
res = []
for i in range(len(c)):
    res.append([c[i],d[i]])
    # print(res)
with open('数据2.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)