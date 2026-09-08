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
    
conn.set('num', '0')

# incr -> increment
conn.incr('num')
print('自增+1后', conn.get('num'))

conn.incrby('num', 5)
print('增长+5', conn.get('num'))

# decr -> decrement
conn.decr('num')
print('自减-1后', conn.get('num'))

conn.decrby('num', 5)
print('自减-5后', conn.get('num'))

# 如果是复杂计算，就取出来自己算，算完存回去
# num = int(conn.get('num'))

conn.close()


