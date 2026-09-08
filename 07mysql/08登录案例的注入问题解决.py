'''
sql = f"select * from user where user='{username}' and pwd={password}"
如果用户输入' or 1=1 or '则无论输入什么用户名都能登录成功，这就是注入问题

通过%占位符解决注入问题

sql = insert into table values(%s, %s, %s)
cursor.execute(sql, [值1, 值2, 值3])
'''

import pymysql

conn = pymysql.connect(
    host='192.168.88.100',
    port=3306,
    user='root',
    password='123456',
    database='jing_dong',
    charset='utf8'
)

cursor = conn.cursor()

username = input('请输入用户名：')
password = input('请输入密码：')

sql = "select * from user where user=%s and pwd=%s"
cursor.execute(sql,[username, password])

all_result = cursor.fetchall()
print(all_result)
if len(all_result) > 0:
    print('认证通过')
else:
    print('认证失败')

cursor.close()
conn.close()