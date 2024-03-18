import csv
import math
dataf = []
head = ['fips','cases','deaths','date']
nan = []
with open('us-counties.csv',encoding='utf-8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if row[3] == 'fips':
            continue
        if row[4] == '' or row[5] == '':
            continue
        if row[3] == '':
            nan.append(row)
            continue
        if row[0] == '2022-01-26':
            if int(row[4]) == 0:
                row[4] = 1
            if int(row[5]) == 0:
                row[5] = 1
            dataf.append([row[3],math.log(int(row[4]),10)+1,math.log(int(row[5]),10)+1,row[0]])
with open('数据.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in dataf:
        f_csv.writerow(i)
with open('空值.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in nan:
        f_csv.writerow(i)