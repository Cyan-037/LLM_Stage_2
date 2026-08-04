'''
常用于文件

'''

class FileWriteService:

    def __init__(self, file_path, encoding='UTF-8'):
        self.f = open(file_path, 'w', encoding=encoding)

    def write_line(self, content):
        self.f.write(content)
        self.f.write('\n')

    def __del__(self):
        # 关闭文件，保存重要资料，写入文件是在内存，要在关闭之前写入硬盘
        self.f.flush()
        self.f.close()

fws = FileWriteService('data.txt')
fws.write_line('你好')
fws.write_line('基米好')
fws.write_line('大家都好')