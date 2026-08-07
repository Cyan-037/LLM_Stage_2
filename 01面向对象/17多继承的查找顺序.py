class A:
    def run(self):
        print('A run')


class B:
    def run(self):
        print('B run')


class C:
    def run(self):
        print('C run')


class D(A, B, C):
    pass


# 同名方法，先从自身找，没有就从左到右找父类

t = D()
t.run()
