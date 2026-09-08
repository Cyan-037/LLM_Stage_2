import pymysql

conn = pymysql.connect(
    host='192.168.88.100',
    port=3306,
    user='root',
    password='123456',
    charset='utf8'
)

print(conn.get_server_info())

conn.close()