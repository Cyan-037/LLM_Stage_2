


def add(x,y):
    print(f'x+y={x+y}')

def info(name,age):
    print(f'名字：{name},年龄:{age}')

a = (2,3)
b = {'name':'张三','age':14}

add(*a)
add(a[0],a[1])

info(**b)   # 等价于下面，b里的key名字必须和info的形参名一一对应
info(name='张三',age=14)