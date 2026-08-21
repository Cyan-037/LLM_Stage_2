def process(lst):
    lst.append(100)


lst1 = [1, 2, 3]
process(lst1)   # 等于等号赋值,不需要返回值再等于，因为外面的也直接改了
print(lst1)

# 如果不想函数对列表的修改影响到原来的函数，那就用深浅拷贝
process(lst1.copy())
print(lst1)