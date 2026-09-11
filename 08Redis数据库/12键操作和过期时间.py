'''
针对每个key都可以设置TTL（剩余生存时间）
因为redis需要内存，内存金贵，设置过期时间后过一段时间会自动清除
r.expire()
'''

import redis

r = redis.Redis(host='192.168.88.100', port=6379, db=0, password=None, decode_responses=True)

# 检查k是否存在
print('hobby存在？：', r.exists('hobby'))
print('hobby222存在？：', r.exists('hobby222'))

# TTL(Time to live 剩余生存时间设置)
# hobby 5秒后删除
r.expire('hobby', 5)
r.expire('num', 300)

# r.expire('num', 300)
num_ttl = r.ttl('num')
print('key num ttl: ', num_ttl)

# 取消TTL persist（持久化）
r.persist('num')
# TTL为-1 表示永久
print('key num ttl: ', r.ttl('num'))

# 查看redis全部key
keys = r.keys('*')
print(keys)

# 查看全部user开头的key
user_keys = r.keys('user*') # 等同于linux * 通配符写法
print(user_keys)

r.close()