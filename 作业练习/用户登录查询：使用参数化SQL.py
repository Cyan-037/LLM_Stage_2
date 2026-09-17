'''
背景：
小王正在开发一个简单的登录功能。用户会输入用户名和密码，程序需要到数据库中查询是否存在对应用户。为了避免 SQL 注入，不能直接拼接用户输入。
问题：
请写出使用 PyMySQL 参数化查询的核心代码，根据 username 和 password 查询用户。
'''
import pymysql

conn = pymysql.connect(host='192.168.88.100', port=3306, user='root', password='123456', charset='utf8', database='jing_dong')

cursor = conn.cursor()

username = input('请输入用户名：')
password = input('请输入密码：')

cursor.execute(f"select * from user where user='{username}' and pwd='{password}';")
result = cursor.fetchall()

if result:
    print('登录成功！')
    print(f'查询到{len(result)}个用户')
else:
    print('无法登录')

cursor.close()
conn.close()