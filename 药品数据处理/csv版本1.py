def function11():
    def function1():
        import csv
        import xlwt
        data = []
        target1 = int(u.get())-1
        target2 = int(e.get())-1
        with open('sheet1.csv','r')as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                data.append(row[:255])
        c1 = data[:1][0]
        s1 = data[1:]
        # print(s1)
        # target1 = int(input('请输入sheet1要对比的是第几列:')) - 1
        for i in range(len(s1)):
            for j in range(len(s1[i])):
                if j == target1:
                    s1[i][j] = s1[i][j].replace(' ','')
        data = []
        with open('sheet2.csv','r',errors='ignore')as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                data.append(row[:255])
        c2 = data[:1][0]
        s2 = data[1:]
        # target2 = int(input('请输入sheet2要对比的是第几列:')) - 1
        for i in range(len(s2)):
            for j in range(len(s2[i])):
                if j == target1:
                    s2[i][j] = s2[i][j].replace(' ','')
        s3 = []
        for i in s1:
            for j in s2:
                if i[target1] == j[target2]:
                    s3.append(i)
                    break
        s4 = []
        for i in s2:
            for j in s1:
                if i[target2] == j[target1]:
                    s4.append(i)
                    break
        s3.sort(key=lambda x:x[target1])
        s4.sort(key=lambda x:x[target2])
        style1 = xlwt.easyxf('')
        style2 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')
        workbook = xlwt.Workbook(encoding = 'utf-8')
        sheet3 = workbook.add_sheet('sheet3',cell_overwrite_ok=True)
        for i in range(len(c1)):
            sheet3.write(0, i, label=c1[i])
        for i in range(1,len(s3)):
            for j in range(len(c1)):
                try:
                    if s3[i-1][target1] == s3[i][target1] or s3[i-1][target1] == s3[i-2][target1]:
                        sheet3.write(i,j,label = s3[i-1][j],style = style2)
                    else:
                        sheet3.write(i, j, label=s3[i-1][j], style=style1)
                except:
                    sheet3.write(i, j, label=s3[i-1][j], style=style1)
        workbook.save('sheet3.xls')
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet4 = workbook.add_sheet('sheet4',cell_overwrite_ok=True)
        for i in range(len(c2)):
            sheet4.write(0, i, label=c2[i])
        for i in range(1,len(s4)):
            for j in range(len(c2)):
                try:
                    if s4[i-1][target2] == s4[i][target2] or s4[i-1][target2] == s4[i-2][target2]:
                        sheet4.write(i,j,label = s4[i-1][j],style = style2)
                    else:
                        sheet4.write(i, j, label=s4[i-1][j], style=style1)
                except:
                    sheet4.write(i, j, label=s4[i-1][j], style=style1)
        workbook.save('结果.xls')
    # function1()
    import tkinter as tk
    window=tk.Tk()
    window.title('')
    window.geometry('450x300')
    tk.Label(window,text='请输入sheet1要对比的列:').place(x=30,y=100)
    tk.Label(window,text='请输入sheet2要对比的列:').place(x=30,y=140)
    u=tk.Entry(window)
    u.place(x=190,y=100)
    e=tk.Entry(window)
    e.place(x=190,y=140)
    bt_login=tk.Button(window,text='开始',command=function1)
    bt_login.place(x=140,y=230)
    #主循环
    window.mainloop()