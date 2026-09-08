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

sql = f"select * from user where user='{username}' and pwd='{password}'"
cursor.execute(sql)

all_result = cursor.fetchall()

if len(all_result) > 0:
    print('认证通过')
else:
    print('认证失败')

cursor.close()
conn.close()