def merge(intervals):
    res = []
    intervals.sort()
    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1], i[1])
    return res
import xlrd
import csv
data = xlrd.open_workbook('gff.xls')
table = data.sheets()[2]
data = []
for i in range(table.nrows):
    aw = []
    for j in range(table.ncols):
        aw.append(table.cell_value(i, j))
    data.append(aw)
dic = {}
for i in data:
    try:
        dic[i[0]].append([i[2],i[3]])
    except:
        dic[i[0]] = [[i[2],i[3]]]
for i,j in dic.items():
    dic[i] = merge(j)
rows = []
for i,j in dic.items():
    for t in j:
        rows.append([i,'gene',t[0],t[1]])
with open('结果.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in rows:
            f_csv.writerow(i)
