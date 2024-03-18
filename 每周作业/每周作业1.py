city1 = {1:-18,2:-15,3:0,4:10,5:24,6:28,7:30,8:30,9:25,10:12,11:5,12:-10}
city2 = {1:5,2:16,3:20,4:25,5:30,6:35,7:38,8:38,9:35,10:30,11:20,12:15}
# sy1-1.py
import csv
head = ['城市','月份1','月份2','月份3','月份4','月份5','月份6','月份7','月份8','月份9','月份10','月份11','月份12']
with open('city_temp.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    f_csv.writerow(['北方甲市',city1[1],city1[2],city1[3],city1[4],city1[5],city1[6],city1[7],city1[8],city1[9],city1[10],city1[11],city1[12]])
    f_csv.writerow(['南方乙市',city2[1],city2[2],city2[3],city2[4],city2[5],city2[6],city2[7],city2[8],city2[9],city2[10],city2[11],city2[12]])
# sy1-2.py
import csv
data = []
with open('city_temp.csv',encoding="gbk")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
data = data[1:]
maxn = -100
maxi = 0
min = 100
mini = 0
for i in range(1,len(data[0])):
    if int(data[0][i]) > maxn:
        maxn = int(data[0][i])
        maxi = i
    if int(data[0][i]) < min:
        min = int(data[0][i])
        mini = i
maxil = []
minil = []
for i in range(1,len(data[0])):
    if int(data[0][i]) == maxn:
        maxil.append(str(i))
for i in range(1,len(data[0])):
    if int(data[0][i]) == min:
        minil.append(str(i))
print('北方甲市最高温为：' + str(maxn) + '  ' + ','.join(maxil) + '月')
print('北方甲市最低温为：' + str(min) + '  ' +  ','.join(minil) + '月')
maxn = -100
maxi = 0
min = 100
mini = 0
for i in range(1,len(data[1])):
    if int(data[1][i]) > maxn:
        maxn = int(data[1][i])
        maxi = i
    if int(data[1][i]) < min:
        min = int(data[1][i])
        mini = i
maxil = []
minil = []
for i in range(1,len(data[1])):
    if int(data[1][i]) == maxn:
        maxil.append(str(i))
for i in range(1,len(data[1])):
    if int(data[1][i]) == min:
        minil.append(str(i))
print('南方乙市最高温为：' + str(maxn) + '  ' + ','.join(maxil) + '月')
print('南方乙市最低温为：' + str(min) + '  ' + ','.join(minil) + '月')
# sy1-3.py
data = []
with open('city_temp.csv',encoding="gbk")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
data = data[1:]
maxn = 0
maxi = 0
for i in range(1,len(data[0])):
    if abs(int(data[0][i]) - int(data[1][i])) > maxn:
        maxn = abs(int(data[0][i]) - int(data[1][i]))
        maxi = i
print('温差最大为：' + str(maxn) + '  ' + str(maxi) + '月')
# sy1-4.py
data = []
with open('city_temp.csv',encoding="gbk")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
data = data[1:]
data1 = data[0]
res1 = []
data2 = data[1]
for i in range(1,13):
    a = []
    for j in range(7):
        if i+j > 12:
            t = i+j-12
        else:
            t = i+j
        a.append(int(data1[t]))
    res1.append(a)
res1 = [len([j for j in i if j < 20]) for i in res1]
if 0 in res1:
    print('北方甲市满足要求')
else:
    print('北方甲市不满足要求')
res1 = []
for i in range(1,13):
    a = []
    for j in range(7):
        if i+j > 12:
            t = i+j-12
        else:
            t = i+j
        a.append(int(data2[t]))
    res1.append(a)
res1 = [len([j for j in i if j < 20]) for i in res1]
# print(res1)
if 0 in res1:
    print('南方乙市满足要求')
else:
    print('南方乙市不满足要求')
# sy1-5
data = []
with open('city_temp.csv',encoding="gbk")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
data = data[1:]
dic1 = {}
dic2 = {}
for i in range(1,len(data[0])):
    dic1[str(i)] = int(data[0][i])
for i in range(1,len(data[1])):
    dic2[str(i)] = int(data[1][i])
print('北方甲市:' + str(dic1))
print('南方乙市:' + str(dic2))


