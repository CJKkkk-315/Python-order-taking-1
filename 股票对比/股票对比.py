import csv
data1 = []
data2 = []
data2f = []
# 对买卖编码为1和2，方便后续对比处理
bs = {'Sell':'2','Buy':'1'}
# 将source2文件所需要的列数据读入data2列表中
with open('Execution_source2.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        try:
            data2.append([row[3],row[5],float(row[6]),float(row[7]),bs[row[8]],float(row[10])])
        except:
            pass
dic = {}
# print(data2)
# 对data2数据按照orderid进行归类，相同orderid归为一类
for i in data2:
    try:
        dic[i[0]].append(i)
    except:
        dic[i[0]] = [i]
# 归类以后遍历每组orderid，对有重复orderid的数据，交易量和税费求和，价格求平均
for i,j in dic.items():
    if len(j) == 1:
        data2f.append([j[0][1][2:],j[0][2],j[0][3],j[0][4],j[0][5]])
    else:
        all = sum([n[3] for n in j])
        p = sum(n[3]/all*n[2] for n in j)
        f = sum(n[5] for n in j)
        data2f.append([j[0][1][2:],round(p,3),all,j[0][4],round(f,2)])
# 将source1文件所需要的列数据读入data1列表中
with open('Execution_source1.txt',encoding='utf-8')as f:
    data1 = f.readlines()
# 将data1按行分组，只保留我们需要的行
data1 = [[j for j in i.replace('\n','').split(' ') if j] for i in data1 if i[:8] == '20211210']
data1 = [i for i in data1 if i[4][:4] != '证券冻结'][2:]
# 同样对data1买卖进行编码
bs = {'证券买入':'1','证券卖出':'2'}
# 对data1交易金额进行处理，去掉逗号改为数字形式，同时将印花税和手续费相加
data1f = [[i[4][4:10],float(i[6]),float(i[5].replace(',','')),bs[i[4][:4]],round(float(i[9]) + float(i[10]),2)] for i in data1]
# 对两组数据进行排序 方便后续比较时加快速度
data1f.sort(key=lambda x:x[0])
data2f.sort(key=lambda x:x[0])
res = []
# 将两组数据进行比较，查看除去税费以外是否所有数据相同，将不同的数据单独加入到res列表中
for i in data1f:
    flag = 0
    for j in data2f:
        if i[:4] == j[:4]:
            flag = 1
            break
    if flag == 0:
        res.append(i + [1])
for i in data2f:
    flag = 0
    for j in data1f:
        if i[:4] == j[:4]:
            flag = 1
            break
    if flag == 0:
        res.append(i + [2])
# print(res)
# 对res的买卖和来源进行逆编码
bs = {'1':'Buy','2':'Sell'}
s = {1:'Execution_source1.txt',2:'Execution_source2.csv'}
head = ['Source','ContractId','Price','Volume','Direction','Fee']
code ={'60':'11','30':'21','00':'21','15':'22'}
# 将最后结果写入到answer.csv中
with open('answer.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in res:
        f_csv.writerow([s[i[-1]],code[i[0][:2]]+i[0],i[1],i[2],bs[i[3]],i[4]])
