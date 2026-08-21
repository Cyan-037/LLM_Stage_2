'''
闭包语法；
1. 函数有嵌套（外层函数内写内层函数）
2. 内层函数使用外层函数的局部变量（形参，定义的）
3. 外层函数要返回内层函数本身
'''

# Global,函数内部修改全局变量
# nonlocal,嵌套函数，内层函数修改外层函数局部变量

def outer():
    num = 100   # 外层函数的局部变量

    def inner():
        nonlocal num    # 内层函数修改外层函数局部变量，需要nonlocal声明
        num += 1
        print(num)

    return inner

f1 = outer()
f2 = outer()

# f1,f2本身是：函数

f1()
f1()
f1()

f2()
f2()
f1()
# 效果: 函数中的num被保留，没有被销毁