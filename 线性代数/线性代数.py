import xlrd
data = xlrd.open_workbook('测试集.xls')
sheet1 = data.sheets()[0]
sheet2 = data.sheets()[1]
G1ALL = 0
G2ALL = 0
t1 = 0
t2 = 0
t3 = 0
f1 = 0
f2 = 0
f3 = 0
for i in range(1,sheet1.nrows):
    G1ALL += sheet1.cell_value(i, 1)
for i in range(1,sheet2.nrows):
    G2ALL += sheet2.cell_value(i, 1)
for i in range(1,sheet1.nrows):
    t1 += sheet1.cell_value(i, 2)*sheet1.cell_value(i, 1)/G1ALL
f1 = G1ALL - G2ALL*t1
for i in range(1,sheet1.nrows):
    t2 += sheet1.cell_value(i, 2)*(sheet1.cell_value(i, 1)/G1ALL - sheet2.cell_value(i, 1)/G2ALL)
f2 = G1ALL * t2
for i in range(1,sheet1.nrows):
    t3 += (sheet1.cell_value(i, 2)-sheet2.cell_value(i, 2))*sheet1.cell_value(i, 1)/G1ALL
f3 = G1ALL * t3
print(f1)
print(f2)
print(f3)
print(f1+f2+f2)