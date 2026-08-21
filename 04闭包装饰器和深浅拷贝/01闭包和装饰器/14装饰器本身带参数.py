'''
装饰器带有参数效果，需要三层嵌套

最外层接收@outer('+')
中间接收原函数
里面的是新函数
'''

def outer(operator):
    def middle(fn):

        def inner(*args,**kwargs):
            if operator == "+":
                print(f'正在做加法运算')
            if operator == "-":
                print(f'正在做减法运算')
            r = fn(*args,**kwargs)
            return r
        return inner
    return middle

@outer('+')
def add(a, b):
    print(f'a+b={a + b}')

@outer('-')
def sub(a, b):
    print(f'a-b={a - b}')

add(23,1)
sub(87,29)