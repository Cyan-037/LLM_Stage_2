from data_class import DataClass
import json

class FileReader:
    def __init__(self, path, encoding='utf-8'):
        self.fr = open(path,'r',encoding=encoding)

    def read_csv(self) -> list[DataClass]:
        data_list = []
        # 把标头切一下
        for line in self.fr.readlines()[1:]:
            # 剔除换行空格
            line = line.strip()
            # 分割为列表，以,为标志分割
            arr = line.split(',')

            dc = DataClass(arr[0], arr[1], float(arr[2]), arr[3])
            data_list.append(dc)

        return data_list

    def read_json(self) -> list[DataClass]:
        '''
        json长什么样
            {"日期":"2026-05-29","订单ID":"ORD5713902","销售额":2410,"省份":"安徽"}
            json就是字典的字符串形式
        如何把json字符串转为字典？
            json.loads(字符串)
        '''
        data_list = []
        for line in self.fr.readlines():
            line = line.strip()
            #字符串转字典
            data_dict = json.loads(line)

            dc = DataClass(data_dict['日期'], data_dict['订单ID'], data_dict['销售额'], data_dict['省份'])
            data_list.append(dc)

        return data_list