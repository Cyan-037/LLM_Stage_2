'''
使用Union类型，可以定义联合类型注解
Union联合类型注解，在变量直接，函数（方法）形参和返回值注解中，均可使用

需要导包
from typing import Union
两种写法
标准写法：
    x: Union[int, float]
快捷写法：
    x: int | float
'''
from typing import Union

def add(x: Union[int, float],y: Union[int, float]) -> int | float:
    return x + y

