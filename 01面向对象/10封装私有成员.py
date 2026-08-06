'''
面向对象编程，是许多编程语言都支持的一种编程思想

简单理解：基于模版（类）去创建实体（对象），使用对象完成 功能开发

面向对象三大主要特性：封装，继承，多态
> 封装:
    > 将现实世界事物的属性和方法，封装到类中，描述为成员变量，成员方法
    > 对用户隐藏的属性和行为，但不代表这些属性和行为都是开放给用户使用的
        > 私有成员：私有成员变量：变量名以__开头; 私有成员方法：方法名以__开头
> 继承
> 多态

'''

# 私有成员方法
class Phone:
    producer = 'apple'

    __running_voltage = 1.12   # 运行电压

    def __init__(self,name):
        self.name = name
        self.__current_voltage = 1.15  # 当前电压

    def __cpu_boost(self):
        self.__current_voltage = 1.5
        print('CPU超频')

    def power_mode(self, mode):
        if mode == 'high':
            self.__cpu_boost()
        else:
            print('默认模式')

    def camera(self):
        print('拍照了')

    def call(self):
        print('通话了')

phone = Phone('猫猫的phone')
print(phone.name)
phone.camera()
phone.call()

# 无法直接调用
# print(phone.__current_voltage)
# phone.__cpu_boost()

# 只能在厂家给的框框里选择
phone.power_mode('high')