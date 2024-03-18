from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
import sys
import csv
def showcity():
    # 单独定义一个字典用来存储以岗位为键的平均薪资和最大薪资
    # 定义岗位对应的顺序，为后面数据装入city_dic做准备
    posi_dic = {'JAVA开发工程师':0,'PYTHON开发工程师':1,'C++开发工程师':2,'前端开发工程师':3,'软件测试工程师':4,'Android开发工程师':5,'算法工程师':6,'linux工程师':7,'数据工程师':8}
    # 定义城市字典，该字典键名为城市名称，对应的值为一个装有9个空列表的列表
    city_dic = {'北京':[[] for _ in range(9)],'上海':[[] for _ in range(9)],'广州':[[] for _ in range(9)],'深圳':[[] for _ in range(9)],'武汉':[[] for _ in range(9)],'杭州':[[] for _ in range(9)],'福州':[[] for _ in range(9)],'厦门':[[] for _ in range(9)]}
    # 打开清洗后的数据
    result = []
    # 打开清洗后的数据
    with open('数据(清洗后).csv', 'r') as f:
        fcsv = csv.reader(f)
        for i in fcsv:
            result.append(i)
    for row in result:
        city_dic[row[1]][posi_dic[row[0]]].append(float(row[3]))
        # 同时将其薪资以岗位分类装入dic字典
    def back():
        root.destroy()
        root.quit()
    # 不同岗位城市可视化函数
    def show(posi):
        # 每次执行前先清空画布，避免图片在上一次的画布上重叠
        plt.clf()
        # 根据函数输入的岗位，定位到数据存储在字典的第几列表中
        n = posi_dic[posi]
        # 设置x轴，以及平均薪资图和最大薪资图的y轴
        x,y,ymax = [],[],[]
        # 遍历字典的键值对
        for i,j in city_dic.items():
            # 不需要总体数据 跳过
            if i == '总体':
                continue
            # 将城市名装入x轴中，对应城市名列表中的对应岗位列表的平均值和最大值分别装入y和ymax
            x.append(i)
            y.append(round(sum(j[n])/len(j[n]),2))
            ymax.append(max(j[n]))
        aw1 = []
        aw2 = []
        for i,j,k in zip(x,y,ymax):
            aw1.append([i,j])
            aw2.append([i,k])
        aw1.sort(key=lambda x:x[1])
        aw2.sort(key=lambda x:x[1])
        x = [i[0] for i in aw1]
        y = [i[1] for i in aw1]
        xmax = [i[0] for i in aw2]
        ymax = [i[1] for i in aw2]
        # 同总体概览可视化
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.subplot(2, 1, 1)
        plt.title(posi + '平均薪资')
        plt.bar(x, y)
        plt.ylabel('岗位平均薪资（单位：万）')
        plt.subplot(2, 1, 2)
        plt.title(posi + '最高薪资')
        plt.bar(xmax, ymax)
        plt.ylabel('岗位最高薪资（单位：万）')
        canvas_spice.draw()
    # 创建tkinter的主窗口
    root = Tk()
    root.title("城市-薪资可视化")
    root.geometry('900x700')
    # 生成图像比例及画布
    fig = plt.figure(figsize=(10,9),dpi=75,facecolor='snow')
    # 设置图像的背景色与界面一致，避免色差
    fig.set_facecolor((0.9411,0.9411,0.9411,1))
    # 将画布与界面绑定
    canvas_spice = FigureCanvasTkAgg(fig,root)
    # 放置位置
    canvas_spice.get_tk_widget().place(x=150,y=0)
    # 设置总体及各个岗位的按钮，绑定按钮函数
    button = Button(root,text='返回',width=15,heigh=2,command=back)
    button.place(x=50,y=0+50)
    button = Button(root,text='JAVA开发工程师',width=15,heigh=2,command=lambda :show('JAVA开发工程师'))
    button.place(x=50,y=60+50)
    button = Button(root,text='C++开发工程师',width=15,heigh=2,command=lambda :show('C++开发工程师'))
    button.place(x=50,y=120+50)
    button = Button(root,text='PYTHON开发工程师',width=15,heigh=2,command=lambda :show('PYTHON开发工程师'))
    button.place(x=50,y=180+50)
    button = Button(root,text='Android开发工程师',width=15,heigh=2,command=lambda :show('Android开发工程师'))
    button.place(x=50,y=240+50)
    button = Button(root,text='前端开发工程师',width=15,heigh=2,command=lambda :show('前端工程师'))
    button.place(x=50,y=300+50)
    button = Button(root,text='软件测试工程师',width=15,heigh=2,command=lambda :show('软件测试工程师'))
    button.place(x=50,y=360+50)
    button = Button(root,text='linux工程师',width=15,heigh=2,command=lambda :show('Linux工程师'))
    button.place(x=50,y=420+50)
    button = Button(root,text='算法工程师',width=15,heigh=2,command=lambda :show('算法工程师'))
    button.place(x=50,y=480+50)
    button = Button(root,text='数据工程师',width=15,heigh=2,command=lambda :show('数据工程师'))
    button.place(x=50,y=540+50)
    # 主循环
    root.mainloop()