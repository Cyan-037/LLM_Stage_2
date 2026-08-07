'''
子类继承父类成员属性或方法时，若不满意，可以重新定义
即子类定义自己的子类成员或方法
'''
class OldProgrammer:
    def programming(self):
        print('古法编程，纯手搓，100%无AI添加')

class NewProgrammer(OldProgrammer):
    def programming(self):  # 对父类方法的编写
        print('纯AI编程，拒绝古法手搓')

np = NewProgrammer()
np.programming()