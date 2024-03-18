import tkinter.messagebox
import tkinter as tk
import csv
data = []
with open('豆瓣.csv',encoding='gbk')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
data = data[1:]
def search():
    res = []
    key = u.get()
    for i in data:
        if key in i[1]:
            res.append(i[1])
    for i in res:
        lb.insert('end',i)
window = tk.Tk()
window.title('图书查询系统')
window.geometry('760x600')
tk.Label(window, text='请输入关键词').place(x=30, y=20)
u = tk.Entry(window)
u.place(x=110, y=20)
bt_login1 = tk.Button(window, text='开始搜索',command = search)
bt_login1.place(x=300, y=15)
lb = tk.Listbox(window,width=100,height=28)
lb.place(x=30, y=50)
def myPrint(self):
    name = lb.get(lb.curselection())
    for i in data:
        if i[1] == name:
            people = i[2]
            company = i[3]
            url = i[4]
    s = '书名：'+ name + '\n作者：' + people + '\n出版社：' + company + '\n豆瓣链接：' + url
    tk.messagebox.askokcancel(title='图书具体信息', message=s)
lb.bind("<Double-Button-1>",myPrint)
window.mainloop()