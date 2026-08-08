# 接口：设计规范，要求实现（生产实体）接口要对着规范做
# 接口：图纸 实现就是施工，施工要对着图纸来
'''
严格的图纸语法, 给父类加上后，子类如果没有按照图纸结构完整写完就会报错：
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def a(self):
        pass
'''
from io import TextIOWrapper
from abc import ABC, abstractmethod

class ABCFileService(ABC):
    '''
    不能真正干活,是抽象类,是图纸,结构
    '''
    @abstractmethod
    def read_oneline(self) -> str:
        pass

    @abstractmethod
    def write_oneline(self, context: str) -> bool:
        pass

    @abstractmethod
    def print_all(self) -> None:
        pass

    @abstractmethod
    def read_all(self) -> str:
        pass


class TextFileService(ABCFileService):
    def __init__(self, file_path):
        # 以文本模式（'r'、'w'、'a'，并指定了 encoding）调用 open() 时，返回的对象类型就是 TextIOWrapper。它是用来处理字符串（str）类型数据的文件对象。
        self.fr: TextIOWrapper = open(file_path, 'r', encoding='utf-8')
        self.fw: TextIOWrapper = open(file_path, 'a', encoding='utf-8')

    def read_oneline(self) -> str:
        return self.fr.readline()

    def write_oneline(self, context: str) -> bool:
        try:
            self.fw.write(context)
            self.fw.write('\n')
            return True
        except Exception:
            return False

    def print_all(self) -> None:
        # 这样子每次读指针都从开头开始，不会出现读完之后再读时指针停在最后，导致返回None
        self.fr.seek(0)
        print(self.fr.read())

    def read_all(self) -> str:
        self.fr.seek(0)
        return self.fr.read()

tfs = TextFileService('data.txt')
tfs.write_oneline('abcde')
tfs.write_oneline('啦啦啦')
print(tfs.read_all())
