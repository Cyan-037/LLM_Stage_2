'''
redis结构是k+v
k 字符串
v 是各类类型，这里演示的是字符串
set 存入 set(k,v)

'''

import redis

conn = redis.Redis(
    host='192.168.88.100',      # redis 服务器地址
    port=6379,                  # redis 服务器端口
    db=0,                       # 数据库编号，默认0
    password=None,              # 密码，如果没有设置密码则为None
    decode_responses=True       # 自动解码，返回字符串而不是字节
)

conn.set('name', '周杰伦')
conn.set('age', '23')

name = conn.get('name')
age = conn.get('age')

age123 = conn.get('age123') # 不存在结果为none
print(f"取出name:{name}, age: {age}, {age123}")

print('---------------------------------------')

# mset multiset 批量设置
conn.mset({'hobby':'唱跳rap', 'money':'2837398', 'gender':'男'})
values = conn.mget(['hobby', 'money', 'gender'])
print(f'批量取出:{values}')

conn.close()
