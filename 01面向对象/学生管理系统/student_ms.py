from student import Student


class StudentMS:

    def __init__(self):
        # 建立{学生姓名: Student}结构的字典
        self.stu_dict = {}

        self.fr = open('stu.txt', 'r', encoding='utf-8')
        all_stu_line = self.fr.readlines()
        for line in all_stu_line:
            line = line.strip()

            stu = Student.generate(line)
            self.stu_dict[stu.name] = stu

        print(f'学生管理系统已经加载完成，从文件中读取{len(all_stu_line)}条学生记录')
        self.fw = None

    def add(self):
        print('准备添加学生，请依次填入学生信息：')
        name = input('请输入学生姓名:')

        if name in self.stu_dict:
            print(f'学生{name}已存在，如果添加则会覆盖信息，是否继续')
            is_continue = input('继续请输入y,否则输入其他内容')
            if is_continue != 'y':
                return None

        gender = input('请输入学生性别:')
        tel = input('请输入学生电话:')
        age = input('请输入学生年龄:')
        info = input('请输入学生其他信息:')

        stu = Student(name, gender, tel, age, info)

        # 将学生添加到字典
        self.stu_dict[name] = stu

        print(f'学生{name}信息添加完毕')

    def modify(self):
        name = input('修改学生信息，请输入要修改信息的学生姓名：')
        # 判断学生是否在记录中
        if name not in self.stu_dict:
            print('此学生不在系统中，请重试')
            return None

        gender = input('请输入学生性别：')
        tel = input('请输入学生电话：')
        age = int(input('请输入学生年龄：'))
        info = input('请输入学生其他信息：')

        stu = Student(name, gender, tel, age, info)

        # 将学生添加到字典
        self.stu_dict[name] = stu

        print(f'学生{name}信息修改完毕')

    def delete(self):
        # 要求输入学生姓名
        name = input('删除学生信息，请输入要删除信息的学生姓名：')
        # 判断，学生存在删除，不存在提示不存在
        if name in self.stu_dict:
            del self.stu_dict[name]
            print(f'学生{name}删除完成')
        else:
            print(f'学生{name}不在系统中，无需删除')

    def query(self):
        # 要求输入学生姓名
        name = input('查询学生信息，请输入要查询的学生姓名：')
        # 学生存在，输出学生信息
        if name in self.stu_dict:
            stu = self.stu_dict[name]
            print(f'姓名:{stu.name} 性别：{stu.gender} 电话：{stu.tel} 年龄：{stu.age} 其他信息：{stu.info}')
        # 不存在则提示不存在
        else:
            print(f'学生{name}不存在系统中')

    def show(self):
        print('姓名\t性别\t电话\t\t\t年龄\t其他信息')
        for _, stu in self.stu_dict.items():
            print(f'{stu.name}\t{stu.gender}\t{stu.tel}\t{stu.age}\t{stu.info}')

    def save(self):
        with open('stu.txt','w',encoding='utf-8') as self.fw:
            for name, stu in self.stu_dict.items():
                self.fw.write(str(stu))
                self.fw.write('\n')
        print(f'保存完成，本次保存{len(self.stu_dict)}条学生信息')

    @staticmethod
    def print_info():
        print('=====黑马程序员学生管理系统V2.0=====')
        print('=====请输入你的选择序号=====')
        print('=====1.新增学生')
        print('=====2.修改学生')
        print('=====3.删除学生')
        print('=====4.查询学生')
        print('=====5.显示全部')
        print('=====6.保存信息')
        print('=====0.退出系统')
        print('==========')
        return input('请输入你的选择序号：')