'''
基础类型注解
只是一个注释，看起来方便，就算标错了也没影响

变量: 类型 = 值
'''
var_1: int = 10
var_2: float = 12.23
var_3: bool = True
var_4: str = 'dsf'

var_5: str = 10
print(var_5)
print(type(var_5))


# 2.类类型
class Student:
    pass

stu: Student = Student()

# 3.容器类型
my_list: list = [1, True, 'A']
my_tuple: tuple = (1, True)
my_set: set = {1, True}
my_dict: dict = {1: 2, 3: 3}

# 4.同元素类型容器注解
my_list2: list[int] = [1, 32, 3]
my_tuple2: tuple[str] = ("a", "b")
my_dict2: dict[str:int] = {'a': 3, 'b': 4}
my_set2: set[float] = {3.4, 2.1}

# 5.在注释中写类型描述
num1 = 10   #type:int # 这是标准写法
num2 = 10
num3 = 12.33    #type:float
