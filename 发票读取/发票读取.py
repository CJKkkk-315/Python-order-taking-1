import pdfplumber
import os
import csv
ext='.pdf'
res = []
files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1]==ext]
for file in files:
    with pdfplumber.open(file) as pdf:
        first_page = pdf.pages[0]
        for i in first_page.extract_text().split('\n'):
            print(i)
            if i[:4] == '发票号码':
                id = i[5:]
            if i[:4] == '开票日期':
                time = i[5:]
            if i[:5] == '购 名 称':
                name = i[7:].split(' ')[0]
            if i[:5] == '名 称： ':
                cname = i[5:].split(' ')[0]
            if i[0] == '*':
                aw = i.split(' ')
                serve = aw[0]
                num = aw[3]
                price = aw[4]
                all = aw[5]
                ra = aw[6]
                ranum = aw[7]
        res.append([name,id,time,cname,serve,num,price,all,ra,ranum])
with open('输出.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['购买方名称','发票号码','发票日期','销售方名称','服务名称','数量','单价','总价','税率','税额'])
    for i in res:
        f_csv.writerow(i)
