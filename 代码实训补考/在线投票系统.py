menu_info = \
            '''
            ＋－－－－－－－－－－－－－－－－－－－－－－＋
                      欢迎进入学生管理系统
            ｜ 1.添加投票候选人 
            ｜ 2.删除投票候选人 
            ｜ 3.为候选人投票 
            ｜ 4.删除投票 
            ｜ 5.展示所有候选人及投票情况
            ｜ 6.退出投票系统 
            ＋－－－－－－－－－－－－－－－－－－－－－－＋
            '''
people_list = [['张三',11],['李四',5],['王五',7]]
def add():
    global people_list
    name = input('请输入要添加的候选人姓名：')
    if name in [i[0] for i in people_list]:
        print('该候选人已存在！')
        return
    people_list.append([name,0])
def delete():
    global people_list
    name = input('请输入要删除的候选人姓名：')
    for i in people_list:
        if i[0] == name:
            people_list.remove(i)
            return
    print('没有该候选人！')
def vote():
    global people_list
    name = input('请输入要投票的候选人姓名：')
    for i in people_list:
        if i[0] == name:
            i[1] += 1
            return
    print('没有该候选人！')
def devote():
    global people_list
    name = input('请输入要删除投票的候选人姓名：')
    for i in people_list:
        if i[0] == name:
            if not i[1]:
                print('该候选人未被投票！')
                return
            i[1] -= 1
            return
    print('没有该候选人！')
def show():
    global people_list
    for i in people_list:
        print('姓名：' + i[0] + ' 票数：' + str(i[1]) + '\n')
while True:
    print(menu_info)
    k = int(input('请输入功能序号：\n'))
    if k == 1:
        add()
    elif k == 2:
        delete()
    elif k == 3:
        vote()
    elif k == 4:
        devote()
    elif k == 5:
        show()
    elif k == 6:
        break
    else:
        print('输入错误，请输入1~6之间的数字！')