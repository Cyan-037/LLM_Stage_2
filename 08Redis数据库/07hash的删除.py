import redis

r = redis.Redis(
    host='192.168.88.100',
    port=6379,
    db=0,
    password='123456',
    decode_responses=True
)

# r.hdel(k1,k2)
r.hset('user1001', mapping={'name':'翠花', 'age':'23', 'gender':'女'})
values = r.hvals('user1001')
r.hdel('user1001','age')


r.close()