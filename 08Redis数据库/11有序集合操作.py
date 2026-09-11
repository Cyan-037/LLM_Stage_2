import redis

r = redis.Redis(host='192.168.88.100', port=6379, db=0, password=None, decode_responses=True)

# zadd添加有序集合 --> mapping -> dict
# 被存的其实是'小曹','小花'等等，没有分数，是个集合，分数只是附带的
r.zadd('leaderboard', {
    "小曹": 2000,     # k -> v   信息->分数
    "小花": 5000,
    "小汪": 6000,
    "小崔": 1000,
})

# 升序
# 这个还是无序的
r.zrange('leaderboard', 0, -1)
# 这个根据分数升序
r.zrange('leaderboard', 0, -1, withscores=True)

# 降序
desc_names = r.zrevrange('leaderboard', 0, -1, withscores=True)
print(desc_names)

# 获取分数
print('小曹分数：', r.zscore('leaderboard', '小曹'))

# 增加分数
r.zincrby('leaderboard', 1000, '小曹')
print('小曹分数：', r.zscore('leaderboard', '小曹'))

# 得到排名从高到低，从0开始排名
print('小曹排名：', r.zrevrank('leaderboard','小曹'))

# 按分数范围获取
scores = r.zrangebyscore('leaderboard', 1000, 5000, withscores=True)
print(scores)
r.close()