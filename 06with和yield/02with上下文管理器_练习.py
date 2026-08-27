'''
实现1个类，内容随意，要求支持对象使用with
要求：with语句开始执行，自动输出开始
with语句结束，自动输出结束
with语句内部代码随意，比如print一些东西
'''
class A:

    def __enter__(self):
        print('输出开始')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('输出结束')

    def test(self):
        for _ in range(4):
            print('我在打字')

with A() as a:
    a.test()