from collections import Counter
import tkinter as tk
from random import randint
encode = {0:'错',1:'对'}
data = []
key = 100
def search():
    global key
    key = u.get()
    lb.delete(0, 'end')
    for i in data[:int(key)]:
        lb.insert('end',i)
    b = list(Counter([i[-1] for i in data]).items())
    lb.insert('end', b)
def f3():
    global data
    lb.delete(0, 'end')
    print(key)
    for i in range(len(data)):
        if data[i]:
            if data[i][-1] == '对':
                data[i] = ''
    data = [i for i in data if i != '']
    for i in range(len(data)):
        if data[i]:
            data[i] = data[i] + encode[randint(0,1)]
    print(data)
    for i in data[:int(key)]:
        if i:
            lb.insert('end',i)
    b = list(Counter([i[-1] for i in data]).items())
    lb.insert('end', b)
def f2():
    global data
    lb.delete(0, 'end')
    print(key)
    for i in range(len(data)):
        if data[i]:
            if data[i][-1] == '错':
                data[i] = ''
    data = [i for i in data if i != '']
    for i in range(len(data)):
        if data[i]:
            data[i] = data[i] + encode[randint(0,1)]
    print(data)
    for i in data[:int(key)]:
        if i:
            lb.insert('end',i)
    b = list(Counter([i[-1] for i in data]).items())
    lb.insert('end', b)
def f1():
    lb.delete(0, 'end')
    global data
    data = []
    for i in range(100):
        data.append(encode[randint(0,1)])
    for i in data:
        lb.insert('end',i)
    b = list(Counter([i[-1] for i in data]).items())
    lb.insert('end', b)
window = tk.Tk()
window.title('')
window.geometry('760x600')
tk.Label(window, text='显示数量').place(x=30, y=20)
u = tk.Entry(window)
u.place(x=110, y=20)
bt_login1 = tk.Button(window, text='修改显示数量',command = search)
bt_login1.place(x=300, y=15)
bt_login2 = tk.Button(window, text='删除所有0',command = f2)
bt_login2.place(x=400, y=15)
bt_login3 = tk.Button(window, text='删除所有1',command = f3)
bt_login3.place(x=500, y=15)
bt_login3 = tk.Button(window, text='随机',command = f1)
bt_login3.place(x=600, y=15)
lb = tk.Listbox(window,width=100,height=28)
lb.place(x=30, y=50)
window.mainloop()