'''
修改成功
conn.commit() 确认修改

修改失败
conn.rollback() 回滚已做修改

基础结构
try:
    数据库的操作
    cursor.execute()

    conn.commit()   # 没问题确认
except Exception:
    conn.rollback() # 有问题撤回
'''




