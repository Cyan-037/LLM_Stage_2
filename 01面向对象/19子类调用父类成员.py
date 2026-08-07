'''
调用父类
'''
class OldProgrammer:
    def programming(self):
        print('古法编程，纯手搓，100%无AI添加')

class NewProgrammer(OldProgrammer):
    def programming(self, use_old_school=False):
        # 对父类方法的编写

        if use_old_school:
            # 方法一：父类名.方法(self) self自己填
            # OldProgrammer.programming(self)

            # (推荐) 方法二：super().方法,super()代表父类
            super().programming()
        else:
            print('纯AI编程，拒绝古法手搓')



np = NewProgrammer()
np.programming(True)
np.programming(False)
np.programming()