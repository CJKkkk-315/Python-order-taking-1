#-----------------------------
#
#ID:your ID
#Name:your name
#
#-----------------------------


import course
import student




# 展示所有课程函数
def show(courses_list):
    # 打印标题
    print('''
========================================
All Courses Information
========================================
''')
    # 循环遍历课程列表，依次打印每个课程的各个属性
    for i in courses_list:
        print('----------------------------------------')
        print('Course Name:' + i.get_course_name())
        print('Course ID|Credits:' + i.get_course_id() + '|' + i.get_credit())
        print('Instructor Name:' + i.get_instructor_name())
        print('Address:' + i.get_address())
        print('Description:' + i.get_description())
# 按照ID搜索课程函数
def search(coursers_list):
    # 通过input函数输入id
    id = input('Please enter course ID:')
    # 遍历课程列表 查看id是否在列表中
    for i in coursers_list:
        # 如果在 则打印该课程各个属性
        if i.get_course_id() == id:
            print('Course Name:' + i.get_course_name())
            print('Course ID|Credits:' + i.get_course_id() + '|' + i.get_credit())
            print('Instructor Name:' + i.get_instructor_name())
            print('Address:' + i.get_address())
            print('Description:' + i.get_description())
            return
    # 如果遍历完成还没有找到 则输出不在列表中
    print('Course(ID=' + id + ') is not found in the course list.')
# 添加课程函数
def add(coursers_list):
    # input函数获取用户输入的课程id
    id = input('Please enter course ID:')
    # 遍历课程列表，查看id是否已经存在
    for i in coursers_list:
        # 若存在 则输出已经在列表中
        if i.get_course_id() == id:
            print('Course(ID={}) already exists in the courses list.'.format(id))
            return
    # 若不存在，则让用户依次输入课程信息
    name = input('Please enter course name:')
    credits = input('Please enter course credits:')
    instructor = input('Please enter course instructor:')
    address = input('Please enter course address:')
    description = input('Please enter course description:')
    # 在课程列表末尾添加初始化好的新的课程对象
    coursers_list.append(course.Course(name,id,credits,instructor,address,description))
    # 输出课程添加成功
    print('Successfully added the Course(ID={}) to the courses list.'.format(id))
# 课程信息更新函数
def update(coursers_list):
    # input函数获取用户输入的课程id
    id = input('Please enter course ID:')
    # 遍历查看id是否在课程列表中
    for i in coursers_list:
        # 若在课程列表中，则先打印出未更新的课程信息
        if i.get_course_id() == id:
            print('Before updating,the course information:')
            print('----------------------------------------')
            print('Course Name:' + i.get_course_name())
            print('Course ID|Credits:' + i.get_course_id() + '|' + i.get_credit())
            print('Instructor Name:' + i.get_instructor_name())
            print('Address:' + i.get_address())
            print('Description:' + i.get_description())
            print('----------------------------------------')
            # 让用户输入希望更新的相关信息
            name = input('Please enter course name:')
            credits = input('Please enter course credits:')
            instructor = input('Please enter course instructor:')
            address = input('Please enter course address:')
            description = input('Please enter course description:')
            # 使用set函数更新该课程对象的各个信息
            i.set_course_name(name)
            i.set_credit(credits)
            i.set_instructor_name(instructor)
            i.set_address(address)
            i.set_description(description)
            # 输出更新成功
            print('Successfully updated the Course(ID={}) to the courses list.'.format(id))
            return
    # 若在课程列表中未发现该id，则返回没有找到该课程
    print('Course(ID={}) is not found in the courses list.'.format(id))
# 展示所有学生信息函数
def display(coursers_list,students_list):
    # 打印标题
    print('''
    ========================================
    All Students Information
    ========================================
    ''')
    # 遍历学生列表，展示每个学生的各个信息
    for i in students_list:
        print('----------------------------------------')
        print('Student Name:' + i.get_name())
        print('Course ID(Gender):' + i.get_id() + '(' + i.get_gender() + ')')
        print('Major:' + i.get_major())
        print('Selected Course({}):'.format(i.get_number_courses()))
        # 在课程中，以id为桥梁，拼接课程列表中对应id的课程名输出
        for j in i.get_courses():
            print('     ' + j + ':' + [k.get_course_name() for k in coursers_list if k.get_course_id() == j][0])
