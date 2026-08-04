
class FileReadService(object):

    def __init__(self,file_path,encoding='utf-8'):
        self.f = open(file_path, 'r', encoding=encoding)

    def read_line(self):
        print(self.f.read())

    def __del__(self):
        print('即将被销毁，关闭文件')
        self.f.close()

f1 = FileReadService('data.txt')
f1.read_line()

