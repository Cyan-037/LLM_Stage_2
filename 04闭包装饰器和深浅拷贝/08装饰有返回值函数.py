
def print_info(fn):
    def inner(x,y):
        print('开始')
        ans = fn(x,y)
        print('结束')
        return ans
    return inner

@print_info
def add(x, y):
    return x + y

print(add(2,3))