def retrieve(coursers_list,students_list):
    # input函数获取用户输入的学生id
    id = input('Please enter student ID:')
    # 遍历学生列表 查看id是否在列表中
    for i in students_list:
        # 如果在 则打印该学生各个属性
        if i.get_id() == id:
            print('----------------------------------------')
            print('Student Name:' + i.get_name())
            print('Course ID(Gender):' + i.get_id() + '(' + i.get_gender() + ')')
            print('Major:' + i.get_major())
            print('Selected Course({}):'.format(i.get_number_courses()))
            for j in i.get_courses():
                print('     ' + j + ':' + [k.get_course_name() for k in coursers_list if k.get_course_id() == j][0])
            return
    # 如果遍历完成还没有找到 则输出不在列表中
    print('Student(ID=' + id + ') is not found in the students list.')
def insert(students_list):
    # 通过input函数输入id
    id = input('Please enter student ID:')
    # 遍历学生列表，查看id是否已经存在
    for i in students_list:
        if i.get_id() == id:
            # 若存在 则输出已经在列表中
            print('Student(ID={}) already exists in the students list.'.format(id))
            return
    # 若不存在，则让用户依次输入学生信息
    name = input('Please enter student name:')
    gender = input('Please enter student gender:')
    major = input('Please enter student major:')
    # 在学生列表的末尾插入新定义的学生类变量
    students_list.append(student.Student(name,id,gender,major))
    # 输出插入成功
    print('Successfully added the Student(ID={}) to the students list.'.format(id))
def modify(coursers_list,students_list):
    # input函数获取用户输入的课程id
    id = input('Please enter student ID:')
    # 遍历查看id是否在学生列表中
    for i in students_list:
        # 若在学生列表中，则让用户进一步输入要选择的选项
        if i.get_id() == id:
            c = input('Student(ID=' + id + ') [major|enroll|drop]:')
            # 若用户输入修改专业
            if c == 'major':
                # 则让用户输入新的专业名称
                major = input('Please enter student major:')
                # 通过set函数修改学生类对象的专业
                i.set_major(major)
                # 打印学生的完整信息
                print('Modified the major of Student(ID={}).'.format(id))
                print('----------------------------------------')
                print('Student Name:' + i.get_name())
                print('Course ID(Gender):' + i.get_id() + '(' + i.get_gender() + ')')
                print('Major:' + i.get_major())
                print('Selected Course({}):'.format(i.get_number_courses()))
                for j in i.get_courses():
                    print('     ' + j + ':' +
                          [k.get_course_name() for k in coursers_list if k.get_course_id() == j][0])
                return
            # 若用户输入加入新课程
            elif c == 'enroll':
                # 则让用户输入新的课程id
                cid = input('Please enter course ID:')
                # 遍历课程列表，查看课程id是否在列表中
                for j in coursers_list:
                    # 若存在 则进一步判断课程id是否已经在该学生的课程中
                    if j.get_course_id() == cid:
                        # 若存在 则输出该课程已经被选上
                        if cid in i.get_courses():
                            print('Course(ID={}) is already in the enrolled courses list.'.format(cid))
                            return
                        # 若不存在 通过set函数将新的课程id添加到学生课程列表的末尾，同时让学生的已选择课程数+1
                        else:
                            i.set_number_courses(int(i.get_number_courses()) + 1)
                            i.set_courses_list(i.get_courses()+ [cid])
                        # 输出更新后的学生信息
                        print('Modified the major of Student(ID={}).'.format(id))
                        print('----------------------------------------')
                        print('Student Name:' + i.get_name())
                        print('Course ID(Gender):' + i.get_id() + '(' + i.get_gender() + ')')
                        print('Major:' + i.get_major())
                        print('Selected Course({}):'.format(i.get_number_courses()))
                        for j in i.get_courses():
                            print('     ' + j + ':' +
                                  [k.get_course_name() for k in coursers_list if k.get_course_id() == j][0])
                        return
                # 若id不存在课程列表中 则输出未找到该课程
                print('Course(ID=' + cid + ') is not found in the course list.')
                return
            # 若用户选择删除课程
            elif c =='drop':
                # 则让用户输入要删除的课程id
                cid = input('Please enter course ID:')
                # 判断该课程是否在课程列表中
                for j in coursers_list:
                    # 若存在课程列表中
                    if j.get_course_id() == cid:
                        # 判断该课程是否存在学生课程列表中
                        if cid in i.get_courses():
                            # 若也存在 则通过set函数 设置新的学生课程列表为去掉该课程后的新列表
                            aw = i.get_courses()
                            aw.remove(cid)
                            i.set_courses_list(aw)
                            # 同时使得学生课程数减一
                            i.set_number_courses(int(i.get_number_courses()) - 1)
                            # 输出修改后的学生信息
                            print('Modified the major of Student(ID={}).'.format(id))
                            print('----------------------------------------')
                            print('Student Name:' + i.get_name())
                            print('Course ID(Gender):' + i.get_id() + '(' + i.get_gender() + ')')
                            print('Major:' + i.get_major())
                            print('Selected Course({}):'.format(i.get_number_courses()))
                            for j in i.get_courses():
                                print('     ' + j + ':' +
                                      [k.get_course_name() for k in coursers_list if k.get_course_id() == j][0])
                            return
                        # 若不存在学生列表中 输出对应错误信息
                        else:
                            print('Course(ID={}) is not in the enrolled courses list.'.format(cid))
                            return
                # 若不存在课程列表中 输出对应错误信息
                print('Course(ID=' + cid + ') is not found in the course list.')
                return
            # 若指令不在上面三种指令范围内 输出非法指令
            else :
                print('Not a valid command-returning to main menu.')
                return
    # 若学生id不在学生列表中 输出没有找到该学生
    print('Student(ID=' + id + ') is not found in the students list.')
