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


conn.set('name', 'Cyan')
v = conn.get('name')
print(v)

conn.mset({'age':'24', 'gender':'女'})
value = conn.mget(['age','gender'])
print(value)
conn.close()
