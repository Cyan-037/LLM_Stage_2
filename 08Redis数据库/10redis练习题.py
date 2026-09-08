import redis

r = redis.Redis(
    host='192.168.88.100',      # redis 服务器地址
    port=6379,                  # redis 服务器端口
    db=0,                       # 数据库编号，默认0
    password=None,              # 密码，如果没有设置密码则为None
    decode_responses=True       # 自动解码，返回字符串而不是字节
)

# 1.在redis中存入2个列表
try:
    r.lpop('lst1',r.llen('lst1'))
    r.lpop('lst2', r.llen('lst2'))

except Exception as e:
    print(f'没有lst1')


r.rpush('lst1', 1,2,3,4,5)
r.lpush('lst2', 'a','b','c','d','e')
e1 = r.lrange('lst1', 0, -1)
e2 = r.lrange('lst2', 0, -1)
print(e1)
print(e2)

# 2. 在redis中存入2个集合
r.sadd('set1', 1,1,2,3,4,5,5,6)
r.sadd('set2', 'a','b','c','d','e','e')
print(r.smembers('set1'))
print(r.smembers('set2'))













r.close()