def remove(coursers_list,students_list):
    # input函数获取用户输入的要删除的课程id
    id = input('Please enter course ID:')
    # 若该课程id在课程列表中
    for i in coursers_list:
        if i.get_course_id() == id:
            # 则再课程列表中删除该课程
            coursers_list.remove(i)
            cid = id
            # 同时遍历学生选择的课程列表 若有选择这一课程 同时删除这一课程
            for j in students_list:
                if cid in j.get_courses():
                    aw = j.get_courses()
                    aw.remove(cid)
                    j.set_courses_list(aw)
                    j.set_number_courses(int(j.get_number_courses()) - 1)
            print('Successfully removed the Course(ID={}) from the courses list'.format(id))
            return
    # 若不存在该课程id 输出对应错误信息
    print('Course(ID=' + id + ') is not found in the course list.')
def delete(students_list):
    # input函数获取用户输入的要删除的学生id
    id = input('Please enter student ID:')
    # 遍历学生列表
    for i in students_list:
        # 若该id存在学生列表中 则删除
        if i.get_id() == id:
            students_list.remove(i)
            # 并输出成功删除信息
            print('Successfully delete the Student(ID={}) from the students list'.format(id))
            return
    # 若不存在 则输出未找到该学生id
    print('Student(ID=' + id + ') is not found in the students list.')
