class Student(object):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        pass

    def __str__(self):
        return f'姓名：{self.name},' \
               f'性别：{self.gender},' \
               f'年龄：{self.age}'

