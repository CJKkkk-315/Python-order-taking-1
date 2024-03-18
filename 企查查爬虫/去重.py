import csv
data = []
name = []
with open('数据.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if row[0] not in name:
            data.append(row)
            name.append(row[0])
with open('数据(去重后).csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        try:
            f_csv.writerow(i)
        except:
            pass