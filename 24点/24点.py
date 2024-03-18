from random import randint
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import re

# 生成4个随机数
num = [str(randint(1,10)) for i in range(4)]
# num = ['1','10','6','7']
def comsum():
    # 获取用户输入的计算式
    s = u.get()
    # 提取用户输入的所有数字
    n = re.findall(r"\d+\.?\d*", s)
    # 判断用户输入的数字是否和4张牌一样，否则输出错误
    if sorted(n) == sorted(num):
        # 如果一样 是否结果为24，否则输出错误
        if eval(s) == 24:
            tk.messagebox.askokcancel(title='结果', message='答对了！')
        else:
            tk.messagebox.askokcancel(title='结果', message='答错了！')
    else:
        tk.messagebox.askokcancel(title='结果', message='答错了！')
def reset():
    global num
    num = [str(randint(1, 10)) for i in range(4)]
    Button(root, width=6, height=4, text=str(num[0]), font=('Arial', 25)).place(x=30, y=30)
    Button(root, width=6, height=4, text=str(num[1]), font=('Arial', 25)).place(x=230, y=30)
    Button(root, width=6, height=4, text=str(num[2]), font=('Arial', 25)).place(x=430, y=30)
    Button(root, width=6, height=4, text=str(num[3]), font=('Arial', 25)).place(x=630, y=30)
root = Tk()
root.title('24点小游戏')
root.geometry('800x420')
path = StringVar()
Button(root, width=6, height=4, text=str(num[0]),font = ('Arial' , 25)).place(x=30, y=30)
Button(root, width=6, height=4, text=str(num[1]),font = ('Arial' , 25)).place(x=230, y=30)
Button(root, width=6, height=4, text=str(num[2]),font = ('Arial' , 25)).place(x=430, y=30)
Button(root, width=6, height=4, text=str(num[3]),font = ('Arial' , 25)).place(x=630, y=30)
tk.Label(root,text='请输入答案:').place(x=280,y=300)
u=tk.Entry(root)
u.place(x=370,y=300)
Button(root, width=13, height=2, text='验证结果',command=comsum).place(x=430, y=360)
Button(root, width=13, height=2, text='重新发牌',command=reset).place(x=180, y=360)
root.mainloop()