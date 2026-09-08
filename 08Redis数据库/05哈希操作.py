import redis

conn = redis.Redis(
    host='192.168.88.100',
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)
try:
    conn.ping()
    print('已连接redis')
except Exception as e:
    print('连接失败：', e)

'''
所谓hash，指的是一个键值对（k-v）

'''
# hset(k1, k2, v)
# redis记录的是k,v
# k是k1，v是(k2,v)键值对
conn.hset('user小刘','age','21')
conn.hset('user小刘', 'hobby', '玩游戏')
conn.hset('user小刘','height', '165')

# 取出
# conn.hget(k1,k2)
hobby = conn.hget('user小刘','hobby')
print(hobby)

print('---------------------------------------------')

# hash批量设置, conn.hset(k, mapping={k1:v1, k2:v2, k3:v3})
conn.hset(
    'user小张', mapping={
        'name': '张三',
        'age': "23",
        'hobby': '写代码'
    }
)

# 取出
# conn.hgetall(k1)取指定key
zhang = conn.hgetall('user小张')
print(zhang)

print('---------------------------------------------')

keys = conn.hkeys('user小张')
print('小张的keys', keys)

values = conn.hvals('user小张')
print('小张的values', values)

conn.close()


