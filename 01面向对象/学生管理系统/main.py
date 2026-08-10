from student import Student
from student_ms import StudentMS

# 创建管理系统类对象
sms = StudentMS()

while True:
    user_input = sms.print_info()

    if user_input == '0':
        print('用户输入0，退出程序')
        break

    if user_input == '1':
        sms.add()
    elif user_input == '2':
        sms.modify()
    elif user_input == '3':
        sms.delete()
    elif user_input == '4':
        sms.query()
    elif user_input == '5':
        sms.show()
    elif user_input == '6':
        sms.save()
    else:
        print('输入不合规')

    print()



print('欢迎下次光临，再见')