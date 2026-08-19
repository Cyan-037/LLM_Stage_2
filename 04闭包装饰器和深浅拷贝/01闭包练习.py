'''
通过闭包实现对变量info字符串的保存
'''
def inv():
    info = '保存这个'
    def keep():
        print(info)
    return keep

f = inv()
f()
f()