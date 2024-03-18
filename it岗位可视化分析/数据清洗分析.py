import csv
data = []
# 打开未清洗的数据
with open('数据.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        #将其全部读入data列表中
        data.append(row)
dataf = []
# 设置各个关键词，不区分大小写，用来判断是否有错误的数据
keys = [['JAVA','java','Java'],['C++','c++','c'],['Python','python','PYTHON'],['前端'],['测试'],['Android','ANDROID','android'],['算法'],['数据'],['LINUX','Linux','linux']]
# 遍历列表，对列表的岗位分类找到keys中对应的关键词，再判断对应的关键词是否出现在了岗位名称中，若一个都没有出现，则判断为错误数据，不将其插入新列表
for i in data:
    flag = 1
    for key in keys:
        for word in key:
            if word in i[0]:
                for w in key:
                    if w in i[2]:
                        flag = 0
                        dataf.append(i)
                        break
res = []
# 遍历去除错误数据后的新列表
for i in dataf:
    # 对每个薪资以-符号分隔为2个元素
    if '-' in i[3]:
        aw = i[3].split('-')
        # 第一个元素即为薪资下限 第二个元素的数字部分即为薪资上限
        low = float(aw[0])
        # 在第二个元素中判断单位和时间，统一转化为月/万的
        if '万' in aw[1]:
            hight = float(aw[1].split('万')[0])
        elif '千' in aw[1]:
            hight = float(aw[1].split('千')[0])
            hight /= 10
            low /=10
        if '年' in aw[1]:
            hight /= 12
            low /= 12
        # 将完全处理好的数据加入到最后列表中
        res.append([i[0],i[1],i[2],round((hight+low)/2,2)])
# 将清洗后的数据写入csv文件中
with open('数据(清洗后).csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)

