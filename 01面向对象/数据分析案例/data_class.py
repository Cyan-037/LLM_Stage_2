'''
数据封装类
'''

# 用类对象，存放数据
class DataClass:
    def __init__(self, date, order_id, sale_amount, province):
        self.date = date
        self.order_id = order_id
        self.sale_amount = sale_amount
        self.province = province

    # 直接打印容器要用__str__
    def __str__(self):
        return f'日期：{self.date}, 订单ID：{self.order_id}, 销售额：{self.sale_amount}, 省份：{self.province}\n'
    # 如果对象在容器内要输出要用__repr__
    def __repr__(self):
        return f'日期：{self.date}, 订单ID：{self.order_id}, 销售额：{self.sale_amount}, 省份：{self.province}\n'