#-----------------------------
# define the function main
#-----------------------------        
def main():
    courses_list=[]
    students_list=[]
    # 打开课程txt文件
    with open('courses.txt','r') as f:
        # 先将txt中的内容全部读入data列表中 一行为一个数据
        data = f.readlines()
    # 课程文件中每两行为一个课程数据，所以循环时步长设置为2
    for i in range(0,len(data),2):
        # 第一行将数据以，分隔开来 获得5个基础的课程信息 保存在l1中
        l1 = data[i].split(',')
        # 第二行单独为description信息，将换行符\n去掉以后即为对应信息
        l2 = data[i+1].replace('\n','')
        # 将上述数据初始化为course对象，添加到课程列表中
        courses_list.append(course.Course(l1[0],l1[1],l1[2],l1[3],l1[4].replace('\n',''),l2))
    # 打开学生txt文件
    with open('students.txt','r') as f:
        # 将txt内容全部读入data列表中 同样一行一个数据
        data = f.readlines()
    # 由于学生文件每位学生所占行数不确定 所以需要一个变量line做记录
    line = 0
    # 通过循环判别line是否超出了数据行数
    while line < len(data):
        # 第一行为学生基础信息 同样以，分隔保存在l1列表中
        l1 = data[line].split(',')
        # 第一行的信息就足够我我们初始化student对象 添加到学生列表中
        s = student.Student(l1[0],l1[1],l1[2],l1[3].replace('\n',''))
        # 转入下一行
        line += 1
        # 第二行信息为该学生选了几门课 同时也代表了我们还要向下读几行才能全部读完该为学生数据
        # 转为int型 存储在变量l2中
        l2 = int(data[line].replace('\n',''))
        # 将学生的课程数量设置为l2
        s.set_number_courses(l2)
        # 转入下一行
        line += 1
        # 获取学生的课程列表，由于是刚刚初始化的该学生对象 所以l列表必定为空
        l = s.get_courses()
        # 循环往下读l2行 每一行都为该学生选择的课程id
        for i in range(l2):
            # 将该学生选择的课程Id 去掉换行符添加到l中
            l.append(data[line].replace('\n',''))
            line += 1
        # 一位学生的课程信息全部读入完毕 利用set函数设置该学生读入好的课程列表
        s.set_courses_list(l)
        # 一位学生的所有信息全部读入完毕 将其添加到学生列表中
        students_list.append(s)
    # 通过循环防止程序自动退出
    while True:
        # 打印主菜单
        print('''
    -------------------------------------------------------------------------------------------
    The choice to maintain COURSEs information [add|remove|update|search|show]
    The choice to maintain STUDENTs information [insert|delete|modify|retrieve|display]
    The choice quit means to finish the program.[quit]
    
    
        ''')
        # 读取用户输入的指令
        c = input('Please enter choice: ')
        # 判断用户输入的指令 对应操作相关的函数
        if c == 'add':
            add(courses_list)
        elif c == 'remove':
            remove(courses_list,students_list)
        elif c == 'update':
            update(courses_list)
        elif c == 'search':
            search(courses_list)
        elif c == 'show':
            show(courses_list)
        elif c == 'insert':
            insert(students_list)
        elif c == 'delete':
            delete(students_list)
        elif c == 'modify':
            modify(courses_list,students_list)
        elif c =='retrieve':
            retrieve(courses_list,students_list)
        elif c == 'display':
            display(courses_list,students_list)
        elif c == 'quit':
            # 若用户退出程序 则新建两个txt文件用来存储更新后的信息
            with open('new_courses.txt', 'w') as f:
                # 遍历课程列表 将每一项课程的所有信息添加到l字符串中
                for i in courses_list:
                    # 注意在description之前添加一个\n换行符
                    l = ','.join([i.get_course_name(),i.get_course_id(),i.get_credit(),i.get_instructor_name(),i.get_address()]) + '\n' + i.get_description() + '\n'
                    # 将字符串写入文件中
                    f.write(l)
            with open('new_students.txt', 'w') as f:
                # 遍历学生列表 将每一位学生的所有信息添加到字符串l中
                for i in students_list:
                    # 在课程数量之前添加一个换行符
                    l = ','.join([i.get_name(),i.get_id(),i.get_gender(),i.get_major()]) + '\n' + str(i.get_number_courses()) + '\n'
                    # 同时遍历学生的选课列表，依次将每个课程号添加到l之中，每一个都要加上换行符
                    for j in i.get_courses():
                        l += j + '\n'
                    # 将字符串写入文件中
                    f.write(l)
            # break退出循环 程序结束
            break
        # 若非法则提示错误信息
        else:
            print('Not a valid command-please try again.')


#-----------------------------
# Program 
#-----------------------------
main()
