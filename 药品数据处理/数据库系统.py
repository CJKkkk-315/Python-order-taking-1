def function3():
    import tkinter.messagebox
    import tkinter as tk
    import csv
    import xlrd
    import os
    ext = '.csv'
    ext2 = '.csv'
    files = os.listdir(os.getcwd() + '\\数据文件')
    print(os.getcwd() + '\\数据文件')
    data = []
    res = []
    ex = []
    for file in files:
        with open(os.getcwd() + '\\数据文件\\' + file, 'r',errors='ignore')as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                # print(1)
                data.append(row[:255])
        # dataw = xlrd.open_workbook(os.getcwd() + '\\数据文件\\' + file)
        # table = dataw.sheets()[0]
        # for i in range(1,table.nrows):
        #     r = []
        #     for j in range(table.ncols):
        #         a = table.cell_value(i, j)
        #         r.append(str(a))
        #     data .append(r)

    def search():
        global res
        res = []
        key = u.get()
        for i in data:
            for j in i:
                if key in j:
                    res.append(i)
                    break
        lb.delete(0, 'end')
        for i in res:
            lb.insert('end', ' '.join(i))

    def export():
        global res
        global ex
        f = open('查询结果.csv', 'a+', newline='')
        f_csv = csv.writer(f)
        for i in ex:
            f_csv.writerow(i)
        f.close()

    def show(event):
        global ex
        global res
        ex = []
        object = event.widget
        indexs = object.curselection()
        # print(indexs)
        for index in indexs:
            ex.append(res[index])
        # print(ex)
    window = tk.Tk()
    window.title('药品查询系统')
    window.geometry('760x600')
    sc = tkinter.Scrollbar(window)
    sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    tk.Label(window, text='请输入关键词').place(x=30, y=20)
    u = tk.Entry(window)
    u.place(x=110, y=20)
    bt_login1 = tk.Button(window, text='开始搜索',command = search)
    bt_login1.place(x=300, y=15)
    bt_login1 = tk.Button(window, text='导出结果',command = export)
    bt_login1.place(x=400, y=15)
    lb = tk.Listbox(window,width=100,height=28,yscrollcommand=sc.set,selectmode=tkinter.MULTIPLE)
    lb.bind("<<ListboxSelect>>", show)
    lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    lb.place(x=30, y=50)
    sc.config(command=lb.yview)
    ma = 0
    for i in data:
        # print(2)
        ma += 1
        if ma == 2000:
            break
        lb.insert('end', ' '.join(i))
    window.mainloop()
# function3()