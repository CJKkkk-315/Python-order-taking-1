import csv
from collections import Counter
price = []
name = []
p = []

with open('楼盘名.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        price.append(row[0])
with open('房价.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        name.append(row[0])
        p.append(row[1])
n = [0 for i in range(len(price))]
print(price)
# print(len(p))
for i in range(len(name)):
    if name[i] in price:
        try:
            n[price.index(name[i])] = p[i]
        except:
            # print(name[i])
            pass
res = []
print(len(n))
for i in range(len(n)):
    res.append([price[i],n[i]])
    # print(res)
print(Counter(n))
with open('数据.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)