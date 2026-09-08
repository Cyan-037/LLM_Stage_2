import pymysql

# 1 连接TCP
conn = pymysql.connect(
    host='192.168.88.100',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    database='jing_dong'
)

# 2 游标
cursor = conn.cursor()

# 3 干活
order = 'insert into user values (2, "王大锤", "123")'
num_line = cursor.execute(order)
print(num_line)     # 打印收到影响的行的行号

# 4 确认修改，只有老大conn有权确认，小弟cursor没法确认
conn.commit()   # 确认

# 5 关闭
cursor.close()
conn.close()


