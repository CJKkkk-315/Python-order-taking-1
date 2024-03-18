import pandas as pd
import sys
import matplotlib.pyplot as plt


def read_file(filename):   #从excel文件中将数据读出，并以列表的形式返回
    data = pd.read_excel(filename)
    ls = data.values.tolist()    #将dataframe类型的数据转换成列表类型
    return ls


def sort_lst(ls):   #对二维列表ls按最后一列排序
    ls.sort(key=lambda x:x[-1])   #升序
    return ls

def query(data, name, all=False):
    if all:
        print('电影票房如下：')
        for line in data:
            print('{}：{}'.format(line[0], line[1]))
        return
    for line in data:
        if name in line[0]:
            print('电影名：{}, 票房：{}'.format(line[0], line[1]))
            return
    print('未找到电影票房：{}'.format(name))

def modify(data, name):
    for line in data:
        if line[0] == name:
            value = input('请输入修改后的票房：')
            line[1] = float(value)
            print('{}电影票房修改成功！'.format(line[0]))
            return
    print('未找到电影：{}'.format(name))

def show_pie(data):
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    labels = [line[0] for line in data]
    values = [line[1] for line in data]
    value_sum = sum(values)
    sizes = [round(v / value_sum, 2) for v in values]
    # explode = (0,0,0,0.1,0,0)
    plt.pie(sizes,explode=None,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
    plt.title("电影票房饼图")
    plt.show()

    
def menu():  #菜单函数
    print('======2021年部分电影票房分析系统======')
    print('1、电影票房查询')
    print('2、电影票房修改')
    print('3、电影票房修改饼图')
    print('4、查看所有电影票房')
    print('0、退出')
    print('==========================')


if __name__ == '__main__':
    lst = read_file(r'2021年部分电影票房.xls')
    while True:
        menu()
        choice = input('请选择菜单：')
        if choice == '0':
            sys.exit(0)
        elif choice == '1':
            name = input('请输入电影名称：')
            query(lst, name)
        elif choice == '2':
            name = input('请输入电影名称：')
            modify(lst, name)
        elif choice == '3':
            show_pie(lst)
        elif choice == '4':
            query(lst, '', True)
        else:
            print('输入错误，请重新输入！')
        
