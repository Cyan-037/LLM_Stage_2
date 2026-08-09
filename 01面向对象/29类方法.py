'''
几乎没用过，知道就好
类方法：基于类创建的全部对象共享的方法，方便于对类属性进行操作
(带有self的是成员方法)

类属性的私有限制不住

格式：
@classmethod
def A(cls):
    cls.? = ?
'''


class Phone:
    brand = '联想'

    @classmethod
    def set_new_brand(cls, new_brand):
        cls.brand = new_brand


# 修改类属性
Phone.set_new_brand('黑箱')
print(Phone.brand)
