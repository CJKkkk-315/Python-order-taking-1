# managerSystem.py
from student import *

pass
class StudentManager(object):
    def __init__(self):
        self.stu_list = []

    def run(self):
        self.load_stu()

        while True:
            self.show_menu()
            k = int(input('请输入功能序号：\n'))
            if k == 1:
                self.add_stu()
            elif k == 2:
                self.del_stu()
            elif k == 3:
                self.modify_stu()
                pass
            elif k == 4:
                self.find_stu()
            elif k == 5:
                self.show_stu()
            elif k == 6:
                self.show_stu_age_rise()
                pass
            elif k == 7:
                self.show_stu_age_reduce()
            elif k == 8:
                self.save()
            elif k == 9:
                # 补充代码，实现结束循环
                break
                pass
            else:
                print('输入错误，请输入1~9之间的数字！')

    @staticmethod
    def show_menu():
        menu_info = \
            '''
            ＋－－－－－－－－－－－－－－－－－－－－－－＋
                      欢迎进入学生管理系统
            ｜ 1.添加学员 
            ｜ 2.删除学员 
            ｜ 3.修改学员信息 
            ｜ 4.查询学员信息 
            ｜ 5.显示全部学员信息 
            ｜ 6.按年龄从小到大显示全部学员信息 
            ｜ 7.按年龄从大到小显示全部学员信息 
            ｜ 8.保存学员信息 
            ｜ 9.退出系统 
            ＋－－－－－－－－－－－－－－－－－－－－－－＋
            '''
        print(menu_info)


    def add_stu(self):
        while True:
            try:
                name = input("请输入姓名：")
                if name == '':
                    raise BaseException('姓名不能为空！')
                gender = input('请输入您的性别：')
                if gender != '男' and gender !='女':
                    print('性别只能是男或女')
                    continue
                # 补充代码，实现判断如果输入的gender不是男也不是女，则抛出异常，异常提示信息为“性别只能是男或女”
                pass
                age = int(input("请输入年龄："))
            except ValueError:
                print("输入无效，不是整形数值．．．．重新录入信息")
                continue
            except BaseException as e:
                print(e)
                continue
            # 根据输入的姓名、性别和年龄创建学生对象stu
            stu = Student(name=name,gender=gender,age=age)
            pass
            self.stu_list.append(stu)
            print(stu)
            break


    def del_stu(self):
        del_name = input('请输入要删除学员姓名：')
        # 补充代码，实现功能：判断要删除的学员姓名是否存在，如果存在则删除，如果不存在则输出“查无此人”
        for i in self.stu_list:
            if i.name == del_name:
                self.stu_list.remove(i)
                return
        print('查无此人')
        pass
        

    def new_input(self, old, new):
        input_str = input(new)
        if len(input_str) > 0:
            return input_str
        else:
            return old

    def modify_stu(self):
        modify_name = input('请输入要修改的学员姓名：')
        for i in self.stu_list:
            if i.name == modify_name:
                i.name = self.new_input(i.name,'请输入新修改的名字[回车则不修改]:')
                i.gender = self.new_input(i.gender, '请输入新修改的性别[回车则不修改]:')
                i.age = self.new_input(i.age, '请输入新修改的年龄[回车则不修改]:')
                break
        print('该学员不存在！')
        # 补充代码，实现功能：判断要修改的学员姓名是否存在，
        # 如果存在，则提示用户“请输入新修改的名字[回车则不修改]:”、'请输入新修改的性别[回车则不修改]:'、 '请输入新修改的年龄[回车则不修改]:'
        # 并调用new_input方法修改学员信息
        # 如果不存在，则提示“该学员不存在！”
        pass

    def find_stu(self):
        find_name = input('请输入要查询的学员姓名：')
        flag = False
        for i in self.stu_list:
            if i.name == find_name:
                flag = True
                print(f'姓名：{i.name},性别：{i.gender},年龄：{i.age}\n')
                break
        print('该学员不存在！')
        pass


    def show_stu(self):
        for i in self.stu_list:
            print(f'姓名：{i.name},性别：{i.gender},年龄：{i.age}')


    def show_stu_age_rise(self):
        new_list = sorted(self.stu_list, key=lambda student: student.age)
        for i in new_list:
            print(f'姓名：{i.name},性别：{i.gender},年龄：{i.age}')


    def show_stu_age_reduce(self):
        new_list = sorted(self.stu_list, key=lambda student: student.age, reverse=True)
        for i in new_list:
            print(f'姓名：{i.name},性别：{i.gender},年龄：{i.age}')

    def save(self):
        f = open('student.data', 'w', encoding='utf_8')
        new_list = [i.__dict__ for i in self.stu_list]
        f.write(str(new_list))
        pass
        f.close()


    def load_stu(self):
        global f
        # 补充代码，实现以"r"模式打开学员数据文件，如果文件不存在（即发生异常）则以"w"模式打开文件
        try:
            f = open('student.data','r',encoding='utf_8')
        except:
            f = open('student.data','w',encoding='utf_8')
        else:
            data = f.read()
            new_list = eval(data)
            self.stu_list = [Student(i['name'], i['gender'], i['age']) for i in new_list]
        finally:
            f.close()


