
import sqlite3
import openpyxl
import os
# 读取学分绩点排名下所有文件名
files = os.listdir(os.getcwd() + '\\学分绩点排名')
datas = []
# 遍历读取的文件
for file in files:
    # 依次将数据写入到datas中
    wb = openpyxl.load_workbook(os.getcwd() + '\\学分绩点排名\\' + file)
    sheet_names = wb.get_sheet_names()
    ws = wb.get_sheet_by_name(sheet_names[0])
    for i in ws.iter_rows():
        r = []
        for cell in i:
            if cell.value == '学号':
                break
            r.append(cell.value)
        if r:
            datas.append(tuple([r[0],r[1],r[2],r[8]]))
print(datas)
# 连接sqlite3数据库
conn = sqlite3.connect("student_data.db")
c = conn.cursor()
# 尝试创建表
try:
    c.execute('''CREATE TABLE Student
          (ID INT PRIMARY KEY     NOT NULL,
          NAME           TEXT    NOT NULL,
          SCORE            INT     NOT NULL,
          AVE              FLOAT   NOT NULL);''')
# 若创建失败， 则说明表已经存在
except:
    pass
# 调用sql语句，将数据写入
sql = 'insert into Student (ID, NAME, SCORE, AVE) values(?, ?, ?, ?)'
with conn:
    conn.executemany(sql, datas)
