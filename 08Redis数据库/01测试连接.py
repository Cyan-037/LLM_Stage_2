'''
redis能托管的数据低，但是性能高，基于内存记录数据，键值对形式存储
MySQL托管的数据极大，性能比Redis低，硬盘

AI中
MySQL用于全量记忆（对话历史记录）的存储
Redis用于当前会话，记忆的缓存
'''
import redis

conn = redis.Redis(
    host='192.168.88.100',      # redis 服务器地址
    port=6379,                  # redis 服务器端口
    db=0,                       # 数据库编号，默认0
    password=None,              # 密码，如果没有设置密码则为None
    decode_responses=True       # 自动解码，返回字符串而不是字节
)

# 测试连接
try:
    response = conn.ping()
    print('Redis 连接成功', response)
except redis.ConnectionError as e:
    print('Redis 连接失败', e)

conn.close()