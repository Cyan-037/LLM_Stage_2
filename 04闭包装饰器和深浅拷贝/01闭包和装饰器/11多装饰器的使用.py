
def login_check(fn):
    def inner():
        print('登录验证通过')
        fn()
    return inner

def code_check(fn):
    def inner():
        print('验证码验证通过')
    return inner

'''
可以有多个装饰器
装饰顺序从上到下
login_check(code_check(comment))
如果涉及到返回值，返回的是第一个装饰器
'''
@login_check
@code_check
def comment():
    print('这家餐馆好吃')

comment()