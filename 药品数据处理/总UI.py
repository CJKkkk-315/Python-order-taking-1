import os
import tkinter.messagebox
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from 数据库系统 import function3
from csv版本1 import function11
from 药品数据处理2 import function22
def f3():
    root.destroy()
    function3()
def f1():
    root.destroy()
    function11()
def f2():
    root.destroy()
    function22()
def f12():
    Button(root, width=22, height=3, text='信息比对输出', command=f1).place(x=160, y=50)
    Button(root, width=22, height=3, text='信息调整输出', command=f2).place(x=160, y=150)
    root.mainloop()
root = Tk()
root.title('药品信息筛查比对调整系统')
root.geometry('500x300')
Button(root, width=22, height=3, text='药品信息比对调整模块', command=f12).place(x=160, y=50)
Button(root, width=22, height=3, text='药品信息查询输出模块', command=f3).place(x=160, y=150)
root.mainloop()