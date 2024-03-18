import openpyxl
import os
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts import options as opts
# 读取学分绩点排名下所有文件名
files = os.listdir(os.getcwd() + '\\学分绩点排名')
data = {}
# 遍历读取的文件
for file in files:
    # 获取每条数据的专业
    key = ''.join([i for i in file if not i.isdigit()]).split('.')[0].replace('班','')
    wb = openpyxl.load_workbook(os.getcwd() + '\\学分绩点排名\\' + file)
    sheet_names = wb.get_sheet_names()
    ws = wb.get_sheet_by_name(sheet_names[0])
    # 将不同专业的数据存入到字典中
    for i in ws.iter_rows():
        r = []
        for cell in i:
            if cell.value == '学号':
                break
            r.append(cell.value)
        if r:
            try:
                data[key].append(r)
            except:
                data[key] = [r]
res = []
print(data)
# 分别计算不同专业的平均成绩，平均绩点和挂科率，添加到列表中
for key,value in data.items():
    a = round(sum([float(i[8]) for i in value])/len(value),2)
    b = round(sum([float(i[10]) for i in value])/len(value),2)
    c = sum(i[7] != '100%' for i in value)
    res.append([key,a,b,c])
key = [i[0] for i in res]
n1 = [i[1] for i in res]
n2 = [i[2] for i in res]
n3 = [i[3] for i in res]
# 利用上述求得的列表分别求不同专业平均分，不及格人数，以及分数分布情况
bar1 = (
    Bar()
    .add_xaxis(key)
    .add_yaxis("平均分", n1,yaxis_index=0,)
    .add_yaxis("加权平均分", n2,yaxis_index=0,)
    .extend_axis(yaxis=opts.AxisOpts())
    .set_global_opts(title_opts=opts.TitleOpts(title="学生平均分及不及格人数情况"))
)
bar2 = (
    Bar()
    .add_xaxis(key)
    .add_yaxis("不及格人数", n3,yaxis_index=1)

)
bar1.overlap(bar2)
bar1.render('专业学生平均分及不及格人数情况.html')
keys = []
res1 = []
res2 = []
res3 = []
for key,value in data.items():
    fenbu = [0,0,0]
    for j in value:
        if float(j[8]) > 80:
            fenbu[0] += 1
        elif float(j[8]) < 80 and float(j[8]) > 70:
            fenbu[1] += 1
        else:
            fenbu[2] += 1
    keys.append(key)
    res1.append(fenbu[0])
    res2.append(fenbu[1])
    res3.append(fenbu[2])
bar = (
    Bar()
    .add_xaxis(keys)
    .add_yaxis(">80分人数", res1)
    .add_yaxis("70-80分人数", res2)
    .add_yaxis("<70分人数", res3)
    .set_global_opts(title_opts=opts.TitleOpts(title="学生平均分分布情况"))
)
bar.render('专业学生平均分分布情况.html')