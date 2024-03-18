import xgboost as xgb
from pandas import DataFrame
xlf_new = xgb.Booster()  # init model
xlf_new.load_model("1.model")  # load data
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
d1 = {'男':1,'女':2}
d2 = {'是':1,'否':2}
d3 = {'是':1,'否':2}
d5 = {'颈内动脉':1,'椎动脉':2,'颈内动脉+椎动脉':3}
d6 = {'DSA':1,'夹闭术':2,'未手术':3}
d8 = {'是':1,'否':2}
d13 = {'是':1,'否':2}
aa = {'性别':[1],'吸烟史':[1],'饮酒史':[1],'Hunt-Hess评分':[1],'责任动脉部位':[1],'治疗方式':[1],'成熟中性粒细胞绝对值':[1],'罂粟碱':[1],'年龄':[1],'嗜酸性粒细胞绝对值':[1],'幼稚中性粒细胞绝对值':[1],'高敏肌钙蛋白T':[1],'赖氨酸':[1]}
def function():
    aa['性别'][0] = d1[u1.get()]
    aa['吸烟史'][0] = d2[u2.get()]
    aa['饮酒史'][0] = d3[u3.get()]
    aa['Hunt-Hess评分'][0] = float(u4.get())
    aa['责任动脉部位'][0] = d5[u5.get()]
    aa['治疗方式'][0] = d6[u6.get()]
    aa['成熟中性粒细胞绝对值'][0] = float(u7.get())
    aa['罂粟碱'][0] = d8[u8.get()]
    aa['年龄'][0] = float(u9.get())
    aa['嗜酸性粒细胞绝对值'][0] = float(u10.get())
    aa['幼稚中性粒细胞绝对值'][0] = float(u11.get())
    aa['高敏肌钙蛋白T'][0] = float(u12.get())
    aa['赖氨酸'][0] = d13[u13.get()]
    bb = DataFrame(aa)
    data_test = xgb.DMatrix(bb)
    print(bb)
    pred_new = xlf_new.predict(data_test)
    print(pred_new)
    if pred_new[0] < 0.5:
        tk.messagebox.askokcancel(title='结果', message='预测结果为低危')
    elif pred_new[0] >= 0.5:
        tk.messagebox.askokcancel(title='结果', message='预测结果为高危')
window=tk.Tk()
window.title('欢迎进入预测系统')
window.geometry('500x630')
tk.Label(window,text='性别:').place(x=30,y=50)
tk.Label(window,text='吸烟史:').place(x=30,y=130)
tk.Label(window,text='饮酒史:').place(x=30,y=170)
tk.Label(window,text='Hunt-Hess评分:').place(x=30,y=210)
tk.Label(window,text='责任动脉部位:').place(x=30,y=250)
tk.Label(window,text='手术方式:').place(x=30,y=530)
tk.Label(window,text='成熟中性粒细胞绝对值（10^9/L）:').place(x=30,y=290)
tk.Label(window,text='罂粟碱:').place(x=30,y=450)
tk.Label(window,text='年龄:').place(x=30,y=90)
tk.Label(window,text='嗜酸性粒细胞绝对值（10^9/L）:').place(x=30,y=370)
tk.Label(window,text='幼稚中性粒细胞绝对值（10^9/L）:').place(x=30,y=330)
tk.Label(window,text='高敏肌钙蛋白T（pg/mL）:').place(x=30,y=410)
tk.Label(window,text='赖氨酸:').place(x=30,y=490)
u1=ttk.Combobox(window)
u1['value'] = ('男','女')
u1.place(x=250,y=50)
u2=ttk.Combobox(window)
u2['value'] = ('是','否')
u2.place(x=250,y=130)
u3=ttk.Combobox(window)
u3['value'] = ('是','否')
u3.place(x=250,y=170)
u4=tk.Entry(window)
u4.place(x=250,y=210)
u5=ttk.Combobox(window)
u5['value'] = ('颈内动脉','椎动脉','颈内动脉+椎动脉')
u5.place(x=250,y=250)
u6=ttk.Combobox(window)
u6['value'] = ('DSA','夹闭术','未手术')
u6.place(x=250,y=530)
u7=tk.Entry(window)
u7.place(x=250,y=290)
u8=ttk.Combobox(window)
u8['value'] = ('是','否')
u8.place(x=250,y=450)
u9=tk.Entry(window)
u9.place(x=250,y=90)
u10=tk.Entry(window)
u10.place(x=250,y=370)
u11=tk.Entry(window)
u11.place(x=250,y=330)
u12=tk.Entry(window)
u12.place(x=250,y=410)
u13=ttk.Combobox(window)
u13['value'] = ('是','否')
u13.place(x=250,y=490)
bt_login=tk.Button(window,text='开始预测',command = function)
bt_login.place(x=140,y=580)
#主循环
window.mainloop()