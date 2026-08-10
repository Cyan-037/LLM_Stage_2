
class Student:

    def __init__(self, name, gender, tel, age, info):
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.info = info

    def __str__(self):
        '''
        方便讲学生对象，转换诶字符串，写入文件
        :return: 转换后的字符串
        '''
        # return ','.join([self.name, self.gender, str(self.tel), str(self.age), self.info])
        return f'{self.name},{self.gender},{self.tel},{self.age},{self.info}'

    @staticmethod
    def generate(stu_str: str):
        '''
        传入一行学生信息，以逗号分隔姓名，性别，电话，年龄，信息
        :param stu_str:
        :return:
        '''
        arr = stu_str.split(',')
        return Student(arr[0],arr[1],arr[2],arr[3],arr[4])