# 验证一个密码，长度最少八位，最少一个大写字母，最少一个小写字母，最少1个特殊符号
import re


def check_passwd():
    s = input('设置密码：')

    # 长度
    if len(s) < 8:
        print('长度不足')
        return False

    #
    p = r"[A-Z]"
    result = re.search(p, s)

    if not result:
        print('必须包含大写字母')
        return False

    # 小写
    p = r'[a-z]'
    result = re.search(p, s)

    if not result:
        print('必须包含大写字母')
        return False

    p = r"\W"
    result = re.search(p, s)

    if not result:
        print('必须包含特殊字符')
        return False

    print('密码设置OK')
    return True

check_passwd()