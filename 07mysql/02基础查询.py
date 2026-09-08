# 1. 导入模块
import pymysql

# 2. 创建连接类的类对象
conn = pymysql.connect(
    host='192.168.88.100',      # 指定mysql服务器的ip
    port=3306,                  # 默认在3306端口
    user='root',                # 指定用户名
    password='123456',          # 指定密码
    charset='utf8',             # 指定编码集
    database='jing_dong'        # 指定数据库
)

# 3. 创建游标

# 干活的是游标对象
# conn负责的是整个网络的链接通常
# 游标对象是干活的小弟
# conn是老大，包吃住网络，游标cursor是小弟，干活
cursor = conn.cursor()

# 4.执行sql查询，execute执行
cursor.execute("SELECT * from goods")

# 4.1 小弟执行完sql后，结果小弟cursor保存了，可以取出
# fetchone()抓取一行结果，格式是元组，(列，列，列)
r = cursor.fetchone()

print(r)
# 4.2 抓取全部
r = cursor.fetchall()
# 返回结果，元组套元组（（列,列）,(列，列)）
print(r)

# 5.关闭游标
cursor.close()

# 6.关闭连接
conn.close()