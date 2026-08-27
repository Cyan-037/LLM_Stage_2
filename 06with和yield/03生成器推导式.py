'''
生成器语法：
    列表语法把[]改成()
    调用next(生成器对象)临时产生对象
生成器作用：
    用于节省内存
'''

lst1 = [i for i in range(1,10001)]
print(lst1) # lst1存法全部10000个元素


generator = (i for i in range(1, 10001)) # lst2是一个生成器对象，记录生成数据的规则
print(generator)
print(next(generator))   # 使用next(生成器),按生成规则，临时产生一条数据给你
print(next(generator))


for num in generator:
    print(num, end=' ')

# 规则耗尽就无法得到下一个了
# print(next(generator))

print()
while True:
    try:
        print(next(generator))
    except StopIteration:
        print('生成器用完了')
        break