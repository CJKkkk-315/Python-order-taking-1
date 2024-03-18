import csv
data = []
with open('数据.csv','r') as f:
    ff = csv.reader(f)
    for i in ff:
        data.append(i[-3])
print(len(data))