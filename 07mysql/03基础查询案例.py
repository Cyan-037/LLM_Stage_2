# 查询商品名称，品牌，价格，要求是大于5000的价格
# 输出格式是：每一个商品输出为：商品名称：xxx，商品价格：xxx

# 1导包
import pymysql
import os

r = os.getenv('mysqlpassword')


# 2连接
conn = pymysql.connect(
    host='192.168.88.100',
    port=3306,
    database='jing_dong',
    user='root',
    password='123456',
    charset='utf8'
)

# 3创建游标
cursor = conn.cursor()

# 4游标干活
order = "select name 商品名称, brand_name 品牌, price 价格 from goods where price > 5000"
cursor.execute(order)

# 抓取回应
ans = cursor.fetchall()
for one in ans:
    print(f'商品名称: {one[0]}\t商品品牌: {one[1]}\t商品价格: {one[2]}')

# 游标关
cursor.close()

# 连接关
conn.close()