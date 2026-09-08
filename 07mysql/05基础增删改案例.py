# 向user插入10000条数据
import pymysql
import random

names = ['a','b','c','d','e','f']
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

# 3 执行sql
for data_id in range(4, 10004):
    user = random.choice(names) + random.choice(names) + random.choice(names)
    password = '123456'
    sql = f"INSERT INTO user VALUES({data_id},'{user}','{password}')"
    cursor.execute(sql)

# 4 确认
conn.commit()

cursor.close()
conn.close()