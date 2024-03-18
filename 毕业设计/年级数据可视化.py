import openpyxl
import os
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Page
from pyecharts import options as opts
# 读取学分绩点排名下所有文件名
files = os.listdir(os.getcwd() + '\\学分绩点排名')
data = [[],[],[]]
# 遍历读取的文件
for file in files:
    # 依次将数据写入到datas中
    wb = openpyxl.load_workbook(os.getcwd() + '\\学分绩点排名\\' + file)
    sheet_names = wb.get_sheet_names()
    ws = wb.get_sheet_by_name(sheet_names[0])
    for i in ws.iter_rows():
        r = []
        for cell in i:
            # 跳过第一行表头
            if cell.value == '学号':
                break
            r.append(cell.value)
        # 根据不同年级，添加进不同列表
        data[int(file[:2])-18].append(r)
aw = data[::]
data = [[],[],[]]
# 清楚掉空数据
for i in aw[0]:
    if i :
        data[0].append(i)
for i in aw[1]:
    if i :
        data[1].append(i)
for i in aw[2]:
    if i :
        data[2].append(i)
# 求出每个年级的平均分
ave = [round(sum([float(j[8]) for j in i])/len(i),2) for i in data]
print(ave)
# 求出每个年级的平均绩点
avepoint = [round(sum([float(j[10]) for j in i])/len(i),2) for i in data]
# 求出每个年级的挂科率
fall = [sum([j[7] != '100%' for j in i]) for i in data]
# 利用pyecharts分别画图
bar1 = (
    Bar()
    .add_xaxis(["18年级", "19年级", "20年级"])
    .add_yaxis("平均分", ave,yaxis_index=0,)
    .add_yaxis("加权平均分", avepoint,yaxis_index=0,)
    .extend_axis(yaxis=opts.AxisOpts())
    .set_global_opts(title_opts=opts.TitleOpts(title="学生平均分及不及格人数情况"))
)
bar2 = (
    Bar()
    .add_xaxis(["18年级", "19年级", "20年级"])
    .add_yaxis("不及格人数", fall,yaxis_index=1)

)
bar1.overlap(bar2)
bar1.render('年级学生平均分及不及格人数情况.html')
fenbu = [0,0,0]
# 计算不同年级的成绩分布情况，画出3张图
for j in data[0]:
        if float(j[8]) > 80:
            fenbu[0] += 1
        elif float(j[8]) < 80 and float(j[8]) > 70:
            fenbu[1] += 1
        else:
            fenbu[2] += 1
pie1=(
        Pie()
        .add("", [list(z) for z in zip(['>80分人数','70-80分人数','<70分人数'], fenbu)])
        .set_global_opts(title_opts=opts.TitleOpts(title="18学生平均分分布情况"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
fenbu = [0,0,0]
for j in data[1]:
        if float(j[8]) > 80:
            fenbu[0] += 1
        elif float(j[8]) < 80 and float(j[8]) > 70:
            fenbu[1] += 1
        else:
            fenbu[2] += 1
pie2=(
        Pie()
        .add("", [list(z) for z in zip(['>80分人数','70-80分人数','<70分人数'], fenbu)])
        .set_global_opts(title_opts=opts.TitleOpts(title="19学生平均分分布情况"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
fenbu = [0,0,0]
for j in data[2]:
        if float(j[8]) > 80:
            fenbu[0] += 1
        elif float(j[8]) < 80 and float(j[8]) > 70:
            fenbu[1] += 1
        else:
            fenbu[2] += 1
pie3=(
        Pie()
        .add("", [list(z) for z in zip(['>80分人数','70-80分人数','<70分人数'], fenbu)])
        .set_global_opts(title_opts=opts.TitleOpts(title="20学生平均分分布情况"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
page = Page(layout=Page.SimplePageLayout)
page.add(pie1,pie2,pie3)
page.render("年级学生平均分分布情况.html")