'''
背景：
客服系统导出的留言中，经常同时包含邮箱和工单编号。运营同学希望程序能从一段文本中自动提取这些关键信息，减少人工复制。
问题：
给定文本：
text = "用户 zhangsan@example.com 提交了工单 NO1001，备用邮箱 service_01@test.cn，关联工单 NO1002。"

请使用正则表达式完成：

提取所有邮箱地址。(4分)
提取所有工单编号，编号格式为 NO 后跟 4 位数字。(4分)
分别打印两个列表。(2分)
'''

import re

def get_info(text):
    em_p = r'\w+@\w+\.\w+'
    gd_p = r'NO\w{4}'
    em_list = re.findall(em_p,text)
    gd_list = re.findall(gd_p,text)
    if em_list:
        print(em_list)
    else:
        print('未提取到邮箱')
    if gd_list:
        print(gd_list)
    else:
        print('未提取到工单编号')

get_info("用户 zhangsan@example.com 提交了工单 NO1001，备用邮箱 service_01@test.cn，关联工单 NO1002。")


