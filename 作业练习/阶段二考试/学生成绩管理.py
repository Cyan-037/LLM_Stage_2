'''
背景：
某学校的班主任希望开发一个简单的学生成绩管理工具，用于保存学生的多科成绩，并快速查看学生平均分和指定科目成绩。为了方便后续扩展更多学生功能，要求使用类进行封装。
题目：
定义一个 Student 类，构造方法接收 name 和 scores 两个参数。
参数说明： (2分)
1.name：学生姓名，字符串类型
2.scores：学生成绩，字典类型，例如 {"数学": 85, "英语": 78}
要求实现以下方法：
1.get_average()：返回该学生所有科目的平均分，保留 2 位小数。(3分)
2.get_score(subject)：根据学科名称返回对应成绩，如果学科不存在，返回 None。(3分)
3.show_info()：打印学生姓名、所有成绩和平均分。(2分)
4.在 if __name__ == "__main__": 块中，创建学生对象：Student("Bob", {"数学": 85, "英语": 78, "Python": 92})并调用 show_info() 方法。(2分)
'''
class Student:
    def __init__(self, name: str, scores: dict[str: float]):
        self.name: str = name
        self.scores: dict[str: float] = scores

    def get_average(self):
        all_score = 0
        for score in self.scores.values():
            all_score += score
        avg = round(all_score / len(self.scores), 2)
        return avg

    def get_score(self, subject):
        if subject in self.scores.key():
            return self.scores[subject]
        else:
            return None

    def show_info(self):
        print('学生姓名：', self.name)
        print('所有成绩:')
        for key,value in self.scores.items():
            print(f'{key}: {value}',end=' ')
        print()
        avg = self.get_average()
        print('平均分：', avg)

if __name__ == '__main__':
    a = Student("Bob", {"数学": 85, "英语": 78, "Python": 92})
    a.show_info()

