import csv
code = []
with open('测试例子.csv',encoding='utf-8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            code.append(int(row[4]))
        except:
            pass
data = []
with open('输出.csv') as f_read:
    while True:
        line = f_read.readline()
        if not line:
            break
        data.append(line.split(','))
code = sorted(list(set(code)))
head = ['价格']
for i in code[::-1]:
    head.append(str(i))
data.insert(0,head)
data = [[row[i] for row in data] for i in range(len(data[0]))]
n = 0
with open('输出.csv','w',newline='')as f:
    for row in data:
        f.write(','.join(row) + '\n')