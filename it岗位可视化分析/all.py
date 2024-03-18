from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from showcity import showcity
from showexp import showexp
from showsize import showsize
def showall():
    # 单独定义一个字典用来存储以岗位为键的平均薪资和最大薪资
    dic = {}
    result = []
    # 打开清洗后的数据
    with open('数据(清洗后).csv','r') as f:
        fcsv = csv.reader(f)
        for i in fcsv:
            result.append(i)
    test = []
    for row in result:
        try:
            dic[row[0]].append(float(row[3]))
        except:
            dic[row[0]] = [float(row[3])]
        # test.append(row[5])
    # 可视化总体概览函数
    def show_all():
        # 每次执行前先清空画布，避免图片在上一次的画布上重叠
        plt.clf()
        # 设置x轴，以及平均薪资图和最大薪资图的y轴
        x,y,ymax = [],[],[]
        # 将dic字典的岗位名装入x轴，对应岗位名列表的平均值和最大值分别装入y和ymax
        for i,j in dic.items():
            x.append(i)
            y.append(round(sum(j)/len(j),2))
            ymax.append(max(j))
        # 用来正常显示中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 设置画图为2行1列 开始画第一张
        plt.subplot(2, 1, 1)
        plt.title('平均薪资')
        # 传入xy 生成柱状图
        plt.bar(x, y)
        # 将x轴文字倾斜15度角，避免重叠
        plt.xticks(rotation=15)
        # 加上y轴标签
        plt.ylabel('岗位平均薪资（单位：万）')
        # 开始画第二张
        plt.subplot(2, 1, 2)
        plt.title('最高薪资')
        plt.bar(x, ymax)
        plt.xticks(rotation=15)
        plt.ylabel('岗位最高薪资（单位：万）')
        # 将画布内容打印到界面上
        canvas_spice.draw()
    def f1():
        root.withdraw()
        showcity()
        root.deiconify()
    def f2():
        root.withdraw()
        showsize()
        root.deiconify()
    def f3():
        root.withdraw()
        showexp()
        root.deiconify()
    root = Tk()

    root.title("数据可视化")
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
    show_all()
    button = Button(root,text='城市-薪资可视化',width=15,heigh=2,command=f1)
    button.place(x=50,y=180+50)
    button = Button(root,text='规模-薪资可视化',width=15,heigh=2,command=f2)
    button.place(x=50,y=240+50)
    button = Button(root,text='经验-薪资可视化',width=15,heigh=2,command=f3)
    button.place(x=50,y=300+50)
    root.mainloop()
if __name__ == '__main__':
    showall()