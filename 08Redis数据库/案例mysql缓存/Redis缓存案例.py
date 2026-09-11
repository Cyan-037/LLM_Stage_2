import redis
import pymysql

class MySQLService:

    def __init__(self,
                 host='192.168.88.100',
                 port=3306,
                 user='root',
                 pswd='123456',
                 db='my_db',
                 charset='utf8'
                 ):
        # 创建连接
        self.connect = pymysql.Connection(
            host=host,
            port=port,
            user=user,
            password=pswd,
            database=db,
            charset=charset
        )
        # 创建游标对象
        self.cursor = self.connect.cursor()

    def __del__(self):
        # 自动关闭连接
        self.cursor.close()
        self.connect.close()

    def get_user_info(self, username):
        # fetchall((),())
        sql = "select * from userinfo where name=%s"
        self.cursor.execute(sql, [username])

        # 获取结果
        return self.cursor.fetchall()

class RedisService:

    def __init__(self, ms: MySQLService,
                 host='192.168.88.100',
                 port=6379,
                 pswd=None,
                 db=0
                 ):
        self.redis_conn = redis.Redis(
            host=host,
            port=port,
            password=pswd,
            db=db,
            decode_responses=True
        )
        self.ms: MySQLService = ms

    def __del__(self):
        self.redis_conn.close()

    def __ttl_reset(self, key, ttl_time=300):
        # 重设TTL为5分钟
        # 只在内部被使用，不需要在外部使用，可以__保护一下
        self.redis_conn.expire(key,ttl_time)

    def __save_user_info(self, username, infos):
        # 周杰伦: --> ((),())
        # redis: key:周杰伦，value，list[(),(),()]
        for info in infos:
            self.redis_conn.rpush(username,','.join(str(col) for col in info))
        # 设置过期时间
        self.__ttl_reset(username)

    def get_user_info(self, username):
        # redis内有没有
        if self.redis_conn.exists(username):
            # 找到缓存
            print(f'查询{username},缓存命中，重设TTL')
            # 重设ttl
            self.__ttl_reset(username)

            return self.redis_conn.lrange(username, 0, -1)

        print(f'查询{username},缓存未命中，跳转MySQL查询')

        infos = self.ms.get_user_info(username)
        if infos:   # 空元组是false，非空是True
            print(f'查询{username}, 缓存未命中，从Mysql中查询得到信息，共检索到{len(infos)}条信息')
            self.__save_user_info(username, infos)
        else:
            print(f'查询{username},缓存未命中，MySQL也没查到，没有此用户')
        return infos


if __name__ == '__main__':
    ms = MySQLService()
    rs = RedisService(ms)

    while True:
        username = input('输入要查询的姓名，要退出输入exit: ')
        if username == 'exit':
            break

        infos = rs.get_user_info(username)
        print(infos)

