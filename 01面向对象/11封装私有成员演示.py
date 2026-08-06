
class Salary(object):

    def __init__(self, name, work_id):
        self.name = name
        self.work_id = work_id

        self.__salary = 0

    def work_one_day(self):
        print('工作一天了')
        self.__salary += 1000



    def get_salary(self):
        return self.__salary

worker = Salary('猫猫','001')

worker.work_one_day()
worker.work_one_day()
worker.work_one_day()
print(f'目前薪水:{worker.get_salary()}')