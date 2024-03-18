import numpy as np
import csv
import time as teee

start = teee.time()
timeline = {}
data = []
maxsize = 0
minsize = 999999999999
code = []
encode = {}
decode = {}
with open('测试例子.csv',encoding='utf-8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            data.append([row[1],row[2],row[3],int(row[4]),int(row[5])])
            maxsize = max(maxsize,int(row[4]))
            code.append(int(row[4]))
        except:
            pass
for i in data:
    if i[3] == 0:
        if i[2] == 'B':
            i[3] = maxsize
code = sorted(list(set(code)))
for i in range(len(code)):
    encode[code[i]] = i
    decode[i] = code[i]
for i in data:
    i[3] = encode[i[3]]
maxsize = len(code)

# rnew = [['价格']]
# for i in code:
#     rnew.append([str(i)])
testf = open('输出.csv','w')
time = data[0][0]
warline = [[0,[]] for i in range(maxsize)]
flags = maxsize-1
for i in data:
    # print(i)
    if i[0] != time:
        aw2 = []
        awtime = str(time)
        timeline[time] = warline[::]
        time = i[0]
        timeline[time] = []
        for r in range(1,len(code)+1):
            f = []
            tp = {}
            ta = []
            for q in warline[r-1][1]:
                try:
                    tp[q[-1]].append(str(q[0]))
                except:
                    tp[q[-1]] = [str(q[0])]
            for key,value in tp.items():
                ta.append([key,value])
            ta.sort(key=lambda x:x[0])
            for timenum in range(1,len(ta)):
                if int(ta[timenum][0]) - int(ta[timenum-1][0]) < 30:
                    ta[timenum][1] = ta[timenum][1] + ta[timenum-1][1]
                    ta[timenum-1] = 0
            while 1:
                # print(1)
                try:
                    ta.remove(0)

                except:
                    # print('---------------------------')
                    break
            for _ta in ta:
                if len(_ta[1]) > 1:
                    f.append(str(sum(map(int,_ta[1]))) + ' (' + '，'.join(_ta[1]) + ')')
                else:
                    f.append(_ta[1][0])
            if warline[r-1][0] == 0:
                aw2.append(str(warline[r-1][0]))
            else:
                aw2.append(str(warline[r-1][0]) +'(' + '，'.join(f) + ')')
        aw2 = aw2[::-1]
        aw2.insert(0,awtime)
        testf.write(','.join(aw2) + '\n')
    if i[2] == 'B':
        for j in range(i[3]+1):
            if i[-1] == 0:
                break
            if warline[j][0] <=0 and j!=i[3]:
                continue
            elif warline[j][0] <=0 and j==i[3]:
                warline[j][0] -= i[-1]
                warline[j][1].append([i[-1],i[1],i[0]])
            elif warline[j][0] > 0 and j!=i[3]:
                while(1):
                    # print(2)
                    if warline[j][1][0][0] <= i[-1]:
                        i[-1] -= warline[j][1][0][0]
                        warline[j][0] -= warline[j][1][0][0]
                        del warline[j][1][0]
                        if warline[j][0] == 0:
                            break
                    else:
                        warline[j][1][0][0] -= i[-1]
                        warline[j][0] -= i[-1]
                        i[-1] = 0
                        break
            elif warline[j][0] > 0 and j==i[3]:
                while (1):
                    # print(3)
                    try:
                        if warline[j][1][0][0] <= i[-1]:
                            i[-1] -= warline[j][1][0][0]
                            warline[j][0] -= warline[j][1][0][0]
                            del warline[j][1][0]
                            if warline[j][0] == 0:
                                warline[j][0] -= i[-1]
                                warline[j][1].append([i[-1],i[1],i[0]])
                                break
                        else:
                            warline[j][1][0][0] -= i[-1]
                            warline[j][0] -= i[-1]
                            i[-1] = 0
                            break
                    except:
                        break
    elif i[2] == 'S':
        for j in range(maxsize-1,i[3]-1,-1):
            if i[-1] == 0:
                break
            if warline[j][0] >=0 and j!=i[3]:
                continue
            elif warline[j][0] >=0 and j==i[3]:
                warline[j][0] += i[-1]
                warline[j][1].append([i[-1],i[1],i[0]])
            elif warline[j][0] < 0 and j!=i[3]:
                while(1):
                    # print(4)
                    if warline[j][1][0][0] <= i[-1]:
                        i[-1] -= warline[j][1][0][0]
                        warline[j][0] += warline[j][1][0][0]
                        del warline[j][1][0]
                        if warline[j][0] == 0:
                            break
                    else:
                        warline[j][1][0][0] -= i[-1]
                        warline[j][0] += i[-1]
                        i[-1] = 0
                        break
            elif warline[j][0] < 0 and j==i[3]:
                while (1):
                    # print(5)
                    if warline[j][1][0][0] <= i[-1]:
                        i[-1] -= warline[j][1][0][0]
                        warline[j][0] += warline[j][1][0][0]
                        del warline[j][1][0]
                        if warline[j][0] == 0:
                            warline[j][0] += i[-1]
                            warline[j][1].append([i[-1],i[1],i[0]])
                            break
                    else:
                        warline[j][1][0][0] -= i[-1]
                        warline[j][0] += i[-1]
                        i[-1] = 0
                        break
    elif i[2] == 'C':
        for j in range(len(warline[i[-2]][1])):
            if warline[i[-2]][1][j][1] == i[1]:
                if warline[i[-2]][1][j][0] <= i[-1]:
                    if warline[i[-2]][0] > 0:
                        warline[i[-2]][0] -= warline[i[-2]][1][j][0]
                    else:
                        warline[i[-2]][0] += warline[i[-2]][1][j][0]
                    del warline[i[-2]][1][j]
                else:
                    if warline[i[-2]][0] > 0:
                        warline[i[-2]][0] -= i[-1]
                    else:
                        warline[i[-2]][0] += i[-1]
                    warline[i[-2]][1][j][0] -= i[-1]
                break
aw2 = []
i = data[-1]
awtime = str(time)
timeline[time] = warline[::]
time = i[0]
timeline[time] = []

for r in range(1,len(code)+1):
    f = []
    tp = {}
    ta = []
    for q in warline[r-1][1]:
        try:
            tp[q[-1]].append(str(q[0]))
        except:
            tp[q[-1]] = [str(q[0])]
    for key,value in tp.items():
        ta.append([key,value])
    ta.sort(key=lambda x:x[0])
    for timenum in range(1,len(ta)):
        if int(ta[timenum][0]) - int(ta[timenum-1][0]) < 30:
            ta[timenum][1] = ta[timenum][1] + ta[timenum-1][1]
            ta[timenum-1] = 0
    while 1:
        # print(6)
        try:
            ta.remove(0)
        except:
            break
    for _ta in ta:
        if len(_ta[1]) > 1:
            f.append(str(sum(map(int,_ta[1]))) + ' (' + '，'.join(_ta[1]) + ')')
        else:
            f.append(_ta[1][0])
    if warline[r-1][0] == 0:
        aw2.append(str(warline[r - 1][0]))
    else:
        aw2.append(str(warline[r-1][0]) +'(' + '，'.join(f) + ')')
aw2 = aw2[::-1]
aw2.insert(0,awtime)
testf.write(','.join(aw2) + '\n')
elapsed = (teee.time() - start)
print("Time used:",elapsed)
testf.close()
data = []
with open('输出.csv') as f_read:
    while True:
        line = f_read.readline()
        if not line:
            break
        data.append(line.replace('\n','').split(','))
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


