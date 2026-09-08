import redis

r = redis.Redis(
    host='192.168.88.100',
    port=6379,
    db=0,
    password='123456',
    decode_responses=True
)

# 存入集合（去重）set
r.sadd('set1', 'python', 'itheima', 'itcast', 'python')
# 获取全部
all_tags: set = r.smembers('set1')

print(all_tags)

# 判断元素是否有
is_member = r.sismember('set1', 'python')
print('是否有python结果：', is_member)    # 结果1为True 0为False

# 随机弹出元素（集合没下标）
tag = r.spop('set1')
print('弹出：', tag)

# 指定弹出（删除）元素
r.srem('set1', 'itheima')
print('删除后：', r.smembers('set1'))

r.sadd('seta', 'a', 'b', 'c')
r.sadd('setb', 'd', 'b', 'b')

# 交集 sinter -> set intersection
intersection = r.sinter('seta', 'setb')
print('交集：',intersection)

# 并集 sunion -> set union
union = r.sunion('seta', 'setb')
print('并集：',union)

# 差集 sdiff -> set difference , 谁在前面谁是主集，主集有的，另一个没有的就是返回值
difference = r.sdiff('seta', 'setb')
print(f'差集：', difference)

r.close()