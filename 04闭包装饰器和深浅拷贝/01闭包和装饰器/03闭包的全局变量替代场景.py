'''
可以保护计数器的安全
'''

count1 = 0

def work1():
    global count1
    count1 += 1
    print(f'我爱工作，工作使我快乐！请记件:{count1}')


def work2():
    count = 0

    def add_count():
        nonlocal count
        count += 1
        print(f'count2:{count}')
    return add_count

def work(f):
    f()

f = work2()
f()
f()

work(work1)
work(work1)
work(f)
work(f)

# print(f.__closure__[0].cell_contents)