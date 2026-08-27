'''
电脑内存不可能100%比要读取的文件大
为了小内存读取大文件，可以用生成器的方式，一条条对外吐内容
'''


def file_line_gen(path):
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            # for line in f 相当于一次次调用f.readline()
            # 每次只占用1行数据的内层
            yield line.strip()

for line in file_line_gen('data.txt'):
    print(line)