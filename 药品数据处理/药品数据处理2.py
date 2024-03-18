def function22():
    def function1():
        import xlrd
        import csv
        data = xlrd.open_workbook('结果.xls')
        table3 = data.sheets()[0]
        table4 = data.sheets()[1]
        wh3 = []
        wh4 = []
        data3 = []
        data4 = []
        cc3 = ['']
        cc4 = ['']
        target3 = int(u.get())-1
        target4 = int(e.get())-1
        # target3 = int(input('请输入sheet1要对比的是第几列:')) - 1
        # target4 = int(input('请输入sheet2要对比的是第几列:')) - 1
        for i in range(table3.ncols):
            cc3.append(table3.cell_value(0, i))
        for i in range(table4.ncols):
            cc4.append(table4.cell_value(0, i))
        # for i in range(table3.ncols):
        #     if table3.cell_value(0, i) == '批准文号':
        #         target3 = i
        # for i in range(table4.ncols):
        #     if table4.cell_value(0, i) == '批准文号':
        #         target4 = i
        for i in range(1,table3.nrows):
            r = []
            for j in range(table3.ncols):
                if j == target3:
                    wh = table3.cell_value(i, j)
                a = table3.cell_value(i, j)
                r.append(a)
            if wh not in wh3:
                wh3.append(wh)
                data3.append(r)
            else:
                pass
        for i in range(1,table4.nrows):
            r = []
            for j in range(table4.ncols):
                if j == target4:
                    wh = table4.cell_value(i, j)
                a = table4.cell_value(i, j)
                r.append(a)
            if wh not in wh4:
                wh4.append(wh)
                data4.append(r)
            else:
                pass
        c3 = int(u1.get())-1
        c4 = int(e1.get())-1
        # c3 = int(input('请输入sheet3要对比的是第几列：')) - 1
        # c4 = int(input('请输入sheet4要对比的是第几列：')) - 1
        res1 = []
        res2 = []
        for i,j in zip(data3,data4):
            if i[c3] != j[c4]:
                res1.append([j[c4]]  + i)
                res2.append([i[c3]] + j)
        with open('sheet5.csv','w',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(cc3)
            for i in res1:
                f_csv.writerow(i)
        with open('sheet6.csv','w',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(cc4)
            for i in res2:
                f_csv.writerow(i)
    import tkinter as tk
    window=tk.Tk()
    window.title('')
    window.geometry('450x300')
    tk.Label(window,text='请输入sheet1要对比的列:').place(x=30,y=60)
    tk.Label(window,text='请输入sheet2要对比的列:').place(x=30,y=100)
    tk.Label(window,text='请输入sheet3要对比的列:').place(x=30,y=140)
    tk.Label(window,text='请输入sheet4要对比的列:').place(x=30,y=180)
    u=tk.Entry(window)
    u.place(x=190,y=60)
    e=tk.Entry(window)
    e.place(x=190,y=100)
    u1=tk.Entry(window)
    u1.place(x=190,y=140)
    e1=tk.Entry(window)
    e1.place(x=190,y=180)
    bt_login=tk.Button(window,text='开始',command=function1)
    bt_login.place(x=140,y=230)
    #主循环
    window.mainloop()
