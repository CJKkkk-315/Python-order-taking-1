from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

def choosepic1():
    path_=askopenfilename()
    path.set(path_)
    img_open = Image.open(e1.get())
    img=ImageTk.PhotoImage(img_open)
    l1.config(image=img)
    l1.image=img #keep a reference
def choosepic2():
    img_open = Image.open('2.png')
    img=ImageTk.PhotoImage(img_open)
    l1.config(image=img)
    l1.image=img #keep a reference
def choosepic3():
    img_open = Image.open('3.png')
    img=ImageTk.PhotoImage(img_open)
    print(type(img))
    l1.config(image=img)
    l1.image=img #keep a reference
def choosepic4():
    result = tk.messagebox.askokcancel(title = '精度评价',message='精度指数：xx.xxxxxxxx%')
def choosepic5():
    result = tk.messagebox.askokcancel(title = '保存图片',message='保存成功')
root = Tk()
root.geometry('800x520')
path = StringVar()
Button(root, width = 13, height = 2,text='打开图像', command=choosepic1).place(x=30,y=30)
Button(root, width = 13, height = 2,text='训练样本', command=choosepic2).place(x=30,y=130)
Button(root, width = 13, height = 2,text='图像分类', command=choosepic3).place(x=30,y=230)
Button(root, width = 13, height = 2,text='精度评价', command=choosepic4).place(x=30,y=330)
Button(root, width = 13, height = 2,text='保存图片', command=choosepic5).place(x=30,y=430)
e1 = Entry(root, state='readonly', text=path)
# e1.pack()
l1 = Label(root)
l1.place(x=150,y=20)
root.mainloop()