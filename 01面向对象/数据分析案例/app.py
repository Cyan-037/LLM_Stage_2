from file_reader import FileReader
from data_class import DataClass
from draw_bar_chart import draw_bar_chart_optimized


def read_all_data(csv_path, json_path) -> list[DataClass]:
    fr1 = FileReader(csv_path)
    fr2 = FileReader(json_path)

    list1 = fr1.read_csv()
    list2 = fr2.read_json()
    all_data_list = list1 + list2

    return all_data_list


# 得到每日的营销额
# list1: [2026-04-01, 2026-04-02, ...]
# list2: [1111, 2233, ...]
def data_process(data: list[DataClass]) -> tuple[list,list]:
    # 将同一日的销售额聚合
    data_dict = {}
    for dc in data:
        if dc.date in data_dict:
            # 日期在字典内，已经记录过值了，取出来+新值，放回去
            data_dict[dc.date] += dc.sale_amount
        else:
            data_dict[dc.date] = dc.sale_amount

    # data_dict 字典转列表
    data = [(k,v) for k,v in data_dict.items()]
    # 方便排序，按元组第一个元素进行排序
    data.sort()
    # 提取日期列表
    date_list = [t[0] for t in data]
    amount_list = [t[1] for t in data]

    return date_list, amount_list


if __name__ == '__main__':
    csv_path = r'D:\AI\bigModalCode\STAGE_2\销售数据\2026年4月销售数据.csv'
    json_path = r'D:\AI\bigModalCode\STAGE_2\销售数据\2026年5月销售数据.txt'
    data = read_all_data(csv_path, json_path)
    date_list, amount_list = data_process(data)

    # 生成优化后的图表
    chart = draw_bar_chart_optimized(date_list, amount_list)

    # 渲染为 HTML 文件（自动打开）
    chart.render("optimized_sales_bar_chart.html")
