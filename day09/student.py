'''
继承
'''

from day09.person import Person
class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s 的 %s 正在学习 %s' % (self._grade, self._name, course))

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %s 正在讲 %s' % (self._name, self._title, course))

def main():
    stu = Student('王大', 15, '初三')
    stu.study('数学')
    stu.play()
    t = Teacher('李四', 30, '老教授')
    t.teach('python')
    t.play()

if __name__ == '__main__':
    main()
